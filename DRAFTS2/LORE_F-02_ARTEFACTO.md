# LORE_F-02 — Artefacto pre-veredicto

> **Basado en hechos reales.**
> **Proyecto marco:** `Diseñador de universos`
> **Naturaleza:** artefacto derivado del caso semilla. No altera el conteo de 51 piezas ni sustituye al lore limpio.
> **Estado:** abierto — iteración v2 en curso (FEAT-04 completado, FEAT-05 pendiente).

---

## Objeto

Este documento abre la segunda mitad de `LORE_F.md` como artefacto narrativo pre-veredicto.

Su función no es fijar qué ocurrió después del `17-abr-2026`, sino diseñar una pieza dramática de hasta `7` minutos sostenida solo por el corpus ya documentado. La capa exterior asume el marco **Diseñador de universos**: un dispositivo artístico que toma un caso real, preserva su trazabilidad documental y lo abre en futuros posibles sin confundir bifurcación con hecho probado.

La pieza concreta resultante vive en [LORE_F-02_CORTO.md](LORE_F-02_CORTO.md).

---

## Encaje DRY

- El SDK y la separación `SDK / mod / lore` se toman de [INDICE_DRY_SDK_MOD_LORE.md](INDICE_DRY_SDK_MOD_LORE.md).
- La vista acumulativa del corpus y su disponibilidad textual se toman de [CORPUS_PREVIEW.md](CORPUS_PREVIEW.md).
- El hilo narrativo fuente es [LORE_F.md](LORE_F.md), que corta el caso entre el juicio `[T-12]` y el veredicto `[T-14]`.
- Este artefacto vive en `DRAFTS2/` porque es materia dramática pre-veredicto: no es lore limpio ni infraestructura reusable del mod.

---

## Ficha técnica

| Campo | Valor |
|-------|-------|
| Artefacto | `LORE_F-02` |
| Proyecto marco | `Diseñador de universos` |
| Pieza original | [LORE_F-02_CORTO.md](LORE_F-02_CORTO.md) — *Tres Lunes Para Una Misma Sala* |
| Piezas derivadas | 3 relatos desde universo-1 (ver § Resultados) |
| Grafo | [LORE_F-02_UNIVERSO.md](LORE_F-02_UNIVERSO.md) — 19 nodos, 4 ramas |
| Rama expandida | [universo/universo-1.md](universo/universo-1.md) — R4 contraataque, 7 nodos (R4.1–R4.7) |
| Tipo de pieza | Tratamiento de corto ramificado |
| Duración objetivo | `<= 6 min` (~900-1100 palabras) |
| Estado | Abierto — iteración v2 en curso |
| Corte temporal de partida | `17-abr-2026` |
| Hilo fuente | [LORE_F.md](LORE_F.md) |
| Corpus fuente | [CORPUS_PREVIEW.md](CORPUS_PREVIEW.md) — 51 piezas |
| Marco técnico de capa | [INDICE_DRY_SDK_MOD_LORE.md](INDICE_DRY_SDK_MOD_LORE.md) |
| Disponibilidad | Texto versionado en `DRAFTS2/` — 4 obras generadas |

---

## Reglas de construcción

1. No se introducen personajes fuera del corpus.
2. No se introducen hechos previos no documentados.
3. Las únicas novedades permitidas son **ramas futuras explicitadas como tales**.
4. La obra interior no usa marcas meta del lore ni discurso explicativo sobre el propio método.
5. La trazabilidad de cada tensión dramática debe poder volver a una pieza existente.
6. **Separación dato/relato obligatoria** — cada movimiento declara qué bloque trata como dato-ancla (cifra, hecho, pieza citada) y cuál como relato conectivo (ficción plausible, transición dramática). Ambos pueden coexistir, pero deben estar distinguibles. El dramaturgo no disuelve el dato entre prosa.

---

## Anti-ejemplos: los 4 cortos anteriores

Los relatos generados desde universo-1 v1 (17-abr-2026) documentan lo que NO repetir:

