---
name: universo
description: Crear o expandir un universo propio — grafo conversacional de futuros ramificados desde el corpus.
argument-hint: "[crear nuevo | expandir existente | generar obra desde grafo]"
agent: Dramaturgo
tools: [vscode, execute, read, agent, edit, search, web, browser, todo]
---

# /universo — Diseñar un universo propio

Activa al `@dramaturgo` para construir o expandir un **universo propio**: un grafo de futuros ramificados desde el corpus, construido conversacionalmente.

## Flujo de entrada

1. **Leer** `corpus/corpus.md` — estado actual del corpus
2. **Buscar universos existentes** en el mod:
   - `mod/universos/` si existe
   - Cualquier archivo `*.universo.md` en el mod
   - Para el lore legislativa: `DRAFTS2/LORE_F-02_ARTEFACTO.md` como grafo semilla candidato
3. **Detectar qué quiere el usuario:**
   - Si especificó argumento (`crear nuevo` / `expandir existente` / `generar obra`): seguir ese camino
   - Si no especificó: presentar estado y preguntar

## Tres caminos

### crear nuevo
No hay universo activo. El dramaturgo:
1. Construye grafo semilla desde el corpus (nodos T=0, bifurcaciones detectadas en T+1)
2. Presenta el grafo con plausibilidades
3. Pregunta: ¿expandimos esta línea o prefieres otra?

### expandir existente
Hay un universo activo. El dramaturgo:
1. Presenta el estado actual del grafo (nodos, arcos, ramas activas, caminos no tomados)
2. Propone las 2-3 expansiones más productivas según las tensiones abiertas
3. Pregunta: ¿cuál seguimos?

### generar obra desde grafo
Hay un universo activo. El dramaturgo:
1. Presenta las ramas disponibles del grafo
2. Pregunta: ¿desde qué rama o estado del grafo generamos la obra?
3. Aplica tratamiento literario (Fase 5 del skill futures-engine) sobre la selección
4. Ofrece persistir la obra en el mod

## Conversación libre
Si el usuario no usa ninguna de estas palabras clave, el dramaturgo detecta la intención y elige el camino más adecuado.

## Nota de uso
Una vez activo el flujo, la conversación es abierta. El usuario puede pedir:
- "expandir la línea del recurso"
- "¿qué pasa si el archivo reaparece?"
- "dame el relato desde la absolución"
- "¿cuál es el camino más probable ahora?"
- "guarda el grafo como YAML"

El dramaturgo responde operando sobre el grafo — sin salirse del corpus.
