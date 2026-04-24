# MOD/LEGISLATIVA — §3. BLOQUE C — Cristalización: documentos legales

← [Bloque B](mod_legislativa_B.md) · [Índice](mod_legislativa_INDEX.md) · Siguiente: [Bloque D →](mod_legislativa_D.md)

---

### C-1. Redefinición del output del cristalizador

El skill `voice-crystallization` ([.github/skills/voice-crystallization/SKILL.md](.github/skills/voice-crystallization/SKILL.md))
es explícitamente agnóstico respecto al formato de salida:

> *"El formato lo define el mod [...] La skill solo garantiza que, cualquiera que sea
> el formato, la voz sea recognosciblemente del corpus."*

El mod/legislativa DEBERÁ crear un skill de cristalización que defina:
- El formato de salida: documento legal normativo
- El perfil de lector: letrado, procurador, juzgado, parte
- La cláusula de *animus iocandi* obligatoria

### C-2. Catálogo de tipos documentales (pack)

El cristalizador DEBERÁ producir plantillas para, como mínimo, los siguientes
tipos documentales:

| ID | Tipo documental | Destinatario | Registro |
|----|----------------|-------------- |----------|
| D-01 | Demanda | Juzgado | Formal-procesal |
| D-02 | Contestación a la demanda | Juzgado | Formal-procesal |
| D-03 | Denuncia | Fiscalía / Juzgado de Guardia | Formal-penal |
| D-04 | Querella | Juzgado de Instrucción | Formal-penal |
| D-05 | Recurso de apelación | Audiencia Provincial | Formal-recurso |
| D-06 | Recurso de casación | Tribunal Supremo | Formal-recurso |
| D-07 | Escrito de conclusiones | Juzgado / Tribunal | Formal-procesal |
| D-08 | Solicitud de medidas cautelares | Juzgado | Formal-cautelar |
| D-09 | Escrito de alegaciones | Administración / Juzgado | Formal-administrativo |
| D-10 | Reclamación previa | Administración | Formal-administrativo |

Este catálogo es un punto de partida. El cristalizador PODRÁ proponer tipos
adicionales conforme el corpus lo justifique.

### C-3. Estructura de un documento legal cristalizado

Cada documento generado DEBERÁ contener, como mínimo:

```markdown
---
layout: documento
title: "[Tipo] — [Referencia del caso]"
tipo: D-XX
date: YYYY-MM-DD
procedimiento: "[referencia]"
corpus_refs: [lista de IDs de actuaciones del corpus que fundamentan este documento]
published: true
animus_iocandi: true
---

⚠️ ANIMUS IOCANDI — Este documento ha sido generado por un sistema agéntico
a partir de un corpus procesal. No constituye asesoramiento jurídico.
Su forma reproduce convenciones del foro con finalidad exclusivamente
demostrativa, formativa o lúdica.

---

## ENCABEZAMIENTO
[Juzgado/Tribunal, partes, procedimiento, representación]

## HECHOS
[Numerados. Cada hecho con referencia al corpus: (ref: actuacion-NNN)]

## FUNDAMENTOS DE DERECHO
[Numerados. Marco normativo extraído de Sección I del análisis Bartleby]

## SUPLICO / SOLICITO
[Petitum concreto]
```

### C-4. Cláusula de *animus iocandi*

Todo documento cristalizado DEBE incluir la cláusula de aviso en posición
prominente (antes del encabezamiento). El frontmatter DEBE incluir
`animus_iocandi: true`.

La plantilla Jekyll DEBERÁ renderizar este aviso con estilo visual diferenciado
(fondo, borde o icono) para que sea inequívocamente visible.

### C-5. Prompts de cristalización

DEBERÁN crearse prompts específicos en `mod/prompts/` para los tipos documentales.

**Opción de diseño (pendiente de decisión):**
- Opción A: un prompt por tipo documental (`/demanda`, `/denuncia`, `/apelacion`...)
- Opción B: un prompt único `/documento` con argumento de tipo (`/documento demanda`, `/documento apelacion`...)

La Opción B es más escalable y coherente con la convención SDK (6 prompts core,
no 6+N). **Propuesta: Opción B.**

**Backlog item:**
- [ ] **TASK C-5.1** — Crear `mod/skills/voice-crystallization/` con el protocolo de cristalización legal (formato, registro, cláusula *animus iocandi*)
- [ ] **TASK C-5.2** — Crear `mod/prompts/documento.prompt.md` con la lógica de selección de tipo y generación
- [ ] **TASK C-5.3** — Crear plantilla de guion adaptada al ciclo procesal en `mod/` (o evaluar si `guion-ciclo.template.md` del SDK es suficiente con instrucciones de mod)
- [ ] **TASK C-5.4** — Decidir Opción A vs Opción B y documentar la decisión
