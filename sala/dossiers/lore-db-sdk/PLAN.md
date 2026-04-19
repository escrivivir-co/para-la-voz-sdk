# Plan — lore-db-sdk

> **Fecha:** 19-abr-2026
> **Autor:** Claude Opus 4.6
> **Dossier:** `sala/dossiers/lore-db-sdk/`

## 1. Contexto

Hoy el concepto de "base de datos de piezas" (inventario tipado, schema, validación, routing) vive entero en `mod/legislativa`:

- `DRAFTS2/LORE_INDEX.md` — inventario de piezas con marcas `[P-XX]`, `[S-XX]`, etc.
- `mod/instructions/lore-schema.instructions.md` — ontología de tipos, campos obligatorios, DoR/DoD
- `mod/instructions/lore-estado.instructions.md` — conteos canónicos y estado del pipeline
- `mod/instructions/lore-routing.instructions.md` — mapa de rutas canónicas → reales
- `mod/agents/puzzle.agent.md` — valida piezas contra schema
- `mod/agents/archivero-lore.agent.md` — ingesta pack verificado, genera corpus

Pero la **gestión de piezas tipadas** no es específica de un lore jurídico. Cualquier mod necesita:
- Un inventario de piezas con marcas estables
- Un schema que defina tipos válidos y campos por tipo
- Un mecanismo de routing (dónde vive cada cosa)
- Un agente que valide consistencia inventario ↔ disco

Lo que sí es lore-specific: los tipos concretos (P=personaje, S=social, N=noticia), los campos concretos ("Emisor", "Medio"), y cómo las piezas se conectan al pipeline (corpus → grafo → universos → cortos).

## 2. Anclas

| Artefacto | Ubicación actual | Estado |
|-----------|-----------------|--------|
| Archivero SDK | `.github/agents/archivero.agent.md` | Operativo — corpus/diff/merge/status |
| Archivero Lore | `mod/agents/archivero-lore.agent.md` | Operativo — extiende SDK con ingest |
| Puzzle | `mod/agents/puzzle.agent.md` | Operativo — valida piezas contra schema |
| lore-schema | `mod/instructions/lore-schema.instructions.md` | 6 tipos, campos por tipo |
| lore-estado | `mod/instructions/lore-estado.instructions.md` | 51 piezas, conteos |
| lore-routing | `mod/instructions/lore-routing.instructions.md` | Mapa canónico → real |
| LORE_INDEX | `DRAFTS2/LORE_INDEX.md` | Inventario de 51 piezas en 6 bloques |
| FEAT-06 Pipeline Refresh | `DRAFTS2/FEAT-06_PIPELINE_REFRESH.md` | Grafo de dependencias piezas → derivados |
| TASK-02 Refactor Archivero | `sala/archivo/sprint-cristalizacion-v1/dossiers/cristalizacion-cadena-agentica/tasks/TASK-02_REFACTOR_ARCHIVERO_LORE.md` | Pendiente (sprint archivado) |

## 3. Restricciones

- Las piezas SDK van a `main` → `.github/` (agents, instructions, templates)
- El concepto genérico NO define tipos concretos: solo el protocolo (qué es un tipo, qué campos tiene como mínimo, cómo se marca)
- El `@archivero` SDK se extiende, no se reescribe
- Rutas: usar `{{LORE_DIR}}` como variable genérica (el mod resuelve a `lore/` o donde sea)
- No romper la cadena existente de `mod/legislativa` — solo extraer la capa genérica

## 4. Propuesta

### 4.1. Schema genérico de piezas (SDK)

Crear `.github/instructions/pieza-schema.instructions.md`:

```
Cada mod define sus tipos de pieza. Un tipo tiene:
- Prefijo de marca (1-2 chars, ej: P, S, N)
- Nombre del tipo
- Campos obligatorios (tabla)
- Campos opcionales (tabla)
- DoR / DoD

El inventario vive en {{LORE_DIR}}/INDEX.md con formato estándar.
```

### 4.2. Template de inventario (SDK)

Crear `.github/templates/pieza-index.template.md` — plantilla genérica para el inventario de piezas de cualquier mod.

### 4.3. Template de schema de tipos (SDK)

Crear `.github/templates/pieza-schema.template.md` — plantilla que un mod rellena con sus tipos concretos.

### 4.4. Crear @Loreador SDK

Nuevo agente en `.github/agents/loreador.agent.md`:
- Operaciones: `abrir` (init/verificar db), `pieza` (crear/editar/localizar), `validar` (formato genérico), `inventario` (listar piezas y estado), `localizar` (resolver rutas vía routing)
- Lee: `pieza-schema.instructions.md`, `{{LORE_DIR}}/INDEX.md`, routing del mod
- Handoffs: → `@Bartleby` (analizar pieza), → `@Archivero` (pasar a corpus)
- No asume tipos concretos — el mod los define y el Loreador del mod los valida

Reemplaza la propuesta anterior de ampliar `@archivero` SDK — el archivero sigue en su dominio (corpus diff/merge/status) y el Loreador gestiona la lore-db.

### 4.5. Documentar en copilot-instructions.md

Añadir sección "Piezas del lore" al SDK con la estructura esperada y la variable `{{LORE_DIR}}`.

### 4.6. Scaffold lore-db en main + inicialización

Como se hizo con `sala/`: crear `lore/` en main con README genérico, .gitkeep stubs, templates de inicialización. Añadir Paso 0b en `sala-aleph.prompt.md` para que inicialice la lore-db si está vacía (como hace Paso 0 con la sala).

Variable `{{LORE_DIR}}` documentada junto a `{{SALA_DIR}}` en copilot-instructions.md.

## 5. Salida operativa

- Tracking: [BACKLOG.md](./BACKLOG.md)
- Decisiones del PO: [RESPUESTAS.md](./RESPUESTAS.md)
- Tasks: carpeta [tasks](./tasks)
