# Guía de Producción del Lore y Product Backlog

> Estado: documento rector de trabajo
> Ubicación: `DRAFTS2/`
> Función: ordenar la extracción de piezas, la refactorización editorial y la investigación pendiente
> No forma parte del conteo de piezas del lore

---

## 1. Objetivo del plan

Este documento fija una guía de trabajo para seguir sacando piezas del lore sin perder el criterio ya ganado en el proceso documental.

El objetivo no es producir más texto por inercia, sino:

- separar correctamente tipos de pieza
- decidir qué puede inflarse desde corpus interno y qué requiere referencia externa
- mantener una política clara de soportes raw y ficheros auxiliares
- usar `LORE_DRAFT.md` como cantera cruda
- tratar `LORE_DRAFT_CORE.md` como encargo editorial, no como pieza del lore

---

## 2. Jerarquía de fuentes

### 2.1. Fuente cruda

- `DRAFTS2/LORE_DRAFT.md` es la cantera primaria cuando haya que recuperar formulaciones, conexiones o ideas que pudieron perderse al limpiar.
- Si una intuición estaba en el draft y se diluyó en los bloques limpios, se puede rescatar desde aquí.

### 2.2. Fuente estructurada

- `LORE_A.md` a `LORE_F.md` son la capa limpia y estable del lore.
- `LORE_INDEX.md` fija marcas, conteo y mapa general.

### 2.3. Soportes por pieza

- `LORE_S-*` y `LORE_N-*` son expansiones reutilizables.
- No añaden piezas nuevas al conteo; sacan evidencia y detalle fuera del bloque.

### 2.4. Encargo editorial

- `DRAFTS2/LORE_DRAFT_CORE.md` no es lore limpio ni pieza autónoma.
- Debe tratarse como nota del PO / issue editorial.
- Su función actual es una sola: pedir refactor de `LORE_F.md` para restituir mejor la presunción de inocencia y absorber nueva evidencia documental.

---

## 3. Principios de trabajo

### 3.1. Regla por formato

Tambien creo que hay que fijar una regla por formato. Esta regla no debe volver a improvisarse en cada iteración.

| Formato | Qué es | Fichero de soporte propio | Raw `.txt` en `tmp/media-cache/` | Investigación externa | Nota operativa |
|---------|--------|---------------------------|----------------------------------|----------------------|----------------|
| `S-*` | pieza social, vídeo, stream, clip, post | Sí, cuando haya suficiente densidad documental | Sí, cuando haya transcripción o verbatim útil | A veces | Es el carril más claro para STT y extractos |
| `N-*` | noticia, anuncio, artículo, caso oficial | Sí | Sí, cuando exista verbatim o recorte textual útil | Sí, casi siempre | Importa preservar etiquetas, sección y encuadre |
| `P-*` | personaje / nodo de actor | Sí, si ya hay material acumulado suficiente en otras piezas | No por defecto | A veces | Suele ser pieza derivada del resto del corpus |
| `T-*` | fase cronológica / mecanismo del caso | Sí, si hay suficiente evidencia interna | No por defecto | No siempre | Son piezas de síntesis, no fuentes primarias |
| `R-*` | recurso contextual / miniensayo | Sí, cuando se aborde | No por defecto | Sí, normalmente | Conviene tratarlas como investigación aparte |
| `F` | hilo narrativo concentrado | No es soporte; es salida compuesta | No | No aplica | Debe reescribirse cuando cambian las evidencias |

### 3.2. Soportes textuales versionados

- `tmp/media-cache/*.txt` puede usarse para raw textuales enlazados desde piezas de lore.
- Aquí entran tanto transcripciones STT como verbatim manuales de prensa o anuncios.
- No subir binarios ni estado técnico efímero.

### 3.3. Regla de prudencia narrativa

- El lore no debe convertir imputación en culpabilidad probada.
- Cuando el corpus solo permite decir que algo se imputa, presume o acusa, así debe quedar escrito.
- Esta regla afecta sobre todo a `LORE_F.md`, `T-*` y `P-*`.

### 3.4. Regla de estabilidad

- Una marca estable no se renumera salvo necesidad extrema.
- Los soportes no cambian el total de piezas.
- El índice solo cambia el total cuando nace una marca nueva real.

---

