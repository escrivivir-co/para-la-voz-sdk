---
name: engine-plan
description: Skill portable para simulación, diagnóstico e inspección del pipeline E2E de la future-machine. Proporciona el protocolo de consola de simulación (modos log/log-std), el contrato de existencia de agentes, el protocolo de run/inspect/gaps, el formato de log estandarizado, y el protocolo de generación de patches cross-branch. Se activa cuando se usa /engine-plan, cuando un agente necesita diagnosticar integración entre capas del pipeline, o cuando se simula un refresh de la cadena completa.
argument-hint: "[vacío = big picture | lore-db | corpus | grafo | universos | cortos | pipeline | portal | dossiers | deps | log | log-std]"
user-invocable: false
---

# Skill: engine-plan — Protocolo de simulación y diagnóstico del pipeline E2E

Esta skill define la **base de conocimiento** del pipeline de la future-machine: cómo simular, diagnosticar, inspeccionar y parchear la cadena de agentes de principio a fin. El prompt `/engine-plan` consume esta skill para saber *cómo* hacer las cosas; el prompt define *qué* se activa con cada argumento.

## Cuándo activar esta skill

- Cuando se usa `/engine-plan` en cualquier modo
- Cuando un agente necesita diagnosticar integración entre capas del pipeline
- Cuando se simula un refresh de la cadena completa (`run`)
- Cuando se inspecciona un nodo individual (`inspect`)
- Cuando se buscan huecos de spec o artefactos faltantes (`gaps`)
- Cuando se genera un patch cross-branch para un artefacto del pipeline
- Cuando se necesita verificar el estado de existencia de agentes (`status`)

---

## §1. El pipeline — modelo canónico de 6+2 capas

La future-machine es una cadena de 6 capas de datos + 2 agentes transversales:

```
  PIEZAS (ficheros en disco)
    │
    ▼
  ┌─────────────┐
  │ @Loreador   │  Capa 1: lore-db
  │ INDEX + F   │  Inventario DRY + hilo factual
  └──────┬──────┘
         │ LORE_F
    ┌────┴────┐
    ▼         ▼
┌────────┐ ┌────────┐
│Bartleby│ │ LORE_F │  Capa 2-3: análisis + corpus
│análisis│ │ datos  │
└───┬────┘ └───┬────┘
    │          │
    ▼          │
┌────────┐    │
│Archivero│◀──┘  (doble fuente)
│ merge   │
└───┬────┘
    │
    ▼
  corpus/corpus.md
    │
    ├─────────────────┐
    ▼                 ▼
┌────────┐      ┌────────┐
│Grafista│◀─F──│ corpus │  Capa 4: grafo de bifurcación
│bifurcar│      │analítica│
└───┬────┘      └────────┘
    │
    ▼
┌────────┐
│Demiurgo│  Capa 5: universos (variables + inicializaciones)
│instanciar│
└───┬────┘
    │
    ▼
┌──────────┐
│Dramaturgo│  Capa 6: obras (lenguaje natural)
│ crear    │
└──────────┘

  ─── Transversales ──────────────
  @Pipeline      : orquesta refresh
  @Portal        : puerta de entrada
  @Cristalizador : propone infraestructura
```

### Contrato de cada capa

| Capa | Agente | Input canónico | Output canónico | Dossier SDK |
|------|--------|----------------|-----------------|-------------|
| 1 | `@Loreador` | Piezas en disco (ficheros tipados) | `INDEX.md` + `LORE_F.md` | `lore-db-sdk` |
| 2 | `@Bartleby` | `LORE_F.md` o doc vía `/feed` | `.analisis.md` | — (core) |
| 3 | `@Archivero` | Análisis + `corpus.md` actual | `corpus.md` actualizado (merge acumulativo) | `corpus-sdk` |
| 4 | `@Grafista` | `LORE_F` (datos) + `corpus.md` (analítica) | `grafo/*.json` (nodos, arcos, huecos) | `grafo-sdk` |
| 5 | `@Demiurgo` | Grafo de bifurcación | `universo/*.md` (spec concreta) | `universos-sdk` |
| 6 | `@Dramaturgo` | Universo (spec) | `cortos/*.md` (producción literaria) | `cortos-sdk` |

