# LORE_F-02 — Artefacto pre-veredicto

> **Basado en hechos reales.**
> **Proyecto marco:** `Disenador de universos`
> **Naturaleza:** artefacto derivado del caso semilla. No altera el conteo de 48 piezas ni sustituye al lore limpio.
> **Estado:** cerrado — resultados producidos, diagnóstico incorporado.

---

## Objeto

Este documento abre la segunda mitad de `LORE_F.md` como artefacto narrativo pre-veredicto.

Su funcion no es fijar que ocurrio despues del `17-abr-2026`, sino disenar una pieza dramatica de hasta `7` minutos sostenida solo por el corpus ya documentado. La capa exterior asume el marco **Disenador de universos**: un dispositivo artistico que toma un caso real, preserva su trazabilidad documental y lo abre en futuros posibles sin confundir bifurcacion con hecho probado.

La pieza concreta resultante vive en [LORE_F-02_CORTO.md](LORE_F-02_CORTO.md).

---

## Encaje DRY

- El SDK y la separacion `SDK / mod / lore` se toman de [INDICE_DRY_SDK_MOD_LORE.md](INDICE_DRY_SDK_MOD_LORE.md).
- La vista acumulativa del corpus y su disponibilidad textual se toman de [CORPUS_PREVIEW.md](CORPUS_PREVIEW.md).
- El hilo narrativo fuente es [LORE_F.md](LORE_F.md), que corta el caso entre el juicio `[T-12]` y el veredicto `[T-14]`.
- Este artefacto vive en `DRAFTS2/` porque es materia dramatica pre-veredicto: no es lore limpio ni infraestructura reusable del mod.

---

## Ficha tecnica

| Campo | Valor |
|-------|-------|
| Artefacto | `LORE_F-02` |
| Proyecto marco | `Disenador de universos` |
| Pieza original | [LORE_F-02_CORTO.md](LORE_F-02_CORTO.md) — *Tres Lunes Para Una Misma Sala* |
| Piezas derivadas | 3 relatos desde universo-1 (ver § Resultados) |
| Grafo | [LORE_F-02_UNIVERSO.md](LORE_F-02_UNIVERSO.md) — 18 nodos, 4 ramas |
| Rama expandida | [universo/universo-1.md](universo/universo-1.md) — R4 contraataque, 6 nodos |
| Tipo de pieza | Tratamiento de corto ramificado |
| Duracion objetivo | `<= 7 min` |
| Estado | Cerrado con resultados y diagnostico |
| Corte temporal de partida | `17-abr-2026` |
| Hilo fuente | [LORE_F.md](LORE_F.md) |
| Corpus fuente | [CORPUS_PREVIEW.md](CORPUS_PREVIEW.md) — 48 piezas |
| Marco tecnico de capa | [INDICE_DRY_SDK_MOD_LORE.md](INDICE_DRY_SDK_MOD_LORE.md) |
| Disponibilidad | Texto versionado en `DRAFTS2/` — 4 obras generadas |

---

## Regla de construccion

1. No se introducen personajes fuera del corpus.
2. No se introducen hechos previos no documentados.
3. Las unicas novedades permitidas son **ramas futuras explicitadas como tales**.
4. La obra interior no usa marcas meta del lore ni discurso explicativo sobre el propio metodo.
5. La trazabilidad de cada tension dramatica debe poder volver a una pieza existente.

---

## Piezas activas para la bifurcacion

| Funcion | Piezas |
|---------|--------|
| Corte del hilo y estado de espera | [LORE_F.md](LORE_F.md), [LORE_T-12.md](LORE_T-12.md) |
| Hipotesis de lucro y su disputa | [LORE_T-09.md](LORE_T-09.md), [LORE_T-13.md](LORE_T-13.md) |
| Testimonio directo de Feo | [LORE_S-01.md](LORE_S-01.md), [LORE_S-02.md](LORE_S-02.md), [LORE_P-01.md](LORE_P-01.md) |
| Lectura juridica y alternativa | [LORE_S-03.md](LORE_S-03.md), [LORE_N-04.md](LORE_N-04.md), [LORE_P-04.md](LORE_P-04.md) |
| Cruce mediatico e institucional | [LORE_S-05.md](LORE_S-05.md) |
| Encuadres de prensa enfrentados | [LORE_N-02.md](LORE_N-02.md), [LORE_N-03.md](LORE_N-03.md) |
| Marco estructural de justicia | [LORE_R-09.md](LORE_R-09.md), [LORE_F.md](LORE_F.md) |
| Nodo corporativo acusador | [LORE_P-09.md](LORE_P-09.md) |
| Dato duro: 11.007 vs 40 | [LORE_S-10.md](LORE_S-10.md) |
| Hydra archiving: canal replicado | [LORE_S-11.md](LORE_S-11.md) |
| 2ª cola mediatica: datos Cerezo | [LORE_S-09.md](LORE_S-09.md) |
| Ecosistema distribuidora independiente | [LORE_S-04.md](LORE_S-04.md) |
| Mainstream: Xataka + patron EGEDA | [LORE_N-05.md](LORE_N-05.md) |