## 4. Carriles de trabajo

Para no mezclar trabajos heterogéneos, el proyecto se divide en cuatro carriles.

### Carril A — Piezas internas inflables

Piezas que ya pueden crecer casi enteramente desde el corpus actual, sin mucha búsqueda externa.

Candidatas principales:

- `P-01` Feo
- `P-09` Cerezo
- `T-09` Lucro: cesante, directo/indirecto
- `T-10` La CAUSA
- `T-12` El juicio
- `T-13` Las penas

### Carril B — Piezas con referencia externa aportada

Piezas que requieren URL, recorte, clip o transcripción concreta dada por el usuario o recuperada con apoyo documental.

Candidatas principales:

- `N-02`, `N-03` y futuras noticias
- `S-05` Facu → Bustinduy
- `S-06` Rubén: crónica Facu/Bustinduy
- `S-07` Rubén: entrevista David Bravo
- `S-08` Rubén sobre la idea feliz
- futura edición en papel de Diario de Burgos vinculada a `N-03`

### Carril C — Recursos contextuales de investigación

Piezas `R-*` que son miniensayos o contextos históricos y no deben inflarse solo por extrapolación.

Candidatas:

- `R-01` a `R-08`

### Carril D — Refactor editorial del hilo

Trabajo de reescritura de `LORE_F.md` a la luz de las nuevas piezas y soportes.

Este carril toma como input principal:

- `LORE_DRAFT_CORE.md`
- `S-01`, `S-02`, `S-03`
- `N-02`, `N-03`
- futuras piezas que modifiquen el encuadre del caso

---

## 5. Definition of Ready

Una pieza está lista para trabajarse cuando cumple estas condiciones mínimas.

### 5.1. Para piezas internas (`P-*`, `T-*`)

- hay al menos dos anclajes claros en bloques limpios o soportes ya creados
- el `LORE_DRAFT.md` añade matiz o formulación recuperable
- no depende críticamente de una fuente externa aún ausente

### 5.2. Para piezas externas (`S-*`, `N-*`)

- hay URL, recorte, anuncio, transcript o copia textual suficiente
- se puede citar una fuente principal identificable
- existe materia para distinguir dato, encuadre y lectura útil

### 5.3. Para recursos (`R-*`)

- hay un eje temático claro
- existe una lista mínima de hitos, casos o bibliografía a tratar
- no se confunde contexto general con afirmaciones específicas del caso

---

## 6. Definition of Done

Una pieza se considera terminada cuando cumple lo siguiente.

### 6.1. Piezas `S-*` y `N-*`

- aparece o se actualiza en su bloque principal
- tiene soporte `LORE_*` si el volumen lo justifica
- enlaza a raw `.txt` versionado cuando exista
- deja anclajes útiles y extractos preservados
- especifica qué fija y qué deja fuera

### 6.2. Piezas `P-*` y `T-*`

- tiene ficha propia derivada del corpus
- deja visibles dependencias con otras marcas
- evita sobrerelatar o dar por demostrado lo que no está demostrado

### 6.3. Recursos `R-*`

- delimita bien su función contextual
- no invade el caso concreto con inferencias no soportadas
- deja una estructura reutilizable para futura entrada documental

### 6.4. `LORE_F.md`

- usa el corpus actualizado
- no sentencia antes del veredicto
- absorbe los contrapesos documentales entre piezas
- conserva la función de relato mínimo robusto que usa todas las marcas

---

## 7. Features / Epics

### FEAT-01 — Gobernanza del lore

Objetivo:

- fijar reglas por formato
- separar fuente cruda, soporte y salida compuesta
- evitar que `LORE_DRAFT_CORE.md` contamine el pipeline de piezas

Entregables:

- esta guía
- criterio estable para soportes y raws

### FEAT-02 — Expansión documental por pieza

Objetivo:

- sacar del bloque principal las piezas con densidad suficiente
- volverlas fácilmente referenciables por agentes y por la futura entrada documental

Entregables:

- `LORE_S-*`, `LORE_N-*`, futuros `LORE_P-*`, `LORE_T-*`, `LORE_R-*`

### FEAT-03 — Refactor de `LORE_F.md`

Objetivo:

- corregir el hilo a la luz de evidencia nueva
- mantener su función de concentrado robusto de todas las piezas