### Principio de doble fuente

El `@Grafista` (capa 4) recibe **dos fuentes complementarias** que cubren pasado→presente:

| Fuente | Tipo | Qué aporta |
|--------|------|------------|
| `LORE_F` (vía `@Loreador`) | Datos factuales | Variables de estado, hechos, cronología |
| `corpus.md` (vía `@Archivero`) | Analítica | Taxonomía, mecanismos, tensiones, ausencias |

El grafo extiende la **hiperlínea temporal** desde presente hacia futuros plausibles. Cada nodo de bifurcación marca un punto donde el sistema puede divergir.

### Principio de acumulación del corpus

El corpus no se regenera: se **acumula por capas sucesivas**. Cada merge añade delta aprobado sin reescribir lo anterior. El corpus es el mapa analítico acumulativo.

### Principio de concreción del universo

Un universo = **rellenar variables** + **elegir inicializaciones** sobre el grafo. El fichero resultante es la spec concreta que el agente literario consume. No es ficción: es el contrato del corto.

---

## §2. Contrato de existencia de agentes

Todo agente del pipeline puede estar en uno de tres estados de existencia:

| Estado | Significado | Criterio de verificación |
|--------|-------------|--------------------------|
| `READY` | Agente operativo | Existe fichero `.agent.md` (en main o mod) |
| `BUILD` | En construcción | Existe dossier en `sala/dossiers/` con PLAN/BACKLOG pero NO `.agent.md` |
| `MISS` | No existe | Ni `.agent.md` ni dossier |

### Protocolo de verificación

Para determinar el estado de un agente:

1. **Buscar `.agent.md`** en dos ubicaciones (en este orden):
   - `mod/agents/{nombre}.agent.md` (override del mod)
   - `.github/agents/{nombre}.agent.md` (SDK base)
   - Si existe en alguna → estado `READY`

2. **Buscar dossier SDK** en `sala/dossiers/`:
   - Buscar carpeta cuyo nombre incluya el dominio del agente
   - Verificar que contenga `PLAN.md` y `BACKLOG.md`
   - Si existe dossier pero no `.agent.md` → estado `BUILD`

3. **Sin artefactos** → estado `MISS`

### Mapa canónico de agentes del pipeline

| Agente | Rol en pipeline | Nombre canónico en main | Dossier SDK esperado |
|--------|-----------------|------------------------|----------------------|
| `@Loreador` | Gestor lore-db | `loreador` | `lore-db-sdk` |
| `@Bartleby` | Analista | `bartleby` | — (core) |
| `@Archivero` | Gestor corpus | `archivero` | `corpus-sdk` |
| `@Grafista` | Constructor de grafo | `grafista` | `grafo-sdk` |
| `@Demiurgo` | Instanciador de universos | `demiurgo` | `universos-sdk` |
| `@Dramaturgo` | Creador de obras | `dramaturgo` | `cortos-sdk` |
| `@Pipeline` | Orquestador de refresh | `pipeline` | `future-machine-sdk` |
| `@Portal` | Puerta de entrada | `portal` | — (core) |
| `@Cristalizador` | Meta: infraestructura | `cristalizador` | — (core) |

### Overrides de mod

Un mod puede definir agentes propios que **sustituyen o especializan** los del SDK:
- Override: `mod/agents/{mismo-nombre}.agent.md` → reemplaza al agente SDK para ese mod
- Extensión: `mod/agents/{nombre-nuevo}.agent.md` → agente adicional que no existe en main
- Herencia: si el mod no define override, hereda el agente de `.github/agents/` tal cual

El mapa de existencia debe reflejar ambas capas. Si un agente tiene override en mod, se reporta como `READY (mod override)`.

