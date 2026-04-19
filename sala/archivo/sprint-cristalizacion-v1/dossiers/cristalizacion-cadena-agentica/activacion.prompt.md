Qué es\
Cristalización de la cadena agéntica: implementar los 5 agentes especializados del mod legislativa (Puzzle, Archivero Lore, Grafista, Demiurgo, Dramaturgo Cortos) con roles disjuntos y handoffs claros.

Qué problema resuelve\
Hoy el Grafista mezcla construcción de grafo con generación de universo, no existe un agente validador de entrada (Puzzle) ni un diseñador de universos separado (Demiurgo). La cadena actual es de facto 3 agentes haciendo 5 trabajos.

Qué se ha hecho ya

- Se abrió el dossier siguiendo `mod/skills/cristalizacion-feature/SKILL.md`.
- Se fijaron las decisiones del PO, scrum master y cliente (6 puntos).
- Se descompuso el trabajo en 8 tasks (CA-00 a CA-07).
- Se mapearon las dependencias: CA-01 (Puzzle) y CA-03 (refactor Grafista) pueden ir en paralelo.

Qué NO se ha hecho aún

- No existe `puzzle.agent.md`.
- No existe `demiurgo.agent.md`.
- Grafista no ha sido refactorizado (sigue mezclando grafo + universo).
- Archivero Lore no ha sido refactorizado (sigue haciendo inventario propio).
- Dramaturgo Cortos no ha sido recableado (sigue apuntando a Grafista, no a Demiurgo).
- Pipeline no refleja la cadena de 5 en sus handoffs.

Backlog real, en una línea

- CA-00: completada (contexto persistido).
- CA-01: Cristalizador crea `puzzle.agent.md`.
- CA-02: Cristalizador refactoriza `archivero-lore.agent.md`.
- CA-03: Cristalizador refactoriza `grafista.agent.md` (solo grafo, no universos).
- CA-04: Cristalizador crea `demiurgo.agent.md`.
- CA-05: Cristalizador recablea `dramaturgo.agent.md` (handoff de Demiurgo, no Grafista).
- CA-06: Cristalizador actualiza `pipeline.agent.md` con handoffs a los 5.
- CA-07: Pipeline valida la cadena completa.

Decisión de producto que se protege\
Un agente, una transformación. La cadena es pipeline limpio, no un superagente monolítico.

Lectura ejecutiva\
Feature de complejidad media: 2 agentes nuevos, 2 refactors, 1 recableado, 1 update pipeline, 1 validación. Las 2 ramas de dependencia (Puzzle → Archivero y Grafista → Demiurgo → Dramaturgo) pueden avanzar en paralelo.
