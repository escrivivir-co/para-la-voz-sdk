# Plan — future-machine-sdk

> **Fecha:** 19-abr-2026
> **Refactorizado:** 19-abr-2026 — Claude Opus 4.6 (sesión Cristalizador)
> **Dossier:** `sala/dossiers/future-machine-sdk/`

---

## 0. El pipeline completo — vista por agente

### En `main` (SDK genérico: contratos, no datos)

| # | Agente | Directorio/ficheros clave | Qué hace | Input | Output |
|---|--------|--------------------------|----------|-------|--------|
| 1 | **`@Loreador`** | *No existe aún* — previsto como `.github/agents/loreador.agent.md` | Gestiona la DB de piezas tipadas y la composición de LORE_F | Piezas sueltas del usuario (ficheros en disco) | `{{LORE_DIR}}/INDEX.md` (inventario DRY), `LORE_F.md` (hilo factual) |
| 2 | **`@Bartleby`** | `.github/agents/bartleby.agent.md`, `.github/skills/documental-analysis/` | Analiza documentos sin juzgar. Extrae herencia, taxonomía, mecanismos, emergencias | `LORE_F.md` o cualquier documento vía `/feed` | `corpus/analisis/*.analisis.md` |
| 3 | **`@Archivero`** | `.github/agents/archivero.agent.md`, prompts: `/feed`, `/diff-corpus`, `/merge-corpus`, `/status` | Gestiona la capa corpus: diff, merge acumulativo, status | Análisis de Bartleby + `corpus/corpus.md` actual | `corpus/corpus.md` actualizado (merge acumulativo) |
| 4 | **`@Grafista`** | *No existe aún en main* — previsto en `grafo-sdk` | Construye el grafo de bifurcación desde datos + analítica | `LORE_F` (datos factuales) + `corpus/corpus.md` (analítica) | `{{LORE_DIR}}/derivados/grafo/*.json` (nodos, arcos, huecos) |
| 5 | **`@Demiurgo`** | *No existe aún en main* — previsto en `universos-sdk` | Instancia universos: rellena variables + elige inicializaciones | Grafo de bifurcación | `{{LORE_DIR}}/derivados/universo/*.md` (spec concreta) |
| 6 | **`@Dramaturgo`** | `.github/agents/dramaturgo.agent.md`, `.github/skills/futures-engine/`, prompt: `/universo` | Genera obra literaria desde un universo | Universo (spec concreta) | `{{LORE_DIR}}/derivados/cortos/*.md` (producción en lenguaje natural) |
| 7 | **`@Pipeline`** | *No existe aún* — previsto en este dossier como `.github/agents/pipeline.agent.md` | Orquesta el refresh de la cadena cuando cambian las piezas base | `FUTURE_MACHINE.md` (manifiesto de slots) | Deltas por nivel + handoffs al siguiente agente |
| 8 | **`@Portal`** | `.github/agents/portal.agent.md` | Puerta de entrada: detecta perfil, ofrece el camino correcto | La machine si existe, o el corpus | Navegación al agente correcto |
| — | **`@Cristalizador`** | `.github/agents/cristalizador.agent.md`, prompt: `/design` | Propone infraestructura agéntica nueva | Workspace + `COPILOT/` | Propuestas, dossiers, artefactos en `mod/` |

### En `mod/legislativa` (datos reales en DRAFTS2/ esperando migrar)