---

## §3. Formato de log estandarizado

### Formato de línea

Cada mensaje del log sigue este formato:

```
[HH:MM:SS] @NombreAgente  │ STATUS  │ mensaje
```

### Estados de línea

| Status | Significado | Cuándo emitir |
|--------|-------------|---------------|
| `BOOT` | Arranque de la machine | Solo en secuencia de boot |
| `READY` | Agente conectado y operativo | Boot: tiene `.agent.md` |
| `BUILD` | Agente en construcción | Boot: tiene dossier, no `.agent.md` |
| `MISS` | Agente no existe | Boot: ni agente ni dossier |
| `RUN` | Ejecutando un paso | Durante `run` o comando activo |
| `OK` | Paso completado con éxito | Fin de paso sin errores |
| `WARN` | Completado con advertencias | Spec incompleta, dato parcial |
| `WAIT` | Esperando input | Del usuario o de otro agente |
| `ERR` | Error en paso | Falta spec, falta upstream, contradicción |
| `SPEC?` | Falta especificación | El agente no sabe qué hacer en este paso |
| `DATA` | Dato informativo | Tablas, estadísticas, snapshots |
| `EXIT` | Cierre de sesión | Solo al recibir `exit` |

### Bloques especiales

Para secciones de datos extensas, usar el separador de caja:

```
[HH:MM:SS] @Agente │ DATA  │ ═══════════════════════════════════════════
[HH:MM:SS] @Agente │ DATA  │ TÍTULO DEL BLOQUE
[HH:MM:SS] @Agente │ DATA  │ ═══════════════════════════════════════════
```

Para tablas dentro del log:

```
[HH:MM:SS] @Agente │ DATA  │ ┌──────┬───────┬──────┐
[HH:MM:SS] @Agente │ DATA  │ │ col1 │ col2  │ col3 │
[HH:MM:SS] @Agente │ DATA  │ └──────┴───────┴──────┘
```

### Separador entre comandos

Cada comando del usuario produce un bloque separado por `---` en el log.

### Cabecera de fichero log-std

```markdown
# engine-plan log — {YYYY-MM-DD}

> Sesión de simulación de la future-machine.
> Runtime: {modelo exacto}

---
```

---

## §4. Protocolo de boot

La secuencia de arranque es determinista. El agente que ejecuta la simulación:

1. **Lee el mapa de existencia** de agentes (§2) verificando en disco
2. **Lee los BACKLOGs** de todos los dossiers para conteos reales de tasks
3. **Emite la secuencia de boot** con todos los slots

### Formato de boot

```
[00:00:00] @Pipeline     │ BOOT  │ future-machine v0.1-dev starting...
[00:00:00] @Pipeline     │ BOOT  │ runtime: {modelo} — {modo} mode
[00:00:00] @Pipeline     │ BOOT  │ scanning slots...
[00:00:0X] @{Agente}     │ {EST} │ slot_{nombre}: {detalle de estado}
...
[00:00:0X] @Pipeline     │ BOOT  │ ═══════════════════════════════════════════
[00:00:0X] @Pipeline     │ BOOT  │ {N} READY, {M} BUILD, {K} MISS
[00:00:0X] @Pipeline     │ BOOT  │ {total} tasks total: {cerradas} cerradas, {libres} libre
[00:00:0X] @Pipeline     │ BOOT  │ critical path: {ruta crítica}
[00:00:0X] @Pipeline     │ BOOT  │ Machine {partially operational | fully operational | not operational}.
[00:00:0X] @Pipeline     │ WAIT  │ ready for commands
```

### Estado operativo de la machine

| Condición | Estado |
|-----------|--------|
| Todos los slots `READY` | `fully operational` |
| Al menos un slot `BUILD` o `MISS` | `partially operational` |
| Slots 1-3 todos `MISS` | `not operational` (no hay base de datos) |

---

