# Plan — cortos-sdk

> **Fecha:** 19-abr-2026
> **Autor:** GPT-5.4
> **Dossier:** `sala/dossiers/cortos-sdk/`

## 1. Contexto

La cadena ya separa tres capas downstream del corpus:

```
grafo -> universos -> cortos
```

La parte de **cortos** no debe quedar absorbida dentro de `universos-sdk`, porque introduce una fase distinta:

- agente distinto (`@Dramaturgo` / extensiones del mod)
- persistencia distinta (múltiples versiones por modelo)
- reglas de escritura y guardado distintas
- validación distinta: una cosa es persistir ramas; otra, persistir obras derivadas

El SDK ya tiene al Dramaturgo como agente base y el skill `futures-engine` ya describe el tratamiento literario. Lo que falta cristalizar es la **capa persistente de obra derivada desde universo**.

Relación con otros dossiers:

| Dossier | Branch | Qué hace | Relación |
|---------|--------|----------|----------|
| `grafo-sdk` | main | Contrato genérico de grafo | Upstream lejano |
| `universos-sdk` | main | Contrato portable de universo persistido | Upstream directo |
| **cortos-sdk** | main | **Contrato portable de obras derivadas por modelo** | Este dossier |
| `cortos-legislativa` | mod/legislativa | Migra y adapta los cortos concretos del caso | Hereda este contrato |

## 2. Anclas

| Artefacto | Ubicación | Estado |
|-----------|-----------|--------|
| Dramaturgo SDK | `.github/agents/dramaturgo.agent.md` | Ya contempla `generar obra` desde el grafo |
| Skill futures-engine | `.github/skills/futures-engine/SKILL.md` | Ya define la Fase 5 de tratamiento literario |
| Dramaturgo Cortos (mod) | `mod/agents/dramaturgo.agent.md` | Persistencia actual ligada a `DRAFTS2/` |
| Cortos actuales | `DRAFTS2/LORE_F-02_CORTO*.md` | 5 ficheros |

## 3. Restricciones

- Este dossier **no migra datos** del caso legislativa.
- No crea un agente nuevo distinto de Dramaturgo en el SDK; cristaliza la convención portable que las extensiones del mod deben seguir.
- La capa de cortos es downstream del universo: no redefine la estructura del universo.

## 4. Propuesta

### 4.1. Schema genérico de corto derivado

Crear `.github/instructions/corto-schema.instructions.md` con:

- `obra_id`
- `universo_fuente`
- `modelo_generador`
- `registro_literario`
- `fecha_generacion`
- `artefacto_fuente`
- `grafo_fuente`

### 4.2. Template de corto

Crear `.github/templates/corto.template.md` con el header mínimo y el cuerpo de prosa narrativa.

### 4.3. Convención de ubicación y naming

Las obras derivadas viven en `{{LORE_DIR}}/derivados/cortos/`.

Naming portable:

```
LORE_F-02_CORTO-[universo]-[modelo].md
```

Si existe colisión, sufijo numérico (`-2`, `-3`).

### 4.4. Ajuste de Dramaturgo SDK

Ampliar `.github/agents/dramaturgo.agent.md` para documentar la persistencia de obras derivadas por modelo cuando el mod quiera materializarlas en disco.

### 4.5. Documentar la fase en copilot-instructions.md

Añadir la capa `cortos` a la secuencia persistente y a la convención de rutas.

## 5. Salida operativa

- Tracking: [BACKLOG.md](./BACKLOG.md)
- Decisiones del PO: [RESPUESTAS.md](./RESPUESTAS.md)
- Tasks: carpeta [tasks](./tasks)