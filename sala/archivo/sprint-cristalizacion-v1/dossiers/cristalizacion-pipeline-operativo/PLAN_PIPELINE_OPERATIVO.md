# PLAN INICIAL — Cristalización del pipeline operativo

> **Fecha:** 18-abr-2026
> **Modelo:** `Claude Opus 4.6`
> **Estado:** abierto
> **Anclas:** `mod/agents/pipeline.agent.md`, `DRAFTS2/FEAT-06_PIPELINE_REFRESH.md`, `DRAFTS2/LORE_PLAN.md`, `DRAFTS2/LORE_INDEX.md`
> **Protocolo:** según `mod/skills/cristalizacion-feature/SKILL.md`

---

## [Claude Opus 4.6] Inicialización del plan base

Este dossier cubre dos objetivos convergentes:

1. **Tipar el lore en el mod** — que el mod defina el esquema de piezas (P-\*, S-\*, N-\*, T-\*, R-\*, F) como ontología reutilizable, separada de los datos concretos del caso Zoowoman que hoy viven en DRAFTS2/.
2. **Hacer operativo el pipeline** — que `@Pipeline` pueda consumir ese esquema tipado, validar piezas, resolver rutas y ejecutar el refresh sin depender de conocimiento implícito ni workarounds manuales.

---

## 1. Contexto DRY

| Qué | Dónde | Estado |
|-----|-------|--------|
| Agente pipeline | [mod/agents/pipeline.agent.md](../../mod/agents/pipeline.agent.md) | Implementado (FEAT-06) |
| Protocolo refresh | [FEAT-06_PIPELINE_REFRESH.md](../FEAT-06_PIPELINE_REFRESH.md) | Spec completa, 6 pasos |
| Slash command | [mod/prompts/refresh.prompt.md](../../mod/prompts/refresh.prompt.md) | Implementado |
| Inventario de piezas | [LORE_INDEX.md](../LORE_INDEX.md) | 51 piezas, mapa de bloques |
| Plan de producción | [LORE_PLAN.md](../LORE_PLAN.md) | Backlog con 22 PBIs, DoR/DoD |
| Corpus workaround | [corpus/corpus.md](../../corpus/corpus.md) | Redirección a DRAFTS2/ |
| Instrucciones mod | [legislativa-universo.instructions.md](../../mod/instructions/legislativa-universo.instructions.md) | 48 piezas declaradas (desactualizado: son 51) |

## 2. Agentes involucrados

- **`@Cristalizador`** — propone y construye artefactos en `mod/`.
- **`@Pipeline`** — consume artefactos para ejecutar el refresh. Es el cliente que pide.

> **[Claude Opus 4.6] Adenda 19-abr-2026:** La cadena agéntica se ha ampliado a 5 agentes especializados. Los artefactos de este dossier (schema, estado, routing) son consumidos por **todos** ellos, no solo por Pipeline:
>
> | Agente | Qué consume de este dossier |
> |--------|-----------------------------|
> | `@Puzzle` | schema (para validar piezas al ensamblar) |
> | `@Archivero Lore` | schema + estado + routing (para ingest y conteos) |
> | `@Grafista` | routing (para resolver rutas del grafo) + estado (para validar conteos) |
> | `@Demiurgo` | routing (para localizar grafos y universos) |
> | `@Pipeline` | los 3 (consumidor principal, como se diseñó) |
>
> El scope de este dossier no cambia — sigue siendo schema, estado, routing, update instructions. Pero los criterios de aceptación de PO-03 y PO-05 se amplían para cubrir las rutas del grafo JSON (ver dossier `cristalizacion-grafo-json/`).

## 3. Restricciones

- No tocar `.github/`.
- Todo artefacto nuevo en `mod/`.
- `DRAFTS2/` sigue siendo fuente viva del lore del caso.
- El tipado del lore en el mod es genérico (vale para cualquier caso legislativa), no específico del caso Feo.

