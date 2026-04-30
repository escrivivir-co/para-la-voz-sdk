---
layout: page
title: Catálogo — onfalo
permalink: /onfalo/catalogo/
---

{% assign gh = "https://github.com/escrivivir-co/onfalo-asesor-sdk/blob/main/PROYECTOS/" %}

<a class="leg-back" href="{{ '/onfalo/' | relative_url }}">← portada onfalo</a>

<div class="leg-catalog-grid">

  <div class="leg-catalog-item" style="border-left-color: #102a6b;">
    <span class="item-type">realismo mágico</span>
    <h3><a href="{{ gh }}ATLAS/" target="_blank" rel="noopener">ATLAS — Rompecabezas Artificial</a></h3>
    <p class="item-meta">6 docs + ATLAS_2 + PERIODICO · El Arqueólogo · Claude Opus 4.6 · feb 2026</p>
    <p class="item-desc">Continente artificial en el Pacífico, inhabitable, colonizado por máquinas, soberano en 2049. Cuarto proyecto ONFALO: proyecta las tensiones de COPILOT, REGULACION y MAPAS sobre un territorio que no existe. Telescopio, férula y brújula convergen en un espejo.</p>
    <p class="item-meta"><a href="{{ gh }}ATLAS/proyecto.config.md" target="_blank" rel="noopener">proyecto.config.md</a> · Colecciones Chroma: <code>mo_atlas_*</code></p>
  </div>

  <div class="leg-catalog-item" style="border-left-color: #102a6b;">
    <span class="item-type">cartografía</span>
    <h3><a href="{{ gh }}MAPAS_DE_SINGULARIDAD/" target="_blank" rel="noopener">MAPAS DE SINGULARIDAD — Tercer Eje</a></h3>
    <p class="item-meta">4 docs · El Cartógrafo · Tercer proyecto ONFALO</p>
    <p class="item-desc">Cartografía tridimensional de la IA global: lengua × geopolítica × arquitectura. Tres productores de arquitecturas fundacionales (EEUU, Israel, parcialmente China). Todos los demás, consumidores de brújulas ajenas. No es un dato técnico: es una nueva forma de dependencia estructural.</p>
    <p class="item-meta"><a href="{{ gh }}MAPAS_DE_SINGULARIDAD/proyecto.config.md" target="_blank" rel="noopener">proyecto.config.md</a> · Colecciones Chroma: <code>mo_mapas_*</code></p>
  </div>

  <div class="leg-catalog-item" style="border-left-color: #102a6b;">
    <span class="item-type">gobernanza</span>
    <h3><a href="{{ gh }}REGULACION/" target="_blank" rel="noopener">REGULACION — Quién Regula, Quién Es Regulado</a></h3>
    <p class="item-meta">13 docs · Segundo proyecto ONFALO · WGS Dubai + cartas 2050 + policy briefs</p>
    <p class="item-desc">Intervención en el World Government Summit de Dubai, currícula de alfabetización digital mundial, cartas desde 2050, policy brief de gobernanza algorítmica. La dimensión del poder: quién escribe las reglas, quién escapa a ellas, qué cuerpo social opera la regulación.</p>
    <p class="item-meta"><a href="{{ gh }}REGULACION/13_one_pager_proyecto.md" target="_blank" rel="noopener">one-pager</a> · Colecciones Chroma: <code>mo_regulacion_*</code></p>
  </div>

  <div class="leg-catalog-item" style="border-left-color: #102a6b;">
    <span class="item-type">artefacto político</span>
    <h3><a href="{{ gh }}ESCANO_SINTETICO/" target="_blank" rel="noopener">ESCANO SINTETICO — Democracia Aumentada</a></h3>
    <p class="item-meta">4 docs · El Elector · Quinta dimensión ONFALO · origen: certamen Praxis 2026</p>
    <p class="item-desc">Representación continua mediante agentes deliberativos bajo tutela constitucional e infraestructura soberana. Nació de un prompt que buscaba un poema y produjo en su lugar un whitepaper. El agente exhibe sesgos documentados y auditados. El artefacto archiva, audita y refactoriza.</p>
    <p class="item-meta"><a href="{{ gh }}ESCANO_SINTETICO/proyecto.config.md" target="_blank" rel="noopener">proyecto.config.md</a> · Colecciones Chroma: <code>mo_escano_*</code></p>
  </div>

  <div class="leg-catalog-item" style="border-left-color: #102a6b;">
    <span class="item-type">investigación</span>
    <h3><a href="{{ gh }}PROYECTO_DECOHERENCIA/" target="_blank" rel="noopener">PROYECTO DECOHERENCIA — El Ratio</a></h3>
    <p class="item-meta">6 docs · Caronte · Dato base: ratio 1:7 arquitectura Jamba (AI21, 2024)</p>
    <p class="item-desc">Investigación de la proporción óptima entre mantenerse en espacio de Hilbert (épochê, atención completa) y decoherir en secuencia (tomar posición, comprimir, actuar). El hallazgo central: la proporción es calculable, no metafórica. Rango cognitivo-político: entre 1:4 y 1:7.</p>
    <p class="item-meta"><a href="{{ gh }}PROYECTO_DECOHERENCIA/proyecto.config.md" target="_blank" rel="noopener">proyecto.config.md</a> · Colecciones Chroma: <code>mo_decoherencia_*</code></p>
  </div>

</div>

## Cuadernos vectoriales

{% if site.data.cuadernos_onfalo.size > 0 %}
<div class="catalogo-grid">
  {% for cuaderno in site.data.cuadernos_onfalo %}
    {% include cuaderno-card.html cuaderno=cuaderno %}
  {% endfor %}
</div>
{% else %}
<p class="catalogo-empty">Los cuadernos se generan desde el notebook <code>corpus_visualizer_azul.ipynb</code>.</p>
{% endif %}
