# Backlog — future-machine-sdk

> **Última actualización:** 19-abr-2026 — Claude Opus 4.6 (refactor Cristalizador)

## Regla DRY del backlog

El backlog es índice y tracking. El detalle vive en `tasks/`.
No se duplican reglas de `.github/`, `sala/` ni del mod.

## Tracking

| Task | Estado | Agente | Dependencias | Entrega | Brief |
|------|--------|--------|--------------|---------|-------|
| FS-00 | cerrada | GPT-5.4 | — | contexto congelado | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| FS-01 | libre | — | FS-00, PS-01†, CS-01‡, GS-01§, US-01¶, COS-01# | `.github/instructions/future-machine-schema.instructions.md` | [TASK-01](./tasks/TASK-01_SCHEMA_Y_SLOTS.md) |
| FS-02 | libre | — | FS-01, PS-05†, CS-04‡, GS-04§, US-03¶, COS-04# | `.github/templates/future-machine.template.md` | [TASK-02](./tasks/TASK-02_TEMPLATE_Y_MANIFEST.md) |
| FS-03 | libre | — | FS-01 | Portal SDK reconoce la future-machine si existe | [TASK-03](./tasks/TASK-03_INTEGRAR_PORTAL_SDK.md) |
| FS-04 | libre | — | FS-01, FS-02, FS-03, FS-05, FS-06 | Docs SDK + init de lore actualizados | [TASK-04](./tasks/TASK-04_DOCUMENTAR_CIERRE_Y_INIT.md) |
| FS-05 | libre | — | FS-01 | `.github/agents/pipeline.agent.md` | [TASK-05](./tasks/TASK-05_PIPELINE_SDK.md) |
| FS-06 | libre | — | FS-01, FS-05 | 3 prompts de entrypoint base | [TASK-06](./tasks/TASK-06_ENTRYPOINTS_SDK.md) |

> † PS-01/PS-05 — `lore-db-sdk` (schema de piezas y scaffold `lore/`).
> ‡ CS-01/CS-04 — `corpus-sdk` (schema y cierre de la capa corpus).
> § GS-01/GS-04 — `grafo-sdk` (schema y cierre de la capa grafo).
> ¶ US-01/US-03 — `universos-sdk` (schema y cierre de la capa universos).
> # COS-01/COS-04 — `cortos-sdk` (schema y cierre de la capa obras derivadas).

## Criterio de cierre

- [ ] `@Pipeline` SDK existe con contrato de refresh genérico basado en manifiesto de slots
- [ ] Existen 3 prompts de entrypoint base (`machine-start`, `machine-status`, `machine-refresh`)
- [ ] Existe contrato portable de slots para la machine (`.github/instructions/future-machine-schema.instructions.md`)
- [ ] Existe template de `{{LORE_DIR}}/FUTURE_MACHINE.md`
- [ ] Portal SDK detecta y presenta la machine si el mod la declara
- [ ] La documentación del SDK trata la machine como cierre compositivo del ciclo
- [ ] La inicialización del lore puede dejar preparada la carcasa `future-machine`
- [ ] `mod/legislativa` puede heredar `@Pipeline` SDK y rellenarlo con su cadena sin rotura

## Notas pendientes para dossiers hermanos

Ver sección 7 de [PLAN.md](./PLAN.md). Las notas van dirigidas a:
- `lore-db-sdk` — dualidad piezas/LORE_F
- `corpus-sdk` — protocolo de acumulación del merge
- `grafo-sdk` — doble fuente de datos + ponderación de plausibilidad
- `universos-sdk` — universo = rellenar variables + elegir inicializaciones
- `cortos-sdk` — producciones al uso en lenguaje natural