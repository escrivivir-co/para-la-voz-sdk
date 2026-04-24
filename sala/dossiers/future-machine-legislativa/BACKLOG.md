# Backlog — future-machine-legislativa

> **Última actualización:** 19-abr-2026 — GPT-5.4

## Tracking

| Task | Estado | Agente | Dependencias | Entrega | Brief |
|------|--------|--------|--------------|---------|-------|
| FL-00 | cerrada | GPT-5.4 | — | contexto congelado | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| FL-01 | libre | — | FL-00, FS-02†, LP-01b‡, CP-01§, GL-01¶, UL-01#, CL-01** | `lore/FUTURE_MACHINE.md` instanciado | [TASK-01](./tasks/TASK-01_INSTANTIAR_MACHINE.md) |
| FL-02 | libre | — | FL-01, LP-04‡‡, LP-05‡‡ | Pipeline y lore-pipeline adaptados a la machine | [TASK-02](./tasks/TASK-02_CONECTAR_PIPELINE.md) |
| FL-03 | libre | — | FL-01 | Portal + start here + status conectados | [TASK-03](./tasks/TASK-03_CONECTAR_PORTAL_Y_ENTRYPOINTS.md) |
| FL-04 | libre | — | FL-01, FL-02, FL-03 | Datos y slots reales levantados en el manifest | [TASK-04](./tasks/TASK-04_LEVANTAR_DATOS_ACTUALES.md) |
| FL-05 | libre | — | FL-02, FL-03, FL-04 | Informe de validación del cierre de ciclo | [TASK-05](./tasks/TASK-05_VALIDAR_CIERRE_DE_CICLO.md) |

> † FS-02 es del dossier `future-machine-sdk`.
> ‡ LP-01b es del dossier `lore-db-legislativa`.
> § CP-01 es del dossier `corpus-legislativa`.
> ¶ GL-01 es del dossier `grafo-legislativa`.
> # UL-01 es del dossier `universos-legislativa`.
> ** CL-01 es del dossier `cortos-legislativa`.
> ‡‡ LP-04 y LP-05 son del dossier `lore-db-legislativa`.

## Criterio de cierre

- [ ] Existe `lore/FUTURE_MACHINE.md` con slots reales del caso Feo
- [ ] `Portal`, `/user-empieza-aqui` y `/lore-status` presentan la machine del mod
- [ ] `Pipeline` aparece como slot técnico de refresh dentro del ciclo
- [ ] El manifest levanta corpus, grafo, universos y cortos ya existentes
- [ ] El cierre de ciclo queda validado de punta a punta