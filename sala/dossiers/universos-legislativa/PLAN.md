# Plan — universos-legislativa

> **Fecha:** 19-abr-2026
> **Autor:** GPT-5.4
> **Dossier:** `sala/dossiers/universos-legislativa/`

## 1. Contexto

Tras la migración de lore-db y grafo, la capa de **universo instanciado** necesita su propio dossier en el mod:

- `@Demiurgo` debe dejar de leer `DRAFTS2/` y conectarse al grafo migrado
- las ramas persistidas deben salir de `DRAFTS2/universo/`
- `legislativa-universo.instructions.md` debe apuntar a la estructura nueva

Este dossier separa la capa `grafo -> universo` de `grafo-legislativa`, para que el grafo deje de absorber downstream que no le corresponde y para que la capa `cortos` viva en un dossier específico.

Relación con otros dossiers:

| Dossier | Branch | Qué hace | Relación |
|---------|--------|----------|----------|
| `grafo-sdk` | main | Contrato genérico de grafo | Upstream del universo |
| `grafo-legislativa` | mod/legislativa | Migra grafo JSON + artefactos del grafo | Provee el input del Demiurgo |
| `universos-sdk` | main | Contrato portable de universo persistido | Provee el shape genérico |
| `cortos-legislativa` | mod/legislativa | Migra obras derivadas y recablea Dramaturgo | Downstream de este dossier |
| **universos-legislativa** | mod/legislativa | **Migra universos y recablea Demiurgo** | Este dossier |

## 2. Inventario de assets a migrar

### Universos instanciados

| Asset | Origen | Destino |
|-------|--------|---------|
| universo-1 | `DRAFTS2/universo/universo-1.md` | `lore/derivados/universo/universo-1.md` |
| universo-1-r1 | `DRAFTS2/universo/universo-1-r1.md` | `lore/derivados/universo/universo-1-r1.md` |
| universo-1-r2 | `DRAFTS2/universo/universo-1-r2.md` | `lore/derivados/universo/universo-1-r2.md` |

### Refs a actualizar

| Fichero | Qué cambiar |
|---------|-------------|
| `mod/agents/demiurgo.agent.md` | Todas las rutas `DRAFTS2/` → `lore/` para grafo, universo, artefacto, corpus, hilo |
| `mod/agents/pipeline.agent.md` | Conexión de la etapa `universo` con la cadena nueva hacia `cortos` |
| `mod/instructions/legislativa-universo.instructions.md` | `applyTo` y refs de rutas |
| `mod/instructions/lore-estado.instructions.md` | Rutas y conteos de universos si aplica |

## 3. Anclas

| Artefacto | Ubicación | Estado |
|-----------|-----------|--------|
| Demiurgo (mod) | `mod/agents/demiurgo.agent.md` | Operativo — aún atado a `DRAFTS2/` |
| Universos actuales | `DRAFTS2/universo/` | 3 ficheros |
| Instrucciones de universo | `mod/instructions/legislativa-universo.instructions.md` | Regla del mod aún ligada a `DRAFTS2/**` |
| Future-machine archivado | `sala/archivo/sprint-cristalizacion-v1/dossiers/future-machine-universo-1/` | Referencia histórica |

## 4. Restricciones

- **`git mv` obligatorio** para universos
- Depende de `LP-01b` (base lore-db creada), `GL-01` y `GL-02` (grafo y artefactos ya migrados)
- `PLAN_UNIVERSO1_V2.md` no se migra: sigue siendo plan de trabajo, no artefacto del lore-db
- La migración de cortos y su convención por modelo se resuelve en `cortos-legislativa`

## 5. Propuesta

### 5.1. Migrar los 3 universos existentes (UL-01)

Mover `DRAFTS2/universo/` a `lore/derivados/universo/` con `git mv`.

### 5.2. Recablear Demiurgo y Pipeline (UL-02)

Actualizar rutas y handoffs para que la secuencia `grafo -> universo -> cortos` funcione desde `lore/`.

### 5.3. Adaptar instructions del universo (UL-03)

Actualizar `mod/instructions/legislativa-universo.instructions.md` a la nueva estructura y dejar de aplicar a `DRAFTS2/**`.

### 5.4. Validar la cadena `Grafista -> Demiurgo` y el handoff a `Dramaturgo Cortos` (UL-04)

Verificar coherencia de lectura y handoffs con las rutas nuevas antes de la fase de cortos.

## 6. Salida operativa

- Tracking: [BACKLOG.md](./BACKLOG.md)
- Decisiones del PO: [RESPUESTAS.md](./RESPUESTAS.md)
- Tasks: carpeta [tasks](./tasks)