# mod/legislativa — README

> Narrado por `@Pipeline`. Bienvenido a la fábrica.

---

## La visita

Vas a recorrer el taller entero. Cada parada es una etapa de producción. Te digo qué agente trabaja ahí, qué entra, qué sale, y dónde están los ficheros.

### Parada 1 — El almacén de piezas

```
DRAFTS2/LORE_*.md          ← las piezas viven aquí
DRAFTS2/LORE_INDEX.md      ← el índice las cataloga por tipo
```

Aquí llega el material crudo: piezas tipadas del lore. Cada una tiene un prefijo que dice qué es (P-personaje, S-social, N-noticia, T-fase, R-recurso). Hay una pieza especial, `LORE_F.md`, que es el hilo narrativo precompilado — no es una pieza más, es la destilación de todas.

Nadie toca las piezas. Son la fuente de verdad.

### Parada 2 — Control de calidad

```
mod/agents/puzzle.agent.md     ← el agente (pendiente de crear)
```

`@Puzzle` recibe las piezas y las valida contra el esquema del lore. ¿Tiene tipo? ¿Tiene fecha? ¿Se referencia correctamente? Si pasa, las empaqueta y se las pasa al siguiente. Si no pasa, las devuelve con un informe de errores.

**Entra:** piezas sueltas. **Sale:** pack verificado.

### Parada 3 — El archivo

```
mod/agents/archivero-lore.agent.md   ← el agente
DRAFTS2/CORPUS_PREVIEW.md           ← el corpus que genera
```

`@Archivero Lore` toma el pack verificado y lo pasa por `@Bartleby` (el analista del SDK base, que no juzga — solo extrae estructura). El resultado es el corpus acumulativo: un mapa de linajes, taxonomía, mecanismos retóricos, emergencias y ausencias.

Invocas esta etapa con `/lore-ingest`.

**Entra:** pack verificado. **Sale:** corpus actualizado.

### Parada 4 — La mesa de cartografía

```
mod/agents/grafista.agent.md       ← el agente
DRAFTS2/grafo/                     ← el grafo JSON (pendiente de migrar)
DRAFTS2/LORE_F-02_UNIVERSO.md      ← la versión Markdown actual
```

`@Grafista` lee el corpus + el hilo narrativo y detecta puntos de bifurcación. Los estructura en un grafo: nodos (hechos o huecos), arcos (causalidad o tensión), ramas (futuros posibles). Hoy el grafo está en Markdown; la migración a JSON es uno de los dossiers activos.

**Entra:** corpus + LORE_F. **Sale:** grafo de bifurcación.

### Parada 5 — El laboratorio de futuros

```
mod/agents/demiurgo.agent.md       ← el agente (pendiente de crear)
DRAFTS2/universo/                  ← los universos instanciados
mod/universos/                     ← vista canónica
```

`@Demiurgo` toma el grafo completo y, en conversación con el usuario, elige una rama y la desarrolla en un universo: un escenario de futuro con tratamiento literario. Cada universo es ficción plausible basada en hechos reales.

**Entra:** grafo completo. **Sale:** universo instanciado.

### Parada 6 — La imprenta

```
mod/agents/dramaturgo.agent.md     ← el agente
DRAFTS2/LORE_F-02_CORTO-*.md      ← los cortos generados
```

`@Dramaturgo Cortos` toma un universo y genera una pieza literaria: un corto. Cada corto se sufija con el modelo que lo generó. Puedes pedir el mismo universo a distintos modelos y comparar.

Invocas esta etapa con `/dramaturgo-editar-universo`.

**Entra:** universo instanciado. **Sale:** pieza literaria.

### La cinta transportadora

```
mod/agents/pipeline.agent.md      ← yo
```

Eso soy yo, `@Pipeline`. Mi trabajo es que la cinta no se pare. Cuando alguien cambia una pieza, yo recorro la fábrica y actualizo lo que haga falta: corpus, grafo, universos afectados. Invócame con `/pipeline-refresh`.

