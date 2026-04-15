---
layout: page
title: Catálogo
permalink: /catalogo/
---

{% assign poemas_pub = site.poemas | where: "published", true | sort: "date" | reverse %}

{% if poemas_pub.size > 0 %}
<div class="catalogo-grid">
  {% for poema in poemas_pub %}
    {% include poema-card.html poema=poema %}
  {% endfor %}
</div>
{% else %}
<p class="catalogo-empty">Los poemas se generan desde el corpus.</p>
{% endif %}
