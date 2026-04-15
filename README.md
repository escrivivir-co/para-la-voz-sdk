# para-la-voz-sdk — SDK agéntico de análisis editorial

## Qué es esto

**para-la-voz-sdk** es un SDK de agentes VS Code Copilot para analizar textos editoriales desde la posición Bartleby: sin juzgar, sin debatir, extrayendo la arquitectura de la herencia y lo emergente sobre ella.

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
│   ├── prompts/                     → 5 comandos core
│   ├── skills/editorial-analysis/   → protocolo de análisis (sin datos lore)
│   ├── hooks/                       → automatismos del pipeline
│   └── instructions/                → reglas de voz Bartleby
├── .vscode/
│   └── settings.json                → registra mod/ como ubicación adicional
├── COPILOT/                         → docs de referencia VS Code Copilot (sync mensual)
├── proyecto.config.template.md      → plantilla de configuración para mods
└── README.md

── (solo en ramas mod/) ──────────────────────────────────────────────────────
├── corpus/                          → datos del lore
│   ├── corpus.md                    → mapa acumulativo de taxonomía y linajes
│   ├── editoriales/                 → textos originales verbatim (.md)
│   └── analisis/                    → informes Bartleby (.analisis.md)
├── mod/                             → artefactos creados por el cristalizador
│   ├── agents/                      → agentes nuevos para este lore
│   ├── prompts/                     → comandos nuevos
│   ├── skills/editorial-analysis/   → taxonomía base y ejemplos del lore
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
| `@portal-editorial` | Interfaz adaptativa: visitante, comité, editor. | invocación directa |

## Los 5 comandos core

| Comando | Acción |
|---------|--------|
| `/feed` | Recibe editorial → genera `.analisis.md` → dispara diff automático |
| `/diff-corpus` | Muestra delta: nuevo, confirma, discrepa |
| `/merge-corpus` | Integra hallazgos aprobados en `corpus/corpus.md` |
| `/design` | Propone cristalización agéntica en `mod/` |
| `/status` | Estado del corpus |

## Ciclo operativo

```
NUEVA EDITORIAL
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
| — | `mod/` (solo en mod) |
| — | `proyecto.config.md` (solo en mod — nombre diferente) |

`git pull origin main` en un mod actualiza el SDK sin tocar nunca los datos del lore.

## Cómo crear un nuevo mod

```bash
git checkout main
git pull origin main
git checkout -b mod/[nombre]

# Crear estructura de datos
mkdir -p corpus/editoriales corpus/analisis
touch corpus/corpus.md

# Crear estructura mod (para artefactos del cristalizador)
mkdir -p mod/agents mod/prompts mod/skills/editorial-analysis mod/hooks mod/instructions
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
  "chat.instructionsFilesLocations": { "mod/instructions": true }
}
```

En `main` estas rutas apuntan a directorios inexistentes (inofensivo). En cualquier mod, los directorios existen y VS Code los descubre automáticamente.
