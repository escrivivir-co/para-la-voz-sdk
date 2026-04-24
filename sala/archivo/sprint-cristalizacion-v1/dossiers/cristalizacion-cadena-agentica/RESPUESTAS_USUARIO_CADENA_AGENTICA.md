# Respuestas del usuario — Cristalización de la cadena agéntica

> **Fecha:** 19-abr-2026
> **Registradas por:** `Claude Opus 4.6`
> **Propósito:** fijar las decisiones de PO, scrum master y cliente en disco.

## Punto 1 — Separación en 5 roles (PO + cliente)

- **Decisión:** La cadena agéntica se separa en 5 agentes con una sola transformación cada uno: Puzzle (ensambla), Archivero Lore (reduce a corpus), Grafista (estructura grafo), Demiurgo (bifurca universos), Dramaturgo Cortos (narra).
- **Efecto operativo:** Se crean 2 agentes nuevos (Puzzle, Demiurgo), se refactorizan 2 (Archivero Lore, Grafista) y se recablea 1 (Dramaturgo Cortos).

## Punto 2 — Puzzle como validador de entrada (cliente)

- **Decisión del cliente:** El lore es un "puzzle" cuyas piezas deben ser tipadas y validadas antes de entrar al pipeline. No es un feed.
- **Efecto operativo:** Puzzle valida contra `lore-schema.instructions.md`. Archivero Lore pierde su paso de inventario/validación.

## Punto 3 — Grafista solo hace grafo (PO)

- **Decisión del PO:** Grafista construye el grafo de bifurcación. No genera universos. Eso es del Demiurgo.
- **Efecto operativo:** Grafista pierde handoff a Dramaturgo Cortos. Se añade handoff a Demiurgo.

## Punto 4 — Demiurgo como diseñador de universos (PO)

- **Decisión del PO:** Demiurgo es conversacional: presenta ramas, resuelve huecos con el usuario, instancia el universo. Es el "director de escena" antes del dramaturgo.
- **Efecto operativo:** Demiurgo aplica futures-engine Fase 4 (instanciación). Dramaturgo Cortos recibe universo listo.

## Punto 5 — Grafo en JSON con gramática cerrada (cliente)

- **Decisión del cliente:** El grafo pasa de Markdown a JSON con gramática que solo acepta términos del corpus. Se trata en dossier aparte (`cristalizacion-grafo-json/`).
- **Efecto operativo:** Grafista se prepara para consumir JSON pero hoy sigue leyendo Markdown. El refactor no bloquea.

## Punto 6 — Versatilidad para el showcase (scrum master)

- **Decisión del scrum master:** La cadena de 5 agentes es una alegría al cliente. Muestra que el mod puede tener agentes especializados más allá del SDK core.
- **Efecto operativo:** Los agentes deben ser autocontenidos y con handoffs claros. No agentes-todo.
