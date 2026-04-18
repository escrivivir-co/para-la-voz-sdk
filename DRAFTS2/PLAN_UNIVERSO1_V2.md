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

| FEAT | Estado | Fecha | Modelo | Entrega |
|------|--------|-------|--------|---------|
| FEAT-01 | **Completado** | 18-abr-2026 | `GPT-5.4` | `LORE_S-12`, `LORE_S-13`, `LORE_R-10` + ampliación de `LORE_S-11` + actualización de índices |
| FEAT-02 | **Completado** | 18-abr-2026 | `GPT-5.4` | mejora de `LORE_S-04`, `LORE_N-04`, `LORE_S-09` y `CORPUS_PREVIEW.md` |
| FEAT-03 | **Completado** | 18-abr-2026 | `GPT-5.4` | rediseño de `universo/universo-1.md` y `LORE_F-02_UNIVERSO.md` con `R4.7`, cierre tenso y huecos resueltos |
| FEAT-03.5 | **Refactorizado** | 18-abr-2026 | `Gemini 3.1 Pro` | Corrección de ortografía/tildes en piezas nuevas y propuesta de "checkpoint de verificación dato/relato" antes de avanzar a FEAT-04. |
| FEAT-03.9 | **Completado** | 18-abr-2026 | `Claude Opus 4.6` | Fix ortográfico comprensivo real (73 fixes en 8 archivos: S-12, S-13, R-10, S-11, universo-1, S-04, N-04, S-09). Sincronización del artefacto a v2: estado abierto, 19 nodos, 7 nodos R4, Regla 6, anti-ejemplos, piezas nuevas en tabla activa. |
| FEAT-04 | Pendiente | — | — | Pipeline refresh: 04.1 CORPUS_PREVIEW → 04.2 LORE_F → 04.3 ARTEFACTO → 04.4 UNIVERSO → 04.5 universo-1 → 04.6 validación cruzada |
| FEAT-05 | Pendiente | — | — | Generar corto v2 desde pipeline limpio |

**Estado actual de la tarea:** FEAT-01 a FEAT-03.9 completados. FEAT-04 rediseñado como **pipeline refresh completo** — refrescar toda la cadena de dependencias (CORPUS_PREVIEW → LORE_F → ARTEFACTO → UNIVERSO → universo-1 → validación cruzada) para dejar el pipeline limpio antes de FEAT-05.

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

### FEAT-04 — Pipeline refresh: de piezas a grafo listo

**Objetivo:** Refrescar toda la cadena de dependencias de abajo arriba, dejando el pipeline listo para FEAT-05. El esquema de dependencias es:

```
PIEZAS (51)
    │
    ├──(composición narrativa)──→ LORE_F.md (hilo temporal)
    │                                  │
    └──(pipeline Bartleby)────→ CORPUS_PREVIEW.md (mapa estructural)
                                       │
                                       ├───────────────────┘
                                       ▼
                              LORE_F-02_ARTEFACTO.md (spec de construcción)
                                       │
                                       ▼
                              LORE_F-02_UNIVERSO.md (grafo de futuros)
                                       │
                                       ▼
                              universo/universo-1.md (rama R4 expandida)
                                       │
                                       ▼
                                  FEAT-05 (generar corto)
```

Cada tarea refresca un nivel y valida coherencia con el nivel anterior.

---

#### FEAT-04.1 — Recrear CORPUS_PREVIEW.md

**Input:** Las 51 piezas individuales (bloques A–E + ficheros de soporte).
**Acción:** Regenerar el mapa Bartleby completo:
- Linaje primario y por exclusión — ¿cambió algo con S-12, S-13, R-10, S-11 expandida?
- Taxonomía funcional — incorporar verbos nuevos (`desgastar`, `federar`, `replicar`) ya parcialmente añadidos, verificar árbol completo
- Mecanismos retóricos heredados — ¿las piezas nuevas aportan alguno nuevo?
- Emergencias sobre la tradición — la hydra como ecosistema, la segunda ola, el tándem legal
- Vista desde el hueco — ¿las piezas nuevas cerraron algún hueco o abrieron otro?
- Registro de merges — documentar la ingesta de las 7 piezas nuevas/mejoradas

**Criterio de aceptación:** CORPUS_PREVIEW dice 51 piezas en todas sus secciones, el árbol funcional refleja las categorías que S-12, S-13, R-10 y S-11 expandida añadieron, el registro de merges incluye las 7 piezas.

---

#### FEAT-04.2 — Verificar LORE_F.md

**Input:** LORE_F.md + las piezas nuevas/mejoradas.
**Acción:** Verificar si el hilo narrativo necesita actualizaciones. LORE_F cubre T-∞ → presente (17-abr). Las piezas nuevas (S-12, S-13, R-10) son piezas conceptuales y marcos de lectura, no eventos temporales — probablemente no alteran la secuencia de LORE_F. Las mejoras (S-04, N-04, S-09) amplían piezas que LORE_F ya referenciaba.

**Criterio de aceptación:** Confirmar que LORE_F no requiere cambios, o aplicar las actualizaciones mínimas necesarias. No reescribir el hilo.

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

### FEAT-05 — Generar el nuevo corto con @Dramaturgo Cortos

**Objetivo:** Invocar `mod/prompts/corto-universo.prompt.md` a través de `mod/agents/dramaturgo.agent.md` con el pipeline refrescado como input.

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
6. `mod/instructions/legislativa-universo.instructions.md` — datos duros, consignas, metáforas drenadas
7. Anti-ejemplos: los 4 cortos anteriores

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
FEAT-04 — Pipeline refresh (6 tareas):
    04.1 → Recrear CORPUS_PREVIEW
    04.2 → Verificar LORE_F
    04.3 → Re-derivar ARTEFACTO
    04.4 → Re-derivar UNIVERSO
    04.5 → Re-derivar universo-1
    04.6 → Validación cruzada
    ↓
FEAT-05 (generar corto desde pipeline limpio)
```

La cadena es estricta: cada nivel se deriva del anterior. Si 04.1 cambia el mapa, 04.3 cambia el artefacto, 04.4 cambia el grafo, 04.5 cambia la rama. Si 04.1 confirma que el mapa está bien, las tareas downstream son verificaciones rápidas.

---

## Notas de producción

- Los cortos anteriores no se borran. Son versiones del mismo universo con otro estado del grafo.
- El nuevo corto se sufijará con el modelo que lo genere (e.g., `claude-opus-4-3.md` si es la tercera versión Opus).
- Si el corto cumple criterios, se actualiza el campo "Obras generadas" en `LORE_F-02_UNIVERSO.md`.
- Las piezas nuevas (FEAT-01) entran en el conteo del corpus. Si se crean 3 nuevas → corpus pasa de 48 a 51 piezas.
