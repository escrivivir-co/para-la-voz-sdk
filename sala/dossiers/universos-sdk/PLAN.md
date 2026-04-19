# Plan — universos-sdk

> **Fecha:** 19-abr-2026
> **Autor:** GPT-5.4
> **Dossier:** `sala/dossiers/universos-sdk/`

## 1. Contexto

El SDK ya contiene la **lógica** de universos en el skill `futures-engine`: qué es un universo propio, cómo se bifurca y cómo se expande. Lo que todavía no está cristalizado en `.github/` es la **capa persistente** de universo:

- dónde vive un universo dentro de la lore-db
- qué metadatos mínimos debe guardar
- cómo se relaciona con el grafo del que nace
- cómo un agente SDK debe descubrir universos ya existentes antes de crear otros nuevos

Hoy esa capa vive de facto solo en el mod/legislativa:

- `mod/agents/demiurgo.agent.md` — instancia universos desde el grafo
- `DRAFTS2/universo/` — 3 universos persistidos (`universo-1`, `r1`, `r2`)
- `mod/instructions/legislativa-universo.instructions.md` — reglas y datos específicos del lore

Relación con otros dossiers:

| Dossier | Branch | Qué hace | Relación |
|---------|--------|----------|----------|
| `lore-db-sdk` | main | Estructura genérica de la lore-db | Provee `{{LORE_DIR}}` |
| `grafo-sdk` | main | Contrato genérico del grafo | Provee el upstream del universo |
| **universos-sdk** | main | **Contrato portable del universo persistido** | Este dossier |
| `universos-legislativa` | mod/legislativa | Migra y adapta los universos concretos del caso | Hereda este contrato |
| `cortos-sdk` | main | Contrato portable de obras derivadas por modelo | Downstream del universo |
| `future-machine-sdk` | main | Carcasa compositiva — `slot_universos` | **Downstream:** US-01 → FS-01, US-03 → FS-02 |

## 2. Anclas

| Artefacto | Ubicación | Estado |
|-----------|-----------|--------|
| Skill futures-engine | `.github/skills/futures-engine/SKILL.md` | Ya define el protocolo de universo propio |
| Demiurgo (mod) | `mod/agents/demiurgo.agent.md` | Operativo — instancia universos concretos |
| Future-machine archivado | `sala/archivo/sprint-cristalizacion-v1/dossiers/future-machine-universo-1/` | Referencia histórica |
| Universo-1 actual | `DRAFTS2/universo/` | 3 ficheros persistidos |

## 3. Restricciones

- Este dossier **no migra datos** del caso Feo. Solo cristaliza la capa portable en el SDK.
- En esta iteración **no** se crea `@Demiurgo` a nivel SDK. Demiurgo sigue siendo una especialización del mod.
- No se introducen campos específicos de legislativa ni vocabulario del caso.
- El universo es downstream del grafo y upstream de la obra: no reabre `grafo-sdk` ni absorbe la capa `cortos-sdk`.

## 4. Propuesta

### 4.1. Schema genérico de universo persistido

Crear `.github/instructions/universo-schema.instructions.md`:

Un universo persistido define, como mínimo:
- `universo_id`
- `grafo_fuente`
- `rama` o ramas activadas
- `nodos_activados`
- `huecos_resueltos` y `huecos_abiertos`
- `piezas_ancla`
- `obras_generadas`
- metadatos de corte temporal y última actualización

### 4.2. Template de universo

Crear `.github/templates/universo.template.md` para que cualquier mod pueda persistir un universo sin reinventar su estructura documental.

### 4.3. Convención de ubicación

El universo persistido vive en `{{LORE_DIR}}/derivados/universo/`. Es downstream del grafo y upstream de las obras derivadas.

### 4.4. Documentar en copilot-instructions.md

Añadir sección de universos persistidos al SDK con la relación:

```
lore-db -> corpus/hilo -> grafo -> universo -> obras
```

## 5. Salida operativa

- Tracking: [BACKLOG.md](./BACKLOG.md)
- Decisiones del PO: [RESPUESTAS.md](./RESPUESTAS.md)
- Tasks: carpeta [tasks](./tasks)