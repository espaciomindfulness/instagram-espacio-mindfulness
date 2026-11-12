#!/usr/bin/env python3
"""Carrusel del curriculum 2026 del MBSR, para publicar como colaborativo
entre @espaciomindfulness y @chris.mind2.

Se rehace con el sistema visual de EM (turquesa + crema, Georgia + Calibri)
y no con el teal oscuro y Segoe UI de la version anterior: si el unico posteo
del feed que habla de autoridad es tambien el unico que parece de otra marca,
se pierde justo lo que se quiere transmitir.

La placa 1 NO es la foto de Jon Kabat-Zinn sino la tira del Zoom. La foto de
el solo es mas linda, pero la puede publicar cualquiera; la tira es la prueba
de que Christian estuvo ahi, y eso es lo que no puede copiar nadie.

Reglas de este material:
  - Christian es MBSR Teacher calificado por el GMC. NUNCA por Brown. Participo
    de un encuentro convocado por Brown y el GMC, que es otra cosa.
  - No se enumeran los expositores: hubo mas de los cuatro que figuran en el
    material y una lista incompleta queda mal. Se nombra a Jon Kabat-Zinn.
  - Participantes: el material registrado dice 713 y Christian recuerda 750.
    Se publica "mas de 700", que es cierto con cualquiera de los dos.
  - Nada de datos de terceros: la foto de JKZ se recorto para sacar una
    burbuja de reaccion con el nombre de una asistente.
  - Sin precios.
"""
from PIL import Image, ImageDraw

# piezas reexporta todo marca, y de ahi sale cierre_cta para la ultima placa.
from piezas import *

FOTOS_LOCALES = RAIZ / "contenido" / "fotos"


def _poner(img, nombre, caja):
    """Pega una imagen recortada tipo cover dentro de la caja dada."""
    x0, y0, x1, y1 = caja
    an, al = x1 - x0, y1 - y0
    im = Image.open(FOTOS_LOCALES / nombre).convert("RGB")
    escala = max(an / im.width, al / im.height)
    im = im.resize((max(1, round(im.width * escala)),
                    max(1, round(im.height * escala))), Image.LANCZOS)
    x = (im.width - an) // 2
    y = (im.height - al) // 2
    img.paste(im.crop((x, y, x + an, y + al)), (x0, y0))


