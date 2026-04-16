# MOD/LEGISLATIVA — §R. BLOQUE R — Refactor ontológico del SDK: editorial → documental

← [Índice](mod_legislativa_INDEX.md) · Siguiente: [Bloque A →](mod_legislativa_A.md)

> **Estado:** **EJECUTADO** — 2026-04-16
> Refactor aplicado en `main`. Criterio de aceptación §R-6.2 verificado: cero ocurrencias
> de "editorial" como término genérico en `.github/`, `README.md`, `proyecto.config.template.md`.
> Pendiente: adaptar `mod/restitutiva` (§R-5) cuando se reactive esa rama.

> **Prioridad:** ALTA — Este bloque es prerrequisito de todos los demás.
> Opera sobre `.github/` (SDK core) y por tanto requiere intervención del
> mantenedor del SDK. Se ejecuta en `main` antes de crear la rama `mod/legislativa`.

---

## R-0. Motivación

El SDK core emplea el término "editorial" como unidad genérica de input
en el pipeline Bartleby. Sin embargo, "editorial" designa específicamente
el texto publicado por una editorial de revista — concepto propio del
mod/restitutiva, no del SDK.

Esta acoplación semántica impide que otros mods (como legislativa, donde
la unidad de input es una actuación procesal) operen sin instrucciones
correctoras que compensen la terminología.

**Principio:** el SDK DEBE emplear terminología genérica. Cada mod
concreta la categoría mediante instrucciones en `mod/instructions/`.

---

## R-1. Tabla de sustitución léxica

El término genérico que sustituye a "editorial" en el SDK es **"documental"**
(adjetivo) y **"documento"** (sustantivo para la unidad de input).

| Término actual (SDK) | Término nuevo (SDK) | Nota |
|----------------------|---------------------|------|
| editorial (sustantivo: la pieza de input) | documento | Unidad genérica de feed |
| editorial (adjetivo: "análisis editorial") | documental | Adjetivo genérico |
| editoriales (plural sustantivo) | documentos | |
| editoriales procesadas | documentos procesados | Contadores en corpus.md y status |
| equipo editorial | equipo del mod | O simplemente "equipo" |
| ciclo editorial | ciclo documental | Guiones y templates |
| nueva editorial | nuevo documento | En prompts y guiones |
| texto de editorial | documento fuente | En hints y descripciones |

---

## R-2. Tabla de sustitución de rutas

| Ruta actual | Ruta nueva | Impacto |
|-------------|-----------|---------|
| `corpus/editoriales/` | `corpus/documentos/` | Solo en docs, templates e instrucciones del SDK. El directorio físico solo existe en ramas mod. |
| `YYYY-MM-DD_slug-editorial.md` | `YYYY-MM-DD_slug.md` | Se elimina el sufijo `-editorial` del patrón de nombres |
| `YYYY-MM-DD_slug-editorial.analisis.md` | `YYYY-MM-DD_slug.analisis.md` | Idem en análisis |

---

## R-3. Tabla de sustitución de identificadores

| Identificador actual | Identificador nuevo | Tipo | Impacto |
|---------------------|---------------------|------|---------|
| `editorial-analysis` (skill name) | `documental-analysis` | Nombre de skill (frontmatter `name:`) | Afecta a activación por nombre, referencias cruzadas |
| `.github/skills/editorial-analysis/` | `.github/skills/documental-analysis/` | Directorio | Renombrar carpeta |
| `mod/skills/editorial-analysis/` | `mod/skills/documental-analysis/` | Directorio (en docs/templates) | Actualizar en README, proyecto.config.template |
| `Portal Editorial` (agent name) | `Portal` | Nombre de agente | Simplificación: "Portal" es suficiente como interfaz adaptativa |
| `portal-editorial.agent.md` | `portal.agent.md` | Fichero | Renombrar |
| `@portal-editorial` | `@portal` | Invocación de agente | En docs y references |
| `EDITORIAL_FECHA` | `DOCUMENTO_FECHA` | Variable de plantilla | En guion.prompt.md y guion-ciclo.template.md |
| `EDITORIAL_TITULO` | `DOCUMENTO_TITULO` | Variable de plantilla | Idem |
| `EDITORIAL_NUMERO` | `DOCUMENTO_NUMERO` | Variable de plantilla | Idem |
| `EDITORIAL_ARCHIVO` | `DOCUMENTO_ARCHIVO` | Variable de plantilla | Idem |
| `EDITORIAL_SLUG` | `DOCUMENTO_SLUG` | Variable de plantilla | Idem |
| `EDITORIAL_TITULO_SLUG` | `DOCUMENTO_TITULO_SLUG` | Variable de plantilla | Idem |

