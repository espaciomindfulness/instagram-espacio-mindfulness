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
  "Arranca el sábado 10 de abril. Un sábado al mes, de 10 a 14, de abril a "
  "diciembre: los cinco primeros encuentros en vivo por Zoom y los cuatro "
  "últimos presenciales en Villa Urquiza.\n\n"
  "Es para egresados del programa MBSR. Ese es el requisito y no es un "
  "capricho: no se enseña a guiar algo que no se transitó primero en carne "
  "propia.\n\n"
  "Trescientas horas certificadas, con numeración única verificable.\n\n"
  "La inscripción está abierta y los cupos son limitados. Escribinos y te "
  "pasamos el temario completo de los nueve módulos 🌿", HT_PRO),

 "post43-anuncio-ultima-cohorte": (
  "Hiciste el MBSR. ¿Y si el próximo paso es enseñarlo?\n\n"
  "El Instructorado en Mindfulness 2027 arranca el sábado 10 de abril 👉 "
  "deslizá.\n\n"
  "Un sábado al mes de 10 a 14, de abril a diciembre. Nueve módulos: los "
  "cinco primeros en vivo por Zoom y los cuatro últimos presenciales en "
  "Villa Urquiza.\n\n"
  "Se ve manejo de grupos y rol del instructor, neuroeducación, mindfulness "
  "con niños, psicodeporte, mindfulness empresarial, diseño de talleres "
  "—MBSR, MBCT y MSC— y prácticas compasivas. Trescientas horas certificadas.\n\n"
  "Y la advertencia que hacemos siempre, incluso si elegís formarte en otro "
  "lado: en mindfulness no hay matrícula ni colegio que regule. Cualquiera "
  "puede llamarse instructor mañana. Antes de anotarte donde sea, preguntá "
  "quién dirige la formación y con qué acreditación.\n\n"
  "Acá la dirección académica es del Lic. Christian Arpa, psicólogo (UBA) y "
  "MBSR Teacher acreditado por Global Mindfulness Collaborative.\n\n"
  "Escribinos por WhatsApp y te pasamos el temario completo 🌿", HT_PRO),

 "post44-ultima-llamada": (
  "Mañana arranca la presencial, con el cupo completo.\n\n"
  "Fue la última cohorte presencial del año y se llenó. Gracias 🌿\n\n"
  "Si te quedaste afuera, no se termina acá:\n\n"
  "· Hay lista de espera, por si se libera un lugar.\n"
  "· La próxima cohorte online arranca a principios del año que viene.\n"
  "· La charla gratuita de 45 minutos sigue abierta todo el mes.\n\n"
  "Y si lo tuyo es formarte para enseñar, el Instructorado 2027 arranca el "
  "10 de abril y el Diplomado el 13. Los dos con inscripción abierta.\n\n"
  "Escribinos por WhatsApp y vemos cuál te sirve.", HT),

 "post51-diplomado-2027": (
  "Diplomado en Psicoterapia Basada en Procesos — Cohorte 2027.\n\n"
  "Mindfulness, ACT y Compasión: los tres enfoques con más evidencia clínica, "
  "integrados en un solo marco de trabajo. Por procesos del paciente, no por "
  "protocolos cerrados 👉 deslizá.\n\n"
  "Arranca el martes 13 de abril. Nueve encuentros de cuatro horas, un martes "
  "por mes de 10 a 14, todos en vivo por Zoom, hasta diciembre. Más el cierre "
  "presencial del sábado 18 de diciembre en Buenos Aires: práctica intensiva, "
  "supervisión final y graduación.\n\n"
  "En vivo, dicho en serio: no es una plataforma con clases grabadas y una "
  "reunión al mes. Se cursa con el grupo, con supervisión y con casos "
  "clínicos reales.\n\n"
  "Diecisiete módulos en cinco bloques, y uno de ellos es solo de integración "
  "clínica — que es donde suelen quedar cortas las formaciones que enseñan "
  "los modelos por separado. Doscientas cincuenta horas certificadas, con "
  "numeración única verificable.\n\n"
  "Escribinos y te pasamos el temario completo en PDF 🌿", HT_PRO),
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
