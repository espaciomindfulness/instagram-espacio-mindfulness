#!/usr/bin/env python3
"""Noviembre de @espaciomindfulness: 12 publicaciones del 11/11 al 02/12.

Dos ejes a la vez, porque la audiencia se partio en dos:

  1. FIN DE ANIO para el publico general. Es el tema estacional obvio y no lo
     tocamos nunca en 61 publicaciones: balance, reuniones familiares,
     propositos, brindis. Son los problemas que la gente va a tener en las
     proximas seis semanas, y lo que resuelve un problema concreto es lo que
     se guarda.

  2. LAS DOS FORMACIONES 2027. La matricula bonificada de las dos vence el
     30/11 (verificado en las landings el 09/11/2026), y el aviso de busqueda
     laboral de octubre trajo +341 seguidores que en su mayoria son
     psicologos. Publico y plazo coinciden una sola vez.

El Instructorado nunca se habia anunciado en EM. Requisito: ser egresado del
programa MBSR. Al 09/11 la landing decia "Quedan 8 lugares".

Diplomado: 200 horas certificadas. La landing decia 250 hasta octubre y se
corrigio; el carrusel del 29/10 salio con 250 y hay que editarle el pie.

Sin montos, como siempre. "Matricula bonificada" se puede decir; el numero no.
"""
from piezas import *


# ── 11/11 · Instructorado ─────────────────────────────────────────────────
def p54_instructorado():
    return [
        ("post54_inst_1.png", cubierta(
            "Instructorado", "en Mindfulness",
            "Cohorte 2027 · Para quienes ya hicieron el MBSR.", claro=True)),
        ("post54_inst_2.png", punto(
            "PARA QUIÉN", "Para egresados del programa MBSR.",
            "Ese es el requisito y no es un trámite: no se enseña a guiar algo "
            "que no se transitó primero en carne propia.")),
        ("post54_inst_3.png", punto(
            "CUÁNDO", "Un sábado al mes, de 10 a 14.",
            "Segundos sábados, de abril a diciembre de 2027. Los cinco "
            "primeros encuentros en vivo por Zoom y los cuatro últimos "
            "presenciales, en Villa Urquiza.")),
        ("post54_inst_4.png", punto(
            "QUÉ SE VE", "Nueve módulos, del rol al oficio.",
            "Manejo de grupos, neuroeducación, mindfulness con niños, "
            "psicodeporte, mindfulness empresarial, diseño de talleres "
            "—MBSR, MBCT y MSC— y prácticas compasivas.")),
        ("post54_inst_5.png", cierre_cta(
            "Arranca el 10 de abril",
            "Trescientas horas certificadas, con numeración única. La "
            "matrícula está bonificada hasta el 30 de noviembre y los grupos "
            "son chicos.",
            "ESCRIBINOS POR WHATSAPP", "CUPOS LIMITADOS")),
    ]


# ── 13/11 · el estrés de fin de año ───────────────────────────────────────
def p55_fin_de_anio():
    return [
        ("post55_finanio_1.png", cubierta(
            "El cansancio de noviembre", "no es el de marzo",
            "Por qué el final del año pega distinto, y qué hacer con eso.")),
        ("post55_finanio_2.png", punto(
            None, "Se acumulan los cierres.",
            "Todo lo que se postergó durante el año vence ahora, y en "
            "simultáneo. No es que trabajes más: es que trabajás contra un "
            "calendario que se achica.", 1)),
        ("post55_finanio_3.png", punto(
            None, "Aparece el balance, y casi nunca es amable.",
            "Diciembre invita a comparar lo que pasó con lo que habías "
            "planeado en enero. Esa comparación la hacemos con una vara que "
            "no le aplicaríamos a nadie más.", 2)),
        ("post55_finanio_4.png", punto(
            None, "Vuelven las reuniones que no elegiste.",
            "Brindis de trabajo, familia extendida, gente que no ves hace un "
            "año y te pregunta cómo venís. Es exigencia social concentrada en "
            "tres semanas.", 3)),
        ("post55_finanio_5.png", punto(
            None, "Y el descanso se promete, no se toma.",
            "«En enero descanso» sostiene noviembre y diciembre a crédito. El "
            "cuerpo no acepta pagarés.", 4)),
        ("post55_finanio_6.png", cierre_cta(
            "No se trata de bajar el ritmo",
            "A veces no se puede. Se trata de notar cuál de estas cuatro cosas "
            "te está pesando de verdad, porque cada una se trabaja distinto.",
            "CHARLA GRATUITA · LINK EN BIO")),
    ]


# ── 15/11 · frase ─────────────────────────────────────────────────────────
def p56_frase_descanso():
    return texto_suelto(
        "PARA PENSAR",
        "Descansar no es lo que queda después de terminar todo.",
        "Si fuera así, nunca tocaría. El descanso es una decisión que se toma "
        "con cosas pendientes, o no se toma nunca.",
        None, claro=True)


