# Plan — grafo-legislativa

> **Fecha:** 19-abr-2026
> **Autor:** Claude Opus 4.6
> **Dossier:** `sala/dossiers/grafo-legislativa/`

## 1. Contexto

El dossier `grafo-sdk` extrae el **concepto genérico** de grafo al SDK main (schema, template, convención `derivados/grafo/`). Este dossier es su contraparte en el mod: migra el grafo **concreto** del caso Zoowoman desde `DRAFTS2/` a la estructura canónica `lore/derivados/grafo/` y actualiza las refs de todos los agentes consumidores.

Relación con otros dossiers:

| Dossier | Branch | Qué hace | Relación |
|---------|--------|----------|----------|
| `lore-db-sdk` | main | Schema genérico de piezas, scaffold `lore/` | Provee la estructura base |
| `lore-db-legislativa` | mod/legislativa | Migra piezas + derivados a `lore/` | Crea `lore/derivados/` donde vivirá el grafo |
| `grafo-sdk` | main | Schema genérico de grafo, template gramática | Provee las reglas genéricas |
| **grafo-legislativa** | mod/legislativa | **Migra el grafo concreto + actualiza agentes** | Este dossier |

## 2. Inventario de assets a migrar

### Grafo JSON (5 ficheros)

| Asset | Origen | Destino |
|-------|--------|---------|
| gramática | `DRAFTS2/grafo/gramatica.md` | `lore/derivados/grafo/gramatica.md` |
| index.json | `DRAFTS2/grafo/index.json` | `lore/derivados/grafo/index.json` |
| nodos.json (289 líneas) | `DRAFTS2/grafo/nodos.json` | `lore/derivados/grafo/nodos.json` |
| arcos.json (199 líneas) | `DRAFTS2/grafo/arcos.json` | `lore/derivados/grafo/arcos.json` |
| huecos.json (50 líneas) | `DRAFTS2/grafo/huecos.json` | `lore/derivados/grafo/huecos.json` |

### Derivados del grafo (universos, artefacto, cortos)

| Asset | Origen | Destino |
|-------|--------|---------|
| artefacto | `DRAFTS2/LORE_F-02_ARTEFACTO.md` | `lore/derivados/LORE_F-02_ARTEFACTO.md` |
| universo (markdown) | `DRAFTS2/LORE_F-02_UNIVERSO.md` | `lore/derivados/LORE_F-02_UNIVERSO.md` |
| corto original | `DRAFTS2/LORE_F-02_CORTO.md` | `lore/derivados/LORE_F-02_CORTO.md` |
| corto claude-opus-4 | `DRAFTS2/LORE_F-02_CORTO-universo-1-claude-opus-4.md` | `lore/derivados/LORE_F-02_CORTO-universo-1-claude-opus-4.md` |
| corto claude-opus-4-2 | `DRAFTS2/LORE_F-02_CORTO-universo-1-claude-opus-4-2.md` | `lore/derivados/LORE_F-02_CORTO-universo-1-claude-opus-4-2.md` |
| corto gemini | `DRAFTS2/LORE_F-02_CORTO-universo-1-gemini-3.1-pro.md` | `lore/derivados/LORE_F-02_CORTO-universo-1-gemini-3.1-pro.md` |
| corto gpt-5 | `DRAFTS2/LORE_F-02_CORTO-universo-1-gpt-5-4.md` | `lore/derivados/LORE_F-02_CORTO-universo-1-gpt-5-4.md` |
| rama universo-1 | `DRAFTS2/universo/universo-1.md` | `lore/derivados/universo/universo-1.md` |
| rama universo-1-r1 | `DRAFTS2/universo/universo-1-r1.md` | `lore/derivados/universo/universo-1-r1.md` |
| rama universo-1-r2 | `DRAFTS2/universo/universo-1-r2.md` | `lore/derivados/universo/universo-1-r2.md` |

### Refs internas a actualizar

| Fichero | Qué cambiar |
|---------|-------------|
| `lore/derivados/grafo/index.json` | `corpus_ref`, `artefacto_ref`, `hilo_ref`, `universo_ref` → rutas `lore/` |
| `lore/derivados/grafo/gramatica.md` | Cabecera `Target` → `lore/derivados/grafo/` |
| `mod/agents/grafista.agent.md` | 7 rutas `DRAFTS2/` → `lore/` (vía `{{LORE_DIR}}` o directas) |
| `mod/agents/demiurgo.agent.md` | Rutas a grafo y universo |
| `mod/agents/dramaturgo.agent.md` | 7 rutas `DRAFTS2/` → `lore/` |
| `mod/agents/archivero-lore.agent.md` | Rutas `DRAFTS2/LORE_INDEX`, `DRAFTS2/LORE_F` |
| `mod/instructions/lore-estado.instructions.md` | Rutas si las tiene |
| `mod/instructions/legislativa-universo.instructions.md` | Rutas si las tiene |

## 3. Anclas

| Artefacto | Ubicación | Estado |
|-----------|-----------|--------|
| Grafo JSON v1.0 | `DRAFTS2/grafo/` | 20 nodos, 22 arcos, 7 huecos |
| Gramática v1.0 | `DRAFTS2/grafo/gramatica.md` | 4 tipos nodo, 4 estratos |
| Universo-1 instanciado | `DRAFTS2/universo/` | 3 ficheros + 5 cortos |
| Dossier archivado | `sala/archivo/sprint-cristalizacion-v1/dossiers/cristalizacion-grafo-json/` | Referencia histórica |
| lore-db-legislativa LP-01 | `sala/dossiers/lore-db-legislativa/` | Crea `lore/derivados/` |
| grafo-sdk GS-01..04 | `sala/dossiers/grafo-sdk/` | Schema + template genéricos |

## 4. Restricciones

- **`git mv` obligatorio** — preservar historial de los ficheros migrados
- No modificar contenido del grafo durante la migración (solo rutas)
- La gramática legislativa sigue siendo del mod — no se mueve al SDK
- Depende de LP-01 (estructura `lore/derivados/` ya creada) y GS-01 (schema genérico ya definido)
- Los agentes deben seguir funcionando con las rutas nuevas inmediatamente después de la migración

## 5. Propuesta

### 5.1. Migrar grafo JSON (GL-01)

`git mv DRAFTS2/grafo/ lore/derivados/grafo/` — los 5 ficheros de golpe. Actualizar `index.json` con rutas nuevas.

### 5.2. Migrar derivados del universo (GL-02)

`git mv` de artefacto, universo markdown, cortos, ramas. Son ~10 ficheros.

### 5.3. Actualizar refs en agentes (GL-03)

Grafista, Demiurgo, Dramaturgo, Archivero — todas las rutas `DRAFTS2/` → `lore/derivados/` o `lore/piezas/` según corresponda. También gramática header y index.json refs.

### 5.4. Validar integridad (GL-04)

Verificar que `piezas_ancla` de nodos.json siguen resolviendo contra `lore/derivados/CORPUS_PREVIEW.md`. Que los agentes leen sin error. Que el pipeline documenta la ruta nueva.

## 6. Salida operativa

- Tracking: [BACKLOG.md](./BACKLOG.md)
- Decisiones del PO: [RESPUESTAS.md](./RESPUESTAS.md)
- Tasks: carpeta [tasks](./tasks)
