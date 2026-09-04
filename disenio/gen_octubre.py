#!/usr/bin/env python3
"""Octubre de @espaciomindfulness: 16 publicaciones, del 01/10 al 31/10.

El mes tiene un quiebre en el medio: el viernes 16/10 arranca la ULTIMA
cohorte presencial del anio. Antes de esa fecha el mes empuja hacia ahi;
despues ya no hay nada que vender en 2026, asi que pasa a valor puro,
charla gratuita y siembra del Diplomado 2027.

Los fondos alternan crema y turquesa para que la grilla del perfil no quede
monocroma. Sin precios.
"""
from piezas import *


# ── 01/10 · psicoeducación ────────────────────────────────────────────────
def p37_ansiedad_que_es():
    return [
        ("post37_ansiedad_1.png", cubierta(
            "Qué es la ansiedad", "y qué no",
            "Distinguirla del miedo y del estrés cambia cómo la tratás.", claro=True)),
        ("post37_ansiedad_2.png", punto(
            None, "El miedo tiene objeto. La ansiedad, no.",
            "El miedo aparece frente a algo concreto y se va cuando eso pasa. "
            "La ansiedad se anticipa a algo que todavía no ocurrió, y por eso "
            "no tiene un final claro.", 1)),
        ("post37_ansiedad_3.png", punto(
            None, "Es útil hasta que deja de serlo.",
            "Un poco de ansiedad te hace preparar la reunión. Mucha te hace "
            "no dormir la noche anterior y llegar peor. La diferencia es de "
            "cantidad, no de tipo.", 2)),
        ("post37_ansiedad_4.png", punto(
            None, "Vive en el cuerpo antes que en la cabeza.",
            "Pecho apretado, mandíbula, estómago. Muchas veces el cuerpo ya "
            "está en alerta y la explicación llega después, inventada.", 3)),
        ("post37_ansiedad_5.png", punto(
            None, "No se elimina: se regula.",
            "Buscar que desaparezca del todo es la meta que más ansiedad "
            "genera. El objetivo razonable es que no maneje tus decisiones.", 4)),
        ("post37_ansiedad_6.png", cierre_cta(
            "Se puede trabajar",
            "El MBSR no promete que se vaya. Entrena la capacidad de notarla "
            "temprano y no reaccionar en automático.",
            "CHARLA GRATUITA · LINK EN BIO",
            "NO REEMPLAZA UN TRATAMIENTO PSICOLÓGICO", claro=True)),
    ]


# ── 03/10 · frase ─────────────────────────────────────────────────────────
def p38_frase_control():
    return frase("Querer controlar lo incontrolable es la forma más agotadora de cuidarse.",
                 "Christian D. Arpa", "de «Soltar con Mindfulness»")


# ── 05/10 · profesionales de la salud ─────────────────────────────────────
def p39_profesionales():
    return [
        ("post39_prof_1.png", cubierta(
            "Si trabajás", "acompañando a otros",
            "Cuatro razones por las que el mindfulness es distinto para vos.",
            "IMG_5705.JPG", 0.40, claro=True)),
        ("post39_prof_2.png", punto(
            "PRIMERO", "Escuchar cansa de una manera particular.",
            "No es el cansancio de hacer: es el de sostener. Y no se recupera "
            "durmiendo más, porque el desgaste es atencional.")),
        ("post39_prof_3.png", punto(
            "SEGUNDO", "Tu atención es tu herramienta de trabajo.",
            "En cualquier otra profesión la distracción cuesta tiempo. "
            "En la tuya cuesta vínculo: el otro se da cuenta.")),
        ("post39_prof_4.png", punto(
            "TERCERO", "No podés dar lo que no practicás.",
            "Enseñar regulación emocional sin entrenarla uno mismo se nota. "
            "Los pacientes leen el estado del terapeuta antes que sus palabras.")),
        ("post39_prof_5.png", punto(
            "CUARTO", "Y hay evidencia específica.",
            "Los programas de mindfulness para profesionales de la salud "
            "muestran reducciones en burnout y en fatiga por compasión.")),
        ("post39_prof_6.png", cierre_cta(
            "Formate en serio",
            "Tenemos programas para profesionales, con aval internacional. "
            "El primer paso es la charla gratuita.",
            "CHARLA GRATUITA · LINK EN BIO", "ACREDITADOS POR GMC", claro=True)),
    ]


