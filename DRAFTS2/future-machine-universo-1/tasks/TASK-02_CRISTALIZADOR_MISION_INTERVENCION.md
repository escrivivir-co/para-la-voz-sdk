# TASK-02 — Cristalizador: misión de intervención

> **Estado:** pendiente
> **Agente recomendado:** `Cristalizador`
> **Dependencias:** FM-00
> **Entrega esperada:** `DRAFTS2/future-machine-universo-1/ENTREGA_FM-02_PROPUESTA_CRISTALIZADOR.md`

## Lee primero

- [Plan inicial local](../PLAN_FUTURE_MACHINE_UNIVERSO1.md)
- [Respuestas del usuario](../RESPUESTAS_USUARIO_FUTURE_MACHINE_UNIVERSO1.md)
- [Plan madre del sprint](../../PLAN_UNIVERSO1_V2.md)
- [Custom agents en COPILOT](../../../COPILOT/custom-agents.instructions.md)
- [Skills en COPILOT](../../../COPILOT/skill.instructions.md)
- [Agents en COPILOT](../../../COPILOT/agents.instructions.md)
- [Prompts en COPILOT](../../../COPILOT/prompt.instructions.md)
- [Hooks en COPILOT](../../../COPILOT/hooks.instructions.md)
- [Skill core futures-engine](../../../.github/skills/futures-engine/SKILL.md)
- [Dramaturgo del mod](../../../mod/agents/dramaturgo.agent.md)

## Objetivo

Diseñar la intervención future-machine para `mod/legislativa`, explotando la carpeta `COPILOT/` como fuente de capacidades y proponiendo todo lo necesario para maximizar uso agéntico en `mod/`.

## Restricciones

- No tocar `.github/`.
- No duplicar contenido ya fijado en el SDK o en el mod salvo que haga falta para un override local justificado.
- Proponer solo artefactos que vivan en `mod/`.
- Tratar `DRAFTS2/` como fuente temporal del lore mientras dure el workaround.

## Salida mínima esperada

1. Propuesta de artefactos en formato Cristalizador.
2. Secuencia recomendada de implementación.
3. Decisión argumentada entre:
   - override local `mod/skills/futures-engine/SKILL.md`;
   - skill nuevo `mod/skills/future-machine/SKILL.md`;
   - combinación de ambos.
4. Recomendación de agentes, prompts, instructions, hooks, subagentes internos o handoffs si aportan valor real.

## Misión sugerida para el agente

Como `@Cristalizador`, lee el contexto compartido de esta carpeta, el skill core `futures-engine`, la extensión actual del mod y la documentación de `COPILOT/`. Propón la intervención future-machine para `mod/legislativa` con foco en `universo-1`. No dupliques el SDK; detecta huecos, overrides locales y wiring faltante. Maximiza el uso agéntico en `mod/` y prioriza artefactos reutilizables. Devuelve una propuesta lista para aprobar e implementar.

## Criterio de aceptación

La propuesta deja claro qué se implementa, por qué, en qué ruta de `mod/`, y qué capacidad de Copilot activa o reutiliza en esta intervención.