#!/usr/bin/env python3
"""Correccion: la cohorte presencial del 16/10 se lleno antes de tiempo.

Cuatro publicaciones programadas vendian lugares que ya no existen. En vez de
borrarlas, se reconvierten: el cupo lleno se usa como prueba social y la
energia comercial se redirige a lo que SI tiene inscripcion abierta, que son
las dos formaciones profesionales de 2027.

  15/09  post26  anuncio de la cohorte  ->  cupo completo + que sigue
  29/09  post33  cierre de septiembre   ->  Instructorado 2027 (anuncio)
  13/10  post43  anuncio de la cohorte  ->  Instructorado 2027 (carrusel)
  15/10  post44  ultima llamada         ->  lista de espera + charla gratuita
  29/10  post51  Diplomado              ->  mismos datos, ahora correctos

Ademas se sacan las fotos de archivo de las portadas de post43 y post51: ya
hay bastantes placas con fotos de 2019 y conviene no estirar mas ese material.

Datos de las formaciones — FUENTE: las landings publicadas, chequeadas el
04/09/2026. El tablero del proyecto tenia varias desactualizadas.

  Instructorado 2027 — inicio sabado 10/04/2027. UN sabado al mes (segundos),
  de 10 a 14, de abril a diciembre. 9 modulos en 4 bloques. Hibrido: modulos
  1-5 en vivo por Zoom, 6-9 presenciales en Villa Urquiza. 300 hs certificadas.
  REQUISITO: haber completado el programa MBSR de 8 semanas.
  El certificado lo emite Espacio Mindfulness; el GMC acredita a Christian
  como MBSR Teacher, no al Instructorado. No confundir las dos cosas.

  Diplomado 2027 — inicio martes 13/04/2027. 9 encuentros de 4 h, un martes
  por mes de 10 a 14, 100% en vivo por Zoom, de abril a diciembre. Cierre
  presencial el sabado 18/12/2027 en Buenos Aires. 17 modulos en 5 bloques.
  Mindfulness clinico, ACT y Compasion bajo el marco de la Psicoterapia
  Basada en Procesos.
  No se pone la carga horaria total: la landing dice 250 hs y el tablero
  interno dice 200. Hasta que se resuelva, mejor no publicar el numero.
"""
from piezas import *


# ── 15/09 · el cupo se lleno ──────────────────────────────────────────────
def p26_cupo_completo():
    return [
        ("post26_anuncio_1.png", cubierta(
            "Se llenó", "la presencial de octubre",
            "Gracias. Y esto es lo que sigue para quien quedó afuera.",
            claro=True)),
        ("post26_anuncio_2.png", punto(
            "QUÉ PASÓ", "La última cohorte del año completó sus lugares.",
            "Antes de lo previsto. No abrimos vacantes extra: el grupo "
            "reducido no es un detalle de folleto, es parte de cómo funciona "
            "el programa.")),
        ("post26_anuncio_3.png", punto(
            "SI TE QUEDASTE AFUERA", "Hay lista de espera.",
            "Si se libera un lugar avisamos por orden de anotación. Y si no, "
            "la próxima cohorte online arranca a principios del año que viene.")),
        ("post26_anuncio_4.png", punto(
            "MIENTRAS TANTO", "La charla gratuita sigue abierta.",
            "Cuarenta y cinco minutos: qué es el mindfulness, qué dice la "
            "evidencia y cómo funciona el MBSR por dentro. Sin costo y sin "
            "compromiso.")),
        ("post26_anuncio_5.png", cierre_cta(
            "Gracias por la confianza",
            "Escribinos y te ubicamos donde te sirva: lista de espera, "
            "cohorte online o la charla gratuita de este mes.",
            "ESCRIBINOS POR WHATSAPP", "PRÓXIMA ONLINE · PRINCIPIOS DE 2027",
            claro=True)),
    ]


# ── 29/09 · Instructorado, anuncio ────────────────────────────────────────
def p33_instructorado_anuncio():
    return texto_suelto(
        "FORMACIÓN PROFESIONAL · 2027",
        "Instructorado en Mindfulness",
        "Un sábado al mes, de abril a diciembre, entre Zoom y presencial. "
        "Trescientas horas certificadas para pasar de practicar a poder "
        "enseñar.",
        "ARRANCA EL 10 DE ABRIL", claro=False)


