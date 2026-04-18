Qué es\
Cristalización del pipeline operativo: tipar el lore en el mod y dar a los 5 agentes de la cadena (Puzzle, Archivero Lore, Grafista, Demiurgo, Pipeline) lo que necesitan para funcionar sin workarounds manuales.

Qué problema resuelve\
Hoy los agentes operan con conocimiento implícito: no saben qué tipos de pieza existen, no tienen fuente de verdad para conteos (piezas ni grafo), y cada uno resuelve el routing a DRAFTS2 por su cuenta. Este feature formaliza el esquema, el estado y las rutas como instrucciones del mod.

Qué se ha hecho ya

- Se abrió el dossier siguiendo `mod/skills/cristalizacion-feature/SKILL.md`.
- Se simuló el diálogo cristalizador↔pipeline para detectar huecos reales.
- Se fijaron las decisiones del PO, scrum master y cliente.
- Se descompuso el trabajo en 6 tasks (PO-00 a PO-05).
- [19-abr-2026] Se amplió el scope: los artefactos son consumidos por los 5 agentes de la cadena, no solo Pipeline. El estado incluye grafo y universos. El routing incluirá rutas del grafo JSON.

Qué NO se ha hecho aún

- No existen los 3 ficheros de instructions propuestos (schema, estado, routing).
- No se ha actualizado `legislativa-universo.instructions.md` para eliminar conteos duplicados.
- No se ha validado el pipeline ni los demás agentes con los nuevos artefactos.

Backlog real, en una línea

- PO-00: completada (contexto persistido).
- PO-01: Cristalizador crea `lore-schema.instructions.md`.
- PO-02: Cristalizador crea `lore-estado.instructions.md`.
- PO-03: Cristalizador crea `lore-routing.instructions.md`.
- PO-04: Cristalizador actualiza `legislativa-universo.instructions.md`.
- PO-05: Pipeline valida con `/refresh status`.

Decisión de producto que se protege\
Separar esquema (mod) de datos (caso). El mod define qué tipos de pieza existen; DRAFTS2 tiene las piezas concretas del caso Feo. Cuando se archive este caso y se abra otro, el esquema sigue.

Lectura ejecutiva\
Feature bien acotado: 4 instrucciones nuevas/editadas + 1 validación. La secuencia tiene dependencias lineales claras. El siguiente paso es aprobar PO-01 y dejar que el Cristalizador lo ejecute.
