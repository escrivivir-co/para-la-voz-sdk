# Backlog — Cristalización del pipeline operativo

> **Fecha de apertura:** 18-abr-2026
> **Estado:** abierto
> **Modelo de inicialización:** `Claude Opus 4.6`
> **Anclas:** `mod/agents/pipeline.agent.md`, `DRAFTS2/FEAT-06_PIPELINE_REFRESH.md`

## Contexto compartido

Todos los tasks heredan este contexto:

- [Plan local](./PLAN_PIPELINE_OPERATIVO.md)
- [Respuestas del usuario](./RESPUESTAS_USUARIO_PIPELINE_OPERATIVO.md)
- [Protocolo refresh](../FEAT-06_PIPELINE_REFRESH.md)
- [Agente pipeline](../../mod/agents/pipeline.agent.md)
- [LORE_PLAN.md](../LORE_PLAN.md) — §3.1 (regla por formato), §5 (DoR), §6 (DoD)
- [LORE_INDEX.md](../LORE_INDEX.md) — inventario actual
- [Skill cristalización-feature](../../mod/skills/cristalizacion-feature/SKILL.md)

## Regla DRY del backlog

- El backlog es índice y tracking.
- El detalle vive en `tasks/`.
- No se duplican reglas de `.github/`, `mod/` ni del plan.

## Tracking

| Task | Estado | Agente recomendado | Modelo | Dependencias | Entrega | Brief |
|---|---|---|---|---|---|---|
| PO-00 | **Completado** | `Claude Opus 4.6` | `Claude Opus 4.6` | — | plan + backlog + conversación simulada | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| PO-01 | Pendiente | `Cristalizador` | modelo activo | PO-00 | `mod/instructions/lore-schema.instructions.md` | [TASK-01](./tasks/TASK-01_LORE_SCHEMA.md) |
| PO-02 | Pendiente | `Cristalizador` | modelo activo | PO-01 | `mod/instructions/lore-estado.instructions.md` | [TASK-02](./tasks/TASK-02_LORE_ESTADO.md) |
| PO-03 | Pendiente | `Cristalizador` | modelo activo | PO-02 | `mod/instructions/lore-routing.instructions.md` | [TASK-03](./tasks/TASK-03_LORE_ROUTING.md) |
| PO-04 | Pendiente | `Cristalizador` | modelo activo | PO-02 | actualización `legislativa-universo.instructions.md` | [TASK-04](./tasks/TASK-04_UPDATE_UNIVERSO_INSTRUCTIONS.md) |
| PO-05 | Pendiente | `Pipeline` | modelo activo | PO-01..PO-04 | validación `@Pipeline /refresh status` | [TASK-05](./tasks/TASK-05_VALIDACION_PIPELINE.md) |

## Criterio de cierre del feature

1. Existe un esquema de tipos de pieza en `mod/instructions/` consumible por agentes.
2. Existe un fichero de estado canónico del lore con conteos verificables.
3. Existe un mapa de rutas canónicas que resuelve el workaround DRAFTS2.
4. `legislativa-universo.instructions.md` no duplica conteos: referencia al estado canónico.
5. `@Pipeline /refresh status` funciona sin workaround ad hoc.
