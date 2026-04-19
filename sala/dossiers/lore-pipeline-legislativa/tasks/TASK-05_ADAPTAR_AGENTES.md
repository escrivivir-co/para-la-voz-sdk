# TASK-05 — Adaptar agentes del mod para referenciar SDK

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** LP-02, LP-04
> **Entrega esperada:** ediciones de agentes en `mod/agents/`

## Lee primero

- [Plan §4.5](../PLAN.md)
- `mod/agents/archivero-lore.agent.md`
- `mod/agents/puzzle.agent.md`
- `mod/agents/pipeline.agent.md`
- `.github/agents/archivero.agent.md` — el SDK base que extienden

## Objetivo

Adaptar los agentes del mod para que referencien el protocolo genérico del SDK y la nueva instruction de pipeline.

## Cambios esperados

### archivero-lore.agent.md
- Sección "Fuentes que lees" → añadir `pieza-schema.instructions.md` del SDK antes del lore-schema
- Sección "Por qué existes" → mencionar que hereda del archivero SDK que ahora entiende piezas genéricas

### puzzle.agent.md
- Sección "Fuentes que lees" → añadir `pieza-schema.instructions.md` del SDK
- Paso 1 → cargar schema SDK primero, luego schema del mod

### pipeline.agent.md
- Añadir referencia a `lore-pipeline.instructions.md` como grafo de dependencias formalizado
- Los pasos de refresh ya referencian los nodos — solo se actualiza la fuente

## Qué NO se toca

- Los agentes SDK (`.github/agents/`) no se tocan aquí — eso es PS-03
- No se crean agentes nuevos
- Los handoffs no cambian

## Criterio de aceptación

Los 3 agentes del mod referencian el SDK genérico y la instruction de pipeline formalizada.
