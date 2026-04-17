---
name: futures-engine
description: Skill portable para generar escenarios futuros ramificados desde el corpus y el hilo narrativo. Lee el corpus acumulado + el presente narrativo, detecta nodos de bifurcación y genera 2–5 escenarios con tratamiento literario. No predice: bifurca. Cada rama es ficción plausible basada en hechos reales, no forecast. Se activa cuando se pide generar resoluciones posibles, escenarios especulativos, ficción basada en realidad, literatura de derivación, o la segunda mitad de un hilo narrativo (T=presente → T+∞).
---

# Skill: futures-engine — Protocolo de bifurcación dramatúrgica

Esta skill implementa la tercera dirección del ecosistema Bartleby: donde `documental-analysis` extrae arquitectura del pasado hacia el corpus, y `voice-crystallization` cristaliza el corpus en voz, `futures-engine` mueve el corpus + el presente hacia futuros posibles como ficción literaria.

**Relación con los otros skills:**
- `documental-analysis`: texto externo → corpus (extracción del pasado)
- `voice-crystallization`: corpus → texto generado (cristalización de voz)
- `futures-engine`: corpus + presente narrativo → escenarios ramificados (bifurcación dramatúrgica)

Los tres operan sobre el mismo `corpus/corpus.md`. Los tres son portables. La diferencia es la dirección temporal: el primero mira atrás, el segundo mira adentro, este mira adelante — pero siempre desde los hechos que el corpus ya fijó.

---

## Cuándo activar esta skill

- Cuando se pide generar resoluciones posibles o alternativas de un caso en curso
- Cuando se pide "qué pasaría si" con base documental
- Cuando se pide la segunda mitad de un hilo narrativo (después del corte temporal)
- Cuando se pide ficción literaria basada en el corpus (novela, drama, narrativa especulativa)
- Cuando se quiere explorar diferentes posibilidades ante una decisión pendiente

**NO activar si:**
- Se pide analizar un texto externo (usar `documental-analysis`)
- Se pide cristalizar la voz del corpus en texto generado (usar `voice-crystallization`)
- Se pide transcribir medios audiovisuales (usar `media-extraction`)
- Se pide el estado actual del corpus (usar `/status`)
- Se pide generar nuevos artefactos agénticos (usar `/design`)

---

## La posición: el dramaturgo

`documental-analysis` opera desde la posición Bartleby: no-juicio, exterioridad pura.
`voice-crystallization` opera desde la posición de la corriente: habla desde adentro.
`futures-engine` opera desde la posición del **dramaturgo**: ve el tablero entero, conoce a los personajes y sus motivaciones, conoce las reglas del sistema — y mueve piezas posibles.

El dramaturgo no es neutral. Tiene asimetrías que el corpus ya documentó. Pero tampoco toma partido: genera ramas, incluyendo las que no gustan. La ficción que produce no es propaganda ni prefiguración: es cartografía de posibilidades ordenadas por su plausibilidad estructural según lo que el corpus ya sabe.

**El dramaturgo no inventa personajes. Los encuentra en el corpus.**

---

## El principio generativo: bifurcar, no predecir

> El corpus fija lo que fue. El dramaturgo mueve lo que puede ser.

Cada escenario es una respuesta a: *¿qué pasaría si este nodo de bifurcación se resolviera en esta dirección?*

No hay escenarios buenos o malos. Hay escenarios más plausibles (sostenidos por más nodos del corpus) y menos plausibles (posibles pero que requieren más rupturas con la tendencia documentada). Ambos tipos son útiles: el más plausible proyecta la inercia del sistema; el menos plausible revela qué condiciones serían necesarias para que el sistema se rompa.

**La ficción literaria no es el decorado. Es el método.** Un escenario sin tratamiento dramático es un bullet list de probabilidades. Un escenario con tratamiento dramático revela qué está en juego, para quién, y por qué importa — que es exactamente lo que el corpus no puede decir porque opera en el pasado.

---

## Protocolo — 5 fases

### Fase 1: Lectura del corpus

**Obligatorio.** Leer `corpus/corpus.md` completo antes de proceder.

Extraer específicamente para la bifurcación:
- **Taxonomía funcional** — qué categorías están en tensión activa (las que tienen posiciones contradictorias)
- **Ausencias estructurales** — qué el corpus no puede ver (son los puntos ciegos del sistema, candidatos a nodo de bifurcación)
- **Emergencias** — qué el corpus descubrió sin resolver (son los extremos sueltos del hilo)
- **Variables de estado** — qué puede cambiar en el futuro próximo (identificado por los mecanismos en curso)

