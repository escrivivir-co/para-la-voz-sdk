# Backlog — engine-plan-sdk

> **Última actualización:** 20-abr-2026 — Claude Opus 4.6 (Aleph)

## Regla DRY del backlog

El backlog es índice y tracking. El detalle vive en `tasks/`.
No se duplican reglas de `.github/`, `sala/` ni del mod.

## Tracking

| Task | Estado | Agente | Dependencias | Entrega | Brief |
|------|--------|--------|--------------|---------|-------|
| EP-00 | cerrada | Claude Opus 4.6 | — | SKILL.md + prompt + ejemplo | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| EP-01 | libre | — | EP-00 | Protocolo base verificado E2E | [TASK-01](./tasks/TASK-01_PROTOCOLO_BASE_VERIFICADO.md) |
| EP-02 | libre | — | EP-01 | Formato log estandarizado + log-std | [TASK-02](./tasks/TASK-02_LOG_FORMAT_Y_LOG_STD.md) |
| EP-03 | libre | — | EP-01 | Patch cross-branch protocol | [TASK-03](./tasks/TASK-03_PATCH_CROSS_BRANCH.md) |
| EP-04 | libre | — | EP-01 | `diff`, `history`, `validate` por nodo | [TASK-04](./tasks/TASK-04_DIFF_HISTORY_VALIDATE.md) |
| EP-05 | libre | — | EP-01 | `trace {marca}` a lo largo de la cadena | [TASK-05](./tasks/TASK-05_TRACE_MARCA.md) |
| EP-06 | libre | — | EP-05 | `coverage` — porcentaje por capa | [TASK-06](./tasks/TASK-06_COVERAGE.md) |
| EP-07 | libre | — | EP-01, skill `dossier-feature` | `task-suggest` basado en gaps | [TASK-07](./tasks/TASK-07_TASK_SUGGEST.md) |
| EP-08 | libre | — | EP-07 | `sprint-scope` desde ruta crítica | [TASK-08](./tasks/TASK-08_SPRINT_SCOPE.md) |
| EP-09 | libre | — | EP-01 | `dossier-sync` coherencia dossier ↔ sim | [TASK-09](./tasks/TASK-09_DOSSIER_SYNC.md) |
| EP-10 | libre | — | FS-05 (`future-machine-sdk`) | `@Pipeline` real reemplaza simulación | [TASK-10](./tasks/TASK-10_PIPELINE_REAL.md) |
| EP-11 | libre | — | EP-10, hooks `preview` | Hook PostToolUse schema validation | [TASK-11](./tasks/TASK-11_HOOK_POST_TOOL.md) |
| EP-12 | libre | — | EP-10, hooks `preview` | Hook SessionStart auto-status | [TASK-12](./tasks/TASK-12_HOOK_SESSION_START.md) |
| EP-13 | libre | — | EP-10, MCP | MCP server del pipeline | [TASK-13](./tasks/TASK-13_MCP_SERVER.md) |
| EP-14 | libre | — | EP-10, EP-11, EP-13, plugins `preview` | Plugin packaging | [TASK-14](./tasks/TASK-14_PLUGIN_PACKAGING.md) |
| EP-15 | libre | — | EP-01 | Dashboard persistente MACHINE_STATUS.md | [TASK-15](./tasks/TASK-15_DASHBOARD_PERSISTENTE.md) |
| EP-16 | libre | — | EP-04, EP-06 | Métricas de cadena (coverage, drift, stale) | [TASK-16](./tasks/TASK-16_METRICAS_CADENA.md) |
| EP-17 | libre | — | EP-01, skill `futures-engine` | Simulación de futuros del pipeline | [TASK-17](./tasks/TASK-17_FUTUROS_PIPELINE.md) |
| EP-18 | libre | — | EP-07, EP-08 | Auto-priorización de tasks | [TASK-18](./tasks/TASK-18_AUTO_PRIORIZACION.md) |

> Gates condicionados: EP-11, EP-12 requieren hooks `preview`. EP-13 requiere MCP. EP-14 requiere plugins `preview`.

## Criterio de cierre del feature

- [ ] El skill funciona E2E con datos reales de al menos un mod (`mod/legislativa`)
- [ ] Los 11 comandos base del prompt producen output verificable
- [ ] El formato de log es consistente en todas las sesiones
- [ ] `@Pipeline` puede heredar el protocolo del skill cuando exista
- [ ] Al menos un tier 2 integrado (task-suggest o dossier-sync)
