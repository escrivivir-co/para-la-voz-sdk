# Plan — grafo-sdk

> **Fecha:** 19-abr-2026
> **Autor:** Claude Opus 4.6
> **Dossier:** `sala/dossiers/grafo-sdk/`

## 1. Contexto

El concepto de "grafo de bifurcación" existe hoy solo en mod/legislativa:

- `DRAFTS2/grafo/` — gramática JSON + datos (index, nodos, arcos, huecos)
- `DRAFTS2/grafo/gramatica.md` — spec de la gramática (tipos de nodo, arcos, huecos)
- `mod/agents/grafista.agent.md` — construye el grafo desde corpus + hilo
- `mod/agents/demiurgo.agent.md` — instancia universos desde el grafo
- `.github/skills/futures-engine/SKILL.md` — el skill **ya es SDK** (portable)
- `.github/agents/dramaturgo.agent.md` — el Dramaturgo SDK **ya usa futures-engine**

Pero la capacidad de "corpus → grafo de bifurcación → universos" no es exclusiva de un mod jurídico. Cualquier mod con un corpus podría bifurcar futuros. El skill ya es genérico; lo que falta es:

1. Un **schema genérico de grafo** (qué es un nodo, arco, hueco — sin asumir tipos concretos)
2. Un **scaffold `grafo/`** o convención de dónde vive el grafo
3. El Dramaturgo SDK ya existe — pero necesita saber dónde buscar el grafo del mod

Lo que sí es mod-specific:
- Los tipos de nodo concretos (`estado`, `bifurcacion`, `rama`, `hueco` — legislativa)
- La gramática JSON con campos como `plausibilidad`, `piezas_ancla`
- La cadena Grafista → Demiurgo → Dramaturgo Cortos
- Los datos concretos (19 nodos del caso Zoowoman)

## 2. Anclas

| Artefacto | Ubicación | Estado |
|-----------|-----------|--------|
| futures-engine (SDK) | `.github/skills/futures-engine/SKILL.md` | Operativo — genérico |
| Dramaturgo (SDK) | `.github/agents/dramaturgo.agent.md` | Operativo — usa futures-engine |
| Grafista (mod) | `mod/agents/grafista.agent.md` | Operativo — construye grafo |
| Demiurgo (mod) | `mod/agents/demiurgo.agent.md` | Operativo — instancia universos |
| Gramática JSON (mod) | `DRAFTS2/grafo/gramatica.md` | v1.0 — 4 tipos de nodo |
| Datos del grafo (mod) | `DRAFTS2/grafo/*.json` | 19 nodos, 4 ramas |
| Dossier archivado | `sala/archivo/sprint-cristalizacion-v1/dossiers/cristalizacion-grafo-json/` | 7 tasks (completado) |
| FEAT-06 Pipeline | `DRAFTS2/FEAT-06_PIPELINE_REFRESH.md` | Grafo de deps piezas → derivados |

## 3. Restricciones

- Las piezas SDK van a `main` → `.github/` (instructions, templates, agentes)
- No romper el grafo JSON ya existente en mod/legislativa
- futures-engine skill **no se toca** — ya es genérico
- El Dramaturgo SDK se amplía mínimamente (referencia a grafo genérico)
- La gramática legislativa (gramatica.md) sigue viviendo en el mod

## 4. Propuesta

### 4.1. Schema genérico de grafo (SDK)

Crear `.github/instructions/grafo-schema.instructions.md`:

Un mod puede definir un grafo de bifurcación. Un grafo tiene:
- **Nodos**: unidades con tipo, contenido y referencias a piezas del lore
- **Arcos**: conexiones dirigidas entre nodos con peso y justificación
- **Huecos**: vacíos estructurales explícitos

El SDK define la estructura mínima (qué campos tiene un nodo como mínimo, qué es un arco). El mod define tipos de nodo concretos, campos adicionales y reglas de validación.

### 4.2. Template de gramática (SDK)

Crear `.github/templates/grafo-gramatica.template.md` — plantilla que un mod rellena con sus tipos de nodo y reglas de validación.

### 4.3. Convención de ubicación del grafo

El grafo vive dentro de la lore-db: `{{LORE_DIR}}/derivados/grafo/`. Es un derivado (se genera desde corpus + hilo).

Añadir a `pieza-schema.instructions.md` o a `copilot-instructions.md` la nota de que los mods pueden definir un `grafo/` dentro de derivados.

### 4.4. Ampliar Dramaturgo SDK

El `@Dramaturgo` en `.github/agents/` ya usa futures-engine. Añadir:
- Referencia al concepto de grafo (si el mod define `grafo/`, léelo antes de bifurcar)
- Handoff al Grafista del mod (si existe)

No se crean Grafista ni Demiurgo a nivel SDK — son especializaciones del mod.

### 4.5. Documentar en copilot-instructions.md

Añadir sección "Grafo de bifurcación" al SDK con estructura mínima esperada y relación con futures-engine.

## 5. Salida operativa

- Tracking: [BACKLOG.md](./BACKLOG.md)
- Decisiones del PO: [RESPUESTAS.md](./RESPUESTAS.md)
- Tasks: carpeta [tasks](./tasks)
