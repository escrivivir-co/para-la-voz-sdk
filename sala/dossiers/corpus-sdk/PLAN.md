# Plan — corpus-sdk

> **Fecha:** 19-abr-2026
> **Autor:** GPT-5.4
> **Dossier:** `sala/dossiers/corpus-sdk/`

## 1. Contexto

El SDK ya tiene una **capa corpus** operativa, pero hoy solo está cristalizada para el flujo documental incremental:

- `.github/prompts/feed.prompt.md` — documento nuevo -> análisis Bartleby
- `.github/agents/archivero.agent.md` — diff, merge, status sobre `corpus/corpus.md`
- `.github/prompts/diff-corpus.prompt.md` y `merge-corpus.prompt.md` — integración manual aprobada
- `corpus/` — superficie canónica esperada por prompts, agentes y skills del SDK

Lo que todavía no está abstraído en `main` es el segundo modo que legislativa ya cristalizó en el mod: **corpus batch desde una lore-db tipada**.

Hoy esa capacidad vive de facto en:

- `mod/agents/archivero-lore.agent.md` — ingest batch -> Bartleby -> `CORPUS_PREVIEW.md`
- `mod/prompts/lore-ingest.prompt.md` — punto de entrada batch del mod
- `corpus/README.md` y `corpus/corpus.md` — workarounds para compatibilidad mientras el lore vive en `DRAFTS2/`

La consecuencia es una ambigüedad que conviene cerrar:

- `lore-db-sdk` ya separó la **gestión de piezas** del dominio del Archivero
- pero la **reducción a corpus** sigue medio repartida entre `@Archivero`, `@Archivero Lore` y el workaround `corpus/`

Este dossier cristaliza esa capa con backward compatibility. No reabre al Archivero fuera de su dominio: lo formaliza como **agente de corpus** en dos modos compatibles.

Relación con otros dossiers:

| Dossier | Branch | Qué hace | Relación |
|---------|--------|----------|----------|
| `lore-db-sdk` | main | Estructura genérica de piezas y `@Loreador` | Upstream opcional del corpus batch |
| **corpus-sdk** | main | **Contrato portable de la capa corpus** | Este dossier |
| `corpus-legislativa` | mod/legislativa | Migra el corpus real del caso y adapta el mod | Hereda este contrato |
| `grafo-sdk` | main | Contrato genérico del grafo | Downstream directo del corpus |

## 2. Anclas

| Artefacto | Ubicación | Estado |
|-----------|-----------|--------|
| Archivero SDK | `.github/agents/archivero.agent.md` | Operativo — diff/merge/status |
| Feed SDK | `.github/prompts/feed.prompt.md` | Operativo — flujo incremental |
| Diff SDK | `.github/prompts/diff-corpus.prompt.md` | Operativo |
| Merge SDK | `.github/prompts/merge-corpus.prompt.md` | Operativo |
| Status SDK | `.github/prompts/status.prompt.md` | Operativo |
| Guion de ciclo | `.github/templates/guion-ciclo.template.md` | Operativo — asume `/feed -> /diff -> /merge` |
| Archivero Lore (mod) | `mod/agents/archivero-lore.agent.md` | Operativo — ingest batch |
| Workaround corpus/ | `corpus/README.md`, `corpus/corpus.md` | Temporal |

## 3. Restricciones

- **Backward compatibility obligatoria** con `/feed`, `/diff-corpus`, `/merge-corpus` y `/status`
- `@Archivero` sigue **sin analizar documentos directamente**; cualquier ingest delega a `@Bartleby`
- `lore-db-sdk` sigue siendo dueño de la **gestión de piezas**; `corpus-sdk` solo cristaliza la **transformación a corpus**
- `corpus/` vuelve a definirse como **superficie canónica de corpus**, aunque un mod resuelva sus fuentes desde `{{LORE_DIR}}/piezas/`
- No se introduce vocabulario ni shape específico de legislativa en `.github/`

## 4. Propuesta

### 4.1. Contrato portable de la capa corpus

Crear `.github/instructions/corpus-schema.instructions.md` con el shape mínimo:

- `corpus/documentos/` — textos o piezas fuente resolubles desde la capa corpus
- `corpus/analisis/` — análisis Bartleby persistidos cuando el flujo los materializa
- `corpus/corpus.md` — mapa acumulativo canónico

El contrato debe admitir dos modos:

1. **Incremental documental** — un documento entra por `/feed`, se analiza y se mergea
2. **Batch desde lore-db** — un conjunto de piezas validadas se reduce a corpus sin pasar por el usuario documento a documento

### 4.2. Reabrir al Archivero dentro de su dominio de corpus

Actualizar `.github/agents/archivero.agent.md` para formalizar que el Archivero es el agente del corpus en dos planos:

- **curación incremental**: `diff`, `merge`, `status`
- **corpuseado batch**: `ingest` o equivalente, siempre delegando análisis a `@Bartleby`

La clave del corte: el Archivero **no** gestiona piezas ni valida la lore-db; eso sigue siendo de `@Loreador`. Pero sí es dueño de convertir análisis o packs ya validados en `corpus/corpus.md`.

### 4.3. Compatibilidad explícita entre flujos

Actualizar prompts y templates del SDK para documentar los dos caminos válidos:

```text
/feed -> @Bartleby -> corpus/analisis/*.analisis.md -> /diff-corpus -> /merge-corpus
```

```text
@Loreador -> @Archivero ingest -> corpus/corpus.md -> downstream (grafo, etc.)
```

El flujo clásico sigue intacto. El batch se añade como abstracción compatible, no como sustitución.

### 4.4. Documentar corpus como capa propia del SDK

Actualizar `.github/copilot-instructions.md` para dejar explícita la secuencia:

```text
lore-db -> corpus -> grafo -> universos -> cortos
```

y aclarar que, si un mod usa `lore/` como base de datos de piezas, la capa pública de corpus sigue siendo `corpus/`.

## 5. Salida operativa

- Tracking: [BACKLOG.md](./BACKLOG.md)
- Decisiones del PO: [RESPUESTAS.md](./RESPUESTAS.md)
- Tasks: carpeta [tasks](./tasks)