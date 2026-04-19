Promover el patrón "dossier de feature" al SDK (.github/).

Dos artefactos: `dossier.prompt.md` (prompt /dossier) y `cristalizacion-feature/SKILL.md` (protocolo de ciclo de vida). Ambos nacieron en mod/legislativa, se usaron en 5 features, y son 100% genéricos.

Hecho: dossier creado con PLAN, BACKLOG, 4 tasks.
Pendiente: DF-01 (prompt), DF-02 (SKILL), DF-03 (integración SDK + cleanup).

Decisión de producto: los dossiers viven en `{{SALA_DIR}}/dossiers/`. El prompt y el SKILL deben usar esa variable, sin refs a lore específico.

Lectura ejecutiva: [BACKLOG.md](./BACKLOG.md) → [PLAN.md](./PLAN.md) → [RESPUESTAS.md](./RESPUESTAS.md) → tasks/
