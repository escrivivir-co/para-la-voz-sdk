---
layout: page
title: Corpus Visualizer — legislativa
permalink: /legislativa/cuadernos/corpus-visualizer/
---

<a class="leg-back" href="{{ '/legislativa/cuadernos/' | relative_url }}">← cuadernos</a>

<section class="leg-hero">
  <h1>Corpus Visualizer</h1>
  <p class="leg-subtitle">64 piezas · UMAP 2D/3D · Chroma local</p>
  <p class="leg-intro">
    Proyección de los embeddings de las 5 colecciones (<code>ml_personajes</code>,
    <code>ml_eventos</code>, <code>ml_recursos</code>, <code>ml_piezas_media</code>,
    <code>ml_hilo_narrativo</code>) en espacio 2D mediante UMAP. Cada punto es una pieza del lore.
  </p>
</section>

<div class="cuaderno-tabs">
  <a class="cuaderno-tab cuaderno-tab--active" href="#viz-2d">2D</a>
  <a class="cuaderno-tab" href="#viz-3d">3D</a>
  <a class="cuaderno-tab" href="#viz-clusters">clusters</a>
</div>

<div class="cuaderno-frame" id="viz-2d">
  <iframe
    src="{{ '/legislativa/cuadernos/corpus_2d.html' | relative_url }}"
    width="100%"
    height="680"
    frameborder="0"
    loading="lazy"
    title="Corpus 2D — mod/legislativa"
  ></iframe>
</div>

<div class="cuaderno-frame cuaderno-frame--hidden" id="viz-3d">
  <iframe
    src="{{ '/legislativa/cuadernos/corpus_3d.html' | relative_url }}"
    width="100%"
    height="720"
    frameborder="0"
    loading="lazy"
    title="Corpus 3D — mod/legislativa"
  ></iframe>
</div>

<div class="cuaderno-frame cuaderno-frame--hidden" id="viz-clusters">
  <iframe
    src="{{ '/legislativa/cuadernos/corpus_clusters.html' | relative_url }}"
    width="100%"
    height="680"
    frameborder="0"
    loading="lazy"
    title="Clusters — mod/legislativa"
  ></iframe>
</div>

<script>
  document.querySelectorAll('.cuaderno-tab').forEach(tab => {
    tab.addEventListener('click', e => {
      e.preventDefault();
      document.querySelectorAll('.cuaderno-tab').forEach(t => t.classList.remove('cuaderno-tab--active'));
      document.querySelectorAll('.cuaderno-frame').forEach(f => f.classList.add('cuaderno-frame--hidden'));
      tab.classList.add('cuaderno-tab--active');
      const target = tab.getAttribute('href');
      document.querySelector(target).classList.remove('cuaderno-frame--hidden');
    });
  });
</script>

<section class="leg-section">
  <h2>Sobre este cuaderno</h2>
  <table class="home-note-table">
    <tr><td>Fuente</td><td>Chroma persistente · <code>ARCHIVO/PLUGINS/VECTOR_MACHINE/STORAGE</code></td></tr>
    <tr><td>Colecciones</td><td>5 (personajes, eventos, recursos, media, hilo narrativo)</td></tr>
    <tr><td>Piezas</td><td>64 documentos vectorizados</td></tr>
    <tr><td>Embedding</td><td>all-MiniLM-L6-v2 (Sentence Transformers, default Chroma)</td></tr>
    <tr><td>Proyección</td><td>UMAP · n_neighbors=5 · min_dist=0.2</td></tr>
    <tr><td>Tenant</td><td>scriptorium · database: mod-legislativa</td></tr>
  </table>
</section>
