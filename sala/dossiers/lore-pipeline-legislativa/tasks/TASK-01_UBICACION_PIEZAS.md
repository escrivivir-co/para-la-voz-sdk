# TASK-01 — Decidir e implementar ubicación definitiva de piezas

> **Estado:** libre
> **Agente recomendado:** PO (decisión) + cualquiera (ejecución)
> **Dependencias:** LP-00
> **Entrega esperada:** Decisión documentada en RESPUESTAS + migración (si aplica)

## Lee primero

- [Plan §4.1](../PLAN.md)
- `mod/instructions/lore-routing.instructions.md` — mapa actual
- `DRAFTS2/LORE_INDEX.md` — inventario de 51 piezas

## Objetivo

Decidir la ubicación canónica de las piezas y ejecutar la migración si cambia.

## Opciones

| Opción | Ruta | Pros | Contras |
|--------|------|------|---------|
| A | `corpus/piezas/` | Alineado con estructura SDK (`corpus/documentos/`) | Requiere migrar 40+ ficheros, actualizar todas las refs |
| B | `lore/` (renombrar DRAFTS2) | Nombre limpio, mínimo cambio de paths | Pierde historial git de DRAFTS2 si se usa `mv` |
| C | `DRAFTS2/` formalizado | Zero migration, solo actualizar routing | Nombre feo, marca de "borrador" permanente |

## Checklist de ejecución (post-decisión)

- [ ] Documentar decisión en RESPUESTAS.md
- [ ] Definir `{{PIEZA_DIR}}` en lore-routing
- [ ] Migrar ficheros si aplica (git mv para preservar historial)
- [ ] Actualizar refs en todos los ficheros que apuntan a la ruta vieja
- [ ] Verificar que pipeline, agentes, instructions siguen funcionando

## Criterio de aceptación

`{{PIEZA_DIR}}` resuelto, piezas en su ubicación definitiva, routing actualizado.