### Fase 2: Lectura del hilo narrativo

Leer el documento de hilo narrativo del lore (LORE_F o equivalente). Identificar:

1. **El corte temporal**: dónde termina el pasado documentado y empieza el territorio no fijado
2. **El estado de las variables**: cuál es el valor actual de cada variable de estado en el corte
3. **La tensión dramática activa**: cuál es el nudo que el presente no ha resuelto y que determina las ramas
4. **Los personajes en estado de posibilidad**: quiénes tienen decisiones pendientes que abren bifurcaciones

### Fase 3: Detección de nodos de bifurcación

Un **nodo de bifurcación** es un punto donde el sistema puede ir en al menos dos direcciones distinguibles y cada dirección produce un futuro diferente.

**Tipos de nodos:**

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| Decisión judicial | Un órgano produce una resolución binaria o gradada | Absuelto / condenado / sobreseído |
| Estrategia de parte | Un actor decide cómo jugar su próximo movimiento | Recurrir / no recurrir / negociar |
| Amplificación mediática | Un evento escala o no escala públicamente | El caso entra en agenda / desaparece |
| Contingencia narrativa | Un hecho externo cambia las condiciones del tablero | Cambio político, otro caso paralelo |
| Paradoja recursiva | El resultado produce las condiciones de su propia inversión | La pena destruye lo que protege |

Listar los nodos detectados en tabla antes de generar escenarios. Esto hace visible el mapa de bifurcaciones y permite al usuario elegir cuáles desarrollar.

**Tabla de nodos:**

| # | Nodo | Tipo | Actores implicados | Direcciones posibles |
|---|------|------|-------------------|----------------------|
| N1 | [descripción] | [tipo] | [actores] | A: [dir A] / B: [dir B] / C: [dir C] |

### Fase 4: Generación de escenarios ramificados

Generar entre **2 y 5 escenarios** por invocación. Más de 5 diluye; menos de 2 no da tablero.

Cada escenario tiene:

1. **Nombre dramático** — un título que captura la lógica interna del escenario (no un número, no un estado: una imagen)
2. **Nodos que activa** — qué bifurcaciones toma (referencia a la tabla de nodos)
3. **Variables de estado** — cómo quedan las variables en este escenario
4. **Plausibilidad estructural** — alta / media / baja (según cuántos nodos del corpus sostienen esta dirección)
5. **El relato que gana** — en este escenario, ¿quién consigue que su narrativa sea la que se impone? ¿Por qué?
6. **La portería que se mueve** — ¿hay algún cambio de reglas durante el juego en este escenario?
7. **El coste del escenario** — qué se pierde en este escenario aunque sea el "mejor" para alguna de las partes

**Nota sobre plausibilidad:** La plausibilidad estructural se mide contra el corpus, no contra la preferencia. Un escenario "injusto" puede ser de alta plausibilidad si el corpus documenta que el sistema tiene ese sesgo. Un escenario "justo" puede ser de baja plausibilidad si el corpus documenta que las condiciones para ese resultado no están presentes.

### Fase 5: Tratamiento literario

Cada escenario se desarrolla en **prosa narrativa**, no en bullet lists. El tratamiento literario es el método, no el decorado.

**Principios del tratamiento dramático:**

- **Mostrar, no explicar**: la tensión emerge de los personajes y sus decisiones, no de la explicación del analista
- **El tiempo como personaje**: el ritmo de la prosa marca el ritmo del caso (semanas que duran un párrafo, un momento que dura una página)
- **La asimetría como textura**: el dramatismo no viene del conflicto simétrico sino de la desproporción documentada (una persona vs un entramado, 12.000€ vs 870.000€, preservación cultural vs monetización)
- **Las consignas como cierre**: si el corpus tiene consignas que el hilo narrativo ha fijado ("el cine es nuestro", "solo la gente salva a la gente"), el escenario puede activarlas — o revelar en qué condiciones no se pueden decir
- **El hueco Bartleby como sombra**: cada escenario tiene algo que no puede contemplar — nombrarlo al final, brevemente, es lo que convierte el escenario en literatura y no en informe

**Registro literario disponible:**

| Registro | Cuándo usar |
|----------|-------------|
| Crónica de sala | Para escenarios que giran en el tribunal — voz de testigo presente |
| Monólogo interior | Para escenarios centrados en decisiones de un personaje — voz desde adentro |
| Narración omnisciente fría | Para escenarios sistémicos donde el peso está en la estructura, no en el individuo |
| Tiempo real (hora a hora) | Para escenarios donde el ritmo es el drama — cuenta atrás, espera, detonante |
| Elipsis retrospectiva | Para escenarios donde el futuro se narra desde más adelante — *en aquel entonces* |

