# Respuestas del usuario — Cristalización del pipeline operativo

> **Fecha:** 18-abr-2026
> **Registradas por:** `Claude Opus 4.6`
> **Propósito:** fijar las decisiones de PO, scrum master y cliente en disco.

## Punto 1 — Tipado del lore en el mod (cliente)

- **Respuesta del cliente:** El lore debe estar tipado en el mod. Una cosa es el catálogo de tipos de pieza (esquema genérico del mod legislativa) y otra los datos concretos del caso Feo en DRAFTS2.
- **Efecto operativo:** Se crea `lore-schema.instructions.md` como ontología del mod, no del caso. Los datos siguen en DRAFTS2.

## Punto 2 — Plan limpio para Pipeline (scrum master)

- **Respuesta del scrum master:** Quiere plan limpio para el pipeline basado en el patrón de `future-machine-universo-1`. El cristalizador en modo "dime qué te armo" y el pipeline pidiendo por su cuenta.
- **Efecto operativo:** El plan incluye diálogo simulado cristalizador↔pipeline (§4 del PLAN). Las tasks siguen la secuencia que ese diálogo fijó.

## Punto 3 — Abstracción del protocolo (PO)

- **Respuesta del PO:** Crear plantilla reutilizable del patrón de dossier de cristalización. Luego usarla en directo para pipeline.
- **Efecto operativo:** Se crea `mod/skills/cristalizacion-feature/SKILL.md` como protocolo abstracto. Este dossier es la primera instancia creada desde esa plantilla.

## Punto 4 — Restricción `.github/` (todas las partes)

- **Decisión compartida:** Todo en `mod/`. No se toca `.github/`.
- **Efecto operativo:** Heredado. Sin cambios.

## Punto 5 — DRAFTS2 sigue vivo (todas las partes)

- **Decisión compartida:** Los datos del caso siguen en DRAFTS2 hasta que se decida lo contrario. El mod define esquema, no aloja datos del caso.
- **Efecto operativo:** El routing workaround se formaliza en `lore-routing.instructions.md` en lugar de dejarlo como nota solitaria en `corpus/corpus.md`.

## Punto 6 — Cadena de 5 agentes (19-abr-2026)

- **Decisión del PO + cliente:** La cadena agéntica se separa en 5 roles: Puzzle (ensamblar lore), Archivero Lore (reducir a corpus), Grafista (estructurar grafo JSON), Demiurgo (bifurcar universos), Dramaturgo Cortos (narrar).
- **Efecto operativo:** Los artefactos de este dossier (schema, estado, routing) son consumidos por los 5 agentes, no solo por Pipeline. El estado canónico debe incluir conteos de grafo (nodos, ramas, universos), no solo piezas de lore. El routing debe incluir las rutas del grafo JSON cuando se definan.

## Punto 7 — Grafo en formato JSON (19-abr-2026)

- **Decisión del cliente:** El grafo pasa de Markdown narrativo a gramática JSON estructurada (`index.json`, `nodos.json`, `arcos.json`, `huecos.json`) con una gramática que solo acepta términos identificados en el corpus.
- **Efecto operativo:** El routing (PO-03) necesitará incluir `DRAFTS2/grafo/` como ruta nueva. El estado (PO-02) necesitará una sección de estado del grafo.