| Corto | Modelo | Problema principal |
|-------|--------|-------------------|
| *Once Mil Siete* | Claude Opus 4.6 | Intercambiable con los otros; parafraseo del grafo sin decisión narrativa |
| *El Peso del Reloj* | Gemini 3.1 Pro | Mismo arco, misma resolución, mismas consignas en el mismo orden |
| *El Lunes Que Tardó Un Año* | GPT-5.4 | Ejecución fiel del grafo = no autoría |
| *Tres Lunes Para Una Misma Sala* | (original pre-grafo) | 3 universos en 6 movimientos; demasiado largo (~2500 palabras) |

**Lección:** el grafo v1 determinaba el relato tan completamente que no dejaba espacio para omisión, énfasis o riesgo. El v2 debe dar al dramaturgo margen para elegir qué enfatizar y qué elidir.

---

## Piezas activas para la bifurcación

| Función | Piezas |
|---------|--------|
| Corte del hilo y estado de espera | [LORE_F.md](LORE_F.md), [LORE_T-12.md](LORE_T-12.md) |
| Hipótesis de lucro y su disputa | [LORE_T-09.md](LORE_T-09.md), [LORE_T-13.md](LORE_T-13.md) |
| Testimonio directo de Feo | [LORE_S-01.md](LORE_S-01.md), [LORE_S-02.md](LORE_S-02.md), [LORE_P-01.md](LORE_P-01.md) |
| Lectura jurídica y alternativa | [LORE_S-03.md](LORE_S-03.md), [LORE_N-04.md](LORE_N-04.md), [LORE_P-04.md](LORE_P-04.md) |
| Cruce mediático e institucional | [LORE_S-05.md](LORE_S-05.md) |
| Encuadres de prensa enfrentados | [LORE_N-02.md](LORE_N-02.md), [LORE_N-03.md](LORE_N-03.md) |
| Marco estructural de justicia | [LORE_R-09.md](LORE_R-09.md), [LORE_F.md](LORE_F.md) |
| Nodo corporativo acusador | [LORE_P-09.md](LORE_P-09.md) |
| Dato duro: 11.007 vs 40 | [LORE_S-10.md](LORE_S-10.md) |
| Hydra archiving: canal replicado | [LORE_S-11.md](LORE_S-11.md) |
| 2ª cola mediática: datos Cerezo | [LORE_S-09.md](LORE_S-09.md) |
| Ecosistema distribuidora independiente | [LORE_S-04.md](LORE_S-04.md) |
| Mainstream: Xataka + patron EGEDA | [LORE_N-05.md](LORE_N-05.md) |
| Segunda ola: indignación → filmotecas | [LORE_S-12.md](LORE_S-12.md) |
| Tándem legal ciudadano | [LORE_S-13.md](LORE_S-13.md) |
| Thiel invertido: monopolio y contrapeso | [LORE_R-10.md](LORE_R-10.md) |

---

## Nodos de bifurcación detectados

| # | Nodo | Tipo | Actores implicados | Direcciones posibles | Piezas ancla |
|---|------|------|-------------------|----------------------|--------------|
| N1 | Veredicto del lunes 21 | Decisión judicial | juez, Feo, Bravo, Cerezo/EGEDA | A: absolución o salida favorable / B: condena ejemplarizante / C: salida intermedia recurrible | `LORE_F`, `LORE_T-12`, `LORE_T-13` |
| N2 | Relato que se impone | Relato vs relato | defensa, acusación, prensa, analistas | A: preservación cultural / B: piratería-lucro / C: relato dividido | `LORE_N-02`, `LORE_N-03`, `LORE_S-03`, `LORE_S-05` |
| N3 | Destino del archivo | Paradoja recursiva | Zoowoman, audiencia, industria | A: no vuelve / B: se intenta borrar y reaparece distribuido / C: queda suspendido como ausencia | `LORE_S-01`, `LORE_S-02`, `LORE_T-13` |
| N4 | Duración real del castigo | Estrategia de parte | defensa, tribunal, esfera pública | A: cierre formal / B: cierre que amplifica / C: recurso que prolonga la pena temporal | `LORE_N-04`, `LORE_T-12`, `LORE_R-09` |

---