---

## Nodos de bifurcacion detectados

| # | Nodo | Tipo | Actores implicados | Direcciones posibles | Piezas ancla |
|---|------|------|-------------------|----------------------|--------------|
| N1 | Veredicto del lunes 21 | Decision judicial | juez, Feo, Bravo, Cerezo/EGEDA | A: absolucion o salida favorable / B: condena ejemplarizante / C: salida intermedia recurrible | `LORE_F`, `LORE_T-12`, `LORE_T-13` |
| N2 | Relato que se impone | Relato vs relato | defensa, acusacion, prensa, analistas | A: preservacion cultural / B: pirateria-lucro / C: relato dividido | `LORE_N-02`, `LORE_N-03`, `LORE_S-03`, `LORE_S-05` |
| N3 | Destino del archivo | Paradoja recursiva | Zoowoman, audiencia, industria | A: no vuelve / B: se intenta borrar y reaparece distribuido / C: queda suspendido como ausencia | `LORE_S-01`, `LORE_S-02`, `LORE_T-13` |
| N4 | Duracion real del castigo | Estrategia de parte | defensa, tribunal, esfera publica | A: cierre formal / B: cierre que amplifica / C: recurso que prolonga la pena temporal | `LORE_N-04`, `LORE_T-12`, `LORE_R-09` |

---

## Escenarios considerados

| Escenario | Nodos activados | Plausibilidad estructural | El relato que gana | Coste del escenario |
|-----------|-----------------|---------------------------|--------------------|---------------------|
| **La absolucion sin regreso** | N1-A, N2-A, N3-A, N4-A | Media | Gana la tesis de que no hubo negocio suficiente | El archivo no reaparece por el solo hecho de ganar en sala |
| **La ceremonia ejemplar** | N1-B, N2-B, N3-B, N4-B | Media | Gana el encuadre disciplinario del castigo | El intento de cierre multiplica el fantasma del archivo |
| **La sala sigue abierta** | N1-C, N2-C, N3-C, N4-C | Alta | No gana un relato; gana la prolongacion | La pena real sigue siendo el tiempo y el recurso |

La pieza seleccionada no fuerza una sola rama como verdad futura. Adopta una forma **ramificada**: un mismo lunes que se abre en tres universos minimos. Esa forma conserva el estatuto pre-veredicto y vuelve productivo el marco **Disenador de universos**.

---

## Forma elegida para la pieza

La pelicula adopta una estructura de `6` movimientos:

1. Una manana comun: el lunes del veredicto.
2. Primer universo: salida favorable sin restitucion del archivo.
3. Segundo universo: condena y efecto Streisand.
4. Tercer universo: salida recurrible y castigo por prolongacion.
5. Coda comun: la circulacion cultural persiste en los tres casos.
6. Corte antes del guion: este documento entrega tratamiento, no dialogado tecnico.

La forma elegida permite que la segunda mitad de `LORE_F` exista ya como pelicula concreta sin usurpar a `[T-14]` el lugar de hecho todavia no documentado.

---

## Proceso de documentacion y disponibilidad

El artefacto se apoya en una situacion anomala pero util: el caso semilla tiene ya un corpus de `48` piezas y un hilo narrativo de primera mitad, pero no tiene aun sentencia incorporada. [CORPUS_PREVIEW.md](CORPUS_PREVIEW.md) funciona aqui como mapa acumulativo de categorias, tensiones y ausencias; [INDICE_DRY_SDK_MOD_LORE.md](INDICE_DRY_SDK_MOD_LORE.md) fija que `LORE_F.md` fue el primer artefacto compuesto del caso y que esta segunda mitad debe vivir todavia en la capa draft, no en la capa final del lore.