# ── 17/11 · las reuniones ─────────────────────────────────────────────────
def p57_reuniones():
    return [
        ("post57_reuniones_1.png", cubierta(
            "Esa reunión familiar", "de la que no te podés ir",
            "Cinco cosas que ayudan cuando irse no es una opción.",
            claro=True)),
        ("post57_reuniones_2.png", punto(
            None, "Decidí antes a qué vas.",
            "No a pasarla bien necesariamente: quizás vas a ver a una persona "
            "en particular, o a que tus hijos vean a sus primos. Tener clara "
            "la razón cambia lo que estás dispuesto a bancar.", 1)),
        ("post57_reuniones_3.png", punto(
            None, "Esperá la pregunta incómoda.",
            "Vas a saber cuál es y quién la va a hacer. Lo que descoloca no es "
            "la pregunta: es que te agarre desprevenido. Pensá de antemano una "
            "respuesta corta y amable que no abra la discusión.", 2)),
        ("post57_reuniones_4.png", punto(
            None, "Usá el cuerpo como ancla.",
            "Los pies en el piso, el peso en la silla, tres respiraciones sin "
            "que nadie lo note. No es relajarse: es volver a estar ahí en vez "
            "de en la discusión que estás anticipando.", 3)),
        ("post57_reuniones_5.png", punto(
            None, "Date salidas cortas.",
            "Ir a la cocina, salir al balcón, lavar unos platos. Dos minutos "
            "solo cada tanto hacen más que aguantar cuatro horas seguidas.", 4)),
        ("post57_reuniones_6.png", punto(
            None, "Y bajá la expectativa de que sea distinto.",
            "La mayor parte del malestar no viene de lo que pasa, sino de que "
            "esperábamos que esta vez no pasara. Suele pasar.", 5)),
        ("post57_reuniones_7.png", cierre_cta(
            "Guardátelo para diciembre",
            "Ninguna de las cinco cambia a tu familia. Las cinco cambian con "
            "qué llegás vos, que es lo único que está a tu alcance.",
            "CHARLA GRATUITA · LINK EN BIO", claro=True)),
    ]


# ── 19/11 · Diplomado ─────────────────────────────────────────────────────
def p58_diplomado():
    return texto_suelto(
        "FORMACIÓN PROFESIONAL · 2027",
        "Diplomado en Psicoterapia Basada en Procesos",
        "Mindfulness, ACT y compasión integrados en un solo marco. Nueve "
        "encuentros en vivo por Zoom, un martes por mes, más el cierre "
        "presencial. Doscientas horas certificadas.",
        "MATRÍCULA BONIFICADA HASTA EL 30/11", claro=False)


# ── 21/11 · el balance ────────────────────────────────────────────────────
def p59_balance():
    return [
        ("post59_balance_1.png", cubierta(
            "Hacer un balance", "sin maltratarte",
            "Cuatro preguntas mejores que «¿cumplí lo que me propuse?».")),
        ("post59_balance_2.png", punto(
            None, "¿Qué cambió que no estaba en el plan?",
            "El año trae cosas que no figuraban en la lista de enero. Si solo "
            "medís contra el plan, todo eso queda afuera del balance como si "
            "no hubiera existido.", 1)),
        ("post59_balance_3.png", punto(
            None, "¿Qué sostuviste cuando se puso difícil?",
            "No lo que lograste: lo que seguiste haciendo igual. Eso dice más "
            "de cómo venís que cualquier resultado.", 2)),
        ("post59_balance_4.png", punto(
            None, "¿Qué dejaste ir, y estuvo bien?",
            "Abandonar algo que ya no iba no es un fracaso. En la lista de "
            "enero figura como casillero sin tildar, y en la vida real fue "
            "una buena decisión.", 3)),
        ("post59_balance_5.png", punto(
            None, "¿Le dirías a un amigo lo que te estás diciendo?",
            "Si la respuesta es no, el problema no es tu año. Es la voz con la "
            "que lo estás evaluando.", 4)),
        ("post59_balance_6.png", cierre_cta(
            "El balance no es un juicio",
            "Es información para decidir qué hacer distinto. Cuando se vuelve "
            "una condena, deja de servir para las dos cosas.",
            "CHARLA GRATUITA · LINK EN BIO")),
    ]


# ── 23/11 · prueba social ─────────────────────────────────────────────────
def p60_egresados():
    return texto_suelto(
        "DESDE 2012",
        "Más de mil personas pasaron por nuestros programas.",
        "Y más de cuarenta empresas. Lo decimos poco, pero cuando alguien "
        "busca dónde formarse conviene saber hace cuánto está abierto el "
        "lugar y quién lo acredita.",
        "ACREDITADOS POR GMC", claro=True)


