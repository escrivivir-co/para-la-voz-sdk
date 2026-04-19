

## Estructura

```
para-la-voz-sdk/
├── .github/                         → SDK puro (no modificar desde un mod)
│   ├── copilot-instructions.md      → identidad siempre-activa
│   ├── agents/                      → 4 agentes core (Cristalizador proveído por defecto)
│   ├── prompts/                     → 6 comandos core (incluye /guion y /design)
│   ├── skills/documental-analysis/   → protocolo de análisis (sin datos lore)
│   ├── hooks/                       → automatismos del pipeline
│   ├── instructions/                → reglas de voz Bartleby
│   └── templates/                   → plantillas de documentos (guion de ciclo)
├── .vscode/
│   └── settings.json                → registra mod/ como ubicación adicional
├── COPILOT/                         → docs de referencia VS Code Copilot vivo
├── proyecto.config.template.md      → plantilla de configuración para mods
└── README.md

── (solo en ramas mod/) ──────────────────────────────────────────────────────
├── corpus/                          → datos del lore
│   ├── corpus.md                    → mapa acumulativo de taxonomía y linajes
│   ├── documentos/                  → textos originales verbatim (.md)
│   └── analisis/                    → informes Bartleby (.analisis.md)
├── guiones/                         → roadmaps de ciclo documental (.guion.md)
├── mod/                             → artefactos creados por el cristalizador
│   ├── agents/                      → agentes nuevos y overrides locales del cristalizador
│   ├── prompts/                     → comandos nuevos
│   ├── skills/documental-analysis/  → taxonomía base y ejemplos del lore
│   ├── hooks/                       → hooks específicos del mod
│   └── instructions/                → instrucciones específicas del mod
└── proyecto.config.md               → configuración real del mod
```

## Los 5 agentes core

| Agente | Rol | Comandos |
|--------|-----|----------|
| `@bartleby` | Analista (read-only). Produce informes de 5 secciones. No juzga. | `/feed` |
| `@archivero` | Gestor del corpus. Diff, merge, evolución del mapa. | `/diff-corpus`, `/merge-corpus`, `/status` |
| `@cristalizador` | Diseñador agéntico por defecto en `main` del SDK. El repositorio hereda a este agente automáticamente, u opcionalmente lo sobreescribe en `mod/`. Realiza consultas reales en `COPILOT/` para proponer y armar implementaciones maximizadas. | `/design` |
| `@portal` | Interfaz adaptativa: visitante, equipo, editor. | invocación directa |
| `@dramaturgo` | Diseñador de universos. Construye grafos conversacionales de futuros ramificados desde el corpus. | invocación directa |

## Los 7 comandos core

| Comando | Acción |
|---------|--------|
| `/guion` | Genera un guion de ciclo documental desde la plantilla SDK |
| `/feed` | Recibe documento → genera `.analisis.md` → dispara diff automático |
| `/diff-corpus` | Muestra delta: nuevo, confirma, discrepa |
| `/merge-corpus` | Integra hallazgos aprobados en `corpus/corpus.md` |
| `/design` | Forma parte del ciclo. Propone cristalización agéntica (`mod/`) si descubre aprendizajes. Pide acuerdo mutuo al aplicar maximizaciones complejas. |
| `/status` | Estado del corpus |
| `/universo` | Crear o expandir un universo propio — grafo conversacional de futuros ramificados |

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
   si merge significativo o se descubre un gap en el uso
      │
   /design → @cristalizador evalúa necesidad y diseña propuestas con pacto
```
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