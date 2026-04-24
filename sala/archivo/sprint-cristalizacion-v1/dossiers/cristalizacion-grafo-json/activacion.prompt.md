Qué es\
Cristalización del grafo JSON: migrar el grafo de bifurcación del lore legislativa de Markdown a una gramática JSON estructurada con vocabulario cerrado al corpus.

Qué problema resuelve\
Hoy el grafo vive en `LORE_F-02_UNIVERSO.md` como prosa Markdown. Los agentes (Grafista, Demiurgo, Pipeline) parsean texto libre para encontrar nodos, arcos y huecos. Un formato JSON con gramática definida elimina la ambigüedad y permite validación automática de vocabulario.

Qué se ha hecho ya

- Se abrió el dossier siguiendo `mod/skills/cristalizacion-feature/SKILL.md`.
- Se diseñaron los schemas JSON para los 4 ficheros (index, nodos, arcos, huecos) + gramática legible.
- Se fijaron las decisiones del PO y el cliente (4 puntos).
- Se descompuso en 8 tasks (GJ-00 a GJ-07).
- Se mapeó la dependencia con el dossier `cristalizacion-cadena-agentica/` (GJ-07 necesita CA-03 completado).

Qué NO se ha hecho aún

- No existe `DRAFTS2/grafo/` ni ninguno de los 5 ficheros.
- No se ha migrado ningún nodo del Markdown al JSON.
- No se ha validado el vocabulario contra el corpus.
- Grafista no lee JSON todavía.

Backlog real, en una línea

- GJ-00: completada (contexto persistido).
- GJ-01: Cristalizador escribe `gramatica.md`.
- GJ-02: Cristalizador migra nodos a `nodos.json`.
- GJ-03: Cristalizador migra arcos a `arcos.json`.
- GJ-04: Cristalizador migra huecos a `huecos.json`.
- GJ-05: Cristalizador genera `index.json` con estadísticas.
- GJ-06: Grafista valida vocabulario contra corpus.
- GJ-07: Cristalizador actualiza Grafista para leer JSON.

Decisión de producto que se protege\
Solo entran al grafo términos del corpus. Es gramática cerrada, no texto libre.

Lectura ejecutiva\
Feature bien estructurado: 1 spec + 4 migraciones de datos + 1 validación + 1 refactor de agente. GJ-02/03/04 pueden ir en paralelo. Dependencia cruzada: GJ-07 espera al refactor de Grafista del dossier cadena-agéntica.
