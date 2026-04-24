Formalizar el pipeline completo de mod/legislativa: lore-db + piezas → corpus → grafo → universos → cortos. Nuevo mapa agéntico.

Qué es\
Crea `lore/` como base de datos canónica de piezas (con subcarpetas piezas/, derivados/, drafts/), migra la base upstream fuera de `DRAFTS2/` y rehace el mapa agéntico del mod: `@Loreador Legislativa` (nuevo, extiende SDK), `@Archivero Legislativa` (renombrado, corpus específico), `@Puzzle` eliminado. La capa corpus ya no se absorbe aquí: se recorta en `corpus-legislativa`.

Qué problema resuelve\
Hoy las piezas están en DRAFTS2/ (nombre de borrador), el pipeline existe de facto pero está disperso, Puzzle y Archivero Lore confunden nombres con el SDK. Esto formaliza todo y homogeneiza la cadena.

Backlog real, en una línea\
LP-00 cerrada · LP-01 lore-db (libre, dep PS-05) · LP-01b migrar piezas (libre, dep LP-01) · LP-02 adaptar schema (libre, dep LP-01b+PS-01) · LP-03 adaptar routing (libre) · LP-04 formalizar pipeline (libre) · LP-05 nuevo mapa agéntico (libre, dep LP-04+PS-03)

Cadena Pipeline nueva\
`Loreador Legislativa → Archivero Legislativa → Grafista → Demiurgo → Dramaturgo Cortos`

Siguiente paso recomendado\
Primero ejecutar PS-05 (scaffold lore/ en main) + PS-03 (Loreador SDK), luego LP-01 + LP-01b (lore-db + migración upstream). La materialización de `corpus/` pasa a `corpus-legislativa`.
