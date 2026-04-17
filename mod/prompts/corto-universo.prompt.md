---
name: corto-universo
description: "Genera un corto literario desde una rama del grafo de universos. Cada invocación produce un fichero sufijado con el nombre del modelo."
argument-hint: "[universo-1 | universo-2 | ...]"
agent: Dramaturgo Cortos
tools: [vscode, execute, read, agent, edit, search, web, browser, todo]
---

# /corto-universo — Generar corto desde rama del grafo

Genera una pieza literaria (corto) desde una rama específica del grafo de universos del caso Zoowoman.

## Contexto que debes cargar

Lee estos ficheros en orden antes de hacer nada:

1. [Estado del lore](../../DRAFTS2/LORE_F-02_UNIVERSO.md) — grafo principal, nodos T=0, pivote X, ramas R1-R4, metadatos
2. La rama solicitada — e.g., [universo/universo-1.md](../../DRAFTS2/universo/universo-1.md) para R4
3. [Reglas de construcción](../../DRAFTS2/LORE_F-02_ARTEFACTO.md) — las 5 reglas son vinculantes, la ficha técnica fija el marco
4. [Corto original](../../DRAFTS2/LORE_F-02_CORTO.md) — *Tres Lunes Para Una Misma Sala* — referencia de tono, registro y longitud
5. [Instrucciones del mod](../instructions/legislativa-universo.instructions.md) — peculiaridades del lore legislativa que no están en los ficheros generales

## Qué haces

1. **Lees** todo lo anterior
2. **Presentas plan**: nodos que activarás, huecos que elides o dejas como tensión, registro literario, estructura de movimientos, duración estimada
3. **Esperas aprobación** del usuario
4. **Escribes** la pieza en prosa narrativa aplicando las 5 reglas del artefacto y los 3 ejes de drama de futures-engine
5. **Guardas** como `DRAFTS2/LORE_F-02_CORTO-[universo]-[modelo].md` donde `[modelo]` es tu propio nombre de modelo en kebab-case
6. **Actualizas** metadatos del universo (campo "Obras generadas")

## Ejemplo de invocación

```
/corto-universo universo-1
```

Produce: `DRAFTS2/LORE_F-02_CORTO-universo-1-claude-sonnet-4.md` (si el modelo activo es Claude Sonnet 4)

## Múltiples versiones

Cambiar de modelo en el picker y volver a invocar `/corto-universo universo-1` produce otro fichero con otro sufijo. No se sobreescriben. Si por alguna razón el nombre coincide, añade `-2`, `-3`, etc.
