# TASK-01 — Refactorizar el agente core

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** CR-00
> **Entrega esperada:** `.github/agents/cristalizador.agent.md` refactorizado

## Lee primero

1. `.github/agents/cristalizador.agent.md` — contrato actual
2. `.github/prompts/design.prompt.md` — superficie de entrada
3. `.github/copilot-instructions.md` — flujo `main -> mod/*`
4. `README.md` § `COPILOT/ — Sincronización mensual`
5. `sala/archivo/sprint-cristalizacion-v1/dossiers/future-machine-universo-1/PLAN_FUTURE_MACHINE_UNIVERSO1.md`
6. `sala/archivo/sprint-cristalizacion-v1/dossiers/future-machine-universo-1/tasks/TASK-02_CRISTALIZADOR_MISION_INTERVENCION.md`
7. `sala/archivo/sprint-cristalizacion-v1/dossiers/future-machine-universo-1/tasks/TASK-06_WARNING_MAIN_SI_APLICA.md`
8. `COPILOT/indice.md` y los documentos concretos que el agente necesite según la misión (`custom-agents`, `skills`, `hooks`, `agents`, `mcp`, `language-models`, `tools`, `plugins`, `context`)

## Objetivo

Refactorizar el agente core para que el Cristalizador quede definido como agente SDK por defecto, con comportamiento branch-aware, consulta real de `COPILOT/` y pacto explícito con el usuario antes de maximizar con features condicionadas.

## Cambios requeridos

1. **Default SDK + override local:** dejar explícito que este agente vive en `main` y que un mod solo lo sustituye si crea `mod/agents/cristalizador.agent.md`.
2. **Superficie de escritura:** distinguir entre refactor SDK en `main`, extensión de `mod/` y trabajo de sala. En ramas `mod/*`, `.github/` y `COPILOT/` quedan como referencia.
3. **Lookup documental real:** sustituir el catálogo cerrado por un protocolo de consulta que parta de `COPILOT/indice.md` y baje a la familia documental relevante.
4. **Registro de capacidad:** reportar, al menos en la respuesta, el delta entre capacidades ya usadas, capacidades disponibles y capacidades condicionadas por preview/admin/premium.
5. **Pacto de maximización:** si la propuesta depende de preview, gating organizacional, premium requests, instalaciones extra, plugins o MCP, el agente debe explicitarlo y pedir acuerdo.
6. **Salida enriquecida:** cada propuesta debe declarar docs consultados, superficie objetivo (`main` o `mod`), gates operativos y fallback baseline si existe.
7. **Sin lore fijo:** no introducir referencias a legislativa ni a ningún mod concreto.

## Salida mínima esperada

1. Candidato de `.github/agents/cristalizador.agent.md` en carpeta temporal del agente.
2. ENTREGA con diff y explicación de los cambios de contrato.

## Criterio de aceptación

- El agente deja clara la herencia `main -> mod`.
- En una rama `mod/*`, el contrato impide escribir en `.github/` como vía normal.
- El agente ya no depende de una lista fija y cerrada de documentos `COPILOT/`.
- Las respuestas del Cristalizador hacen visible el pacto de maximización con el usuario.
- Grep de `legislativa|DRAFTS2|future-machine-universo-1` en el candidato = 0 hits.