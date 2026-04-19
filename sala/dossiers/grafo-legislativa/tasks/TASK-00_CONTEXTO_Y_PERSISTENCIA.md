# TASK-00 — Contexto y persistencia del dossier grafo-legislativa

> **Estado:** cerrada
> **Agente:** Claude Opus 4.6
> **Fecha:** 19-abr-2026

## Contexto congelado

### Inventario del grafo actual

**Grafo JSON** (`DRAFTS2/grafo/`, v1.0):
- `index.json` — metadatos, versión, estadísticas (20 nodos, 22 arcos, 7 huecos)
- `nodos.json` — 289 líneas, 4 tipos (estado, bifurcacion, rama, hueco), 3 estratos (T0, X, X-Tinf)
- `arcos.json` — 199 líneas, conexiones dirigidas con peso y justificación
- `huecos.json` — 50 líneas, 7 huecos (5 resueltos, 2 abiertos)
- `gramatica.md` — spec de la gramática JSON, 130 líneas

**Derivados del grafo** (en `DRAFTS2/`):
- `LORE_F-02_ARTEFACTO.md` — artefacto de construcción (ficha técnica, reglas, nodos)
- `LORE_F-02_UNIVERSO.md` — grafo principal markdown (T=0 → X → T+∞)
- `LORE_F-02_CORTO.md` — corto original (*Tres Lunes Para Una Misma Sala*)
- `LORE_F-02_CORTO-universo-1-claude-opus-4.md` — corto Claude Opus 4
- `LORE_F-02_CORTO-universo-1-claude-opus-4-2.md` — corto Claude Opus 4 (2ª iteración)
- `LORE_F-02_CORTO-universo-1-gemini-3.1-pro.md` — corto Gemini 3.1 Pro
- `LORE_F-02_CORTO-universo-1-gpt-5-4.md` — corto GPT-5.4

**Ramas instanciadas** (`DRAFTS2/universo/`):
- `universo-1.md` — rama principal instanciada
- `universo-1-r1.md` — revisión 1
- `universo-1-r2.md` — revisión 2

### Refs cruzadas en agentes (rutas a actualizar)

**Grafista** (`mod/agents/grafista.agent.md`):
- `DRAFTS2/CORPUS_PREVIEW.md`, `DRAFTS2/LORE_F.md`, `DRAFTS2/grafo/index.json`, `DRAFTS2/LORE_F-02_ARTEFACTO.md`, `DRAFTS2/LORE_F-02_UNIVERSO.md`, `DRAFTS2/grafo/gramatica.md`

**Dramaturgo** (`mod/agents/dramaturgo.agent.md`):
- `DRAFTS2/LORE_F-02_UNIVERSO.md`, `DRAFTS2/universo/`, `DRAFTS2/LORE_F-02_ARTEFACTO.md`, `DRAFTS2/LORE_F-02_CORTO.md`, `DRAFTS2/LORE_F.md`, `DRAFTS2/CORPUS_PREVIEW.md`

**Archivero Lore** (`mod/agents/archivero-lore.agent.md`):
- `DRAFTS2/LORE_INDEX.md`, `DRAFTS2/LORE_F.md`

**Demiurgo** (`mod/agents/demiurgo.agent.md`):
- Refs a grafo y universo (verificar)

### Refs internas en ficheros del grafo

**`index.json`** — campos con rutas DRAFTS2:
```json
"corpus_ref": "DRAFTS2/CORPUS_PREVIEW.md",
"artefacto_ref": "DRAFTS2/LORE_F-02_ARTEFACTO.md",
"hilo_ref": "DRAFTS2/LORE_F.md",
"universo_ref": "DRAFTS2/LORE_F-02_UNIVERSO.md"
```

**`gramatica.md`** — cabecera:
```
Target: [...] ficheros JSON bajo `DRAFTS2/grafo/` para el mod legislativa.
```

### Dossier archivado de referencia

El grafo JSON fue cristalizado en el sprint anterior: `sala/archivo/sprint-cristalizacion-v1/dossiers/cristalizacion-grafo-json/` (7 tasks, completado).

### Dependencias

- **LP-01** (`lore-db-legislativa`): crea la estructura `lore/derivados/` donde el grafo aterrizará
- **GS-01** (`grafo-sdk`): define el schema genérico que la gramática legislativa especializa
- **LP-01b** (`lore-db-legislativa`): migra piezas — las `piezas_ancla` del grafo deben resolver contra la nueva ubicación del corpus
