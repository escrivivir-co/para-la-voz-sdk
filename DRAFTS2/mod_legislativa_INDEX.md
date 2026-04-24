# MOD/LEGISLATIVA — Especificación técnica

**Identificador:** `mod/legislativa`
**Versión:** 0.1.0-draft
**Fecha:** 2026-04-16
**Estado:** BORRADOR — pendiente de validación por el promotor
**Base SDK:** `para-la-voz-sdk` @ `.github/` (inmutable desde el mod)
**Registro:** especificación DevOps — lenguaje normativo según convención RFC 2119 adaptada

> **Convención terminológica.** DEBE, NO DEBE, DEBERÁ y PODRÁ tienen el significado
> prescriptivo habitual. Los requisitos se numeran con prefijo de bloque (R-, A-, B-, C-, D-, E-, F-)
> y cada uno referencia el artefacto de la codebase que lo implementa.

---

## Índice de bloques

| Bloque | Título | Fichero |
|--------|--------|---------|
| §0 | Objeto y alcance | (este fichero) |
| §R | **Refactor ontológico del SDK: editorial → documental** | [mod_legislativa_R.md](mod_legislativa_R.md) |
| §1 · A | Identidad del mod y separación del SDK | [mod_legislativa_A.md](mod_legislativa_A.md) |
| §2 · B | Naturaleza del feed y semántica del corpus | [mod_legislativa_B.md](mod_legislativa_B.md) |
| §3 · C | Cristalización: documentos legales | [mod_legislativa_C.md](mod_legislativa_C.md) |
| §4 · D | Caso semilla y bootstrap del corpus | [mod_legislativa_D.md](mod_legislativa_D.md) |
| §5 · E | Trazabilidad en el catálogo y plantillas | [mod_legislativa_E.md](mod_legislativa_E.md) |
| §6 · F | Ciclo de vida: archivar y reiniciar | [mod_legislativa_F.md](mod_legislativa_F.md) |
| §7 | Resumen del backlog | (este fichero) |
| §8 | Decisiones pendientes | (este fichero) |

---

## §0. Objeto y alcance

La presente especificación define los requisitos para la creación de un nuevo mod
del SDK `para-la-voz` destinado al ámbito jurídico-procesal. El mod operará sobre
evidencia documental de casos concretos (declaraciones, partes judiciales, resoluciones,
escritos de parte) y cristalizará artefactos con la forma y disposición de documentos
normativos habituales del foro, debidamente señalizados con cláusula de *animus iocandi*.

El mod NO es una herramienta de decisión jurídica. El archivero reúne; el cristalizador
da forma. La verdad procesal queda fuera del alcance agéntico.

---

## §7. Resumen del backlog

### Fase -1 — Refactor ontológico del SDK ✅ COMPLETADO 2026-04-16

> Detalle completo en [§R — Bloque R](mod_legislativa_R.md).
> Commits: `17752c8` (refactor SDK) + `70d5e73` (spec plan)

| Task | Descripción | Artefacto |
|------|-------------|-----------|
| R-4.1 a R-4.16 | Sustitución léxica: "editorial" → "documental/documento" en 16 ficheros SDK | `.github/**`, `README.md`, `proyecto.config.template.md` |
| R-4.3 | Renombrar `portal-editorial.agent.md` → `portal.agent.md` | `.github/agents/` |
| R-4.10 | Renombrar `editorial-analysis/` → `documental-analysis/` | `.github/skills/` |
| R-5.1 | Renombrar `corpus/editoriales/` → `corpus/documentos/` | rama `mod/restitutiva` |
| R-5.2 | Instrucción de especialización terminológica | `mod/instructions/terminologia-editorial.instructions.md` (restitutiva) |

### Fase 0 — Infraestructura (depende de Fase -1)

| Task | Descripción | Artefacto |
|------|-------------|-----------|
| A-3.1 | Crear árbol `mod/` | directorios + `.gitkeep` |
| A-3.2 | Crear árbol `corpus/` (con `actuaciones/`) | directorios + `corpus.md` vacío |
| A-3.3 | Crear `docs/_documentos/` | directorio colección Jekyll |
| A-4.1 | Crear `proyecto.config.md` | fichero de configuración |
| A-5.1 | Crear `docs/_config.yml` | configuración Jekyll |
| A-6.1 | Crear workflow de despliegue | `.github/workflows/pages.yml` |
| F-4.1 | Crear `archivo/` | directorio + `.gitignore` |

