# Respuestas del usuario — Finalización del LORE_PLAN

> **Fecha:** 19-abr-2026
> **Registradas por:** `Claude Opus 4.6`
> **Propósito:** fijar las decisiones de PO, scrum master y cliente en disco.

## Punto 1 — LORE_PLAN debe ser final (PO)

- **Decisión del PO:** "Pasarlo ya a final." El plan ha sido borrador de trabajo desde Sprint 0. Tiene que reflejar el estado real y cerrarse como documento rector v1.0.
- **Efecto operativo:** Reconciliar PBIs, cerrar sprints, actualizar conteos, marcar como final.

## Punto 2 — No duplicar lo que vivirá en schema/estado (PO + cliente)

- **Decisión compartida:** Las DoR/DoD (§5, §6) y la tabla de formatos (§3.1) son candidatas a migrar a `lore-schema.instructions.md`. El plan debe marcarlas como "fuente temporal" y no ser la autoridad una vez que el schema exista.
- **Efecto operativo:** LP-05 añade nota DRY en §5 y §6.

## Punto 3 — Referenciar los features agénticos (PO)

- **Decisión del PO:** El plan original no preveía la cadena agéntica, el grafo JSON ni el pipeline operativo. Esos son features reales del proyecto que deben estar en §7.
- **Efecto operativo:** LP-04 añade FEAT-06 (pipeline operativo), FEAT-07 (cadena agéntica), FEAT-08 (grafo JSON) con referencias a sus dossiers.

## Punto 4 — El plan sigue en DRAFTS2 (PO)

- **Decisión del PO:** El LORE_PLAN es del caso, no del mod ni del SDK. Se queda en DRAFTS2 incluso cuando sea final.
- **Efecto operativo:** Sin cambio de ubicación.
