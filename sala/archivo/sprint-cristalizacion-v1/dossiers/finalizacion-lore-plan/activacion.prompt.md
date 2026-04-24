Qué es\
Finalización del LORE_PLAN: pasar el plan de producción del lore de borrador de trabajo a documento rector v1.0 final.

Qué problema resuelve\
El LORE_PLAN.md es la guía de producción del caso Feo. Fue creado en Sprint 0 y ha acumulado PBIs, sprints y decisiones, pero nunca se cerró formalmente. Tiene secciones redundantes (§10 recomienda trabajo ya hecho), conteos desactualizados y no menciona los features agénticos (cadena de 5, grafo JSON, pipeline operativo).

Qué se ha hecho ya

- Se abrió el dossier siguiendo `mod/skills/cristalizacion-feature/SKILL.md`.
- Se identificaron 5 problemas concretos (desync conteos, PBIs desactualizados, sprints sin cierre, falta de features agénticos, DoR/DoD duplicadas con futuro schema).
- Se fijaron las decisiones del PO (4 puntos).
- Se descompuso en 9 tasks (LP-00 a LP-08).

Qué NO se ha hecho aún

- No se han reconciliado los PBIs contra disco.
- No se han cerrado los sprints.
- No se han añadido los features agénticos al plan.
- No se ha marcado como v1.0 final.

Backlog real, en una línea

- LP-00: completada (contexto persistido).
- LP-01: Archivero Lore reconcilia PBIs §8 contra disco.
- LP-02: Cristalizador cierra sprints §9.
- LP-03: Cristalizador elimina §10 redundante.
- LP-04: Cristalizador añade features agénticos a §7.
- LP-05: Cristalizador marca §5-§6 como DRY pendiente.
- LP-06: Cristalizador actualiza conteos.
- LP-07: Cristalizador marca como v1.0 final.
- LP-08: Archivero Lore valida plan ↔ disco.

Decisión de producto que se protege\
El plan es del caso, no del mod. Vive en DRAFTS2 siempre. Pero debe estar limpio y cerrado.

Lectura ejecutiva\
Feature de baja complejidad pero alta visibilidad: es la portada del proyecto de lore. 8 ediciones al mismo fichero + 1 validación. LP-01 (reconciliación) es la task crítica: de ella dependen las demás.
