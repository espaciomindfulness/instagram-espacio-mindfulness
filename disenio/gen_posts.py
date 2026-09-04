#!/usr/bin/env python3
"""Genera las placas de los posts 4, 5, 7, 8 y 9 de @espaciomindfulness."""
from PIL import ImageDraw
from marca import *   # sistema de diseno de la marca


# ==========================================================================
# POST 4 — Testimonio real de Google (imagen suelta)
# ==========================================================================
def post4_testimonio():
    ALTO_FOTO = 516
    img = lienzo(CREMA)
    img.paste(foto("IMG_5816.JPG", W, ALTO_FOTO, foco_y=0.42).convert("RGBA"), (0, 0))
    velo(img, (0, 0, W, 240), TURQ_OSCURO, 190, 0)   # para que se lea el isotipo
    circulos(img, (23, 144, 155), [(1010, 1240, 190, 12)])
    poner_isotipo(img, W // 2, 44, 78)
    d = ImageDraw.Draw(img)

    y = ALTO_FOTO + 74
    estrellas(d, (W - ancho_estrellas(5, 34, 11)) // 2, y, tam=34, sep=11)

    util = W - 2 * MARGEN - 16
    y = parrafo(d, "“No salís igual de cómo entraste.”", fuente(SERIF_I, 62),
                MARGEN, y + 84, util, GRIS_TITULO, interlinea=1.30, centrado=True)

    y = parrafo(d, "Un grupo humano hermoso. Lo recomiendo desde el día 1 hasta el último.",
                fuente(SANS, 42), MARGEN + 20, y + 34, util - 40, GRIS,
                interlinea=1.46, centrado=True)

    d.line([(W // 2 - 60, y + 52), (W // 2 + 60, y + 52)], fill=LINEA_CLARA, width=3)
    espaciado(d, "SU VÁZQUEZ SANZ", fuente(SANS_B, 32), 0, y + 96, TURQUESA, sep=6, centrado_en=W)
    espaciado(d, "RESEÑA VERIFICADA EN GOOGLE  ·  4.9 DE 5  ·  40 RESEÑAS",
              fuente(SANS, 26), 0, y + 148, GRIS_CLARO, sep=2, centrado_en=W)

    pie(d)
    return img.convert("RGB")


# ==========================================================================
# POST 5 — Carrusel: que es el MBSR
# ==========================================================================
def p5_portada():
    img = lienzo(TURQUESA)
    img.paste(foto("IMG_5699.JPG", W, H, foco_y=0.45).convert("RGBA"), (0, 0))
    velo(img, (0, 0, W, H), TURQ_OSCURO, 226, 244)
    circulos(img, (255, 255, 255), [(950, 1160, 210, 12)])
    poner_isotipo(img, W // 2, 140, 118)
    d = ImageDraw.Draw(img)

    y = 400
    y = parrafo(d, "Qué es el MBSR", fuente(SERIF_B, 104), MARGEN, y,
                W - 2 * MARGEN, CREMA, interlinea=1.16, centrado=True)
    y = parrafo(d, "y para quién es", fuente(SERIF_I, 86), MARGEN, y + 10,
                W - 2 * MARGEN, TURQ_PALIDO, interlinea=1.16, centrado=True)

    d.line([(W // 2 - 90, y + 76), (W // 2 + 90, y + 76)], fill=CREMA_SUAVE, width=3)
    parrafo(d, "El programa de mindfulness con más respaldo científico del mundo.",
            fuente(SANS, 42), MARGEN + 40, y + 142, W - 2 * MARGEN - 80,
            CREMA_SUAVE, interlinea=1.45, centrado=True)

    f = fuente(SANS_B, 34)
    total = espaciado(d, "DESLIZÁ", f, 0, H - 250, CREMA, sep=6, centrado_en=W - 46)
    flecha(d, (W + total) // 2 - 6, H - 235, CREMA)
    pie(d, CREMA_SUAVE)
    return img.convert("RGB")


def p5_dato(etiqueta, titulo, cuerpo, foto_nombre=None, foco_y=0.5):
    img = lienzo(CREMA)
    alto_foto = 0
    if foto_nombre:
        alto_foto = 470
        img.paste(foto(foto_nombre, W, alto_foto, foco_y=foco_y).convert("RGBA"), (0, 0))
    circulos(img, (23, 144, 155), [(60, 1250, 170, 12), (1010, 700, 130, 10)])
    d = ImageDraw.Draw(img)

    y = alto_foto + (120 if foto_nombre else 150)
    espaciado(d, etiqueta, fuente(SANS_B, 32), MARGEN, y, TURQUESA, sep=8)
    d.line([(MARGEN, y + 64), (MARGEN + 78, y + 64)], fill=AZUL, width=4)

    util = W - 2 * MARGEN - 16
    y = parrafo(d, titulo, fuente(SERIF_B, 66), MARGEN, y + 122, util,
                GRIS_TITULO, interlinea=1.24)
    parrafo(d, cuerpo, fuente(SANS, 45), MARGEN, y + 54, util, GRIS, interlinea=1.48)

    pie(d)
    return img.convert("RGB")


def p5_cierre():
    img = lienzo(TURQUESA)
    circulos(img, (255, 255, 255), [(150, 240, 240, 11), (960, 1150, 230, 14)])
    poner_isotipo(img, W // 2, 120, 104)
    d = ImageDraw.Draw(img)

    y = 300
    y = parrafo(d, "Próximas cohortes", fuente(SERIF_B, 78), MARGEN, y,
                W - 2 * MARGEN, CREMA, interlinea=1.20, centrado=True)
    d.line([(W // 2 - 70, y + 52), (W // 2 + 70, y + 52)], fill=TURQ_PALIDO, width=3)

    y += 116
    for titulo, detalle in (
        ("13 de agosto · Online", "Jueves de 19 a 21 h"),
        ("16 de octubre · Presencial", "Viernes de 19 a 21 h · Villa Urquiza"),
    ):
        caja_translucida(img, [MARGEN, y, W - MARGEN, y + 152], alfa=34)
        d2 = ImageDraw.Draw(img)
        parrafo(d2, titulo, fuente(SANS_B, 46), MARGEN + 44, y + 30,
                W - 2 * MARGEN - 88, CREMA, interlinea=1.2)
        parrafo(d2, detalle, fuente(SANS, 36), MARGEN + 44, y + 88,
                W - 2 * MARGEN - 88, TURQ_PALIDO, interlinea=1.2)
        y += 182

    d = ImageDraw.Draw(img)
    parrafo(d, "8 semanas · 2 h por encuentro · un retiro de día completo",
            fuente(SANS, 36), MARGEN, y + 20, W - 2 * MARGEN, TURQ_PALIDO,
            interlinea=1.4, centrado=True)

    caja_y = y + 116
    d.rounded_rectangle([MARGEN + 60, caja_y, W - MARGEN - 60, caja_y + 126], radius=18, fill=AZUL)
    espaciado(d, "ESCRIBINOS POR WHATSAPP", fuente(SANS_B, 34), 0, caja_y + 44,
              BLANCO, sep=4, centrado_en=W)

    pie(d, CREMA_SUAVE)
    return img.convert("RGB")


def post5_mbsr():
    return [
        ("post5_mbsr_1.png", p5_portada()),
        ("post5_mbsr_2.png", p5_dato(
            "QUÉ ES",
            "Un programa de 8 semanas, no una clase suelta.",
            "Nació en 1979 en la Facultad de Medicina de la Universidad de "
            "Massachusetts. Es el protocolo de mindfulness más estudiado que existe.",
            "IMG_5777.JPG", 0.42)),
        ("post5_mbsr_3.png", p5_dato(
            "CÓMO SE CURSA",
            "Un encuentro semanal de dos horas.",
            "Prácticas guiadas, material para llevarte a casa y un retiro de día "
            "completo sobre el final del programa. Online o presencial.",
            "IMG_5758.JPG", 0.45)),
        ("post5_mbsr_4.png", p5_dato(
            "PARA QUIÉN ES",
            "Para el que llega cansado de su propia cabeza.",
            "Estrés sostenido, ansiedad, insomnio, rumiación, dolor crónico. "
            "También para profesionales de la salud que quieren incorporarlo "
            "a su práctica. No hace falta experiencia previa.")),
        ("post5_mbsr_5.png", p5_dato(
            "QUÉ NO ES",
            "No es una religión ni un curso de relajación.",
            "Es entrenamiento de la atención, con base científica y lenguaje laico. "
            "Y no reemplaza un tratamiento médico o psicológico: lo complementa.")),
        ("post5_mbsr_6.png", p5_cierre()),
    ]


# ==========================================================================
# POST 7 — Autoridad (imagen suelta)
# ==========================================================================
def post7_autoridad():
    img = lienzo(TURQUESA)
    fondo = foto("IMG_5705.JPG", W, H, foco_y=0.40).filter(ImageFilter.GaussianBlur(7))
    img.paste(fondo.convert("RGBA"), (0, 0))
    velo(img, (0, 0, W, H), TURQ_OSCURO, 232, 252)
    poner_isotipo(img, W // 2, 120, 112)
    d = ImageDraw.Draw(img)

    y = 330
    y = parrafo(d, "Desde 2012 enseñando mindfulness",
                fuente(SERIF_B, 82), MARGEN, y, W - 2 * MARGEN, CREMA,
                interlinea=1.20, centrado=True)
    y = parrafo(d, "con base científica", fuente(SERIF_I, 74), MARGEN, y + 8,
                W - 2 * MARGEN, TURQ_PALIDO, interlinea=1.20, centrado=True)

    d.line([(W // 2 - 80, y + 66), (W // 2 + 80, y + 66)], fill=CREMA_SUAVE, width=3)

    y += 140
    for numero, texto in (("+1000", "personas formadas"),
                          ("40+", "empresas acompañadas"),
                          ("13", "años de trayectoria")):
        f_num = fuente(SERIF_B, 60)
        an = ancho(d, numero, f_num)
        f_txt = fuente(SANS, 40)
        an_txt = ancho(d, texto, f_txt)
        total = an + 24 + an_txt
        x = (W - total) // 2
        d.text((x, y), numero, font=f_num, fill=CREMA)
        d.text((x + an + 24, y + 18), texto, font=f_txt, fill=TURQ_PALIDO)
        y += 96

    espaciado(d, "ACREDITADOS POR GLOBAL MINDFULNESS COLLABORATIVE",
              fuente(SANS_B, 27), 0, y + 46, CREMA, sep=3, centrado_en=W)
    pie(d, CREMA_SUAVE)
    return img.convert("RGB")


# ==========================================================================
# POST 8 — Carrusel: que dice la evidencia
# ==========================================================================
def p8_portada():
    # Portada clara: en la grilla del perfil rompe la seguidilla de turquesas.
    img = lienzo(CREMA)
    circulos(img, (23, 144, 155), [(940, 190, 230, 13), (120, 1180, 260, 11)])
    poner_isotipo(img, W // 2, 130, 118)
    d = ImageDraw.Draw(img)

    y = 350
    y = parrafo(d, "Qué cambia en 8 semanas", fuente(SERIF_B, 92), MARGEN, y,
                W - 2 * MARGEN, GRIS_TITULO, interlinea=1.18, centrado=True)
    y = parrafo(d, "según la evidencia", fuente(SERIF_I, 82), MARGEN, y + 12,
                W - 2 * MARGEN, TURQUESA, interlinea=1.18, centrado=True)

    d.line([(W // 2 - 90, y + 76), (W // 2 + 90, y + 76)], fill=LINEA_CLARA, width=3)
    parrafo(d, "Cinco efectos que la investigación asocia al programa MBSR. "
               "Sin exagerar nada.",
            fuente(SANS, 42), MARGEN + 40, y + 142, W - 2 * MARGEN - 80,
            GRIS, interlinea=1.45, centrado=True)

    f = fuente(SANS_B, 34)
    total = espaciado(d, "DESLIZÁ", f, 0, H - 250, TURQUESA, sep=6, centrado_en=W - 46)
    flecha(d, (W + total) // 2 - 6, H - 235, TURQUESA)
    pie(d, GRIS_CLARO)
    return img.convert("RGB")


def p8_hallazgo(numero, titulo, cuerpo):
    img = lienzo(CREMA)
    circulos(img, (23, 144, 155), [(1000, 1230, 190, 13), (70, 140, 160, 10)])
    d = ImageDraw.Draw(img)

    # numero grande de fondo, marca de agua
    f_num = fuente(SERIF_B, 260)
    d.text((MARGEN - 12, 150), str(numero), font=f_num, fill=(23, 144, 155, 255))
    img_capa = None

    util = W - 2 * MARGEN - 16
    f_tit, f_cue = fuente(SERIF_B, 64), fuente(SANS, 45)
    alto_t = alto_parrafo(d, titulo, f_tit, util, 1.24)
    alto_c = alto_parrafo(d, cuerpo, f_cue, util, 1.48)
    total = alto_t + 58 + alto_c
    y = 470 + max(0, (H - 210 - 470 - total) // 2)

    y = parrafo(d, titulo, f_tit, MARGEN, y, util, GRIS_TITULO, interlinea=1.24)
    parrafo(d, cuerpo, f_cue, MARGEN, y + 58, util, GRIS, interlinea=1.48)

    pie(d)
    return img.convert("RGB")


def p8_cierre():
    img = lienzo(TURQUESA)
    circulos(img, (255, 255, 255), [(140, 230, 240, 11), (960, 1150, 230, 14)])
    poner_isotipo(img, W // 2, 130, 108)
    d = ImageDraw.Draw(img)

    y = 330
    y = parrafo(d, "Con una aclaración importante", fuente(SERIF_B, 70), MARGEN, y,
                W - 2 * MARGEN, CREMA, interlinea=1.22, centrado=True)
    d.line([(W // 2 - 70, y + 54), (W // 2 + 70, y + 54)], fill=TURQ_PALIDO, width=3)

    y = parrafo(d,
                "El mindfulness no cura ni reemplaza un tratamiento médico o "
                "psicológico. Es una herramienta que suma, y que funciona mejor "
                "cuando se aprende bien acompañado.",
                fuente(SANS, 44), MARGEN + 20, y + 124, W - 2 * MARGEN - 40,
                CREMA_SUAVE, interlinea=1.50, centrado=True)

    caja_y = y + 110
    d.rounded_rectangle([MARGEN + 60, caja_y, W - MARGEN - 60, caja_y + 126], radius=18, fill=AZUL)
    espaciado(d, "CHARLA GRATUITA · LINK EN BIO", fuente(SANS_B, 32), 0, caja_y + 44,
              BLANCO, sep=4, centrado_en=W)
    pie(d, CREMA_SUAVE)
    return img.convert("RGB")


HALLAZGOS = [
    ("Baja el estrés percibido",
     "Es el efecto más replicado: los meta-análisis muestran reducciones "
     "consistentes en las escalas de estrés después de completar el programa."),
    ("Mejora la ansiedad y el ánimo",
     "La investigación reporta mejoras de magnitud moderada en síntomas de "
     "ansiedad y depresión, sostenidas en los seguimientos."),
    ("Se duerme mejor",
     "Muchos participantes reportan mejor calidad de sueño. Suele ser de los "
     "primeros cambios que la gente nota, y no es casualidad: baja la rumiación "
     "nocturna."),
    ("Menos piloto automático",
     "Entrenás la capacidad de darte cuenta de dónde está tu atención. "
     "Eso cambia la relación con los pensamientos: dejás de creerles todo."),
    ("Otra relación con el dolor",
     "Para esto nació el MBSR en 1979: pacientes con dolor crónico que no "
     "respondían a otros tratamientos. La intensidad puede no bajar; el "
     "sufrimiento alrededor, sí."),
]


def post8_evidencia():
    placas = [("post8_evidencia_1.png", p8_portada())]
    for i, (titulo, cuerpo) in enumerate(HALLAZGOS, start=1):
        placas.append((f"post8_evidencia_{i + 1}.png", p8_hallazgo(i, titulo, cuerpo)))
    placas.append(("post8_evidencia_7.png", p8_cierre()))
    return placas


# ==========================================================================
# POST 9 — Ultima llamada (imagen suelta)
# ==========================================================================
def post9_ultima():
    img = lienzo(TURQUESA)
    circulos(img, (255, 255, 255), [(950, 200, 240, 12), (110, 1200, 260, 10)])
    poner_isotipo(img, W // 2, 118, 108)
    d = ImageDraw.Draw(img)

    y = 260
    espaciado(d, "EMPIEZA ESTA SEMANA", fuente(SANS_B, 34), 0, y, TURQ_PALIDO, sep=8, centrado_en=W)

    y = parrafo(d, "MBSR · Reducción de estrés en 8 semanas",
                fuente(SERIF_B, 74), MARGEN, y + 72, W - 2 * MARGEN, CREMA,
                interlinea=1.22, centrado=True)

    d.line([(W // 2 - 80, y + 60), (W // 2 + 80, y + 60)], fill=TURQ_PALIDO, width=3)

    y += 120
    for titulo, detalle in (
        ("Jueves 13/08 · Online", "de 19 a 21 h"),
        ("Presencial · próxima cohorte", "Viernes 16/10 · Villa Urquiza"),
    ):
        caja_translucida(img, [MARGEN, y, W - MARGEN, y + 140], alfa=34)
        dd = ImageDraw.Draw(img)
        parrafo(dd, titulo, fuente(SANS_B, 46), MARGEN + 44, y + 28, W - 2 * MARGEN - 88, CREMA)
        parrafo(dd, detalle, fuente(SANS, 36), MARGEN + 44, y + 86, W - 2 * MARGEN - 88, TURQ_PALIDO)
        y += 166

    d = ImageDraw.Draw(img)
    caja_y = y + 30
    d.rounded_rectangle([MARGEN + 60, caja_y, W - MARGEN - 60, caja_y + 126], radius=18, fill=AZUL)
    espaciado(d, "CONSULTÁ POR WHATSAPP", fuente(SANS_B, 34), 0, caja_y + 44,
              BLANCO, sep=4, centrado_en=W)

    espaciado(d, "MODALIDAD ONLINE  ·  ACREDITADOS GMC", fuente(SANS, 27), 0,
              caja_y + 150, TURQ_PALIDO, sep=3, centrado_en=W)
    pie(d, CREMA_SUAVE)
    return img.convert("RGB")


def main():
    todas = []
    todas.append(("post4_testimonio.png", post4_testimonio()))
    todas += post5_mbsr()
    todas.append(("post7_autoridad.png", post7_autoridad()))
    todas += post8_evidencia()
    todas.append(("post9_ultima_llamada.png", post9_ultima()))
    guardar(todas, "preview_resto.jpg", cols=4)


if __name__ == "__main__":
    main()
