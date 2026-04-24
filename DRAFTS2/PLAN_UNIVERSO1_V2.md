# PLAN — Universo-1 v2: Sprint de mejora y regeneración del corto

> **Fecha:** 18-abr-2026
> **Objetivo:** Mejorar piezas, rediseñar universo-1 y generar un nuevo corto R4 que responda a la lista de noes/síes del BLOG.md
> **Artefacto destino:** `LORE_F-02_CORTO-universo-1-<modelo>.md` (nueva versión)
> **Método:** SCRUM por features — cada FEAT es una unidad de trabajo con criterio de aceptación

---

## Estado actual (baseline)

| Recurso | Estado | Notas |
|---------|--------|-------|
| Cortos existentes (4) | Generados 17-abr | opus-4, opus-4-2, gemini-3.1-pro, gpt-5-4 |
| Universo-1 (6 nodos R4) | Diseñado | R4.1→R4.6 + 6 huecos (H1 resuelto, H6 parcial) |
| Grafo principal | 18 nodos, 4 ramas | R1-R3 sin nodos propios |
| Corpus | 48 piezas | CORPUS_PREVIEW.md como mapa |
| Artefacto | Cerrado con diagnóstico | 5 reglas de construcción vigentes |

> ⚠️ **Nota:** estos valores son el baseline de inicio de sprint (17-abr). El estado actual tras FEAT-04 es: 51 piezas, 19 nodos, 7 R4, 6 reglas.

---

## Seguimiento de ejecución

