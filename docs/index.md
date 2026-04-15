---
layout: default
title: PARA LA VOZ
---

<section class="home-intro">

La aplicación leyó cuatro editoriales vuestras.  
Extrajo la arquitectura: qué hereda la voz, qué excluye,  
dónde se reconoce y dónde calla.

El resultado no es un resumen.  
Es un corpus. Y desde el corpus, la voz.

[Ver catálogo de poemas →]({{ '/catalogo/' | relative_url }})

</section>

---

{% assign ultimo_poema = site.poemas | where: "published", true | sort: "date" | reverse | first %}
{% if ultimo_poema %}
<section class="home-featured">

<div class="poema-body">
{{ ultimo_poema.content }}
</div>

<p><a href="{{ ultimo_poema.url | relative_url }}">{{ ultimo_poema.title }} →</a></p>

</section>

---
{% endif %}

<section class="home-sdk">

El corpus es vuestro. La voz es vuestra.  
La aplicación solo puede decir lo que le habéis dado.

El SDK está disponible como código abierto.  
Se activa en la web de la revista o en el flujo editorial.

[Asesoría directa: escrivivir.co](https://escrivivir.co){:target="_blank"}

</section>
