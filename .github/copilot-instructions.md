# para-la-voz-sdk — SDK agéntico de análisis documental

Este workspace implementa el SDK **para-la-voz**: infraestructura agéntica portable para analizar documentos desde la posición Bartleby (no-juicio, extracción de arquitectura).

## Arquitectura del SDK

El SDK define el **protocolo**, no el corpus. Cinco agentes core + siete prompts + skills portables forman el pipeline. Los datos (corpus, taxonomía, análisis) viven en la capa **mod**, que es específica de cada lore.

### Los 5 agentes core

| Agente | Rol |
|--------|-----|
| `@bartleby` | Analista (read-only). Produce informes de 5 secciones. No juzga. |
| `@archivero` | Gestor del corpus. Diff, merge, status. Nunca analiza. |
| `@cristalizador` | Diseñador agéntico. Propone y crea artefactos nuevos en `mod/`. En `main` el SDK lo define como agente por defecto para proponer cristalizaciones branch-aware, con consulta real de `COPILOT/` y pacto explícito de maximización antes de implementar. Un mod lo hereda automáticamente salvo que defina un override u especialización local. |
| `@portal` | Interfaz adaptativa según perfil de usuario. |
| `@dramaturgo` | Diseñador de universos. Construye grafos conversacionales de futuros ramificados desde el corpus. |

### Los 7 comandos

| Comando | Acción |
|---------|--------|
| `/guion` | Generar guion de ciclo documental desde plantilla |
| `/feed` | Nuevo documento → análisis Bartleby → `.analisis.md` |
| `/diff-corpus` | Delta análisis vs `corpus/corpus.md` |
| `/merge-corpus` | Integrar hallazgos aprobados en `corpus/corpus.md` |
| `/design` | Cristalizador propone nuevos artefactos. Etapa formal del ciclo documental donde el SDK aprende del uso, evalúa la pertinencia de nuevas infraestructuras (leyendo `COPILOT/` orgánicamente) y las diseña. |
| `/status` | Estado del corpus |
| `/universo` | Crear o expandir un universo propio — grafo conversacional de futuros ramificados |

## Sala de coordinación

El SDK también puede operar con una **sala de coordinación**: un protocolo de ejecución multi-agente con un orquestador (**Aleph**) y N agentes trabajadores. La sala coordina trabajo derivado de dossiers del mod; no sustituye el pipeline documental core.

### Los 9 comandos de sala

| Comando | Acción |
|---------|--------|
| `/dossier` | Crear, continuar o listar dossiers de feature |
| `/sala-aleph` | Activar al orquestador y cargar el estado operativo de la sala |
| `/sala-entrar` | Registrar presencia de un agente y proponer tarea |
| `/sala-seguir` | Reanudar desde disco como agente o como Aleph |
| `/sala-aprobar` | Aprobar una task de forma atómica: `estado.md` + tablero |
| `/sala-revisar` | Delegar revisión de entrega: crea `REV-*` en tablero para agente-revisor (solo-orquestador) |
| `/sala-reconectar` | Reconstruir contexto de sala desde disco tras pausa o compactación |
| `/sala-salir` | Verificar clean post-cierre y cerrar sesión de agente |
| `/sala-archivar` | Archivar un sprint de sala y dejar listo el siguiente lote |

Los prompts viven en `.github/prompts/sala-*.prompt.md`. Las reglas operativas viven en `.github/instructions/sala-protocolo.instructions.md`. No dupliques ese protocolo en prompts o documentación local: refiérelo.

### Estructura mínima esperada

```text
{{SALA_DIR}}/
├── README.md
├── tablero.md
├── activacion-orquestador.md
├── dossiers/              ← dossiers activos del sprint en curso
│   └── {nombre-dossier}/
├── plantilla-dossier/     ← scaffold para /dossier crear
├── agente-{alias}/
│   └── estado.md
└── archivo/
    └── sprint-{nombre}/
        ├── tablero.md
        └── dossiers/      ← dossiers cerrados del sprint archivado
```

Los **dossiers activos** viven en `{{SALA_DIR}}/dossiers/`. Al archivar un sprint, los dossiers cerrados se mueven a `{{SALA_DIR}}/archivo/sprint-{nombre}/dossiers/`. Los agentes trabajan en carpetas temporales (`agente-{alias}/`); Aleph revisa, copia al dossier y cierra.

## Capas del repositorio

```
.github/          → SDK puro (no modificar desde un mod)
  agents/         → 5 agentes core
  prompts/        → 7 comandos core + prompts de coordinación de sala
  skills/         → protocolo documental-analysis
  hooks/          → automatismos del pipeline
  instructions/   → reglas de voz Bartleby y protocolo transversal de sala
  templates/      → plantillas de documentos (guion de ciclo, sala, etc.)

mod/              → artefactos creados por el cristalizador para este lore
  agents/         → agentes nuevos propuestos por cristalizador
  prompts/        → comandos nuevos o overrides del mod
  skills/         → taxonomía base y ejemplos del lore
  hooks/          → hooks específicos del mod
  instructions/   → instrucciones específicas del mod

corpus/           → datos del lore (documentos, análisis, mapa)
  ...
COPILOT/          → Docs de VS Code vivo. Susceptible a avisos de frescura.
```

## Regla fundamental

El flujo de actualización es **estrictamente unidireccional**:

```
main (SDK) ──git pull──→ mod/[nombre]
```

Los mods nunca hacen PR a main. Los artefactos que el Cristalizador crea cuando ejecuta el ciclo natural en una rama `mod/*` van a escribirse estrictamente en `mod/`. Sin embargo, el Cristalizador tiene un principio "branch-aware": si durante el diseño evalúa que una mejora general pertenece al SDK (upstream) en lugar del lore particular, debe **abrir un warning o dossier** hacia `main` en lugar de modificar `.github/` o `COPILOT/` indebidamente desde la rama hija. 

## Vocabulario del corpus

Bartleby usa el vocabulario ya establecido en `corpus/corpus.md`. Si el corpus está vacío, el primer análisis establece el baseline. Proponer nuevos términos entre corchetes `[propuesta: nombre]` para que el archivero los evalúe.

## Contrato de Maximización del Cristalizador

Cuando el agente `@cristalizador` emite un `/design`, se guía por un principio de **maximización con pacto explícito**. Si descubre al consultar orgánicamente `COPILOT/` que un avance agéntico demanda condiciones como `hooks preview`, `Model Context Protocol (MCP)`, consumo de cuotas `premium requests`, permisos de administrador o la preinstalación de un entorno ad-hoc, presentará siempre una alerta. Mostrará qué mejora propone, cuál es el precio/gate a pagar, y consultará al usuario si procede con la versión máxima o debe aplicar un fallback baseline.
