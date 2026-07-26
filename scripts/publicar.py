#!/usr/bin/env python3
"""
Publicador automatico de Instagram - Espacio Mindfulness.

Lee contenido/calendario.json, busca los posts cuya fecha/hora ya llego y
todavia estan en estado "pendiente", y los publica via la Instagram API con
Login de Instagram (host graph.instagram.com, sin pagina de Facebook).

No usa dependencias externas: solo la libreria estandar de Python 3.9+.

Variables de entorno:
  IG_USER_ID          (obligatoria) ID numerico de la cuenta de Instagram
  IG_ACCESS_TOKEN     (obligatoria) token de larga duracion (Instagram Login)
  IG_BASE_URL         (obligatoria) URL publica de la carpeta contenido/publicar
  IG_API_HOST         opcional, default graph.instagram.com
  IG_API_VERSION      opcional, default v23.0
  IG_DRY_RUN          "1" = simula todo sin publicar nada
  IG_GRACIA_HORAS     opcional, default 12. Si un post quedo mas atrasado que
                      esto (por ej. el workflow estuvo caido), no se publica
                      tarde: se marca "vencido" para que vos decidas.
  IG_MAX_POR_CORRIDA  opcional, default 1. Cuantos posts como maximo publicar
                      en una sola ejecucion.
"""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

RAIZ = Path(__file__).resolve().parent.parent
CALENDARIO = RAIZ / "contenido" / "calendario.json"

API_HOST = os.environ.get("IG_API_HOST", "graph.instagram.com")
API_VERSION = os.environ.get("IG_API_VERSION", "v23.0")
IG_USER_ID = os.environ.get("IG_USER_ID", "")
TOKEN = os.environ.get("IG_ACCESS_TOKEN", "")
BASE_URL = os.environ.get("IG_BASE_URL", "").rstrip("/")
DRY_RUN = os.environ.get("IG_DRY_RUN", "0") == "1"
GRACIA_HORAS = int(os.environ.get("IG_GRACIA_HORAS", "12"))
MAX_POR_CORRIDA = int(os.environ.get("IG_MAX_POR_CORRIDA", "1"))
MAX_INTENTOS = 3

TZ_DEFECTO = "America/Argentina/Buenos_Aires"


class ErrorAPI(Exception):
    """Meta devolvio un error."""


# --------------------------------------------------------------------------
# Capa HTTP
# --------------------------------------------------------------------------