Por eso la disponibilidad de esta pieza es deliberadamente sobria: texto versionado, trazable, reusable para pasar a guion, sin disfrazar de hecho lo que aun es bifurcacion.

---

## Resultados

### Grafo construido

El universo quedo formalizado en [LORE_F-02_UNIVERSO.md](LORE_F-02_UNIVERSO.md). Estructura final: 18 nodos, 10 arcos, 4 ramas post-pivote.

| Zona | Nodos | Contenido |
|------|-------|-----------|
| T=0 (presente) | 8 | Estado documentado del caso al 17-abr-2026 |
| X (pivote) | 4 direcciones | Veredicto con 4 salidas posibles (X-A…X-D) |
| R4 (contraataque) | 6 | Unica rama expandida — [universo/universo-1.md](universo/universo-1.md) |
| R1–R3 | ejes heredados, sin nodos propios | Pendientes de diseno |

### Obras generadas

Pieza original pre-veredicto (3 universos minimos en 6 movimientos, anterior al grafo):

- [LORE_F-02_CORTO.md](LORE_F-02_CORTO.md) — *Tres Lunes Para Una Misma Sala*

Tres relatos generados desde la rama R4 del grafo con 3 modelos distintos, mismas instrucciones, mismo protocolo:

| Relato | Modelo | Enlace |
|--------|--------|--------|
| *Once Mil Siete* | Claude Opus 4.6 | [LORE_F-02_CORTO-universo-1-claude-opus-4.md](LORE_F-02_CORTO-universo-1-claude-opus-4.md) |
| *El Peso del Reloj* | Gemini 3.1 Pro | [LORE_F-02_CORTO-universo-1-gemini-3.1-pro.md](LORE_F-02_CORTO-universo-1-gemini-3.1-pro.md) |
| *El Lunes Que Tardo Un Ano* | GPT-5.4 | [LORE_F-02_CORTO-universo-1-gpt-5-4.md](LORE_F-02_CORTO-universo-1-gpt-5-4.md) |

### Diagnostico

Los tres relatos recorren R4.1→R4.6 en el mismo orden, activan las mismas consignas del corpus y cierran con la misma paradoja recursiva (el caso se cerro sin sentencia, ergo sin jurisprudencia). Son intercambiables para un lector: la variacion es de prosa, no de decision narrativa.

El grafo determina el relato tan completamente que no deja espacio para que el modelo tome decisiones propias. El resultado es ejecucion fiel del grafo, no autoria. Las tres piezas prueban que la infraestructura agentica produce parafraseo del grafo con distinto estilo, no literatura con riesgo narrativo propio.

Esta observacion no invalida el dispositivo: documenta su limite actual. El universo funciona como marco dramaturgico y como trazabilidad documental. La generacion de obra desde el universo requiere un protocolo que permita omision, enfasis y riesgo — operaciones que el dramaturgo actual no contempla.

---

## Metadatos futures-engine

| Campo | Valor |
|---|---|
| Fecha de invocacion | `2026-04-17` |
| Corpus fuente | `DRAFTS2/CORPUS_PREVIEW.md` |
| Hilo narrativo fuente | `DRAFTS2/LORE_F.md` |
| Corte temporal | Espera entre juicio (`9-abr-2026`) y veredicto (`21-abr-2026`) |
| Piezas del corpus al cierre | `48` |
| Nodos de bifurcacion detectados | `4` |
| Escenarios generados | `3` (pre-veredicto) + `4` ramas post-pivote |
| Plausibilidad alta | `1` escenario (R3) |
| Plausibilidad media | `2` escenarios (R1, R2) |
| Plausibilidad baja | `1` escenario (R4) |
| Rama expandida | R4 — 6 nodos en [universo/universo-1.md](universo/universo-1.md) |
| Huecos abiertos en R4 | `4` (H2–H5; H1 resuelto por `[S-10]`, H6 parcial por `[N-05]`) |
| Nodos totales del grafo | `18` |
| Registro literario usado | `elipsis retrospectiva`, `narracion omnisciente fria` |
| Paradojas recursivas identificadas | `3` |
| Obras generadas | `4` — 1 corto original + 3 relatos desde universo-1 |
| Modelos usados | Claude Opus 4.6, Gemini 3.1 Pro, GPT-5.4 |
| Diagnostico de generacion | Los 3 relatos desde el grafo son intercambiables: el protocolo produce parafraseo fiel, no autoria diferenciada |
| Estado | Cerrado con resultados y diagnostico |
