# Q&A Study

App de estudio con preguntas **Multiple Choice** y de **Desarrollo**, con timer y selección por tema. Funciona **sin internet** en el celular (Android y iPhone), y las preguntas quedan guardadas en el dispositivo.

**Abrir la app:** https://santiagoa245.github.io/Q-A-Study/

> Ojo: la app está en **github.io**, no en github.com. Si creás el acceso directo desde la página del repo (github.com/...), el ícono abre GitHub y no la app.

---

## Instalarla en el celular

### Android (Chrome)
1. Abrí **santiagoa245.github.io/Q-A-Study** escribiéndolo directo en **Chrome**. No uses el link desde WhatsApp ni desde la app de GitHub, porque se abre adentro de esas apps y ahí no se puede instalar.
2. Fijate que se vea la app (título "Q&A Study", fondo oscuro).
3. Menú **⋮** > **Instalar app** o **Agregar a la pantalla principal**.
4. Abrila una vez desde el ícono con internet. Desde ahí funciona sin conexión.

**Si dice que no se puede instalar:**
- En Xiaomi, Redmi o Poco: Ajustes > Apps > Chrome > **Otros permisos** > activá **"Accesos directos en la pantalla de inicio"**. En otras marcas está en Ajustes > Apps > Chrome > Permisos.
- Si igual falla: menú ⋮ > Agregar a la pantalla principal > **Crear acceso directo**. Funciona igual.

### iPhone (Safari)
1. Abrí **santiagoa245.github.io/Q-A-Study** en **Safari**. Desde Chrome u otras apps puede no aparecer la opción.
2. Tocá **Compartir** (el cuadrado con la flecha para arriba) > **Agregar a pantalla de inicio** > **Agregar**.
3. Abrila una vez desde el ícono con internet. Desde ahí funciona sin conexión.

---

## Cómo se usa

- **Modalidad:** Multiple Choice (MO) o Desarrollo.
- **Timer:** en MO da 30 segundos por pregunta (si se acaba, cuenta como errada). En Desarrollo es un cronómetro por pregunta y del total.
- **Importar preguntas (.txt):** elegís uno o varios archivos con el formato de abajo. Pasalos al celular por WhatsApp, Drive o mail y guardalos en Archivos/Descargas. Si el bloque ya existe, se agregan solo las preguntas nuevas.
- **Escribir o pegar preguntas:** pegás directo el texto de un archivo.
- **Ver bloques cargados:** tildás qué bloques y temas entran en la partida, elegís el % de preguntas por tema (se sortean en cada partida) y podés **Editar** o **Borrar** bloques.
- **Partida guardada:** si cambiás de app, se apaga la pantalla o cerrás la app en medio de una partida, se guarda sola (pregunta actual, respuestas y tiempo; el timer se pausa mientras no la estás usando). Al volver a abrirla te ofrece **Continuar** o **Descartar**.
- **Exportar copia de seguridad:** guarda todos tus bloques en un .txt que podés volver a importar.

### Formato de los archivos de preguntas

Texto `.txt` (UTF-8). Una etiqueta por línea y `---` entre preguntas:

```
BLOQUE: Biología celular

TEMA: Organelas
PREGUNTA: ¿Cuál es la función principal de la mitocondria?
FALSA: Sintetizar proteínas
FALSA: Almacenar el material genético
FALSA: Realizar la fotosíntesis
CORRECTA: Producir energía (ATP) mediante la respiración celular
SOLUCION: La mitocondria produce energía en forma de ATP mediante la respiración celular.
---
```

- `TEMA:` es opcional. `FALSA:` va una por línea: MO necesita al menos 2, y con más de 3 se eligen 3 al azar.
- `SOLUCION:` es para Desarrollo. El % de coincidencia cuenta las palabras clave de la solución que aparecen en tu respuesta.
- Cada pregunta queda como **MOD** (sirve para los dos modos), **MO**, **D** o **E** (le falta algo y no se juega).

Más detalle en `FORMATO_PREGUNTAS.md` de la app de PC.

---

## Importante

- Las preguntas se guardan **en cada celular**, no en GitHub. El Android, el iPhone y la PC tienen cada uno sus propios bloques.
- Si borrás los datos del navegador o desinstalás la app, se pierden. **Exportá una copia** de vez en cuando.
- Para actualizar la app, reemplazá los archivos del repo. El celular toma la versión nueva la próxima vez que la abras con internet.

## Archivos del repo

Tienen que estar todos en la raíz del repo, no adentro de una carpeta:

| Archivo | Para qué sirve |
|---|---|
| `index.html` | La app completa |
| `manifest.webmanifest` | Nombre e ícono para instalarla |
| `sw.js` | Guarda la app para que funcione sin internet |
| `icon-180.png`, `icon-192.png`, `icon-512.png` | Íconos |

## Publicarla (si hay que rehacerlo)

1. Repo **público** con los archivos de arriba en la raíz.
2. **Settings** > **Pages** > Branch: **main** > **/ (root)** > **Save**.
3. A los 1 o 2 minutos la dirección aparece arriba en esa misma pantalla. Si da 404, esperá un poco más y revisá que `index.html` esté en la raíz.
