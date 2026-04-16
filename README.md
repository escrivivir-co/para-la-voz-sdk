# para-la-voz-sdk — SDK agéntico de análisis documental

## Qué es esto

**para-la-voz-sdk** es un SDK de agentes VS Code Copilot para analizar documentos desde la posición Bartleby: sin juzgar, sin debatir, extrayendo la arquitectura de la herencia y lo emergente sobre ella.

El SDK define el **protocolo**. Los datos (corpus, taxonomía, análisis) y los artefactos agénticos específicos viven en ramas **mod**, que heredan el SDK vía `git pull origin main`.

## Arquitectura de ramas

```
main              → SDK puro: protocolo, agentes core, sin datos de lore
mod/[nombre]      → Lore concreto: corpus + mod/ (artefactos del cristalizador)
```

### Regla fundamental: flujo unidireccional

```
main (SDK) ──git pull──→ mod/[nombre]
```

Los mods **nunca** hacen PR a main. Los artefactos que el cristalizador crea en `mod/` son específicos del lore. `main` lo actualiza solo el mantenedor del SDK.

## Estructura

```
para-la-voz-sdk/
├── .github/                         → SDK puro (no modificar desde un mod)
│   ├── copilot-instructions.md      → identidad siempre-activa
│   ├── agents/                      → 4 agentes core
│   ├── prompts/                     → 6 comandos core (incluye /guion)
│   ├── skills/documental-analysis/   → protocolo de análisis (sin datos lore)
│   ├── hooks/                       → automatismos del pipeline
│   ├── instructions/                → reglas de voz Bartleby
│   └── templates/                   → plantillas de documentos (guion de ciclo)
├── .vscode/
│   └── settings.json                → registra mod/ como ubicación adicional
├── COPILOT/                         → docs de referencia VS Code Copilot (sync mensual)
├── proyecto.config.template.md      → plantilla de configuración para mods
└── README.md

── (solo en ramas mod/) ──────────────────────────────────────────────────────
├── corpus/                          → datos del lore
│   ├── corpus.md                    → mapa acumulativo de taxonomía y linajes
│   ├── documentos/                  → textos originales verbatim (.md)
│   └── analisis/                    → informes Bartleby (.analisis.md)
├── guiones/                         → roadmaps de ciclo documental (.guion.md)
├── mod/                             → artefactos creados por el cristalizador
│   ├── agents/                      → agentes nuevos para este lore
│   ├── prompts/                     → comandos nuevos
│   ├── skills/documental-analysis/  → taxonomía base y ejemplos del lore
│   ├── hooks/                       → hooks específicos del mod
│   └── instructions/                → instrucciones específicas del mod
└── proyecto.config.md               → configuración real del mod
```

## Los 4 agentes core

| Agente | Rol | Comandos |
|--------|-----|----------|
| `@bartleby` | Analista (read-only). Produce informes de 5 secciones. No juzga. | `/feed` |
| `@archivero` | Gestor del corpus. Diff, merge, evolución del mapa. | `/diff-corpus`, `/merge-corpus`, `/status` |
| `@cristalizador` | Diseñador agéntico. Propone y crea artefactos en `mod/`. | `/design` |
| `@portal` | Interfaz adaptativa: visitante, equipo, editor. | invocación directa |

## Los 6 comandos core

| Comando | Acción |
|---------|--------|
| `/guion` | Genera un guion de ciclo documental desde la plantilla SDK |
| `/feed` | Recibe documento → genera `.analisis.md` → dispara diff automático |
| `/diff-corpus` | Muestra delta: nuevo, confirma, discrepa |
| `/merge-corpus` | Integra hallazgos aprobados en `corpus/corpus.md` |
| `/design` | Propone cristalización agéntica en `mod/` |
| `/status` | Estado del corpus |

## Guiones de ciclo

Un **guion** es un roadmap ejecutable para procesar un documento por el pipeline Bartleby. Es un documento markdown con checkboxes que una persona del equipo sigue paso a paso en VS Code.

**Momento en el flujo:** el guion se crea **antes** de activar ningún agente. Es lo primero que hace el usuario cuando llega un nuevo documento.

```
usuario crea guion  →  sigue el guion  →  agentes ejecutan los pasos
     /guion                                /feed  /diff  /merge
```

**Dónde viven:** `guiones/YYYY-MM-DD_slug.guion.md` — uno por documento, en la raíz del mod.

**Cómo se generan:** con `/guion corpus/documentos/YYYY-MM-DD_slug.md` o manualmente copiando la plantilla en `.github/templates/guion-ciclo.template.md`.

**Son documentos vivos:** los checkboxes se marcan durante la ejecución. Cuando todos están marcados, el ciclo está completo.

## Ciclo operativo

