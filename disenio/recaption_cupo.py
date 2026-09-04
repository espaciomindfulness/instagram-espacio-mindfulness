#!/usr/bin/env python3
"""Reescribe las captions de las publicaciones tocadas por el cupo lleno.

Va aparte de gen_correccion_cupo.py a proposito: las placas y el texto se
pueden corregir por separado, y asi se puede volver a correr uno sin el otro.
"""
import json
from pathlib import Path

RUTA = Path(__file__).resolve().parent.parent / "contenido" / "calendario.json"

HT = ("#Mindfulness #MBSR #MindfulnessArgentina #SaludMental #Ansiedad "
      "#ReduccionDeEstres #EspacioMindfulness")

HT_PRO = ("#Mindfulness #MBSR #MindfulnessArgentina #Psicologia #ACT "
          "#FormacionProfesional #SaludMental #EspacioMindfulness")

NUEVAS = {

 "post26-anuncio-octubre": (
  "Se llenó la presencial de octubre.\n\n"
  "La última cohorte presencial del año completó sus lugares antes de lo "
  "previsto. Gracias de verdad a cada persona que escribió 🌿\n\n"
  "No vamos a abrir vacantes extra: el grupo reducido no es un detalle de "
  "folleto, es parte de cómo funciona el programa. Con veinte personas el "
  "MBSR deja de ser MBSR.\n\n"
  "Si te quedaste afuera, tres caminos 👉 deslizá.\n\n"
  "Hay lista de espera por si se libera un lugar, la próxima cohorte online "
  "arranca a principios del año que viene, y la charla gratuita de 45 minutos "
  "sigue abierta este mes.\n\n"
  "Escribinos por WhatsApp y te ubicamos donde te sirva.", HT),

 "post33-cierre-septiembre": (
  "Instructorado en Mindfulness — Cohorte 2027.\n\n"
  "Trescientas horas, los sábados, para pasar de practicar a poder conducir "
  "grupos. Nueve módulos con formación en los tres programas — MBSR, MBCT y "
  "MSC — más mindfulness aplicado al ámbito organizacional.\n\n"
  "Una aclaración que hacemos siempre: en mindfulness no hay matrícula ni "
  "colegio que regule. Cualquiera puede llamarse instructor mañana. Por eso "
  "lo único que te protege como alumno es mirar quién certifica a quien te "
  "enseña.\n\n"
  "Espacio Mindfulness está acreditado por Global Mindfulness Collaborative y "
  "enseña desde 2012. Chequealo, y chequeá a cualquiera con quien vayas a "
  "formarte.\n\n"
  "La inscripción está abierta. Escribinos y te pasamos el temario completo 🌿",
  HT_PRO),

 "post43-anuncio-ultima-cohorte": (
  "Formarte para enseñar es otra cosa que practicar.\n\n"
  "El Instructorado en Mindfulness 2027 es para profesionales de la salud, la "
  "educación y el ámbito organizacional que ya tienen práctica personal y "
  "quieren conducir grupos 👉 deslizá.\n\n"
  "Trescientas horas, los sábados, nueve módulos a lo largo del año. Se "
  "recorren los tres programas — MBSR, MBCT y MSC — y se suma mindfulness "
  "aplicado a empresas, que es donde más demanda hay y menos gente formada.\n\n"
  "La cuarta placa es la que nos importa: en este rubro no hay matrícula. "
  "Antes de anotarte en cualquier formación, preguntá quién la certifica y "
  "fijate si esa institución existe fuera de su propia web.\n\n"
  "Nosotros estamos acreditados por Global Mindfulness Collaborative y "
  "enseñamos desde 2012.\n\n"
  "Escribinos por WhatsApp y te pasamos el temario y el calendario 🌿",
  HT_PRO),

 "post44-ultima-llamada": (
  "Mañana arranca la presencial, con el cupo completo.\n\n"
  "Fue la última cohorte presencial del año y se llenó. Gracias 🌿\n\n"
  "Si te quedaste afuera, no se termina acá:\n\n"
  "· Hay lista de espera, por si se libera un lugar.\n"
  "· La próxima cohorte online arranca a principios del año que viene.\n"
  "· La charla gratuita de 45 minutos sigue abierta todo el mes.\n\n"
  "Y si lo tuyo es formarte para enseñar, el Instructorado y el Diplomado 2027 "
  "ya tienen la inscripción abierta.\n\n"
  "Escribinos por WhatsApp y vemos cuál te sirve.", HT),

 "post51-diplomado-2027": (
  "Diplomado en Psicoterapia Basada en Procesos — Cohorte 2027.\n\n"
  "Para psicólogos y profesionales de la salud mental que ya atienden y "
  "quieren incorporar mindfulness y ACT a su práctica con método, no de "
  "oído 👉 deslizá.\n\n"
  "Nueve encuentros de cuatro horas, un martes por mes, en vivo por Zoom, de "
  "abril a diciembre. Más un cierre presencial en Buenos Aires con práctica "
  "intensiva y graduación. Doscientas horas en total, diecisiete módulos en "
  "cinco bloques.\n\n"
  "En vivo, dicho en serio: no es una plataforma con clases grabadas y una "
  "reunión mensual. Se cursa con el grupo y con supervisión.\n\n"
  "Y lo que más nos importa: lo dicta gente que atiende. No es teoría de "
  "manual, es lo que el equipo hace todos los días en el consultorio.\n\n"
  "Arranca el martes 13 de abril. Escribinos y te pasamos el temario "
  "completo 🌿", HT_PRO),
}

# Retoques chicos: el 45 sigue siendo valido, pero conviene que diga que
# arranco lleno — es prueba social gratis.
PARCHES = {
 "post45-ocho-semanas-por-dentro": [
   ("Ayer arrancó la última cohorte presencial del año, así que aprovechamos "
    "para contarte el recorrido completo por dentro",
    "Ayer arrancó la última cohorte presencial del año — con el cupo completo — "
    "así que aprovechamos para contarte el recorrido completo por dentro"),
 ],
}


def main():
    d = json.load(open(RUTA, encoding="utf-8"))
    tocados = 0
    for p in d["posts"]:
        if p["id"] in NUEVAS:
            if p["estado"] != "pendiente":
                print(f"  ! {p['id']} ya esta {p['estado']}, no lo toco")
                continue
            cuerpo, ht = NUEVAS[p["id"]]
            p["caption"] = cuerpo + "\n\n" + ht
            tocados += 1
            print(f"  ~ {p['fecha']} {p['id']}")
        for viejo, nuevo in PARCHES.get(p["id"], []):
            if viejo in p.get("caption", ""):
                p["caption"] = p["caption"].replace(viejo, nuevo)
                tocados += 1
                print(f"  ~ {p['fecha']} {p['id']} (parche)")

    open(RUTA, "w", encoding="utf-8").write(
        json.dumps(d, ensure_ascii=False, indent=2) + "\n")

    largo = max(len(p["caption"]) for p in d["posts"])
    print(f"\n{tocados} captions reescritas | la mas larga: {largo} de 2200")

    # Red de seguridad: que no quede ninguna pendiente vendiendo el 16/10.
    import re
    sobras = [p["id"] for p in d["posts"] if p["estado"] == "pendiente"
              and re.search(r"reserv[aá]|guardamos el lugar|16 de octubre",
                            p["caption"], re.I)]
    print("Pendientes que todavia venden la cohorte:", sobras or "ninguna")


if __name__ == "__main__":
    main()
