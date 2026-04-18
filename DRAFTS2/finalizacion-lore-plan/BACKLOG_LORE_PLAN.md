# Backlog — Finalización del LORE_PLAN

> **Fecha de apertura:** 19-abr-2026
> **Estado:** abierto
> **Modelo de inicialización:** `Claude Opus 4.6`
> **Anclas:** `DRAFTS2/LORE_PLAN.md`, `DRAFTS2/LORE_INDEX.md`

## Contexto compartido

Todos los tasks heredan este contexto:

- [Plan local](./PLAN_LORE_PLAN.md)
- [Respuestas del usuario](./RESPUESTAS_USUARIO_LORE_PLAN.md)
- [Skill cristalización-feature](../../mod/skills/cristalizacion-feature/SKILL.md)
- [LORE_PLAN.md](../LORE_PLAN.md) — el fichero a finalizar
- [LORE_INDEX.md](../LORE_INDEX.md) — inventario canónico de piezas
- [mod_legislativa_INDEX.md](../mod_legislativa_INDEX.md) — spec de separación de capas

## Regla DRY del backlog

- El backlog es índice y tracking.
- El detalle vive en `tasks/`.
- No se duplican reglas de `.github/`, `mod/` ni del plan.

## Tracking

| Task | Estado | Agente recomendado | Modelo | Dependencias | Entrega | Brief |
|---|---|---|---|---|---|---|
| LP-00 | **Completado** | `Claude Opus 4.6` | `Claude Opus 4.6` | — | plan + backlog + respuestas | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| LP-01 | Pendiente | `Archivero Lore` | modelo activo | LP-00 | reconciliación §8 | [TASK-01](./tasks/TASK-01_RECONCILIAR_PBIS.md) |
| LP-02 | Pendiente | `Cristalizador` | modelo activo | LP-01 | cierre sprints §9 | [TASK-02](./tasks/TASK-02_CERRAR_SPRINTS.md) |
| LP-03 | Pendiente | `Cristalizador` | modelo activo | LP-01 | eliminar §10 | [TASK-03](./tasks/TASK-03_ELIMINAR_REDUNDANCIAS.md) |
| LP-04 | Pendiente | `Cristalizador` | modelo activo | LP-00 | sección features agénticos §7 | [TASK-04](./tasks/TASK-04_FEATURES_AGENTICOS.md) |
| LP-05 | Pendiente | `Cristalizador` | modelo activo | LP-00 | preparar DRY §5-§6 | [TASK-05](./tasks/TASK-05_DRY_SCHEMA.md) |
| LP-06 | Pendiente | `Cristalizador` | modelo activo | LP-01 | actualizar conteos | [TASK-06](./tasks/TASK-06_CONTEOS.md) |
| LP-07 | Pendiente | `Cristalizador` | modelo activo | LP-01..LP-06 | marcar como v1.0 final | [TASK-07](./tasks/TASK-07_MARCAR_FINAL.md) |
| LP-08 | Pendiente | `Archivero Lore` | modelo activo | LP-07 | validación plan ↔ disco | [TASK-08](./tasks/TASK-08_VALIDACION.md) |

## Dependencias entre tasks

```
LP-00 (contexto)
  ├── LP-01 (reconciliar PBIs) ──→ LP-02 (cerrar sprints) ──→ LP-03 (eliminar §10)
  │                             └──→ LP-06 (conteos)
  ├── LP-04 (features agénticos) ──────────────────────────────────┐
  └── LP-05 (DRY schema) ─────────────────────────────────────────┤
                                                                    │
LP-01..LP-06 ──────────────────────────────────────────→ LP-07 (marcar final)
                                                                    │
                                                              LP-08 (validación)
```

LP-04 y LP-05 pueden ejecutarse **en paralelo** con LP-01.

## Criterio de cierre del feature

1. Todos los PBIs de §8 tienen estado verificado contra disco.
2. Los sprints completados tienen marca de cierre con fecha.
3. No hay secciones redundantes (§10 eliminado o sustituido).
4. Los features agénticos están referenciados.
5. Las DoR/DoD están marcadas como "pendientes de migración a lore-schema".
6. Los conteos son correctos (51 piezas).
7. La cabecera dice "v1.0 final".
