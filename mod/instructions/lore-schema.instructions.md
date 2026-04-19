---
description: "Esquema normativo de tipos de pieza del lore legislativa. Define ontología, campos obligatorios, DoR/DoD y reglas de conteo."
applyTo: "DRAFTS2/LORE_*.md"
---

# Esquema de tipos de pieza — mod legislativa

> **Fuente:** formalización de `LORE_PLAN.md` §3, §5, §6 + convenciones de `LORE_INDEX.md`.
> **Uso:** un agente que lea este fichero puede responder sin ambigüedad:
> "¿esta pieza tiene formato válido?", "¿cumple DoR?", "¿qué campos le faltan?"

---

## 1. Ontología de tipos

| Tipo | Qué es | Fichero propio | Raw `.txt` | Investigación externa |
|------|--------|----------------|------------|-----------------------|
| `P-*` | Personaje / nodo de actor | Sí, si hay material acumulado suficiente en otras piezas | No por defecto | A veces |
| `S-*` | Pieza social: vídeo, stream, clip, post | Sí, con densidad documental suficiente | Sí, cuando haya transcripción o verbatim | A veces |
| `N-*` | Noticia, anuncio, artículo, caso oficial | Sí | Sí, cuando exista verbatim o recorte útil | Sí, casi siempre |
| `T-*` | Fase cronológica o mecanismo del caso | Sí, con evidencia interna suficiente | No por defecto | No siempre |
| `R-*` | Recurso contextual / miniensayo | Sí, cuando se aborde | No por defecto | Sí, normalmente |
| `F` | Hilo narrativo concentrado (salida compuesta) | No: `F` es salida, no fuente | No | No aplica |

---

## 2. Campos por tipo

### 2.1. `P-*` — Personaje

**Cabecera obligatoria:**
```markdown
# `[P-NN]` — {Nombre}

> ← {bloque-principal}.md
> ← LORE_INDEX.md
```

**Tabla de identificación obligatoria:**

| Campo | Descripción |
|-------|-------------|
| `Marca` | `[P-NN]` — no reasignable |
| `Nombre` | Nombre canónico del personaje |
| `Rol` | Función en el caso (ej: "Acusado / protagonista") |
| `Esfera` | Dominio (ej: "Caso", "Judicial", "Mediático") |
| `Bloque principal` | Referencia a `LORE_A.md §X.N` |
| `Estado` | Texto libre: "Ficha derivada del corpus interno", "En construcción", etc. |

**Campos opcionales:** subsecciones de perfil, tabla de actividad, motivación, referencias cruzadas.

**Ejemplo mínimo:**
```markdown
## Identificación

| Campo | Valor |
|-------|-------|
| Marca | `[P-01]` |
| Nombre | Feo |
| Rol | Acusado / protagonista del caso |
| Esfera | Caso |
| Bloque principal | [LORE_A.md](LORE_A.md) §A.1 |
| Estado | Ficha derivada del corpus interno |
```

---

### 2.2. `S-*` — Pieza social

**Cabecera obligatoria:**
```markdown
# `[S-NN]` — {Título corto}

> ← {bloque-principal}.md
> ← LORE_INDEX.md
```

**Tabla de identificación obligatoria:**

| Campo | Descripción |
|-------|-------------|
| `Marca` | `[S-NN]` |
| `Emisor` | Marca del personaje que produce la pieza (`[P-NN]`) |
| `Tipo` | Clase de pieza (ej: "Testimonio directo", "Livestream", "Post") |
| `Fuente` | URL de la fuente original |
| `Título` | Título de la pieza (cursiva en la tabla) |
| `Estado` | Texto libre |

**Campos opcionales:**

| Campo | Cuándo usarlo |
|-------|---------------|
| `Duración` | Vídeos y audios |
| `Cache local` | Cuando haya fichero en `tmp/media-cache/` |
| `Transcripciones versionadas` | Cuando haya STT local |

