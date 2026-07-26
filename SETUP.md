# Puesta en marcha — Publicación automática en Instagram

Guía de una sola vez. Cuando termines estos pasos, el sistema publica solo
y no tenés que tocar nada más: solo agregar contenido al calendario.

Esta versión usa la **Instagram API con Login de Instagram**: publica con tu
cuenta profesional de Instagram **sin necesidad de una página de Facebook**.
(Tu Facebook borrado no importa: tu cuenta de Instagram alcanza.)

Tiempo estimado: 30–45 minutos.

---

## Requisitos previos

1. **Cuenta de Instagram en modo Profesional (Business o Creator).**
   @espaciomindfulness ya lo es. Si dejara de serlo: Instagram →
   Configuración → Herramientas profesionales → Cambiar a cuenta profesional.

2. **Una cuenta de Facebook para entrar al panel de desarrolladores.**
   Solo se usa para crear la app en developers.facebook.com. **No hace falta
   página, ni vincular nada, ni volver a usarla.** Si tu Facebook viejo se
   borró, creá uno nuevo y vacío en facebook.com/signup (2 minutos).

3. **Cuenta de GitHub** (gratis): github.com/signup con tu email.

---

## Parte A — App de Meta con producto Instagram (15 min)

1. Entrá a https://developers.facebook.com e iniciá sesión con tu cuenta de
   Facebook. La primera vez te pide registrarte como desarrollador (aceptás
   los términos y listo).
2. **My Apps → Create App**.
   - Si te pregunta el caso de uso, elegí **Other** → Tipo: **Business**.
   - Nombre: `Publicador Espacio Mindfulness`. Creá la app.
3. En el panel de la app, en **Add products** buscá **Instagram** y clic en
   **Set up**. Elegí la opción **"API setup with Instagram business login"**
   (configuración de la API con inicio de sesión de Instagram).
4. Ahí vas a ver un botón para **agregar tu cuenta de Instagram**
   ("Add account" / "Conectar"). Clic, y se abre el login de **Instagram**
   (usuario y contraseña de @espaciomindfulness, NO de Facebook). Autorizá
   los permisos que pida.
5. Confirmá que entre los permisos (scopes) estén marcados:
   - `instagram_business_basic`
   - `instagram_business_content_publish`
6. Anotá el **App Secret**: **App settings → Basic → App Secret** (botón Show).
7. No hace falta pasar App Review ni modo Live: publicando en tu propia
   cuenta, con tu cuenta conectada, el modo desarrollo alcanza.

## Parte B — Generar el token (5 min)

1. Volvé a la sección **Instagram → API setup with Instagram business login**.
2. Al lado de tu cuenta conectada hay un botón **"Generate token"**
   (Generar token). Clic, autorizá si lo pide.
3. Copiá el token que aparece (una tira larga). Puede durar 1 hora o ya 60
   días; el script de la Parte C se encarga de dejarlo en 60 días igual.

## Parte C — Token definitivo e ID de la cuenta (5 min)

En esta carpeta, abrí una terminal y corré:

```bash
python scripts/obtener_token.py
```

Pega el **App Secret** (Parte A) y el **token** (Parte B) cuando te los pida.
El script verifica el token, lo pasa a larga duración si hace falta, y al
final te muestra:

- `IG_USER_ID` → el ID numérico de tu cuenta de Instagram
- `IG_ACCESS_TOKEN` → el token de larga duración (60 días)

Guardalos para la Parte D. **No los pegues en ningún archivo del repo.**

## Parte D — Repositorio en GitHub (15 min)

1. Creá el repo: github.com/new
   - Nombre: `instagram-espacio-mindfulness`
   - **Public** ⚠️ — necesario para que Instagram pueda descargar las
     imágenes vía `raw.githubusercontent.com`. Las imágenes y captions van a
     ser visibles para quien tenga el link (de todos modos es contenido que
     va a Instagram público). Los tokens NO van al repo: van en Secrets, que
     son privados siempre.
