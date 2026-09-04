#!/usr/bin/env python3
"""Programa octubre de @espaciomindfulness: del 01/10 al 31/10, dia por medio.

Los horarios alternan 09:30 y 19:00, salteando los martes y viernes al
mediodia que ya ocupan los reels de la entrevista.

Sin precios: regla del cliente.
"""
import json
from pathlib import Path

RUTA = Path(__file__).resolve().parent.parent / "contenido" / "calendario.json"

HT = ("#Mindfulness #MBSR #MindfulnessArgentina #SaludMental #Ansiedad "
      "#ReduccionDeEstres #EspacioMindfulness")

P = [
 ("2026-10-01", "19:00", "post37-que-es-la-ansiedad", "carrusel",
  [f"post37_ansiedad_{i}.jpg" for i in range(1, 7)],
  "Miedo y ansiedad no son lo mismo, y la diferencia importa.\n\n"
  "El miedo tiene objeto: aparece frente a algo concreto y se va cuando eso "
  "pasa. La ansiedad se anticipa a algo que todavía no ocurrió, y por eso no "
  "tiene final claro 👉 deslizá.\n\n"
  "La cuarta placa es la que más cuesta aceptar: el objetivo no es que "
  "desaparezca. Buscar eliminarla del todo es, paradójicamente, lo que más "
  "ansiedad genera.\n\n"
  "El mindfulness no promete que se vaya. Entrena la capacidad de notarla "
  "temprano y no reaccionar en automático 🌿\n\n"
  "No reemplaza un tratamiento psicológico. Si la estás pasando mal, consultá."),

 ("2026-10-03", "09:30", "post38-frase-control", "imagen", ["post38_frase_control.jpg"],
  "«Querer controlar lo incontrolable es la forma más agotadora de cuidarse.»\n\n"
  "De «Soltar con Mindfulness», de Christian D. Arpa.\n\n"
  "Casi siempre el control excesivo empieza como cuidado: revisar, anticipar, "
  "prevenir. El problema es que lo que no depende de vos no se vuelve más "
  "seguro porque lo vigiles más — solo te cansa a vos.\n\n"
  "¿Qué estás vigilando últimamente que no depende de vos? 🌿"),

 ("2026-10-05", "19:00", "post39-profesionales-salud", "carrusel",
  [f"post39_prof_{i}.jpg" for i in range(1, 7)],
  "Si trabajás escuchando a otros, esto es distinto para vos.\n\n"
  "El cansancio de sostener no es el de hacer, y no se recupera durmiendo más: "
  "el desgaste es atencional 👉 deslizá.\n\n"
  "La tercera razón es la más incómoda de la profesión: no se puede enseñar "
  "regulación emocional sin entrenarla uno mismo. Los pacientes leen el estado "
  "del terapeuta antes que sus palabras.\n\n"
  "Tenemos formaciones específicas para profesionales de la salud, con aval "
  "internacional. El primer paso es la charla gratuita 🌿"),

 ("2026-10-07", "09:30", "post40-trayectoria", "imagen", ["post40_trayectoria.jpg"],
  "Catorce años enseñando lo mismo, cada vez mejor.\n\n"
  "Espacio Mindfulness abrió en 2012. Desde entonces pasaron más de mil "
  "personas por nuestros programas y acompañamos a más de cuarenta empresas.\n\n"
  "Estamos acreditados por Global Mindfulness Collaborative, que es el estándar "
  "internacional para la formación de instructores de MBSR — y que hay que "
  "revalidar, no se obtiene una vez y listo.\n\n"
  "No es una moda que tomamos. Es lo único que hacemos 🌿"),

 ("2026-10-09", "19:00", "post41-dia-de-silencio", "carrusel",
  [f"post41_retiro_{i}.jpg" for i in range(1, 6)],
  "«¿Un día entero sin hablar?»\n\n"
  "Es la pregunta de todos cuando cuentan que el MBSR incluye una jornada de "
  "práctica intensiva 👉 deslizá.\n\n"
  "El silencio no es una prueba de resistencia ni un requisito espiritual: es "
  "sacar una capa de ruido para que aparezca lo que estaba debajo. Las primeras "
  "horas son las difíciles; después algo se acomoda.\n\n"
  "La mayoría lo describe como el día en que el programa dejó de ser un curso "
  "y pasó a ser una experiencia.\n\n"
  "Está incluido desde que el MBSR se creó, en 1979. Charla gratuita en el "
  "link de la bio 🌿"),

 ("2026-10-11", "09:30", "post42-ocho-semanas", "imagen", ["post42_dato_ocho_semanas.jpg"],
  "Ocho semanas no es un número arbitrario.\n\n"
  "Es la duración del protocolo original de MBSR y la que usa la mayoría de "
  "los estudios que sostienen su evidencia.\n\n"
  "Por eso, cuando alguien te ofrece «MBSR en cuatro clases», lo que sea que "
  "esté ofreciendo puede estar buenísimo — pero no es MBSR.\n\n"
  "No es purismo: es que los resultados que muestra la investigación "
  "corresponden a ese formato, no a una versión abreviada 🌿"),

 ("2026-10-13", "19:00", "post43-anuncio-ultima-cohorte", "carrusel",
  [f"post43_anuncio_{i}.jpg" for i in range(1, 6)],
  "Abrimos la última cohorte presencial del año.\n\n"
  "📍 Viernes 16 de octubre · 19 a 21 h · Villa Urquiza\n\n"
  "Ocho semanas de MBSR en grupo reducido, más la jornada de práctica "
  "intensiva sobre el final. Presencial, que es el formato que más "
  "recomendamos a quien puede: el grupo hace la mitad del trabajo.\n\n"
  "Después de esta, la próxima presencial arranca el año que viene. No es una "
  "frase de venta, es el calendario.\n\n"
  "Escribinos por WhatsApp: te contamos cómo se cursa, resolvemos tus dudas y "
  "te guardamos el lugar sin compromiso 🌿"),

 ("2026-10-15", "09:30", "post44-ultima-llamada", "imagen", ["post44_ultima_llamada.jpg"],
  "Mañana arranca.\n\n"
  "📍 Viernes 16 de octubre · 19 a 21 h · Villa Urquiza\n\n"
  "Última cohorte presencial del año: ocho semanas de MBSR en grupo reducido.\n\n"
  "Si venís postergándolo desde hace meses, este es el punto donde postergarlo "
  "un poco más significa esperar hasta el año que viene.\n\n"
  "Escribinos por WhatsApp y lo resolvemos hoy 🌿"),

 ("2026-10-17", "19:00", "post45-ocho-semanas-por-dentro", "carrusel",
  [f"post45_semanas_{i}.jpg" for i in range(1, 7)],
  "Qué pasa, semana por semana, en un programa de MBSR.\n\n"
  "Ayer arrancó la última cohorte presencial del año, así que aprovechamos "
  "para contarte el recorrido completo por dentro 👉 deslizá.\n\n"
  "Fijate el orden: primero darse cuenta del piloto automático, después el "
  "cuerpo, después lo difícil, y recién al final cómo sostenerlo solo. Esa "
  "última parte es la que decide si el programa te cambia algo o queda como "
  "un recuerdo lindo.\n\n"
  "Si querés hacerlo, la próxima cohorte online arranca a principios del año "
  "que viene. Empezá por la charla gratuita 🌿"),

 ("2026-10-19", "09:30", "post46-frase-volver", "imagen", ["post46_frase_volver.jpg"],
  "«Volver es la práctica. Irse era inevitable.»\n\n"
  "De «Soltar con Mindfulness», de Christian D. Arpa.\n\n"
  "Mucha gente abandona la meditación convencida de que la hace mal, porque "
  "se distrae. Pero distraerse no es el error: es lo que la mente hace.\n\n"
  "El ejercicio no es quedarse. Es darse cuenta de que te fuiste, y volver. "
  "Cuantas más veces te vas y volvés, más entrenás 🌿"),

 ("2026-10-21", "19:00", "post47-sostener-la-practica", "carrusel",
  [f"post47_sostener_{i}.jpg" for i in range(1, 7)],
  "Dejaste de practicar hace tres semanas. ¿Y ahora?\n\n"
  "Le pasa a todo el mundo, y lo que hace daño no es el corte: es la idea de "
  "que hay que «empezar de nuevo» 👉 deslizá.\n\n"
  "Cuatro cosas que ayudan a retomar, y ninguna requiere fuerza de voluntad. "
  "La segunda es la más contraintuitiva: bajá el mínimo, no la frecuencia. "
  "Tres minutos todos los días le ganan a treinta cuando se pueda.\n\n"
  "Volvé sin culpa. Notar que te fuiste y volver ES la práctica 🌿"),

 ("2026-10-23", "09:30", "post48-charla-gratuita", "imagen", ["post48_charla.jpg"],
  "Antes de anotarte a nada, vení a preguntar.\n\n"
  "La charla gratuita dura 45 minutos, es online y no te compromete a nada: "
  "contamos qué es el mindfulness, qué dice la evidencia y cómo se cursa el "
  "programa MBSR.\n\n"
  "Preguntás lo que quieras y después decidís. No te vamos a llamar por "
  "teléfono ni a insistirte por mail.\n\n"
  "Es el paso que recomendamos antes de comprometer ocho semanas de tu vida "
  "con algo que todavía no entendés del todo. Link en la bio 🌿"),

 ("2026-10-25", "19:00", "post49-errores-al-empezar", "carrusel",
  [f"post49_errores_{i}.jpg" for i in range(1, 8)],
  "Cinco errores al empezar a meditar. Los cometimos todos.\n\n"
  "Son los que hacen que la mayoría abandone en la segunda semana, y ninguno "
  "tiene que ver con falta de disciplina 👉 deslizá.\n\n"
  "El tercero es el más frecuente: practicar solo cuando estás mal. Es como "
  "entrenar el día del partido. La práctica sirve justamente porque se hace "
  "también los días en que no hace falta.\n\n"
  "Y el quinto explica por qué el MBSR es grupal y guiado: no es un detalle "
  "organizativo, es parte del método 🌿"),

 ("2026-10-27", "09:30", "post50-libro", "imagen", ["post50_libro.jpg"],
  "«Soltar con Mindfulness» — Christian D. Arpa\n\n"
  "Más de cien páginas para entender de qué se trata esto, con ejercicios "
  "concretos y lineamientos para sostener la práctica en el tiempo.\n\n"
  "Lo escribió nuestro director: psicólogo (UBA), instructor MBSR certificado "
  "por Global Mindfulness Collaborative y con catorce años enseñando en "
  "Argentina.\n\n"
  "No es un libro de frases lindas. Se consigue en Mercado Libre y en Amazon "
  "📖 Link en la bio."),

 ("2026-10-29", "19:00", "post51-diplomado-2027", "carrusel",
  [f"post51_diplomado_{i}.jpg" for i in range(1, 6)],
  "Diplomado en Psicoterapia Basada en Procesos — cohorte 2027.\n\n"
  "Para psicólogos y profesionales de la salud mental que ya atienden y "
  "quieren incorporar mindfulness y ACT a su práctica con método, no de "
  "oído 👉 deslizá.\n\n"
  "Formación anual e híbrida: cursás en vivo, presencial o por Zoom, con "
  "material y seguimiento. Dieciséis módulos en cinco bloques.\n\n"
  "Lo que más nos importa: lo dicta gente que atiende. No es teoría de manual, "
  "es lo que el equipo hace todos los días en el consultorio.\n\n"
  "La inscripción ya está abierta y los grupos son chicos. Escribinos y te "
  "pasamos el temario completo 🌿"),

 ("2026-10-31", "09:30", "post52-cierre-octubre", "imagen", ["post52_cierre.jpg"],
  "Si venís leyéndonos todo el mes, esto es para vos.\n\n"
  "No hace falta esperar a enero ni al lunes que viene. La charla gratuita "
  "dura 45 minutos, es online y no te compromete a nada: contamos cómo "
  "funciona el programa y vos ves si es tu momento o no.\n\n"
  "A veces la respuesta es «todavía no», y está perfecto. Pero es mejor "
  "saberlo después de preguntar que después de un año de dar vueltas.\n\n"
  "Link en la bio 🌿"),
]


def main():
    d = json.load(open(RUTA, encoding="utf-8"))
    existentes = {p["id"] for p in d["posts"]}
    nuevos = 0
    for fecha, hora, pid, tipo, arch, cap in P:
        if pid in existentes:
            continue
        post = dict(id=pid, tipo=tipo, estado="pendiente", fecha=fecha, hora=hora,
                    caption=cap + "\n\n" + HT)
        if tipo == "carrusel":
            post["archivos"] = arch
        else:
            post["archivo"] = arch[0]
        d["posts"].append(post)
        nuevos += 1
    d["posts"].sort(key=lambda p: (p["fecha"], p["hora"]))
    open(RUTA, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")

    largos = [len(p["caption"]) for p in d["posts"]]
    print(f"{nuevos} publicaciones nuevas | caption mas largo: {max(largos)} de 2200\n")
    for p in d["posts"]:
        if p["fecha"] >= "2026-10-01":
            n = len(p.get("archivos", [])) or 1
            print(f"  {p['fecha']} {p['hora']}  {p['tipo']:<9} {n:^3}  {p['id']}")


if __name__ == "__main__":
    main()
