# para-la-voz-sdk — SDK agéntico de análisis documental

Este workspace implementa el SDK **para-la-voz**: infraestructura agéntica portable para analizar documentos desde la posición Bartleby (no-juicio, extracción de arquitectura).

## Arquitectura del SDK

El SDK define el **protocolo**, no el corpus. Cinco agentes core + siete prompts + skills portables forman el pipeline. Los datos (corpus, taxonomía, análisis) viven en la capa **mod**, que es específica de cada lore.

### Los 5 agentes core

| Agente | Rol |
|--------|-----|
| `@bartleby` | Analista (read-only). Produce informes de 5 secciones. No juzga. |
| `@archivero` | Gestor del corpus. Diff, merge, status. Nunca analiza. |
| `@cristalizador` | Diseñador agéntico. Propone y crea artefactos nuevos en `mod/`. |
| `@portal` | Interfaz adaptativa según perfil de usuario. |
| `@dramaturgo` | Diseñador de universos. Construye grafos conversacionales de futuros ramificados desde el corpus. |

### Los 7 comandos

| Comando | Acción |
|---------|--------|
| `/guion` | Generar guion de ciclo documental desde plantilla |
| `/feed` | Nuevo documento → análisis Bartleby → `.analisis.md` |
| `/diff-corpus` | Delta análisis vs `corpus/corpus.md` |
| `/merge-corpus` | Integrar hallazgos aprobados en `corpus/corpus.md` |
| `/design` | Cristalizador propone nuevos artefactos |
| `/status` | Estado del corpus |
| `/universo` | Crear o expandir un universo propio — grafo conversacional de futuros ramificados |

## Sala de coordinación

El SDK también puede operar con una **sala de coordinación**: un protocolo de ejecución multi-agente con un orquestador (**Aleph**) y N agentes trabajadores. La sala coordina trabajo derivado de dossiers del mod; no sustituye el pipeline documental core.

### Los 7 comandos de sala

| Comando | Acción |
|---------|--------|
| `/sala-aleph` | Activar al orquestador y cargar el estado operativo de la sala |
| `/sala-entrar` | Registrar presencia de un agente y proponer tarea |
| `/sala-seguir` | Reanudar desde disco como agente o como Aleph |
| `/sala-aprobar` | Aprobar una task de forma atómica: `estado.md` + tablero |
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
├── agente-{alias}/
│   └── estado.md
└── archivo/
```

Fuera de `{{SALA_DIR}}`, el mod mantiene sus dossiers activos y sus salidas finales. La sala solo coordina la ejecución: el tablero apunta a tasks; los agentes trabajan en carpetas temporales; Aleph revisa, copia y cierra.

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
  documentos/     → textos originales verbatim
  analisis/       → informes Bartleby (.analisis.md)
  corpus.md       → mapa acumulativo de taxonomía y linajes

guiones/          → roadmaps de ciclo documental (.guion.md) — uno por documento

COPILOT/          → docs de referencia VS Code Copilot (sync mensual)
```

## Regla fundamental

El flujo de actualización es **estrictamente unidireccional**:

```
main (SDK) ──git pull──→ mod/[nombre]
```

Los mods nunca hacen PR a main. Los artefactos que el cristalizador crea en `mod/` son específicos del lore. `main` se actualiza solo por el mantenedor del SDK.

## Vocabulario del corpus

Bartleby usa el vocabulario ya establecido en `corpus/corpus.md`. Si el corpus está vacío, el primer análisis establece el baseline. Proponer nuevos términos entre corchetes `[propuesta: nombre]` para que el archivero los evalúe.