**Secciones esperadas:** `## Anclajes útiles` (tabla: Eje / Dato útil / Conecta con), `## Nota de soporte` (si aplica).

**Ejemplo mínimo:**
```markdown
## Identificación

| Campo | Valor |
|-------|-------|
| Marca | `[S-01]` |
| Emisor | `[P-01]` Feo |
| Tipo | Testimonio directo |
| Fuente | https://... |
| Título | *Título* |
| Estado | Pieza expandida con transcripción |
```

---

### 2.3. `N-*` — Noticia / caso oficial

**Cabecera obligatoria:**
```markdown
# `[N-NN]` — {Titular corto}

> ← {bloque-principal}.md
> ← LORE_INDEX.md
```

**Tabla de identificación obligatoria:**

| Campo | Descripción |
|-------|-------------|
| `Marca` | `[N-NN]` |
| `Medio` | Nombre del medio |
| `Tipo` | Clase (ej: "Noticia / encuadre de caso") |
| `Fuente` | URL |
| `Título` | Titular exacto en cursiva |
| `Fecha visible` | Fecha de publicación legible en la fuente |
| `Estado` | Texto libre |

**Campos opcionales:**

| Campo | Cuándo usarlo |
|-------|---------------|
| `Etiquetas visibles` | Cuando el medio muestre etiquetas o categorías |
| `Verbatim versionado` | Enlace a `tmp/media-cache/{archivo}.txt` cuando exista |

**Secciones esperadas:** `## Anclajes útiles`, `## Arquitectura del encuadre` (análisis funcional).

---

### 2.4. `T-*` — Fase cronológica / mecanismo

**Cabecera obligatoria:**
```markdown
# `[T-NN]` — {Nombre de la fase}

> ← {bloque-principal}.md
> ← LORE_INDEX.md
```

**Tabla de identificación obligatoria:**

| Campo | Descripción |
|-------|-------------|
| `Marca` | `[T-NN]` |
| `Fase` | Nombre canónico de la fase o mecanismo |
| `Tipo` | Función (ej: "Categorías jurídicas clave del caso") |
| `Grupo` | Grupo temporal del bloque D (ej: "D.1 — Pasado visible en T=0") |
| `Bloque principal` | Referencia a `LORE_D.md` |
| `Estado` | Texto libre |

**Nota de uso:** las `T-*` son piezas de síntesis, no fuentes primarias. No afirman más de lo que el corpus soporta.

---

### 2.5. `R-*` — Recurso contextual

**Cabecera obligatoria:**
```markdown
# `[R-NN]` — {Título del recurso}

> ← {bloque-principal}.md
> ← LORE_INDEX.md
```

**Si es emergencia (+), añadir nota de emergencia en la cabecera:**
```markdown
> **Emergencia (+):** pieza no prevista en el draft original. [Justificación.]
> **Función:** [qué aporta al corpus sin invadir el caso concreto.]
```

**Tabla de identificación obligatoria:**

| Campo | Descripción |
|-------|-------------|
| `Marca` | `[R-NN]` |
| `Tipo` | Clase (ej: "Recurso contextual — mapa de tensión institucional") |
| `Bloque principal` | Referencia a `LORE_E.md` |
| `Estado` | Texto libre |

**Campo opcional:** `Periodo cubierto` cuando aplique rango temporal.

**Nota de uso:** delimita su función contextual. No invade el caso concreto con inferencias no soportadas.

---

### 2.6. `F` — Hilo narrativo

`F` no es un tipo de soporte: es la salida compuesta del corpus. No tiene fichero propio de soporte. Debe reescribirse cuando cambia el corpus. Usa todas las marcas (`[P-*]`, `[S-*]`, `[N-*]`, `[T-*]`, `[R-*]`). No sentencia antes del veredicto. No convierte imputación en culpabilidad probada.

---

## 3. Convenciones de nombrado