### Fase 1 — Instrucciones del mod (depende de Fase 0)

| Task | Descripción | Artefacto |
|------|-------------|-----------|
| B-1.1 | Instrucción de input procesal | `mod/instructions/input-procesal.instructions.md` |
| B-2.1 | Instrucción Bartleby legal | `mod/instructions/bartleby-legal.instructions.md` |
| B-3.1 | Instrucción discrepancia legal | `mod/instructions/discrepancia-legal.instructions.md` |
| B-4.1 | Frontmatter obligatorio de actuaciones | amplía B-1.1 |

### Fase 2 — Skills y prompts del mod (depende de Fase 1)

| Task | Descripción | Artefacto |
|------|-------------|-----------|
| C-5.1 | Skill de cristalización legal | `mod/skills/voice-crystallization/` |
| C-5.2 | Prompt `/documento` | `mod/prompts/documento.prompt.md` |
| C-5.3 | Evaluación de plantilla de guion | decisión documentada |
| C-5.4 | Decisión Opción A vs B (prompt único vs múltiple) | decisión documentada |
| B-3.2 | Evaluación agente archivero-legal | decisión documentada |

### Fase 3 — Plantillas Jekyll (depende de Fase 0)

| Task | Descripción | Artefacto |
|------|-------------|-----------|
| E-4.1 | Layout `documento.html` | `docs/_layouts/documento.html` |
| E-4.2 | Card `documento-card.html` | `docs/_includes/documento-card.html` |
| E-4.3 | SCSS documento | `docs/_sass/_documento.scss` |
| E-4.4 | Catálogo multi-colección | `docs/catalogo.md` modificado |
| E-4.5 | Config trazabilidad | `docs/_config.yml` ampliado |
| E-5.1 | Renderizado de refs inline | en cristalización (Opción C) |

### Fase 4 — Ciclo de vida (depende de Fase 2)

| Task | Descripción | Artefacto |
|------|-------------|-----------|
| F-2.1 | Prompt `/archive` | `mod/prompts/archive.prompt.md` |
| F-3.1 | Prompt `/reset` | `mod/prompts/reset.prompt.md` |
| F-4.2 | Evaluación SDK vs mod para archive/reset | decisión documentada |

### Fase 5 — Caso semilla (depende de Fases 1-4)

| Task | Descripción | Artefacto |
|------|-------------|-----------|
| D-3.1 | Preparar actuaciones del caso | `corpus/actuaciones/` |
| D-3.2 | Ejecutar primer ciclo completo | pipeline end-to-end |
| D-3.3 | Verificar corpus acumulado | `corpus/corpus.md` validado |

---

## §8. Decisiones pendientes

| ID | Decisión | Bloque | Propuesta | Estado |
|----|----------|--------|-----------|--------|
| DEC-01 | ¿Prompt único `/documento` o uno por tipo? | C | Opción B (único con argumento) | PROPUESTA |
| DEC-02 | ¿Archivero-legal como agente separado o solo instrucciones? | B | Solo instrucciones (MVP) | PROPUESTA |
| DEC-03 | ¿Archive/reset en SDK o en mod? | F | En mod para MVP, evaluar migración | PROPUESTA |
| DEC-04 | ¿ZIPs de archivo en git o en .gitignore? | F | En .gitignore | PROPUESTA |
| DEC-05 | ¿Renderizado de refs inline: plugin, JS o preproceso? | E | Preproceso en cristalización (MVP) | PROPUESTA |
| DEC-06 | ¿Plantilla de guion SDK suficiente o crear variante legal? | C | Evaluar tras primer ciclo | PENDIENTE |
| DEC-07 | ¿Caso semilla: orden de ingesta? | D | Pendiente de datos del caso | PENDIENTE |
| DEC-08 | ¿"Portal Editorial" → "Portal" o "Portal Documental"? | R | "Portal" (suficiente) | **APROBADO** |
| DEC-09 | ¿Mantener `slug-editorial` en patrón de nombres o simplificar a `slug`? | R | Simplificar a `YYYY-MM-DD_slug.md` | **APROBADO** |