```
NUEVA ENTRADA
      │
   /guion → genera guiones/YYYY-MM-DD_slug.guion.md (roadmap)
      │
   usuario sigue el guion:
      │
   /feed → @bartleby analiza → corpus/analisis/YYYY-MM-DD_slug.analisis.md
      │
   (hook automático notifica)
      │
   /diff-corpus → @archivero → delta visible
      │
   usuario aprueba
      │
   /merge-corpus → @archivero → corpus/corpus.md actualizado
      │
   si merge significativo
      │
   /design → @cristalizador → propuesta en mod/
```

## Separación SDK / mod: por qué no hay conflictos en el pull

| Existe en main | Existe en mod |
|----------------|---------------|
| `.github/` | `.github/` (actualizado por pull) |
| `.vscode/settings.json` | `.vscode/settings.json` (actualizado por pull) |
| `COPILOT/` | `COPILOT/` (actualizado por pull) |
| `proyecto.config.template.md` | `proyecto.config.template.md` (actualizado) |
| — | `corpus/` (solo en mod) |
| — | `guiones/` (solo en mod) |
| — | `mod/` (solo en mod) |
| — | `corpus/` (solo en mod) |
| — | `guiones/` (solo en mod) |
| — | `mod/` (solo en mod) |
| — | `proyecto.config.md` (solo en mod — nombre diferente) |

`git pull origin main` en un mod actualiza el SDK sin tocar nunca los datos del lore.

## Cómo crear un nuevo mod

```bash
git checkout main
git pull origin main
git checkout -b mod/[nombre]

# Crear estructura de datos
mkdir -p corpus/documentos corpus/analisis
touch corpus/corpus.md

# Crear carpeta de guiones
mkdir guiones

# Crear estructura mod (para artefactos del cristalizador)
mkdir -p mod/agents mod/prompts mod/skills/documental-analysis mod/hooks mod/instructions
touch mod/agents/.gitkeep mod/prompts/.gitkeep mod/hooks/.gitkeep mod/instructions/.gitkeep

# Copiar plantilla de configuración
cp proyecto.config.template.md proyecto.config.md
# → editar proyecto.config.md con datos del lore

git add . && git commit -m "feat: inicializar mod/[nombre]"
git push origin mod/[nombre]
```

## COPILOT/ — Sincronización mensual

La carpeta `COPILOT/` contiene documentación de referencia de VS Code Copilot que el cristalizador usa para maximizar el uso de capacidades disponibles. Sincronizar mensualmente desde:

- https://code.visualstudio.com/docs/copilot/overview

El cristalizador revisa esta carpeta en cada iteración `/design` para detectar capacidades nuevas o actualizadas.

## Configuración VS Code

`.vscode/settings.json` registra `mod/` como ubicación adicional para todos los tipos de artefactos:

```json
{
  "chat.agentFilesLocations":        { "mod/agents": true },
  "chat.skillsLocations":            { "mod/skills": true },
  "chat.promptFilesLocations":       { "mod/prompts": true },
  "chat.hookFilesLocations":         { "mod/hooks": true },
  "chat.instructionsFilesLocations": { "mod/instructions": true },
  "github.copilot.chat.search.semanticTextResults": true
}
```

En `main` estas rutas apuntan a directorios inexistentes (inofensivo). En cualquier mod, los directorios existen y VS Code los descubre automáticamente.

## Semantic search (índice del workspace)

El SDK activa la búsqueda semántica vía `github.copilot.chat.search.semanticTextResults` en `.vscode/settings.json`. Esto permite que los agentes busquen por significado (no solo por texto exacto) en todo el workspace.

### Cómo funciona el índice entre ramas

- **El índice opera sobre los archivos en disco**, no sobre una rama concreta. Al cambiar de rama, VS Code actualiza el índice incrementalmente.
- **Es un solo índice por workspace abierto**, no uno por rama.
- **En `main`** el índice cubre el SDK (`.github/`, `COPILOT/`, plantillas).
- **En `mod/[nombre]`** el índice cubre SDK + corpus + artefactos del mod — todo lo que los agentes necesitan para buscar en el lore.

### Verificación post-pull

Tras hacer `git pull origin main` en un mod existente, verificar que el índice semántico está activo:

1. Abrir VS Code en la rama del mod
2. Barra de estado → icono de Copilot → comprobar "Workspace index: Ready"
3. Si aparece "Build Index", hacer clic para construirlo

El índice se construye una sola vez y se actualiza automáticamente. Si el repo está en GitHub, el índice remoto puede estar disponible inmediatamente.

---

## Mods activos

