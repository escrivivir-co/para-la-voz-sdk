# TASK-01 — Agente Puzzle

> **Estado:** pendiente
> **Agente recomendado:** `Cristalizador`
> **Dependencias:** CA-00
> **Entrega esperada:** `mod/agents/puzzle.agent.md`

## Lee primero

- [Plan local §4.1 — Puzzle](../PLAN_CADENA_AGENTICA.md)
- [LORE_INDEX.md](../../LORE_INDEX.md) — inventario que Puzzle consume
- [lore-schema.instructions.md](../../../mod/instructions/lore-schema.instructions.md) — esquema contra el que Puzzle valida (si existe)
- [archivero-lore.agent.md](../../../mod/agents/archivero-lore.agent.md) — para entender qué se le quita

## Objetivo

Crear el agente Puzzle como primer eslabón de la cadena. Valida las piezas del lore contra el schema y presenta un pack verificado al Archivero Lore.

## Contenido esperado del agent.md

### Frontmatter

```yaml
name: Puzzle
description: "Lector y ensamblador del pack de lore. Valida piezas contra el schema, detecta inconsistencias y empaqueta el input para el Archivero Lore."
argument-hint: "[validar | inventario | status]"
tools: [vscode, read, search]
agents: [Archivero Lore]
handoffs:
  - label: Pasar pack verificado al Archivero Lore
    agent: Archivero Lore
    prompt: El pack está verificado. Procede a generar el corpus.
    send: true
  - label: Refrescar pipeline
    agent: Pipeline
    prompt: /refresh status
    send: true
```

### Protocolo

1. Lee `lore-routing.instructions.md` para resolver rutas.
2. Lee `lore-schema.instructions.md` para los tipos válidos.
3. Lee `LORE_INDEX.md` y contrasta contra ficheros en disco.
4. Validaciones: piezas huérfanas (en disco, no en índice), piezas fantasma (en índice, no en disco), campos obligatorios faltantes, tipo mal asignado.
5. Presenta informe y, si todo OK, ofrece handoff a Archivero Lore.

### Qué NO hace

- No analiza contenido (eso es Bartleby vía Archivero).
- No genera corpus.
- No modifica piezas — es read-only.

## Criterio de aceptación

Puzzle puede listar las 51 piezas actuales, detectar si falta alguna, y pasar handoff al Archivero Lore con un pack limpio.
