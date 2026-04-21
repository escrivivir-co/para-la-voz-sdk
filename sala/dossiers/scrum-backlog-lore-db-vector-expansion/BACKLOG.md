# Backlog — scrum-backlog-lore-db-vector-expansion

> **Última actualización:** 22-abr-2026 — GPT-5.4

## Contexto compartido

- Referencias compartidas y trabajo avanzado: `ref/INDEX.md`
- Plan compartido del equipo transversal: `../../../../sala/dossiers/scrum-backlog-lore-db-vector-expansion/PLAN.md`
- Ancla local previa: `sala/dossiers/lore-db-sdk/PLAN.md`

## Regla DRY del backlog

Este backlog no replica el plan compartido ni la investigación del día. Solo indexa el trabajo del frente `DocumentMachineSDK`.

## Tracking

| Task | Estado | Agente | Dependencias | Entrega | Brief |
|------|--------|--------|--------------|---------|-------|
| SBLVX-DM-00 | cerrada | GPT-5.4 | — | definiciones pre-scrum locales congeladas | [TASK-00](./tasks/TASK-00_PRESCRUM_DEFINITIONS.md) |
| SBLVX-DM-01 | cerrada | GPT-5.4 | SBLVX-DM-00 | planificación local DRY y sesión inicializada | [TASK-01](./tasks/TASK-01_PLANIFICATION_DRY.md) |
| SBLVX-DM-02 | libre | vacante | SBLVX-DM-01 | plan compartido aprobado o enmendado desde el frente documental | [TASK-02](./tasks/TASK-02_REFINEMENT_APROBAR_O_ENMENDAR_PLAN.md) |
| SBLVX-DM-03 | libre | vacante | SBLVX-DM-02 | refinement local de skill y layout de datos | [TASK-03](./tasks/TASK-03_REFINEMENT_SKILL_Y_LAYOUT_LOCAL.md) |
| SBLVX-DM-04 | libre | vacante | SBLVX-DM-02, SBLVX-DM-03 | handoff documental listo para integrar | [TASK-04](./tasks/TASK-04_HANDOFF_DOCUMENTAL.md) |

## Criterio de cierre del feature

- [ ] El frente documental aprueba o enmienda el plan compartido.
- [ ] El scope local del skill y del layout queda refinado sin duplicar la arquitectura global.
- [ ] Queda preparado el handoff de integración hacia Scriptorium.