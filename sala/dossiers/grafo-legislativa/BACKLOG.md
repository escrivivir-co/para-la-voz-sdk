# Backlog — grafo-legislativa

> **Última actualización:** 19-abr-2026 — Claude Opus 4.6

## Tracking

| Task | Estado | Agente | Dependencias | Entrega | Brief |
|------|--------|--------|--------------|---------|-------|
| GL-00 | cerrada | Claude Opus 4.6 | — | contexto congelado | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| GL-01 | libre | — | GL-00, LP-01b†, CP-01‡, GS-01§ | `lore/derivados/grafo/` con 5 ficheros + index.json actualizado | [TASK-01](./tasks/TASK-01_MIGRAR_GRAFO_JSON.md) |
| GL-02 | libre | — | GL-00, LP-01b†, CP-01‡ | `LORE_F-02_ARTEFACTO.md` + `LORE_F-02_UNIVERSO.md` migrados | [TASK-02](./tasks/TASK-02_MIGRAR_ARTEFACTOS_GRAFO.md) |
| GL-03 | libre | — | GL-01, GL-02 | Grafo consumible desde Grafista, Archivero e instructions del mod | [TASK-03](./tasks/TASK-03_ACTUALIZAR_REFS_AGENTES.md) |
| GL-04 | libre | — | GL-03 | Informe de validación: integridad piezas_ancla + agentes operativos | [TASK-04](./tasks/TASK-04_VALIDAR_INTEGRIDAD.md) |

> † LP-01b es del dossier `lore-db-legislativa` — deja piezas + `LORE_F.md` migrados a `lore/`.
> ‡ CP-01 es del dossier `corpus-legislativa` — materializa el corpus canónico fuera de `DRAFTS2/`.
> § GS-01 es del dossier `grafo-sdk` — fija el schema genérico que el mod especializa.

## Criterio de cierre

- [ ] `DRAFTS2/grafo/` migrado a `lore/derivados/grafo/` (5 ficheros, `git mv`)
- [ ] `index.json` actualizado con rutas `lore/` (corpus_ref, artefacto_ref, hilo_ref, universo_ref)
- [ ] `LORE_F-02_ARTEFACTO.md` y `LORE_F-02_UNIVERSO.md` migrados a `lore/derivados/`
- [ ] `gramatica.md` cabecera actualizada a `lore/derivados/grafo/`
- [ ] Consumidores del grafo (Grafista, Archivero e instructions del mod) sin refs obsoletas a `DRAFTS2/`
- [ ] Validación: `piezas_ancla` en nodos.json resuelven contra `corpus/corpus.md` o routing canónico equivalente
- [ ] `DRAFTS2/grafo/` vacío o reducido a `.gitkeep` tras la migración

## Downstream: future-machine-legislativa

> GL-01 (migrar grafo JSON) → FL-01 (`slot_grafo`). GL-02 (artefactos markdown) → FL-01.
