# PLAN INICIAL — Finalización del LORE_PLAN

> **Fecha:** 19-abr-2026
> **Modelo:** `Claude Opus 4.6`
> **Estado:** abierto
> **Anclas:** `DRAFTS2/LORE_PLAN.md`, `DRAFTS2/LORE_INDEX.md`, `DRAFTS2/mod_legislativa_INDEX.md`
> **Protocolo:** según `mod/skills/cristalizacion-feature/SKILL.md`

---

## [Claude Opus 4.6] Inicialización del plan base

Este dossier cubre la transición de `LORE_PLAN.md` de **borrador de trabajo** a **documento rector final**. El plan existe desde el Sprint 0 y ha acumulado decisiones, PBIs completados y sprints reales, pero nunca se cerró formalmente como spec definitiva.

---

## 1. Contexto DRY

| Qué | Dónde | Estado |
|-----|-------|--------|
| LORE_PLAN.md | [DRAFTS2/LORE_PLAN.md](../LORE_PLAN.md) | 11 secciones, 22 PBIs, 5 sprints + sprint emergente |
| LORE_INDEX.md | [DRAFTS2/LORE_INDEX.md](../LORE_INDEX.md) | 51 piezas, mapa de bloques |
| mod_legislativa_INDEX.md | [DRAFTS2/mod_legislativa_INDEX.md](../mod_legislativa_INDEX.md) | spec de la separación SDK/mod/lore |
| Estado canónico (futuro) | `mod/instructions/lore-estado.instructions.md` | No existe aún (dossier pipeline-operativo PO-02) |
| Schema de tipos (futuro) | `mod/instructions/lore-schema.instructions.md` | No existe aún (dossier pipeline-operativo PO-01) |

## 2. Agentes involucrados

- **`@Cristalizador`** — ejecuta las ediciones al plan.
- **`@Archivero Lore`** — valida que los conteos y estados reflejen la realidad del lore.

## 3. Restricciones

- No tocar `.github/`.
- El LORE_PLAN sigue en `DRAFTS2/` (es del caso, no del mod ni del SDK).
- No duplicar información que vivirá en `lore-schema` o `lore-estado` cuando se creen.
- Preservar las decisiones ya tomadas (DoR, DoD, reglas por formato).

---

## 4. Problemas identificados

### 4.1. Desync de conteos

El plan original habla de cantidades implícitas y prioridades que ya no son actuales. Ejemplo: §10 "siguiente lote prioritario" recomienda P-01, P-09, T-09 y refactor LORE_F — los cuatro ya están hechos.

### 4.2. Estado de PBIs desactualizado

La tabla del §8 tiene 22 PBIs. Varios están marcados como "Hecho" pero otros pueden haber avanzado sin actualizar la tabla. Necesita reconciliación contra disco.

### 4.3. Sprints sin cierre

Los sprints 0–3 + emergente tienen marcas de completitud parcial. Sprint 4 y 5 están pendientes. No hay cierre formal ni retrospectiva.

### 4.4. Falta de referencia a la cadena agéntica

El plan no menciona la cadena de 5 agentes, el pipeline de refresh ni el grafo JSON. Estos son features nuevos que impactan el flujo de trabajo del lore.

### 4.5. DoR/DoD migrarán al schema

Las §5 y §6 (Definition of Ready / Done) están en el plan, pero por decisión del dossier pipeline-operativo (§4 diálogo, aceptación de Pipeline) migrarán a `lore-schema.instructions.md`. El plan debería referenciar el schema en lugar de mantener la copia.

---

## 5. Plan de finalización

| Paso | Acción | Descripción |
|------|--------|-------------|
| LP-01 | Reconciliar PBIs | Contrastar tabla §8 contra disco: qué ficheros existen, qué está realmente Hecho/Pendiente/Bloqueado |
| LP-02 | Actualizar sprints | Cerrar sprints completados con marca de fecha. Actualizar Sprint 3 (parcial). Ajustar Sprint 4-5 si procede |
| LP-03 | Eliminar §10 redundante | "Siguiente lote prioritario" ya está cumplido. Sustituir por referencia al backlog vivo |
| LP-04 | Añadir sección de features agénticos | Referenciar los 3 dossiers de cristalización como FEAT-06, FEAT-07, FEAT-08 del plan |
| LP-05 | Preparar DRY para schema | Marcar §5 y §6 como "fuente temporal, migrará a lore-schema.instructions.md cuando se cree" |
| LP-06 | Actualizar conteos | Sincronizar todos los números con LORE_INDEX.md (51 piezas) |
| LP-07 | Marcar como final | Cambiar cabecera "Estado: documento rector de trabajo" → "Estado: documento rector — v1.0 final" |
| LP-08 | Validar | Archivero Lore verifica coherencia plan ↔ disco |

---

## 6. Resumen de entregas

| # | Artefacto | Ruta | Tipo | Dependencias |
|---|-----------|------|------|-------------|
| LP-01 | Reconciliación de PBIs | edición `LORE_PLAN.md` §8 | edición | Ninguna |
| LP-02 | Cierre de sprints | edición `LORE_PLAN.md` §9 | edición | LP-01 |
| LP-03 | Eliminar §10 redundante | edición `LORE_PLAN.md` §10 | edición | LP-01 |
| LP-04 | Sección features agénticos | edición `LORE_PLAN.md` §7 | edición | Ninguna |
| LP-05 | Preparar DRY para schema | edición `LORE_PLAN.md` §5, §6 | edición | Ninguna |
| LP-06 | Actualizar conteos | edición `LORE_PLAN.md` | edición | LP-01 |
| LP-07 | Marcar como final | edición `LORE_PLAN.md` cabecera | edición | LP-01..LP-06 |
| LP-08 | Validación | informe en dossier | validación | LP-07 |

---

## Salida operativa

- Tracking: [BACKLOG_LORE_PLAN.md](./BACKLOG_LORE_PLAN.md)
- Respuestas: [RESPUESTAS_USUARIO_LORE_PLAN.md](./RESPUESTAS_USUARIO_LORE_PLAN.md)
- Tasks: carpeta [tasks](./tasks)