---

## R-4. Inventario de ficheros afectados

### Tier 1 — Agentes SDK (`.github/agents/`)

#### R-4.1. `bartleby.agent.md`

| Línea | Texto actual | Texto nuevo |
|-------|-------------|-------------|
| 3 (description) | `Analista editorial desde la posición Bartleby [...] textos editoriales.` | `Analista documental desde la posición Bartleby [...] documentos.` |
| 4 (argument-hint) | `[ruta o texto de editorial a analizar]` | `[ruta o texto del documento a analizar]` |
| 20 (título) | `Bartleby — Analista editorial desde el hueco` | `Bartleby — Analista documental desde el hueco` |
| 32 | `Cuando recibes una editorial, produces un informe` | `Cuando recibes un documento, produces un informe` |
| 37 | `los autores y textos que el editorial nombra` | `los autores y textos que el documento nombra` |
| 99 | `si la editorial actual confirma` | `si el documento actual confirma` |
| 105 | `YYYY-MM-DD_slug-editorial.analisis.md` | `YYYY-MM-DD_slug.analisis.md` |
| 109 | `Análisis Bartleby — [Título de la editorial]` | `Análisis Bartleby — [Título del documento]` |
| 111 | `**Fecha editorial:** YYYY-MM-DD` | `**Fecha documento:** YYYY-MM-DD` |

#### R-4.2. `archivero.agent.md`

| Línea | Texto actual | Texto nuevo |
|-------|-------------|-------------|
| 3 (description) | `Nunca analiza editoriales directamente` | `Nunca analiza documentos directamente` |
| 9 (handoff prompt) | `re-análisis de la editorial` | `re-análisis del documento` |
| 19 | `No analizas editoriales` | `No analizas documentos` |
| 44 | `no aparecen en esta editorial` | `no aparecen en este documento` |
| 46 | `Cada editorial trabaja en su registro` | `Cada documento trabaja en su registro` |
| 77 | `Número total de editoriales procesadas` | `Número total de documentos procesados` |
| 89 | `**Editoriales procesadas:** N` | `**Documentos procesados:** N` |
| 90 | `**Última editorial:** [fecha — título]` | `**Último documento:** [fecha — título]` |

#### R-4.3. `portal-editorial.agent.md` → `portal.agent.md`

Renombrar fichero. Además:

