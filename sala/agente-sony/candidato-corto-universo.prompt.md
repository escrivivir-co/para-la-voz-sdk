---
name: corto-universo
description: "Genera un corto literario desde una rama del grafo de universos del mod activo. Cada invocación produce un fichero sufijado con el nombre del modelo."
argument-hint: "[universo-1 | universo-2 | ...]"
agent: Dramaturgo Cortos
tools: [vscode, execute, read, agent, edit, search, todo]
---

# /corto-universo — Generar corto desde rama del grafo

Genera una pieza literaria (corto) desde una rama específica del grafo de universos instanciado.

> **Instrucciones del mod activo:** carga `mod/instructions/legislativa-universo.instructions.md` para reglas de voz y peculiaridades del lore.

## Contexto que debes cargar

Lee estos ficheros en orden antes de hacer nada:

1. **Grafo principal** — `DRAFTS2/LORE_F-02_UNIVERSO.md` (nodos T=0, pivote X, ramas R1–R4, metadatos)
2. **Rama solicitada** — e.g., `DRAFTS2/universo/universo-1.md` para R4 (ajusta según argumento)
3. **Reglas de construcción** — `DRAFTS2/LORE_F-02_ARTEFACTO.md` — las 5 reglas son vinculantes
4. **Corto de referencia** — `DRAFTS2/LORE_F-02_CORTO.md` — tono, registro y longitud canónicos
5. **Instrucciones del mod** — `mod/instructions/legislativa-universo.instructions.md`

## Qué haces

### Paso 1 — Plan

Presenta un plan al usuario con:

- Nodos del grafo que activarás (lista con IDs)
- Huecos que elides o mantienes como tensión narrativa
- Registro literario elegido (prosa interior / narración externa / fragmento epistolar / etc.)
- Estructura de movimientos (2–4 movimientos con título provisional)
- Duración estimada (páginas o palabras)

**Espera aprobación del usuario antes de escribir.**

### Paso 2 — Escritura

Una vez aprobado el plan:

1. Escribe la pieza en prosa narrativa aplicando:
   - Las 5 reglas del artefacto (`LORE_F-02_ARTEFACTO.md`)
   - Los 3 ejes de drama de futures-engine (si está disponible)
   - La voz y registro canónicos de `LORE_F-02_CORTO.md`

2. Guarda como `DRAFTS2/LORE_F-02_CORTO-{{universo}}-{{modelo}}.md`
   - `{{universo}}` = argumento recibido (e.g., `universo-1`)
   - `{{modelo}}` = tu propio nombre de modelo en kebab-case (e.g., `claude-sonnet-4-6`)
   - Si el nombre ya existe, añade `-2`, `-3`, etc.

3. Actualiza el campo `Obras generadas` en los metadatos del universo correspondiente.

## Argumento

```
/corto-universo universo-1
```

Produce: `DRAFTS2/LORE_F-02_CORTO-universo-1-{modelo}.md`

## Múltiples versiones

Cambiar de modelo en el picker y volver a invocar el prompt produce otro fichero con distinto sufijo de modelo. Los ficheros **no se sobreescriben**. El sistema de sufijos garantiza trazabilidad por modelo.

## Salida esperada

- `DRAFTS2/LORE_F-02_CORTO-{{universo}}-{{modelo}}.md` — pieza literaria completa
- Metadatos del universo actualizados (`Obras generadas`)
- Confirmación breve en chat: título de la pieza + ruta del fichero
