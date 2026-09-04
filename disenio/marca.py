#!/usr/bin/env python3
"""Sistema de diseno de Espacio Mindfulness para las placas de Instagram.

Paleta muestreada del logo real (grilla 3x3 de esferas azul/gris sobre
fondo turquesa). Todo se dibuja a 1080x1350 (4:5), sin escalados intermedios.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1350
MARGEN = 96

TURQUESA = (23, 144, 155)       # #17909B
TURQ_OSCURO = (16, 108, 118)    # sombra del turquesa, para degrades
TURQ_CLARO = (91, 191, 193)     # #5BBFC1
TURQ_PALIDO = (176, 226, 227)
AZUL = (14, 136, 196)           # #0E88C4  esferas azules -> accion
GRIS = (90, 103, 112)           # #5A6770  esferas grises -> cuerpo
GRIS_CLARO = (154, 166, 177)
GRIS_TITULO = (42, 52, 60)
CREMA = (245, 239, 230)         # #F5EFE6
CREMA_SUAVE = (222, 214, 201)
LINEA_CLARA = (223, 214, 202)
BLANCO = (255, 255, 255)
DORADO = (214, 168, 76)         # solo para las estrellas de las resenias

F = "C:/Windows/Fonts/"
SERIF_B, SERIF_I, SERIF, SANS, SANS_B = (
    "georgiab.ttf", "georgiai.ttf", "georgia.ttf", "calibri.ttf", "calibrib.ttf")

RAIZ = Path(r"C:/Users/chris/OneDrive/Desktop/IG ESP MIND IA/Instagram")
DESTINO = RAIZ / "contenido" / "originales"
FOTOS = Path(r"C:/Users/chris/OneDrive/Desktop/TRABAJO/MINDFULNESS/FOTOS/para publi")
ISOTIPO = Image.open(RAIZ / "contenido" / "marca" / "isotipo.png").convert("RGBA")


def fuente(nombre, tam):
    return ImageFont.truetype(F + nombre, tam)


# --- texto ----------------------------------------------------------------

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


def alto_parrafo(d, texto, fnt, max_ancho, interlinea=1.42):
    return int(len(envolver(d, texto, fnt, max_ancho)) * fnt.size * interlinea)


def parrafo(d, texto, fnt, x, y, max_ancho, color, interlinea=1.42, centrado=False):
    lineas = envolver(d, texto, fnt, max_ancho)
    salto = int(fnt.size * interlinea)
    for i, linea in enumerate(lineas):
        px = x + (max_ancho - ancho(d, linea, fnt)) // 2 if centrado else x
        d.text((px, y + i * salto), linea, font=fnt, fill=color)
    return y + len(lineas) * salto


def espaciado(d, texto, fnt, x, y, color, sep=6, centrado_en=None):
    """Letter-spacing manual: Pillow no lo trae."""
    total = sum(ancho(d, c, fnt) + sep for c in texto) - sep
    px = x if centrado_en is None else (centrado_en - total) // 2
    for c in texto:
        d.text((px, y), c, font=fnt, fill=color)
        px += ancho(d, c, fnt) + sep
    return total


# --- elementos graficos ---------------------------------------------------

def circulos(img, color, especificaciones):
    capa = Image.new("RGBA", img.size, (0, 0, 0, 0))
    dc = ImageDraw.Draw(capa)
    for cx, cy, r, alfa in especificaciones:
        dc.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color + (alfa,))
    img.alpha_composite(capa)


def poner_isotipo(img, centro_x, y, alto_px):
    iso = ISOTIPO.copy()
    iso = iso.resize((int(iso.width * alto_px / iso.height), alto_px), Image.LANCZOS)
    img.alpha_composite(iso, (centro_x - iso.width // 2, y))


def flecha(d, x, y, color, escala=1.0):
    s = 18 * escala
    d.polygon([(x, y - s / 2), (x + s * 0.85, y), (x, y + s / 2)], fill=color)


def estrellas(d, x, y, cantidad=5, tam=30, color=DORADO, sep=10):
    """Cinco estrellas de 5 puntas dibujadas a mano (no dependemos de emojis)."""
    import math
    for n in range(cantidad):
        cx = x + n * (tam + sep) + tam / 2
        cy = y + tam / 2
        puntos = []
        for i in range(10):
            radio = tam / 2 if i % 2 == 0 else tam / 4.6
            ang = math.radians(-90 + i * 36)
            puntos.append((cx + radio * math.cos(ang), cy + radio * math.sin(ang)))
        d.polygon(puntos, fill=color)
    return cantidad * (tam + sep) - sep


def foto(nombre, ancho_px, alto_px, foco_x=0.5, foco_y=0.5):
    """Recorta una foto al tamanio pedido cubriendo todo el marco (tipo CSS cover)."""
    im = Image.open(FOTOS / nombre).convert("RGB")
    escala = max(ancho_px / im.width, alto_px / im.height)
    nuevo = (max(1, round(im.width * escala)), max(1, round(im.height * escala)))
    im = im.resize(nuevo, Image.LANCZOS)
    x = int((im.width - ancho_px) * foco_x)
    y = int((im.height - alto_px) * foco_y)
    return im.crop((x, y, x + ancho_px, y + alto_px))


def velo(img, caja, color, alfa_desde, alfa_hasta, vertical=True):
    """Degradado translucido para que el texto se lea sobre la foto."""
    x0, y0, x1, y1 = caja
    an, al = x1 - x0, y1 - y0
    grad = Image.new("L", (1, al) if vertical else (an, 1))
    for i in range(al if vertical else an):
        t = i / max(1, (al if vertical else an) - 1)
        grad.putpixel((0, i) if vertical else (i, 0),
                      int(alfa_desde + (alfa_hasta - alfa_desde) * t))
    grad = grad.resize((an, al))
    capa = Image.new("RGBA", (an, al), color + (0,))
    capa.putalpha(grad)
    img.alpha_composite(capa, (x0, y0))


def caja_translucida(img, caja, color=BLANCO, alfa=30, radio=18):
    """Rectangulo redondeado semitransparente.

    Ojo: dibujar con ImageDraw sobre una imagen RGBA PISA el canal alfa en vez
    de mezclarlo. Hay que dibujar en una capa aparte y componerla.
    """
    capa = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(capa).rounded_rectangle(caja, radius=radio, fill=color + (alfa,))
    img.alpha_composite(capa)


def ancho_estrellas(cantidad=5, tam=30, sep=10):
    return cantidad * (tam + sep) - sep


def pie(d, color=GRIS_CLARO):
    espaciado(d, "@espaciomindfulness", fuente(SANS, 30), 0, H - 78, color, sep=3, centrado_en=W)


def lienzo(fondo):
    return Image.new("RGBA", (W, H), fondo)


def guardar(placas, nombre_preview, cols=4):
    """Guarda los PNG en originales/ y arma una hoja de contacto para revisar."""
    DESTINO.mkdir(parents=True, exist_ok=True)
    for nombre, img in placas:
        img.save(DESTINO / nombre)
        print("  +", nombre, img.size)
    tw, th = 300, 375
    filas = (len(placas) + cols - 1) // cols
    hoja = Image.new("RGB", (cols * tw, filas * th), "white")
    for i, (_, img) in enumerate(placas):
        mini = img.copy()
        mini.thumbnail((tw - 8, th - 8))
        hoja.paste(mini, ((i % cols) * tw + 4, (i // cols) * th + 4))
    # Siempre al lado del generador: si se guarda relativo al cwd, la preview
    # cae en la raiz del repo cuando el script se corre desde afuera y uno
    # termina mirando la version vieja sin darse cuenta.
    salida = Path(__file__).resolve().parent / nombre_preview
    hoja.save(salida, quality=90)
    print("preview:", salida)
