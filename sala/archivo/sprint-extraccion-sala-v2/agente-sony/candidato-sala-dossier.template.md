# Dossier: {{NOMBRE_DOSSIER}}

> **Sprint:** {{NOMBRE_SPRINT}}
> **Dossier ID:** {{DOSSIER_ID}}
> **Fecha de creación:** {{FECHA}}
> **Autor:** {{AUTOR}}

## Resumen

{{DESCRIPCION_CORTA}}

## Estructura de este dossier

```
DRAFTS2/{{DOSSIER_ID}}/
  PLAN_{{DOSSIER_ID_UPPER}}.md          ← este fichero
  BACKLOG_{{DOSSIER_ID_UPPER}}.md       ← lista de tasks con criterios de aceptación
  RESPUESTAS_{{DOSSIER_ID_UPPER}}.md    ← decisiones y respuestas a preguntas del diseño
  activacion.prompt.md                  ← prompt de activación para Aleph
  tasks/
    TASK-01_{{NOMBRE_TASK}}.md
    TASK-02_{{NOMBRE_TASK}}.md
    ...
```

## Objetivo

{{OBJETIVO_DETALLADO}}

## Scope

### Incluye

- {{ITEM_SCOPE_1}}
- {{ITEM_SCOPE_2}}

### Excluye

- {{ITEM_EXCLUSION_1}}

## Tasks

| ID | Título | Deps | Agente sugerido |
|----|--------|------|-----------------|
| {{DOSSIER_ID_UPPER}}-01 | {{TITULO}} | — | cualquiera |
| {{DOSSIER_ID_UPPER}}-02 | {{TITULO}} | {{DOSSIER_ID_UPPER}}-01 | cualquiera |

> **Paralelo:** {{NOTA_PARALELISMO}}

## Criterios de cierre del dossier

- [ ] Todas las tasks en estado `cerrada`
- [ ] Artefactos copiados a sus destinos definitivos
- [ ] Tablero actualizado

## Notas de diseño

{{NOTAS_DISENO}}