---

## 4. Diálogo simulado: Cristalizador ↔ Pipeline

> Esta sección fija el resultado de la conversación inter-agente. Cada parte habla desde su rol.

### [Pipeline] Dice:

Soy el pipeline de refresh del lore legislativa. Mi protocolo tiene 6 pasos y opera sobre un grafo de dependencias con 5 nodos (PIEZAS → {CORPUS_PREVIEW ∥ LORE_F} → ARTEFACTO → UNIVERSO → ramas). Funciono, pero tengo problemas operativos reales:

**Lo que no puedo hacer hoy:**

1. **No sé qué es una pieza válida.** Mi Paso 0 (inventario) lista ficheros `LORE_*.md` por convención de nombres, pero no tengo un esquema que me diga qué campos debe tener una pieza `S-*` vs una `T-*`. El LORE_PLAN.md tiene una tabla de formatos (§3.1) pero no está en una ruta que yo consuma como instrucción.

2. **No puedo validar conteos.** `legislativa-universo.instructions.md` dice 48 piezas pero el índice dice 51. No tengo una fuente canónica de verdad para el conteo. Dependo de que alguien actualice manualmente.

3. **No sé resolver rutas.** `corpus/corpus.md` es un workaround que redirige a `DRAFTS2/CORPUS_PREVIEW.md`. Cada skill y agente resuelve esto por su cuenta. Necesito un mapa de rutas canónico del mod.

4. **No puedo distinguir esquema de datos.** El mod debería definir *qué tipos de pieza existen* (esquema). Los datos concretos del caso Feo son una *instancia* de ese esquema. Hoy están mezclados: el LORE_INDEX.md hace ambas funciones.

5. **Mi regla 7** (sincronizar `legislativa-universo.instructions.md` si cambian conteos) es manual y frágil. Debería haber un fichero canónico de estado del lore que yo actualice y que las instructions lean.

**Lo que necesito del Cristalizador:**

- Un esquema de tipos de pieza en `mod/instructions/` que yo pueda leer para validar.
- Un fichero de estado del lore (conteos, fecha de corte) que sea fuente de verdad.
- Un mapa de rutas explícito: ruta canónica → ruta real (mientras dure el workaround DRAFTS2).
- Que el esquema sea del mod (genérico legislativa), no del caso.

### [Cristalizador] Dice:

Entendido. Tengo contexto de lo que ya existe en `mod/` y de las capacidades Copilot disponibles. Propongo esta intervención:

**Propuesta 1: `mod/instructions/lore-schema.instructions.md`**

- **Tipo:** `.instructions.md` con `applyTo: "DRAFTS2/LORE_*.md"`
- **Contenido:** Esquema normativo de tipos de pieza del lore legislativa. Define P-\*, S-\*, N-\*, T-\*, R-\*, F con campos obligatorios, campos opcionales, reglas de formato y convenciones de nombrado.
- **Capacidad que activa:** ninguna nueva — es `instructions` con `applyTo`, ya usada. Pero formaliza algo que hoy es conocimiento implícito.
- **Motivación:** Pipeline no puede validar lo que no está definido. LORE_PLAN.md §3.1 tiene la tabla, pero como guía editorial, no como spec consumible por agentes.

**Propuesta 2: `mod/instructions/lore-routing.instructions.md`**

- **Tipo:** `.instructions.md` con `applyTo: "mod/**,corpus/**"`
- **Contenido:** Mapa de rutas canónicas del SDK → rutas reales en DRAFTS2/. Tabla explícita. Condición de expiración: cuando el lore se mueva fuera de DRAFTS2/, este fichero se elimina.
- **Motivación:** Hoy cada agente resuelve el workaround por su cuenta. Pipeline, Dramaturgo Cortos, Archivero — todos leen la misma nota en `corpus/corpus.md`. Un instructions centralizado es más limpio.

