---
layout: page
title: Cuadernos — legislativa
permalink: /legislativa/cuadernos/
---

{% assign gh = "https://github.com/escrivivir-co/para-la-voz-sdk/blob/mod/legislativa/" %}

<a class="leg-back" href="{{ '/legislativa/' | relative_url }}">← portada legislativa</a>

<section class="leg-hero">
  <h1>cuadernos</h1>
  <p class="leg-subtitle">mod/legislativa · análisis interactivos</p>
  <p class="leg-intro">Cuadernos Jupyter exportados como visualizaciones interactivas. Cada cuaderno conecta directamente con la base vectorial Chroma del pipeline.</p>
</section>

<div class="leg-catalog-grid">

  <div class="leg-catalog-item">
    <span class="item-type">visualización · chroma + umap</span>
    <h3><a href="{{ '/legislativa/cuadernos/corpus-visualizer/' | relative_url }}">Corpus Visualizer — mod/legislativa</a></h3>
    <p class="item-meta">64 piezas · 5 colecciones · UMAP 2D/3D · KMeans · query probe</p>
    <p class="item-desc">
      Proyección de los embeddings Chroma en espacio 2D/3D. Detecta clusters semánticos automáticos
      y divergencias entre la taxonomía textual del Archivero y la geometría vectorial.
      Incluye visor de query: introduce un texto y ve dónde aterriza en el corpus.
    </p>
    <div class="item-links">
      <a href="{{ '/legislativa/cuadernos/corpus-visualizer/' | relative_url }}">abrir →</a>
      <a href="{{ gh }}VectorMachineSDK/corpus_visualizer.ipynb" target="_blank" rel="noopener">notebook (.ipynb)</a>
    </div>
  </div>

</div>
