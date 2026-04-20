---
layout: page
title: Pipeline — PARA LA VOZ
permalink: /restitutiva/pipeline/
---

{% assign gh = "https://github.com/escrivivir-co/para-la-voz-sdk/blob/mod/restitutiva/" %}
{% assign gh_leg = "https://github.com/escrivivir-co/para-la-voz-sdk/blob/mod/legislativa/" %}
{% assign scriptorium = "https://escrivivir-co.github.io/aleph-scriptorium/" %}

<a class="leg-back" href="{{ '/restitutiva/' | relative_url }}">← portada restitutiva</a>

<section class="leg-section">
  <h2>La future-machine</h2>
  <p>El SDK no es un programa que ejecutas. Es una <strong>caja con slots</strong>: cada slot es un agente + una carpeta de datos + unos ficheros de entrada y salida. El usuario le da a la rueda. La future-machine es el agente que orquesta los slots.</p>
  <p>En <strong class="pipeline-red">v1 (rojo)</strong> se hizo el subpipeline que el Archivero subsume en v2: <code>feed → análisis → corpus → poemas</code>.<br>
  En <strong>v2 (negro)</strong> se construye la pipeline completa: lore-db → corpus → grafo → universos → cortos.</p>
</section>

<div class="hero" style="min-height: auto; padding: 1.5rem;">
<div class="hero-inner">
  <div class="hero-pipeline">
    <div class="pipe-step">
      <div class="pipe-icon">P</div>
      <span class="pipe-label">Puzzle</span>
      <span class="pipe-count">validar</span>
    </div>
    <div class="pipe-arrow">→</div>
    <div class="pipe-step">
      <div class="pipe-icon">A</div>
      <span class="pipe-label">Archivero</span>
      <span class="pipe-count">corpus</span>
    </div>
    <div class="pipe-arrow">→</div>
    <div class="pipe-step">
      <div class="pipe-icon">G</div>
      <span class="pipe-label">Grafista</span>
      <span class="pipe-count">grafo</span>
    </div>
    <div class="pipe-arrow">→</div>
    <div class="pipe-step">
      <div class="pipe-icon">D</div>
      <span class="pipe-label">Demiurgo</span>
      <span class="pipe-count">universo</span>
    </div>
    <div class="pipe-arrow">→</div>
    <div class="pipe-step">
      <div class="pipe-icon">T</div>
      <span class="pipe-label">Dramaturgo</span>
      <span class="pipe-count">cortos</span>
    </div>
  </div>
  <p style="font-size: 0.65rem; opacity: 0.35; font-family: monospace; text-align: center; margin: 0;">Pipeline — orquesta el refresh de toda la cadena</p>
</div>
</div>

---

## Momentos del proceso

El pipeline tiene dos fases. La primera acumula datos sin relato. La segunda transforma la información en obra.

---

<section class="leg-section">
  <h2>Fase I — Datos sin relato</h2>
  <p>Desde un T pasado al presente. Algo pasa, el hype avanza, y el SDK se pone en modo lore-db.</p>
</section>

### a) Lore-DB — piezas, piezas, piezas

Algo sucede en el mundo y hay que capturarlo. El SDK entra en **modo lore-db**: el usuario trabaja las piezas individualmente, clasificándolas e identificándolas por tipo.

<div class="leg-pack">
  <h4>Tipos de pieza</h4>
  <ul>
    <li><strong>P</strong> — Personajes (actores del caso)</li>
    <li><strong>S</strong> — Piezas sociales (contexto, reacciones, comunidad)</li>
    <li><strong>N</strong> — Normativas (leyes, resoluciones, procedimientos)</li>
    <li><strong>T</strong> — Temporales (cronología, hitos, fechas)</li>
    <li><strong>R</strong> — Resolución (hipótesis, desenlaces, salidas)</li>
  </ul>
</div>

Cada pieza es un fichero `LORE_X-NN.md`. El usuario las escribe, las clasifica, las numera. El SDK no interviene todavía — solo organiza el almacén.

**Agente:** ninguno todavía (el usuario es el operador)
**Carpeta:** `DRAFTS2/LORE_*.md`
**Salida:** piezas tipadas en disco

---

### b) Loreador — la vista panorámica

Cuando hay muchas piezas, el **loreador** monta la pieza `LORE_F`: una vista compuesta, el hilo narrativo precompilado de todas las piezas. No es una pieza más — es el mapa del lore hasta la fecha.

El **Puzzle** valida todas las piezas contra el schema (tipos válidos, campos obligatorios, piezas fantasma vs huérfanas) y entrega un pack limpio al pipeline.

**Agente:** Puzzle (validación read-only)
**Entrada:** `LORE_INDEX.md` + piezas en disco
**Salida:** pack verificado con inventario + `LORE_F.md` (hilo compilado)

---

### c) Archivero — el subpipeline Bartleby

El Archivero Lore ejecuta el subpipeline que en <strong class="pipeline-red">v1 (rojo)</strong> era el pipeline entero: ingesta de las piezas y el corpus, análisis bartlebiano, generación de corpus acumulativo.

