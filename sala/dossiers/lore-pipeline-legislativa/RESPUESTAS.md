# Respuestas del usuario — lore-pipeline-legislativa

> **Fecha:** 19-abr-2026
> **Registradas por:** Claude Opus 4.6

## Punto 1 — Ubicación definitiva de piezas → lore-db

- **Contexto:** Hoy las piezas viven en `DRAFTS2/` como workaround. Opciones: `corpus/piezas/`, renombrar a `lore/`, o formalizar `DRAFTS2/`.
- **Respuesta del usuario (19-abr-2026):** "LP-01 tiene que ser lore-db. Migrar piezas existentes SIN PERDER DATOS a carpeta fuera de DRAFTS2. La db se inicializa desde scaffold de main (como sala-aleph inicializa la sala)."
- **Efecto operativo:**
  - `lore/` es la carpeta canónica — `{{LORE_DIR}}` = `lore/`
  - El SDK provee scaffold `lore/` en main (PS-05) con README, .gitkeep stubs, templates
  - `/sala-aleph` o un prompt de init inicializa la db si no existe (copia templates)
  - LP-01 crea la estructura, LP-01b migra los 40+ ficheros con `git mv`

## Punto 2 — Vinculación corpus + grafo + universos + cortos

- **Contexto:** El usuario pide explícitamente formalizar "cómo se vincula luego ese lore con todo el resto: corpus + grafo + universos + cortos".
- **Respuesta del usuario:** Se implementa como `mod/instructions/lore-pipeline.instructions.md` que documenta el grafo de dependencias y los handoffs entre agentes.
- **Efecto operativo:** Task LP-04.
