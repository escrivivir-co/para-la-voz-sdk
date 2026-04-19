# TASK-03 — Crear @Loreador SDK

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** PS-01
> **Entrega esperada:** `.github/agents/loreador.agent.md`

## Lee primero

- [Plan §4.4](../PLAN.md)
- `.github/agents/archivero.agent.md` — el archivero SDK (no se toca — Loreador es agente separado)
- `mod/agents/puzzle.agent.md` — validación de piezas (su función se absorbe aquí como genérica)
- `mod/agents/archivero-lore.agent.md` — ingest batch (referencia de qué NO va en el SDK)

## Decisión del PO (19-abr-2026)

El usuario pidió "que tenga su agente Loreador para ayudar al usuario a abrir la db, editar piezas, localizar las carpetas". Puzzle desaparece como agente; Archivero SDK no se toca.

## Objetivo

Crear `@Loreador` — gestor de la lore-db a nivel SDK. Punto de entrada del usuario para trabajar con piezas.

### Operaciones

| Operación | Qué hace |
|-----------|----------|
| `abrir` | Init/verificar la db — crea `lore/` si falta, copia templates, verifica INDEX |
| `pieza` | Crear/editar/localizar pieza — usa el schema del mod para campos obligatorios |
| `validar` | Validación genérica de formato (marca, cabecera, campos mínimos) |
| `inventario` | Listar piezas en disco vs INDEX, conteos, estado |
| `localizar` | Resolver rutas vía routing — "¿dónde está X?" |

### Fuentes que lee

1. `.github/instructions/pieza-schema.instructions.md` — schema genérico
2. `{{LORE_DIR}}/INDEX.md` — inventario de piezas
3. `mod/instructions/lore-routing.instructions.md` (si existe) — routing del mod
4. `mod/instructions/lore-schema.instructions.md` (si existe) — tipos concretos del mod

### Handoffs

- → `@Bartleby` — analizar una pieza
- → `@Archivero` — pasar piezas analizadas al corpus (diff/merge)

### Extensión por el mod

El mod crea `@Loreador Legislativa` que hereda de `@Loreador` y añade:
- Tipos concretos (P, S, N, T, R, F) con sus campos
- DoR/DoD por tipo
- Validación contra `lore-schema.instructions.md` del mod
- Handoff a `@Archivero Legislativa` para ingest batch

## Qué NO se toca

- `@Archivero` SDK — sigue en su dominio (corpus.md)
- No se crean tipos concretos en el SDK
- No se define pipeline — eso es del mod

## Criterio de aceptación

- `.github/agents/loreador.agent.md` existe con las 5 operaciones
- Lee schema genérico y routing sin asumir tipos del mod
- Handoffs a Bartleby y Archivero definidos
- Documentado en copilot-instructions.md (PS-04)