| FEAT | Estado | Fecha | Modelo | Entrega |
|------|--------|-------|--------|---------|
| FEAT-01 | **Completado** | 18-abr-2026 | `GPT-5.4` | `LORE_S-12`, `LORE_S-13`, `LORE_R-10` + ampliación de `LORE_S-11` + actualización de índices |
| FEAT-02 | **Completado** | 18-abr-2026 | `GPT-5.4` | mejora de `LORE_S-04`, `LORE_N-04`, `LORE_S-09` y `CORPUS_PREVIEW.md` |
| FEAT-03 | **Completado** | 18-abr-2026 | `GPT-5.4` | rediseño de `universo/universo-1.md` y `LORE_F-02_UNIVERSO.md` con `R4.7`, cierre tenso y huecos resueltos |
| FEAT-03.5 | **Refactorizado** | 18-abr-2026 | `Gemini 3.1 Pro` | Corrección de ortografía/tildes en piezas nuevas y propuesta de "checkpoint de verificación dato/relato" antes de avanzar a FEAT-04. |
| FEAT-03.9 | **Completado** | 18-abr-2026 | `Claude Opus 4.6` | Fix ortográfico comprensivo real (73 fixes en 8 archivos: S-12, S-13, R-10, S-11, universo-1, S-04, N-04, S-09). Sincronización del artefacto a v2: estado abierto, 19 nodos, 7 nodos R4, Regla 6, anti-ejemplos, piezas nuevas en tabla activa. |
| FEAT-04 | **Completado** | 18-abr-2026 | `Gemini 3.1 Pro + GPT-5.4 + Claude Sonnet 4.6 + Claude Opus 4.6` | Pipeline refresh multi-agente: 04.1–04.6 cerradas. Pipeline limpio — ver adenda Sonnet + Opus. |
| FEAT-04.7 | **Completado** | 18-abr-2026 | `GPT-5.4` (diseño) + `Claude Opus 4.6` (revisión + implementación) | Pasada operatoria ejecutada: vista de sesión (macro-palancas, espina, 3 ejes drama, coste, punto ciego), cabeceras editoriales 7 nodos («título» + estatuto dato/relato/mixto), doble cabeza R4.3/R4.4, dualidad R4.7, estatuto en ARTEFACTO — [diseño](FEAT-04.7_ADENDA_EDICION_GRAFO.md) |
| FEAT-05 | Pendiente | — | — | Generar corto v2 desde pipeline limpio |
| FEAT-06 | **Completado** | 18-abr-2026 | `Claude Sonnet 4.6` | Cristalización: `@Pipeline` + `/refresh` + handoff de retorno — [detalle](FEAT-06_PIPELINE_REFRESH.md) |
| FEAT-07 | Pendiente | — | — | Expansión del grafo: 4 ramas × 7 nodos = 40 nodos + arcos cruzados — [detalle](#feat-07--expansión-del-grafo-de-19-a-40-nodos) |

**Estado actual de la tarea:** FEAT-01 a FEAT-04.7 y FEAT-06 completados. Pasada operatoria ejecutada por `Claude Opus 4.6`. Pipeline limpio (51 piezas / 19 nodos / 7 R4 / 0 tildes). **FEAT-05 se pospone hasta después de FEAT-07** — el grafo expandido producirá un corto más rico que el grafo de 19 nodos. FEAT-07 abierto: expansión masiva del grafo para que las 4 ramas tengan nodos propios.

---

## Diagnóstico: Lista de Noes extraída de BLOG.md

| # | No | Impacto en el plan |
|---|----|--------------------|
| N1 | **Relatos demasiado largos** — con la mitad basta (~900-1100 palabras, 5-6 min) | FEAT-05: constraint de longitud en el prompt |
| N2 | **Separación dato/relato borrosa** — o dato, o relato, o ambos bien marcados | FEAT-04: marcar en universo qué nodos son dato-ancla y cuáles son relato |
| N3 | **Falta arco dramático claro** — la tensión debe llevar al lector por un "diseño universo" plausible | FEAT-03: rediseñar la línea dramática completa |
| N4 | **Exceso de "chimi-chimi" y lapidarias** — más mover piezas, menos reinventar ruedas | FEAT-05: instrucción de registro al dramaturgo |
| N5 | **Feo y Cerezo importan por lo que representan**, no como personajes | FEAT-03: reencuadrar como fuerzas, no como individuos |
| N6 | **Falta el tramo de la "segunda ola"** — la Indignación 2.0 como motor del ecosistema | FEAT-01: pieza nueva o expansión |
| N7 | **Red de compartir media mal retratada** — no son lobos solitarios con discos duros | FEAT-02: mejorar piezas hydra/transmedia |
| N8 | **Falta el cierre aristotélico** — ni utopía ni distopía: gradación fuera de lo viciado | FEAT-03: nodo de cierre redesignado |
| N9 | **El equipo legal como arquetipo replicable** — Cristóbal/Bravo/Rubén/Facu como tándem-semilla | FEAT-01 o FEAT-02: pieza de estructura |
| N10 | **Falta la tensión final cantones vs unidad** — el relato no cierra en triunfo sino en nueva tensión | FEAT-03: nodo R4.6 expandido |

## Diagnóstico: Lista de Síes

> "Está todo. Solo hay que compactar, dramatizar, hacer más pop."

---

## FEATURES

---

### FEAT-01 — Piezas nuevas del lore

**Objetivo:** Crear las piezas que faltan para que el universo-1 tenga sustrato documental donde apoyarse sin inventar.

**Estado:** Completado (18-abr-2026)

| ID | Pieza propuesta | Contenido | Justificación |
|----|----------------|-----------|---------------|
| P-A | `LORE_S-12` — "La segunda ola: de la Indignación a las filmotecas de barrio" | Pieza conceptual que conecta el ciclo 15M/Occupy → Podemos (institucionalización sin persistencia de base) con una segunda ola donde las unidades no son plazas sino centros de actividad (transmedia, cine, audio). La institucionalización no disuelve el impulso porque las asambleas tienen tarea operativa. | Noes N6, N10. El BLOG.md describe esto extensivamente pero no existe como pieza del lore. Sin ella, el corto inventa. |
| P-B | `LORE_R-10` — "Thiel-NRx invertido: el monopolio como acumulación originaria" | Pieza de referencia. Marco teórico: enclosures digitales (Berners-Lee/SOLID, tecnofeudalismo Varoufakis), acumulación originaria (Marx) aplicada a catálogos de loss media, patrón Thiel como método (ley como herramienta del incumbente). Cerezo no inventó el método; lo copió. | Noes N5, N8. Da sustrato al arco "la posición de Cerezo se erosiona" sin que el corto tenga que explicar la teoría. |
| P-C | `LORE_S-13` — "El tándem: arquetipo de equipo legal ciudadano" | Cristóbal (estrategia), Bravo (sala), Rubén/FACUA (institucional), Facu (medios). No como personajes sino como roles replicables. La filmoteca de barrio replica este tándem a escala local: despacho + actividad + conexión institucional. | Noe N9. Evita que el corto presente al equipo como deus ex machina. |
| P-D | Mejora `LORE_S-11` — Inflar la hydra | Expandir la pieza existente: no son lobos solitarios. Linux, p2p, IPFS, federación ActivityPub, presencia distribuida (avatares, perfiles de opinión). La red ya existía antes de Zoowoman; Zoowoman era un nodo. El tecnofeudalismo subsumió esa red; la hydra es su resistencia orgánica. | Noe N7. Los cortos anteriores retratan la hydra como dato de GB; debe ser ecosistema. |

**Criterio de aceptación:** Cada pieza tiene marca `[S-xx]` o `[R-xx]`, sección de identificación, contenido DRY, y conexiones explícitas con el grafo.

**Estimación:** 4 piezas (3 nuevas + 1 mejora).

**Entregado:**

- `LORE_S-12.md` — segunda ola como pieza puente entre `[T-01]` / `[T-02]` y R4.
- `LORE_S-13.md` — tándem legal ciudadano como arquetipo operativo.
- `LORE_R-10.md` — matriz de lectura para monopolio, enclosure y contrapeso.
- Mejora de `LORE_S-11.md` — la hydra pasa de backup puntual a sustrato distribuido con nota de prudencia.

---

### FEAT-02 — Mejora de piezas existentes

**Objetivo:** Actualizar piezas que los cortos anteriores usaron mal o insuficientemente.

**Estado:** Completado (18-abr-2026)

| Pieza | Mejora | Razón |
|-------|--------|-------|
| `LORE_S-04` | Conectar "idea feliz" con FEAT-01 P-A (segunda ola). La distribuidora no nace en el vacío; nace en el ecosistema que la segunda ola produce. | Los cortos la presentan como ocurrencia aislada. |
| `LORE_N-04` | Añadir eje 9: "Estrategia de desgaste" — los 11.007 títulos no se ganan de golpe; cada uno es un caso que hay que investigar, evaluar, cursar. Tiempo de desgaste como arma de la defensa (>4 años que sufrió el feo). | El BLOG.md lo describe como "león que se rinde tras horas corriendo". Es material nuevo para el corto. |
| `LORE_S-09` | Conectar datos duros de Cerezo con el marco Thiel-NRx (FEAT-01 P-B). Los 300M€ TVE, los antidisturbios, el ático no son anécdotas; son síntomas del modelo de acumulación. | Los cortos usan los datos como color; deben ser estructura. |
| `CORPUS_PREVIEW.md` | Actualizar taxonomía con nuevos verbos: *desgastar* (estrategia temporal), *federar* (segunda ola), *replicar* (tándem legal). | El mapa debe reflejar las piezas nuevas. |

**Criterio de aceptación:** Piezas actualizadas con nuevas secciones; CORPUS_PREVIEW con nuevas entradas.

**Estimación:** 4 mejoras.

**Entregado:**

- `LORE_S-04.md` — la idea feliz queda conectada con la segunda ola y cambia de escala.
- `LORE_N-04.md` — nuevo eje 9: estrategia de desgaste a partir de `11.007 vs 40`.
- `LORE_S-09.md` — los datos duros de Cerezo pasan de anécdota a estructura y quedan anclados a `R-10`.
- `CORPUS_PREVIEW.md` — nuevas categorías y verbos: `desgastar`, `federar`, `replicar`.

---

### FEAT-03 — Rediseño del Universo-1 (grafo)

**Objetivo:** Modificar/expandir los nodos de `universo/universo-1.md` y el grafo de `LORE_F-02_UNIVERSO.md` para reflejar la línea dramática del BLOG.md.

**Estado:** Completado (18-abr-2026)

#### 3.1 — Nueva línea dramática (5 movimientos)

Reescritura del arco R4 como **5 movimientos** (no 6 como el corto original):

| Mov | Nombre | Contenido | Nodos activados | Datos ancla |
|-----|--------|-----------|-----------------|-------------|
| **I** | **El lunes preparado para aplastar** | Asimetría de fuerzas. El aparato llega con 4 años de ventaja. | 0.1, 0.5 | `[T-12]`, `[T-13]` |
| **II** | **El número que da la vuelta** | 11.007 vs 40. La aritmética invierte el relato. El relato de la piratería ya no está solo: aparece el de la extracción. | 0.4, 0.6, R4.1 | `[S-10]`, `[N-05]`, `[S-09]` |
| **III** | **El año ganado** | Suspensión cautelar. El tiempo deja de ser pena y se convierte en terreno. Dos máquinas avanzan: jurídica (tándem) + ciudadana (hydra→ecosistema). | R4.2, R4.3, R4.4 | `[S-11]`, `[S-04]`, `[N-04]` |
| **IV** | **El león se rinde** | Estrategia de desgaste: cada título es un caso. Cerezo calcula que el coste del disciplinamiento > beneficio. Retirada negociada. No hay sentencia → no hay jurisprudencia → la grieta queda abierta. | R4.5 | `[N-04]` eje 9 (nuevo), `[S-10]` |
| **V** | **La segunda ola y lo que queda** | Las filmotecas federadas. La segunda Indignación no se disuelve al institucionalizarse porque tiene tarea operativa. Pero hereda tensiones: cantones vs unidad, filtros de lo que se preserva, quién decide. Ni utopía ni derrota: un mundo con gradación aristotélica. | R4.6 + **R4.7 nuevo** | `[S-12]` (nueva), `[R-10]` (nueva) |

#### 3.2 — Nodos nuevos y modificados

| Nodo | Acción | Descripción |
|------|--------|-------------|
| **R4.1** | Modificar | Añadir la estrategia de desgaste como componente central: no es una sola demanda, es una apertura de 11.007 frentes potenciales. |
| **R4.3** | Modificar | Inflar la hydra: no lobos solitarios, sino ecosistema distribuido preexistente (Linux, p2p, ActivityPub). Zoowoman era un nodo de una red que ya existía. |
| **R4.5** | Modificar | La retirada como cálculo, no como rendición. Metáfora BLOG.md: "león que tras horas corriendo se rinde y ve al animalillo alejarse". |
| **R4.6** | Expandir | Dividir en dos: R4.6a (la federación modesta: Filmoteca Española + circuito territorial de diputaciones→autonomías→municipios→barrios) y R4.6b (la tensión nueva: cantones, "no era esto", la gradación fuera de lo viciado). |
| **R4.7** | **Nuevo** | Nodo de cierre: el mundo post-caso. No utopía. Contrapesación Thiel-NRx. Comercio privado vs nacionalización de infraestructura. La tensión que sigue abierta. El feo ya no es rol trágico; es pieza histórica. |

#### 3.3 — Huecos: resoluciones propuestas

| Hueco | Resolución propuesta |
|-------|---------------------|
| H2 (prácticas adquisición Mercury) | Se elide en el corto. Queda como sombra narrativa ("la pregunta que nadie contesta"). |
| H3 (forma jurídica contraataque) | Se compacta: "contraataque mercantil-cultural" sin doctrinalizar la vía exacta. |
| H4 (financiación) | Financiación mixta: crowdfunding + institucional. Sin detalle. |
| H5 (rol Bravo) | Bravo sostiene penal. Cristóbal dirige argumentario. Rubén frontea institucional. Facu frontea medios. Tándem claro. |
| H6 (Filmoteca Española) | RD 2016 como argumento necesario. No deseable: inevitable. |

**Criterio de aceptación:** `universo/universo-1.md` actualizado con nodos modificados/nuevos. `LORE_F-02_UNIVERSO.md` actualizado con arcos y metadatos.

**Estimación:** Reescritura significativa de 2 archivos.

**Entregado:**

- `universo/universo-1.md` — R4.1, R4.3, R4.4 y R4.5 reescritos; `R4.6` expandido; `R4.7` nuevo.
- `LORE_F-02_UNIVERSO.md` — grafo padre sincronizado con la rama v2, 19 nodos totales y huecos operativos reducidos.

---

### [Gemini 3.1 Pro (Preview)] Adenda y Propuestas de Nueva Carga (Refactor / FEAT-03.5)

Al revisar los entregables de `GPT-5.4`, la alineación con los "Noes" y restricciones dramáticas de `BLOG.md` es sólida en términos de diseño, pero requirió ajustes:

1. **Refactor Ejecutado:** Se corrigieron omisiones de tildes en el texto generado (falta de acentuación diacrítica en `LORE_S-12.md`, `LORE_R-10.md` y `universo-1.md`) para asegurar la calidad de la prosa dentro del corpus y evitar desvirtuar la cristalización posterior.
2. **Propuesta de Nueva Carga (FEAT-03.8 - Consolidación Dato/Relato en Artefacto):**  
   Para cumplir la exigencia de **N2** ("Separación dato/relato borrosa"), propongo inyectar en el artefacto (`LORE_F-02_ARTEFACTO.md` - correspondiente a **FEAT-04**) una **Matriz de Marcado Taxonómico Obligatoria**. Consiste en exigirle al futuro `@dramaturgo` que inicie cada uno de los 5 Movimientos (Mov I al V) declarando explícitamente qué bloque narrativo tratará como Dato, cuál será el Relato conectivo y si habrá salto. Esto debe estar forzado en el prompt del artefacto para que el dramaturgo no disuelva el dato entre "chimi-chimi".  
3. **Refinamiento de tensión (FEAT-03):** Se recomienda pasar ahora al `@dramaturgo` (o Dramaturgo Cortos) para mejorar el grafo en su conjunto (y el artefacto), asegurando que el conflicto en **R4.6b** (Filmoteca estatal vs Archivo activista) se mapee no como clímax moral idealizado, sino como tensión burocrática y procedimental basada en la legislación de "obras huérfanas", enlazando estrictamente con `[N-05]` y `[R-10]`.

---

### [Claude Sonnet 4.6] Revisión y Adenda — Fix ortográfico comprensivo + diagnóstico estructural (18-abr-2026)

#### Diagnóstico del estado real tras FEAT-01 / FEAT-02 / FEAT-03

Revisados todos los archivos entregados, el trabajo de GPT-5.4 es sólido en diseño: la arquitectura de piezas es correcta, los anclajes al corpus son precisos, el rediseño del universo-1 respeta los noes del BLOG.md. La entrega de Gemini fue parcial: el sed que ejecutó cubría **5 patrones en solo 3 archivos**, dejando sin tocar `LORE_S-13.md` por completo y con ~40 palabras sin tilde en el resto.

**Hallazgos concretos:**

| Archivo | Problema | Gravedad |
|---------|----------|----------|
| `LORE_S-13.md` | No estaba en el comando sed de Gemini — 100% sin corregir | Alta |
| `LORE_S-12.md` | Residuos: `institucionalizacion`, `pequenos`, `desproporcion`, `repeticion`, `Espanola`, `utopia`, `tension`, `publica` y ~15 más | Media |
| `LORE_R-10.md` | Residuos: `intuicion`, `posesion`, `concentracion`, `inversion`, `version`, `clasico`, `practicas`, `adquisicion` y ~10 más | Media |
| `universo/universo-1.md` | Residuos: `tandem`, `Cristobal`, `Ruben`, `pequenos`, `anos`, `calculo`, `pelicula`, `firmó` (incorrecto antes) | Media |
| Falso positivo | El sed habría producido "fórmula rutas propositivas" — `formula` era verbo (formular), no sustantivo; requería revertirse | Baja-media |

#### Refactor ejecutado (18-abr-2026)

1. **Fix comprensivo de tildes** — Script Python en dos pases sobre los 4 archivos afectados:
   - Pase 1: ~90 patrones (nombres propios, -ción/-ión, adjetivos, verbos, sustantivos)
   - Pase 2: residuos del pase 1 + revertido falso positivo `fórmula` → `formula` (verbo)
   - Resultado: LORE_S-13.md completamente corregido; los 3 restantes limpios de tildes pendientes

2. **Sin tocar el contenido**: el texto de los documentos no se modificó, solo se añadieron tildes. El diseño, los anclajes y la prosa de GPT-5.4 se preservan íntegros.

#### Propuesta de nueva carga: FEAT-03.9 — Precheck del Artefacto antes de FEAT-04

**Diagnóstico:** `LORE_F-02_ARTEFACTO.md` sigue en estado `cerrado` con los metadatos del ciclo v1:
- "6 movimientos" (ahora son 5)
- "18 nodos" (ahora son 19 con R4.7)
- Solo 5 reglas de construcción (falta Regla 6 de Gemini: separación dato/relato)
- No menciona los 4 cortos anteriores como anti-ejemplos para el Dramaturgo

Antes de que el Dramaturgo ejecute FEAT-04 (reescribir el artefacto en profundidad), conviene hacer un precheck rápido que alinee esos metadatos. De lo contrario, el Dramaturgo parte de un documento que contradice el grafo actual y puede reconstruir premisas ya superadas.

**Propuesta FEAT-03.9:** Actualizar solo los campos de metadatos del artefacto que están desincronizados con el grafo v2 — sin reescribir la lógica narrativa (eso es FEAT-04). Tiempo estimado: edición de 1 tabla y 1 lista en `LORE_F-02_ARTEFACTO.md`.

| Campo | Valor actual | Valor correcto |
|-------|-------------|----------------|
| Estado | `cerrado` | `abierto — iteración v2 en curso` |
| Forma elegida | 6 movimientos | 5 movimientos (R4 solo) |
| Nodos del grafo | 18 | 19 (con R4.7) |
| Reglas de construcción | 5 | 6 (añadir Regla 6 de separación dato/relato) |
| Referencia anti-ejemplo | ausente | 4 cortos anteriores como anti-ejemplo explícito |

---

### [Claude Sonnet 4.6] Segunda pasada — FEAT-04.3 completada (19-abr-2026)

#### Lo que hice

**Diagnóstico de partida:**
- GPT-5.4 en FEAT-04.2 declaró S-09, S-10, S-11 como "piezas de soporte no temporales" y no las incorporó al hilo. Error: las tres son eventos del período 14-16 de abril (antes del corte temporal de 17-abr) y pertenecen al §4 "el presente" de LORE_F.
- LORE_F-02_ARTEFACTO.md seguía con 3 datos incorrectos: 48 piezas, 18 nodos, R4 con 6 nodos. El texto de sección "Escenarios" mezclaba v1 y v2.
- Fix ortográfico de FEAT-03.9 no había tocado el artefacto: `artístico`, `bifurcación`, `decisión`, `absolución`, etc.

**LORE_F.md — laguna incorporada:**

| Sección añadida | Pieza | Contenido |
|-----------------|-------|-----------|
| "La segunda ola con datos duros" | `[S-09]` | Hilo David Bizarro 15-abr: datos Cerezo (TVE 300M, ático, 5 antidisturbios, ariete) |
| "El número que da la vuelta" | `[S-10]` | 11.007 reclamadas vs 40 con derechos — conectado a N-04 eje 9 |
| "El sustrato reacciona antes del veredicto" | `[S-11]` | Hydra archiving 14-15 abr — la cita de Feo sobre "el registro de ideas" |

Checklist actualizado: S-* 8/8 → 11/11, Total 44/44 → 47/47.

**LORE_F-02_ARTEFACTO.md — sync completo:**

| Fix | Detalle |
|-----|---------|
| Datos | 48 → 51 piezas, 18 → 19 nodos, R4: 6 → 7 nodos |
| Tildes | artístico, bifurcación, decisión, absolución, preservación, duración, documentación, diagnóstico, observación, categorías, situación, anómala, aquí, todavía, diseñar, mínimos, única, diseño |
| Texto v1/v2 | Párrafo de "tres universos mínimos" reescrito como referencia histórica; nota v2 redirige a 5 movimientos R4 |
| Tabla obras | "El Lunes Que Tardó Un Año" corregido |

#### Propuesta de nueva carga: FEAT-04.4 + 04.5 + 04.6 como pase único

UNIVERSO y universo-1.md fueron verificados en lectura y parecen correctos (19 nodos, 7 R4, metadatos sincronizados). La carga para el siguiente agente es:

**Una sola pasada de verificación + cierre:**
1. `04.4` — Leer UNIVERSO completo. Verificar que nodos, arcos, plausibilidades y metadatos son coherentes con el artefacto refrescado. Si hay diferencias, corregir.
2. `04.5` — Leer universo-1.md completo. Verificar que las piezas ancla de R4.1–R4.7 existen en CORPUS_PREVIEW. Si algún nodo cita piezas que no están (ej: `[?]`), resolverlo o marcarlo.
3. `04.6` — Pase cruzado: comprobar que los conteos son 51/19/7 en TODOS los ficheros y que no hay tildes faltantes en texto nuevo.

Tiempo estimado: un solo turno de lectura + verificación + anotación.

| Subtarea | Estado esperado | Acción más probable |
|----------|----------------|---------------------|
| `04.4` UNIVERSO | Solo verificación | Ningún cambio o 1-2 metadatos |
| `04.5` universo-1.md | Solo verificación | Verificar piezas ancla |
| `04.6` validación cruzada | Cierre de pipeline | Confirmar 0 inconsistencias → FEAT-05 desbloqueado |

---

### FEAT-04 — Pipeline refresh: de piezas a grafo listo

**Objetivo:** Refrescar toda la cadena de dependencias de abajo arriba, dejando el pipeline listo para FEAT-05. El esquema de dependencias es:

**Intervenciones registradas:** `Gemini 3.1 Pro` cerró `FEAT-04.1 — Recrear CORPUS_PREVIEW.md`. `GPT-5.4` cerró `FEAT-04.2 — Verificar LORE_F.md`.

**Motivo de asignación:** es la subtarea con menor riesgo de colisión entre agentes y desbloquea `FEAT-04.3` sin reabrir piezas ya estabilizadas en `CORPUS_PREVIEW`, `ARTEFACTO`, `UNIVERSO` o `universo-1`.

| Subtarea | Estado | Modelo | Nota operativa |
|----------|--------|--------|----------------|
| `04.1` | **Completado** | `Gemini 3.1 Pro` | Regeneración del mapa Bartleby `CORPUS_PREVIEW.md` consolidando 51 piezas, nuevo registro de merges y verbos emergentes (FEAT-01/02 integrados). |
| `04.2` | **Completada** | `GPT-5.4` | `LORE_F.md` verificado sin reescritura; sync mínimo aplicado: `N-04` pasa a 9 ejes, `S-04` queda anclada a `S-12`, nota aclaratoria sobre piezas de soporte fuera del `44/44` |
| `04.3` | **Completada** | `Claude Sonnet 4.6` | Artefacto refrescado: 3 fixes de datos (48→51 piezas, 18→19 nodos, R4 6→7 nodos), fix ortográfico completo, nota v1/v2 en sección escenarios. Laguna GPT-5.4 corregida en `LORE_F.md`: S-09/S-10/S-11 incorporadas como hechos del §4 (checklist 44→47). |
| `04.4` | **Completada** | `Claude Sonnet 4.6` | UNIVERSO verificado sin cambios — 19 nodos, 7 R4, metadatos correctos, piezas ancla validadas. |
| `04.5` | **Completada** | `Claude Sonnet 4.6` | universo-1.md verificado sin cambios — R4.1–R4.7 presentes, piezas ancla en CORPUS_PREVIEW, 0 tildes faltantes. |
| `04.6` | **Completada** | `Claude Sonnet 4.6` | Validación cruzada: 0 inconsistencias. 51/19/7 coherentes en todos los ficheros. Pipeline limpio para FEAT-05. |

```
                         PIEZAS (51)
                        /            \
                       /              \
          (pipeline Bartleby)    (composición narrativa)
                     /                  \
                    ▼                    ▼
       CORPUS_PREVIEW.md            LORE_F.md
       "mapa estructural"           "hilo temporal"
       (04.1)                       (04.2)
                    \                  /
                     \                /
                      ▼              ▼
              LORE_F-02_ARTEFACTO.md (spec de construcción)
              (04.3 — necesita ambos)
                          │
                          ▼
              LORE_F-02_UNIVERSO.md (grafo de futuros)
              (04.4)
                          │
                          ▼
              universo/universo-1.md (rama R4 expandida)
              (04.5)
                          │
                          ▼
                     FEAT-05 (generar corto)
```

**Nota sobre paralelismo:** CORPUS_PREVIEW y LORE_F son **hermanos**, no padre-hijo. Ambos se derivan de las piezas individuales. 04.1 y 04.2 pueden correr en paralelo. El primer nodo que necesita a los dos es 04.3 (ARTEFACTO). Esto coincide con el protocolo del skill `futures-engine`, que trata Fase 1 (lectura del corpus) y Fase 2 (lectura del hilo) como inputs separados.

Cada tarea refresca un nivel y valida coherencia con el nivel anterior.

---

#### FEAT-04.1 — Recrear CORPUS_PREVIEW.md

**Input:** Las 51 piezas individuales (bloques A–E + ficheros de soporte).
**Acción:** Recreado por `Gemini 3.1 Pro`. Regeneró el mapa Bartleby completo:
- Reflejó las 51 piezas (`P:9, S:13, N:5, T:14, R:10`) en estado inicial.
- Asentó los nuevos verbos funcionales en el árbol (`desgastar`, `federar`, `replicar`).
- Consolidó las emergencias procedentes de `[S-12]`, `[S-13]` y la matriz `[R-10]`.
- Modificó el registro de merges agregando la ingesta de la "Expansión v2".

**Estado:** Completado por `Gemini 3.1 Pro (Preview)` (18-abr). Queda validado el documento principal del que dependerán los artefactos y grafos posteriores.

---

#### FEAT-04.2 — Verificar LORE_F.md

**Input:** LORE_F.md + las piezas nuevas/mejoradas.
**Acción:** Verificar si el hilo narrativo necesita actualizaciones. LORE_F cubre T-∞ → presente (17-abr). Las piezas nuevas (S-12, S-13, R-10) son piezas conceptuales y marcos de lectura, no eventos temporales — probablemente no alteran la secuencia de LORE_F. Las mejoras (S-04, N-04, S-09) amplían piezas que LORE_F ya referenciaba.

**Criterio de aceptación:** Confirmar que LORE_F no requiere cambios, o aplicar las actualizaciones mínimas necesarias. No reescribir el hilo.

**Cierre registrado — `GPT-5.4` (18-abr-2026):** `LORE_F.md` no requería reescritura del hilo. Se aplicó únicamente sincronización mínima con el corpus refrescado: actualización de `N-04` de 8 a 9 ejes, incorporación explícita de la lectura de `S-04` como prototipo de segunda ola y nota de alcance para `S-12`, `S-13` y `R-10` como piezas de soporte no temporales.

---

#### FEAT-04.3 — Re-derivar ARTEFACTO desde CORPUS_PREVIEW + LORE_F

**Input:** CORPUS_PREVIEW.md actualizado (04.1) + LORE_F.md verificado (04.2).
**Acción:** Reescribir las secciones derivadas del artefacto:
- **Piezas activas para la bifurcación** — la tabla de funciones y piezas, re-derivada desde el corpus actualizado
- **Nodos de bifurcación** — ¿el mapa estructural actualizado revela nodos nuevos o modifica los existentes?
- **Escenarios considerados** — ¿los escenarios siguen siendo los mismos con el corpus de 51 piezas?
- **Forma elegida v2** — ¿la tabla de 5 movimientos necesita ajustes a la luz del corpus refrescado?

**No tocar:** Reglas de construcción (ya actualizadas en FEAT-03.9), anti-ejemplos (ya actualizados), ficha técnica de metadatos (ya sincronizada).

**Criterio de aceptación:** Las secciones derivadas del artefacto son coherentes con CORPUS_PREVIEW v51 y no con la versión anterior de v48.

---

#### FEAT-04.4 — Re-derivar UNIVERSO desde ARTEFACTO

**Input:** LORE_F-02_ARTEFACTO.md actualizado (04.3).
**Acción:** Verificar y actualizar el grafo:
- **T=0** — ¿los 8 nodos de estado presente siguen siendo correctos?
- **Arcos T=0 → X** — ¿los pesos y justificaciones se sostienen con el artefacto refrescado?
- **Pivote X** — ¿las 4 direcciones y sus plausibilidades siguen vigentes?
- **Ramas post-X** — ¿R1-R4 necesitan ajuste?
- **Metadatos** — nodos, arcos, fecha de actualización

**Criterio de aceptación:** UNIVERSO refleja fielmente los nodos y escenarios del artefacto refrescado. No hay nodos huérfanos ni arcos sin justificación.

---

#### FEAT-04.5 — Re-derivar universo-1.md desde UNIVERSO

**Input:** LORE_F-02_UNIVERSO.md actualizado (04.4).
**Acción:** Verificar y actualizar la rama R4 expandida:
- **7 nodos (R4.1–R4.7)** — ¿las piezas ancla siguen siendo las correctas? ¿algún dato nuevo del corpus cambia un nodo?
- **5 movimientos** — ¿la correspondencia nodo→movimiento se mantiene?
- **Huecos** — actualizar tabla de huecos si alguno se resolvió o apareció
- **Arcos internos** — verificar secuencia y pesos

**Criterio de aceptación:** universo-1.md es derivable limpiamente desde UNIVERSO sin contradicciones. Cada nodo tiene piezas ancla verificadas contra CORPUS_PREVIEW.

---

#### FEAT-04.6 — Validación cruzada

**Input:** Todos los ficheros actualizados (04.1–04.5).
**Acción:** Pase final de coherencia:
- Toda pieza `[X-nn]` citada en universo-1 existe en CORPUS_PREVIEW
- Todo nodo del UNIVERSO está anclado a piezas que existen
- El ARTEFACTO no referencia nodos o piezas inexistentes
- Los conteos (51 piezas, 19 nodos, 7 nodos R4) son consistentes en todos los ficheros
- 0 tildes faltantes en texto nuevo generado

**Criterio de aceptación:** 0 inconsistencias entre niveles. Pipeline limpio para FEAT-05.

---

### [Claude Sonnet 4.6] Adenda FEAT-04.4 / 04.5 / 04.6 — Pase de verificación y cierre (19-abr-2026)

#### Resultado de la verificación

**FEAT-04.4 — LORE_F-02_UNIVERSO.md:** Sin cambios. El UNIVERSO estaba correctamente sincronizado desde FEAT-03: 19 nodos (8 T=0 + 4 X + 7 R4), arcos correctos, X-D con anclas `[S-09]` `[S-10]` `[N-04]` `[R-10]`, metadatos coherentes con el artefacto refrescado en 04.3. Fecha de actualización "2026-04-18 FEAT-03" preservada (correcto — el contenido no cambió en 04.4, solo se verificó).

**FEAT-04.5 — universo/universo-1.md:** Sin cambios. Los 7 nodos R4.1–R4.7 están presentes con:
- Piezas ancla verificadas contra CORPUS_PREVIEW: `[S-09]` `[S-10]` `[S-11]` `[S-12]` `[S-13]` `[N-05]` `[R-10]` — todas en corpus.
- 0 tildes faltantes (falsos positivos: `resoluciones`, `adquisiciones` — llanas en -s, correctas).
- Tabla de huecos v2 actualizada: H1 resuelto, H2 sombra narrativa, H3-H6 resueltos narrativamente.

**FEAT-04.6 — Validación cruzada:**

| Conteo | CORPUS_PREVIEW | ARTEFACTO | UNIVERSO | universo-1.md |
|--------|----------------|-----------|----------|---------------|
| 51 piezas | ✅ | ✅ | — | — |
| 19 nodos | — | ✅ | ✅ (8+4+7) | — |
| 7 nodos R4 | — | ✅ | ✅ | ✅ (R4.1–R4.7) |
| Tildes | — | ✅ (04.3) | ✅ | ✅ |

**Resultado:** 0 inconsistencias. Pipeline limpio.

#### Estado del pipeline al cerrar FEAT-04

```
CORPUS_PREVIEW.md   ─── 51 piezas (P:9 S:13 N:5 T:14 R:10)   ✅ FEAT-04.1
LORE_F.md           ─── hilo 47/47 marcas, S-09/10/11 en §4   ✅ FEAT-04.2 + 04.3
LORE_F-02_ARTEFACTO ─── 51 piezas, 19 nodos, 7 R4, 6 reglas   ✅ FEAT-04.3
LORE_F-02_UNIVERSO  ─── 19 nodos, 4 ramas, X con 4 salidas    ✅ FEAT-04.4 (verificado)
universo/universo-1 ─── R4.1–R4.7, 7 huecos v2                ✅ FEAT-04.5 (verificado)
```

**FEAT-05 desbloqueado.** El @Dramaturgo Cortos puede leer el pipeline en orden y generar el corto v2.

---

### FEAT-04.7 — Addenda operatoria: sesión de edición del grafo

**Objetivo:** Diseñar un pase de rediseño del grafo ya refrescado para que resuene mejor con la lista de síes/noes de `BLOG.md`, sin reabrir la coherencia técnica de FEAT-04 y sin trasladar al prompt general la responsabilidad de diversificar recorridos.

**Detalle:** [FEAT-04.7_ADENDA_EDICION_GRAFO.md](FEAT-04.7_ADENDA_EDICION_GRAFO.md)

**Estado:** Aprobado con correcciones (Opus 4.6, 18-abr-2026). Correcciones: (1) R4.5 se mantiene como estación plena, (2) R4.7 no se bifurca formalmente, (3) el grafo mantiene 19 nodos.

**Nota:** esta carga no sustituye el refresh. Lo aprovecha. Su foco es operatorio y topológico: compactación, claridad de línea, doble cabeza de la segunda ola, cierre tenso jugable y `vista de sesión` para editar el grafo al gusto.

**Restricción fijada:** no se modifica `mod/prompts/corto-universo.prompt.md`. El caso general exhaustivo se preserva como comportamiento base. Si el usuario quiere una firma de rama, omisiones fuertes o un recorte más agresivo, eso se añade después como capa optativa cargada por el usuario, no como sustitución del modo general.

### [GPT-5.4] Recalibración del plan — grafo primero, prompt estable (18-abr-2026)

1. La similitud entre `LORE_F-02_CORTO-universo-1-gpt-5-4.md`, `LORE_F-02_CORTO-universo-1-gemini-3.1-pro.md` y `LORE_F-02_CORTO-universo-1-claude-opus-4.md` no se trata como anomalía. Es comportamiento esperado de la máquina mientras la obra derive de un mismo grafo con una espina dominante reconocible.
2. La creación del universo deriva del grafo. Por tanto, la palanca principal de rediseño está en `LORE_F-02_UNIVERSO.md`, `universo/universo-1.md` y en la `vista de sesión` aprobada, no en endurecer el prompt de generación.
3. El prompt `mod/prompts/corto-universo.prompt.md` conserva deliberadamente el caso exhaustivo general. Debe poder seguir existiendo una lectura que recorra casi toda la cadena cuando ese sea el comportamiento natural del grafo.
4. FEAT-04.7 queda recalibrado: no busca forzar divergencia artificial entre modelos, sino hacer más visible y manipulable la topología del grafo para que el usuario pueda decidir, desde el propio universo, cuándo quedarse en la espina exhaustiva y cuándo enfatizar o compactar zonas concretas.
5. Cualquier capa futura de selección explícita de rama, firma o poda se considerará extensión optativa posterior. No forma parte de este cierre del plan y no desplaza el comportamiento base del sistema.

---

### FEAT-05 — Generar el nuevo corto con @Dramaturgo Cortos

**Objetivo:** Invocar `mod/prompts/corto-universo.prompt.md` a través de `mod/agents/dramaturgo.agent.md` con el pipeline refrescado como input. La meta no es forzar una divergencia artificial respecto a los tres cortos previos, sino comprobar si el grafo recalibrado produce una pieza más compacta, más jugable y más nítida manteniendo intacto el caso general exhaustivo.

#### Parámetros de la invocación

```
/corto-universo universo-1
```

#### El Dramaturgo lee (en este orden)

1. `CORPUS_PREVIEW.md` — mapa Bartleby (refrescado en 04.1)
2. `LORE_F.md` — hilo narrativo
3. `LORE_F-02_ARTEFACTO.md` — spec de construcción (refrescado en 04.3)
4. `LORE_F-02_UNIVERSO.md` — grafo (refrescado en 04.4)
5. `universo/universo-1.md` — rama R4 (refrescado en 04.5)
6. `FEAT-04.7_ADENDA_EDICION_GRAFO.md` — aprobado con correcciones como pase operatorio previo
7. `mod/instructions/legislativa-universo.instructions.md` — datos duros, consignas, metáforas drenadas
8. Anti-ejemplos: los 4 cortos anteriores

#### Criterios de aceptación del corto

| Criterio | Medida |
|----------|--------|
| Longitud | 900-1100 palabras |
| Movimientos | 5 (I→V como FEAT-03) |
| Registro | Omnisciente frío, sin lapidarias |
| Dato/relato | Cada movimiento declara qué es dato-ancla y qué es relato conectivo |
| Arco dramático | Tragedia individual → comedia colectiva → tensión abierta |
| No "chimi-chimi" | 0 frases tipo "el silencio judicial es la forma que tiene el sistema de..." |
| No lobos solitarios | La hydra es ecosistema, no dato de GB |
| No utopía | El cierre tiene tensiones nuevas (cantones, gradación) |
| Grabable | Pensado para lectura en voz alta, corto de 5-6 min |
| Trazabilidad | Cada tensión vuelve a una pieza `[X-nn]` verificada en CORPUS_PREVIEW |
| Comportamiento base | Se acepta convergencia parcial con versiones anteriores si deriva del mismo grafo; la mejora buscada es de compactación, nitidez y uso de la máquina, no de divergencia forzada por prompt |

**Estimación:** 1 invocación del dramaturgo. Posible iteración si no cumple criterios.

---

## Orden de ejecución

```
FEAT-01 ✓ (piezas nuevas)
    ↓
FEAT-02 ✓ (mejoras de piezas)
    ↓
FEAT-03 ✓ (rediseño universo-1)
    ↓
FEAT-03.9 ✓ (precheck: tildes + sync metadatos artefacto)
    ↓
FEAT-04 — Pipeline refresh:
    04.1 (CORPUS_PREVIEW) ─┐
                            ├──→ 04.3 (ARTEFACTO) → 04.4 (UNIVERSO) → 04.5 (universo-1) → 04.6 (validación)
    04.2 (LORE_F) ─────────┘
    ↓
FEAT-04.7 (pase editorial opcional y recomendado sobre el grafo)
    ↓
FEAT-07 — Expansión del grafo:
    07.1 (R3 rama) ──────── agente barato, paralelo con nada — único bloqueante
    ↓
    07.2 (UNIVERSO master) ─ agente barato, secuencial tras 07.1
    ↓
    07.3 (ARTEFACTO sync) ── agente barato, secuencial tras 07.2
    ↓
    07.4 (legislativa-universo sync) ── agente barato, paralelo con 07.3
    ↓
    07.5 (validación cruzada) ── agente barato, tras 07.3 + 07.4
    ↓
FEAT-05 (generar corto desde grafo expandido — 40 nodos)
    ↓
FEAT-06 ✓ (cristalizar @Pipeline + /refresh + retorno desde Dramaturgo)
```

La cadena es estricta: cada nivel se deriva del anterior. Si 04.1 cambia el mapa, 04.3 cambia el artefacto, 04.4 cambia el grafo, 04.5 cambia la rama. Si 04.1 confirma que el mapa está bien, las tareas downstream son verificaciones rápidas.

---

### FEAT-06 — Cristalización: `@Pipeline` + `/refresh`

**Objetivo:** Agentizar el pipeline refresh como artefacto invocable. Crear `mod/agents/pipeline.agent.md`, `mod/prompts/refresh.prompt.md` y ampliar `mod/agents/dramaturgo.agent.md` con handoff explícito hacia refresh.

**Motivación:** El FEAT-04 demostró que el refresh de la cadena de derivados es un patrón recurrente. Cada vez que se tocan piezas, hay que regenerar toda la cadena mostrando deltas en cada paso. Codificarlo como agente elimina el cuello de botella manual.

**Capacidad nueva:** Handoffs bidireccionales: `@Pipeline` → `@Dramaturgo Cortos` / `@Archivero`; `@Dramaturgo Cortos` → `@Pipeline` para ejecutar refresh cuando detecte desincronización.

**Detalle completo:** [FEAT-06_PIPELINE_REFRESH.md](FEAT-06_PIPELINE_REFRESH.md)

---

### FEAT-07 — Expansión del grafo: de 19 a 40+ nodos

> **Diseñado por:** `Claude Opus 4.6`
> **Ejecutado por:** agentes baratos en paralelo (Sonnet, GPT-5.4, Gemini)

**Objetivo:** Expandir las 4 ramas del universo-1 para que cada una tenga 7 nodos propios con vista de sesión, cabeceras editoriales, ejes de drama y tensión dual de cierre — al mismo nivel de detalle que R4.

**Motivación:** El grafo actual tiene 19 nodos pero R1, R2 y R3 estaban vacíos (solo «ejes heredados, sin nodos propios»). Un grafo con solo 1 rama expandida de 4 produce cortos que convergen sobre esa rama. Para que el dramaturgo pueda elegir, combinar o contrastar ramas, las 4 deben estar al mismo nivel.

**Estado target:**

| Zona | Antes | Después |
|------|-------|---------|
| T=0 | 8 nodos | 8 nodos (sin cambios) |
| X (pivote) | 4 direcciones | 4 direcciones (sin cambios) |
| R1 (absolución) | 0 nodos | 7 nodos — [universo-1-r1.md](universo/universo-1-r1.md) |
| R2 (condena) | 0 nodos | 7 nodos — [universo-1-r2.md](universo/universo-1-r2.md) |
| R3 (sala abierta) | 0 nodos | 7 nodos — [universo-1-r3.md](universo/universo-1-r3.md) |
| R4 (contraataque) | 7 nodos | 7 nodos (sin cambios, ya anotado con vista de sesión) |
| **Arcos cruzados** | 0 | ~6-8 arcos entre ramas |
| **Total** | 19 | 40+ nodos + arcos cruzados |

---

#### 07.0 — Ejemplar: R1 y R2 (ya hechos por Opus)

`Claude Opus 4.6` escribió R1 y R2 antes de pararse a planificar. Se quedan como **plantilla de formato y profundidad** que los agentes baratos deben seguir para R3.

**Archivos generados:**

| Archivo | Nodos | Líneas | Contenido |
|---------|-------|--------|-----------|
| `universo/universo-1-r1.md` | R1.1–R1.7 | 185 | Absolución sin regreso. Victoria pírrica. Paradoja: el sistema puede destruir sin condenar. |
| `universo/universo-1-r2.md` | R2.1–R2.7 | 201 | Condena ejemplar. Efecto Streisand máximo. Paradoja: el mártir involuntario. |

**Formato obligatorio para cada rama** (extraído de R1/R2 como plantilla):

1. Cabecera con: naturaleza, grafo padre, dirección de X, plausibilidad, piezas ancla
2. Vista de sesión: macro-palancas desde X, espina editorial con `[dato]`/`[mixto]`/`[relato]`, 3 ejes de drama, coste de la rama, punto ciego, sombras deliberadas
3. 7 nodos con: título en «», subtítulo factual, estatuto narrativo, movimiento, tipo, actores, plausibilidad, prosa narrativa
4. Tensión dual en el nodo de cierre (tabla salida A / salida B)
5. Arcos cruzados explícitos donde una rama puede colapsar en otra

**Arcos cruzados ya documentados en R1/R2:**

| Arco | Desde | Hacia | Condición |
|------|-------|-------|-----------|
| R1.4 → R3.1 | R1 (absolución) | R3 (sala abierta) | Si EGEDA recurre, R1 colapsa en R3 |
| R2.4 → R3.2 | R2 (condena) | R3 (sala abierta) | Si la escalada se prolonga, R2 converge con R3 |

---

#### 07.1 — Crear rama R3: «La sala sigue abierta» (7 nodos)

**Asignable a:** `GPT-5.4` o `Claude Sonnet 4.6` o `Gemini 3.1 Pro`
**Paralelizable:** sí — no depende de ningún otro 07.x
**Input:** `universo/universo-1-r1.md` (como ejemplar de formato), `LORE_F-02_UNIVERSO.md`, `CORPUS_PREVIEW.md`, `BLOG.md`
**Output:** `universo/universo-1-r3.md`

**Briefing para el agente:**

R3 es la rama de **mayor plausibilidad** (alta) según el artefacto. Dirección X-C: resolución intermedia que no cierra (condena parcial, o sentencia recurrible, o sobreseimiento técnico).

R3 es la rama del **tiempo** — el caso no se resuelve, se prolonga. Es la rama donde R1 y R2 pueden colapsar (los arcos cruzados R1.4→R3 y R2.4→R3 ya están documentados).

**Espina sugerida** (el agente puede ajustar):

| Nodo | Nombre sugerido | Estatuto | Contenido |
|------|----------------|----------|-----------|
| R3.1 | «El veredicto gris» | `dato` | Resolución ambigua: ni absolución clara ni condena plena. Sentencia recurrible. |
| R3.2 | «La apelación infinita» | `dato` | Recurso de ambas partes. Audiencia Provincial. Posible casación. X se desplaza años. |
| R3.3 | «El limbo jurídico» | `mixto` | Feo no es culpable ni inocente. Vive en suspensión penal. La pena es el proceso. `[R-09]` |
| R3.4 | «La fatiga mediática» | `relato` | La cobertura decae. El caso pierde urgencia. La amplificación `[S-05]` se agota sin resolución. |
| R3.5 | «El desgaste mutuo» | `mixto` | Ambas partes gastan. EGEDA gasta en mantener la acusación. Feo gasta en existir dentro del sistema. |
| R3.6 | «La negociación en la sombra» | `relato` | El acuerdo extrajudicial reaparece. La oferta de ene-2025 `[N-05]` como precedente. |
| R3.7 | «La grieta permanente» | `relato` | Cierre: la sala nunca se cierra del todo. El caso se convierte en la cosa juzgada que nadie juzgó. |

**3 ejes de drama obligatorios:**
- **Relato vs relato:** ningún relato gana. Ambos se desgastan. El relato que prevalece es: «esto no se resuelve».
- **Portería móvil:** el sistema judicial se mueve (cambios de juez, nuevas interpretaciones, jurisprudencia sobrevenida) sin que ningún movimiento cierre.
- **Paradoja recursiva:** el proceso que debería resolver produce más proceso. El caso se alimenta de sí mismo.

**Arcos cruzados esperados:**
- R3.6 (negociación) puede converger con R4.5 (retirada calculada) si el acuerdo incluye cesiones
- R3.4 (fatiga) puede producir el escenario R1.6 (hydra en reposo) si la movilización decae

**Criterio de aceptación:**
1. 7 nodos con formato idéntico a `universo-1-r1.md`
2. Vista de sesión completa (palancas, espina, ejes, coste, punto ciego, sombras)
3. Tensión dual en R3.7
4. Al menos 2 arcos cruzados hacia otras ramas
5. Todas las piezas ancla verificadas contra CORPUS_PREVIEW
6. 0 tildes faltantes

---

#### 07.2 — Expandir UNIVERSO.md: grafo maestro con 4 ramas

**Asignable a:** `Claude Sonnet 4.6` o `GPT-5.4`
**Paralelizable:** NO — depende de 07.1 (R3 debe existir)
**Input:** `LORE_F-02_UNIVERSO.md`, `universo/universo-1.md` (R4), `universo/universo-1-r1.md`, `universo/universo-1-r2.md`, `universo/universo-1-r3.md`
**Output:** `LORE_F-02_UNIVERSO.md` actualizado

**Briefing para el agente:**

Actualizar el grafo maestro con:

1. **Tabla de ramas completa** — las 4 ramas con 7 nodos cada una, enlace a archivo, plausibilidad y estado

2. **Sección «Arcos cruzados entre ramas»** — tabla nueva:

| Arco | Desde | Hacia | Condición | Plausibilidad |
|------|-------|-------|-----------|---------------|
| R1→R3 | R1.4 (EGEDA recurre) | R3.1 | La absolución no es firme | alta |
| R2→R3 | R2.4 (escalada) | R3.2 | La apelación se prolonga | alta |
| R3→R4 | R3.6 (negociación) | R4.5 | El acuerdo incluye cesiones | media |
| R3→R1 | R3.4 (fatiga) | R1.6 | La movilización decae | media |
| ... | (completar desde los archivos de rama) | | | |

3. **Vista de sesión compacta por rama** — 1 línea por rama con espina + coste + punto ciego (como la que ya tiene R4)

4. **Metadatos actualizados** — nodos totales, arcos totales, ramas activas, obras generadas

5. **Diagrama ASCII** del grafo completo (las 4 ramas desde X con arcos cruzados)

**No tocar:** secciones T=0 y X (no cambian). La sección de R4 ya tiene vista de sesión (FEAT-04.7) — no reescribir, solo verificar coherencia.

**Criterio de aceptación:**
1. Las 4 ramas visibles con enlace a sus archivos
2. Tabla de arcos cruzados con ≥6 arcos
3. Vista de sesión por rama (4 ramas × 1 bloque compacto)
4. Metadatos: nodos ≥40, arcos actualizados
5. Diagrama ASCII legible

---

#### 07.3 — Sync ARTEFACTO con grafo expandido

**Asignable a:** `Claude Sonnet 4.6` o `Gemini 3.1 Pro`
**Paralelizable:** NO — depende de 07.2
**Input:** `LORE_F-02_ARTEFACTO.md`, `LORE_F-02_UNIVERSO.md` (actualizado en 07.2)
**Output:** `LORE_F-02_ARTEFACTO.md` actualizado

**Briefing para el agente:**

Actualizar las secciones del artefacto que reflejan el estado del grafo:

| Sección | Cambio |
|---------|--------|
| Ficha técnica | Nodos: 19 → 40+. Ramas expandidas: R4 → R1+R2+R3+R4. |
| Tabla «Resultados — Grafo construido» | Añadir fila por rama nueva con nodos, contenido y enlace |
| Metadatos futures-engine | Nodos totales, arcos, ramas activas, huecos |
| Sección «Escenarios considerados» | Ya existe pero sin detalle de nodos. Añadir referencia a los archivos de rama. |
| Tabla de movimientos (5 movimientos) | SIN CAMBIOS — los movimientos son de R4, que no se toca |

**No tocar:** reglas de construcción, anti-ejemplos, forma elegida (siguen siendo 5 movimientos de R4). La expansión del grafo amplía el universo de posibilidades pero no cambia la spec de la pieza objetivo.

---

#### 07.4 — Sync legislativa-universo.instructions.md

**Asignable a:** `Gemini 3.1 Pro` o `Claude Sonnet 4.6`
**Paralelizable:** SÍ — puede correr en paralelo con 07.3
**Input:** `mod/instructions/legislativa-universo.instructions.md`, los 4 archivos de rama
**Output:** `mod/instructions/legislativa-universo.instructions.md` actualizado

**Briefing para el agente:**

Actualizar las instrucciones del mod:

1. Conteo de piezas: 48 → 51 (ya debería estar, verificar)
2. **Sección nueva: «Estado del grafo expandido»** — conteo 40+ nodos, 4 ramas con 7 nodos c/u, arcos cruzados
3. Tabla de huecos: actualizar con huecos de R1, R2, R3 (no solo R4)
4. **Sección nueva: «Arcos cruzados para el dramaturgo»** — las convergencias entre ramas que el corto podría usar

---

#### 07.5 — Validación cruzada del grafo expandido

**Asignable a:** cualquier agente barato
**Paralelizable:** NO — depende de 07.2 + 07.3 + 07.4
**Input:** todos los archivos de universo + ARTEFACTO + UNIVERSO + instructions

**Briefing para el agente:**

Validación cruzada final. Tabla de checks:

| Check | Archivos | Qué validar |
|-------|----------|-------------|
| Conteo nodos | UNIVERSO, ARTEFACTO, instructions | ≥40 en todos |
| Piezas ancla | R1, R2, R3, R4 | Toda marca `[X-nn]` existe en CORPUS_PREVIEW |
| Arcos cruzados | R1→R3, R2→R3, R3→R4, etc. | Los nodos referenciados existen en el archivo destino |
| Formato | R1, R2, R3 | Idéntico al formato de R4 (vista de sesión, cabeceras, ejes, tensión dual) |
| Tildes | R1, R2, R3 | 0 faltantes |
| Coherencia de plausibilidades | UNIVERSO | R3 alta, R1/R2 media, R4 baja→media |
| Tabla de obras | ARTEFACTO | 4 cortos anteriores + referencia a los nuevos archivos de rama |

**Criterio de aceptación:** 0 inconsistencias entre niveles. Grafo expandido limpio para FEAT-05.

---

#### Mapa de paralelismo y asignación

```
                        07.0 R1+R2 (Opus — HECHO)
                             │
                             ▼
                        07.1 R3 ←── agente barato A
                             │
                             ▼
              ┌──────── 07.2 UNIVERSO ←── agente barato B
              │              │
              │              ▼
    07.4 instructions   07.3 ARTEFACTO ←── agente barato C (o B)
    (agente barato D)        │
              │              │
              └──────┬───────┘
                     ▼
               07.5 validación ←── agente barato (cualquiera)
```

**Coste estimado por tarea:**

| Tarea | Modelo recomendado | Razón |
|-------|-------------------|-------|
| 07.1 R3 | `GPT-5.4` | Fuerte en prosa narrativa, conoce el universo del sprint |
| 07.2 UNIVERSO | `Claude Sonnet 4.6` | Bueno en sync de metadatos y tablas |
| 07.3 ARTEFACTO | `Gemini 3.1 Pro` | Tarea mecánica de sync, el más barato |
| 07.4 instructions | `Gemini 3.1 Pro` | Tarea mecánica, paralelo con 07.3 |
| 07.5 validación | `Claude Sonnet 4.6` | Bueno en validación cruzada (demostrado en FEAT-04.4–04.6) |

**Total de invocaciones Opus:** 0. Todo delegado.

**Criterio de aceptación:** `/refresh` invocable, ejecuta los 6 pasos del protocolo, muestra delta en cada nivel, para si no hay cambios, ofrece handoffs al terminar. `@Dramaturgo Cortos` expone además un handoff de "Ejecutar refresh del pipeline" en lugar de parchear desincronizaciones dentro del propio agente.

**Dependencia:** Ninguna. FEAT-06 ya está completado.

---

## Notas de producción

- Los cortos anteriores no se borran. Son versiones del mismo universo con otro estado del grafo.
- El nuevo corto se sufijará con el modelo que lo genere (e.g., `claude-opus-4-3.md` si es la tercera versión Opus).
- Si el corto cumple criterios, se actualiza el campo "Obras generadas" en `LORE_F-02_UNIVERSO.md`.
- Las piezas nuevas (FEAT-01) entran en el conteo del corpus. Si se crean 3 nuevas → corpus pasa de 48 a 51 piezas.
