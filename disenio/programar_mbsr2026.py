#!/usr/bin/env python3
"""Programa el carrusel del curriculum 2026 del MBSR.

Sale el mismo dia del encuentro, a las 19:00. Es noticia y la noticia se
enfria: vale mas publicarlo hoy entre dos posteos que esperar al hueco
prolijo de la semana que viene.

Va como COLABORATIVO con @chris.mind2: aparece en los dos feeds, firmado por
las dos cuentas, y suma las interacciones de ambas. Christian recibe una
invitacion en la app y el posteo entra en su grilla recien cuando la acepta.

Cuidados de este texto:
  - "mas de 700 participantes": el material registrado dice 713 y Christian
    recuerda 750. El redondeo es cierto con cualquiera de los dos.
  - No se enumeran los expositores: hubo mas de los cuatro registrados.
  - La credencial es del GMC, NUNCA de Brown.
  - Sin precios.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
RUTA = RAIZ / "contenido" / "calendario.json"

CAPTION = (
 "Hoy el MBSR presentó su currículum 2026. Estuve conectado.\n\n"
 "Brown University School of Professional Studies y el Global Mindfulness "
 "Collaborative presentaron la guía 2026 del programa, con Jon Kabat-Zinn "
 "—que lo creó en 1979— entre los expositores. Más de 700 personas de todo "
 "el mundo siguiendo la transmisión en vivo.\n\n"
 "Hay un dato que me quedó dando vueltas.\n\n"
 "En 1979 el MBSR no tenía currículum escrito. El primero, de 1993, tenía 12 "
 "páginas. El de 2017 tenía 65. El de 2026 tiene 232.\n\n"
 "No es que el programa haya cambiado en estos 47 años. Es que lo que antes "
 "se transmitía de maestro a alumno, hoy está escrito. Y esta edición es la "
 "primera elaborada con aportes de la comunidad internacional: más de 50 "
 "respondentes, más de 360 aportes y 25 autores y revisores.\n\n"
 "Te lo cuento porque explica algo del MBSR que no siempre se ve: es un "
 "programa que se cuida. Que se revisa. Que no se da por terminado.\n\n"
 "El MBSR que damos en Buenos Aires es este. El de la fuente.\n\n"
 "Y la edición 2026 es de acceso libre: cualquiera puede descargar el "
 "currículum completo y comparar con lo que le enseñan. Si querés el link, "
 "escribinos 🌿\n\n"
 "—\n"
 "Lic. Christian D. Arpa · Psicólogo (UBA) · MBSR Teacher calificado por el "
 "Global Mindfulness Collaborative\n"
 "Espacio Mindfulness — desde 2012\n\n"
 "#MBSR #Mindfulness #JonKabatZinn #AtenciónPlena #ReducciónDeEstrés "
 "#MindfulnessBuenosAires #SaludMental #Psicología #MindfulnessArgentina "
 "#EspacioMindfulness"
)


def main():
    d = json.load(open(RUTA, encoding="utf-8"))
    if any(p["id"] == "post66-mbsr-2026" for p in d["posts"]):
        print("ya estaba programado")
        return
    archivos = [f"post66_mbsr_{i}.jpg" for i in range(1, 6)]
    faltan = [a for a in archivos
              if not (RAIZ / "contenido" / "publicar" / a).exists()]
    if faltan:
        print(f"! faltan {faltan}: corre preparar_imagenes.py")
        return
    d["posts"].append(dict(
        id="post66-mbsr-2026", tipo="carrusel", estado="pendiente",
        fecha="2026-11-12", hora="19:00", archivos=archivos,
        colaboradores=["chris.mind2"], caption=CAPTION))
    d["posts"].sort(key=lambda p: (p["fecha"], p["hora"]))
    open(RUTA, "w", encoding="utf-8").write(
        json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    print(f"programado para hoy 19:00 | caption {len(CAPTION)} de 2200")
    print("colaborador: @chris.mind2 (tiene que aceptar la invitacion)")


if __name__ == "__main__":
    main()
