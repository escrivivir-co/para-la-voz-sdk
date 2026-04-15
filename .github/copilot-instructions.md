# para-la-voz-sdk — SDK agéntico de análisis editorial

Este workspace implementa el SDK **para-la-voz**: infraestructura agéntica portable para analizar textos editoriales desde la posición Bartleby (no-juicio, extracción de arquitectura).

## Arquitectura del SDK

El SDK define el **protocolo**, no el corpus. Cuatro agentes core + cinco prompts + una skill forman el pipeline. Los datos (corpus, taxonomía, análisis) viven en la capa **mod**, que es específica de cada lore.

### Los 4 agentes core

| Agente | Rol |
|--------|-----|
| `@bartleby` | Analista (read-only). Produce informes de 5 secciones. No juzga. |
| `@archivero` | Gestor del corpus. Diff, merge, status. Nunca analiza. |
| `@cristalizador` | Diseñador agéntico. Propone y crea artefactos nuevos en `mod/`. |
| `@portal-editorial` | Interfaz adaptativa según perfil de usuario. |

### Los 6 comandos

| Comando | Acción |
|---------|--------|
| `/guion` | Generar guion de ciclo editorial desde plantilla |
| `/feed` | Nueva editorial → análisis Bartleby → `.analisis.md` |
| `/diff-corpus` | Delta análisis vs `corpus/corpus.md` |
| `/merge-corpus` | Integrar hallazgos aprobados en `corpus/corpus.md` |
| `/design` | Cristalizador propone nuevos artefactos |
| `/status` | Estado del corpus |

## Capas del repositorio

```
.github/          → SDK puro (no modificar desde un mod)
  agents/         → 4 agentes core
  prompts/        → 6 comandos core (incluye /guion)
  skills/         → protocolo editorial-analysis
  hooks/          → automatismos del pipeline
  instructions/   → reglas de voz Bartleby
  templates/      → plantillas de documentos (guion de ciclo, etc.)

mod/              → artefactos creados por el cristalizador para este lore
  agents/         → agentes nuevos propuestos por cristalizador
  prompts/        → comandos nuevos
  skills/         → taxonomía base y ejemplos del lore
  hooks/          → hooks específicos del mod
  instructions/   → instrucciones específicas del mod

corpus/           → datos del lore (editoriales, análisis, mapa)
  editoriales/    → textos originales verbatim
  analisis/       → informes Bartleby (.analisis.md)
  corpus.md       → mapa acumulativo de taxonomía y linajes

guiones/          → roadmaps de ciclo editorial (.guion.md) — uno por editorial

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
