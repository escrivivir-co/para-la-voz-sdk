# Plan — scrum-backlog-lore-db-vector-expansion

> **Fecha:** 22-abr-2026
> **Autor:** GPT-5.4
> **Dossier:** `sala/dossiers/scrum-backlog-lore-db-vector-expansion/`

## 1. Contexto

Este dossier es el espejo **local y DRY** del feature `scrum-backlog-lore-db-vector-expansion` para el equipo de `DocumentMachineSDK`. No duplica el plan compartido: lo referencia y lo traduce a backlog del subequipo documental.

La sesión de hoy ya dejó trabajo avanzado suficiente. Aquí no se vuelve a investigar la arquitectura general; se inicializa el frente local para que el siguiente paso sea **aprobar o enmendar el plan** y después refinar la parte de skill, layout de datos y handoff hacia Scriptorium.

## Contexto compartido

- `sala/dossiers/scrum-backlog-lore-db-vector-expansion/ref/INDEX.md`
- `sala/dossiers/lore-db-sdk/PLAN.md`
- `../../../../sala/dossiers/scrum-backlog-lore-db-vector-expansion/PLAN.md`
- `../../../../sala/PLAN-VECTOR/PLAN.md`

## 2. Anclas

- El plan compartido y las decisiones del PO ya existen fuera de este dossier; aquí se referencian, no se reescriben.
- `DocumentMachineSDK` es dueño del skill local y del layout `lore-db/` + `lore-db-vector/`.
- `LORE_F` se maneja como fichero completo trabajado fuera del server; la validación comprueba referencias contra la DB.
- La topología server/datos ya está fijada: server en Scriptorium, datos y skill aquí.

## 3. Restricciones

- No duplicar el plan compartido ni el diseño del server MCP.
- Este dossier solo cubre el refinement del frente documental.
- El backlog es índice y tracking. El detalle vive en `tasks/`.

## 4. Propuesta

### 4.1 Inicialización de la sesión

La sesión local queda inicializada con dos tareas ya cerradas:

- `SBLVX-DM-00` — pre-scrum definitions local
- `SBLVX-DM-01` — planification local DRY

### 4.2 Siguiente paso

El siguiente paso visible es:

- **aprobar el plan o enmendarlo** desde la perspectiva `DocumentMachineSDK` (`SBLVX-DM-02`)

Después se abre el refinement local para:

- concretar el skill/local bootstrap y el layout de datos (`SBLVX-DM-03`)
- preparar el handoff documental hacia la integración posterior (`SBLVX-DM-04`)

## 5. Salida operativa

- Tracking: [BACKLOG.md](./BACKLOG.md)
- Decisiones del PO: [RESPUESTAS.md](./RESPUESTAS.md)
- Activación del dossier: [activacion.prompt.md](./activacion.prompt.md)
- Referencias DRY: carpeta [ref](./ref)
- Tasks: carpeta [tasks](./tasks)