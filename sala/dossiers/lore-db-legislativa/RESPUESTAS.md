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

## Punto 3 — Subcarpetas confirmadas (19-abr-2026)

- **Contexto:** ¿Piezas y derivados en subcarpetas separadas (`lore/piezas/`, `lore/derivados/`) o todo plano en `lore/`?
- **Respuesta del usuario:** "Subcarpetas."
- **Efecto operativo:** Se mantiene el diseño de LP-01: `lore/piezas/`, `lore/derivados/`, `lore/drafts/`. Se asume el coste de actualizar ~20 refs cruzadas entre piezas y derivados en LP-01b.

## Punto 4 — Puzzle desaparece como agente (19-abr-2026)

- **Contexto:** Puzzle valida piezas contra schema. Con `@Loreador` en el SDK, esa función se absorbe.
- **Respuesta del usuario:** "Desaparece."
- **Efecto operativo:** Puzzle se elimina. Su función de validación se absorbe en `@Loreador` (SDK) / `@Loreador Legislativa` (mod). LP-05 (adaptar agentes) incluye la eliminación.

## Punto 5 — Archivero Lore → Archivero Legislativa (19-abr-2026)

- **Contexto:** Pipeline necesita incorporar al Loreador. ¿Qué pasa con Archivero Lore?
- **Respuesta del usuario:** "Fíjate en pipeline, ahora necesita incorporar al loreador. ¿El archivero que como archivero legislativa, no? Que hace corpus específico."
- **Efecto operativo:**
  - `@Archivero Lore` se renombra a `@Archivero Legislativa`
  - Su rol: generar corpus específico del mod (ingest batch → Bartleby → CORPUS_PREVIEW)
  - Pipeline ahora: `Loreador Legislativa → Archivero Legislativa → Grafista → Demiurgo → Dramaturgo Cortos`
  - `@Loreador` (SDK genérico) gestiona la lore-db; `@Archivero Legislativa` genera corpus desde las piezas validadas

## Punto 6 — Grafo a nuevo dossier: SDK + mod (19-abr-2026)

- **Contexto:** El grafo de bifurcación (futures-engine, Grafista, Demiurgo) hoy vive en el mod. ¿Se abstrae al SDK?
- **Respuesta del usuario:** "Tenemos que hacer un nuevo dossier para grafo. Igual, sacar la feature a main-sdk, y traer aquí, y entonces homogeneizar."
- **Efecto operativo:** Nuevo dossier `grafo-sdk` que sigue el patrón de `pieza-sdk`: extraer concepto genérico de grafo al SDK main, luego el mod extiende. Puede requerir un segundo dossier en LP para la adaptación del mod.

## Punto 7 — mod_legislativa_*.md no se tocan (19-abr-2026)

- **Contexto:** Los 8 ficheros `mod_legislativa_*.md` en DRAFTS2/ son spec del mod, no lore.
- **Respuesta del usuario:** "No se tocan de momento."
- **Efecto operativo:** Se quedan en DRAFTS2/ sin migración. No bloquean ninguna task de LP ni PS.