## Escenarios considerados

| Escenario | Nodos activados | Plausibilidad estructural | El relato que gana | Coste del escenario |
|-----------|-----------------|---------------------------|--------------------|---------------------|
| **La absolución sin regreso** | N1-A, N2-A, N3-A, N4-A | Media | Gana la tesis de que no hubo negocio suficiente | El archivo no reaparece por el solo hecho de ganar en sala |
| **La ceremonia ejemplar** | N1-B, N2-B, N3-B, N4-B | Media | Gana el encuadre disciplinario del castigo | El intento de cierre multiplica el fantasma del archivo |
| **La sala sigue abierta** | N1-C, N2-C, N3-C, N4-C | Alta | No gana un relato; gana la prolongación | La pena real sigue siendo el tiempo y el recurso |

La pieza v1 adoptaba una forma **ramificada**: un mismo lunes que se abría en tres universos mínimos (ver anti-ejemplos). Esa forma queda como referencia histórica. La **v2 se concentra en la rama R4** y sus 5 movimientos (ver § Forma elegida para la pieza — v2).

---

## Forma elegida para la pieza — v2

La pieza v2 adopta una estructura de **5 movimientos** (solo rama R4):

| Mov | Nombre | Estatuto | Contenido | Datos ancla |
|-----|--------|----------|-----------|-------------|
| **I** | El lunes preparado para aplastar | `dato` | Asimetría de fuerzas. El aparato llega con 4 años de ventaja. | `[T-12]`, `[T-13]` |
| **II** | El número que da la vuelta | `dato` | 11.007 vs 40. La aritmética invierte el relato. | `[S-10]`, `[N-05]`, `[S-09]` |
| **III** | El año ganado | `mixto` | Suspensión cautelar. Dos máquinas avanzan: tándem + ecosistema. | `[S-11]`, `[S-04]`, `[N-04]` |
| **IV** | El león se rinde | `dato` | Estrategia de desgaste. Retirada calculada. Sin sentencia = sin jurisprudencia. | `[N-04]` eje 9, `[S-10]` |
| **V** | La segunda ola y lo que queda | `relato` | Filmotecas federadas. Tensión nueva: cantones, filtros, gradación. | `[S-12]`, `[R-10]` |

**Constraints v2:**
- Duración: ≤ 6 min, 900-1100 palabras (los anteriores tenían ~2500-3000)
- Registro: narración omnisciente fría (confirmado por BLOG.md: "menos chimi-chimi")
- 0 frases lapidarias tipo "el silencio judicial es la forma que tiene el sistema de..."
- La hydra es ecosistema, no dato de GB
- El cierre tiene tensiones nuevas (cantones, gradación), no utopía

La forma v1 (3 universos en 6 movimientos) queda como referencia histórica. La v2 se concentra en una sola rama (R4) con profundidad y margen de autoría.

---

## Proceso de documentación y disponibilidad

El artefacto se apoya en una situación anómala pero útil: el caso semilla tiene ya un corpus de `51` piezas y un hilo narrativo de primera mitad, pero no tiene aún sentencia incorporada. [CORPUS_PREVIEW.md](CORPUS_PREVIEW.md) funciona aquí como mapa acumulativo de categorías, tensiones y ausencias; [INDICE_DRY_SDK_MOD_LORE.md](INDICE_DRY_SDK_MOD_LORE.md) fija que `LORE_F.md` fue el primer artefacto compuesto del caso y que esta segunda mitad debe vivir todavía en la capa draft, no en la capa final del lore.

Por eso la disponibilidad de esta pieza es deliberadamente sobria: texto versionado, trazable, reusable para pasar a guion, sin disfrazar de hecho lo que aún es bifurcación.

---

## Resultados

### Grafo construido

El universo quedó formalizado en [LORE_F-02_UNIVERSO.md](LORE_F-02_UNIVERSO.md). Estructura final: 19 nodos, 10 arcos, 4 ramas post-pivote.

