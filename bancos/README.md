# Bancos de preguntas públicos

Esta carpeta es la "nube" de Q&A Study. Todo lo que está acá se puede bajar desde la app con el botón **Descargar bancos de la nube** (celular y PC), sin pasar archivos a mano.

Se publica sola con GitHub Pages en:
https://santiagoa245.github.io/Q-A-Study/bancos/index.json

## Cómo agregar o actualizar un banco

1. Subí el `.txt` a esta carpeta (en GitHub: **Add file > Upload files**). Usá un nombre sin espacios ni tildes, por ejemplo `historia-uruguay.txt`. El contenido tiene que tener el formato de siempre (`BLOQUE:`, `TEMA:`, `PREGUNTA:`, `FALSA:`, `CORRECTA:`, `SOLUCION:`, `---`).
2. Agregá una entrada en `index.json` dentro de `"bancos"`:
   ```json
   {
     "archivo": "historia-uruguay.txt",
     "bloque": "Historia del Uruguay",
     "descripcion": "Texto corto que se ve en la app.",
     "preguntas": 40,
     "temas": ["Colonia", "Independencia"]
   }
   ```
   Solo `archivo` es obligatorio. El resto es lo que se muestra en la lista.
   Si tenés Python, `python3 bancos/generar_indice.py` arma el `index.json` solo (cuenta preguntas y temas y conserva las descripciones).
3. En 1 o 2 minutos ya aparece en la app.

Si alguien baja un banco que ya tiene, la app agrega solo las preguntas nuevas y descarta las repetidas, así que podés ir sumando preguntas a un mismo archivo.

Ojo: el repo es público, así que cualquiera con el link puede ver estos archivos.
