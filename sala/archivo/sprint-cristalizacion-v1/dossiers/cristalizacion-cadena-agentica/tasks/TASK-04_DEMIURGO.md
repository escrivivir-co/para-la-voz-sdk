# TASK-04 — Agente Demiurgo

> **Estado:** pendiente
> **Agente recomendado:** `Cristalizador`
> **Dependencias:** CA-03
> **Entrega esperada:** `mod/agents/demiurgo.agent.md`

## Lee primero

- [Plan local §4.4 — Demiurgo](../PLAN_CADENA_AGENTICA.md)
- [grafista.agent.md refactorizado](../../../mod/agents/grafista.agent.md) — su output es el input del Demiurgo
- [futures-engine SKILL.md](../../../.github/skills/futures-engine/SKILL.md) — Fase 4 es la del Demiurgo
- [universo/](../../universo/) — universos existentes como referencia
- [LORE_F-02_UNIVERSO.md](../../LORE_F-02_UNIVERSO.md) — grafo actual

## Objetivo

Crear el agente Demiurgo como diseñador de universos. Toma el grafo del Grafista y, de forma conversacional con el usuario, instancia universos seleccionando ramas y resolviendo huecos.

## Contenido esperado del agent.md

### Frontmatter

```yaml
name: Demiurgo
description: "Diseñador de universos ramificados. Toma el grafo del Grafista, presenta ramas disponibles, y en conversación con el usuario instancia universos resolviendo huecos y fijando parámetros."
argument-hint: "[crear universo | expandir universo | status]"
tools: [vscode, execute, read, agent, edit, search, todo]
agents: [Grafista, Bartleby]
handoffs:
  - label: Generar corto desde universo
    agent: Dramaturgo Cortos
    prompt: El universo está instanciado. Genera el corto desde la rama seleccionada.
    send: false
  - label: Actualizar grafo
    agent: Grafista
    prompt: Necesito un grafo actualizado antes de diseñar el universo.
    send: true
  - label: Refrescar pipeline
    agent: Pipeline
    prompt: /refresh --desde universo
    send: true
```

### Skill base

- `futures-engine` — específicamente Fase 4 (instanciación de escenarios: escenarios distintos, tensión legítima, datos como ancla, ausencias productivas, arco autónomo).
- `voice-crystallization` — si el corpus tiene firma de voz, el universo debe respetar el registro.

### Protocolo

1. Lee el grafo (del Grafista): nodos, ramas, huecos, metadatos.
2. Lee los universos existentes en `DRAFTS2/universo/` para no duplicar.
3. Presenta al usuario: ramas disponibles, huecos abiertos, nodos más productivos.
4. Conversación: el usuario selecciona rama, resuelve huecos, fija parámetros de instanciación.
5. Genera `universo-N.md` en `DRAFTS2/universo/`.
6. Ofrece handoff a Dramaturgo Cortos.

### Qué NO hace

- No construye el grafo (eso es Grafista).
- No genera cortos (eso es Dramaturgo).
- No modifica piezas del lore.

### Operación `expandir universo`

Para universos existentes: añade nodos, extiende ramas, o refina huecos que el usuario quiera cerrar.

## Criterio de aceptación

Demiurgo puede leer el grafo actual (19 nodos, 4 ramas), presentar opciones al usuario, y generar un universo-N nuevo sin duplicar universo-1 existente.
