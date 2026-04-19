Dossier preparado fuera del sprint activo. No está en el tablero actual.

Capa portable de corpus en el SDK.

Qué es\
Cristaliza `corpus/` como fase propia entre `lore-db` y `grafo`, y formaliza al `@Archivero` como agente del corpus tanto para el flujo clásico `/feed` como para el modo batch desde una lore-db.

Qué problema resuelve\
Hoy el SDK tiene corpus incremental y el mod legislativa tiene corpus batch, pero no existe una abstracción común. Eso deja `corpus/` a medio camino entre API pública y workaround.

Backlog real, en una línea\
CS-00 cerrada · CS-01 schema corpus (libre) · CS-02 Archivero capa corpus (libre) · CS-03 compat prompts/flujos (libre) · CS-04 documentar SDK (libre)

Siguiente paso recomendado\
No meter este dossier aún en el tablero. Abrirlo cuando se quiera fijar de verdad la capa `corpus/` y recortar la ambigüedad entre `Archivero` SDK y `Archivero Legislativa`.