Entregables:

- nueva versión de `LORE_F.md`
- checklist editorial derivado del PO

### FEAT-04 — Ingesta de fuentes externas

Objetivo:

- convertir referencias de prensa, streams y entrevistas en piezas útiles y trazables

Entregables:

- raws `.txt`
- fichas `N-*` / `S-*`
- enlaces cruzados con piezas ya existentes

### FEAT-05 — Recursos contextuales

Objetivo:

- desarrollar `R-*` sin mezclar contexto general y hechos del caso

Entregables:

- fichas `LORE_R-*`
- cronologías, tablas y marcos comparativos cuando proceda

---

## 8. Product Backlog

| ID | Feature | Ítem | Tipo | Estado | Prioridad | Dependencias | Salida esperada |
|----|---------|------|------|--------|-----------|--------------|-----------------|
| PB-001 | FEAT-01 | Fijar reglas por formato y soportes | Gobernanza | Hecho | Alta | Ninguna | `LORE_PLAN.md` |
| PB-002 | FEAT-02 | Soporte `P-01` Feo | Interna inflable | Hecho | Alta | `S-01`, `S-02`, `N-02`, `N-03`, `F` | `LORE_P-01.md` |
| PB-003 | FEAT-02 | Soporte `P-09` Cerezo | Interna inflable | Hecho | Alta | `N-01`, `S-01`, `S-03`, `N-02`, `N-03`, `F` | `LORE_P-09.md` |
| PB-004 | FEAT-02 | Soporte `T-09` Lucro | Interna inflable | Hecho | Alta | `S-02`, `S-03`, `N-02`, `N-03`, `F` | `LORE_T-09.md` |
| PB-005 | FEAT-03 | Refactor `LORE_F.md` hasta el presente | Editorial | Ready | Alta | `PB-002`, `PB-003`, `PB-004` idealmente; mínimo `S-01..S-03`, `N-02`, `N-03` | Nueva `LORE_F.md` |
| PB-006 | FEAT-02 | Soporte `T-10` La CAUSA | Interna inflable | Ready | Alta | `N-01`, `N-03`, `F` | `LORE_T-10.md` |
| PB-007 | FEAT-02 | Soporte `T-12` El juicio | Interna inflable | Ready | Media | `S-02`, `N-02`, `F` | `LORE_T-12.md` |
| PB-008 | FEAT-02 | Soporte `T-13` Las penas | Interna inflable | Hecho | Media | `S-02`, `N-02`, `F` | `LORE_T-13.md` |
| PB-009 | FEAT-04 | Soporte `S-05` Facu → Bustinduy | Externa | Hecho | Alta | referencia/audio suficiente | `LORE_S-05.md` + raw GPU |
| PB-010 | FEAT-04 | Soporte `N-03` edición en papel | Externa | Bloqueado | Alta | recorte o referencia directa de papel | ampliación de `LORE_N-03.md` |
| PB-011 | FEAT-04 | Soporte `S-06` Rubén crónica | Externa | Pendiente | Media | referencia concreta | `LORE_S-06.md` |
| PB-012 | FEAT-04 | Soporte `S-07` Rubén / David Bravo | Externa | Pendiente | Media | referencia concreta | `LORE_S-07.md` |
| PB-013 | FEAT-04 | Soporte `S-08` Rubén sobre idea feliz | Externa | Pendiente | Media | referencia concreta | `LORE_S-08.md` |
| PB-014 | FEAT-02 | Soporte `P-02` David Bravo | Mixta | Pendiente | Media | `S-07`, `T-12`, `F` | `LORE_P-02.md` |
| PB-015 | FEAT-02 | Soporte `P-04` Cristóbal | Mixta | Ready | Media | `S-03`, `S-04`, `F` | `LORE_P-04.md` |
| PB-016 | FEAT-02 | Soporte `P-05` Facu | Mixta | Pendiente | Media | `S-05`, `S-06`, `F` | `LORE_P-05.md` |
| PB-017 | FEAT-02 | Soporte `P-08` Bustinduy | Mixta | Pendiente | Media | `S-05`, `S-06`, `F` | `LORE_P-08.md` |
| PB-018 | FEAT-02 | Soporte `P-03` Juez / `T-14` Veredicto | Bloqueada por tiempo | Bloqueado | Baja | veredicto real o decisión de mock | `LORE_P-03.md`, `LORE_T-14.md` |
| PB-019 | FEAT-05 | Desarrollar `R-01` a `R-08` | Investigación | Pendiente | Baja | bibliografía y hitos mínimos | `LORE_R-*.md` |
| PB-020 | FEAT-05 | Recurso `R-09` Tensión judicial | Investigación | Hecho (+) | Media | `R-01`, `R-02`, corpus interno | `LORE_R-09.md` |
| PB-021 | FEAT-04 | Extensión `S-03` cobertura total | Externa | Hecho | Alta | GPU, tail-check verificado | S-03 → 18 chunks, 83 min, end mark |
| PB-022 | FEAT-04 | Noticia `N-04` escrivivir.co | Externa (+) | Hecho | Alta | `S-03` completo | `LORE_N-04.md` + artículo editorial |

