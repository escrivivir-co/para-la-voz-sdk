Formalizar el pipeline completo de mod/legislativa: lore-db + piezas → corpus → grafo → universos → cortos.

Qué es\
Crea `lore/` como base de datos canónica de piezas, migra todo de DRAFTS2/ sin perder datos, y documenta el pipeline específico de cómo las piezas alimentan toda la cadena: corpus, grafo de bifurcación, universos expandidos, y relatos generados.

Qué problema resuelve\
Hoy las piezas están en DRAFTS2/ (nombre de borrador), el pipeline existe de facto pero está disperso, y los agentes no referencian el SDK genérico. Esto formaliza todo.

Backlog real, en una línea\
LP-00 cerrada · LP-01 lore-db (libre, dep PS-05) · LP-01b migrar piezas (libre, dep LP-01) · LP-02 adaptar schema (libre, dep LP-01b+PS-01) · LP-03 adaptar routing (libre) · LP-04 formalizar pipeline (libre) · LP-05 adaptar agentes (libre)

Siguiente paso recomendado\
Primero ejecutar PS-05 (scaffold lore/ en main), luego LP-01 (crear lore-db) y LP-01b (migración).
