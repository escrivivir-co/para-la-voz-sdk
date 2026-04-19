# TASK-05 — Validar compatibilidad de corpus

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** CP-03, CP-04
> **Entrega esperada:** informe de validación SDK/mod

## Objetivo

Comprobar que la nueva capa corpus no rompe ni el SDK base ni la cadena del mod.

## Checks mínimos

1. `/feed` sigue encontrando `corpus/`.
2. `/diff-corpus`, `/merge-corpus`, `/status` siguen resolviendo la ruta canónica.
3. `/lore-ingest` produce el corpus correcto.
4. Grafista, Pipeline, Demiurgo y Dramaturgo leen el corpus correcto.

## Criterio de aceptación

- Existe informe de compatibilidad y no quedan refs públicas a `DRAFTS2/CORPUS_PREVIEW.md` sin justificar.