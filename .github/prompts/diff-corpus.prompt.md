---
name: diff-corpus
description: Compara el análisis más reciente (o el indicado) con el corpus acumulativo. Muestra qué es nuevo, qué confirma patrones, qué discrepa, qué evoluciona.
argument-hint: "[opcional: nombre del archivo de análisis a comparar]"
agent: Archivero
tools: [vscode, execute, read, agent, edit, search, web, browser, todo]
---

# /diff-corpus — Comparar análisis con corpus

Ejecuta la operación DIFF del archivero:

1. Si el usuario especificó un archivo de análisis: úsalo.
2. Si no: busca el análisis más reciente en `corpus/analisis/` (por fecha en el nombre del archivo).

3. Lee `corpus/corpus.md` completo.

4. Compara y produce el informe de diff con cinco categorías:

```
NUEVO: elementos presentes en el análisis pero ausentes en corpus.md
CONFIRMA: elementos que reiteran patrones ya registrados (sube contador ×N)
NO ACTIVADO: elementos del corpus que no aparecen en este documento
  - El corpus es acumulativo: no-activación ≠ discrepancia.
  - Cada documento trabaja en su registro; no tiene que repetir todo.
DISCREPA: elementos que CONTRADICEN ACTIVAMENTE un patrón del corpus
  - Solo si el texto afirma algo incompatible con lo registrado.
  - Que un rasgo no aparezca NO es discrepancia, es NO ACTIVADO.
EVOLUCIONA: variaciones que desarrollan un patrón sin contradecirlo
```

**Exclusiones implícitas:** Solo se incorporan al corpus exclusiones que el texto declare explícitamente. Las omisiones se anotan en el análisis, no en el corpus.

5. Termina con una pregunta al usuario: "¿Apruebas el merge de estos hallazgos en el corpus?"

Si el usuario responde afirmativamente, ofrece el handoff a `/merge-corpus`.