Pasa **todo el pack** por Bartleby — no pieza a pieza, sino como bloque. El resultado es el `CORPUS_PREVIEW.md`: un mapa sin juicio de lo que dicen las piezas, cómo lo dicen, y qué callan.

<div class="leg-pack">
  <h4>Lo que extrae Bartleby (5 secciones)</h4>
  <ul>
    <li><strong>I.</strong> La corriente — radiografía de la herencia (linaje primario + excluido)</li>
    <li><strong>II.</strong> Taxonomía funcional — árbol acumulativo de conceptos</li>
    <li><strong>III.</strong> Mecanismos retóricos — frecuencias y patrones</li>
    <li><strong>IV.</strong> Emergencias — lo que el texto abre sin cerrar</li>
    <li><strong>V.</strong> La vista desde el hueco — ausencias estructurales (lo que no puede contemplar)</li>
  </ul>
</div>

**Agente:** Archivero Lore (extiende al Archivero SDK) + Bartleby
**Entrada:** pack verificado por Puzzle + `LORE_F.md`
**Salida:** `CORPUS_PREVIEW.md` (mapa acumulativo)

---

<section class="leg-section">
  <h2>Fase II — Transformación</h2>
  <p>El SDK se transforma para hacer algo con la información. El corpus se convierte en estructura, la estructura en universos, los universos en obra.</p>
</section>

### d) Grafista — la red de bifurcaciones

El Grafista estructura las piezas y el corpus en una red: el **grafo de bifurcación dramatúrgica**. El grafo no tiene datos — solo referencia a ellos mediante `piezas_ancla`. Cualquier refresco posterior de las piezas traerá la nueva información automáticamente.

<div class="leg-pack">
  <h4>Anatomía del grafo</h4>
  <ul>
    <li>4 ficheros JSON: <code>nodos.json</code>, <code>arcos.json</code>, <code>huecos.json</code>, <code>index.json</code></li>
    <li>Tipos de nodo: <code>estado</code> (hecho probado), <code>bifurcacion</code> (pivote), <code>rama</code> (futuro posible), <code>hueco</code> (tensión abierta)</li>
    <li>Estratos temporales: <strong>T0</strong> (presente) → <strong>T0-X</strong> (descuento) → <strong>X</strong> (pivote) → <strong>X-T∞</strong> (futuros)</li>
    <li>Cada nodo enlaza obligatoriamente a piezas del corpus (trazabilidad)</li>
  </ul>
</div>

El concepto clave es la **gramática**: defines terminales de tu contexto y reglas ad-hoc para crear tu lenguaje-grafo. No hay un grafo universal — cada lore construye el suyo con su propia gramática.

**Agente:** Grafista
**Entrada:** `CORPUS_PREVIEW.md` + `LORE_F.md`
**Salida:** `DRAFTS2/grafo/` (4 JSON) + `LORE_F-02_ARTEFACTO.md` (spec de construcción)

---

### e) Demiurgo — instanciar el universo

Un universo es instanciar el grafo y rellenar variables para disponer un kit generador de cortos. El Demiurgo selecciona ramas del grafo, cierra o deja huecos, y fija los parámetros narrativos.

<div class="leg-pack">
  <h4>Parámetros de un universo</h4>
  <ul>
    <li><strong>Ramas activadas</strong> — qué futuros se exploran</li>
    <li><strong>Huecos resueltos</strong> — qué incógnitas se cierran, cuáles quedan como tensión</li>
    <li><strong>Piezas ancla</strong> — datos del corpus que sostienen cada nodo</li>
    <li><strong>Estatuto</strong> — cada nodo es <code>dato</code>, <code>relato</code> o <code>mixto</code></li>
    <li><strong>Registro literario</strong> — narración omnisciente fría, crónica, ensayo…</li>
    <li><strong>Consignas</strong> — frases del corpus activables (máx 1 vez cada una)</li>
    <li><strong>Léxico prohibido</strong> — metáforas drenadas que no deben usarse</li>
  </ul>
</div>

**Agente:** Demiurgo
**Entrada:** grafo (`DRAFTS2/grafo/`) + `LORE_F-02_ARTEFACTO.md`
**Salida:** `DRAFTS2/universo/universo-N.md`

---

### f) Dramaturgo — los cortos

El Dramaturgo toma un universo instanciado y genera la pieza literaria final. Puede generar tantas como desee. **Cada invocación con un modelo LLM distinto produce un fichero diferente** — el modelo se registra en la ficha de producción.

