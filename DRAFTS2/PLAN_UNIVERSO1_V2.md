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

---

## Seguimiento de ejecución

| FEAT | Estado | Fecha | Entrega |
|------|--------|-------|---------|
| FEAT-01 | **Completado** | 18-abr-2026 | `LORE_S-12`, `LORE_S-13`, `LORE_R-10` + ampliación de `LORE_S-11` + actualización de índices |
| FEAT-02 | **Completado** | 18-abr-2026 | mejora de `LORE_S-04`, `LORE_N-04`, `LORE_S-09` y `CORPUS_PREVIEW.md` |
| FEAT-03 | **Completado** | 18-abr-2026 | rediseño de `universo/universo-1.md` y `LORE_F-02_UNIVERSO.md` con `R4.7`, cierre tenso y huecos resueltos |
| FEAT-04 | Pendiente | — | — |
| FEAT-05 | Pendiente | — | — |

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

### FEAT-04 — Actualizar el Artefacto

**Objetivo:** Abrir `LORE_F-02_ARTEFACTO.md` para reflejar la v2 del universo.

| Cambio | Detalle |
|--------|---------|
| Estado | De "cerrado" a "abierto — iteración v2" |
| Forma elegida | De 6 movimientos (corto original R1-R3) a 5 movimientos (R4 solo) |
| Duración | Target ≤ 6 min, 900-1100 palabras |
| Regla añadida | **Regla 6:** Separación dato/relato explícita — cada movimiento puede usar dato O relato O ambos, pero marcado. |
| Registro | Narración omnisciente fría (confirmado por BLOG.md: "menos chimi-chimi") |
| Constraint de longitud | Max 1100 palabras (los anteriores tenían ~2500-3000) |

**Criterio de aceptación:** Artefacto actualizado, coherente con el nuevo grafo.

**Estimación:** Edición contenida de 1 archivo.

---

### FEAT-05 — Generar el nuevo corto con @Dramaturgo Cortos

**Objetivo:** Invocar `mod/prompts/corto-universo.prompt.md` a través de `mod/agents/dramaturgo.agent.md` con el universo-1 v2 como input.

#### Parámetros de la invocación

```
/corto-universo universo-1
```

#### Contexto extra para el prompt

- Referencia: los 4 cortos anteriores como anti-ejemplo (lo que NO repetir)
- Constraint: 900-1100 palabras, 5 movimientos, narración omnisciente fría
- Noes del BLOG.md como lista de exclusión explícita
- Síes: "compactar, dramatizar, hacer más pop"

#### Criterios de aceptación del corto

| Criterio | Medida |
|----------|--------|
| Longitud | 900-1100 palabras |
| Movimientos | 5 (I→V como FEAT-03) |
| Registro | Omnisciente frío, sin lapidarias |
| Dato/relato | Cada movimiento claramente anclado |
| Arco dramático | Tragedia individual → comedia colectiva → tensión abierta |
| No "chimi-chimi" | 0 frases tipo "el silencio judicial es la forma que tiene el sistema de..." |
| No lobos solitarios | La hydra es ecosistema, no dato de GB |
| No utopía | El cierre tiene tensiones nuevas (cantones, gradación) |
| Grabable | Pensado para lectura en voz alta, corto de 5-6 min |
| Trazabilidad | Cada tensión vuelve a una pieza `[X-nn]` existente |

**Estimación:** 1 invocación del dramaturgo. Posible iteración si no cumple criterios.

---

## Orden de ejecución

```
FEAT-01 (piezas nuevas)
    ↓
FEAT-02 (mejoras de piezas)
    ↓
FEAT-03 (rediseño universo-1)
    ↓
FEAT-04 (actualizar artefacto)
    ↓
FEAT-05 (generar corto)
```

Cada FEAT depende del anterior: las piezas nuevas alimentan el rediseño, el rediseño alimenta el artefacto, el artefacto alimenta al dramaturgo.

---

## Notas de producción

- Los cortos anteriores no se borran. Son versiones del mismo universo con otro estado del grafo.
- El nuevo corto se sufijará con el modelo que lo genere (e.g., `claude-opus-4-3.md` si es la tercera versión Opus).
- Si el corto cumple criterios, se actualiza el campo "Obras generadas" en `LORE_F-02_UNIVERSO.md`.
- Las piezas nuevas (FEAT-01) entran en el conteo del corpus. Si se crean 3 nuevas → corpus pasa de 48 a 51 piezas.
