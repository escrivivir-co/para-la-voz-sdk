Dossier preparado fuera del sprint activo. No está en el tablero actual.

Capa corpus real en mod/legislativa.

Qué es\
Saca `corpus` del limbo entre shim y fuente viva. Materializa la capa `corpus/`, adapta a `@Archivero Legislativa` y recablea a los consumidores downstream.

Qué problema resuelve\
Hoy el caso real usa `DRAFTS2/CORPUS_PREVIEW.md`, mientras `corpus/` solo finge ser canónico para satisfacer al SDK. Esa ambigüedad ya no escala una vez que la arquitectura se ha separado en fases.

Backlog real, en una línea\
CP-00 cerrada · CP-01 materializar corpus (libre) · CP-02 documentos+analisis (libre) · CP-03 adaptar Archivero/ingest (libre) · CP-04 recablear consumidores (libre) · CP-05 validar compatibilidad (libre)

Siguiente paso recomendado\
No meter este dossier aún en el tablero. Abrirlo cuando se quiera convertir `corpus/` en capa real y dejar de depender públicamente de `DRAFTS2/CORPUS_PREVIEW.md`.