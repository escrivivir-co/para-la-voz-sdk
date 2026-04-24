# Plan — grafo-legislativa

> **Fecha:** 19-abr-2026
> **Autor:** Claude Opus 4.6
> **Dossier:** `sala/dossiers/grafo-legislativa/`

## 1. Contexto

El dossier `grafo-sdk` extrae el **concepto genérico** de grafo al SDK main (schema, template, convención `derivados/grafo/`). Este dossier es su contraparte en el mod: migra el grafo **concreto** del caso Zoowoman desde `DRAFTS2/` a la estructura canónica `lore/derivados/grafo/` y actualiza las refs de los agentes y artefactos que consumen el **grafo**.

Relación con otros dossiers:

| Dossier | Branch | Qué hace | Relación |
|---------|--------|----------|----------|
| `lore-db-sdk` | main | Schema genérico de piezas, scaffold `lore/` | Provee la estructura base |
| `lore-db-legislativa` | mod/legislativa | Migra piezas + hilo base a `lore/` | Crea `lore/` y deja `LORE_F.md` en la base upstream |
| `corpus-legislativa` | mod/legislativa | Materializa el corpus canónico | Sustituye la dependencia anterior de `CORPUS_PREVIEW.md` en `lore/derivados/` |
| `grafo-sdk` | main | Schema genérico de grafo, template gramática | Provee las reglas genéricas |
| `universos-sdk` | main | Contrato portable de universo persistido | Define la capa universo sobre el grafo |
| `universos-legislativa` | mod/legislativa | Migra universos instanciados | Separa la capa universo del dossier de grafo |
| `cortos-legislativa` | mod/legislativa | Migra obras derivadas por modelo | Separa la capa cortos del dossier de grafo |
| **grafo-legislativa** | mod/legislativa | **Migra el grafo concreto + actualiza agentes** | Este dossier |
| `future-machine-legislativa` | mod/legislativa | Instancia la machine del caso Feo — `slot_grafo` | **Downstream:** GL-01 → FL-01 |

## 2. Inventario de assets a migrar

### Grafo JSON (5 ficheros)

| Asset | Origen | Destino |
|-------|--------|---------|
| gramática | `DRAFTS2/grafo/gramatica.md` | `lore/derivados/grafo/gramatica.md` |
| index.json | `DRAFTS2/grafo/index.json` | `lore/derivados/grafo/index.json` |
| nodos.json (289 líneas) | `DRAFTS2/grafo/nodos.json` | `lore/derivados/grafo/nodos.json` |
| arcos.json (199 líneas) | `DRAFTS2/grafo/arcos.json` | `lore/derivados/grafo/arcos.json` |
| huecos.json (50 líneas) | `DRAFTS2/grafo/huecos.json` | `lore/derivados/grafo/huecos.json` |

### Artefactos del grafo (construcción + legacy)

| Asset | Origen | Destino |
|-------|--------|---------|
| artefacto | `DRAFTS2/LORE_F-02_ARTEFACTO.md` | `lore/derivados/LORE_F-02_ARTEFACTO.md` |
| universo (markdown) | `DRAFTS2/LORE_F-02_UNIVERSO.md` | `lore/derivados/LORE_F-02_UNIVERSO.md` |

### Refs internas a actualizar

| Fichero | Qué cambiar |
|---------|-------------|
| `lore/derivados/grafo/index.json` | `corpus_ref`, `artefacto_ref`, `hilo_ref`, `universo_ref` → rutas canónicas nuevas |
| `lore/derivados/grafo/gramatica.md` | Cabecera `Target` → `lore/derivados/grafo/` |
| `mod/agents/grafista.agent.md` | Rutas `DRAFTS2/` → `corpus/` para corpus y `lore/` para hilo/grafo/artefactos |
| `mod/agents/archivero-lore.agent.md` | Rutas `DRAFTS2/LORE_INDEX`, `DRAFTS2/LORE_F` |
| `mod/instructions/lore-estado.instructions.md` | Rutas si las tiene |

## 3. Anclas

| Artefacto | Ubicación | Estado |
|-----------|-----------|--------|
| Grafo JSON v1.0 | `DRAFTS2/grafo/` | 20 nodos, 22 arcos, 7 huecos |
| Gramática v1.0 | `DRAFTS2/grafo/gramatica.md` | 4 tipos nodo, 4 estratos |
| Grafo markdown legacy | `DRAFTS2/LORE_F-02_UNIVERSO.md` | 20 nodos, 4 ramas, pivote X |
| Dossier archivado | `sala/archivo/sprint-cristalizacion-v1/dossiers/cristalizacion-grafo-json/` | Referencia histórica |
| lore-db-legislativa LP-01 | `sala/dossiers/lore-db-legislativa/` | Crea `lore/derivados/` |
| grafo-sdk GS-01..04 | `sala/dossiers/grafo-sdk/` | Schema + template genéricos |

## 4. Restricciones

- **`git mv` obligatorio** — preservar historial de los ficheros migrados
- No modificar contenido del grafo durante la migración (solo rutas)
- La gramática legislativa sigue siendo del mod — no se mueve al SDK
- Depende de LP-01b (estructura creada + hilo base migrado), CP-01 (corpus canónico materializado) y GS-01 (schema genérico ya definido)
- Los agentes deben seguir funcionando con las rutas nuevas inmediatamente después de la migración

## 5. Propuesta

### 5.1. Migrar grafo JSON (GL-01)

`git mv DRAFTS2/grafo/ lore/derivados/grafo/` — los 5 ficheros de golpe. Actualizar `index.json` con rutas nuevas.

### 5.2. Migrar artefactos de construcción del grafo (GL-02)

`git mv` de `LORE_F-02_ARTEFACTO.md` y `LORE_F-02_UNIVERSO.md`. Son los dos artefactos markdown ligados al grafo como construcción y representación legacy.

### 5.3. Actualizar refs en consumidores del grafo (GL-03)

Grafista, Archivero y las instructions que consumen estado/rutas del grafo — rutas `DRAFTS2/` → `lore/derivados/` o `lore/piezas/` según corresponda. También gramática header e `index.json`.

### 5.4. Validar integridad (GL-04)

Verificar que `piezas_ancla` de nodos.json siguen resolviendo contra `corpus/corpus.md` o su routing explícito. Que los agentes leen sin error. Que el pipeline documenta la ruta nueva.

## 6. Salida operativa

- Tracking: [BACKLOG.md](./BACKLOG.md)
- Decisiones del PO: [RESPUESTAS.md](./RESPUESTAS.md)
- Tasks: carpeta [tasks](./tasks)
