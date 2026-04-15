---
layout: default
title: Inicio
---

<section class="sdk-home">

**{{ site.sdk_name }}** es un SDK agéntico de análisis editorial.  
Extrae la arquitectura de la herencia. No juzga. No debate.

{% if site.mod_name %}
Este sitio corresponde al mod **{{ site.mod_name }}** — {{ site.mod_description }}.

[Ver catálogo →]({{ '/catalogo/' | relative_url }})
{% else %}
[Código fuente →](https://github.com/{{ site.sdk_repo }})
{% endif %}

</section>