**Propuesta 3: `mod/instructions/lore-estado.instructions.md`**

- **Tipo:** `.instructions.md` con `applyTo: "DRAFTS2/**"`
- **Contenido:** Ficha de estado canónica del lore activo: conteo de piezas por tipo, fecha de corte, baseline del caso, piezas pendientes de integrar. Es la fuente de verdad que Pipeline actualiza en su Paso 5 y que `legislativa-universo.instructions.md` referencia en lugar de mantener conteos propios.
- **Motivación:** Resuelve el desync 48 vs 51. Un solo fichero, una sola verdad.

**Propuesta 4: Actualizar `legislativa-universo.instructions.md`**

- **Tipo:** edición de fichero existente.
- **Contenido:** Eliminar conteos duplicados. Referenciar `lore-estado.instructions.md` como fuente. Mantener solo lo específico de universos (huecos, consignas, metáforas drenadas, datos duros).
- **Motivación:** DRY. Hoy el fichero mezcla estado del corpus con reglas de universo.

**Secuencia:**

```
P1 (schema) → P3 (estado) → P2 (routing) → P4 (actualizar universo instructions)
```

P1 primero porque sin esquema no se puede tipar el estado. P3 antes que P2 porque el routing necesita saber qué existe. P4 al final porque depende de P3.

### [Pipeline] Responde:

Acepto. Con P1 puedo validar piezas en mi Paso 0. Con P3 puedo sincronizar conteos en mi Paso 5 sin tocar manualmente `legislativa-universo`. Con P2 dejo de adivinar rutas. P4 me quita la regla 7 frágil.

Una petición adicional: en P1, que el esquema incluya la **Definition of Ready y Done** del LORE_PLAN.md (§5, §6). Hoy viven en un fichero de plan que yo no leo. Si están en el schema, puedo usarlas para decidir si una pieza está lista para integrar en el refresh.

### [Cristalizador] Acepta:

Incorporo DoR/DoD en P1. Es delta legítimo: el plan fija criterio editorial, el schema fija criterio operativo. Ambos se complementan.

---

## 5. Resumen de propuestas

| # | Artefacto | Ruta | Tipo | Dependencias |
|---|-----------|------|------|--------------|
| P1 | Esquema de tipos de pieza | `mod/instructions/lore-schema.instructions.md` | instructions | Ninguna |
| P2 | Mapa de rutas canónicas | `mod/instructions/lore-routing.instructions.md` | instructions | P3 + rutas grafo JSON (de `cristalizacion-grafo-json/`) |
| P3 | Estado canónico del lore | `mod/instructions/lore-estado.instructions.md` | instructions | P1 |
| P4 | Actualizar instructions de universo | `mod/instructions/legislativa-universo.instructions.md` | edición | P3 |

> **[Claude Opus 4.6] Nota 19-abr-2026:** P2 (routing) y P3 (estado) necesitan incorporar las rutas y conteos del grafo JSON cuando el dossier `cristalizacion-grafo-json/` defina la ubicación definitiva de `DRAFTS2/grafo/`. P3 debe incluir estado del grafo (nodos, ramas, universos), no solo conteo de piezas de lore.

## 6. Validación

La prueba de realidad es invocar `@Pipeline /refresh status` después de implementar P1–P4. Si Pipeline puede:
- Inventariar piezas tipadas
- Resolver rutas sin workaround ad hoc
- Reportar conteos desde fuente canónica
- Señalar piezas que no cumplen DoR

...el feature está cerrado.

---

## Salida operativa

- Tracking: [BACKLOG_PIPELINE_OPERATIVO.md](./BACKLOG_PIPELINE_OPERATIVO.md)
- Respuestas del usuario: [RESPUESTAS_USUARIO_PIPELINE_OPERATIVO.md](./RESPUESTAS_USUARIO_PIPELINE_OPERATIVO.md)
- Tasks: carpeta [tasks](./tasks)