# ── 1 · la tira del Zoom ──────────────────────────────────────────────────
def p1_estuve_ahi():
    img = lienzo(TURQUESA)
    circulos(img, (255, 255, 255), [(950, 170, 210, 12), (110, 1190, 250, 10)])
    poner_isotipo(img, W // 2, 108, 96)
    d = ImageDraw.Draw(img)
    util = W - 2 * MARGEN

    espaciado(d, "NOVIEMBRE 2026 · ENCUENTRO GLOBAL", fuente(SANS_B, 26), 0, 268,
              TURQ_PALIDO, sep=4, centrado_en=W)
    y = parrafo(d, "El MBSR actualizó su currículum.", fuente(SERIF_B, 82),
                MARGEN, 328, util, CREMA, interlinea=1.16, centrado=True)
    # "Estuvimos" y no "Estuve": la placa sale de la cuenta de la institucion
    # y Christian participo como su director. El cuerpo del texto aclara que
    # fue el, para que el plural no sugiera que fueron varios.
    y = parrafo(d, "Estuvimos ahí.", fuente(SERIF_I, 82), MARGEN, y + 8, util,
                CREMA, interlinea=1.16, centrado=True)

    # La tira entra a todo el ancho util, con su proporcion original.
    tira = Image.open(FOTOS_LOCALES / "tira_zoom.jpg").convert("RGB")
    an = util
    al = round(an * tira.height / tira.width)
    img.paste(tira.resize((an, al), Image.LANCZOS), (MARGEN, y + 70))

    parrafo(d, "Brown University School of Professional Studies y el Global "
               "Mindfulness Collaborative presentaron la guía 2026, con Jon "
               "Kabat-Zinn, que creó el programa en 1979.",
            fuente(SANS, 38), MARGEN + 20, y + al + 118, util - 40, CREMA_SUAVE,
            interlinea=1.45, centrado=True)

    total = espaciado(d, "DESLIZÁ", fuente(SANS_B, 32), 0, H - 196, CREMA, sep=6,
                      centrado_en=W - 44)
    flecha(d, (W + total) // 2 - 6, H - 182, CREMA)
    pie(d, CREMA_SUAVE)
    return img.convert("RGB")


# ── 2 · Jon Kabat-Zinn con la guia ────────────────────────────────────────
def p2_la_guia():
    img = lienzo(CREMA)
    # La foto llega hasta 720 y no 810: con 810 el cuerpo de texto terminaba
    # encima del pie.
    _poner(img, "jkz_guia.jpg", (0, 0, W, 720))
    d = ImageDraw.Draw(img)
    util = W - 2 * MARGEN

    espaciado(d, "LA EDICIÓN 2026", fuente(SANS_B, 26), MARGEN, 790, TURQUESA, sep=7)
    d.line([(MARGEN, 846), (MARGEN + 70, 846)], fill=AZUL, width=4)
    y = parrafo(d, "Doscientas treinta y dos páginas.", fuente(SERIF_B, 62),
                MARGEN, 900, util, GRIS_TITULO, interlinea=1.20)
    parrafo(d, "Publicada en octubre de 2026, con revisiones del propio "
               "Kabat-Zinn y aportes de instructores de todo el mundo.",
            fuente(SANS, 40), MARGEN, y + 40, util, GRIS, interlinea=1.46)
    pie(d)
    return img.convert("RGB")


# ── 3 · la linea de tiempo ────────────────────────────────────────────────
def p3_linea_tiempo():
    img = lienzo(CREMA)
    circulos(img, (23, 144, 155), [(1000, 1240, 180, 12), (70, 150, 150, 9)])
    d = ImageDraw.Draw(img)
    util = W - 2 * MARGEN

    espaciado(d, "1979 — 2026", fuente(SANS_B, 28), MARGEN, 160, TURQUESA, sep=8)
    d.line([(MARGEN, 218), (MARGEN + 70, 218)], fill=AZUL, width=4)
    parrafo(d, "De 12 páginas a 232", fuente(SERIF_B, 74), MARGEN, 272, util,
            GRIS_TITULO, interlinea=1.18)
    parrafo(d, "La guía escrita creció. La forma esencial del programa, no.",
            fuente(SANS, 36), MARGEN, 376, util, GRIS, interlinea=1.4)

    HITOS = [
        ("1979", "Jon Kabat-Zinn crea el MBSR", "Sin currículum escrito"),
        ("1993", "Primer currículum escrito", "12 páginas"),
        ("2017", "Guía autorizada de UMass", "65 páginas"),
        ("2025", "Primera edición abierta a la comunidad", "167 páginas"),
        ("2026", "Edición final con aportes internacionales", "232 páginas"),
    ]
    y0, paso = 492, 134
    x_linea = MARGEN + 150
    d.line([(x_linea, y0 - 6), (x_linea, y0 + paso * 4 + 20)],
           fill=(214, 206, 193), width=3)
    f_anio, f_tit, f_pag = fuente(SERIF_B, 46), fuente(SANS_B, 36), fuente(SANS, 34)
    for i, (anio, titulo, paginas) in enumerate(HITOS):
        y = y0 + i * paso
        d.text((MARGEN, y - 8), anio, font=f_anio, fill=GRIS_TITULO)
        d.ellipse([x_linea - 11, y + 6, x_linea + 11, y + 28], fill=TURQUESA)
        d.text((x_linea + 42, y - 4), titulo, font=f_tit, fill=GRIS_TITULO)
        d.text((x_linea + 42, y + 44), paginas, font=f_pag, fill=TURQUESA)
    pie(d)
    return img.convert("RGB")


# ── 4 · las cifras ────────────────────────────────────────────────────────
def p4_cifras():
    img = lienzo(TURQUESA)
    circulos(img, (255, 255, 255), [(140, 210, 230, 11), (960, 1170, 220, 13)])
    poner_isotipo(img, W // 2, 118, 96)
    d = ImageDraw.Draw(img)
    util = W - 2 * MARGEN

    y = parrafo(d, "No la escribió una sola persona", fuente(SERIF_B, 70),
                MARGEN, 300, util, CREMA, interlinea=1.18, centrado=True)
    d.line([(W // 2 - 70, y + 48), (W // 2 + 70, y + 48)], fill=TURQ_PALIDO, width=3)

    CIFRAS = [
        ("50+", "respondentes de la comunidad"),
        ("360+", "aportes únicos: preguntas, sugerencias y reflexiones"),
        ("25", "autores y revisores del currículum"),
    ]
    # La columna del numero arranca en 300 y no en 250: «360+» a 96 pt se
    # montaba encima del texto.
    y = y + 130
    f_num, f_txt = fuente(SERIF_B, 88), fuente(SANS, 38)
    col = 300
    for numero, texto in CIFRAS:
        d.text((MARGEN + 10, y - 12), numero, font=f_num, fill=CREMA)
        parrafo(d, texto, f_txt, MARGEN + col, y + 8, util - col, CREMA_SUAVE,
                interlinea=1.38)
        y += 168

    espaciado(d, "MANY VOICES. SHARED INQUIRY. A LIVING LEGACY.",
              fuente(SANS, 24), 0, y + 10, TURQ_PALIDO, sep=2, centrado_en=W)
    pie(d, CREMA_SUAVE)
    return img.convert("RGB")


# ── 5 · cierre ────────────────────────────────────────────────────────────
def p5_cierre():
    return cierre_cta(
        "El MBSR que damos acá es este",
        "El de la fuente. Y la edición 2026 es pública: cualquiera puede "
        "descargar el currículum completo y comparar con lo que le enseñan.",
        "ESCRIBINOS POR WHATSAPP",
        "MBSR TEACHER CALIFICADO POR EL GMC", claro=True)


def main():
    guardar([
        ("post66_mbsr_1.png", p1_estuve_ahi()),
        ("post66_mbsr_2.png", p2_la_guia()),
        ("post66_mbsr_3.png", p3_linea_tiempo()),
        ("post66_mbsr_4.png", p4_cifras()),
        ("post66_mbsr_5.png", p5_cierre()),
    ], "preview_mbsr2026.jpg", cols=5)


if __name__ == "__main__":
    main()