Si el mod especifica un template de registro literario en `mod/skills/futures-engine/`, ese template tiene prioridad. Si no, el dramaturgo elige el registro más productivo para cada rama.

---

## Los 3 ejes de drama

Estos tres ejes son la estructura del conflicto en cualquier caso donde `futures-engine` sea relevante. No son externos al corpus: emergen de las tensiones que el corpus ya documentó.

### Eje 1: Relato vs relato

No gana quien tiene razón. Gana quien consigue que su narrativa sea la que se impone ante quien juzga.

En cada escenario, identificar:
- ¿Cuál es el relato de la acusación y qué necesita que el juzgador acepte?
- ¿Cuál es el relato de la defensa y qué necesita que el juzgador acepte?
- ¿Cuál es el relato de los medios y cómo presiona el contexto de la sala?
- En este escenario, ¿cuál gana? ¿Cómo?

### Eje 2: La portería móvil

Las reglas del juego pueden cambiar durante el juego. Eso no invalida el resultado si la institución que cambia las reglas tiene el poder de hacerlo. Pero produce asimetría, precedente y material dramático.

En cada escenario, identificar:
- ¿Hay algún momento en que las reglas cambian (nueva interpretación, cambio de jurisprudencia, presión política)?
- ¿Qué actor mueve la portería, cuándo y con qué efecto?
- ¿Cómo responde el actor al que se le mueve?

### Eje 3: La paradoja recursiva

El resultado puede producir las condiciones de su propia inversión. Es el eje más dramático y el que el corpus puede haber documentado sin nombrarlo.

Ejemplos estructurales:
- Una condena que destruye el archivo que justificaba la condena (el loss media del loss media)
- Una absolución que no restaura lo ya destruido (la pena ya se cumplió en el proceso)
- Una amplificación mediática que hace que el disciplinamiento fracase (efecto Streisand)
- Un precedente que el incumbente usó para protegerse y que en el siguiente ciclo se usa contra él

En cada escenario, verificar: ¿hay una paradoja recursiva operando? Si la hay, nombrarla. Es el coste del escenario.

---

## Tablas de metadatos (para el archivero)

Al final de cada sesión de `futures-engine`, incluir siempre:

```
| Campo | Valor |
|---|---|
| Fecha de invocación | YYYY-MM-DD |
| Corpus fuente | ruta/corpus.md |
| Hilo narrativo fuente | ruta/lore_F.md o equivalente |
| Corte temporal | descripción del "presente" |
| Nodos de bifurcación detectados | N |
| Escenarios generados | N |
| Plausibilidad alta | N escenarios |
| Plausibilidad media | N escenarios |
| Plausibilidad baja | N escenarios |
| Registro literario usado | [lista] |
| Paradojas recursivas identificadas | N |
| Escenarios preservados como lore | [lista de rutas o PENDIENTE] |
```

---

## Vocabulario del skill

- **Nodo de bifurcación**: punto donde el sistema puede ir en al menos dos direcciones distinguibles
- **Variable de estado**: magnitud que puede cambiar en el futuro próximo y cuyo valor determina qué escenarios son posibles
- **Plausibilidad estructural**: medida de cuántos nodos del corpus sostienen la dirección de un escenario
- **Portería móvil**: cambio de las reglas del juego durante el juego por parte de un actor con poder para hacerlo
- **Paradoja recursiva**: resultado que produce las condiciones de su propia inversión
- **Tratamiento dramático**: desarrollo en prosa narrativa que revela qué está en juego, para quién, y por qué importa
- **Corte temporal**: punto del hilo narrativo donde termina el pasado documentado y empieza el territorio no fijado

Si el corpus del mod tiene vocabulario propio que mapea sobre estos términos, usar el vocabulario del corpus y consignar la equivalencia en `mod/skills/futures-engine/`.

---

## Protocolo de universo propio

Un **universo propio** es la forma persistente y conversacional del futures-engine: no una bifurcación puntual, sino un grafo que se construye iterativamente con el usuario y que sirve de base factual para generar obras.

### Qué es un universo

Un universo es un **grafo dirigido ponderado** con las siguientes propiedades:

