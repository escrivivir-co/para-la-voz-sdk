# TASK-03 — Ampliar Dramaturgo SDK para leer grafo

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** GS-01
> **Entrega esperada:** edición de `.github/agents/dramaturgo.agent.md`

## Lee primero

- [Plan §4.4](../PLAN.md)
- `.github/agents/dramaturgo.agent.md`
- `.github/skills/futures-engine/SKILL.md`

## Objetivo

Ampliar el Dramaturgo SDK para que reconozca el concepto de grafo de bifurcación si un mod lo define, sin asumir tipos concretos ni reemplazar al Grafista del mod.

## Cambios esperados

1. Añadir referencia a `{{LORE_DIR}}/derivados/grafo/` como fuente opcional
2. Explicar que el Dramaturgo puede leer un grafo si existe antes de bifurcar
3. Mantener el handoff al Grafista del mod como especialización opcional

## Criterio de aceptación

El Dramaturgo SDK entiende el concepto de grafo y sigue siendo portable para mods sin `grafo/`.