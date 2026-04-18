# PLAN INICIAL — Cristalización de la cadena agéntica

> **Fecha:** 19-abr-2026
> **Modelo:** `Claude Opus 4.6`
> **Estado:** abierto
> **Anclas:** `mod/agents/`, `DRAFTS2/LORE_INDEX.md`, `DRAFTS2/LORE_F-02_ARTEFACTO.md`, `DRAFTS2/LORE_F-02_UNIVERSO.md`
> **Protocolo:** según `mod/skills/cristalizacion-feature/SKILL.md`

---

## [Claude Opus 4.6] Inicialización del plan base

Este dossier cubre la implementación de la **cadena de 5 agentes especializados** para el mod legislativa. La decisión del PO y el cliente (19-abr-2026) separa el pipeline actual en roles bien definidos con un solo tipo de transformación cada uno.

---

## 1. Contexto DRY

| Qué | Dónde | Estado |
|-----|-------|--------|
| Archivero Lore (implementado) | [mod/agents/archivero-lore.agent.md](../../mod/agents/archivero-lore.agent.md) | Operativo, cubre ingest/diff/merge/status |
| Grafista (implementado, necesita refactor) | [mod/agents/grafista.agent.md](../../mod/agents/grafista.agent.md) | Mezcla construcción de grafo con generación de universo — debe separarse |
| Dramaturgo Cortos (implementado) | [mod/agents/dramaturgo.agent.md](../../mod/agents/dramaturgo.agent.md) | Operativo, genera cortos desde universos |
| Pipeline (implementado) | [mod/agents/pipeline.agent.md](../../mod/agents/pipeline.agent.md) | Orquestador, ya tiene handoffs a los 4 anteriores |
| Puzzle (no existe) | — | Nuevo: ensambla el lore como pack |
| Demiurgo (no existe) | — | Nuevo: construye universos desde el grafo |
| Grafo actual en Markdown | [DRAFTS2/LORE_F-02_UNIVERSO.md](../LORE_F-02_UNIVERSO.md) | 19 nodos, 4 ramas — será migrado a JSON (ver dossier `cristalizacion-grafo-json/`) |
| Universos existentes | [DRAFTS2/universo/](../universo/) | universo-1 (R4), universo-1-r1 (R1), universo-1-r2 (R2) |
| Skill futures-engine | [.github/skills/futures-engine/SKILL.md](../../.github/skills/futures-engine/SKILL.md) | 5 fases, inmutable (SDK) |

## 2. Agentes involucrados

- **`@Cristalizador`** — diseña y crea los agentes nuevos en `mod/agents/`.
- **`@Pipeline`** — consumidor: necesita que los handoffs estén cableados correctamente.

## 3. Restricciones

- No tocar `.github/`.
- Todo artefacto nuevo en `mod/`.
- Cada agente tiene **una sola transformación** y handoffs claros al siguiente.
- El grafo JSON no se implementa aquí (tiene su propio dossier). Grafista se prepara para consumirlo pero hoy lee Markdown.

---

## 4. La cadena de 5 agentes

La decisión del PO (19-abr-2026) fija esta secuencia:

```
Puzzle → Archivero Lore → Grafista → Demiurgo → Dramaturgo Cortos
  │           │               │           │            │
  │           │               │           │            └─ genera CORTO-*.md
  │           │               │           └─ genera universo-N.md
  │           │               └─ genera grafo (UNIVERSO.md → JSON)
  │           └─ genera CORPUS_PREVIEW.md
  └─ ensambla pack como input verificado
```

### 4.1. Puzzle (nuevo)

**Rol:** Lector y ensamblador del lore. Es el primer agente de la cadena. Lee las piezas en disco, las valida contra el schema (`lore-schema.instructions.md`) y las empaqueta como input limpio para el Archivero Lore.

**Por qué existe:** Hoy el Archivero Lore hace doble trabajo: inventariar piezas + reducir a corpus. Puzzle separa el inventario/validación del análisis. Además, el Puzzle puede detectar piezas faltantes, duplicadas o mal tipadas antes de que entren al pipeline.

