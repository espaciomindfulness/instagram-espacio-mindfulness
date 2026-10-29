#!/usr/bin/env python3
"""¿Acepta nuestra API el parametro `collaborators`?

Un posteo colaborativo aparece en el feed de las dos cuentas y suma las
interacciones de ambas. Es la forma mas directa de que los 3.800 seguidores
de Espacio Mindfulness vean contenido firmado tambien por @chris.mind2.

Meta documenta `collaborators` (hasta 3 usuarios, separados por coma) sobre
graph.facebook.com. Nosotros publicamos por graph.instagram.com, que es otra
variante de la API, y ahi no esta documentado. En vez de suponer, se prueba:
se crea un contenedor con el parametro y se mira si lo acepta o lo rechaza.

No publica nada. El contenedor queda sin publicar y Meta lo descarta solo a
las 24 h, igual que en probar_reel.py.

El resultado se escribe en contenido/prueba_colaboracion.md y se commitea,
porque los logs de Actions piden permisos de admin para leerse.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
INFORME = RAIZ / "contenido" / "prueba_colaboracion.md"
GRAPH = "https://graph.instagram.com/v23.0"
IG_USER_ID = os.environ.get("IG_USER_ID", "").strip()
TOKEN = os.environ.get("IG_ACCESS_TOKEN", "").strip()
BASE_URL = os.environ.get("IG_BASE_URL", "").strip().rstrip("/")
COLABORADOR = os.environ.get("IG_COLABORADOR", "chris.mind2").strip()
ARG = timezone(timedelta(hours=-3))


def pedir(ruta: str, datos: dict) -> tuple[bool, str]:
    datos["access_token"] = TOKEN
    cuerpo = urllib.parse.urlencode(datos).encode()
    try:
        pedido = urllib.request.Request(f"{GRAPH}/{ruta}", data=cuerpo, method="POST")
        with urllib.request.urlopen(pedido, timeout=60) as r:
            return True, r.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        return False, f"HTTP {exc.code}: {exc.read().decode('utf-8', 'replace')}"
    except Exception as exc:  # noqa: BLE001 - cualquier fallo es informacion
        return False, str(exc)


def main() -> int:
    if not (IG_USER_ID and TOKEN and BASE_URL):
        print("Faltan IG_USER_ID, IG_ACCESS_TOKEN o IG_BASE_URL.")
        return 1

    # Cualquier imagen ya publicada sirve: lo que se prueba es el parametro,
    # no la imagen.
    imagen = f"{BASE_URL}/charla_27oct.jpg"
    ahora = datetime.now(ARG)
    lineas = [f"# ¿Acepta `collaborators` nuestra API?", "",
              f"Probado el {ahora:%d/%m/%Y %H:%M} contra `graph.instagram.com`.",
              f"Colaborador de prueba: `{COLABORADOR}`", ""]

    # 1) Control: el mismo contenedor SIN el parametro. Si este falla, el
    #    problema es otro y la prueba no diria nada.
    ok_base, resp_base = pedir(f"{IG_USER_ID}/media", {
        "image_url": imagen, "caption": "PRUEBA - no se publica"})
    lineas += [f"**Contenedor de control (sin el parametro):** "
               f"{'OK' if ok_base else 'FALLA'}", "",
               f"```\n{resp_base[:400]}\n```", ""]

    # 2) El mismo contenedor CON el parametro.
    ok_col, resp_col = pedir(f"{IG_USER_ID}/media", {
        "image_url": imagen, "caption": "PRUEBA - no se publica",
        "collaborators": COLABORADOR})
    lineas += [f"**Contenedor con `collaborators`:** "
               f"{'OK' if ok_col else 'FALLA'}", "",
               f"```\n{resp_col[:600]}\n```", ""]

    if ok_base and ok_col:
        veredicto = ("**SIRVE.** La API acepta `collaborators`. Se puede "
                     "automatizar el posteo colaborativo desde el calendario.")
    elif ok_base and not ok_col:
        veredicto = ("**NO SIRVE.** El contenedor sale bien sin el parametro "
                     "y se cae con el: esta variante de la API no lo soporta. "
                     "Los colaborativos hay que hacerlos a mano desde el celular.")
    else:
        veredicto = ("**No concluyente.** Fallo hasta el contenedor de "
                     "control, asi que el problema no es el parametro.")
    lineas += ["## Veredicto", "", veredicto, ""]

    INFORME.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    print("\n".join(lineas))
    destino = os.environ.get("GITHUB_STEP_SUMMARY")
    if destino:
        with open(destino, "a", encoding="utf-8") as f:
            f.write("\n".join(lineas) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
