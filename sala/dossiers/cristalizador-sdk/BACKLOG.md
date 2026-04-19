# Backlog — cristalizador-sdk

> **Última actualización:** 19-abr-2026 — GPT-5.4

## Tracking

| Task | Estado | Agente | Dependencias | Entrega | Brief |
|------|--------|--------|--------------|---------|-------|
| CR-00 | cerrada | GPT-5.4 | — | contexto congelado | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| CR-01 | libre | — | CR-00 | `.github/agents/cristalizador.agent.md` refactorizado | [TASK-01](./tasks/TASK-01_REFACTORIZAR_AGENTE_CORE.md) |
| CR-02 | libre | — | CR-01 | `/design` + ciclo documental alineados | [TASK-02](./tasks/TASK-02_REFACTORIZAR_DESIGN_Y_CICLO.md) |
| CR-03 | libre | — | CR-01 | gobernanza de `COPILOT/` + alerta de frescura | [TASK-03](./tasks/TASK-03_GOBERNANZA_COPILOT_Y_ALERTA.md) |
| CR-04 | libre | — | CR-02, CR-03 | documentación SDK coherente con el nuevo contrato | [TASK-04](./tasks/TASK-04_DOCUMENTAR_CONTRATO_SDK.md) |

## Criterio de cierre

- [ ] El Cristalizador de `.github/` queda definido como agente por defecto de `main`, heredable por los mods salvo override local
- [ ] El contrato branch-aware distingue con claridad entre refactor SDK y extensión de mod
- [ ] `/design` y el guion de ciclo reportan lectura real de `COPILOT/`, target de escritura y gates de aprobación
- [ ] Existe gobernanza auditable para la frescura de `COPILOT/` y un warning utilizable aunque no haya hooks
- [ ] `.github/copilot-instructions.md` y `README.md` documentan la herencia `main -> mod`, el pacto de maximización y la política de sync de `COPILOT/`