| Zona | Nodos | Contenido |
|------|-------|-----------|
| T=0 (presente) | 8 | Estado documentado del caso al 17-abr-2026 |
| X (pivote) | 4 direcciones | Veredicto con 4 salidas posibles (X-A…X-D) |
| R4 (contraataque) | 7 | Única rama expandida — [universo/universo-1.md](universo/universo-1.md) |
| R1–R3 | ejes heredados, sin nodos propios | Pendientes de diseño |

### Obras generadas

Pieza original pre-veredicto (3 universos mínimos en 6 movimientos, anterior al grafo):

- [LORE_F-02_CORTO.md](LORE_F-02_CORTO.md) — *Tres Lunes Para Una Misma Sala*

Tres relatos generados desde la rama R4 del grafo con 3 modelos distintos, mismas instrucciones, mismo protocolo:

| Relato | Modelo | Enlace |
|--------|--------|--------|
| *Once Mil Siete* | Claude Opus 4.6 | [LORE_F-02_CORTO-universo-1-claude-opus-4.md](LORE_F-02_CORTO-universo-1-claude-opus-4.md) |
| *El Peso del Reloj* | Gemini 3.1 Pro | [LORE_F-02_CORTO-universo-1-gemini-3.1-pro.md](LORE_F-02_CORTO-universo-1-gemini-3.1-pro.md) |
| *El Lunes Que Tardó Un Año* | GPT-5.4 | [LORE_F-02_CORTO-universo-1-gpt-5-4.md](LORE_F-02_CORTO-universo-1-gpt-5-4.md) |

### Diagnóstico

Los tres relatos recorren R4.1→R4.6 en el mismo orden, activan las mismas consignas del corpus y cierran con la misma paradoja recursiva (el caso se cerró sin sentencia, ergo sin jurisprudencia). Son intercambiables para un lector: la variación es de prosa, no de decisión narrativa.

El grafo determina el relato tan completamente que no deja espacio para que el modelo tome decisiones propias. El resultado es ejecución fiel del grafo, no autoría. Las tres piezas prueban que la infraestructura agéntica produce parafraseo del grafo con distinto estilo, no literatura con riesgo narrativo propio.

Esta observación no invalida el dispositivo: documenta su límite actual. El universo funciona como marco dramatúrgico y como trazabilidad documental. La generación de obra desde el universo requiere un protocolo que permita omisión, énfasis y riesgo — operaciones que el dramaturgo actual no contempla.

---

## Metadatos futures-engine

| Campo | Valor |
|---|---|
| Fecha de invocación | `2026-04-17` |
| Corpus fuente | `DRAFTS2/CORPUS_PREVIEW.md` |
| Hilo narrativo fuente | `DRAFTS2/LORE_F.md` |
| Corte temporal | Espera entre juicio (`9-abr-2026`) y veredicto (`21-abr-2026`) |
| Piezas del corpus al cierre | `51` |
| Nodos de bifurcación detectados | `4` |
| Escenarios generados | `3` (pre-veredicto) + `4` ramas post-pivote |
| Plausibilidad alta | `1` escenario (R3) |
| Plausibilidad media | `2` escenarios (R1, R2) |
| Plausibilidad baja | `1` escenario (R4) |
| Rama expandida | R4 — 7 nodos en [universo/universo-1.md](universo/universo-1.md) |
| Huecos abiertos en R4 | `1` sombra narrativa (H2); H1 resuelto, H3-H6 resueltos narrativamente |
| Nodos totales del grafo | `19` |
| Registro literario usado | `elipsis retrospectiva`, `narración omnisciente fría` |
| Paradojas recursivas identificadas | `3` |
| Obras generadas | `4` — 1 corto original + 3 relatos desde universo-1 |
| Modelos usados | Claude Opus 4.6, Gemini 3.1 Pro, GPT-5.4 |
| Diagnóstico de generación | Los 3 relatos desde el grafo son intercambiables: el protocolo produce parafraseo fiel, no autoría diferenciada |
| Reglas de construcción | 6 (Regla 6 añadida: separación dato/relato) |
| Anti-ejemplos | 4 cortos anteriores documentados como referencia negativa |
| Estado | Abierto — iteración v2 (FEAT-04 completado, FEAT-05 pendiente) |