- **Patrón:** `LORE_<TIPO>-<NN>.md` (ej: `LORE_P-01.md`, `LORE_S-09.md`)
- **Excepción:** el hilo narrativo es `LORE_F.md` (sin número)
- **Marcas:** `[P-NN]`, `[S-NN]`, `[N-NN]`, `[T-NN]`, `[R-NN]`, `[F]` — **no reasignables**
- **Emergencias:** se sufijan con `(+)` en el índice (ej: `[R-09](+)`)
- **Estabilidad:** una marca asignada no se renumera salvo necesidad extrema documentada

---

## 4. Definition of Ready (DoR) operativa

Un agente puede verificar estas condiciones sin intervención humana.

### 4.1. Piezas internas: `P-*`, `T-*`

- [ ] Al menos **2 anclajes** verificables en bloques limpios (`LORE_A.md`–`LORE_F.md`) o soportes ya existentes
- [ ] `LORE_DRAFT.md` aporta matiz o formulación recuperable (opcional pero preferible)
- [ ] No depende críticamente de una fuente externa aún ausente

### 4.2. Piezas externas: `S-*`, `N-*`

- [ ] Existe **URL, recorte, anuncio, transcript o copia textual suficiente**
- [ ] Se puede citar una **fuente principal identificable** (medio, canal, autor)
- [ ] Hay materia para distinguir: dato vs. encuadre vs. lectura útil

### 4.3. Recursos: `R-*`

- [ ] Tiene un **eje temático claro** (no es cajón de sastre)
- [ ] Existe lista mínima de hitos, casos o bibliografía a tratar
- [ ] No confunde contexto general con afirmaciones específicas del caso

---

## 5. Definition of Done (DoD) operativa

### 5.1. `S-*` y `N-*` — Done cuando:

- [ ] Aparece o se actualiza en su bloque principal (`LORE_B.md` o `LORE_C.md`)
- [ ] Tiene fichero de soporte `LORE_<TIPO>-<NN>.md` si el volumen lo justifica
- [ ] Enlaza a raw `.txt` versionado en `tmp/media-cache/` cuando exista
- [ ] Contiene tabla `## Anclajes útiles` con referencias cruzadas
- [ ] Especifica qué fija y qué deja fuera

### 5.2. `P-*` y `T-*` — Done cuando:

- [ ] Tiene ficha propia derivada del corpus (no de extrapolación)
- [ ] Deja visibles **dependencias con otras marcas** en la tabla de identificación o en el cuerpo
- [ ] No sobrerrelata ni da por demostrado lo que no está demostrado

### 5.3. `R-*` — Done cuando:

- [ ] Delimita su función contextual (no invade el caso concreto)
- [ ] Deja estructura reutilizable para futura entrada documental
- [ ] No incluye inferencias no soportadas sobre el caso Feo/Zoowoman

### 5.4. `F` — Done cuando:

- [ ] Usa el corpus actualizado (todas las marcas activas)
- [ ] No sentencia antes del veredicto
- [ ] Absorbe contrapesos documentales entre piezas
- [ ] Conserva función de relato mínimo robusto

---

## 6. Regla de conteo

| Condición | ¿Suma al total? |
|-----------|-----------------|
| Pieza nueva con marca propia (cualquier tipo) | **Sí** |
| Fichero de soporte de pieza ya contada | **No** |
| Emergencia marcada con `(+)` en el índice | **Sí** (es pieza nueva) |
| `LORE_DRAFT.md`, `LORE_DRAFT_CORE.md` | **No** (cantera / encargo editorial) |
| `LORE_INDEX.md`, `LORE_PLAN.md` | **No** (metadocumentos) |
| `LORE_F.md` | **No** (salida compuesta, no pieza autónoma) |

> El total solo cambia cuando nace una marca nueva real.
> Los soportes no cambian el total aunque sean ficheros `.md` en `DRAFTS2/`.