| # | Agente mod | Ficheros en codebase | Input actual (DRAFTS2/) | Output actual (DRAFTS2/) | Destino tras migración |
|---|-----------|---------------------|------------------------|-------------------------|----------------------|
| 1 | **`@Puzzle`** `mod/agents/puzzle.agent.md` | `mod/instructions/lore-schema.instructions.md`, `mod/instructions/lore-routing.instructions.md` | `DRAFTS2/LORE_INDEX.md` (51 piezas) | Validación de inventario vs disco | `lore/INDEX.md` |
| 1b | **`@Archivero Lore`** `mod/agents/archivero-lore.agent.md` | prompt: `/lore-ingest` | Piezas tipadas: `LORE_S-*.md` (13), `LORE_N-*.md` (4), `LORE_P-*.md` (3), `LORE_T-*.md` (4), `LORE_R-*.md` (2) | — | `lore/piezas/` |
| 1c | — (composición manual) | — | Piezas sueltas | `DRAFTS2/LORE_F.md` (hilo factual completo) | `lore/LORE_F.md` |
| 2 | **`@Bartleby`** (heredado SDK) | — | `LORE_F.md` | Análisis implícito en `CORPUS_PREVIEW.md` | `corpus/analisis/` |
| 3 | **`@Archivero Lore`** (ingest batch) | — | `DRAFTS2/CORPUS_PREVIEW.md` | `corpus/corpus.md` (shim actual) | `corpus/corpus.md` (canónico) |
| 4 | **`@Grafista`** `mod/agents/grafista.agent.md` | `DRAFTS2/grafo/gramatica.md` | `LORE_F.md` + `corpus/corpus.md` | `DRAFTS2/grafo/` — `index.json`, `nodos.json`, `arcos.json`, `huecos.json` (20 nodos, 4 ramas) | `lore/derivados/grafo/` |
| 4b | — | `DRAFTS2/LORE_F-02_ARTEFACTO.md` | Grafo + CORPUS_PREVIEW + LORE_F | Spec de construcción (join de hermanos) | `lore/derivados/grafo/artefacto.md` |
| 5 | **`@Demiurgo`** `mod/agents/demiurgo.agent.md` | `DRAFTS2/LORE_F-02_UNIVERSO.md` | Artefacto (spec del grafo instanciada) | `DRAFTS2/universo/universo-1.md`, `universo-1-r1.md`, `universo-1-r2.md` | `lore/derivados/universo/` |
| 6 | **`@Dramaturgo Cortos`** `mod/agents/dramaturgo.agent.md` | prompts: `/corto-universo` | Universo expandido | 5 cortos: `LORE_F-02_CORTO*.md` (Claude Opus 4, Opus 4.2, Gemini 3.1 Pro, GPT-5.4, original) | `lore/derivados/cortos/` |
| 7 | **`@Pipeline`** `mod/agents/pipeline.agent.md` | prompt: `/pipeline-refresh`, spec: `FEAT-06_PIPELINE_REFRESH.md` | Todo el pipeline | Deltas por nivel + handoffs | Se mantiene en `mod/agents/` (hereda de SDK) |
| 8 | **`@Portal`** `mod/agents/portal.agent.md` | prompts: `/user-empieza-aqui`, `/lore-status` | La machine del mod | Navegación rica con 11 handoffs | Se mantiene en `mod/agents/` |

### Datos en DRAFTS2/ pendientes de migración

| Bloque | Ficheros | Destino propuesto |
|--------|----------|-------------------|
| Piezas (26 ficheros) | `LORE_S-*`, `LORE_N-*`, `LORE_P-*`, `LORE_T-*`, `LORE_R-*`, `LORE_A..F`, `LORE_DRAFT*` | `lore/piezas/` |
| Índice | `LORE_INDEX.md` | `lore/INDEX.md` |
| Hilo factual | `LORE_F.md` | `lore/LORE_F.md` |
| Corpus preview | `CORPUS_PREVIEW.md` | `corpus/corpus.md` (merge canónico) |
| Artefacto | `LORE_F-02_ARTEFACTO.md` | `lore/derivados/grafo/artefacto.md` |
| Grafo JSON (5 ficheros) | `grafo/index.json`, `nodos.json`, `arcos.json`, `huecos.json`, `gramatica.md` | `lore/derivados/grafo/` |
| Universo spec | `LORE_F-02_UNIVERSO.md` | `lore/derivados/universo/` |
| Universo expandido (3 ramas) | `universo/universo-1.md`, `r1.md`, `r2.md` | `lore/derivados/universo/` |
| Cortos (5 ficheros) | `LORE_F-02_CORTO*.md` | `lore/derivados/cortos/` |
| Specs y diarios | `FEAT-06_*.md`, `PLAN_*.md`, `DIARIO_*.png`, `mod_legislativa_*.md` | Archivo o descarte |

---

## 1. Qué es la future-machine

La future-machine no es una capa de datos más. Es la **máquina completa** que ensambla las 5 capas del SDK en un ciclo operativo de principio a fin:

