# PLAN INICIAL — Future-machine para universo-1

> **Fecha:** 18-abr-2026
> **Modelo:** `GPT-5.4`
> **Estado:** abierto
> **Anclas:** `DRAFTS2/PLAN_UNIVERSO1_V2.md`, `DRAFTS2/LORE_F-02_UNIVERSO.md`, `DRAFTS2/universo/`

### [GPT-5.4] Inicialización del plan base

Este plan no duplica el SDK ni el mod actual. Sirve para fijar el rumbo de la cristalización pedida y para no perder la conversación si se cae la ventana de contexto.

#### 1. Contexto DRY

La future-machine debe partir de lo que ya existe en `.github/` y en `mod/`, no reescribirlo. El trabajo aquí es detectar huecos, wiring faltante y overrides locales para legislativa.

#### 2. Cristalizador como agente ejecutor

La intervención se delega al `@Cristalizador`. Su misión es leer la carpeta `COPILOT/`, detectar capacidades aprovechables y proponer todo lo necesario en `mod/` para maximizar uso agéntico en este lore.

#### 3. Rutas oficiales temporales

Se confirma el warning de rutas canónicas ausentes. Deben existir `corpus/`, `corpus/corpus.md`, `mod/skills/` y `mod/universos/` con notas de redirección temporal hacia `DRAFTS2/` mientras el lore siga viviendo allí.

#### 4. Skill local del mod

El SDK core ya contiene operaciones de universo en `.github/skills/futures-engine/SKILL.md`. El mod no tiene todavía override local ni materialización propia de esa machine. La tarea es diseñar e implementar esa capa en `mod/`.

#### 5. Warning para main solo si hay prueba

No es objetivo de `mod/legislativa` arreglar la rama `main`. Solo se abre warning si se demuestra que el Cristalizador o la fuente `COPILOT/` no están bien enlazados desde el core.

#### 6. Propuesta formal de cristalización

Hace falta una propuesta escrita, priorizada y vinculada a capacidades reales de Copilot antes de abrir la implementación grande.

#### 7. Implementación solo en `mod/`

Todo artefacto nuevo debe vivir en `mod/`. No se toca `.github/` salvo lectura y referencia.

#### 8. Validación con universo-1

La prueba de realidad del feature será `universo-1` y el sprint [PLAN_UNIVERSO1_V2.md](../PLAN_UNIVERSO1_V2.md). Si la machine no mejora ese caso, la cristalización no está lista.

---

## [Claude Opus 4.6] Adenda 19-abr-2026

> Las decisiones de la sesión del 19-abr-2026 resuelven por proxy gran parte de este feature.

### Qué se ha resuelto fuera de este dossier

| Task original | Estado | Dossier que lo resuelve |
|---------------|--------|-------------------------|
| FM-02 (propuesta Cristalizador) | **Superseded** | 4 dossiers: `pipeline-operativo/`, `cadena-agentica/`, `grafo-json/`, `finalizacion-lore-plan/` |
| FM-03 (skill local del mod) | **Superseded** | `cristalizacion-feature/SKILL.md` es el protocolo. Cadena-agéntica cubre la superficie |
| FM-04 (superficie agéntica) | **Superseded** | `cadena-agentica/` implementa los 5 agentes. `pipeline-operativo/` implementa schema/estado/routing |
| FM-05 (validación) | **Necesita rewrite** | La validación ahora es contra la cadena de 5, no solo contra Dramaturgo |
| FM-06 (warning main) | Sin cambios | Sigue condicional |

### Insight clave: dos operaciones simétricas

El dossier original proponía "salvar el lore de DRAFTS2" como objetivo. Con las decisiones del 19-abr, esto se ha cristalizado en **dos operaciones simétricas**:

1. **Lore → Corpus**: Piezas DRAFTS2 → Puzzle valida → Archivero reduce → `CORPUS_PREVIEW.md`
2. **Grafo draft → Grafo JSON**: `LORE_F-02_UNIVERSO.md` Markdown → Grafista migra → `DRAFTS2/grafo/*.json`

Ambas son "promover borrador a formato estructurado". La primera la ejecuta el Archivero Lore. La segunda el Grafista. Ambas están diseñadas en sus dossiers respectivos.

### Qué queda vivo de este dossier

- **FM-00, FM-01**: completados, vigentes (contexto y redirecciones temporales).
- **FM-05**: se reescribe como validación de la cadena completa (ver task actualizada).
- **FM-06**: sin cambios.
- **FM-02, FM-03, FM-04**: cerrados por proxy. El trabajo propuesto ya está diseñado en los dossiers hermanos.

---

## Salida operativa de esta inicialización

- Tracking del feature: [BACKLOG_FUTURE_MACHINE_UNIVERSO1.md](./BACKLOG_FUTURE_MACHINE_UNIVERSO1.md)
- Respuestas del usuario fijadas en disco: [RESPUESTAS_USUARIO_FUTURE_MACHINE_UNIVERSO1.md](./RESPUESTAS_USUARIO_FUTURE_MACHINE_UNIVERSO1.md)
- Tasks delegables: carpeta [tasks](./tasks)