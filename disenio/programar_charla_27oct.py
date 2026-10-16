#!/usr/bin/env python3
"""Anuncio de la charla abierta del 27/10 en @espaciomindfulness.

La placa la hizo Christian aparte; aca solo se programa. Va en un hueco libre
(18/10 19:00) para no desplazar nada de la tanda de octubre.

Ojo con no confundirla con post48-charla-gratuita del 23/10: esa es la charla
introductoria de MBSR para publico general. Esta es para colegas y es otra
cosa — misma palabra, audiencias distintas.

Sin precios: es gratuita, y eso si se dice.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
RUTA = RAIZ / "contenido" / "calendario.json"

CAPTION = (
 "Charla abierta y gratuita para psicólogos/as y profesionales de la salud "
 "mental.\n\n"
 "«Del diagnóstico al proceso: qué cambia cuando dejás de tratar trastornos»\n\n"
 "El paciente real casi nunca entra en una sola casilla del manual: viene con "
 "varias, y se alimentan entre sí. La psicoterapia basada en procesos cambia "
 "la pregunta — en vez de qué trastorno tiene, qué procesos sostienen su "
 "sufrimiento y cuáles se pueden activar para que esté mejor.\n\n"
 "En una hora recorremos ese giro y los tres procesos que atraviesan a las "
 "terapias con más evidencia: mindfulness, compasión y flexibilidad "
 "psicológica. Con ejemplos clínicos.\n\n"
 "📅 Martes 27 de octubre · 20:30 (Argentina)\n"
 "💻 Online por Zoom · 1 hora\n"
 "🎟️ Inscripción gratuita · cupos limitados\n\n"
 "El link de inscripción está en la bio.\n\n"
 "A cargo del Lic. Christian Arpa — Psicólogo (UBA), MBSR Teacher acreditado "
 "por Global Mindfulness Collaborative y especialista en ACT. Fundador y "
 "director de Espacio Mindfulness.\n\n"
 "#psicologia #act #mindfulness #psicoterapia #saludmental "
 "#formacionprofesional #psicologosargentina"
)


def main():
    d = json.load(open(RUTA, encoding="utf-8"))
    if any(p["id"] == "post53-charla-27oct" for p in d["posts"]):
        print("ya estaba programada")
        return
    if not (RAIZ / "contenido" / "publicar" / "charla_27oct.jpg").exists():
        print("! falta charla_27oct.jpg: corre antes preparar_imagenes.py")
        return
    d["posts"].append(dict(id="post53-charla-27oct", tipo="imagen",
                           estado="pendiente", fecha="2026-10-18", hora="19:00",
                           archivo="charla_27oct.jpg", caption=CAPTION))
    d["posts"].sort(key=lambda p: (p["fecha"], p["hora"]))
    open(RUTA, "w", encoding="utf-8").write(
        json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    print(f"programada | caption {len(CAPTION)} de 2200")


if __name__ == "__main__":
    main()