```
piezas ──→ LORE_F ──→ corpus ──→ grafo ──→ universo ──→ corto
                         ↑          ↑
                      Bartleby   Archivero
                      (análisis) (merge)
```

Cada capa tiene su dossier hermano que define el contrato individual. Este dossier define:

1. **`@Pipeline`** — el agente SDK que orquesta el refresh de la cadena
2. **3 prompts de entrypoint** — la puerta de entrada, el dashboard y el refresh
3. **El manifiesto** — `FUTURE_MACHINE.md`, el documento que un mod instancia para declarar sus slots
4. **La integración con `@Portal`** — para que la machine sea navegable

## 2. El ciclo contado por sus agentes

### `@Loreador` — la base de datos de piezas

> Dossier: `lore-db-sdk`

Gestiona dos stores:

- **Piezas sueltas** — ficheros aislados en disco, tipados con marca (`[P-XX]`, `[S-XX]`, etc.). El usuario trabaja pieza por pieza y el agente mantiene la referencia en el índice DRY de la lore-db (`{{LORE_DIR}}/INDEX.md`).
- **LORE_F** — primera composición factual de piezas. Aglutina todas o algunas piezas en un hilo temporal que va del pasado al presente. Es la primera exportación. No es análisis: es el dato hilado.

La LORE_F es lo que alimenta tanto a `@Archivero` (para el feed/merge al corpus) como al `@Grafista` (como fuente de datos factuales para el grafo).

> **Nota para `lore-db-sdk`:** formalizar la dualidad piezas/LORE_F como dos modos de la UI del Loreador. En una el usuario trabaja con los ficheros en disco aislados de cada pieza y el agente le ayuda a mantener la referencia en el índice DRY de la lore-db. Aglutinar "todas" o "algunas" de las piezas en una LORE_F es una primera exportación factual.

### `@Archivero` — la capa corpus

> Dossier: `corpus-sdk`

Recibe la LORE_F y la pasa por el pipeline documental:

1. `@Bartleby` analiza (skill `documental-analysis`) → produce `.analisis.md`
2. `@Archivero` hace diff contra `corpus/corpus.md`
3. El usuario aprueba el merge

El **protocolo de acumulación en merge** es clave: el corpus crece por capas sucesivas, cada merge suma hallazgos aprobados sin reescribir lo anterior. El corpus es el mapa analítico acumulativo.

> **Nota para `corpus-sdk`:** documentar explícitamente el protocolo de acumulación del merge. El corpus no se regenera: se acumula. Cada merge añade delta aprobado.

### `@Grafista` — el grafo de bifurcación

> Dossier: `grafo-sdk`

El grafo recibe **dos fuentes de datos complementarias**:

| Fuente | Tipo | Qué aporta |
|--------|------|------------|
| `lore-db` + `LORE_F` | Datos factuales | Variables de estado, hechos, cronología pasado→presente |
| `corpus/corpus.md` | Analítica | Taxonomía, mecanismos, tensiones, ausencias, emergencias |

Ambas cubren la **línea temporal pasado→presente**. El grafo es la **hiperlínea temporal** que extiende desde el presente el radicoma de futuros plausibles. Cada nodo de bifurcación es un punto donde el sistema puede ir en direcciones distinguibles.

El mecanismo de **ponderación de plausibilidad** de las ramas necesita revisión y formalización como parte del schema genérico del grafo (coordinar con el skill `futures-engine` y el equipo Retro).

> **Nota para `grafo-sdk`:** revisar el mecanismo de ponderación de plausibilidad estimada de los mundos. Contactar con el equipo Retro para formalizar los criterios de plausibilidad estructural del skill `futures-engine` dentro del schema genérico del grafo.

### `@Demiurgo` — los universos

> Dossier: `universos-sdk`

Un universo es una **concreción del grafo para un caso**. El proceso es:

1. **Rellenar variables** — elegir valores concretos para las variables de estado que el grafo dejó abiertas
2. **Elegir inicializaciones** — seleccionar qué nodos de bifurcación se activan y en qué dirección

El fichero del universo es el artefacto que resulta de esas elecciones. No es ficción todavía: es la **spec concreta** que el agente literario usa para crear cortos.