2. Cargá los Secrets: en el repo → **Settings → Secrets and variables →
   Actions → New repository secret**. Creá dos:
   - `IG_USER_ID` = el valor de la Parte C
   - `IG_ACCESS_TOKEN` = el valor de la Parte C
3. Subí esta carpeta al repo. Desde esta carpeta (`Instagram/`):

```bash
git init -b main
git add .
git commit -m "Pipeline de publicacion automatica (Instagram Login)"
git remote add origin https://github.com/TU_USUARIO/instagram-espacio-mindfulness.git
git push -u origin main
```

   (Reemplazá `TU_USUARIO` por tu usuario de GitHub. Git te va a pedir
   iniciar sesión la primera vez.)

4. En el repo → pestaña **Actions** → si aparece un aviso, habilitá los
   workflows. Además en **Settings → Actions → General → Workflow
   permissions** marcá **Read and write permissions** (el bot necesita
   commitear el estado del calendario).

## Parte E — Probar sin publicar (5 min)

1. Repo → **Actions → Publicar en Instagram → Run workflow** →
   activá **Simulacro** → Run.
2. Abrí la corrida y mirá el resumen: te dice qué habría publicado y
   con qué URL de imagen. Verificá que la URL abra la imagen en el
   navegador.
3. Cuando el simulacro se vea bien, el cron corre cada 30 minutos y publica
   cuando llegue la fecha/hora de cada post del calendario.

## Parte F — Refresco automático del token (10 min, muy recomendado)

El token de Instagram dura **60 días**. El repo trae un workflow que lo
renueva solo cada semana, así nunca vence. Para que pueda guardar el token
nuevo necesita un permiso extra:

1. Creá un **token de acceso personal** de GitHub:
   github.com/settings/personal-access-tokens → **Generate new token**
   (fine-grained).
   - **Repository access**: Only select repositories → elegí
     `instagram-espacio-mindfulness`.
   - **Permissions → Repository permissions → Secrets**: **Read and write**.
   - Generá y copiá el token (empieza con `github_pat_...`).
2. En el repo → **Settings → Secrets and variables → Actions → New repository
   secret**:
   - `GH_PAT` = ese token personal.
3. Probalo: **Actions → Refrescar token de Instagram → Run workflow**. Si el
   resumen dice "Secret IG_ACCESS_TOKEN actualizado", quedó andando solo.

> Si preferís no hacer esta parte, el sistema igual publica, pero cada ~55
> días vas a tener que repetir las Partes B y C y actualizar el Secret
> `IG_ACCESS_TOKEN` a mano.

---

## Uso diario (esto es todo lo que queda a futuro)

- **Agregar/crear posts**: pedímelo en Claude — la skill `instagram` sabe
  generar los diseños con tu paleta, preparar los JPEG, validar y
  programarlos. Después `git push` y listo.
- **Ver qué pasó**: el campo `estado` en `contenido/calendario.json`
  (el bot lo actualiza), o la pestaña Actions del repo.
- **Publicar algo ya mismo**: Actions → Run workflow (sin simulacro),
  con el post fechado en el pasado reciente.

## Problemas comunes

| Síntoma | Causa probable | Solución |
|---|---|---|
| Post en `error` con "Invalid OAuth" / token vencido | El refresco automático no está activo o falló | Activá la Parte F, o rehacé Partes B–C y actualizá el Secret `IG_ACCESS_TOKEN` |
| "Media download failed" | La URL de la imagen no es accesible | ¿Repo público? ¿El JPEG está commiteado en `contenido/publicar/`? |
| El workflow de refresco falla con "Falta GH_PAT" | No cargaste el token personal | Hacé la Parte F |
| Post quedó `vencido` | El workflow no corrió a tiempo (>12 hs) | Reprogramarlo: estado `pendiente` + nueva fecha |
| Nada corre a la hora exacta | Normal: el cron de GitHub puede demorar minutos | El margen de gracia lo cubre |