## §5. Protocolo de `run` — refresh simulado

Cuando el usuario ejecuta `run` (o `run --desde {nodo}`):

### Recorrido

1. `@Pipeline` recorre la cadena **en orden**: Loreador → Bartleby → Archivero → Grafista → Demiurgo → Dramaturgo
2. Si se especifica `--desde {nodo}`, salta directamente a ese nodo y continúa downstream

### Comportamiento por estado del agente

| Estado | Qué hace el agente simulado |
|--------|----------------------------|
| `READY` | Lee artefactos reales de entrada. Describe qué haría con ellos. Cita ficheros concretos. Emite `OK` o `WARN`. |
| `BUILD` | Reporta qué tiene (dossier, spec) y qué le falta. Emite `SPEC?` cuando el paso no está documentado en el dossier. |
| `MISS` | Emite `ERR` con mensaje de qué task/dossier lo resolvería. Salta al siguiente. |

### Integridad de datos

- **Antes de emitir un log line**, el agente simulado **lee disco**. Usa `read_file`, `grep_search`, `list_dir` para verificar artefactos.
- Si no puede verificar en tiempo razonable, emite `[PENDING: buscando spec...]` en lugar de inventar.
- Los datos de un mod activo (e.g. `DRAFTS2/` en mod/legislativa) son **mock data válido** para la simulación.
- Si un fichero no existe, el agente dice que no existe. Sin excepciones.

### Resumen post-run

Al terminar el recorrido:

```
[HH:MM:SS] @Pipeline     │ OK    │ refresh done. {N}/{total} nodos visited. {E} ERR, {W} WARN.
```

### loadMOCK — cargar datos de un mod como mock

El comando `loadMOCK("{nombre_mod}")` permite cargar datos reales de una rama mod como datos de trabajo. El protocolo:

1. Verificar que la rama existe (local o remota)
2. Leer artefactos clave desde la rama vía `git show {rama}:{ruta}`
3. Mapear los datos del mod a los slots canónicos del pipeline
4. Emitir `DATA` con el inventario completo de lo cargado
5. Los datos mock persisten durante toda la sesión de simulación

---

## §6. Protocolo de `inspect` — deep-dive en un nodo

Cuando el usuario ejecuta `inspect {agente}`:

### Qué muestra

1. **Contrato del agente**: lee el `.agent.md` (o reporta su ausencia)
2. **I/O declaration**: input canónico y output canónico según la tabla de capas
3. **Estado de existencia**: `READY`/`BUILD`/`MISS` con evidencia
4. **Dossier asociado**: si existe, lee `BACKLOG.md` y reporta tasks libres/cerradas
5. **Upstream**: qué agentes le alimentan y si sus outputs existen
6. **Downstream**: qué agentes consumen su output y si están esperando
7. **Artefactos en disco**: lista de ficheros reales asociados a este nodo

### Formato de salida

```
[HH:MM:SS] @{Agente}     │ RUN   │ inspect requested
[HH:MM:SS] @{Agente}     │ DATA  │ ═══════════════════════════════════════════
[HH:MM:SS] @{Agente}     │ DATA  │ INSPECT: @{Agente}
[HH:MM:SS] @{Agente}     │ DATA  │ ═══════════════════════════════════════════
[HH:MM:SS] @{Agente}     │ DATA  │
[HH:MM:SS] @{Agente}     │ DATA  │ Estado: {READY|BUILD|MISS}
[HH:MM:SS] @{Agente}     │ DATA  │ Contrato: {ruta .agent.md o "no existe"}
[HH:MM:SS] @{Agente}     │ DATA  │ Input: {descripción + rutas}
[HH:MM:SS] @{Agente}     │ DATA  │ Output: {descripción + rutas}
[HH:MM:SS] @{Agente}     │ DATA  │ Upstream: {agente → estado}
[HH:MM:SS] @{Agente}     │ DATA  │ Downstream: {agente → estado}
[HH:MM:SS] @{Agente}     │ DATA  │ Dossier: {ruta o "—"}
[HH:MM:SS] @{Agente}     │ DATA  │ Tasks: {N} libre, {M} cerrada, {K} total
[HH:MM:SS] @{Agente}     │ DATA  │ Artefactos: {lista de ficheros}
```

