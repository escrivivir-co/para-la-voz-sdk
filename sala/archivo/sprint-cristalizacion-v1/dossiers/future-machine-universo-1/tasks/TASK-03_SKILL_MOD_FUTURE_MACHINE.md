# TASK-03 — Skill local del mod para future-machine

> **Estado:** pendiente
> **Agente recomendado:** `Cristalizador`
> **Dependencias:** FM-01, FM-02
> **Entrega esperada:** `mod/skills/futures-engine/SKILL.md` y/o `mod/skills/future-machine/SKILL.md`

## Lee primero

- [Plan inicial local](../PLAN_FUTURE_MACHINE_UNIVERSO1.md)
- [Respuestas del usuario](../RESPUESTAS_USUARIO_FUTURE_MACHINE_UNIVERSO1.md)
- [Skill core futures-engine](../../../.github/skills/futures-engine/SKILL.md)
- [corpus/corpus.md](../../../corpus/corpus.md)
- [LORE_F-02_UNIVERSO.md](../../LORE_F-02_UNIVERSO.md)
- [PLAN_UNIVERSO1_V2.md](../../PLAN_UNIVERSO1_V2.md)

## Objetivo

Materializar en `mod/` la capa local de future-machine que hoy no existe, sin romper el skill core ni copiarlo de forma mecánica.

## Lo que debe resolver

- Routing explícito desde rutas canónicas del SDK hacia `DRAFTS2/`.
- Vocabulario o reglas locales del lore legislativa que el core no conoce.
- Operaciones de machine que necesiten quedar fijadas en el mod en lugar de depender solo del skill core.
- Convivencia limpia entre `futures-engine` base y el caso `future-machine` del mod.

## Decisión de diseño esperada

El agente debe decidir y justificar una de estas opciones:

1. **Override local mínimo** en `mod/skills/futures-engine/SKILL.md`.
2. **Skill nuevo** en `mod/skills/future-machine/SKILL.md`.
3. **Capa dual**: override mínimo + skill específico.

## Criterio de aceptación

La solución elegida permite que el mod lea el lore vivo en `DRAFTS2/`, preserve el protocolo core y añada solo lo que legislativa necesita de verdad.