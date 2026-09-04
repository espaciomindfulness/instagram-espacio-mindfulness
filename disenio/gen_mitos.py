#!/usr/bin/env python3
"""Genera el carrusel '5 mitos del mindfulness' para @espaciomindfulness.

Paleta tomada del LOGO: turquesa + crema + gris (y el azul del logo solo
para el boton de accion). Formato 1080x1350 (4:5), el que mas pantalla
ocupa en el feed.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
MARGEN = 96

# --- Paleta de marca (muestreada del logo) --------------------------------
TURQUESA = (23, 144, 155)       # #17909B  fondo oscuro (el del logo)
TURQ_CLARO = (91, 191, 193)     # #5BBFC1  acento sobre claro
TURQ_PALIDO = (176, 226, 227)   # version aclarada, legible sobre el turquesa
AZUL = (14, 136, 196)           # #0E88C4  esferas azules del logo -> CTA
GRIS = (90, 103, 112)           # #5A6770  esferas grises -> cuerpo de texto
GRIS_CLARO = (154, 166, 177)    # #9AA6B1
GRIS_TITULO = (42, 52, 60)      # #2A343C  titulares sobre crema
CREMA = (245, 239, 230)         # #F5EFE6
CREMA_SUAVE = (222, 214, 201)
LINEA_CLARA = (223, 214, 202)

F = "C:/Windows/Fonts/"
def fuente(nombre, tam):
    return ImageFont.truetype(F + nombre, tam)

SERIF_B, SERIF_I, SANS, SANS_B = "georgiab.ttf", "georgiai.ttf", "calibri.ttf", "calibrib.ttf"

RAIZ = Path(r"C:/Users/chris/OneDrive/Desktop/IG ESP MIND IA/Instagram")
DESTINO = RAIZ / "contenido" / "originales"
ISOTIPO = Image.open(RAIZ / "contenido" / "marca" / "isotipo.png").convert("RGBA")


def ancho(d, texto, fnt):
    return d.textbbox((0, 0), texto, font=fnt)[2]


def envolver(d, texto, fnt, max_ancho):
    palabras, lineas, actual = texto.split(), [], ""
    for p in palabras:
        prueba = f"{actual} {p}".strip()
        if ancho(d, prueba, fnt) <= max_ancho:
            actual = prueba
        else:
            if actual:
                lineas.append(actual)
            actual = p
    if actual:
        lineas.append(actual)
    return lineas


def parrafo(d, texto, fnt, x, y, max_ancho, color, interlinea=1.42, centrado=False):
    lineas = envolver(d, texto, fnt, max_ancho)
    alto = int(fnt.size * interlinea)
    for i, linea in enumerate(lineas):
        px = x + (max_ancho - ancho(d, linea, fnt)) // 2 if centrado else x
        d.text((px, y + i * alto), linea, font=fnt, fill=color)
    return y + len(lineas) * alto


def espaciado(d, texto, fnt, x, y, color, sep=6, centrado_en=None):
    """Texto con letter-spacing; Pillow no lo trae de fabrica."""
    total = sum(ancho(d, c, fnt) + sep for c in texto) - sep
    px = x if centrado_en is None else (centrado_en - total) // 2
    for c in texto:
        d.text((px, y), c, font=fnt, fill=color)
        px += ancho(d, c, fnt) + sep
    return total


def circulos(img, color, especificaciones):
    capa = Image.new("RGBA", img.size, (0, 0, 0, 0))
    dc = ImageDraw.Draw(capa)
    for cx, cy, r, alfa in especificaciones:
        dc.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color + (alfa,))
    img.alpha_composite(capa)


def poner_isotipo(img, centro_x, y, alto_px):
    iso = ISOTIPO.copy()
    escala = alto_px / iso.height
    iso = iso.resize((int(iso.width * escala), alto_px), Image.LANCZOS)
    img.alpha_composite(iso, (centro_x - iso.width // 2, y))


def flecha(d, x, y, color, escala=1.0):
    s = 18 * escala
    d.polygon([(x, y - s / 2), (x + s * 0.85, y), (x, y + s / 2)], fill=color)


def pie(d, color):
    espaciado(d, "@espaciomindfulness", fuente(SANS, 30), 0, H - 78, color, sep=3, centrado_en=W)


# --------------------------------------------------------------------------
def portada():
    img = Image.new("RGBA", (W, H), TURQUESA)
    circulos(img, (255, 255, 255), [(960, 170, 220, 14), (110, 1190, 270, 11), (900, 1130, 130, 16)])
    poner_isotipo(img, W // 2, 130, 118)
    d = ImageDraw.Draw(img)

    y = 340
    y = parrafo(d, "5 mitos del mindfulness", fuente(SERIF_B, 96), MARGEN, y,
                W - 2 * MARGEN, CREMA, interlinea=1.16, centrado=True)
    y = parrafo(d, "que conviene romper", fuente(SERIF_I, 88), MARGEN, y + 14,
                W - 2 * MARGEN, TURQ_PALIDO, interlinea=1.16, centrado=True)

    d.line([(W // 2 - 90, y + 80), (W // 2 + 90, y + 80)], fill=CREMA_SUAVE, width=3)

    parrafo(d, "Lo que la evidencia dice, y lo que se repite sin chequear.",
            fuente(SANS, 42), MARGEN + 40, y + 150, W - 2 * MARGEN - 80,
            CREMA_SUAVE, interlinea=1.45, centrado=True)

    f = fuente(SANS_B, 34)
    total = espaciado(d, "DESLIZÁ", f, 0, H - 260, CREMA, sep=6, centrado_en=W - 46)
    flecha(d, (W + total) // 2 - 6, H - 245, CREMA)

    pie(d, CREMA_SUAVE)
    return img.convert("RGB")


def placa_mito(numero, mito, realidad):
    img = Image.new("RGBA", (W, H), CREMA)
    circulos(img, (23, 144, 155), [(980, 1240, 190, 14), (60, 120, 150, 11)])
    d = ImageDraw.Draw(img)

    espaciado(d, f"MITO {numero}", fuente(SANS_B, 32), MARGEN, 132, TURQUESA, sep=8)
    d.line([(MARGEN, 196), (MARGEN + 78, 196)], fill=AZUL, width=4)

    # Medimos el bloque entero para centrarlo verticalmente: si no, las placas
    # con texto corto quedan con un aire raro abajo.
    f_mito, f_real = fuente(SERIF_I, 72), fuente(SANS, 46)
    # 16px de colchon: en italica los remates sobresalen del ancho medido
    util = W - 2 * MARGEN - 16
    alto_mito = int(len(envolver(d, f"\u201c{mito}\u201d", f_mito, util)) * f_mito.size * 1.30)
    alto_real = int(len(envolver(d, realidad, f_real, util)) * f_real.size * 1.48)
    alto_total = alto_mito + 76 + 56 + 68 + alto_real

    desde, hasta = 250, H - 190
    y = desde + max(0, (hasta - desde - alto_total) // 2)

    y = parrafo(d, f"\u201c{mito}\u201d", f_mito, MARGEN, y, util, GRIS_TITULO, interlinea=1.30)
    d.line([(MARGEN, y + 76), (W - MARGEN, y + 76)], fill=LINEA_CLARA, width=3)
    espaciado(d, "LA REALIDAD", fuente(SANS_B, 30), MARGEN, y + 132, AZUL, sep=7)
    parrafo(d, realidad, f_real, MARGEN, y + 200, util, GRIS, interlinea=1.48)

    pie(d, GRIS_CLARO)
    return img.convert("RGB")


def cierre():
    img = Image.new("RGBA", (W, H), TURQUESA)
    circulos(img, (255, 255, 255), [(140, 220, 250, 11), (960, 1150, 230, 14)])
    poner_isotipo(img, W // 2, 130, 110)
    d = ImageDraw.Draw(img)

    y = 330
    y = parrafo(d, "¿Y si lo probás en serio?", fuente(SERIF_B, 78), MARGEN, y,
                W - 2 * MARGEN, CREMA, interlinea=1.20, centrado=True)

    d.line([(W // 2 - 70, y + 56), (W // 2 + 70, y + 56)], fill=TURQ_PALIDO, width=3)

    y = parrafo(d,
                "Charla gratuita de 45 minutos: qué es el mindfulness, "
                "qué dice la evidencia y cómo funciona el programa MBSR.",
                fuente(SANS, 44), MARGEN + 20, y + 130, W - 2 * MARGEN - 40,
                CREMA_SUAVE, interlinea=1.50, centrado=True)

    caja_y = y + 100
    d.rounded_rectangle([MARGEN + 60, caja_y, W - MARGEN - 60, caja_y + 130], radius=18, fill=AZUL)
    espaciado(d, "LINK EN LA BIO", fuente(SANS_B, 40), 0, caja_y + 44, (255, 255, 255), sep=7, centrado_en=W)

    espaciado(d, "ACREDITADOS GMC  ·  DESDE 2012  ·  +1000 ALUMNOS",
              fuente(SANS, 27), 0, caja_y + 220, TURQ_PALIDO, sep=3, centrado_en=W)

    pie(d, CREMA_SUAVE)
    return img.convert("RGB")


MITOS = [
    ("Meditar es poner la mente en blanco.",
     "La mente piensa: esa es su función. Mindfulness no es dejar de pensar, "
     "es darte cuenta de que estás pensando y poder elegir dónde ponés la atención."),
    ("Es para relajarse.",
     "La calma suele aparecer, pero como efecto secundario. Lo que entrenás es la "
     "atención, no la relajación. A veces te vas a encontrar con lo incómodo, "
     "y justo ahí está el trabajo."),
    ("Es una práctica religiosa.",
     "El programa MBSR nació en 1979 en la Facultad de Medicina de la Universidad "
     "de Massachusetts, en un contexto hospitalario y laico. Hoy se investiga en "
     "universidades de todo el mundo."),
    ("Hay que meditar una hora por día.",
     "Se empieza con minutos. Lo que sostiene el cambio es la constancia, "
     "no la duración de cada práctica."),
    ("Si tenés ansiedad, no vas a poder.",
     "Es uno de los motivos más frecuentes por los que la gente empieza. "
     "No se medita «bien» cuando ya estás tranquilo: se aprende a estar "
     "con lo que hay."),
]


def main():
    DESTINO.mkdir(parents=True, exist_ok=True)
    placas = [("post2_mitos_1.png", portada())]
    for i, (mito, realidad) in enumerate(MITOS, start=1):
        placas.append((f"post2_mitos_{i + 1}.png", placa_mito(i, mito, realidad)))
    placas.append(("post2_mitos_7.png", cierre()))

    for nombre, img in placas:
        img.save(DESTINO / nombre)
        print("  +", nombre, img.size)

    cols, tw, th = 4, 300, 375
    filas = (len(placas) + cols - 1) // cols
    hoja = Image.new("RGB", (cols * tw, filas * th), "white")
    for i, (_, img) in enumerate(placas):
        mini = img.copy()
        mini.thumbnail((tw - 8, th - 8))
        hoja.paste(mini, ((i % cols) * tw + 4, (i // cols) * th + 4))
    hoja.save("preview_mitos.jpg", quality=90)
    print("preview_mitos.jpg listo")


if __name__ == "__main__":
    main()