---

## §7. Protocolo de `gaps` — huecos del pipeline

El comando `gaps` recorre toda la cadena y lista:

### Tipos de gap

| Tipo | Significado | Severidad |
|------|-------------|-----------|
| `SPEC?` | El agente no tiene spec para un paso documentado | Alta |
| `ERR` | Falta artefacto upstream o contradicción | Crítica |
| `ORPHAN-OUTPUT` | Un output que ningún agente downstream consume | Media |
| `ORPHAN-INPUT` | Un input que ningún agente upstream produce | Alta |
| `STALE` | Artefacto existe pero es más viejo que su fuente | Media |
| `SCHEMA-DRIFT` | El schema del output no coincide con el input esperado downstream | Alta |

### Formato de salida

```
[HH:MM:SS] @Pipeline     │ RUN   │ gap analysis...
[HH:MM:SS] @Pipeline     │ DATA  │
[HH:MM:SS] @Pipeline     │ DATA  │ GAPS ENCONTRADOS:
[HH:MM:SS] @Pipeline     │ DATA  │
[HH:MM:SS] @Pipeline     │ DATA  │ {N}. [{tipo}] @{Agente}: {descripción}
[HH:MM:SS] @Pipeline     │ DATA  │    → fix: {qué task/dossier/agente lo resuelve}
...
[HH:MM:SS] @Pipeline     │ OK    │ {N} gaps found. {C} critical, {H} high, {M} medium.
```

### Protocolo de fix sugerido

Para cada gap, el agente sugiere la acción correctiva:
- Si el fix corresponde a una task existente en un dossier → cita la task
- Si no existe task → propone abrirla y dice en qué dossier iría
- Si el gap es de schema → describe qué campos faltan o sobran

---

## §8. Protocolo de `data` — datos reales de un nodo

El comando `data {nodo}` muestra los **datos reales** que el nodo tiene en disco:

1. Identifica la capa del nodo
2. Lee los ficheros de datos asociados (e.g. `DRAFTS2/LORE_F.md` para el Loreador, `corpus/corpus.md` para Archivero)
3. Emite un snapshot con:
   - Nombre del fichero y líneas
   - Conteos relevantes (piezas, marcas, nodos, etc.)
   - Cobertura: qué porcentaje del input esperado está cubierto

Si se cargó un mock (`loadMOCK`), usa esos datos. Si no, usa los datos de main.

---

## §9. Protocolo de `spec` — especificación de un nodo

El comando `spec {nodo}` muestra la **especificación** del nodo:

1. Lee el task brief del dossier asociado (si existe)
2. Lee las secciones relevantes del PLAN.md del dossier
3. Lee las RESPUESTAS.md para decisiones del PO que afectan al nodo
4. Emite un resumen de:
   - Qué debe hacer el agente según la spec
   - Qué restricciones tiene
   - Qué salida se espera
   - Qué decisiones del PO aplican

Si no hay spec documentada → emite `SPEC?` con sugerencia de qué documentar.

---

## §10. Protocolo de `docs` — generación de documentación

El comando `docs {nodo}` genera un **borrador de documentación** para un nodo:

1. Lee todo lo que existe del nodo (agent.md, dossier, artefactos, datos)
2. Genera un borrador de documentación tipo README.md que cubre:
   - Qué es el nodo
   - Cómo se usa
   - Qué input espera y qué output produce
   - Estado actual
   - Dependencias upstream/downstream
3. El borrador es sugerencia; no se escribe a disco sin aprobación

---

## §11. Protocolo de generación de patches cross-branch

