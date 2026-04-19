# Backlog — cortos-legislativa

> **Última actualización:** 19-abr-2026 — GPT-5.4

## Tracking

| Task | Estado | Agente | Dependencias | Entrega | Brief |
|------|--------|--------|--------------|---------|-------|
| CL-00 | cerrada | GPT-5.4 | — | contexto congelado | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| CL-01 | libre | — | CL-00, LP-01b†, UL-01‡ | `lore/derivados/cortos/` con 5 cortos migrados | [TASK-01](./tasks/TASK-01_MIGRAR_CORTOS.md) |
| CL-02 | libre | — | CL-01, UL-01‡, GL-02§ | `mod/agents/dramaturgo.agent.md` adaptado | [TASK-02](./tasks/TASK-02_RECABLEAR_DRAMATURGO.md) |
| CL-03 | libre | — | CL-02, UL-02‡ | `mod/agents/pipeline.agent.md` y refs finales actualizados | [TASK-03](./tasks/TASK-03_AJUSTAR_PIPELINE.md) |
| CL-04 | libre | — | CL-02, CL-03 | Informe de validación de naming y trazabilidad | [TASK-04](./tasks/TASK-04_VALIDAR_CORTOS.md) |

> † LP-01b es del dossier `lore-db-legislativa` — deja la base `lore/` disponible.
> ‡ UL-01 y UL-02 son del dossier `universos-legislativa` — dejan la capa universo lista para Dramaturgo.
> § GL-02 es de `grafo-legislativa` — mantiene artefacto y universo markdown legacy en la ruta nueva.

## Criterio de cierre

- [ ] `LORE_F-02_CORTO*.md` migrados a `lore/derivados/cortos/`
- [ ] `@Dramaturgo Cortos` ya no lee ni escribe cortos en `DRAFTS2/`
- [ ] `@Pipeline` refleja la fase `cortos` como último tramo de la cadena
- [ ] Se preservan sufijos de modelo y trazabilidad por universo