# ── 25/11 · los propósitos ────────────────────────────────────────────────
def p61_propositos():
    return [
        ("post61_propositos_1.png", cubierta(
            "Por qué fallan", "los propósitos de enero",
            "Tres razones, y qué hacer distinto este año.", claro=True)),
        ("post61_propositos_2.png", punto(
            None, "Se eligen desde el agotamiento.",
            "Diciembre es el peor momento para decidir cómo va a ser tu año: "
            "estás cansado, y el cansancio pide cambios grandes y rápidos.", 1)),
        ("post61_propositos_3.png", punto(
            None, "Son resultados, no conductas.",
            "«Estar más tranquilo» no es algo que puedas hacer un martes. "
            "«Diez minutos de práctica antes del desayuno» sí.", 2)),
        ("post61_propositos_4.png", punto(
            None, "Y el primer día que se falla, se abandona.",
            "El propósito se plantea como una racha. Una racha se corta una "
            "sola vez. Lo que sostiene algo en el tiempo no es no fallar: es "
            "qué hacés al día siguiente.", 3)),
        ("post61_propositos_5.png", cierre_cta(
            "Volver es la práctica",
            "Sirve para meditar y sirve para cualquier cosa que quieras "
            "sostener. Irse era inevitable; lo entrenable es el regreso.",
            "CHARLA GRATUITA · LINK EN BIO", claro=True)),
    ]


# ── 27/11 · últimos días ──────────────────────────────────────────────────
def p62_ultimos_dias():
    return texto_suelto(
        "QUEDAN POCOS DÍAS",
        "El 30 de noviembre vence la matrícula bonificada.",
        "Vale para las dos formaciones 2027: el Instructorado en Mindfulness, "
        "para egresados del MBSR, y el Diplomado en Psicoterapia Basada en "
        "Procesos, para profesionales de la salud mental.",
        "ESCRIBINOS Y TE PASAMOS EL TEMARIO", claro=False)


# ── 29/11 · comer con atención ────────────────────────────────────────────
def p63_brindis():
    return [
        ("post63_brindis_1.png", cubierta(
            "Comer en diciembre", "sin pelearte con la comida",
            "Cuatro ideas para una época de brindis y sobremesas.")),
        ("post63_brindis_2.png", punto(
            None, "El problema rara vez es la comida.",
            "Es comer sin registrar que estás comiendo: de pie, hablando, con "
            "el plato apoyado en cualquier lado. Después aparece la sensación "
            "de haber comido mucho sin haber disfrutado nada.", 1)),
        ("post63_brindis_3.png", punto(
            None, "Los primeros tres bocados.",
            "Probá comer los primeros tres con atención real: temperatura, "
            "textura, sabor. Después seguí como venías. Alcanza para que el "
            "cuerpo entre en la escena.", 2)),
        ("post63_brindis_4.png", punto(
            None, "La culpa no regula nada.",
            "Comer de más y después castigarse no compensa: solo agrega "
            "malestar a algo que ya pasó, y hace más probable repetirlo.", 3)),
        ("post63_brindis_5.png", punto(
            None, "Sentate.",
            "Es lo más simple y lo que más cambia. Comer sentado y con el "
            "plato servido convierte el picoteo infinito en una comida con "
            "principio y final.", 4)),
        ("post63_brindis_6.png", cierre_cta(
            "No es un plan de alimentación",
            "Es prestar atención a algo que hacemos varias veces por día con "
            "la cabeza en otro lado. Diciembre es un buen momento para probar.",
            "CHARLA GRATUITA · LINK EN BIO")),
    ]


# ── 30/11 · último día ────────────────────────────────────────────────────
def p64_hoy_vence():
    return texto_suelto(
        "HOY ES EL ÚLTIMO DÍA",
        "Se cierra la matrícula bonificada de las formaciones 2027.",
        "Si venías dándole vueltas al Instructorado o al Diplomado, hoy es la "
        "fecha. Escribinos y resolvemos las dudas que te queden, sin "
        "compromiso.",
        "ESCRIBINOS POR WHATSAPP", claro=True)


# ── 02/12 · volver a empezar ──────────────────────────────────────────────
def p65_volver():
    return texto_suelto(
        "SI ABANDONASTE",
        "La práctica que dejaste en marzo todavía te espera.",
        "Nadie sostiene una práctica sin interrupciones. La diferencia entre "
        "quien medita hace diez años y quien abandonó no es que uno no se "
        "haya ido: es que volvió más veces.",
        None, claro=False)


def main():
    placas = []
    placas += p54_instructorado()
    placas += p55_fin_de_anio()
    placas.append(("post56_frase_descanso.png", p56_frase_descanso()))
    placas += p57_reuniones()
    placas.append(("post58_diplomado.png", p58_diplomado()))
    placas += p59_balance()
    placas.append(("post60_egresados.png", p60_egresados()))
    placas += p61_propositos()
    placas.append(("post62_ultimos_dias.png", p62_ultimos_dias()))
    placas += p63_brindis()
    placas.append(("post64_hoy_vence.png", p64_hoy_vence()))
    placas.append(("post65_volver.png", p65_volver()))
    guardar(placas, "preview_noviembre.jpg", cols=7)


if __name__ == "__main__":
    main()
