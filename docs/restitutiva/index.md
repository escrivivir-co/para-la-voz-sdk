---
layout: default
title: PARA LA VOZ — restitutiva
permalink: /restitutiva/
---

{% assign gh = "https://github.com/escrivivir-co/para-la-voz-sdk/blob/mod/restitutiva/" %}

<p class="leg-back"><a href="{{ '/' | relative_url }}">← inicio</a></p>

<section class="home-intro">

  <p class="home-kicker">mod/restitutiva · v1</p>
  <h1 class="home-title">Para la voz</h1>
  <p class="home-deck">SDK agéntico de análisis editorial — corriente <code>restitutiva</code></p>

  <aside class="home-note">
    <p class="home-note-label">v1 → v2</p>
    <p>Este pipeline procesa textos editoriales → análisis → corpus → poemas. En <strong>v2</strong> (<a href="{{ '/' | relative_url }}">legislativa</a>), el mismo flujo se integra como subcadena de un pipeline completo con base de lore, grafos de bifurcación y universos transmedia.</p>
    <table class="home-note-table">
      <tr><td>v1</td><td>textos editoriales → análisis → corpus → poemas</td></tr>
      <tr><td>v2</td><td>piezas tipadas → lore-db → corpus → grafo → universos → cortos</td></tr>
    </table>
    <p class="home-note-links">
      <a href="https://github.com/escrivivir-co/para-la-voz-sdk/tree/mod/restitutiva/corpus/editoriales">editoriales</a> ·
      <a href="https://github.com/escrivivir-co/para-la-voz-sdk/tree/mod/restitutiva/corpus/analisis">análisis</a> ·
      <a href="https://github.com/escrivivir-co/para-la-voz-sdk/blob/mod/restitutiva/corpus/corpus.md">corpus.md</a> ·
      <a href="https://github.com/escrivivir-co/para-la-voz-sdk/tree/mod/restitutiva/guiones">guiones</a>
    </p>
  </aside>

</section>

<section class="leg-section">
  <h2>corpus.md — la pieza central</h2>
  <p>El corpus es el artefacto que genera la future-machine: mapa acumulativo de taxonomía y linajes, construido edición a edición sin juicio editorial.</p>

  <dl class="home-meta">
    <div>
      <dt>Corriente</dt>
      <dd>marxismo-leninismo ortodoxo post-soviético, variante restitutiva</dd>
    </div>
    <div>
      <dt>Pipeline</dt>
      <dd>editorial → análisis Bartleby → corpus → guión → poema</dd>
    </div>
    <div>
      <dt>Estado</dt>
      <dd>4 editoriales procesadas · corriente estable (×4)</dd>
    </div>
  </dl>

  <div class="leg-pack">
    <h4>Métricas del corpus (n=4)</h4>
    <ul>
      <li><strong>33</strong> nodos de linaje primario (Marx → … → AABI)</li>
      <li><strong>17</strong> nodos excluidos (demarcación bilateral)</li>
      <li><strong>5</strong> registros taxonómicos: institucional, generacional, estético, imperialista, método</li>
      <li><strong>~60</strong> verbos de obligación acumulados</li>
      <li><strong>21</strong> mecanismos retóricos identificados</li>
      <li><strong>15</strong> emergencias (E.01–E.15)</li>
      <li><strong>6</strong> ausencias estructurales confirmadas ×4</li>
      <li><strong>1</strong> paradoja fundacional: la ausencia más persistente = la posición Bartleby</li>
    </ul>
  </div>
</section>

<section class="leg-section">
  <h2>Catálogo completo</h2>
  <p>Todas las piezas del pipeline — desde el editorial original hasta el poema cristalizado.</p>
  <a class="leg-cta" href="{{ '/restitutiva/catalogo/' | relative_url }}">ver catálogo →</a>
</section>

<section class="home-sdk">
  <h2>Pipeline</h2>
  <ol class="home-roadmap">
    <li><strong>Ingestión:</strong> En este modo se usaron editorales verbatim de la revista <em>PARA LA VOZ</em>.</li>
    <li><strong>Análisis:</strong> (herencia, taxonomía, mecanismos, emergencias, ausencias).</li>
    <li><strong>Corpus:</strong> mapa acumulativo con taxonomía, linajes, conceptos propuestos y métricas.</li>
    <li><strong>Guiones:</strong> a partir de guiones ad hoc con el ciclo documental (paso a paso para reproducir el análisis).</li>
    <li><strong>Cristalización:</strong> Generación de  poemas generados desde la voz del corpus.</li>
  </ol>
</section>
