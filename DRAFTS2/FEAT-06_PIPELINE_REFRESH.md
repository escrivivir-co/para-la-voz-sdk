# FEAT-06 — Cristalización: `@Pipeline` + `/refresh`

> **Origen:** Sprint universo-1 v2. El refresh manual de la cadena de derivados fue el cuello de botella real.
> **Propuesta del Cristalizador:** Agentizar el pipeline refresh como artefacto invocable.
> **Estado:** Completado — implementación por `Claude Sonnet 4.6`.

---

## Artefactos a crear

| Artefacto | Ruta | Tipo |
|-----------|------|------|
| Agente orquestador | `mod/agents/pipeline.agent.md` | `.agent.md` |
| Slash command de entrada | `mod/prompts/refresh.prompt.md` | `.prompt.md` |
| Retorno desde Dramaturgo | `mod/agents/dramaturgo.agent.md` | ampliación `.agent.md` |

---

## Capacidad nueva que activa

**Handoffs bidireccionales** — al terminar el refresh, botones para saltar directamente a `@Dramaturgo Cortos` o `@Archivero`; y desde `@Dramaturgo Cortos`, un retorno directo a `@Pipeline` para ejecutar refresh cuando el grafo esté desincronizado. No se usan en ningún artefacto de `mod/` todavía. Convierte el pipeline de "serie de invocaciones manuales" en workflow guiado con checkpoints visibles.

---

## Motivación desde el corpus

El sprint de universo-1 v2 demostró que:
1. El grafo de dependencias `PIEZAS → {CORPUS_PREVIEW ∥ LORE_F} → ARTEFACTO → UNIVERSO → rama` existe de facto pero no estaba codificado.
2. CORPUS_PREVIEW y LORE_F son **hermanos** (ambos derivan de piezas), no padre-hijo. Se pueden refrescar en paralelo.
3. El ARTEFACTO es el primer nodo que necesita ambos inputs.
4. Cada vez que se tocaron piezas, hubo que refrescar manualmente toda la cadena antes de generar obra.
5. El skill `futures-engine` ya trata Fase 1 (corpus) y Fase 2 (hilo) como inputs separados, pero no documenta este grafo.

Con 51 piezas y creciendo, el refresh manual es el cuello de botella real del pipeline.

---

## El grafo de dependencias

```
                     PIEZAS (DRAFTS2/LORE_*.md)
                    /                           \
                   /                             \
      (documental-analysis)              (composición narrativa)
                 /                                 \
                ▼                                   ▼
   DRAFTS2/CORPUS_PREVIEW.md              DRAFTS2/LORE_F.md
   "mapa estructural"                     "hilo temporal"
                \                                 /
                 \                               /
                  ▼                             ▼
          DRAFTS2/LORE_F-02_ARTEFACTO.md
          "spec de construcción"
                          │
                          ▼
          DRAFTS2/LORE_F-02_UNIVERSO.md
          "grafo de futuros"
                          │
                          ▼
          DRAFTS2/universo/*.md
          "ramas expandidas"
```

**Regla clave:** CORPUS_PREVIEW y LORE_F son hermanos. Se refrescan en paralelo. El ARTEFACTO es el join.

---

## Protocolo de refresh — 6 pasos

### Paso 0: Inventario

Lee el estado actual de todos los nodos:
1. Lista las piezas en `DRAFTS2/` (LORE_S-\*, LORE_N-\*, LORE_T-\*, LORE_R-\*, LORE_P-\*)
2. Lee las primeras 30 líneas de cada nodo derivado para capturar metadatos
3. Lee `mod/instructions/legislativa-universo.instructions.md` para el estado declarado

Presenta al usuario:

```
## Estado actual del pipeline

| Nodo | Última actualización | Piezas que incorpora |
|------|---------------------|----------------------|
| CORPUS_PREVIEW | [fecha/piezas] | [lista] |
| LORE_F | [fecha/piezas] | [lista] |
| ARTEFACTO | [fecha] | basado en CORPUS_PREVIEW de [X] |
| UNIVERSO | [fecha] | basado en ARTEFACTO de [X] |
| universo-1 | [fecha] | basado en UNIVERSO de [X] |

Piezas no incorporadas: [lista]
```

Si no hay piezas sin incorporar: **"Pipeline al día. No hay piezas pendientes de integrar."** → ofrece handoffs. No continúa.

---

### Paso 1: Refresh de hermanos (CORPUS_PREVIEW ∥ LORE_F)

#### 1a. CORPUS_PREVIEW.md

Carga el skill `documental-analysis`. Lee todas las piezas. Regenera el mapa estructural. Presenta el **delta**:

```
## Delta CORPUS_PREVIEW

### Añadido
- [categoría/término nuevo]: procedente de [pieza]

### Modificado
- [categoría existente]: [qué cambió] ← [pieza]

### Sin cambios
- [categorías estables]
```

Si delta vacío: **"CORPUS_PREVIEW sin cambios."**

#### 1b. LORE_F.md

Lee las piezas con contenido temporal/narrativo. Verifica el hilo. Presenta el **delta**:

```
## Delta LORE_F

### Eventos añadidos al hilo
- [evento]: procedente de [pieza], posición temporal [T=X]

### Correcciones
- [dato corregido]: [antes] → [ahora] ← [pieza]

### Sin cambios
- [secciones estables]
```

Si delta vacío: **"LORE_F sin cambios."**

---

### Paso 2: Refresh del ARTEFACTO

**Condición:** Solo si Paso 1a O Paso 1b produjeron cambios.

