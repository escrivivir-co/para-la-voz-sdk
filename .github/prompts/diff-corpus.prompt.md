---
name: diff-corpus
description: Compara el análisis más reciente (o el indicado) con el corpus acumulativo. Muestra qué es nuevo, qué confirma patrones, qué discrepa, qué evoluciona.
argument-hint: "[opcional: nombre del archivo de análisis a comparar]"
agent: archivero
tools: ['search/codebase']
---

# /diff-corpus — Comparar análisis con corpus

Ejecuta la operación DIFF del archivero:

1. Si el usuario especificó un archivo de análisis: úsalo.
2. Si no: busca el análisis más reciente en `PROYECTOS/BARTLEBY/corpus/analisis/` (por fecha en el nombre del archivo).

3. Lee `PROYECTOS/BARTLEBY/corpus/corpus.md` completo.

4. Compara y produce el informe de diff con cuatro categorías:

```
NUEVO: elementos presentes en el análisis pero ausentes en corpus.md
CONFIRMA: elementos que reiteran patrones ya registrados (con contador)
DISCREPA: elementos que contradicen el patrón del corpus (con descripción precisa)
EVOLUCIONA: variaciones que desarrollan un patrón sin contradecirlo
```

5. Termina con una pregunta al usuario: "¿Apruebas el merge de estos hallazgos en el corpus?"

Si el usuario responde afirmativamente, ofrece el handoff a `/merge-corpus`.
