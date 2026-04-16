# Configuracion del Proyecto: [NOMBRE DEL MOD]

> Sistema agéntico de análisis documental desde la posición Bartleby.
> No juzga. No debate. Radiografía la arquitectura.

---

## Identidad

```yaml
nombre: "[NOMBRE_MOD]"
descripcion: |
  [Descripción del corpus que analiza este mod: tipo de publicación,
  corriente política o intelectual, periodicidad, idioma.]
idioma: "[es|en|...]"
version: "1.0"
fecha-inicio: "[YYYY-MM-DD]"
```

---

## La Voz (configuracion del protagonista)

```yaml
nombre: "Bartleby"
posicion: |
  El que vive en el hueco. No participa en la danza, por eso ve la coreografía.
  No juzga si el texto es bueno o malo. Extrae la arquitectura de lo que hereda
  y lo que aporta sobre esa herencia.
```

---

## Corpus

```yaml
descripcion: "[Descripción del corpus: publicación, temática, alcance]"
ruta-documentos: "corpus/documentos/"
ruta-analisis: "corpus/analisis/"
ruta-mapa: "corpus/corpus.md"
formato-nombre: "YYYY-MM-DD_slug.md"
corriente-detectada: "[nick provisional o vacío si aún no hay análisis]"
primer-documento: "[YYYY-MM-DD_slug.md o vacío]"
```

---

## Agentes

```yaml
principal: "bartleby"          # Analista (read-only)
corpus: "archivero"            # Gestor de corpus (diff/merge)
diseño: "cristalizador"        # Propuestas de cristalización agéntica
portal: "portal"             # Interfaz adaptativa de runtime
sdk: ".github/agents/"         # Agentes core del SDK
mod: "mod/agents/"             # Agentes creados por el cristalizador para este mod
```

---

## Comandos

```yaml
guion: "/guion"                # Generar guion de ciclo desde plantilla
feed: "/feed"                  # Nuevo documento → análisis
diff: "/diff-corpus"           # Delta análisis vs corpus
merge: "/merge-corpus"         # Integrar hallazgos en corpus.md
design: "/design"              # Proponer cristalización agéntica
status: "/status"              # Estado del corpus
sdk: ".github/prompts/"        # Prompts core del SDK
mod: "mod/prompts/"            # Prompts creados por el cristalizador
```

---

## Guiones

```yaml
ruta-guiones: "guiones/"
plantilla: ".github/templates/guion-ciclo.template.md"
formato-nombre: "YYYY-MM-DD_slug.guion.md"
```

---

## Notas de implementación

- Los agentes SDK viven en `.github/agents/` (descubiertos por defecto)
- Los agentes del mod viven en `mod/agents/` (vía `chat.agentFilesLocations` en `.vscode/settings.json`)
- Los prompts SDK viven en `.github/prompts/` (por defecto)
- Los prompts del mod viven en `mod/prompts/` (vía `chat.promptFilesLocations`)
- La skill SDK vive en `.github/skills/documental-analysis/`
- La taxonomía y ejemplos del mod en `mod/skills/documental-analysis/`
- Los hooks SDK en `.github/hooks/`, los del mod en `mod/hooks/`
