---
name: guion
description: Genera un guión de ciclo editorial a partir de la plantilla SDK. El guion es un roadmap paso a paso para que una persona del equipo editorial procese una nueva editorial por el pipeline Bartleby. Se ejecuta antes de activar cualquier agente.
argument-hint: "[ruta a editorial en corpus/editoriales/]"
tools: ['search/codebase', 'file-create']
---

# /guion — Generar guión de ciclo editorial

Genera un documento de seguimiento (`guiones/YYYY-MM-DD_slug.guion.md`) a partir de la plantilla SDK. Este documento es un roadmap que una persona del equipo editorial seguirá paso a paso para procesar la editorial por el pipeline Bartleby.

> **Importante:** El guion se crea ANTES de ejecutar ningún agente del pipeline. Es preparación, no análisis.

## Pasos

1. Lee la plantilla en `.github/templates/guion-ciclo.template.md`. Esa es la única plantilla — no busques alternativas.

2. Lee `corpus/corpus.md` y extrae el valor de `Editoriales procesadas: N`. Ese es `{{CORPUS_PROCESADAS}}`. El valor `{{CORPUS_PROCESADAS_DESPUES}}` es N+1.

3. Lee el archivo de editorial indicado por el usuario (argumento del comando). Extrae:
   - `{{EDITORIAL_FECHA}}` — fecha de publicación (búscala en el texto: formato DD/MM/YYYY o similar, convierte a YYYY-MM-DD)
   - `{{EDITORIAL_TITULO}}` — título completo legible
   - `{{EDITORIAL_NUMERO}}` — número de la publicación si aparece (ej: "PARA LA VOZ 3(1)")
   - `{{EDITORIAL_ARCHIVO}}` — la ruta que el usuario proporcionó
   - `{{EDITORIAL_SLUG}}` — versión kebab-case del nombre de archivo sin fecha ni extensión
   - `{{EDITORIAL_TITULO_SLUG}}` — versión kebab-case corta del título (para el mensaje de commit)

4. Lee la carpeta `guiones/` y lista los archivos `.guion.md` por orden alfabético (= cronológico). El último existente es `{{GUION_ANTERIOR}}`. Si no hay ninguno, el valor es vacío.

5. Determina el valor de `{{MOD_RAMA}}`: no leas el sistema de archivos para esto — simplemente usa `mod/[nombre]` o deja el placeholder para que el usuario lo complete.

6. Determina `{{INCLUIR_DESIGN}}` y `{{INCLUIR_PUSH}}`:
   - Si el usuario va a procesar más editoriales después de esta (hay editoriales en `corpus/editoriales/` sin guion en `guiones/`): `{{INCLUIR_DESIGN}}` = no, `{{INCLUIR_PUSH}}` = no
   - Si esta es la última editorial pendiente: `{{INCLUIR_DESIGN}}` = sí, `{{INCLUIR_PUSH}}` = sí
   - Si no puedes determinarlo con certeza, pregunta al usuario antes de generar.

7. Determina `{{GUION_SIGUIENTE}}`: busca en `corpus/editoriales/` si hay archivos cuya fecha en el nombre sea posterior a `{{EDITORIAL_FECHA}}` y que no tengan guion todavía en `guiones/`. El más próximo cronológicamente es `{{GUION_SIGUIENTE}}` (convierte a convención `YYYY-MM-DD_slug.guion.md`). Si no hay siguiente, el valor es vacío.

8. Calcula `{{PASO_COMMIT}}`:
   - Si `{{INCLUIR_DESIGN}}` = sí: el paso de commit es el 5
   - Si `{{INCLUIR_DESIGN}}` = no: el paso de commit es el 4

9. Rellena todos los `{{PLACEHOLDER}}` en la plantilla. Para las secciones condicionales marcadas con `{{#VARIABLE}}...{{/VARIABLE}}`: incluir el bloque si la variable tiene valor, excluirlo si está vacío o es "no".

10. Guarda el resultado en `guiones/{{EDITORIAL_FECHA}}_{{EDITORIAL_SLUG}}.guion.md`.

11. Informa al usuario:
    ```
    Guion creado: guiones/{{EDITORIAL_FECHA}}_{{EDITORIAL_SLUG}}.guion.md
    Ábrelo y sigue los pasos. Empieza por el Paso 1 (/feed).
    ```

## Convención de nombres

- Archivo de guion: `YYYY-MM-DD_slug.guion.md`
- El slug coincide con el slug del archivo de editorial correspondiente
- Ejemplo: `corpus/editoriales/2024-11-20_materialismo.md` → `guiones/2024-11-20_materialismo.guion.md`
