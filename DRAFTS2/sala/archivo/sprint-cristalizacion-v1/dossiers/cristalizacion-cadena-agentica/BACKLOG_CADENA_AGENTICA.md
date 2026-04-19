# Backlog — Cristalización de la cadena agéntica

> **Fecha de apertura:** 19-abr-2026
> **Estado:** abierto
> **Modelo de inicialización:** `Claude Opus 4.6`
> **Anclas:** `mod/agents/`, `DRAFTS2/LORE_F-02_UNIVERSO.md`

## Contexto compartido

Todos los tasks heredan este contexto:

- [Plan local](./PLAN_CADENA_AGENTICA.md)
- [Respuestas del usuario](./RESPUESTAS_USUARIO_CADENA_AGENTICA.md)
- [Skill cristalización-feature](../../mod/skills/cristalizacion-feature/SKILL.md)
- [Agentes actuales del mod](../../mod/agents/) — estado previo al refactor
- [Skill futures-engine](../../.github/skills/futures-engine/SKILL.md) — 5 fases (inmutable)
- [LORE_INDEX.md](../LORE_INDEX.md) — inventario de piezas (consume Puzzle)
- [lore-schema.instructions.md](../../mod/instructions/lore-schema.instructions.md) — esquema de tipos (si existe)

## Regla DRY del backlog

- El backlog es índice y tracking.
- El detalle vive en `tasks/`.
- No se duplican reglas de `.github/`, `mod/` ni del plan.

## Tracking

| Task | Estado | Agente recomendado | Modelo | Dependencias | Entrega | Brief |
|---|---|---|---|---|---|---|
| CA-00 | **Completado** | `Claude Opus 4.6` | `Claude Opus 4.6` | — | plan + backlog + respuestas | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| CA-01 | Pendiente | `Cristalizador` | modelo activo | CA-00 | `mod/agents/puzzle.agent.md` | [TASK-01](./tasks/TASK-01_PUZZLE.md) |
| CA-02 | Pendiente | `Cristalizador` | modelo activo | CA-01 | refactor `archivero-lore.agent.md` | [TASK-02](./tasks/TASK-02_REFACTOR_ARCHIVERO_LORE.md) |
| CA-03 | Pendiente | `Cristalizador` | modelo activo | CA-00 | refactor `grafista.agent.md` | [TASK-03](./tasks/TASK-03_REFACTOR_GRAFISTA.md) |
| CA-04 | Pendiente | `Cristalizador` | modelo activo | CA-03 | `mod/agents/demiurgo.agent.md` | [TASK-04](./tasks/TASK-04_DEMIURGO.md) |
| CA-05 | Pendiente | `Cristalizador` | modelo activo | CA-04 | recablear `dramaturgo.agent.md` | [TASK-05](./tasks/TASK-05_RECABLEAR_DRAMATURGO.md) |
| CA-06 | Pendiente | `Cristalizador` | modelo activo | CA-01..CA-05 | actualizar `pipeline.agent.md` | [TASK-06](./tasks/TASK-06_ACTUALIZAR_PIPELINE.md) |
| CA-07 | Pendiente | `Pipeline` | modelo activo | CA-06 | informe de validación | [TASK-07](./tasks/TASK-07_VALIDACION_CADENA.md) |

## Dependencias entre tasks

```
CA-00 (contexto)
  ├── CA-01 (Puzzle) ──→ CA-02 (refactor Archivero Lore)
  └── CA-03 (refactor Grafista) ──→ CA-04 (Demiurgo) ──→ CA-05 (recablear Dramaturgo)
                                                              │
CA-01..CA-05 ─────────────────────────────────────────→ CA-06 (Pipeline)
                                                              │
                                                        CA-07 (validación)
```

CA-01 y CA-03 pueden ejecutarse **en paralelo**.

## Criterio de cierre del feature

1. Existen los 5 agentes como `.agent.md` en `mod/agents/` con roles disjuntos.
2. Cada agente tiene handoffs al siguiente en la cadena.
3. Pipeline tiene handoffs actualizados a los 5 agentes.
4. Ningún agente mezcla dos transformaciones (e.g., Grafista no genera universos).
5. `@Pipeline /refresh status` recorre la cadena completa sin error de handoff.