# ── 07/10 · autoridad ─────────────────────────────────────────────────────
def p40_trayectoria():
    return texto_suelto(
        "DESDE 2012",
        "Catorce años enseñando lo mismo, cada vez mejor.",
        "Más de mil personas formadas, más de cuarenta empresas acompañadas y "
        "una acreditación internacional que hay que revalidar. No es una moda "
        "que tomamos: es lo único que hacemos.",
        "ACREDITADOS POR GMC", claro=True)


# ── 09/10 · el retiro ─────────────────────────────────────────────────────
def p41_retiro():
    return [
        ("post41_retiro_1.png", cubierta(
            "El día de silencio", "que nadie te cuenta",
            "La parte del MBSR que más se teme y más se agradece.")),
        ("post41_retiro_2.png", punto(
            "QUÉ ES", "Una jornada completa de práctica, sobre la semana seis.",
            "Varias horas seguidas, en grupo, alternando prácticas sentadas, "
            "en movimiento y de alimentación consciente.")),
        ("post41_retiro_3.png", punto(
            "POR QUÉ ASUSTA", "«¿Un día entero sin hablar?»",
            "Es la pregunta de todos. El silencio no es una prueba de "
            "resistencia: es sacar una capa de ruido para que aparezca lo que "
            "estaba debajo.")),
        ("post41_retiro_4.png", punto(
            "QUÉ SUELE PASAR", "Las primeras horas son las difíciles.",
            "Después algo se acomoda. La mayoría lo describe como el día en "
            "que el programa dejó de ser un curso y pasó a ser una experiencia.")),
        ("post41_retiro_5.png", cierre_cta(
            "Está incluido en el programa",
            "No es un extra ni una actividad optativa: es parte del MBSR "
            "desde que se creó en 1979.",
            "CHARLA GRATUITA · LINK EN BIO")),
    ]


# ── 11/10 · dato ──────────────────────────────────────────────────────────
def p42_dato_ocho_semanas():
    return texto_suelto(
        "LO QUE MUESTRA LA INVESTIGACIÓN",
        "Ocho semanas no es un número arbitrario.",
        "Es la duración del protocolo original y la que usan la mayoría de los "
        "estudios. Por eso cuando alguien te ofrece «MBSR en cuatro clases», "
        "lo que sea que esté ofreciendo no es MBSR.",
        None, claro=True)


# ── 13/10 · ANUNCIO ───────────────────────────────────────────────────────
def p43_anuncio():
    return [
        ("post43_anuncio_1.png", cubierta(
            "La última", "del año",
            "Viernes 16 de octubre · Presencial en Villa Urquiza.",
            "IMG_5816.JPG", 0.42)),
        ("post43_anuncio_2.png", punto(
            "CUÁNDO", "Viernes 16 de octubre, de 19 a 21 h.",
            "Ocho semanas, un encuentro por semana, más la jornada de práctica "
            "intensiva sobre el final.")),
        ("post43_anuncio_3.png", punto(
            "DÓNDE", "Olazábal 5187, Villa Urquiza.",
            "Presencial y en grupo reducido. Es el formato que más "
            "recomendamos a quien puede: el grupo hace la mitad del trabajo.")),
        ("post43_anuncio_4.png", punto(
            "POR QUÉ AHORA", "Después de esta, la próxima es el año que viene.",
            "No es una frase de venta: es el calendario. Si venías "
            "postergándolo, esta es la fecha.")),
        ("post43_anuncio_5.png", cierre_cta(
            "Reservá tu lugar",
            "Escribinos por WhatsApp: te contamos cómo se cursa, resolvemos "
            "tus dudas y te guardamos el lugar sin compromiso.",
            "ESCRIBINOS POR WHATSAPP", "VIERNES 16/10 · VILLA URQUIZA")),
    ]


# ── 15/10 · última llamada ────────────────────────────────────────────────
def p44_ultima_llamada():
    return texto_suelto(
        "MAÑANA ARRANCA",
        "Última cohorte presencial del año.",
        "Viernes 16 de octubre, de 19 a 21 h, en Villa Urquiza. Ocho semanas "
        "de MBSR en grupo reducido. Si estabas esperando el momento, era este.",
        "ESCRIBINOS POR WHATSAPP", claro=True)