| Mod | Corriente | GitHub Pages | Rama |
|-----|-----------|--------------|------|
| PARA LA VOZ | `restitutiva` (marxismo-leninismo ortodoxo post-soviético) | [escrivivir-co.github.io/para-la-voz-sdk](https://escrivivir-co.github.io/para-la-voz-sdk/) | `mod/restitutiva` |

Para añadir un mod a esta tabla: crear la rama, hacer el primer ciclo Bartleby, abrir un issue en el repo principal.

---

## GitHub Pages — Sitio estático del mod

El SDK incluye infraestructura Jekyll mínima en `docs/` para publicar el catálogo de poemas y la voz cristalizada de cada mod.

### Arquitectura (SDK/mod)

```
main (SDK)          →  docs/_layouts/     layout base negro-blanco-rojo
                       docs/_includes/    header, footer, poema-card
                       docs/_sass/        variables, base, layout, poema, catálogo
                       docs/assets/       CSS compilado
                       docs/catalogo.md   catálogo genérico (Liquid loop)
                       docs/index.md      landing genérica (usa site.mod_name)
                       docs/_config.yml.example  plantilla de config

mod/[nombre] (lore) →  docs/_config.yml   config del mod (no en main)
                       docs/index.md      landing del mod (override)
                       docs/_poemas/      colección Jekyll de poemas
                       .github/workflows/pages.yml  deploy workflow
```

### Configuración inicial de un nuevo mod para Pages

```bash
# 1. Copiar la plantilla de config
cp docs/_config.yml.example docs/_config.yml
# Editar: mod_name, mod_branch, mod_corriente, mod_description, mod_contact

# 2. Copiar la plantilla de workflow de despliegue
cp .github/workflows/pages.template.yml .github/workflows/pages.yml
# Editar: cambiar "mod/[nombre-del-mod]" al nombre real de la rama

# 3. Crear landing del mod
# Editar docs/index.md con el contenido específico del lore

# 4. Crear carpeta de poemas
mkdir docs/_poemas

# 5. Activar GitHub Pages en Settings > Pages:
#    Source → GitHub Actions

git add docs/ .github/workflows/pages.yml
git commit -m "feat(pages): activar sitio GitHub Pages"
git push origin mod/[nombre]
```

### Flujo de publicación de poemas

El agente `@voz` crea poemas en `docs/_poemas/`. Cada poema tiene front matter Jekyll:

```yaml
---
title: "Título del poema"
date: YYYY-MM-DD
layout: poema
published: false   # borrador — @voz pregunta si publicar al crear
nota: "Tensión del corpus activada (para el equipo)"
---
```

El agente pregunta al generar: **¿publicar ahora o guardar como borrador?**
También recuerda los poemas en `published: false` no publicados todavía.

Al hacer push, GitHub Actions reconstruye el sitio automáticamente. El catálogo en `/catalogo/` se actualiza sin intervención.

### Gestión de rutas (CRÍTICO)

| Tipo | Patrón correcto |
|------|-----------------|
| Enlace interno (página → página) | `{{ "/catalogo/" \| relative_url }}` |
| CSS / assets | `{{ "/assets/css/style.css" \| relative_url }}` |
| → código fuente GitHub | `https://github.com/{{ site.sdk_repo }}/blob/{{ site.mod_branch }}/ruta` |

**Nunca hardcodear** `/para-la-voz-sdk/` — siempre usar `relative_url` para soportar cualquier `baseurl`.

---

## Cómo usar la aplicación

Hay dos vías de entrada:

### 1. Web (solo lectura)

El catálogo de poemas y la voz cristalizada están publicados en:

> **[escrivivir-co.github.io/para-la-voz-sdk](https://escrivivir-co.github.io/para-la-voz-sdk/)**

Cualquier persona puede leer el corpus hecho voz. No hace falta instalar nada.

### 2. VS Code + GitHub Copilot (pipeline completo)

Para usar los agentes — analizar editoriales, gestionar el corpus, generar desde la voz — se necesita VS Code con GitHub Copilot.

**Requisitos:**

- [VS Code](https://code.visualstudio.com/) (versión 1.99 o superior)
- [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) (extensión instalada y con suscripción activa)
- Git

**Pasos:**

```bash
# 1. Clonar el repositorio y abrir la rama del mod
git clone https://github.com/escrivivir-co/para-la-voz-sdk.git
cd para-la-voz-sdk
git checkout mod/restitutiva

# 2. Abrir en VS Code
code .
```

**Una vez dentro de VS Code:**

1. Abrir el panel de Copilot Chat (Ctrl+Alt+I / Cmd+Alt+I)
2. Los agentes y comandos del SDK están disponibles directamente:
   - `@bartleby` — analizar una editorial
   - `@archivero` — gestionar el corpus (diff, merge, status)
   - `@cristalizador` — proponer nuevos artefactos agénticos
   - `@portal-editorial` — interfaz adaptativa según perfil
   - `@voz` — generar poemas desde el corpus
3. Los comandos se invocan con `/`: `/feed`, `/diff-corpus`, `/merge-corpus`, `/status`, `/design`, `/guion`
4. Para procesar una nueva editorial, empezar con `/guion` y seguir el roadmap generado

> **Nota:** Al abrir el workspace, VS Code detecta automáticamente los agentes en `.github/agents/` y `mod/agents/`, los comandos en `.github/prompts/` y `mod/prompts/`, y las instrucciones en `.github/instructions/` y `mod/instructions/`. No hace falta configurar nada más.