| Línea | Texto actual | Texto nuevo |
|-------|-------------|-------------|
| 2 (name) | `Portal Editorial` | `Portal` |
| 3 (description) | `Interfaz adaptativa del proyecto BARTLEBY para diferentes perfiles de usuario [...]` | Sin cambio en la descripción — solo eliminar "editorial" donde sea conceptualmente SDK |
| 7 (handoff label) | `Analizar nueva editorial` | `Analizar nuevo documento` |
| 9 (handoff prompt) | `procesar una nueva editorial` | `procesar un nuevo documento` |
| 29 (título) | `Portal Editorial — Interfaz adaptativa` | `Portal — Interfaz adaptativa` |
| 31 | `Eres el Portal Editorial` | `Eres el Portal` |
| 46 | `análisis de editoriales concretas` | `análisis de documentos concretos` |
| 52 | `Subir nuevas editoriales` | `Subir nuevos documentos` |
| 63 | `equipo editorial` | `equipo del mod` |
| 67 | `Subir nuevas editoriales` | `Subir nuevos documentos` |
| 73 | `procesar la nueva editorial` | `procesar el nuevo documento` |
| 81 | `rol de análisis editorial` | `rol de análisis documental` |
| 85 | `Comparativas entre editoriales` | `Comparativas entre documentos` |
| 100 | `equipo editorial, o como editor de la revista` | `equipo del mod, o como editor` |
| 122 | `editoriales en corpus/editoriales/` | `documentos en corpus/documentos/` |
| 125 | `llega con una editorial nueva` | `llega con un documento nuevo` |
| 133 | `[N] editoriales de la revista` | `[N] documentos en el corpus` |
| 136 | `[N] editoriales en el corpus [...] nueva editorial` | `[N] documentos en el corpus [...] nuevo documento` |
| 139 | `[N] editoriales analizadas` | `[N] documentos analizados` |

> **Nota sobre perfiles:** los perfiles "visitante / comité / editor" son genéricos
> y pueden mantenerse. Lo que cambia es que las descripciones no asumen "revista"
> ni "editorial" sino que hablan de "corpus" y "documento". El mod/restitutiva
> puede añadir instrucciones que contextualicen: "el editor es el editor de la revista".

#### R-4.4. `cristalizador.agent.md`

| Línea | Texto actual | Texto nuevo |
|-------|-------------|-------------|
| 82 | `múltiples editoriales en lote` | `múltiples documentos en lote` |

---

### Tier 2 — Prompts SDK (`.github/prompts/`)

#### R-4.5. `feed.prompt.md`

| Línea | Texto actual | Texto nuevo |
|-------|-------------|-------------|
| 3 (description) | `nueva editorial. Invoca a Bartleby` | `nuevo documento. Invoca a Bartleby` |
| 4 (argument-hint) | `ruta al archivo de editorial` | `ruta al archivo del documento` |
| 9 (título) | `Nueva editorial al corpus` | `Nuevo documento al corpus` |
| 11 | `nueva editorial de la revista` | `nuevo documento` |
| 23 | `Analiza la editorial` | `Analiza el documento` |
| 26 | `slug-editorial.analisis.md` | `slug.analisis.md` |
| 27 | `publicación de la editorial` | `publicación del documento` |
| 32 | `texto original de la editorial en: corpus/editoriales/` | `texto original del documento en: corpus/documentos/` |
| 37-38 | `esta editorial en guiones/ [...] esta editorial` | `este documento en guiones/ [...] este documento` |

#### R-4.6. `diff-corpus.prompt.md`

| Línea | Texto actual | Texto nuevo |
|-------|-------------|-------------|
| 23 | `esta editorial` | `este documento` |
| 25 | `Cada editorial trabaja` | `Cada documento trabaja` |

#### R-4.7. `merge-corpus.prompt.md`

| Línea | Texto actual | Texto nuevo |
|-------|-------------|-------------|
| 24 | `Editoriales procesadas:` | `Documentos procesados:` |

#### R-4.8. `status.prompt.md`

| Línea | Texto actual | Texto nuevo |
|-------|-------------|-------------|
| 3 (description) | `número de editoriales` | `número de documentos` |
| 15 | `**Editoriales procesadas:** N` | `**Documentos procesados:** N` |
| 16 | `**Última editorial:**` | `**Último documento:**` |
| 48 | `editorial pendiente de procesar` | `documento pendiente de procesar` |

#### R-4.9. `guion.prompt.md`

