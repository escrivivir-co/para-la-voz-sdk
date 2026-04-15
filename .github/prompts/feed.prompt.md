---
name: feed
description: Alimenta el sistema con una nueva editorial. Invoca a Bartleby para analizarla y guarda el análisis en el corpus.
argument-hint: "[ruta al archivo de editorial, o pega el texto directamente]"
agent: bartleby
tools: ['search/codebase', 'file-create']
---

# /feed — Nueva editorial al corpus

Procesa una nueva editorial de la revista usando el análisis Bartleby (5 secciones: herencia, taxonomía, mecanismos, emergencia, vista desde el hueco).

## Pasos

1. Si el usuario pegó el texto directamente en el chat: úsalo tal como está.
2. Si el usuario dio una ruta: lee el archivo desde esa ruta.
3. Si no se proporcionó nada: pide al usuario que pegue el texto o indique la ruta.

4. Lee el contexto del corpus antes de analizar:
   - `corpus/corpus.md` — mapa acumulativo actual
   - `corpus/analisis/` — análisis previos

5. Analiza la editorial aplicando el protocolo Bartleby completo (5 secciones).

6. Determina el nombre del archivo de salida:
   - Formato: `YYYY-MM-DD_slug-editorial.analisis.md`
   - La fecha es la de publicación de la editorial (si está en el texto), o la de hoy.
   - El slug es una versión kebab-case del título.

7. Guarda el análisis en: `corpus/analisis/[nombre-archivo].analisis.md`

8. Guarda el texto original de la editorial en: `corpus/editoriales/[nombre-archivo].md`
   (sin el `.analisis` en el nombre del texto base)

9. Informa al usuario del análisis completado y ofrece el handoff al archivero para ejecutar el diff.

10. Si no existe un guion de seguimiento para esta editorial en `guiones/`, informa al usuario:
    "No hay guion de seguimiento para esta editorial. Puedes generar uno con `/guion {{EDITORIAL_ARCHIVO}}` para tener el roadmap completo del ciclo."

## Recordatorio

El hook `post-feed.json` dispara automáticamente un aviso de diff tras guardar el análisis. Si el hook no está activo, el usuario deberá ejecutar `/diff-corpus` manualmente.