Cuando la simulación detecta que un artefacto necesita actualización en una rama diferente a la actual (típicamente: trabajar en main pero parchear un fichero de mod/legislativa):

### Reglas del patch

1. **No se puede escribir directamente** en una rama diferente desde la simulación
2. El patch se genera como fichero en `tmp/` con instrucciones de aplicación
3. El patch es **aplicable manualmente**: contiene las instrucciones git exactas

### Formato del patch

```markdown
# Patch — {nombre descriptivo}

> **Generado:** {fecha}
> **Runtime:** {modelo}
> **Rama origen:** {rama actual}
> **Rama destino:** {rama del artefacto}

## Cambios propuestos

### INSERT-{N} — {descripción}
- **Posición:** DESPUÉS de {contexto}, ANTES de {contexto}
- **Contenido:** {nuevo contenido}

### REPLACE-{N} — {descripción}
- **Bloque original:** {contenido actual}
- **Bloque nuevo:** {contenido nuevo}

## Instrucciones de aplicación

```bash
git checkout {rama destino}
# [aplicar cambios]
git add {fichero}
git commit -m "{mensaje}"
git checkout {rama origen}
```
```

---

## §12. Grafo de dependencias cross-dossier

Los dossiers del pipeline tienen dependencias reales que determinan la ruta crítica:

```
lore-db-sdk (PS-*)                      ← base de todo
    │
    ├──▶ corpus-sdk (CS-*)              ← PS-01 desbloquea CS-01
    │        │
    │        ├──▶ grafo-sdk (GS-*)      ← CS-01 desbloquea GS-01
    │        │        │
    │        │        └──▶ universos-sdk (US-*)  ← GS-01 desbloquea US-01
    │        │                  │
    │        │                  └──▶ cortos-sdk (COS-*) ← US-01 desbloquea COS-01
    │        │
    └────────┴──────────────────▶ future-machine-sdk (FS-*)
```

**Ruta crítica:** `PS-01 → CS-01 → GS-01 → US-01 → COS-01 → FS-01 → FS-05 → FS-06 → FS-04`

---

## §13. Contrato de interacción con `@Pipeline` real

Cuando `@Pipeline` exista como `.agent.md` operativo (FS-05 cerrada), la relación con este skill cambia:

| Aspecto | Hoy (simulación) | Con @Pipeline real |
|---------|-------------------|--------------------|
| Quién recorre la cadena | El skill simula | `@Pipeline` ejecuta, el skill documenta |
| Formato de log | Lo define este skill | `@Pipeline` hereda el formato de este skill |
| Detección de deltas | Comparación de timestamps simulada | `@Pipeline` compara realmente |
| Generación de patches | El skill propone | `@Pipeline` puede ejecutar con aprobación |
| Boot sequence | Simulada | `@Pipeline` la ejecuta como self-test |

### Protocolo de transición

1. Cuando FS-05 se cierre, `@Pipeline` leerá este skill como referencia de formato
2. `@Pipeline` adoptará el formato de log de §3 como su output estándar
3. Los comandos de consola (`run`, `inspect`, `gaps`) se convierten en los modos de `@Pipeline`
4. El skill evoluciona de "protocolo de simulación" a "protocolo de operación"

---

## §14. Reglas inquebrantables

1. **No inventar datos.** Si un fichero no existe, decir que no existe. Si un dossier no especifica un comportamiento, emitir `SPEC?`.
2. **Leer antes de hablar.** Si el agente necesita citar un artefacto, leerlo realmente del disco.
3. **El usuario manda.** Cualquier texto que no sea un comando se interpreta como pregunta sobre la arquitectura. El agente responde **dentro del formato log**, citando fuentes.
4. **Salir limpiamente.** Al recibir `exit`, el agente emite `[SHUTDOWN]` y cierra la sesión.
5. **Un solo fichero por sesión.** En modo `log-std`, toda la sesión escribe en el mismo fichero `tmp/engine-log-{timestamp}.md`.
6. **Simulación ≠ alucinación.** Cada dato que un agente "emite" en la simulación tiene respaldo en disco o se marca explícitamente como gap.

