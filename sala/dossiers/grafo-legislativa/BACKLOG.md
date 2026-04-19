# Backlog — grafo-legislativa

> **Última actualización:** 19-abr-2026 — Claude Opus 4.6

## Tracking

| Task | Estado | Agente | Dependencias | Entrega | Brief |
|------|--------|--------|--------------|---------|-------|
| GL-00 | cerrada | Claude Opus 4.6 | — | contexto congelado | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| GL-01 | libre | — | GL-00, LP-01b†, GS-01‡ | `lore/derivados/grafo/` con 5 ficheros + index.json actualizado | [TASK-01](./tasks/TASK-01_MIGRAR_GRAFO_JSON.md) |
| GL-02 | libre | — | GL-00, LP-01b† | ~10 ficheros migrados (artefacto, universo md, cortos, ramas) | [TASK-02](./tasks/TASK-02_MIGRAR_DERIVADOS_UNIVERSO.md) |
| GL-03 | libre | — | GL-01, GL-02 | Agentes actualizados (Grafista, Demiurgo, Dramaturgo, Archivero) | [TASK-03](./tasks/TASK-03_ACTUALIZAR_REFS_AGENTES.md) |
| GL-04 | libre | — | GL-03 | Informe de validación: integridad piezas_ancla + agentes operativos | [TASK-04](./tasks/TASK-04_VALIDAR_INTEGRIDAD.md) |

> † LP-01b es del dossier `lore-db-legislativa` — mueve `CORPUS_PREVIEW.md` y `LORE_F.md` a `lore/derivados/`.
> ‡ GS-01 es del dossier `grafo-sdk` — fija el schema genérico que el mod especializa.

## Criterio de cierre

- [ ] `DRAFTS2/grafo/` migrado a `lore/derivados/grafo/` (5 ficheros, `git mv`)
- [ ] `index.json` actualizado con rutas `lore/` (corpus_ref, artefacto_ref, hilo_ref, universo_ref)
- [ ] Artefacto, universo markdown, 5 cortos y 3 ramas migrados a `lore/derivados/`
- [ ] `gramatica.md` cabecera actualizada a `lore/derivados/grafo/`
- [ ] Agentes del mod (Grafista, Demiurgo, Dramaturgo, Archivero) sin refs a `DRAFTS2/`
- [ ] Validación: `piezas_ancla` en nodos.json resuelven contra corpus en ruta nueva
- [ ] `DRAFTS2/grafo/` y `DRAFTS2/universo/` vacíos (solo `.gitkeep` si se conservan)