def api(metodo: str, ruta: str, params: dict | None = None) -> dict:
    """Llama a la Graph API y devuelve el JSON de respuesta."""
    datos = dict(params or {})
    datos["access_token"] = TOKEN
    url = f"https://{API_HOST}/{API_VERSION}/{ruta.lstrip('/')}"

    if metodo == "GET":
        peticion = urllib.request.Request(f"{url}?{urllib.parse.urlencode(datos)}")
    else:
        cuerpo = urllib.parse.urlencode(datos).encode("utf-8")
        peticion = urllib.request.Request(url, data=cuerpo, method="POST")

    try:
        with urllib.request.urlopen(peticion, timeout=90) as respuesta:
            return json.loads(respuesta.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detalle = exc.read().decode("utf-8", "replace")
        raise ErrorAPI(f"HTTP {exc.code} en {ruta} -> {detalle}") from None
    except urllib.error.URLError as exc:
        raise ErrorAPI(f"No se pudo conectar con {API_HOST}: {exc.reason}") from None


def url_publica(archivo: str) -> str:
    """Convierte un nombre de archivo en su URL publica accesible por Meta."""
    return f"{BASE_URL}/{urllib.parse.quote(archivo)}"


# --------------------------------------------------------------------------
# Publicacion
# --------------------------------------------------------------------------

def crear_contenedor(params: dict) -> str:
    respuesta = api("POST", f"{IG_USER_ID}/media", params)
    return respuesta["id"]


def esperar_procesamiento(contenedor_id: str, max_segundos: int = 600) -> None:
    """Los videos tardan en procesarse del lado de Meta. Hay que esperar."""
    inicio = time.monotonic()
    while time.monotonic() - inicio < max_segundos:
        estado = api("GET", contenedor_id, {"fields": "status_code,status"})
        codigo = estado.get("status_code")
        if codigo == "FINISHED":
            return
        if codigo == "ERROR":
            raise ErrorAPI(f"Meta no pudo procesar el video: {estado.get('status')}")
        print(f"    procesando video... ({codigo})")
        time.sleep(15)
    raise ErrorAPI("Timeout: el video sigue procesandose despues de 10 minutos")


def publicar_contenedor(contenedor_id: str) -> str:
    respuesta = api("POST", f"{IG_USER_ID}/media_publish", {"creation_id": contenedor_id})
    return respuesta["id"]


def publicar_post(post: dict) -> str:
    """Publica un post segun su tipo. Devuelve el media_id de Instagram."""
    tipo = post.get("tipo", "imagen")
    caption = post.get("caption", "")

    if tipo == "imagen":
        contenedor = crear_contenedor({
            "image_url": url_publica(post["archivo"]),
            "caption": caption,
        })

    elif tipo == "carrusel":
        hijos = []
        for archivo in post["archivos"]:
            hijo = crear_contenedor({
                "image_url": url_publica(archivo),
                "is_carousel_item": "true",
            })
            hijos.append(hijo)
        contenedor = crear_contenedor({
            "media_type": "CAROUSEL",
            "children": ",".join(hijos),
            "caption": caption,
        })

    elif tipo == "reel":
        params = {
            "media_type": "REELS",
            "video_url": url_publica(post["archivo"]),
            "caption": caption,
            "share_to_feed": "true" if post.get("compartir_en_feed", True) else "false",
        }
        if post.get("portada"):
            params["cover_url"] = url_publica(post["portada"])
        contenedor = crear_contenedor(params)
        esperar_procesamiento(contenedor)

    else:
        raise ErrorAPI(f"Tipo de post desconocido: {tipo!r} (usa imagen, carrusel o reel)")

    return publicar_contenedor(contenedor)


# --------------------------------------------------------------------------
# Calendario
# --------------------------------------------------------------------------

def cargar_calendario() -> dict:
    if not CALENDARIO.exists():
        raise SystemExit(f"No encuentro el calendario en {CALENDARIO}")
    return json.loads(CALENDARIO.read_text(encoding="utf-8"))


def guardar_calendario(calendario: dict) -> None:
    CALENDARIO.write_text(
        json.dumps(calendario, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def momento_de(post: dict, tz: ZoneInfo) -> datetime:
    return datetime.fromisoformat(f"{post['fecha']}T{post['hora']}").replace(tzinfo=tz)


def resumen(lineas: list[str]) -> None:
    """Escribe el resumen en la pestania Summary de GitHub Actions."""
    destino = os.environ.get("GITHUB_STEP_SUMMARY")
    texto = "\n".join(lineas)
    print(texto)
    if destino:
        with open(destino, "a", encoding="utf-8") as archivo:
            archivo.write(texto + "\n")


def main() -> int:
    faltantes = [
        nombre for nombre, valor in (
            ("IG_USER_ID", IG_USER_ID),
            ("IG_ACCESS_TOKEN", TOKEN),
            ("IG_BASE_URL", BASE_URL),
        ) if not valor
    ]
    if faltantes and not DRY_RUN:
        raise SystemExit(
            "Faltan variables de entorno: " + ", ".join(faltantes) +
            "\nRevisa los Secrets del repositorio (ver SETUP.md)."
        )

    calendario = cargar_calendario()
    tz = ZoneInfo(calendario.get("zona_horaria", TZ_DEFECTO))
    ahora = datetime.now(tz)
    lineas = [f"### Corrida {ahora:%Y-%m-%d %H:%M} ({tz})"]
    cambio = False

    vencidos, listos = [], []
    for post in calendario["posts"]:
        if post.get("estado") != "pendiente":
            continue
        cuando = momento_de(post, tz)
        if cuando > ahora:
            continue
        if ahora - cuando > timedelta(hours=GRACIA_HORAS):
            vencidos.append((post, cuando))
        else:
            listos.append((cuando, post))

    for post, cuando in vencidos:
        post["estado"] = "vencido"
        post["nota"] = f"Se paso mas de {GRACIA_HORAS}h de {cuando:%Y-%m-%d %H:%M} sin publicarse."
        lineas.append(f"- VENCIDO `{post['id']}` (estaba para {cuando:%d/%m %H:%M})")
        cambio = True

    listos.sort(key=lambda par: par[0])
    a_publicar = listos[:MAX_POR_CORRIDA]

    if not a_publicar:
        lineas.append("- Nada para publicar en este momento.")
        proximos = sorted(
            (momento_de(p, tz), p) for p in calendario["posts"]
            if p.get("estado") == "pendiente"
        )
        if proximos:
            cuando, post = proximos[0]
            lineas.append(f"- Proximo: `{post['id']}` el {cuando:%d/%m/%Y a las %H:%M}")
        if cambio:
            guardar_calendario(calendario)
        resumen(lineas)
        return 0

    hubo_error = False
    for cuando, post in a_publicar:
        etiqueta = f"`{post['id']}` ({post.get('tipo', 'imagen')}, programado {cuando:%d/%m %H:%M})"
        if DRY_RUN:
            lineas.append(f"- SIMULACRO {etiqueta} -> {url_publica(post.get('archivo', '?'))}")
            continue
        try:
            print(f"Publicando {post['id']}...")
            media_id = publicar_post(post)
            post["estado"] = "publicado"
            post["publicado_en"] = ahora.isoformat(timespec="seconds")
            post["media_id"] = media_id
            post.pop("nota", None)
            lineas.append(f"- PUBLICADO {etiqueta} -> media_id `{media_id}`")
            cambio = True
        except (ErrorAPI, KeyError) as exc:
            intentos = post.get("intentos", 0) + 1
            post["intentos"] = intentos
            post["nota"] = str(exc)[:500]
            if intentos >= MAX_INTENTOS:
                post["estado"] = "error"
                lineas.append(f"- ERROR DEFINITIVO {etiqueta} tras {intentos} intentos: {exc}")
            else:
                lineas.append(f"- FALLO {etiqueta} (intento {intentos}/{MAX_INTENTOS}), reintenta luego: {exc}")
            hubo_error = True
            cambio = True

    if cambio:
        guardar_calendario(calendario)
    resumen(lineas)
    return 1 if hubo_error else 0


if __name__ == "__main__":
    sys.exit(main())