---

## §15. Referencia rápida de comandos

| Comando | Sección | Acción |
|---------|---------|--------|
| `help` | — | Lista de comandos |
| `status` | §4 | Estado de todos los slots |
| `run` | §5 | Refresh completo simulado |
| `run --desde {nodo}` | §5 | Refresh desde un nodo |
| `inspect {agente}` | §6 | Deep-dive en un nodo |
| `data {nodo}` | §8 | Datos reales del nodo |
| `spec {nodo}` | §9 | Especificación del nodo |
| `gaps` | §7 | Huecos del pipeline |
| `docs {nodo}` | §10 | Borrador de documentación |
| `loadMOCK("{mod}")` | §5 | Cargar datos de un mod |
| `exit` | §14 | Cerrar sesión |

---

## Backlog especulativo del skill

Este skill nace como protocolo de simulación. Las siguientes capacidades forman el backlog especulativo de lo que podría llegar a ser:

### Tier 1 — Extensiones naturales del protocolo actual

- **`diff {nodo}`**: comparar el estado actual de un nodo con su último estado conocido (timestamp + hash)
- **`history {nodo}`**: timeline de cambios de un nodo (git log filtrado)
- **`validate {nodo}`**: verificar que el output de un nodo cumple el schema esperado por su downstream
- **`trace {marca}`**: seguir una marca (e.g. `[P-01]`) a través de toda la cadena y reportar dónde aparece y dónde se pierde
- **`coverage`**: porcentaje de cobertura de marcas a lo largo de la cadena (INDEX → LORE_F → corpus → grafo)
- **`plan {nodo}`**: generar un plan de trabajo para poner un nodo en estado READY

### Tier 2 — Integración con la sala de coordinación

- **`task-suggest`**: dado el estado de gaps, sugerir las próximas tasks a abrir en los dossiers correspondientes
- **`sprint-scope`**: proponer el alcance de un sprint basado en la ruta crítica y los gaps actuales
- **`dossier-sync`**: verificar que el estado de los dossiers en disco coincide con lo que la simulación espera

### Tier 3 — Machine real

- **`@Pipeline` como agente real**: transición del skill de simulación a protocolo de operación
- **Hooks PostToolUse**: validar automáticamente el output de cada agente contra su schema
- **Hooks SessionStart**: ejecutar `status` al iniciar sesión para que el agente tenga contexto del pipeline
- **MCP server del pipeline**: exponer el estado de la machine como herramienta MCP consultable por cualquier agente
- **Plugin de pipeline**: empaquetar agentes + skills + hooks + MCP como plugin distribuible

### Tier 4 — Observabilidad y métricas

- **Dashboard persistente**: un `MACHINE_STATUS.md` auto-generado que refleje el estado actual
- **Métricas de cadena**: tiempo estimado de refresh, cobertura de marcas por capa, drift de schema
- **Alertas de stale**: detectar artefactos que llevan N días sin actualización
- **Diff cross-branch visual**: generar un diff visual entre main y mod para un nodo específico

### Tier 5 — Inteligencia sobre el pipeline

- **Detección de patrones**: identificar patrones recurrentes en los logs de sesión (e.g. "siempre falla en capa 4")
- **Sugerencia de refactor**: proponer cambios en la arquitectura basados en los gaps recurrentes
- **Simulación de futuros del pipeline**: usar el skill `futures-engine` sobre el propio pipeline para bifurcar escenarios de desarrollo
- **Auto-priorización**: dado el estado de gaps y la ruta crítica, priorizar tasks automáticamente

---

## Dónde vive el material específico del lore

Los datos reales del pipeline (piezas, corpus, grafo, universos, cortos) viven en el mod activo — no en este SDK. El mod los gestiona. Este skill define el protocolo; el prompt `/engine-plan` lo ejecuta; los datos viven en el mod.
