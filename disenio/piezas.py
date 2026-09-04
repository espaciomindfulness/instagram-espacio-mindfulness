#!/usr/bin/env python3
"""Piezas reutilizables de las placas de @espaciomindfulness.

Vive dentro del repo a proposito: la version anterior estaba en una carpeta
temporal y se perdio entera. Todo lo necesario para regenerar placas tiene
que estar aca.

Reglas de la marca que estan metidas en estas funciones:
  - Formato 1080x1350 (4:5), sin escalados intermedios.
  - Los fondos alternan turquesa y crema post a post: la grilla del perfil
    solo muestra la primera placa de cada publicacion, y si todas son del
    mismo color el perfil se ve plano.
  - El azul del logo se reserva para los botones. Si se usa en todos lados
    pierde fuerza.
  - Nunca precios: los montos van por WhatsApp (regla del cliente).
"""
from PIL import ImageDraw, ImageFilter
from marca import *


def cubierta(titulo, subtitulo, bajada, foto_nombre=None, foco_y=0.45, claro=False):
    """Portada de carrusel. claro=True la hace crema en vez de turquesa.

    Con foto el modo claro se ignora: la foto va con un velo oscuro encima,
    asi que el texto tiene que ser claro si o si. Dejarlo en oscuro lo volvia
    ilegible.
    """
    if foto_nombre:
        claro = False
    fondo = CREMA if claro else TURQUESA
    c_tit = GRIS_TITULO if claro else CREMA
    c_sub = TURQUESA if claro else TURQ_PALIDO
    c_linea = LINEA_CLARA if claro else CREMA_SUAVE
    c_bajada = GRIS if claro else CREMA_SUAVE
    c_acento = TURQUESA if claro else CREMA
    c_pie = GRIS_CLARO if claro else CREMA_SUAVE

    img = lienzo(fondo)
    if foto_nombre:
        img.paste(foto(foto_nombre, W, H, foco_y=foco_y)
                  .filter(ImageFilter.GaussianBlur(5)).convert("RGBA"), (0, 0))
        velo(img, (0, 0, W, H), TURQ_OSCURO, 228, 246)
    circulos(img, (23, 144, 155) if claro else (255, 255, 255),
             [(950, 180, 220, 13), (110, 1180, 260, 11)])
    poner_isotipo(img, W // 2, 132, 116)
    d = ImageDraw.Draw(img)

    util = W - 2 * MARGEN
    f_tit = fuente(SERIF_B, 92 if len(titulo) < 30 else 78)
    y = parrafo(d, titulo, f_tit, MARGEN, 360, util, c_tit, interlinea=1.18, centrado=True)
    y = parrafo(d, subtitulo, fuente(SERIF_I, 80), MARGEN, y + 12, util, c_sub,
                interlinea=1.18, centrado=True)
    d.line([(W // 2 - 90, y + 76), (W // 2 + 90, y + 76)], fill=c_linea, width=3)
    parrafo(d, bajada, fuente(SANS, 42), MARGEN + 40, y + 142, util - 80, c_bajada,
            interlinea=1.45, centrado=True)

    total = espaciado(d, "DESLIZÁ", fuente(SANS_B, 34), 0, H - 250, c_acento, sep=6,
                      centrado_en=W - 46)
    flecha(d, (W + total) // 2 - 6, H - 235, c_acento)
    pie(d, c_pie)
    return img.convert("RGB")


def punto(etiqueta, titulo, cuerpo, numero=None):
    """Placa interior de carrusel: numero grande o etiqueta, titulo y cuerpo."""
    img = lienzo(CREMA)
    circulos(img, (23, 144, 155), [(1000, 1230, 190, 13), (70, 140, 160, 10)])
    d = ImageDraw.Draw(img)

    if numero is not None:
        d.text((MARGEN - 12, 150), str(numero), font=fuente(SERIF_B, 260), fill=TURQUESA)
        arranque = 470
    else:
        espaciado(d, etiqueta, fuente(SANS_B, 32), MARGEN, 150, TURQUESA, sep=8)
        d.line([(MARGEN, 214), (MARGEN + 78, 214)], fill=AZUL, width=4)
        arranque = 290

    util = W - 2 * MARGEN - 16
    f_t, f_c = fuente(SERIF_B, 64), fuente(SANS, 45)
    alto = alto_parrafo(d, titulo, f_t, util, 1.24) + 58 + alto_parrafo(d, cuerpo, f_c, util, 1.48)
    y = arranque + max(0, (H - 210 - arranque - alto) // 2)
    y = parrafo(d, titulo, f_t, MARGEN, y, util, GRIS_TITULO, interlinea=1.24)
    parrafo(d, cuerpo, f_c, MARGEN, y + 58, util, GRIS, interlinea=1.48)
    pie(d)
    return img.convert("RGB")


def cierre_cta(titulo, cuerpo, boton, remate=None, claro=False):
    """Ultima placa del carrusel: la llamada a la accion."""
    fondo = CREMA if claro else TURQUESA
    c_tit = GRIS_TITULO if claro else CREMA
    c_linea = LINEA_CLARA if claro else TURQ_PALIDO
    c_cuerpo = GRIS if claro else CREMA_SUAVE
    c_pie = GRIS_CLARO if claro else CREMA_SUAVE

    img = lienzo(fondo)
    circulos(img, (23, 144, 155) if claro else (255, 255, 255),
             [(140, 230, 240, 11), (960, 1150, 230, 14)])
    poner_isotipo(img, W // 2, 130, 108)
    d = ImageDraw.Draw(img)

    util = W - 2 * MARGEN
    y = parrafo(d, titulo, fuente(SERIF_B, 74), MARGEN, 330, util, c_tit,
                interlinea=1.22, centrado=True)
    d.line([(W // 2 - 70, y + 54), (W // 2 + 70, y + 54)], fill=c_linea, width=3)
    y = parrafo(d, cuerpo, fuente(SANS, 44), MARGEN + 20, y + 124, util - 40, c_cuerpo,
                interlinea=1.50, centrado=True)

    caja_y = y + 100
    d.rounded_rectangle([MARGEN + 60, caja_y, W - MARGEN - 60, caja_y + 126], radius=18, fill=AZUL)
    espaciado(d, boton, fuente(SANS_B, 34 if len(boton) < 26 else 30), 0, caja_y + 44,
              (255, 255, 255), sep=4, centrado_en=W)
    if remate:
        espaciado(d, remate, fuente(SANS, 27), 0, caja_y + 176,
                  TURQUESA if claro else TURQ_PALIDO, sep=3, centrado_en=W)
    pie(d, c_pie)
    return img.convert("RGB")


def frase(texto, autor, fuente_texto, claro=False):
    """Placa de cita, con comillas grandes y atribucion."""
    c_texto = GRIS_TITULO if claro else CREMA
    c_comilla = (222, 214, 201) if claro else (255, 255, 255)
    c_linea = LINEA_CLARA if claro else TURQ_PALIDO
    c_autor = TURQUESA if claro else CREMA
    c_fuente = GRIS_CLARO if claro else TURQ_PALIDO

    img = lienzo(CREMA if claro else TURQUESA)
    circulos(img, (23, 144, 155) if claro else (255, 255, 255),
             [(920, 250, 250, 12), (150, 1160, 240, 10)])
    poner_isotipo(img, W // 2, 120, 100)
    d = ImageDraw.Draw(img)

    d.text((MARGEN - 20, 250), "“", font=fuente(SERIF_B, 240), fill=c_comilla)
    util = W - 2 * MARGEN - 16
    f = fuente(SERIF_I, 76)
    alto = alto_parrafo(d, texto, f, util, 1.34)
    y = 430 + max(0, (980 - 430 - alto) // 2)
    y = parrafo(d, texto, f, MARGEN, y, util, c_texto, interlinea=1.34, centrado=True)

    d.line([(W // 2 - 60, y + 70), (W // 2 + 60, y + 70)], fill=c_linea, width=3)
    espaciado(d, autor.upper(), fuente(SANS_B, 32), 0, y + 116, c_autor, sep=6, centrado_en=W)
    espaciado(d, fuente_texto.upper(), fuente(SANS, 26), 0, y + 168, c_fuente, sep=3, centrado_en=W)
    pie(d, GRIS_CLARO if claro else CREMA_SUAVE)
    return img.convert("RGB")


def texto_suelto(etiqueta, titulo, cuerpo, remate=None, claro=True):
    """Placa de un solo golpe: etiqueta, titular grande y bajada."""
    fondo = CREMA if claro else TURQUESA
    c_tit = GRIS_TITULO if claro else CREMA
    c_etq = TURQUESA if claro else TURQ_PALIDO
    c_linea = LINEA_CLARA if claro else TURQ_PALIDO
    c_cuerpo = GRIS if claro else CREMA_SUAVE

    img = lienzo(fondo)
    circulos(img, (23, 144, 155) if claro else (255, 255, 255),
             [(980, 240, 240, 11), (90, 1180, 250, 12)])
    poner_isotipo(img, W // 2, 120, 100)
    d = ImageDraw.Draw(img)

    util = W - 2 * MARGEN - 16
    espaciado(d, etiqueta, fuente(SANS_B, 30), 0, 300, c_etq, sep=7, centrado_en=W)
    f_t = fuente(SERIF_B, 76 if len(titulo) < 44 else 64)
    y = parrafo(d, titulo, f_t, MARGEN, 372, util, c_tit, interlinea=1.22, centrado=True)
    d.line([(W // 2 - 70, y + 54), (W // 2 + 70, y + 54)], fill=c_linea, width=3)
    y = parrafo(d, cuerpo, fuente(SANS, 44), MARGEN + 10, y + 124, util - 20, c_cuerpo,
                interlinea=1.50, centrado=True)
    if remate:
        espaciado(d, remate, fuente(SANS_B, 28), 0, y + 70, c_etq, sep=5, centrado_en=W)
    pie(d, GRIS_CLARO if claro else CREMA_SUAVE)
    return img.convert("RGB")
