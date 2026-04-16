# MOD/LEGISLATIVA — §5. BLOQUE E — Trazabilidad en el catálogo y plantillas

← [Bloque D](mod_legislativa_D.md) · [Índice](mod_legislativa_INDEX.md) · Siguiente: [Bloque F →](mod_legislativa_F.md)

---

### E-1. Diagnóstico del estado actual

Las plantillas Jekyll del SDK presentan la siguiente estructura de renderizado:

| Artefacto | Fichero | Trazabilidad actual |
|-----------|---------|---------------------|
| Card del catálogo | [docs/_includes/poema-card.html](docs/_includes/poema-card.html) | Muestra `title`, `date` y `nota`. El campo `nota` puede contener referencia al corpus, pero es texto libre |
| Layout del detalle | [docs/_layouts/poema.html](docs/_layouts/poema.html) | Renderiza `{{ content }}` sin ninguna referencia al corpus. Pierde la trazabilidad de la entradilla |
| Layout base | [docs/_layouts/default.html](docs/_layouts/default.html) | Estructura HTML sin lógica de trazabilidad |

**Problema identificado:** al entrar al detalle de un poema, se pierde la conexión
con el corpus que sí aparece en la card del catálogo.

### E-2. Requisito de trazabilidad para documentos legales

En el mod/legislativa, cada sección del documento cristalizado (Hechos,
Fundamentos, Suplico) DEBE mantener trazabilidad a las actuaciones del corpus
que la fundamentan.

**Formato de referencia inline:** `(ref: YYYY-MM-DD_tipo-NNN)` en el markdown
fuente, que la plantilla Jekyll DEBERÁ renderizar como enlace o tooltip
al análisis correspondiente.

### E-3. Activabilidad por mod

Este comportamiento DEBERÁ ser activable por configuración, no hardcoded.

**Propuesta de implementación:**

En `docs/_config.yml`:
```yaml
mod_traceability: true    # false en mod/restitutiva, true en mod/legislativa
```

En el layout de detalle, condicional:
```liquid
{% if site.mod_traceability %}
  [renderizar referencias inline con enlaces]
{% endif %}
```

### E-4. Nuevos artefactos Jekyll requeridos

| Artefacto | Ruta | Acción |
|-----------|------|--------|
| Layout documento | `docs/_layouts/documento.html` | CREAR — análogo a `poema.html` pero con soporte de trazabilidad, cláusula *animus iocandi*, y estructura legal (encabezamiento, hechos, fundamentos, suplico) |
| Card documento | `docs/_includes/documento-card.html` | CREAR — análogo a `poema-card.html` pero con tipo documental, procedimiento, y corpus_refs visibles |
| SCSS documento | `docs/_sass/_documento.scss` | CREAR — estilos para documento legal: tipografía formal, numeración, aviso *animus iocandi*, referencias inline |
| Catálogo | `docs/catalogo.md` | MODIFICAR — condicional: si la colección es `documentos`, usar `documento-card.html`; si es `poemas`, usar `poema-card.html` |
| Variables SCSS | [docs/_sass/_variables.scss](docs/_sass/_variables.scss) | EVALUAR — posiblemente añadir variables para la paleta legal (más sobria que la actual rojo/negro/blanco) |
| Config | `docs/_config.yml` | AÑADIR `mod_traceability: true` |

### E-5. Renderizado de referencias inline

Las referencias `(ref: YYYY-MM-DD_tipo-NNN)` en el contenido markdown DEBERÁN
transformarse en el HTML renderizado. Dos opciones:

- **Opción A (Jekyll plugin):** filtro Liquid personalizado. Más limpio pero requiere plugin.
- **Opción B (JavaScript client-side):** regex post-renderizado en el navegador. Sin dependencias.
- **Opción C (Preproceso en cristalización):** el cristalizador genera el HTML directamente en el markdown. Sin dependencias, sin JS, pero acopla generación y presentación.

**Propuesta: Opción C para MVP, migrar a Opción A si el catálogo crece.**

**Backlog item:**
- [ ] **TASK E-4.1** — Crear `docs/_layouts/documento.html` con soporte de trazabilidad y cláusula *animus iocandi*
- [ ] **TASK E-4.2** — Crear `docs/_includes/documento-card.html` con tipo documental y refs visibles
- [ ] **TASK E-4.3** — Crear `docs/_sass/_documento.scss` con estilos del registro legal
- [ ] **TASK E-4.4** — Modificar `docs/catalogo.md` para soporte multi-colección (documentos + poemas)
- [ ] **TASK E-4.5** — Añadir `mod_traceability` a `docs/_config.yml`
- [ ] **TASK E-5.1** — Implementar renderizado de referencias inline (Opción C para MVP)