> **Nota para `universos-sdk`:** reformular el schema para hacer explícito que un universo es "rellenar variables + elegir inicializaciones" sobre el grafo. El universo es la concreción del artefacto; la obra es su downstream.

### `@Dramaturgo` — los cortos

> Dossier: `cortos-sdk`

Los cortos son **producciones literarias en lenguaje natural**. Son el output final de la máquina. Cada corto nace de un universo concreto, usa un registro literario del skill `futures-engine`, y se persiste con metadatos de modelo generador.

No hay más transformación después del corto. Es la salida.

> **Nota para `cortos-sdk`:** los cortos son producciones al uso en lenguaje natural. Son la salida final. No hay más transformación después.

### `@Pipeline` — el orquestador de refresh

> Dossier: **este** (`future-machine-sdk`)

El agente que recorre la cadena cuando cambian las piezas base. mod/legislativa ya lo validó como `mod/agents/pipeline.agent.md` con handoffs a toda la cadena. Este dossier sube el **contrato genérico** a main.

El Pipeline SDK:

- Lee el manifiesto `FUTURE_MACHINE.md` para saber qué slots existen
- Detecta qué está desincronizado comparando timestamps y deltas entre niveles
- Recorre la cadena en orden, parando si un nivel no cambió
- Delega a los agentes que el mod haya registrado en cada slot
- Ofrece handoffs al terminar

No define la cadena concreta (eso es del mod). Define el **protocolo de recorrido**.

### `@Portal` — la puerta de entrada

> Agente SDK existente: `.github/agents/portal.agent.md`

Se amplía para reconocer la machine cuando exista. Si el mod declara `FUTURE_MACHINE.md`, Portal puede presentar el ciclo completo y ofrecer los entrypoints declarados.

## 3. Relación entre dossiers

```
                    ┌─────────────┐
                    │  lore-db-sdk │  piezas + LORE_F + @Loreador
                    │  PS-01..05   │
                    └──────┬──────┘
                           │ LORE_F
                    ┌──────▼──────┐
                    │  corpus-sdk  │  feed → análisis → merge acumulativo
                    │  CS-01..04   │
                    └──────┬──────┘
                           │ corpus.md
                    ┌──────▼──────┐
                    │  grafo-sdk   │  lore-db + corpus → grafo de bifurcación
                    │  GS-01..04   │  (datos + analítica → hiperlínea temporal)
                    └──────┬──────┘
                           │ grafo
              ┌────────────┼────────────┐
              │                         │
       ┌──────▼──────┐          ┌──────▼──────┐
       │ universos-sdk│          │  cortos-sdk  │
       │ rellenar vars│          │ producciones │
       │ + elegir init│          │ literarias   │
       │  US-01..03   │          │ COS-01..04   │
       └──────┬──────┘          └──────┘
              │ universo (spec)       ↑
              └───────────────────────┘
                                obra ← universo

                ┌─────────────────────┐
                │  future-machine-sdk  │  @Pipeline + entrypoints + manifest
                │  FS-01..06           │
                └─────────────────────┘
```

| Dossier | Branch | Relación |
|---------|--------|----------|
| `lore-db-sdk` | main | Upstream: piezas + LORE_F |
| `corpus-sdk` | main | Upstream: capa corpus acumulativa |
| `grafo-sdk` | main | Intermedio: grafo de bifurcación |
| `universos-sdk` | main | Downstream: concreción del grafo |
| `cortos-sdk` | main | Downstream: producción literaria |
| **future-machine-sdk** | **main** | **Orquestación + entrypoints + manifest** |
| `future-machine-legislativa` | mod/legislativa | Hereda este contrato e instancia con el caso Feo |

## 4. Anclas

| Artefacto | Ubicación | Estado |
|-----------|-----------|--------|
| Pipeline validado | `mod/agents/pipeline.agent.md` (mod/legislativa) | Operativo — evidencia de que funciona |
| FEAT-06 Pipeline Refresh | `DRAFTS2/FEAT-06_PIPELINE_REFRESH.md` (mod/legislativa) | Spec vinculante del refresh |
| Portal SDK | `.github/agents/portal.agent.md` | Operativo |
| Archivero SDK | `.github/agents/archivero.agent.md` | Operativo |
| Dramaturgo SDK | `.github/agents/dramaturgo.agent.md` | Operativo |
| Skill futures-engine | `.github/skills/futures-engine/SKILL.md` | Operativo — genérico |
| Dossier archivado | `sala/archivo/sprint-cristalizacion-v1/dossiers/future-machine-universo-1/` | Referencia histórica |

