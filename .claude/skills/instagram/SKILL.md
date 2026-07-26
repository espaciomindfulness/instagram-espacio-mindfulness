---
name: instagram
description: Gestiona el pipeline de publicación automática de Instagram de Espacio Mindfulness — crear posts nuevos respetando la identidad visual, programarlos en el calendario, preparar imágenes, validar y revisar el estado. Usar cuando el usuario pida crear/programar/reprogramar posts, revisar qué se publicó, o agregar contenido al feed o Reels.
---

# Instagram — Espacio Mindfulness

Pipeline de publicación automática. Las imágenes viven en el repo, un
workflow de GitHub Actions corre cada 30 min y publica vía la Instagram
API con Login de Instagram (host `graph.instagram.com`, SIN página de
Facebook) lo que esté vencido en `contenido/calendario.json`.

## Estructura

```
Instagram/
├── contenido/
│   ├── originales/     # diseños fuente (PNG 1080x1080)
│   ├── publicar/       # JPEG listos para la API (generados, no editar a mano)
│   └── calendario.json # programación + estado de cada post
├── scripts/
│   ├── preparar_imagenes.py  # PNG → JPEG válido para Instagram
│   ├── validar.py            # chequea calendario + archivos antes de publicar
│   ├── publicar.py           # lo ejecuta GitHub Actions, no correr a mano
│   ├── obtener_token.py      # setup inicial de credenciales (una vez)
│   └── refrescar_token.py    # renueva el token de 60 días (workflow semanal)
└── .github/workflows/
    ├── publicar.yml          # cron cada 30 min: publica lo que está vencido
    └── refrescar_token.yml   # cron semanal: renueva el token solo
```

## Identidad visual (respetar SIEMPRE al crear imágenes)

Formato: 1080x1080 px. Fondo degradado vertical suave. Ornamento
circular/flor de puntos blancos arriba del texto. Tipografía serif,
frase principal en bold, subtítulo en itálica, línea divisoria fina,
"Espacio Mindfulness" en itálica pequeña, "@espaciomindfulness"
semitransparente al pie. Círculos decorativos translúcidos en esquinas.

Paletas por tipo de contenido (degradado arriba → abajo):
| Tipo                | Colores                          |
|---------------------|----------------------------------|
| Frase inspiradora   | verde agua `#1B8A8A` → crema `#F3EADF` |
| Tip práctico        | celeste `#C8DCE8` → blanco → `#E5EFF7` |
| Dato científico     | lavanda `#AFA0D2` → blanco → `#DBD3ED` |
| Frase amorosa       | durazno `#E8C4B8` → `#F7E5D1`    |
| Educativo/listas    | verde `#5A9E91` → `#8BBDA9`      |
| Empresarial         | azul noche `#2A3C5A` → `#4A5E7C`, texto blanco |
| Cierre de semana    | terracota `#E19B72` → `#B4766B`  |

Texto blanco sobre fondos saturados; gris oscuro `#3A4A48` sobre fondos claros.

## Reglas de captions

- Español rioplatense (vos: "respirá", "contanos", "guardá").
- Estructura: gancho corto + desarrollo 2-3 párrafos + llamada a la acción
  (pregunta, "guardá este post", "etiquetá a alguien") + bloque de hashtags.
- 7-9 hashtags, siempre incluir `#EspacioMindfulness` al final. Máx 30.
- Máx 2200 caracteres (lo valida `validar.py`).
- Emojis con moderación: 🌿🧘💛✨🤍 acordes a la marca.

## Flujo: agregar un post nuevo

1. Crear el diseño (PNG 1080x1080, paleta según tipo) en `contenido/originales/`.
   Generarlo con Pillow siguiendo la identidad visual de los posts existentes
   (mirar un original como referencia antes de diseñar).
2. `python scripts/preparar_imagenes.py` → genera el JPEG en `contenido/publicar/`.
3. Agregar entrada en `contenido/calendario.json`:
   ```json
   {
     "id": "slug-unico",
     "tipo": "imagen",          // imagen | carrusel | reel
     "estado": "pendiente",     // pendiente | borrador | publicado | error | vencido
     "fecha": "2026-08-10",
     "hora": "09:00",
     "archivo": "nombre.jpg",   // para carrusel: "archivos": ["a.jpg","b.jpg"]
     "caption": "..."
   }
   ```
   Para reels: `"archivo"` es un .mp4 ya subido a `contenido/publicar/`,
   opcional `"portada"` (jpg) y `"compartir_en_feed"` (default true).
4. `python scripts/validar.py` — debe salir sin errores.
5. Commit + push. GitHub Actions publica solo cuando llegue la fecha/hora.

## Flujo: revisar estado

- Leer `contenido/calendario.json`: campo `estado` de cada post.
  `publicado` incluye `publicado_en` y `media_id`. `error`/`vencido`
  incluyen `nota` con el motivo.
- Antes de leerlo, hacer `git pull` — el bot commitea los cambios de estado.
- Para reintentar un post en `error` o `vencido`: corregir la causa,
  poner `"estado": "pendiente"`, borrar `"nota"` e `"intentos"`, y si la
  fecha ya pasó moverla al próximo horario deseado. Push.

## Cadencia y horarios (estrategia de la cuenta)

Día por medio. Mejores horarios: 9–11 AM y 18–20 hs (hora Argentina).
No programar dos posts el mismo día. Zona horaria del calendario:
`America/Argentina/Buenos_Aires`.

## Precauciones

- NUNCA editar `contenido/publicar/` a mano ni commitear tokens.
- No correr `scripts/publicar.py` localmente salvo con `IG_DRY_RUN=1`.
- Si el usuario pide publicar "ya", cambiar fecha/hora del post a un
  momento pasado reciente y push; el workflow lo toma en ≤30 min. También
  se puede disparar a mano desde Actions → "Publicar en Instagram" → Run
  workflow.
- Límite de la API: 100 publicaciones por cuenta cada 24 hs (de sobra).
- El token de Instagram dura 60 días, pero el workflow
  `refrescar_token.yml` lo renueva solo cada semana (necesita el Secret
  `GH_PAT`, ver SETUP.md Parte F). Si Meta lo invalida igual (cambio de
  contraseña, revisión de seguridad) los posts quedan en `error`:
  regenerar con `python scripts/obtener_token.py` y actualizar el Secret
  `IG_ACCESS_TOKEN`.