# ── 17/10 · ya empezó ─────────────────────────────────────────────────────
def p45_las_ocho_semanas():
    return [
        ("post45_semanas_1.png", cubierta(
            "Qué pasa", "en ocho semanas",
            "El recorrido del programa, semana por semana.")),
        ("post45_semanas_2.png", punto(
            "SEMANAS 1 Y 2", "Darse cuenta del piloto automático.",
            "Antes de cambiar algo hay que verlo. Las primeras prácticas son "
            "de registro: qué hace tu atención cuando nadie la mira.")),
        ("post45_semanas_3.png", punto(
            "SEMANAS 3 Y 4", "El cuerpo entra en escena.",
            "Recorrido corporal, movimiento consciente, respiración. Se "
            "empieza a notar la diferencia entre pensar una emoción y sentirla.")),
        ("post45_semanas_4.png", punto(
            "SEMANAS 5 Y 6", "Trabajar con lo difícil.",
            "Acá aparece lo incómodo: el estrés, la reactividad, lo que uno "
            "venía evitando. Y en el medio, la jornada de práctica intensiva.")),
        ("post45_semanas_5.png", punto(
            "SEMANAS 7 Y 8", "Que siga después.",
            "La última parte es sobre sostener la práctica sin el grupo. "
            "Es la que decide si el programa te cambia algo o queda como un "
            "recuerdo lindo.")),
        ("post45_semanas_6.png", cierre_cta(
            "Así es el programa completo",
            "Si querés hacerlo, la próxima cohorte online arranca a principios "
            "del año que viene. Empezá por la charla gratuita.",
            "CHARLA GRATUITA · LINK EN BIO")),
    ]


# ── 19/10 · frase ─────────────────────────────────────────────────────────
def p46_frase_volver():
    return frase("Volver es la práctica. Irse era inevitable.",
                 "Christian D. Arpa", "de «Soltar con Mindfulness»", claro=True)


# ── 21/10 · sostener la práctica ──────────────────────────────────────────
def p47_sostener():
    return [
        ("post47_sostener_1.png", cubierta(
            "Cuando la práctica", "se corta",
            "Pasa siempre. Lo que importa es qué hacés después.")),
        ("post47_sostener_2.png", punto(
            None, "No empezaste de nuevo.",
            "Dejar tres semanas no borra lo aprendido. La idea de «volver a "
            "cero» es la que hace que muchos no vuelvan nunca.", 1)),
        ("post47_sostener_3.png", punto(
            None, "Bajá el mínimo, no la frecuencia.",
            "Mejor tres minutos todos los días que treinta cuando se pueda. "
            "Lo que sostiene el hábito es la regularidad, no la duración.", 2)),
        ("post47_sostener_4.png", punto(
            None, "Atalo a algo que ya hacés.",
            "Después del café, antes de encender la computadora, al llegar a "
            "casa. Los hábitos nuevos se cuelgan de los viejos.", 3)),
        ("post47_sostener_5.png", punto(
            None, "El grupo ayuda más de lo que parece.",
            "Practicar solo es difícil para casi todos. Por eso el MBSR es "
            "grupal: no es un detalle organizativo, es parte del método.", 4)),
        ("post47_sostener_6.png", cierre_cta(
            "Volvé sin culpa",
            "Notar que te fuiste y volver ES la práctica. No hay otra cosa "
            "que aprender.",
            "CHARLA GRATUITA · LINK EN BIO")),
    ]


# ── 23/10 · charla gratuita ───────────────────────────────────────────────
def p48_charla():
    return texto_suelto(
        "45 MINUTOS, GRATIS",
        "Antes de anotarte a nada, vení a preguntar.",
        "Qué es el mindfulness, qué dice la evidencia y cómo se cursa el "
        "programa MBSR. Preguntás lo que quieras y después decidís. Sin "
        "compromiso y sin que te llamemos por teléfono.",
        "LINK EN LA BIO", claro=True)


