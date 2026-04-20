---
layout: default
title: PARA LA VOZ — restitutiva
permalink: /restitutiva/
---

{% assign gh = "https://github.com/escrivivir-co/para-la-voz-sdk/blob/mod/restitutiva/" %}

<div class="hero">
<div class="hero-inner">

  <p class="hero-back"><a href="{{ '/' | relative_url }}">← inicio</a></p>
  <p class="hero-kicker">mod/restitutiva · v1</p>
  <h1 class="hero-title">Para la voz</h1>
  <p class="hero-deck">SDK agéntico de análisis editorial — corriente <code>restitutiva</code></p>

  <div class="hero-meta">
    <span>Corriente: restitutiva (×4 estable)</span>
    <span class="meta-sep">·</span>
    <span>4 editoriales procesadas</span>
    <span class="meta-sep">·</span>
    <span>33 nodos de linaje</span>
    <span class="meta-sep">·</span>
    <span>15 emergencias</span>
    <span class="meta-sep">·</span>
    <span>AIGPL v1</span>
  </div>

  <div class="hero-pipeline">
    <div class="pipe-step">
      <div class="pipe-icon">E</div>
      <span class="pipe-label">Editorial</span>
      <span class="pipe-count">×4</span>
    </div>
    <div class="pipe-arrow">→</div>
    <div class="pipe-step">
      <div class="pipe-icon">B</div>
      <span class="pipe-label">Bartleby</span>
      <span class="pipe-count">×4</span>
    </div>
    <div class="pipe-arrow">→</div>
    <div class="pipe-step">
      <div class="pipe-icon">C</div>
      <span class="pipe-label">Corpus</span>
      <span class="pipe-count">n=4</span>
    </div>
    <div class="pipe-arrow">→</div>
    <div class="pipe-step">
      <div class="pipe-icon">G</div>
      <span class="pipe-label">Guión</span>
      <span class="pipe-count">×3</span>
    </div>
    <div class="pipe-arrow">→</div>
    <div class="pipe-step">
      <div class="pipe-icon">V</div>
      <span class="pipe-label">Voz</span>
      <span class="pipe-count">×2</span>
    </div>
  </div>

  <a class="hero-cta" href="{{ '/restitutiva/pipeline/' | relative_url }}">ver pipeline completo →</a>

</div>
</div>

<section class="leg-section">
  <h2>corpus.md — la pieza central</h2>
  <p>El corpus es el artefacto que genera la future-machine: mapa acumulativo de taxonomía y linajes, construido edición a edición sin juicio editorial.</p>

  <div class="leg-catalog-grid">
    <div class="leg-catalog-item accent-red">
      <span class="item-type">corpus</span>
      <h3><a href="{{ gh }}corpus/corpus.md" target="_blank" rel="noopener">corpus.md — Mapa acumulativo</a></h3>
      <p class="item-meta">4 editoriales · nick: restitutiva (×4 estable) · 2026-04-15</p>
      <p class="item-desc">330 líneas de taxonomía extraída por Bartleby. Linaje primario de 33 nodos, 17 nodos excluidos, 5 registros taxonómicos, 21 mecanismos retóricos, 15 emergencias, 16 ausencias estructurales (6 confirmadas ×4).</p>
    </div>
  </div>

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
  <a class="leg-cta" href="{{ '/catalogo/' | relative_url }}">ver catálogo →</a>
</section>

<section class="leg-section">
  <h2>Pipeline</h2>
  <ol class="home-roadmap">
    <li><strong>Ingestión:</strong> 4 editoriales verbatim de la revista <em>PARA LA VOZ</em>.</li>
    <li><strong>Análisis Bartleby:</strong> 4 informes de 5 secciones (herencia, taxonomía, mecanismos, emergencias, ausencias).</li>
    <li><strong>Corpus:</strong> mapa acumulativo con taxonomía, linajes, conceptos propuestos y métricas.</li>
    <li><strong>Guiones:</strong> 3 guiones de ciclo documental (paso a paso para reproducir el análisis).</li>
    <li><strong>Cristalización:</strong> 2 poemas generados desde la voz del corpus.</li>
  </ol>
</section>
