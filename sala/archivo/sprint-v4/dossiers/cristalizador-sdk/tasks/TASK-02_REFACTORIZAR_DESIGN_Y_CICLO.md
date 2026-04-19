# TASK-02 — Refactorizar `/design` y el ciclo

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** CR-01
> **Entrega esperada:** `.github/prompts/design.prompt.md` y `.github/templates/guion-ciclo.template.md` alineados

## Lee primero

1. `.github/prompts/design.prompt.md`
2. `.github/templates/guion-ciclo.template.md`
3. `.github/agents/cristalizador.agent.md` ya refactorizado por CR-01
4. `README.md` § `COPILOT/ — Sincronización mensual`

## Objetivo

Alinear la superficie `/design` y la documentación del ciclo con el nuevo contrato del Cristalizador, de modo que el usuario vea la consulta a `COPILOT/`, la frontera `main/mod` y los gates de aprobación antes de implementar.

## Cambios requeridos

1. **Consulta documental explícita:** `/design` debe pedir al agente que reporte qué documentos de `COPILOT/` leyó para la petición actual.
2. **Superficie objetivo:** la salida debe indicar si la propuesta va a `main`, a `mod/` o si abre warning/dossier para `main`.
3. **Pacto previo:** la prompt y el guion deben reforzar que primero se propone y se pacta; solo después se implementa.
4. **Maximización condicionada:** si la variante reforzada usa preview, hooks, plugins, MCP o modelos con costes/opt-in, debe aparecer en la propuesta.
5. **Ciclo documental:** el guion debe dejar claro que Cristalizador es el cierre de aprendizaje del ciclo y no solo una fábrica de archivos en `mod/`.
6. **Sin lore específico:** mantenerlo genérico para cualquier mod.

## Criterio de aceptación

- `/design` no se limita a "lee estas 5 docs", sino que pide lookup real según la misión.
- El guion de ciclo describe correctamente la frontera `main/mod`.
- Sigue siendo obligatorio aprobar antes de implementar.
- El texto no induce a editar `.github/` desde una rama `mod/*`.