# ── 13/10 · Instructorado, carrusel ───────────────────────────────────────
def p43_instructorado():
    return [
        ("post43_anuncio_1.png", cubierta(
            "Instructorado", "en Mindfulness",
            "Cohorte 2027 · Arranca el sábado 10 de abril.")),
        ("post43_anuncio_2.png", punto(
            "PARA QUIÉN", "Para egresados del programa MBSR.",
            "El requisito es haber hecho las ocho semanas. No se enseña a "
            "guiar algo que no se transitó primero en carne propia.")),
        ("post43_anuncio_3.png", punto(
            "CUÁNDO", "Un sábado al mes, de 10 a 14 h.",
            "Segundos sábados, de abril a diciembre de 2027. Los cinco "
            "primeros encuentros son en vivo por Zoom y los cuatro últimos "
            "presenciales, en la sede de Villa Urquiza.")),
        ("post43_anuncio_4.png", punto(
            "QUÉ SE VE", "Nueve módulos, del rol al oficio.",
            "Manejo de grupos, neuroeducación, mindfulness con niños, "
            "psicodeporte, mindfulness empresarial, diseño de talleres "
            "—MBSR, MBCT y MSC— y prácticas compasivas.")),
        ("post43_anuncio_5.png", cierre_cta(
            "Cohorte 2027",
            "Trescientas horas certificadas, con numeración única "
            "verificable. Escribinos y te pasamos el temario completo.",
            "ESCRIBINOS POR WHATSAPP", "INICIO 10/04/2027 · CUPOS LIMITADOS")),
    ]


# ── 15/10 · lista de espera ───────────────────────────────────────────────
def p44_lista_de_espera():
    return texto_suelto(
        "MAÑANA EMPIEZA",
        "La presencial arranca con el cupo completo.",
        "Si te quedaste afuera hay lista de espera, y la próxima cohorte "
        "online arranca a principios del año que viene. La charla gratuita "
        "sigue abierta todo el mes.",
        "ESCRIBINOS POR WHATSAPP", claro=True)


# ── 29/10 · Diplomado, con los datos reales ───────────────────────────────
def p51_diplomado():
    return [
        ("post51_diplomado_1.png", cubierta(
            "Diplomado 2027", "inscripción abierta",
            "Mindfulness, ACT y Compasión, bajo el marco de procesos.")),
        ("post51_diplomado_2.png", punto(
            "PARA QUIÉN", "Psicólogos, psiquiatras y profesionales de la salud mental.",
            "Pensado para quien ya atiende y quiere incorporar mindfulness, "
            "ACT y compasión a su práctica clínica con método, no de oído.")),
        ("post51_diplomado_3.png", punto(
            "CUÁNDO", "Nueve encuentros, un martes por mes.",
            "Cuatro horas cada uno, de 10 a 14, todos en vivo por Zoom, de "
            "abril a diciembre. Más el cierre presencial del sábado 18 de "
            "diciembre en Buenos Aires.")),
        ("post51_diplomado_4.png", punto(
            "QUÉ VAS A VER", "Diecisiete módulos en cinco bloques.",
            "Del diagnóstico a los procesos de cambio, con el modelo de Hayes "
            "y Hofmann. Mindfulness clínico, ACT, compasión y un bloque final "
            "de integración con casos reales.")),
        ("post51_diplomado_5.png", cierre_cta(
            "Cohorte 2027",
            "Arranca el martes 13 de abril. Escribinos y te pasamos el "
            "temario completo en PDF. Los grupos son chicos.",
            "ESCRIBINOS POR WHATSAPP", "EN VIVO POR ZOOM · CIERRE PRESENCIAL")),
    ]


def main():
    placas = []
    placas += p26_cupo_completo()
    placas.append(("post33_cierre.png", p33_instructorado_anuncio()))
    placas += p43_instructorado()
    placas.append(("post44_ultima_llamada.png", p44_lista_de_espera()))
    placas += p51_diplomado()
    guardar(placas, "preview_correccion_cupo.jpg", cols=6)


if __name__ == "__main__":
    main()
