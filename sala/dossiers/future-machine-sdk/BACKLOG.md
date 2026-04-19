# Backlog — future-machine-sdk

> **Última actualización:** 19-abr-2026 — GPT-5.4

## Tracking

| Task | Estado | Agente | Dependencias | Entrega | Brief |
|------|--------|--------|--------------|---------|-------|
| FS-00 | cerrada | GPT-5.4 | — | contexto congelado | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| FS-01 | libre | — | FS-00, PS-01†, CS-01‡, GS-01§, US-01¶, COS-01# | `.github/instructions/future-machine-schema.instructions.md` | [TASK-01](./tasks/TASK-01_SCHEMA_Y_SLOTS.md) |
| FS-02 | libre | — | FS-01, PS-05†, CS-04‡, GS-04§, US-03¶, COS-04# | `.github/templates/future-machine.template.md` | [TASK-02](./tasks/TASK-02_TEMPLATE_Y_MANIFEST.md) |
| FS-03 | libre | — | FS-01 | Portal SDK reconoce la future-machine si existe | [TASK-03](./tasks/TASK-03_INTEGRAR_PORTAL_SDK.md) |
| FS-04 | libre | — | FS-01, FS-02, FS-03 | Docs SDK + init de lore actualizados | [TASK-04](./tasks/TASK-04_DOCUMENTAR_CIERRE_Y_INIT.md) |

> † PS-01/PS-05 son del dossier `lore-db-sdk` — schema de piezas y scaffold `lore/`.
> ‡ CS-01/CS-04 son del dossier `corpus-sdk` — schema y cierre de la capa corpus.
> § GS-01/GS-04 son del dossier `grafo-sdk` — schema y cierre de la capa grafo.
> ¶ US-01/US-03 son del dossier `universos-sdk` — schema y cierre de la capa universos.
> # COS-01/COS-04 son del dossier `cortos-sdk` — schema y cierre de la capa obras derivadas.

## Criterio de cierre

- [ ] Existe contrato portable de slots para la machine
- [ ] Existe template de `{{LORE_DIR}}/FUTURE_MACHINE.md`
- [ ] Portal SDK entiende el concepto de machine y sus entrypoints declarados
- [ ] La documentación del SDK trata la machine como cierre compositivo del ciclo, no como capa nueva
- [ ] La inicialización del lore puede dejar preparada la carcasa `future-machine`