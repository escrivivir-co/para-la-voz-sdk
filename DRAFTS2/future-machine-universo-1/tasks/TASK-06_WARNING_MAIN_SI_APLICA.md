# TASK-06 — Warning para main si aplica

> **Estado:** condicional
> **Agente recomendado:** `Explore` o `Cristalizador`
> **Dependencias:** evidencia real de fallo
> **Entrega esperada:** `DRAFTS2/future-machine-universo-1/WARNING_MAIN__COPILOT_LINKAGE.md`

## Objetivo

Abrir warning para el equipo `main` solo si se demuestra que la rama core no deja bien enlazado al Cristalizador con su fuente de documentación `COPILOT/` o con las capacidades que debería ver.

## No hacer

- No abrir este warning por sospecha.
- No convertirlo en bloqueante para `mod/legislativa`.

## Evidencia mínima requerida

1. Fallo reproducible.
2. Ruta o capacidad ausente claramente identificada.
3. Impacto concreto sobre la intervención future-machine.

## Criterio de aceptación

Si el fallo existe, el warning deja una nota útil para `main`. Si no existe, esta task permanece sin ejecutar.