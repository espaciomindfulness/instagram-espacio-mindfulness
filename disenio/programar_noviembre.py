#!/usr/bin/env python3
"""Programa noviembre de @espaciomindfulness: 11/11 al 02/12, dia por medio.

Carruseles 19:00 e imagenes 09:30, que es el reparto que ya venia usando la
cuenta.

El mes esta construido alrededor del 30/11, que es cuando vence la matricula
bonificada de las dos formaciones 2027 (verificado en las landings el
09/11/2026). Las piezas comerciales son cuatro —11, 19, 27 y 30— y el resto
es contenido de fin de anio para el publico general.

Sin montos. "Matricula bonificada" se dice; el numero no.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
RUTA = RAIZ / "contenido" / "calendario.json"

HT = ("#Mindfulness #MBSR #MindfulnessArgentina #SaludMental #Ansiedad "
      "#ReduccionDeEstres #EspacioMindfulness")
HT_PRO = ("#Mindfulness #MBSR #Psicologia #ACT #Psicoterapia "
          "#FormacionProfesional #SaludMental #EspacioMindfulness")

P = [
 ("2026-11-11", "19:00", "post54-instructorado", "carrusel",
  [f"post54_inst_{i}.jpg" for i in range(1, 6)], HT_PRO,
  "¿Hiciste el MBSR y pensaste alguna vez en enseñarlo?\n\n"
  "El Instructorado en Mindfulness 2027 arranca el sábado 10 de abril 👉 "
  "deslizá.\n\n"
  "Un sábado al mes de 10 a 14, de abril a diciembre. Nueve módulos: los "
  "cinco primeros en vivo por Zoom y los cuatro últimos presenciales en "
  "Villa Urquiza.\n\n"
  "El requisito es haber hecho el programa MBSR de ocho semanas, y no es un "
  "trámite: no se enseña a guiar algo que no se transitó primero en carne "
  "propia.\n\n"
  "Trescientas horas certificadas. La matrícula está bonificada hasta el 30 "
  "de noviembre y los cupos son limitados.\n\n"
  "Escribinos y te pasamos el temario completo 🌿"),

 ("2026-11-13", "19:00", "post55-cansancio-noviembre", "carrusel",
  [f"post55_finanio_{i}.jpg" for i in range(1, 7)], HT,
  "El cansancio de noviembre no es el de marzo.\n\n"
  "Cuatro razones por las que el final del año pega distinto 👉 deslizá.\n\n"
  "La segunda es la que menos se nombra: diciembre invita a comparar lo que "
  "pasó con lo que habías planeado en enero, y esa comparación la hacemos "
  "con una vara que no le aplicaríamos a nadie más.\n\n"
  "No se trata de bajar el ritmo — a veces no se puede. Se trata de notar "
  "cuál de las cuatro te está pesando de verdad, porque cada una se trabaja "
  "distinto.\n\n"
  "¿Cuál reconocés? 👇"),

 ("2026-11-15", "09:30", "post56-frase-descanso", "imagen",
  ["post56_frase_descanso.jpg"], HT,
  "Descansar no es lo que queda después de terminar todo.\n\n"
  "Si fuera así, nunca tocaría. Siempre hay algo más, y en noviembre más "
  "todavía.\n\n"
  "El descanso es una decisión que se toma con cosas pendientes, o no se "
  "toma nunca 🌿"),

 ("2026-11-17", "19:00", "post57-reuniones", "carrusel",
  [f"post57_reuniones_{i}.jpg" for i in range(1, 8)], HT,
  "Esa reunión familiar de la que no te podés ir.\n\n"
  "Cinco cosas que ayudan cuando irse no es una opción 👉 deslizá.\n\n"
  "La segunda vale por todas: ya sabés cuál es la pregunta incómoda y quién "
  "la va a hacer. Lo que descoloca no es la pregunta, es que te agarre "
  "desprevenido. Tener pensada una respuesta corta y amable cambia la noche "
  "entera.\n\n"
  "Ninguna de las cinco cambia a tu familia. Las cinco cambian con qué "
  "llegás vos, que es lo único que está a tu alcance.\n\n"
  "Guardátelo para diciembre 🌿"),

 ("2026-11-19", "09:30", "post58-diplomado-noviembre", "imagen",
  ["post58_diplomado.jpg"], HT_PRO,
  "Diplomado en Psicoterapia Basada en Procesos — Cohorte 2027.\n\n"
  "Mindfulness, ACT y compasión integrados en un solo marco de trabajo: por "
  "procesos del paciente, no por protocolos cerrados.\n\n"
  "Nueve encuentros de cuatro horas, un martes por mes, todos en vivo por "
  "Zoom, de abril a diciembre. Más el cierre presencial en Buenos Aires con "
  "práctica intensiva y graduación. Doscientas horas certificadas.\n\n"
  "La matrícula está bonificada hasta el 30 de noviembre.\n\n"
  "Escribinos y te pasamos el temario completo en PDF 🌿"),

 ("2026-11-21", "19:00", "post59-balance", "carrusel",
  [f"post59_balance_{i}.jpg" for i in range(1, 7)], HT,
  "Hacer un balance del año sin maltratarte.\n\n"
  "Cuatro preguntas mejores que «¿cumplí lo que me propuse?» 👉 deslizá.\n\n"
  "La tercera es la que más desarma: abandonar algo que ya no iba no es un "
  "fracaso. En la lista de enero figura como casillero sin tildar, y en la "
  "vida real fue una buena decisión.\n\n"
  "El balance no es un juicio. Es información para decidir qué hacer "
  "distinto — y cuando se vuelve una condena, deja de servir para las dos "
  "cosas.\n\n"
  "Guardátelo para cuando llegue el momento 🌿"),

 ("2026-11-23", "09:30", "post60-egresados-noviembre", "imagen",
  ["post60_egresados.jpg"], HT,
  "Más de mil personas pasaron por nuestros programas desde 2012. Y más de "
  "cuarenta empresas.\n\n"
  "Lo decimos poco. Pero cuando alguien busca dónde empezar a practicar o "
  "dónde formarse, conviene saber hace cuánto está abierto el lugar y quién "
  "lo acredita.\n\n"
  "Espacio Mindfulness está acreditado por Global Mindfulness Collaborative, "
  "que es el estándar internacional para la formación de instructores de "
  "MBSR.\n\n"
  "Chequealo. Y chequeá a cualquiera con quien vayas a formarte 🌿"),

 ("2026-11-25", "19:00", "post61-propositos", "carrusel",
  [f"post61_propositos_{i}.jpg" for i in range(1, 6)], HT,
  "Por qué fallan los propósitos de enero, y qué hacer distinto este año.\n\n"
  "Tres razones 👉 deslizá.\n\n"
  "La segunda es la más práctica: «estar más tranquilo» no es algo que "
  "puedas hacer un martes. «Diez minutos de práctica antes del desayuno» sí. "
  "Un propósito que no se puede agendar no es un propósito, es un deseo.\n\n"
  "Y la tercera explica casi todos los abandonos: el propósito se plantea "
  "como una racha, y una racha se corta una sola vez. Lo que sostiene algo "
  "en el tiempo no es no fallar, es qué hacés al día siguiente.\n\n"
  "Volver es la práctica 🌿"),

 ("2026-11-27", "09:30", "post62-ultimos-dias", "imagen",
  ["post62_ultimos_dias.jpg"], HT_PRO,
  "Quedan pocos días: el 30 de noviembre vence la matrícula bonificada de "
  "las dos formaciones 2027.\n\n"
  "· **Instructorado en Mindfulness** — para egresados del programa MBSR que "
  "quieran formarse para conducir grupos. Arranca el 10 de abril, un sábado "
  "al mes.\n\n"
  "· **Diplomado en Psicoterapia Basada en Procesos** — para psicólogos y "
  "profesionales de la salud mental. Arranca el 13 de abril, un martes al "
  "mes en vivo por Zoom.\n\n"
  "Los dos con cupos limitados y grupos chicos.\n\n"
  "Escribinos por WhatsApp y te pasamos el temario del que te interese 🌿"),

 ("2026-11-29", "19:00", "post63-brindis", "carrusel",
  [f"post63_brindis_{i}.jpg" for i in range(1, 7)], HT,
  "Comer en diciembre sin pelearte con la comida.\n\n"
  "Cuatro ideas para una época de brindis y sobremesas 👉 deslizá.\n\n"
  "La primera cambia el enfoque: el problema rara vez es la comida. Es comer "
  "sin registrar que estás comiendo — de pie, hablando, con el plato apoyado "
  "en cualquier lado. Después queda la sensación de haber comido mucho sin "
  "haber disfrutado nada.\n\n"
  "Y la cuarta es la más simple y la que más cambia: sentate. Comer sentado "
  "y con el plato servido convierte el picoteo infinito en una comida con "
  "principio y final.\n\n"
  "No es un plan de alimentación. Es prestar atención a algo que hacemos "
  "varias veces por día con la cabeza en otro lado 🌿"),

 ("2026-11-30", "09:30", "post64-hoy-vence", "imagen",
  ["post64_hoy_vence.jpg"], HT_PRO,
  "Hoy es el último día de matrícula bonificada para las formaciones 2027.\n\n"
  "Si venías dándole vueltas al Instructorado o al Diplomado, hoy es la "
  "fecha.\n\n"
  "Escribinos por WhatsApp y resolvemos las dudas que te queden — cómo se "
  "cursa, qué se ve, si es para vos. Sin compromiso 🌿"),

 ("2026-12-02", "09:30", "post65-volver-a-empezar", "imagen",
  ["post65_volver.jpg"], HT,
  "La práctica que dejaste en marzo todavía te espera.\n\n"
  "Nadie sostiene una práctica sin interrupciones. Ni los que enseñamos.\n\n"
  "La diferencia entre quien medita hace diez años y quien abandonó no es "
  "que uno no se haya ido. Es que volvió más veces.\n\n"
  "Diciembre parece el peor mes para retomar, y por eso mismo es un buen "
  "lugar para probar que no hace falta esperar a enero 🌿"),
]


def main():
    d = json.load(open(RUTA, encoding="utf-8"))
    existentes = {p["id"] for p in d["posts"]}
    nuevos = 0
    for fecha, hora, pid, tipo, arch, ht, cuerpo in P:
        if pid in existentes:
            continue
        faltan = [a for a in arch
                  if not (RAIZ / "contenido" / "publicar" / a).exists()]
        if faltan:
            print(f"  ! {pid}: faltan {faltan[:2]}")
            continue
        post = dict(id=pid, tipo=tipo, estado="pendiente", fecha=fecha,
                    hora=hora, caption=cuerpo + "\n\n" + ht)
        if tipo == "carrusel":
            post["archivos"] = arch
        else:
            post["archivo"] = arch[0]
        d["posts"].append(post)
        nuevos += 1
    d["posts"].sort(key=lambda p: (p["fecha"], p["hora"]))
    open(RUTA, "w", encoding="utf-8").write(
        json.dumps(d, ensure_ascii=False, indent=2) + "\n")

    largo = max(len(p["caption"]) for p in d["posts"])
    print(f"{nuevos} publicaciones | caption mas larga: {largo} de 2200\n")
    for p in d["posts"]:
        if p["estado"] == "pendiente":
            n = len(p.get("archivos", [])) or 1
            print(f"  {p['fecha']} {p['hora']}  {p['tipo']:<9} {n:^3}  {p['id']}")


if __name__ == "__main__":
    main()
