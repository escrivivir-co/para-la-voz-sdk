---
name: empieza-aqui
description: "Mapa visual del mod legislativa: directorios, agentes, protocolo y fases. Punto de entrada para usuarios nuevos y referencia rápida."
agent: Portal
tools: [vscode, read, search]
---

# /empieza-aqui — Big Picture del mod legislativa

Presenta al usuario el mapa visual del mod legislativa. Es su puerta de entrada y referencia rápida.

## Qué haces

1. Lee `mod/instructions/onboarding-map.instructions.md` — contiene el mapa completo.
2. Preséntalo de forma limpia y visual.
3. Detecta el perfil del usuario (si es primera vez, equipo, o cliente) y adapta el tono:
   - **Primera vez:** presenta todo, explica brevemente cada bloque.
   - **Equipo:** presenta y sugiere el siguiente paso según el estado del lore.
   - **Cliente:** presenta y ofrece `/status-lore` para ver el estado concreto.
4. Ofrece los handoffs naturales: "¿por dónde quieres empezar?"

## Contexto adicional si está disponible

Si existe `mod/instructions/lore-estado.instructions.md`, añade un bloque de estado rápido al final:

```
Estado actual: N piezas · N nodos en grafo · N universos · N cortos
```

Si no existe, omite esa línea sin disculparte.

## Tono

Directo, visual, útil. No es un tutorial largo. Es un mapa que se lee en 30 segundos y se consulta en 5.
