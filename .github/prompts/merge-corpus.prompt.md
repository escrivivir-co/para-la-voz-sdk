---
name: merge-corpus
description: Integra los hallazgos aprobados del diff más reciente en corpus.md. Operación de escritura: solo ejecutar tras aprobación del usuario.
argument-hint: "[opcional: nombre del análisis a mergear, si no es el más reciente]"
agent: archivero
tools: ['search/codebase', 'file-edit']
---

# /merge-corpus — Integrar hallazgos en el corpus

Ejecuta la operación MERGE del archivero.

**Precondición**: se asume que el usuario ha revisado y aprobado un diff previo. Si no hay diff previo en contexto, ejecuta primero `/diff-corpus`.

1. Lee el diff aprobado (del contexto de la conversación, o regenera si es necesario).
2. Lee `corpus/corpus.md` completo.
3. Edita `corpus.md`:
   - Añade los elementos NUEVO a las secciones correspondientes con la fecha de hoy: `[añadido: YYYY-MM-DD]`
   - Actualiza los contadores `[×N]` de los elementos CONFIRMA
   - Registra las DISCREPANCIAS en la sección "Discrepancias abiertas" con fecha
   - Documenta las EVOLUCIONES como variantes del patrón base
4. Actualiza el encabezado de `corpus.md`:
   - `Última actualización:` [fecha de hoy]
   - `Editoriales procesadas:` [incrementar en 1]
   - `Nick de corriente:` [actualiza si el análisis lo revisó]
5. Informa al usuario del merge completado con un resumen de qué cambió.

**Principio de no-borrado**: NO elimines ningún elemento del corpus. Si algo quedó obsoleto o fue refutado, márcalo como `[REVISADO: YYYY-MM-DD — motivo]` pero mantenlo.

Tras el merge, ofrece el handoff al cristalizador si el cambio fue significativo (≥3 elementos NUEVO).