Lee CORPUS_PREVIEW + LORE_F actualizados. Re-deriva las secciones dependientes del artefacto:
- Piezas activas para la bifurcación
- Nodos de bifurcación — ¿el mapa actualizado revela nodos nuevos?
- Escenarios considerados — ¿siguen vigentes?
- Forma elegida — ¿la tabla de movimientos necesita ajustes?

Presenta el **delta**:

```
## Delta ARTEFACTO

### Huecos resueltos
- H[N]: resuelto por [pieza] — [dato]

### Huecos nuevos
- H[N]: detectado — [descripción]

### Reglas de construcción
- [cambios o adiciones]

### Datos duros añadidos
- [dato]: procedente de [pieza]
```

Si solo cambian datos duros pero no la estructura: marcar **"cambio menor — downstream puede no necesitar refresh"**.

---

### Paso 3: Refresh del UNIVERSO

**Condición:** Solo si Paso 2 produjo cambios estructurales (huecos resueltos, reglas nuevas, o nodos de bifurcación alterados).

Carga el skill `futures-engine`. Lee el ARTEFACTO actualizado. Re-deriva el grafo. Presenta el **delta**:

```
## Delta UNIVERSO

### Ramas afectadas
- R[N]: [qué cambió]

### Nodos nuevos
- [nodo]: [descripción] — habilitado por [dato/hueco resuelto]

### Nodos invalidados
- [nodo]: [ya no plausible porque...]
```

---

### Paso 4: Refresh de ramas expandidas

**Condición:** Solo si Paso 3 produjo cambios en ramas que tienen expansión en `DRAFTS2/universo/`.

Para cada rama afectada:
1. Lee la rama expandida actual
2. Identifica qué nodos necesitan actualización
3. Actualiza manteniendo el trabajo previo de diseño
4. Presenta delta de la rama

---

### Paso 5: Resumen y handoff

```
## Refresh completado

| Paso | Nodo | Estado |
|------|------|--------|
| 1a | CORPUS_PREVIEW | ✅ Actualizado (N cambios) / ⏭️ Sin cambios |
| 1b | LORE_F | ✅ Actualizado (N cambios) / ⏭️ Sin cambios |
| 2 | ARTEFACTO | ✅ Actualizado / ⏭️ Saltado |
| 3 | UNIVERSO | ✅ Actualizado / ⏭️ Saltado |
| 4 | universo-1 | ✅ Actualizado / ⏭️ Saltado |

Pipeline listo para generación.
```

Actualiza `mod/instructions/legislativa-universo.instructions.md` con el nuevo conteo de piezas si cambió.

Handoffs automáticos:
- **[Generar corto desde universo-1]** → `@Dramaturgo Cortos`
- **[Ver estado del corpus]** → `@Archivero`

---

## Integración con Dramaturgo Cortos

`mod/agents/dramaturgo.agent.md` debe añadir un handoff explícito:

- **[Ejecutar refresh del pipeline]** → `@Pipeline`

Regla operativa asociada:
- Si el dramaturgo detecta desincronización entre `CORPUS_PREVIEW`, `LORE_F`, `ARTEFACTO`, `UNIVERSO` o la rama expandida, no corrige el grafo por su cuenta.
- Detiene la generación, señala el nivel desfasado y ofrece ese handoff.

---

## Modo parcial: `--desde [nodo]`

`/refresh --desde artefacto` salta Pasos 1a y 1b, empieza desde Paso 2 usando los ficheros actuales como input. Útil cuando el usuario editó el artefacto manualmente.

Nodos válidos: `corpus`, `hilo`, `artefacto`, `universo`.

---

## Boceto de implementación

### `mod/agents/pipeline.agent.md`

```yaml
---
name: Pipeline
description: "Refresca la cadena de derivados tras modificar piezas del lore. Ejecuta paso a paso, muestra deltas, para si no hay cambios."
argument-hint: "[refresh | refresh --desde artefacto | status]"
tools: [vscode, read, edit, search, agent]
agents: [Bartleby, Dramaturgo Cortos]
handoffs:
  - label: "Generar corto desde universo-1"
    agent: Dramaturgo Cortos
    prompt: "Genera el corto de universo-1. El pipeline acaba de refrescar toda la cadena."
    send: false
  - label: "Ver estado del corpus"
    agent: Archivero
    prompt: "/status"
    send: true
---
```

Body: el protocolo de 6 pasos documentado arriba, con el grafo de dependencias, las condiciones de ejecución por paso, y los formatos de delta.

### `mod/prompts/refresh.prompt.md`

```yaml
---
name: refresh
description: "Refresca la cadena de derivados del pipeline tras modificar piezas del lore."
argument-hint: "[--desde corpus|hilo|artefacto|universo]"
agent: Pipeline
tools: [vscode, read, edit, search, agent]
---
```

Body: instrucción de invocar el protocolo de refresh del agente Pipeline, pasando el argumento `--desde` si el usuario lo especificó.

### `mod/agents/dramaturgo.agent.md`

Añadir al frontmatter:

```yaml
handoffs:
  - label: "Ejecutar refresh del pipeline"
    agent: Pipeline
    prompt: "/refresh"
    send: true
```

Y en el body una regla explícita: si el pipeline está desincronizado, el dramaturgo no genera todavía y deriva el refresh por handoff.

---

## Nota sobre portabilidad al SDK

La lección de que corpus y hilo son hermanos es un patrón portable. Si se confirma en otros lores, debería documentarse como nota en el skill `futures-engine` de `.github/skills/`. Pero eso lo hace el mantenedor del SDK, no el cristalizador. Por ahora el grafo queda codificado en el agente de `mod/`.