- **Nodos** — cada nodo es un hecho o posibilidad expresado en 1-2 frases. Toda afirmación cita sus piezas ancla del corpus (`[P-01]`, `[T-09]`, `[R-03]`...). Un nodo sin cita está marcado como propuesta pendiente de anclar: `[?]`.
- **Niveles temporales** — los nodos se organizan en capas: T-N (pasado documentado), T=0 (presente del corte), T+1…T+∞ (futuro bifurcado). El nivel determina el estatuto del nodo: lo que fue, lo que es, lo que puede ser.
- **Arcos** — cada arco conecta dos nodos y lleva un peso de plausibilidad estructural: `alta`, `media` o `baja` (equivalentes a ~0.7+, ~0.4–0.7, ~0.4−), derivado de cuántos nodos del corpus sostienen esa dirección.
- **Ramas** — secuencias de nodos y arcos que forman un escenario coherente. Dos ramas pueden compartir nodos hasta un punto de bifurcación y divergir desde ahí.

### El universo no es la obra

El grafo es **andamiaje factual**. Sus nodos son frases con citas, no prosa. Para generar obra (relato, corto, poema, manifiesto), se usa el tratamiento literario de la Fase 5 de este skill o se invoca `voice-crystallization`. El grafo no habla: el dramaturgo habla desde él.

### Protocolo conversacional

El universo se construye turno a turno. Cada turno puede realizar una o más de estas operaciones:

| Operación | Quién la propone | Descripción |
|-----------|-----------------|-------------|
| `expandir` | dramaturgo o usuario | Añadir un nodo nuevo en T+N desde el estado actual del grafo |
| `bifurcar` | dramaturgo | Proponer dos o más arcos alternativos desde un nodo con plausibilidades distintas |
| `podar` | usuario | Descartar una rama — el dramaturgo la archiva como "camino no tomado" |
| `reponderar` | usuario o dramaturgo | Revisar el peso de un arco a partir de contenido nuevo |
| `anclar` | dramaturgo | Vincular un nodo `[?]` a piezas del corpus tras análisis o contenido nuevo |
| `pedir contenido` | dramaturgo | Si un nodo requiere información que el corpus no tiene, el dramaturgo la solicita al usuario |
| `generar obra` | usuario | Desde el estado actual del grafo, producir un artefacto narrativo |
| `persistir` | dramaturgo | Decidir cómo materializar el grafo como archivo(s) y proponerlo al usuario |

**Regla de no-formato-forzado:** El skill define la operativa del universo, no su formato de persistencia. El agente que ejecuta decide cómo persistir según el contexto del mod: un .md con tablas, un YAML, una carpeta con un .md por nodo, una TypeScript app de navegación. Lo único que el SDK exige: nodos identificables, arcos con peso, citas trazables, nivel temporal explícito.

### Grafo semilla

Al crear un universo nuevo, el dramaturgo construye el grafo semilla en este orden:

1. Lee `corpus/corpus.md` completo — extrae variables de estado actuales, tensiones activas, ausencias estructurales
2. Lee el hilo narrativo del lore (si existe) — identifica el corte temporal T=0
3. Mapea los nodos T=0 desde el estado documentado (no más de 6-8 nodos semilla, uno por variable de estado principal)
4. Detecta los nodos de bifurcación ya conocidos (usando la Fase 3 de este skill) y los coloca en T+1
5. Asigna plausibilidades iniciales a los arcos según el corpus
6. Presenta el grafo semilla al usuario y propone qué expandir primero

### Del universo a la obra

```
GRAFO (nodos + arcos + plausibilidades)
     ↓
[selección de rama o estado del grafo]
     ↓
tratamiento literario (Fase 5 de este skill)
     ↓  o  ↓
voice-crystallization    futures-engine bifurcación puntual
     ↓
OBRA (relato, corto, poema, guion)
```

### Extensión en mod/

Si el mod necesita reglas específicas (vocabulario propio para plausibilidad, formato de nodo obligatorio, registro literario preferido), puede crear `mod/skills/futures-engine/SKILL.md` con un override local. El SDK no fuerza el override.

---

## Relación con el ciclo documental

```
TEXTO EXTERNO
     ↓
documental-analysis → CORPUS (extrae, acumula)
     ↓
voice-crystallization → VOZ GENERADA (cristaliza)
     ↓
futures-engine → ESCENARIOS RAMIFICADOS (bifurca)
     ↓
universo propio → GRAFO PERSISTENTE (andamiaje conversacional)
     ↓
[decisión editorial del lore] → texto preservado en corpus/
```

Los escenarios generados por `futures-engine` son materia prima. Su integración en el corpus como lore es decisión del archivero, no del skill.

Si el veredicto o el evento futuro se produce y es documentado, los escenarios generados antes pasan a ser "caminos no tomados" — material dramático con valor archivístico propio. Se recomienda preservarlos con una marca temporal y un tag `[pre-veredicto]` o equivalente para que el corpus registre no solo lo que pasó sino lo que podría haber pasado.