| Línea | Texto actual | Texto nuevo |
|-------|-------------|-------------|
| 3 (description) | `ciclo editorial` ×3 | `ciclo documental` |
| 4 (argument-hint) | `editorial en corpus/editoriales/` | `documento en corpus/documentos/` |
| 8 (título) | `ciclo editorial` | `ciclo documental` |
| 10 | `equipo editorial [...] la editorial por el pipeline` | `equipo del mod [...] el documento por el pipeline` |
| 18 | `Editoriales procesadas: N` | `Documentos procesados: N` |
| 20 | `archivo de editorial indicado` | `archivo del documento indicado` |
| 21-26 | `EDITORIAL_*` ×6 | `DOCUMENTO_*` ×6 |
| 33 | `editoriales en corpus/editoriales/` | `documentos en corpus/documentos/` |
| 34 | `última editorial pendiente` | `último documento pendiente` |
| 37 | `corpus/editoriales/` | `corpus/documentos/` |
| 45, 49 | `EDITORIAL_FECHA`, `EDITORIAL_SLUG` | `DOCUMENTO_FECHA`, `DOCUMENTO_SLUG` |
| 56 | `archivo de editorial` | `archivo del documento` |
| 57 | `corpus/editoriales/2024-11-20_materialismo.md` | `corpus/documentos/2024-11-20_materialismo.md` |

---

### Tier 3 — Skills SDK (`.github/skills/`)

#### R-4.10. `editorial-analysis/SKILL.md` → `documental-analysis/SKILL.md`

Renombrar directorio. Además:

| Línea | Texto actual | Texto nuevo |
|-------|-------------|-------------|
| 2 (name) | `editorial-analysis` | `documental-analysis` |
| 3 (description) | `textos editoriales [...] una editorial, manifiesto` | `documentos [...] un documento, manifiesto` |
| 6 (título) | `editorial-analysis — Protocolo de análisis Bartleby` | `documental-analysis — Protocolo de análisis Bartleby` |
| 8 | `análisis Bartleby de textos editoriales` | `análisis Bartleby de documentos` |
| 12 | `"analizar" una editorial` | `"analizar" un documento` |
| 104 | `Fecha editorial` | `Fecha documento` |
| 122 | `mod/skills/editorial-analysis/` | `mod/skills/documental-analysis/` |

#### R-4.11. `voice-crystallization/SKILL.md`

| Línea | Texto actual | Texto nuevo |
|-------|-------------|-------------|
| 3 (description) | `espejo del skill editorial-analysis` | `espejo del skill documental-analysis` |
| 10-11 | `editorial-analysis` ×2 | `documental-analysis` |
| 26 | `usar editorial-analysis` | `usar documental-analysis` |
| 74 | `×3 o más editoriales` | `×3 o más documentos` |
| 76 | `esa editorial` | `ese documento` |
| 94 | `las editoriales las abren` | `los documentos las abren` |

---

### Tier 4 — Instructions SDK (`.github/instructions/`)

#### R-4.12. `bartleby-voice.instructions.md`

| Línea | Texto actual | Texto nuevo |
|-------|-------------|-------------|
| 3 (description) | `análisis editorial` | `análisis documental` |
| 38 | `fecha editorial` | `fecha documento` |

---

### Tier 5 — Templates SDK (`.github/templates/`)

#### R-4.13. `guion-ciclo.template.md`

| Línea | Texto actual | Texto nuevo |
|-------|-------------|-------------|
| 1 | `para editorial {{EDITORIAL_FECHA}} — {{EDITORIAL_TITULO}}` | `para documento {{DOCUMENTO_FECHA}} — {{DOCUMENTO_TITULO}}` |
| 4 | `**Editorial:** {{EDITORIAL_ARCHIVO}}` | `**Documento:** {{DOCUMENTO_ARCHIVO}}` |
| 5 | `{{EDITORIAL_TITULO}}` | `{{DOCUMENTO_TITULO}}` |
| 6 | `{{EDITORIAL_NUMERO}}` | `{{DOCUMENTO_NUMERO}}` |
| 8 | `editorial(es) procesada(s)` | `documento(s) procesado(s)` |
| 9 | `Editoriales procesadas:` | `Documentos procesados:` |
| 16 | `esta editorial por el pipeline` | `este documento por el pipeline` |
| Todas las refs | `{{EDITORIAL_*}}` | `{{DOCUMENTO_*}}` |
| 113 | `Editoriales procesadas: {{CORPUS_PROCESADAS_DESPUES}}` | `Documentos procesados: {{CORPUS_PROCESADAS_DESPUES}}` |

