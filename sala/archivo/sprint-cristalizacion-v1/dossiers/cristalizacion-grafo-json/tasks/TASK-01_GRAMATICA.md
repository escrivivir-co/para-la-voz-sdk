# TASK-01 — Gramática legible

> **Estado:** pendiente
> **Agente recomendado:** `Cristalizador`
> **Dependencias:** GJ-00
> **Entrega esperada:** `DRAFTS2/grafo/gramatica.md`

## Lee primero

- [Plan local §4 — Diseño de la gramática](../PLAN_GRAFO_JSON.md)
- [LORE_F-02_ARTEFACTO.md §Ficha técnica](../../LORE_F-02_ARTEFACTO.md) — reglas de construcción originales

## Objetivo

Escribir la spec legible de la gramática JSON del grafo. Este fichero es la referencia para humanos y para agentes que necesiten entender las reglas sin parsear JSON.

## Contenido esperado

1. **Tipos de nodo:** `estado`, `bifurcacion`, `rama`, `hueco` — con campos obligatorios y opcionales.
2. **Estratos temporales:** `T0`, `T0-X`, `X`, `X-Tinf` — semántica de cada uno.
3. **Formato de IDs:** `<estrato>.<número>` para nodos regulares, IDs nominales para pivote.
4. **Arcos:** origen→destino con peso y justificación. Ambos extremos deben existir.
5. **Huecos:** declarados explícitamente, no como `[?]` suelto en texto.
6. **Regla de vocabulario cerrado:** toda pieza ancla referenciada debe existir en el corpus.
7. **Versionado:** cómo se incrementa la versión si cambia la gramática.

## Criterio de aceptación

Un agente que lea `gramatica.md` puede validar cualquier fichero JSON del grafo sin ambigüedad.
