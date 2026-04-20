---
layout: page
title: Catálogo — legislativa
permalink: /legislativa/catalogo/
---

<a class="leg-back" href="{{ '/legislativa/' | relative_url }}">← portada</a>

{% assign gh = "https://github.com/escrivivir-co/para-la-voz-sdk/blob/mod/legislativa/" %}

<div class="leg-catalog-grid">

  <div class="leg-catalog-item">
    <span class="item-type">índice</span>
    <h3><a href="{{ gh }}DRAFTS2/LORE_INDEX.md" target="_blank" rel="noopener">LORE_INDEX.md</a></h3>
    <p class="item-meta">51 piezas · P:9 S:13 N:5 T:14 R:10</p>
    <p class="item-desc">Inventario completo del lore: personajes, piezas sociales, noticias, fases temporales, recursos contextuales. Mapa de referencias cruzadas y convenciones de marcado.</p>
  </div>

  <div class="leg-catalog-item">
    <span class="item-type">corpus</span>
    <h3><a href="{{ gh }}DRAFTS2/CORPUS_PREVIEW-rev-045.md" target="_blank" rel="noopener">CORPUS_PREVIEW — rev-045</a></h3>
    <p class="item-meta">rev-045 · corriente: restitutiva-documental · 20 abr 2026</p>
    <p class="item-desc">Mapa acumulativo de taxonomía y linajes. Resultado de pasar las 51 piezas por el pipeline Bartleby: herencia, linaje por exclusión, taxonomía funcional, mecanismos retóricos, emergencias.</p>
  </div>

  <div class="leg-catalog-item">
    <span class="item-type">universo</span>
    <h3><a href="{{ gh }}DRAFTS2/universo/universo-2.md" target="_blank" rel="noopener">Universo-2 — La segunda ola</a></h3>
    <p class="item-meta">rama R4 rev-045 · Claude Opus 4.6 · 27 nodos, 35 arcos</p>
    <p class="item-desc">Escenario de futuros ramificados desde el grafo. Incorpora sustrato largo como capa de modulación: la segunda ola deja de ser reacción dispersa y se convierte en ecosistema articulado.</p>
  </div>

  <div class="leg-catalog-item">
    <span class="item-type">grafo</span>
    <h3><a href="{{ gh }}engine-logs/red-semantica-LORE_F-rev-044.md" target="_blank" rel="noopener">Red semántica — LORE_F rev-044</a></h3>
    <p class="item-meta">51 nodos · 115 arcos · 10 clusters</p>
    <p class="item-desc">Red semántica de co-ocurrencia cualificada sobre el hilo narrativo. Árbol de significado por capas, clusters temáticos y arcos tipados (causa, contención, amplificación, contradicción).</p>
  </div>

  <div class="leg-catalog-item">
    <span class="item-type">corto</span>
    <h3><a href="{{ gh }}DRAFTS2/LORE_F-02_CORTO-universo-2-claude-opus-4-6.md" target="_blank" rel="noopener">La Segunda Ola — Claude Opus 4.6</a></h3>
    <p class="item-meta">universo-2 · narración omnisciente fría · foco colectivo</p>
    <p class="item-desc">Corto transmedia generado desde universo-2. El aparato llega al lunes con cuatro años de ventaja. Once mil siete películas reclamadas, cuarenta con derechos demostrados.</p>

    <div class="leg-pack">
      <h4>Pack de cortos — universo-2 × 3 modelos</h4>
      <ul>
        <li><a href="{{ gh }}DRAFTS2/LORE_F-02_CORTO-universo-2-claude-opus-4-6.md" target="_blank" rel="noopener">Claude Opus 4.6</a></li>
        <li><a href="{{ gh }}DRAFTS2/LORE_F-02_CORTO-universo-2-gemini-3.1-pro.md" target="_blank" rel="noopener">Gemini 3.1 Pro</a></li>
        <li><a href="{{ gh }}DRAFTS2/LORE_F-02_CORTO-universo-2-gpt-5-4.md" target="_blank" rel="noopener">GPT-5-4</a></li>
      </ul>
    </div>
  </div>

  <div class="leg-catalog-item">
    <span class="item-type">revisión</span>
    <h3><a href="{{ gh }}DRAFTS2/LORE_F-02_CORTO-universo-2-REVIEW.md" target="_blank" rel="noopener">Benchmark comparativo — universo-2</a></h3>
    <p class="item-meta">revisor: Claude Opus 4.6 · 3 modelos evaluados</p>
    <p class="item-desc">Revisión cruzada de los tres cortos del universo-2. Evalúa fidelidad al spec, registro literario, foco colectivo y adherencia al grafo fuente.</p>
  </div>

</div>
