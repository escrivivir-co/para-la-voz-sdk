---
name: feed
description: Alimenta el sistema con un nuevo documento. Invoca a Bartleby para analizarlo y guarda el análisis en el corpus.
argument-hint: "[ruta al archivo del documento, o pega el texto directamente]"
agent: Bartleby
tools: [vscode, execute, read, agent, edit, search, web, browser, todo]
---

# /feed — Nuevo documento al corpus

Procesa un nuevo documento usando el análisis Bartleby (5 secciones: herencia, taxonomía, mecanismos, emergencia, vista desde el hueco).

## Pasos

1. Si el usuario pegó el texto directamente en el chat: úsalo tal como está.
2. Si el usuario dio una ruta: lee el archivo desde esa ruta.
3. Si no se proporcionó nada: pide al usuario que pegue el texto o indique la ruta.

4. Lee el contexto del corpus antes de analizar:
   - `corpus/corpus.md` — mapa acumulativo actual
   - `corpus/analisis/` — análisis previos

5. Analiza el documento aplicando el protocolo Bartleby completo (5 secciones).

6. Determina el nombre del archivo de salida:
   - Formato: `YYYY-MM-DD_slug.analisis.md`
   - La fecha es la de publicación del documento (si está en el texto), o la de hoy.
   - El slug es una versión kebab-case del título.

7. Guarda el análisis en: `corpus/analisis/[nombre-archivo].analisis.md`

8. Guarda el texto original del documento en: `corpus/documentos/[nombre-archivo].md`
   (sin el `.analisis` en el nombre del texto base)

9. Informa al usuario del análisis completado y ofrece el handoff al archivero para ejecutar el diff.

10. Si no existe un guion de seguimiento para este documento en `guiones/`, informa al usuario:
    "No hay guion de seguimiento para este documento. Puedes generar uno con `/guion {{DOCUMENTO_ARCHIVO}}` para tener el roadmap completo del ciclo."

## Recordatorio

El hook `post-feed.json` dispara automáticamente un aviso de diff tras guardar el análisis. Si el hook no está activo, el usuario deberá ejecutar `/diff-corpus` manualmente.
