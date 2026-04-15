---
name: status
description: Muestra el estado actual del corpus Bartleby — número de editoriales, categorías activas, última actualización, discrepancias abiertas y salud del corpus.
agent: archivero
tools: ['search/codebase']
---

# /status — Estado del corpus BARTLEBY

Lee `corpus/corpus.md` y `corpus/analisis/` y produce el informe de estado completo:

```markdown
## Estado del Corpus BARTLEBY
**Fecha:** [hoy]
**Editoriales procesadas:** N
**Última editorial:** [fecha — título]
**Nick de corriente:** [string actual]

### Linaje
- Primario: N nodos
  Top 5: [lista]
- Por exclusión: N nodos
  Lista: [todos]

### Taxonomía funcional
- Categorías: N
  Lista completa: [todas]
- En evolución: [las que han variado entre análisis]

### Mecanismos retóricos
- Detectados: N (lista completa)
- Frecuencias: [ordenados por apariciones ×N]

### Emergencias
- Acumuladas: N
- Lista: [todas, con fecha de primera aparición]

### Ausencias estructurales
- Acumuladas: N
- Lista: [todas]

### Discrepancias abiertas
- Abiertas: N
- [Si hay: descripción breve de cada una]

### Salud del corpus
- Consistencia interna: [alta/media/baja — justificación en una frase]
- Próxima acción sugerida: [si hay editorial pendiente de procesar, merge pendiente, etc.]
```

Si el corpus está vacío o recién inicializado, muestra el estado del seed canónico.
