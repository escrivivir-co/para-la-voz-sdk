# TASK-01 — Crear schema genérico de grafo

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** GS-00
> **Entrega esperada:** `.github/instructions/grafo-schema.instructions.md`

## Lee primero

- [Plan §4.1](../PLAN.md)
- [BACKLOG](../BACKLOG.md)
- `.github/skills/futures-engine/SKILL.md`
- `DRAFTS2/grafo/gramatica.md` — referencia concreta del mod

## Objetivo

Extraer al SDK la estructura mínima de un grafo de bifurcación sin asumir tipos concretos del mod. El schema debe definir qué es un nodo, un arco y un hueco, y qué campos mínimos debe tener cada uno.

## Cambios esperados

1. Crear `.github/instructions/grafo-schema.instructions.md`
2. Definir estructura mínima de nodos, arcos y huecos
3. Explicar qué parte define el SDK y qué parte especializa cada mod
4. Referenciar la convención `{{LORE_DIR}}/derivados/grafo/`

## Criterio de aceptación

Existe `.github/instructions/grafo-schema.instructions.md` con protocolo genérico y lenguaje no específico de legislativa.