---

## 9. Propuesta de sprints

### Sprint 0 — Gobernanza y estructura ✅

Objetivo:

- dejar reglas estables para no rediscutir metodología en cada pieza

Resultado esperado:

- `LORE_PLAN.md`

### Sprint 1 — Núcleo interno del caso ✅

Objetivo:

- consolidar piezas que ya pueden crecer desde corpus interno

Backlog objetivo:

- `PB-002` `P-01` ✅
- `PB-003` `P-09` ✅
- `PB-004` `T-09` ✅
- `PB-008` `T-13` ✅ (adelantado de Sprint 2)

### Sprint 2 — Eje procesal y reparación del hilo (parcial)

Objetivo:

- reforzar el eje jurídico-procesal
- reescribir `LORE_F.md` con mejor prudencia narrativa

Backlog objetivo:

- `PB-006` `T-10` — Ready, pendiente
- `PB-007` `T-12` — Ready, pendiente
- ~~`PB-008` `T-13`~~ — adelantado a Sprint 1
- `PB-005` refactor `LORE_F.md` — Ready, pendiente (ticket formalizado en `LORE_DRAFT_CORE.md`)

### Sprint 3 — Continuación institucional y mediática (parcial)

Objetivo:

- formalizar el salto de ruido social a umbral institucional

Backlog objetivo:

- `PB-009` `S-05` ✅ (GPU transcripción completa)
- `PB-016` `P-05` — Pendiente
- `PB-017` `P-08` — Pendiente

### Sprint emergente — Trabajo no previsto en plan original

Completado fuera de los sprints planificados:

- `PB-020` `R-09` Tensión judicial ✅ — pieza emergente (+), no prevista
- `PB-021` Extensión `S-03` a cobertura total ✅ — 67min → 83min, end mark verificado
- `PB-022` `N-04` escrivivir.co ✅ — noticia posicionada nueva (+), arquetipo de alternativas

### Sprint 4 — Rama Rubén / Bravo

Objetivo:

- abrir la segunda cola mediática del caso

Backlog objetivo:

- `PB-011` `S-06`
- `PB-012` `S-07`
- `PB-013` `S-08`
- `PB-014` `P-02`

### Sprint 5 — Recursos contextuales

Objetivo:

- convertir `R-*` en contexto reusable de alta calidad

Backlog objetivo:

- `PB-019`

---

## 10. Siguiente lote prioritario recomendado

Si el trabajo continúa de forma incremental, el siguiente lote prioritario debería ser:

1. `P-01` Feo
2. `P-09` Cerezo
3. `T-09` Lucro: cesante, directo/indirecto
4. refactor de `LORE_F.md`

Razón:

- son piezas ya muy soportadas por el corpus existente
- reducen la ambigüedad jurídica del hilo principal
- hacen más segura cualquier expansión futura de `T-*`, `P-*` y `N-*`

---

## 11. Regla final de uso

Cada vez que aparezca una nueva referencia, antes de trabajarla hay que decidir en qué casilla cae:

- ¿es pieza interna inflable?
- ¿es pieza externa con fuente aportada?
- ¿es recurso contextual?
- ¿o es una nota editorial tipo `LORE_DRAFT_CORE.md`?

Si no se responde eso primero, el lore vuelve a mezclar corpus, soporte, encargo y salida narrativa.