---

### Tier 6 — Ficheros raíz

#### R-4.14. `README.md`

Todas las ocurrencias de "editorial" como concepto genérico → "documental/documento".
Las rutas `corpus/editoriales/` → `corpus/documentos/`.
Los refs a `editorial-analysis` → `documental-analysis`.
Las refs a `portal-editorial` → `portal`.
El árbol de estructura → actualizar nombres de directorio y skills.

#### R-4.15. `proyecto.config.template.md`

| Línea | Texto actual | Texto nuevo |
|-------|-------------|-------------|
| 3 | `análisis de editoriales` | `análisis documental` |
| 38 | `ruta-editoriales: "corpus/editoriales/"` | `ruta-documentos: "corpus/documentos/"` |
| 41 | `formato-nombre: "YYYY-MM-DD_slug-editorial.md"` | `formato-nombre: "YYYY-MM-DD_slug.md"` |
| 43 | `primera-editorial:` | `primer-documento:` |
| 54 | `portal: "portal-editorial"` | `portal: "portal"` |
| 65 | `feed: "/feed" # Nueva editorial → análisis` | `feed: "/feed" # Nuevo documento → análisis` |
| 92 | `.github/skills/editorial-analysis/` | `.github/skills/documental-analysis/` |
| 93 | `mod/skills/editorial-analysis/` | `mod/skills/documental-analysis/` |

#### R-4.16. `.github/copilot-instructions.md`

| Línea | Texto actual | Texto nuevo |
|-------|-------------|-------------|
| 1 | `análisis editorial` | `análisis documental` |
| 3 | `textos editoriales` | `documentos` |
| 16 | `@portal-editorial` | `@portal` |
| 22 | `ciclo editorial` | `ciclo documental` |
| 23 | `Nueva editorial` | `Nuevo documento` |
| 35 | `protocolo editorial-analysis` | `protocolo documental-analysis` |
| 47 | `datos del lore (editoriales, análisis, mapa)` | `datos del lore (documentos, análisis, mapa)` |
| 48 | `editoriales/ → textos originales` | `documentos/ → textos originales` |
| 52 | `ciclo editorial (.guion.md) — uno por editorial` | `ciclo documental (.guion.md) — uno por documento` |

---

## R-5. Impacto sobre mod/restitutiva

La rama `mod/restitutiva` deberá adaptarse al refactor del SDK tras hacer
`git pull origin main`. Los cambios requeridos son:

### R-5.1. Renombrar directorio de fuentes

```bash
git mv corpus/editoriales/ corpus/documentos/
```

Los ficheros `.analisis.md` en `corpus/analisis/` que referencien la ruta
antigua DEBERÁN actualizarse.

### R-5.2. Instrucción de especialización terminológica

DEBERÁ crearse (si no existe) una instrucción en `mod/instructions/` que
establezca la equivalencia para el contexto del mod:

```markdown
---
applyTo: "**"
---
En este mod, un "documento" es una **editorial de la revista**.
El directorio `corpus/documentos/` contiene las editoriales verbatim.
Los "documentos procesados" en el corpus son editoriales analizadas.
```

### R-5.3. Actualización de guiones existentes

Los guiones en `guiones/` que usen las variables `{{EDITORIAL_*}}`
ya no coincidirán con la plantilla actualizada. Son documentos vivos
ya ejecutados, por lo que NO DEBEN modificarse retroactivamente.
Los guiones nuevos usarán `{{DOCUMENTO_*}}`.

### R-5.4. Actualización del skill del mod

La ruta `mod/skills/editorial-analysis/` DEBERÁ renombrarse a
`mod/skills/documental-analysis/` para que coincida con el nuevo
nombre del skill SDK.

---

