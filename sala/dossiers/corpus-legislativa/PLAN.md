# Plan — corpus-legislativa

> **Fecha:** 19-abr-2026
> **Autor:** GPT-5.4
> **Dossier:** `sala/dossiers/corpus-legislativa/`

## 1. Contexto

El mod legislativa ya probó en la práctica que **corpus** es una capa propia del pipeline, distinta de `lore-db`:

- `DRAFTS2/CORPUS_PREVIEW.md` es el mapa acumulativo real del caso
- `mod/agents/archivero-lore.agent.md` ya hace ingest batch desde piezas tipadas
- `mod/prompts/lore-ingest.prompt.md` ya expone un punto de entrada corpus-first
- `corpus/` hoy existe, pero solo como shim de compatibilidad hacia `DRAFTS2/`

El problema es que la migración reciente de `lore-db` estaba absorbiendo demasiado scope a la vez:

- piezas tipadas y scaffold `lore/`
- corpus batch y routing de `corpus/`
- recableado downstream a grafo

Si aceptamos el criterio que ya separó `grafo`, `universos` y `cortos`, la capa `corpus` también merece pareja propia.

Este dossier es la contraparte mod de `corpus-sdk`.

Relación con otros dossiers:

| Dossier | Branch | Qué hace | Relación |
|---------|--------|----------|----------|
| `lore-db-legislativa` | mod/legislativa | Migra la base de datos de piezas a `lore/` | Upstream directo |
| `corpus-sdk` | main | Contrato portable de la capa corpus | Provee el shape genérico |
| **corpus-legislativa** | mod/legislativa | **Materializa corpus real y adapta Archivero del mod** | Este dossier |
| `grafo-legislativa` | mod/legislativa | Migra grafo y actualiza consumidores downstream | Downstream directo |

## 2. Inventario de assets a migrar o redefinir

| Asset | Estado actual | Destino objetivo |
|-------|---------------|------------------|
| `corpus/README.md` | redirect shim | README de capa corpus real |
| `corpus/corpus.md` | redirect shim | mapa canónico real del corpus |
| `DRAFTS2/CORPUS_PREVIEW.md` | fuente viva temporal | integrado en la capa `corpus/` |
| `corpus/documentos/` | no materializado | superficie canónica de piezas/documentos resolubles |
| `corpus/analisis/` | no materializado | superficie canónica de análisis Bartleby o estado documentado |

## 3. Refs a actualizar

| Fichero | Qué cambiar |
|---------|-------------|
| `mod/agents/archivero-lore.agent.md` | Rutas y narrativa: corpus ya no como preview lateral sino como capa canónica |
| `mod/prompts/lore-ingest.prompt.md` | Input/output corpus sobre la ruta nueva |
| `mod/agents/pipeline.agent.md` | Tramo `lore-db -> corpus -> grafo` explícito |
| `mod/agents/grafista.agent.md` | Lectura del corpus canónico, no de `DRAFTS2/CORPUS_PREVIEW.md` |
| `mod/agents/demiurgo.agent.md` | Referencias factuales del corpus vía ruta canónica |
| `mod/agents/dramaturgo.agent.md` | Referencias factuales del corpus vía ruta canónica |
| `mod/instructions/lore-routing.instructions.md` | `corpus/` deja de ser workaround |
| `mod/instructions/onboarding-map.instructions.md` | `corpus/` pasa a ser capa real |

## 4. Anclas

| Artefacto | Ubicación | Estado |
|-----------|-----------|--------|
| Corpus vivo actual | `DRAFTS2/CORPUS_PREVIEW.md` | Operativo |
| Shim corpus | `corpus/README.md`, `corpus/corpus.md` | Temporal |
| Archivero Lore | `mod/agents/archivero-lore.agent.md` | Operativo — batch |
| lore-ingest | `mod/prompts/lore-ingest.prompt.md` | Operativo |
| FEAT-06 | `DRAFTS2/FEAT-06_PIPELINE_REFRESH.md` | Ya fija `piezas -> {CORPUS_PREVIEW ∥ LORE_F}` |
| lore-routing | `mod/instructions/lore-routing.instructions.md` | Hoy marca `corpus/` como workaround |

## 5. Restricciones

- **Backward compatibility obligatoria** con el SDK base y con los prompts actuales del mod
- La capa `corpus/` vuelve a ser canónica; no puede quedarse en redirect indefinido
- `lore/` sigue siendo la base de datos de piezas; `corpus/` es el mapa corpus, no un duplicado casual de toda la lore-db
- Si hay mirror o routing entre `corpus/documentos/` y `lore/piezas/`, debe quedar documentado y no implícito
- Downstream (`grafo`, `universos`, `cortos`) debe consumir corpus canónico, no rutas `DRAFTS2/` duras

## 6. Propuesta

### 6.1. Materializar `corpus/` como capa real (CP-01)

Dejar de tratar `corpus/README.md` y `corpus/corpus.md` como simples notas de redirección. Este dossier define y ejecuta la migración del corpus vivo hacia la capa `corpus/`.

### 6.2. Definir la relación `lore/piezas/` <-> `corpus/documentos/` (CP-02)

Legislativa ya tiene una lore-db tipada. El corpus debe poder exponer piezas/documentos sin introducir duplicación muda. La task fija si la solución es mirror materializado, routing explícito o una combinación documentada.

### 6.3. Recentrar `@Archivero Legislativa` en la capa corpus (CP-03)

La recomendación de este dossier es mantener el nombre público `@Archivero Legislativa` por compatibilidad, pero dejar explícito que es la especialización legislativa del Archivero corpus del SDK:

- recibe piezas ya validadas upstream
- delega análisis a Bartleby
- escribe corpus canónico

### 6.4. Recablear consumidores downstream (CP-04)

Grafo, Portal, Pipeline y el resto de consumidores dejan de leer `DRAFTS2/CORPUS_PREVIEW.md` como ruta dura y pasan a consumir corpus canónico o routing resuelto desde ahí.

### 6.5. Validar compatibilidad total (CP-05)

Verificar que conviven sin ruptura:

- `/feed`, `/diff-corpus`, `/merge-corpus`, `/status`
- `/lore-ingest`
- Pipeline del mod
- consumidores downstream del corpus

## 7. Salida operativa

- Tracking: [BACKLOG.md](./BACKLOG.md)
- Decisiones del PO: [RESPUESTAS.md](./RESPUESTAS.md)
- Tasks: carpeta [tasks](./tasks)