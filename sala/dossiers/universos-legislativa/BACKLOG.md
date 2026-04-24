# Backlog — universos-legislativa

> **Última actualización:** 19-abr-2026 — GPT-5.4

## Tracking

| Task | Estado | Agente | Dependencias | Entrega | Brief |
|------|--------|--------|--------------|---------|-------|
| UL-00 | cerrada | GPT-5.4 | — | contexto congelado | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| UL-01 | libre | — | UL-00, LP-01b†, GL-01‡, GL-02‡ | `lore/derivados/universo/` con 3 universos migrados | [TASK-01](./tasks/TASK-01_MIGRAR_UNIVERSOS.md) |
| UL-02 | libre | — | UL-01, GL-01‡, GL-02‡ | Demiurgo y Pipeline conectados a `lore/derivados/universo/` | [TASK-02](./tasks/TASK-02_RECABLEAR_UNIVERSOS.md) |
| UL-03 | libre | — | UL-01, GL-02‡ | `legislativa-universo.instructions.md` adaptado | [TASK-03](./tasks/TASK-03_ADAPTAR_UNIVERSO_INSTRUCTIONS.md) |
| UL-04 | libre | — | UL-02, UL-03 | Informe de validación de la cadena `grafo -> universo` + handoff a cortos | [TASK-04](./tasks/TASK-04_VALIDAR_CADENA.md) |

> † LP-01b es del dossier `lore-db-legislativa` — mueve a `lore/` el corpus y el hilo base.
> ‡ GL-01 y GL-02 son de `grafo-legislativa` — proveen el grafo JSON y los artefactos markdown del grafo.

## Criterio de cierre

- [ ] `DRAFTS2/universo/` migrado a `lore/derivados/universo/` con los 3 universos existentes
- [ ] `@Demiurgo` ya no lee ni escribe universos en `DRAFTS2/`
- [ ] `@Pipeline` refleja la etapa universo dentro de la cadena nueva y entrega hacia `cortos`
- [ ] `mod/instructions/legislativa-universo.instructions.md` ya no aplica a `DRAFTS2/**`
- [ ] La secuencia `grafo -> universos` queda conectada sin refs obsoletas

## Downstream: future-machine-legislativa

> UL-01 (migrar universos) → FL-01 (`slot_universos`).