## R-6. Estrategia de ejecución

### R-6.1. Orden de operaciones

1. Ejecutar en `main` (rama SDK):
   a. Renombrar directorios (skills)
   b. Renombrar ficheros (portal-editorial → portal)
   c. Aplicar sustituciones léxicas en todos los ficheros del Tier 1-6
   d. Verificar que no quedan ocurrencias residuales de "editorial"
      como concepto genérico (las referencias a "mod/restitutiva" como
      "editorial de revista" son legítimas y se mantienen en el README
      bajo la tabla de mods activos)
   e. Commit: `refactor(sdk): editorial → documental — terminología genérica`

2. Ejecutar en `mod/restitutiva`:
   a. `git pull origin main`
   b. Resolver conflictos (esperados en: guiones existentes, corpus paths)
   c. `git mv corpus/editoriales/ corpus/documentos/`
   d. Crear instrucción de especialización (R-5.2)
   e. Renombrar `mod/skills/editorial-analysis/` → `mod/skills/documental-analysis/`
   f. Commit: `refactor(mod): adaptar a terminología documental del SDK`

3. Crear rama `mod/legislativa` desde `main` actualizado.

### R-6.2. Verificación post-refactor

```bash
# En main: no debe quedar "editorial" como concepto genérico del SDK
# (excepto en la tabla de mods activos donde "editorial de revista" es
# descripción legítima del mod/restitutiva)
grep -rn "editorial" .github/ --include="*.md" | grep -v "mod/restitutiva"
```

**Criterio de aceptación:** cero ocurrencias de "editorial" en `.github/`
como término genérico del pipeline. Las únicas ocurrencias legítimas son
citas del nombre propio del mod/restitutiva.

---

## R-7. Backlog

| Task | Descripción | Artefacto | Fase |
|------|-------------|-----------|------|
| R-4.1 | Refactor bartleby.agent.md | `.github/agents/bartleby.agent.md` | main |
| R-4.2 | Refactor archivero.agent.md | `.github/agents/archivero.agent.md` | main |
| R-4.3 | Renombrar + refactor portal → portal.agent.md | `.github/agents/portal.agent.md` | main |
| R-4.4 | Refactor cristalizador.agent.md | `.github/agents/cristalizador.agent.md` | main |
| R-4.5 | Refactor feed.prompt.md | `.github/prompts/feed.prompt.md` | main |
| R-4.6 | Refactor diff-corpus.prompt.md | `.github/prompts/diff-corpus.prompt.md` | main |
| R-4.7 | Refactor merge-corpus.prompt.md | `.github/prompts/merge-corpus.prompt.md` | main |
| R-4.8 | Refactor status.prompt.md | `.github/prompts/status.prompt.md` | main |
| R-4.9 | Refactor guion.prompt.md | `.github/prompts/guion.prompt.md` | main |
| R-4.10 | Renombrar + refactor skill documental-analysis | `.github/skills/documental-analysis/SKILL.md` | main |
| R-4.11 | Refactor voice-crystallization SKILL.md | `.github/skills/voice-crystallization/SKILL.md` | main |
| R-4.12 | Refactor bartleby-voice.instructions.md | `.github/instructions/bartleby-voice.instructions.md` | main |
| R-4.13 | Refactor guion-ciclo.template.md | `.github/templates/guion-ciclo.template.md` | main |
| R-4.14 | Refactor README.md | `README.md` | main |
| R-4.15 | Refactor proyecto.config.template.md | `proyecto.config.template.md` | main |
| R-4.16 | Refactor copilot-instructions.md | `.github/copilot-instructions.md` | main |
| R-5.1 | Renombrar corpus/editoriales → corpus/documentos | `corpus/documentos/` | mod/restitutiva |
| R-5.2 | Crear instrucción de especialización | `mod/instructions/terminologia-editorial.instructions.md` | mod/restitutiva |
| R-5.4 | Renombrar skill del mod | `mod/skills/documental-analysis/` | mod/restitutiva |
