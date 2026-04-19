# TASK-02 — Adaptar lore-schema para heredar del SDK

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** LP-00, PS-01 (dossier pieza-sdk)
> **Entrega esperada:** edición de `mod/instructions/lore-schema.instructions.md`

## Lee primero

- [Plan §4.2](../PLAN.md)
- `mod/instructions/lore-schema.instructions.md` — estado actual (6 tipos, ~200 líneas)
- `.github/instructions/pieza-schema.instructions.md` — protocolo genérico del SDK (cuando exista)

## Objetivo

Refactorizar lore-schema para que herede del SDK y defina solo lo específico de legislativa.

## Cambios esperados

1. **Cabecera:** añadir referencia al pieza-schema del SDK como base
2. **Ontología §1:** mantener los 6 tipos pero referenciar que el protocolo base de tipos viene del SDK
3. **Campos §2:** mantener campos específicos de legislativa (Emisor, Medio, Fase, etc.) y referenciar campos genéricos heredados (Marca, Tipo, Estado, Bloque principal)
4. **DoR/DoD §3-5:** mantener tal cual — son específicos del lore
5. **Reglas de conteo §6:** referenciar regla genérica del SDK + añadir excepciones de legislativa (F no suma, emergencias sí)

## Criterio de aceptación

`lore-schema` funciona igual que antes pero referencia el SDK para los conceptos genéricos.
