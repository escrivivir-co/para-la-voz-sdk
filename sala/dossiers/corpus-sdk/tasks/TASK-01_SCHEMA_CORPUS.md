# TASK-01 — Schema portable de corpus

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** CS-00
> **Entrega esperada:** `.github/instructions/corpus-schema.instructions.md`

## Objetivo

Definir el contrato portable de la capa corpus para cualquier mod del SDK.

## Debe cubrir

1. La estructura mínima:
   - `corpus/documentos/`
   - `corpus/analisis/`
   - `corpus/corpus.md`
2. La relación con `{{LORE_DIR}}/piezas/` cuando un mod tenga lore-db propia.
3. La coexistencia de dos modos válidos:
   - flujo incremental documental
   - flujo batch desde piezas ya validadas
4. Qué se considera fuente, análisis y mapa acumulativo.

## Qué no hace

- No define tipos concretos del lore.
- No migra ningún dato de legislativa.

## Criterio de aceptación

- Existe un contrato reutilizable y no legislativa-specific.