**Qué hace:**
- Lee `LORE_INDEX.md` y verifica contra disco
- Valida cada pieza contra `lore-schema.instructions.md`
- Detecta piezas huérfanas (en disco pero no en índice) y fantasma (en índice pero no en disco)
- Presenta pack verificado al Archivero Lore

**Handoffs:**
- → `@Archivero Lore` (pack verificado)
- ← `@Pipeline` (puede pedir validación parcial)

### 4.2. Archivero Lore (refactor menor)

**Rol:** Sin cambios sustanciales. Ya está implementado. El refactor es:
- Eliminar la lógica de inventario/validación de su operación `ingest` (ahora la hace Puzzle).
- Asumir que el input ya viene verificado.
- Su output sigue siendo `CORPUS_PREVIEW.md`.

### 4.3. Grafista (refactor mayor)

**Rol:** Constructor del grafo de bifurcación. **Ya no genera universos.** Solo detecta nodos de bifurcación y los estructura como grafo.

**Refactor necesario:**
- Eliminar toda referencia a "generar universo" de su descripción y protocolo.
- Eliminar el handoff directo a Dramaturgo Cortos (ahora pasa por Demiurgo).
- Su output es el grafo (Markdown hoy, JSON en el futuro).
- Su skill base sigue siendo futures-engine Fases 1-3 (no Fases 4-5).

**Handoffs:**
- → `@Demiurgo` (grafo completo)
- ← `@Archivero Lore` (corpus actualizado)

### 4.4. Demiurgo (nuevo)

**Rol:** Diseñador de universos. Toma el grafo del Grafista y construye universos ramificados seleccionando ramas, instanciando nodos y resolviendo huecos de forma conversacional con el usuario.

**Por qué existe:** Hoy el Grafista hace grafo + universo, y el Dramaturgo necesita que el universo esté "listo" antes de narrar. Separar el diseño del universo (Demiurgo) de la narración (Dramaturgo) permite iterar sobre el universo sin reescribir cortos.

**Qué hace:**
- Lee el grafo (del Grafista)
- Presenta las ramas disponibles
- Conversación con el usuario: selecciona rama, resuelve huecos, fija parámetros
- Genera `universo-N.md` en `DRAFTS2/universo/`
- Aplica futures-engine Fase 4 (instanciación de escenarios)

**Handoffs:**
- → `@Dramaturgo Cortos` (universo instanciado)
- ← `@Grafista` (puede pedir actualización del grafo)

### 4.5. Dramaturgo Cortos (sin cambios funcionales)

**Rol:** Sin cambios. Sigue generando cortos desde universos instanciados. El único cambio de cableado es:
- Recibe handoff de `@Demiurgo` (antes de `@Grafista`).
- Pierde el handoff directo "actualizar grafo" → lo sustituye por "pedir universo actualizado" a Demiurgo.

---

## 5. Resumen de entregas

| # | Artefacto | Ruta | Tipo | Dependencias |
|---|-----------|------|------|-------------|
| CA-01 | Agente Puzzle | `mod/agents/puzzle.agent.md` | agent nuevo | Ninguna (puede crearse en paralelo) |
| CA-02 | Refactor Archivero Lore | `mod/agents/archivero-lore.agent.md` | edición | CA-01 (para definir la interfaz del pack) |
| CA-03 | Refactor Grafista | `mod/agents/grafista.agent.md` | edición | Ninguna |
| CA-04 | Agente Demiurgo | `mod/agents/demiurgo.agent.md` | agent nuevo | CA-03 (para definir la interfaz del grafo) |
| CA-05 | Recablear Dramaturgo Cortos | `mod/agents/dramaturgo.agent.md` | edición | CA-04 |
| CA-06 | Actualizar Pipeline handoffs | `mod/agents/pipeline.agent.md` | edición | CA-01..CA-05 |
| CA-07 | Validación de la cadena completa | informe en dossier | validación | CA-01..CA-06 |

---

## Salida operativa

- Tracking: [BACKLOG_CADENA_AGENTICA.md](./BACKLOG_CADENA_AGENTICA.md)
- Respuestas: [RESPUESTAS_USUARIO_CADENA_AGENTICA.md](./RESPUESTAS_USUARIO_CADENA_AGENTICA.md)
- Tasks: carpeta [tasks](./tasks)
