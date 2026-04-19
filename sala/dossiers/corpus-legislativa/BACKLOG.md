# Backlog — corpus-legislativa

> **Última actualización:** 19-abr-2026 — GPT-5.4

## Tracking

| Task | Estado | Agente | Dependencias | Entrega | Brief |
|------|--------|--------|--------------|---------|-------|
| CP-00 | cerrada | GPT-5.4 | — | contexto congelado | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| CP-01 | libre | — | CP-00, CS-01†, LP-01b‡ | `corpus/` materializado como capa real | [TASK-01](./tasks/TASK-01_MATERIALIZAR_CAPA_CORPUS.md) |
| CP-02 | libre | — | CP-01, LP-01b‡ | `corpus/documentos/` y `corpus/analisis/` definidos/documentados | [TASK-02](./tasks/TASK-02_DOCUMENTOS_Y_ANALISIS.md) |
| CP-03 | libre | — | CP-01, CP-02, CS-02† | `mod/agents/archivero-lore.agent.md` y `lore-ingest` adaptados | [TASK-03](./tasks/TASK-03_ADAPTAR_ARCHIVERO_Y_INGEST.md) |
| CP-04 | libre | — | CP-03 | Consumidores downstream del corpus actualizados | [TASK-04](./tasks/TASK-04_RECABLEAR_CONSUMIDORES.md) |
| CP-05 | libre | — | CP-03, CP-04 | Informe de compatibilidad corpus SDK/mod | [TASK-05](./tasks/TASK-05_VALIDAR_COMPATIBILIDAD.md) |

> † CS-01 y CS-02 son del dossier `corpus-sdk` — fijan contrato y rol del Archivero.
> ‡ LP-01b es del dossier `lore-db-legislativa` — deja las piezas migradas a la lore-db.

## Criterio de cierre

- [ ] `corpus/` deja de ser un shim y pasa a ser capa real del mod
- [ ] `DRAFTS2/CORPUS_PREVIEW.md` deja de ser la ruta canónica pública
- [ ] `@Archivero Legislativa` queda claramente definido como especialización corpus del SDK
- [ ] `@Grafista`, `@Demiurgo`, `@Dramaturgo Cortos`, `@Pipeline` y el Portal consumen corpus canónico
- [ ] Se mantiene compatibilidad con prompts SDK y con `/lore-ingest`