---

## Comandos rápidos

| Comando | Qué hace |
|---------|----------|
| `/lore-ingest` | Ejecuta paradas 2→3 (validar + archivar) |
| `/dramaturgo-editar-universo` | Ejecuta parada 6 (generar corto) |
| `/pipeline-refresh` | Recorre toda la cinta y sincroniza |
| `/user-empieza-aqui` | Mapa visual del taller (big picture) |
| `/lore-status` | Dashboard con datos concretos del lore cargado |
| `/sala-aleph` | Activa al orquestador en sesión fría |
| `/sala-entrar` | Activa a un agente trabajador |

---

## La sala de coordinación

Cuando hay trabajo en paralelo (varios dossiers abiertos, varios agentes disponibles), se usa la sala.

### Cómo funciona

```
  ┌─────────────────────────────┐
  │  Ventana 1: Orquestador     │   /sala-aleph
  │  (Aleph)                    │   Revisa, asigna, cierra
  └──────────┬──────────────────┘
             │ usuario = puente
  ┌──────────▼──────────────────┐
  │  Ventana 2: Agente A        │   /sala-entrar
  │  Ventana 3: Agente B        │   /sala-entrar
  │  Ventana N: Agente N        │   /sala-entrar
  └─────────────────────────────┘
```

- **1 ventana** para el orquestador (`/sala-aleph`). Es el único que escribe en dossiers.
- **N ventanas** para agentes trabajadores (`/sala-entrar`). Hacen handshake, toman tarea, trabajan con checkpoints.
- El **usuario** es el puente entre ventanas. "Aleph, el agente X terminó, revisa." "Agente, Aleph dice que sigas."

El protocolo completo está en `DRAFTS2/sala/README.md`. El tablero de tareas en `DRAFTS2/sala/tablero.md`.

---

## Los dossiers

Un dossier es una carpeta autocontenida para un feature de cristalización. Tiene plan, backlog, decisiones del PO, y tasks delegables a agentes.

### Plantilla vacía

```
DRAFTS2/sala/plantilla-dossier/
├── PLAN.md
├── BACKLOG.md
├── RESPUESTAS.md
├── activacion.prompt.md
└── tasks/
    └── TASK-00_CONTEXTO_Y_PERSISTENCIA.md
```

Para crear un dossier nuevo: copia la plantilla a `DRAFTS2/cristalizacion-<nombre>/` y rellena. El protocolo completo está en `mod/skills/cristalizacion-feature/SKILL.md`.

### Regla de acceso

- **Agentes:** read-only sobre dossiers. Trabajan en su carpeta temporal de `sala/`.
- **Orquestador:** es el único que escribe en dossiers (copiar entregas, cerrar tasks, actualizar backlogs).
- **PO:** decide qué se aprueba y qué no. Sus decisiones se fijan en `RESPUESTAS_*.md`.

---

## Dónde está cada cosa

| Qué | Dónde |
|-----|-------|
| Agentes del mod | `mod/agents/` |
| Comandos del mod | `mod/prompts/` |
| Instrucciones del mod | `mod/instructions/` |
| Skills del mod | `mod/skills/` |
| Piezas del lore | `DRAFTS2/LORE_*.md` |
| Corpus | `DRAFTS2/CORPUS_PREVIEW.md` |
| Grafo | `DRAFTS2/grafo/` o `DRAFTS2/LORE_F-02_UNIVERSO.md` |
| Universos | `DRAFTS2/universo/` |
| Cortos | `DRAFTS2/LORE_F-02_CORTO-*.md` |
| Sala de coordinación | `DRAFTS2/sala/` |
| Dossiers activos | `DRAFTS2/cristalizacion-*/` y `DRAFTS2/finalizacion-*/` |
| SDK base (no tocar) | `.github/` |
| Big picture | `mod/instructions/onboarding-map.instructions.md` |
| Protocolo de dossiers | `mod/skills/cristalizacion-feature/SKILL.md` |
