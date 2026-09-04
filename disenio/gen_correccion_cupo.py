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

Datos de las formaciones (fuente: tablero maestro del proyecto EM, 2026):
  Instructorado 2027 — sabados, 300 hs, 9 modulos, MBSR/MBCT/MSC + empresarial.
  Diplomado 2027 (TBP) — 9 encuentros de 4 h en vivo por Zoom, 2os martes de
  10 a 14, del 13/04 al 14/12, cierre presencial el 18/12 en Buenos Aires,
  17 modulos en 5 bloques, 200 hs.
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
        "Trescientas horas, los sábados, para formarte y poder conducir "
        "grupos: MBSR, MBCT, MSC y mindfulness aplicado al ámbito "
        "organizacional.",
        "INSCRIPCIÓN ABIERTA", claro=False)


# ── 13/10 · Instructorado, carrusel ───────────────────────────────────────
def p43_instructorado():
    return [
        ("post43_anuncio_1.png", cubierta(
            "Instructorado", "en Mindfulness",
            "Cohorte 2027 · La inscripción ya está abierta.")),
        ("post43_anuncio_2.png", punto(
            "PARA QUIÉN", "Para quien quiere enseñar, no solo practicar.",
            "Profesionales de la salud, la educación y el ámbito "
            "organizacional que ya tienen práctica personal y quieren "
            "formarse para conducir grupos.")),
        ("post43_anuncio_3.png", punto(
            "CÓMO ES", "Trescientas horas, los sábados.",
            "Nueve módulos a lo largo del año, con formación en los tres "
            "programas — MBSR, MBCT y MSC — más mindfulness aplicado a "
            "empresas.")),
        ("post43_anuncio_4.png", punto(
            "POR QUÉ ACÁ", "En mindfulness no hay matrícula.",
            "Cualquiera puede llamarse instructor mañana. Por eso importa "
            "quién certifica: estamos acreditados por Global Mindfulness "
            "Collaborative y enseñamos desde 2012.")),
        ("post43_anuncio_5.png", cierre_cta(
            "Cohorte 2027",
            "Escribinos y te pasamos el temario completo de los nueve "
            "módulos y el calendario. Los grupos son chicos.",
            "ESCRIBINOS POR WHATSAPP", "SÁBADOS · 300 HORAS · AVAL GMC")),
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
            "Psicoterapia Basada en Procesos, con mindfulness y ACT.")),
        ("post51_diplomado_2.png", punto(
            "PARA QUIÉN", "Psicólogos y profesionales de la salud mental.",
            "Pensado para quien ya atiende y quiere incorporar mindfulness y "
            "ACT a su práctica clínica con método, no de oído.")),
        ("post51_diplomado_3.png", punto(
            "CÓMO ES", "Nueve encuentros en vivo, un martes por mes.",
            "Cuatro horas cada uno, por Zoom y en vivo, de abril a diciembre. "
            "Más un cierre presencial en Buenos Aires con práctica intensiva "
            "y graduación. Doscientas horas en total.")),
        ("post51_diplomado_4.png", punto(
            "QUÉ VAS A VER", "Diecisiete módulos en cinco bloques.",
            "Del diagnóstico a los procesos de cambio, bajo el marco de la "
            "Terapia Basada en Procesos. Lo dicta gente que atiende todos "
            "los días: no es teoría de manual.")),
        ("post51_diplomado_5.png", cierre_cta(
            "Cohorte 2027",
            "Arranca el martes 13 de abril. Escribinos y te pasamos el "
            "temario completo. Los grupos son chicos.",
            "ESCRIBINOS POR WHATSAPP", "MARTES POR ZOOM · CIERRE PRESENCIAL")),
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
