#!/usr/bin/env python3
"""Historia 1080x1920 con los cuatro recuadros del Zoom del encuentro.

Se usan los cuatro y no un recorte de Christian junto a Jon Kabat-Zinn por
dos razones: en la tira estan en los extremos y pegarlos lado a lado seria
rearmar la escena, y ademas la compania suma — Eric Loucks dirige el
Mindfulness Center de Brown y Frances Saadeh expuso por el GMC.

Se acomodan en 2x2 para que las caras entren grandes: la tira original mide
215 px de alto, asi que estirada a todo el ancho quedaria diminuta.

El contenido se mantiene dentro de la zona segura (y 260 a 1660): Instagram
tapa el borde superior con el avatar y el inferior con la barra de responder.

Privacidad: la tira solo contiene expositores y Christian. No hay panel de
chat, lista de asistentes ni burbujas de reaccion con nombres.
"""
from PIL import Image, ImageDraw

from piezas import *

AN, AL = 1080, 1920
CAPTURA = (RAIZ.parent / "POSTEO - MBSR curriculum 2026" / "captura original.jpg")
# La fila de participantes dentro de la captura de 1996x1450.
TIRA = (337, 0, 1755, 215)


def recuadros():
    """Los cuatro recuadros, cortados de la tira en partes iguales."""
    im = Image.open(CAPTURA).convert("RGB").crop(TIRA)
    paso = im.width / 4
    return [im.crop((round(i * paso), 0, round((i + 1) * paso), im.height))
            for i in range(4)]


def historia():
    img = Image.new("RGB", (AN, AL), TURQUESA)
    capa = Image.new("RGBA", (AN, AL), (0, 0, 0, 0))
    dc = ImageDraw.Draw(capa)
    for cx, cy, r, a in [(900, 300, 280, 12), (150, 1600, 320, 10)]:
        dc.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255, a))
    img = Image.alpha_composite(img.convert("RGBA"), capa).convert("RGB")
    d = ImageDraw.Draw(img)
    util = AN - 2 * MARGEN

    espaciado(d, "12 DE NOVIEMBRE DE 2026", fuente(SANS_B, 30), 0, 330,
              TURQ_PALIDO, sep=6, centrado_en=AN)
    y = parrafo(d, "El MBSR presentó su currículum 2026.", fuente(SERIF_B, 78),
                MARGEN, 400, util, CREMA, interlinea=1.16, centrado=True)
    y = parrafo(d, "Estuvimos ahí.", fuente(SERIF_I, 78), MARGEN, y + 6, util,
                CREMA, interlinea=1.16, centrado=True)

    # Los cuatro en 2x2, con un hilo de aire entre ellos.
    tiles = recuadros()
    hueco = 14
    ancho = (util - hueco) // 2
    alto = round(ancho * tiles[0].height / tiles[0].width)
    y0 = y + 90
    for i, t in enumerate(tiles):
        x = MARGEN + (i % 2) * (ancho + hueco)
        yy = y0 + (i // 2) * (alto + hueco)
        img.paste(t.resize((ancho, alto), Image.LANCZOS), (x, yy))

    pie_y = y0 + 2 * alto + hueco + 90
    parrafo(d, "Brown University School of Professional Studies y el Global "
               "Mindfulness Collaborative presentaron la guía 2026, con Jon "
               "Kabat-Zinn.",
            fuente(SANS, 38), MARGEN + 20, pie_y, util - 40, CREMA_SUAVE,
            interlinea=1.45, centrado=True)
    espaciado(d, "@espaciomindfulness  ·  @chris.mind2", fuente(SANS, 28), 0,
              1620, TURQ_PALIDO, sep=2, centrado_en=AN)
    return img


def main():
    salida = RAIZ / "contenido" / "originales" / "historia_encuentro.png"
    historia().save(salida)
    print("  +", salida.name, Image.open(salida).size)


if __name__ == "__main__":
    main()