<div class="leg-pack">
  <h4>Benchmark: universo-2 × 3 modelos (rev-045, 27 nodos, 35 arcos)</h4>
  <ul>
    <li><strong>Claude Opus 4.6:</strong> 7/7 estaciones cubiertas · 10/11 datos del corpus · 3/3 consignas activadas</li>
    <li><strong>GPT-5.4:</strong> 7/7 estaciones · 10/11 datos · 3/3 consignas</li>
    <li><strong>Gemini 3.1 Pro:</strong> 4/7 estaciones explícitas · 5/11 datos · 1/3 consignas verbatim</li>
  </ul>
  <p style="font-size: 0.78rem; opacity: 0.6; margin-top: 0.5rem;">El grafo/universo hace que distintos modelos LLM produzcan cortos similares en cobertura de estaciones. La gramática es la que manda — no el modelo. <a href="{{ gh_leg }}DRAFTS2/LORE_F-02_CORTO-universo-2-REVIEW.md" target="_blank" rel="noopener">Ver review completa ↗</a></p>
</div>

**Agente:** Dramaturgo Cortos
**Entrada:** `universo/universo-N.md` + `LORE_F-02_ARTEFACTO.md`
**Salida:** `LORE_F-02_CORTO-[universo]-[modelo].md` (con ficha de producción)

---

<section class="leg-section">
  <h2>Artefactos de producción</h2>
  <p>Dos módulos adicionales organizan la carga de trabajo y la simulación del pipeline. El <a href="{{ scriptorium }}">Scriptorium</a> absorberá estos módulos junto con muchos otros preparados allí (<a href="{{ scriptorium }}">ver plugins ↗</a>).</p>
</section>

### Sala + Dossier

Organizas la carga de trabajo en carpetas de trabajo (dossiers) y las ejecutas en salas multi-agente de tipo **orquestador-agentes multi-round**.

<div class="leg-pack">
  <h4>Cómo funciona</h4>
  <ul>
    <li>El <strong>dossier</strong> es el diseño: PLAN, BACKLOG, TASKS, RESPUESTAS</li>
    <li>La <strong>sala</strong> es la ejecución: orquestador (Aleph) + agentes trabajadores</li>
    <li>Flujo: PO diseña dossier → tasks en tablero → Aleph arranca → agentes proponen → Aleph aprueba → entrega → revisión → cierre</li>
    <li>Handshake obligatorio al entrar (rastro en disco: <code>estado.md</code>)</li>
    <li>16 dossiers en legislativa: 8 SDK + 8 mod (corpus, cortos, engine-plan, future-machine, grafo, lore-db, universos)</li>
  </ul>
</div>

### Engine-plan — consola de la future-machine

En modo `log-std` funciona como UI donde la future-machine arranca como servicio virtual. Los agentes del pipeline se manifiestan como servicios conectados y reportan en formato log.

<div class="leg-pack">
  <h4>Formato de salida</h4>

```
[00:00:01] @Bartleby      │ READY │ slot_analysis: .agent.md ✓
[00:00:01] @Archivero     │ READY │ slot_corpus: .agent.md ✓
[00:00:02] @Grafista      │ BUILD │ slot_grafo: dossier grafo-sdk
[00:00:02] @Demiurgo      │ BUILD │ slot_universos: dossier universos-sdk
[00:00:02] @Dramaturgo    │ READY │ slot_obras: .agent.md ✓
[00:00:03] @Pipeline      │ BOOT  │ 5 READY, 4 BUILD, 0 MISS
```

  <p style="font-size: 0.78rem; opacity: 0.6; margin-top: 0.5rem;">Puedes inventar lenguajes afines al runtime de simulación. <a href="{{ gh_leg }}.github/skills/engine-plan/SKILL.md" target="_blank" rel="noopener">Ver skill ↗</a></p>
</div>

---

<section class="leg-section">
  <h2>El usuario en el pipeline</h2>
  <p>El usuario entiende qué flujo sigue la información y cuál es su intervención en relación a los ficheros y el material escrito.</p>
</section>

<div class="leg-pack">
  <h4>¿Dónde interviene el usuario?</h4>
  <ul>
    <li><strong>Lore-DB:</strong> el usuario escribe las piezas, las clasifica, las numera</li>
    <li><strong>Puzzle → Archivero:</strong> el usuario da a la rueda — los agentes validan, analizan, generan corpus</li>
    <li><strong>Grafista:</strong> el usuario define la gramática de su lore (terminales + reglas)</li>
    <li><strong>Demiurgo:</strong> el usuario elige ramas, fija parámetros, cierra huecos</li>
    <li><strong>Dramaturgo:</strong> el usuario aprueba el plan y puede pedir la misma pieza a distintos modelos</li>
    <li><strong>Pipeline:</strong> el usuario dispara el refresh cuando algo cambia</li>
  </ul>
</div>

<div class="leg-pack">
  <h4>¿Dónde le ayuda el SDK?</h4>
  <ul>
    <li>Organiza el almacén de piezas con schema y validación</li>
    <li>Analiza sin juicio (posición Bartleby)</li>
    <li>Estructura en grafo con trazabilidad al corpus</li>
    <li>Instancia universos con parámetros formales</li>
    <li>Genera obra literaria desde la gramática, no desde la intuición del modelo</li>
    <li>Mantiene la coherencia entre niveles con refresh automático</li>
  </ul>
</div>
