#!/usr/bin/env python3
"""Suma a EM dos recortes de la charla del Diplomado, como antesala del 29/10.

Son dos de los cinco reels que se cortaron de la charla; los otros tres quedan
exclusivos de @chris.mind2 para que las dos cuentas no publiquen lo mismo.

Van solo dos porque la audiencia de EM es mayormente publico general y esta
charla le habla a colegas. Puestos el 23 y el 27, arman una secuencia de tres
tiempos que desemboca en el carrusel del Diplomado del 29/10.

Horario 13:00: es el que ya usaban los reels de la radio, elegido para no
pisar los posteos de imagen de las 09:30 y las 19:00.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
RUTA = RAIZ / "contenido" / "calendario.json"

FIRMA = (
    "—\n"
    "Fragmento de una charla sobre psicoterapia basada en procesos.\n\n"
    "Lic. Christian D. Arpa · Psicólogo (UBA) · MBSR Teacher "
    "(Global Mindfulness Collaborative)\n"
    "Director del Diplomado en Psicoterapia Basada en Procesos\n"
    "Espacio Mindfulness — institución acreditada por GMC\n\n"
    "#psicologia #act #mindfulness #mbsr #psicoterapia #saludmental "
    "#formacionprofesional"
)

P = [
 ("2026-10-23", "13:00", "reel9-el-mapa", "09_el_mapa.mp4",
  "Si trabajás en salud mental, este es para vos.\n\n"
  "Llega un paciente con ansiedad, pero también con evitación y autocrítica. "
  "No entra en una sola casilla del manual. ¿Por dónde empezás?\n\n"
  "Un criterio simple: mirá qué proceso predomina.\n\n"
  "· Rumiación → empezá por la atención\n"
  "· Autocrítica → empezá por la compasión\n"
  "· Evitación → empezá por la flexibilidad psicológica\n\n"
  "Rara vez viene un proceso solo. Pero casi siempre hay uno que manda, y "
  "por ahí se empieza.\n\n"),

 ("2026-10-27", "13:00", "reel10-no-alcanza-un-video", "10_no_alcanza_un_video.mp4",
  "Un mapa lo entendés rápido. Dominarlo en la clínica es otra cosa.\n\n"
  "Leer en tiempo real lo que le pasa al paciente, elegir el proceso justo e "
  "integrarlo en la sesión sin que se vuelva una receta: eso no se aprende "
  "mirando un video.\n\n"
  "La teoría la podés estudiar sola, a tu ritmo, frente a una pantalla. La "
  "clínica se entrena en vivo: casos, role-playing, supervisión, alguien que "
  "te devuelve lo que hiciste bien y lo que conviene ajustar.\n\n"
  "Las dos cosas hacen falta.\n\n"
  "Pasado mañana contamos cómo es el Diplomado 2027 por dentro.\n\n"),
]


def main():
    d = json.load(open(RUTA, encoding="utf-8"))
    existentes = {p["id"] for p in d["posts"]}
    nuevos = 0
    for fecha, hora, pid, archivo, cuerpo in P:
        if pid in existentes:
            continue
        falta = not (RAIZ / "contenido" / "publicar" / archivo).exists()
        if falta:
            print(f"  ! falta el video {archivo}, no lo programo")
            continue
        d["posts"].append(dict(id=pid, tipo="reel", estado="pendiente",
                               fecha=fecha, hora=hora, archivo=archivo,
                               caption=cuerpo + FIRMA))
        nuevos += 1
    d["posts"].sort(key=lambda p: (p["fecha"], p["hora"]))
    open(RUTA, "w", encoding="utf-8").write(
        json.dumps(d, ensure_ascii=False, indent=2) + "\n")

    largo = max(len(p["caption"]) for p in d["posts"])
    print(f"{nuevos} reels nuevos | caption mas larga: {largo} de 2200\n")
    for p in sorted(d["posts"], key=lambda x: (x["fecha"], x["hora"])):
        if p["estado"] == "pendiente" and p["fecha"] >= "2026-10-21":
            print(f"  {p['fecha']} {p['hora']}  {p['tipo']:<9} {p['id']}")


if __name__ == "__main__":
    main()