## 5. Restricciones

- `future-machine` **no duplica** los contratos de piezas, corpus, grafo, universos ni cortos — los compone
- `@Pipeline` SDK define el **protocolo de recorrido**, no la cadena concreta de agentes (eso es del mod)
- Los 3 prompts de entrypoint son **baseline overrideable**: el mod los sustituye con sus versiones ricas
- Debe convivir con la inicialización de `lore/` prevista en `lore-db-sdk`
- Tiene que servir tanto para mods simples como para mods con Portal, Pipeline y dashboard ricos

## 6. Propuesta

### 6.1. `@Pipeline` SDK genérico (FS-05)

Crear `.github/agents/pipeline.agent.md` — agente orquestador de refresh con:

- Lectura del manifiesto `FUTURE_MACHINE.md`
- Detección de desincronización entre slots
- Protocolo de recorrido genérico (upstream → downstream, parar si no hay delta)
- Sin handoffs concretos: el mod los inyecta
- Modos: `status`, `refresh`, `refresh --desde [nodo]`

### 6.2. Contrato de slots (FS-01)

Crear `.github/instructions/future-machine-schema.instructions.md` con:

- Slots de capas: `lore_db`, `corpus`, `grafo`, `universos`, `obras`
- Slots de agentes: `pipeline`, `portal`
- Slots de entrypoints: `start`, `status`, `refresh`
- Cada slot declara: ruta, agente propietario, dependencia, estado

### 6.3. Template de manifest (FS-02)

Crear `.github/templates/future-machine.template.md` instanciable como `{{LORE_DIR}}/FUTURE_MACHINE.md`.

### 6.4. 3 prompts de entrypoint base (FS-06)

- `.github/prompts/machine-start.prompt.md` — lee manifest → muestra big picture → ofrece siguiente paso
- `.github/prompts/machine-status.prompt.md` — lee manifest → muestra estado de cada slot
- `.github/prompts/machine-refresh.prompt.md` — delega a `@Pipeline` con el manifest precargado

### 6.5. Integración con Portal (FS-03)

Ampliar `.github/agents/portal.agent.md` para que detecte la machine si existe y la presente como ciclo completo.

### 6.6. Documentación de cierre (FS-04)

Actualizar `.github/copilot-instructions.md` con la machine como cierre compositivo del SDK.

## 7. Notas pendientes para dossiers hermanos

Estas notas se generaron durante el rediseño de la machine. Van dirigidas a cada dossier individual para que las absorba en su PLAN/RESPUESTAS cuando proceda.

### Para `lore-db-sdk`

> Formalizar la dualidad de stores: (a) piezas sueltas en disco con índice DRY, (b) LORE_F como primera composición factual de piezas — hilo temporal pasado→presente. Son dos modos de UI del Loreador, no dos agentes.

### Para `corpus-sdk`

> Documentar explícitamente el protocolo de acumulación del merge. El corpus no se regenera: se acumula por capas sucesivas. Cada merge suma delta aprobado sin reescribir lo anterior.

### Para `grafo-sdk`

> El grafo recibe dos fuentes: lore-db+LORE_F (datos factuales) y corpus (analítica). Ambas cubren pasado→presente; el grafo extiende la hiperlínea hacia futuros. Revisar el mecanismo de ponderación de plausibilidad estimada de los mundos (coordinar con equipo Retro y skill `futures-engine`).

### Para `universos-sdk`

> Reformular: un universo = rellenar variables + elegir inicializaciones sobre el grafo. El fichero resultante es la concreción del artefacto para un caso concreto. Es la spec que el agente literario consume.

### Para `cortos-sdk`

> Los cortos son producciones al uso en lenguaje natural. Son la salida final. No hay más transformación después.

## 8. Salida operativa

- Tracking: [BACKLOG.md](./BACKLOG.md)
- Decisiones del PO: [RESPUESTAS.md](./RESPUESTAS.md)
- Tasks: carpeta [tasks](./tasks)