# ── 25/10 · errores al empezar ────────────────────────────────────────────
def p49_errores():
    return [
        ("post49_errores_1.png", cubierta(
            "Cinco errores", "al empezar a meditar",
            "Casi todos los cometimos. Se corrigen fácil.")),
        ("post49_errores_2.png", punto(
            None, "Esperar que salga bien.",
            "No hay una meditación bien hecha. Si te fuiste veinte veces y "
            "volviste veinte veces, estuvo perfecta.", 1)),
        ("post49_errores_3.png", punto(
            None, "Empezar con sesiones largas.",
            "Veinte minutos el primer día es como correr diez kilómetros sin "
            "entrenar: se puede, pero no lo vas a repetir mañana.", 2)),
        ("post49_errores_4.png", punto(
            None, "Practicar solo cuando estás mal.",
            "Es entrenar el día del partido. La práctica sirve porque se hace "
            "también cuando no hace falta.", 3)),
        ("post49_errores_5.png", punto(
            None, "Buscar la mente en blanco.",
            "Ya lo dijimos y lo repetimos porque es el más común: no es el "
            "objetivo, y perseguirlo garantiza la frustración.", 4)),
        ("post49_errores_6.png", punto(
            None, "Hacerlo solo, siempre.",
            "Con una app se empieza; con un grupo y alguien que te guíe se "
            "sostiene. La diferencia aparece a la tercera semana.", 5)),
        ("post49_errores_7.png", cierre_cta(
            "Se aprende acompañado",
            "El MBSR es grupal y guiado por eso mismo. Empezá por la charla "
            "gratuita y sacate las dudas.",
            "CHARLA GRATUITA · LINK EN BIO")),
    ]


# ── 27/10 · el libro ──────────────────────────────────────────────────────
def p50_libro():
    return texto_suelto(
        "PARA LEER MIENTRAS TANTO",
        "«Soltar con Mindfulness», de Christian D. Arpa",
        "Más de cien páginas con ejercicios concretos y lineamientos para "
        "sostener la práctica. Escrito por nuestro director, que es psicólogo "
        "e instructor MBSR certificado.",
        "MERCADO LIBRE · AMAZON", claro=True)


# ── 29/10 · Diplomado 2027 ────────────────────────────────────────────────
def p51_diplomado():
    return [
        ("post51_diplomado_1.png", cubierta(
            "Diplomado 2027", "inscripción abierta",
            "Psicoterapia basada en procesos, con mindfulness y ACT.",
            "IMG_5777.JPG", 0.42)),
        ("post51_diplomado_2.png", punto(
            "PARA QUIÉN", "Psicólogos y profesionales de la salud mental.",
            "Pensado para quien ya atiende y quiere incorporar mindfulness y "
            "ACT a su práctica clínica con método, no de oído.")),
        ("post51_diplomado_3.png", punto(
            "CÓMO ES", "Formación anual, híbrida.",
            "Cursás en vivo, presencial o por Zoom, con material y "
            "seguimiento. Dieciséis módulos organizados en cinco bloques.")),
        ("post51_diplomado_4.png", punto(
            "QUÉ LO DISTINGUE", "Lo dicta gente que atiende.",
            "No es teoría de manual: el equipo trabaja clínicamente todos los "
            "días y enseña sobre lo que hace.")),
        ("post51_diplomado_5.png", cierre_cta(
            "Cohorte 2027",
            "La inscripción ya está abierta y los grupos son chicos. "
            "Escribinos y te contamos el temario completo.",
            "ESCRIBINOS POR WHATSAPP", "ACREDITADOS POR GMC")),
    ]


# ── 31/10 · cierre de mes ─────────────────────────────────────────────────
def p52_cierre():
    return texto_suelto(
        "CERRANDO OCTUBRE",
        "Si venís leyéndonos, esto es para vos.",
        "No hace falta esperar a enero para empezar. La charla gratuita dura "
        "45 minutos, es online y no te compromete a nada: contamos cómo "
        "funciona el programa y respondés si es tu momento o no.",
        "LINK EN LA BIO", claro=True)


def main():
    placas = []
    placas += p37_ansiedad_que_es()
    placas.append(("post38_frase_control.png", p38_frase_control()))
    placas += p39_profesionales()
    placas.append(("post40_trayectoria.png", p40_trayectoria()))
    placas += p41_retiro()
    placas.append(("post42_dato_ocho_semanas.png", p42_dato_ocho_semanas()))
    placas += p43_anuncio()
    placas.append(("post44_ultima_llamada.png", p44_ultima_llamada()))
    placas += p45_las_ocho_semanas()
    placas.append(("post46_frase_volver.png", p46_frase_volver()))
    placas += p47_sostener()
    placas.append(("post48_charla.png", p48_charla()))
    placas += p49_errores()
    placas.append(("post50_libro.png", p50_libro()))
    placas += p51_diplomado()
    placas.append(("post52_cierre.png", p52_cierre()))
    guardar(placas, "preview_octubre_em.jpg", cols=8)


if __name__ == "__main__":
    main()
