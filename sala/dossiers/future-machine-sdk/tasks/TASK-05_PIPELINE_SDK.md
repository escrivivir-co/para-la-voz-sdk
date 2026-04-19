# TASK-05 — @Pipeline SDK genérico

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** FS-01
> **Entrega esperada:** `.github/agents/pipeline.agent.md`

## Lee primero

1. `mod/agents/pipeline.agent.md` en `mod/legislativa` — el Pipeline validado que sirve de evidencia
2. `DRAFTS2/FEAT-06_PIPELINE_REFRESH.md` en `mod/legislativa` — spec vinculante del refresh
3. `.github/instructions/future-machine-schema.instructions.md` — el schema de slots (FS-01)
4. Sección 0 de `sala/dossiers/future-machine-sdk/PLAN.md` — tabla del pipeline completo

## Objetivo

Crear un agente `@Pipeline` en el SDK que defina el **protocolo genérico de refresh** de la cadena sin hardcodear agentes ni rutas concretas del mod. El mod hereda y rellena con su cadena.

## Contrato del agente

El Pipeline SDK:

1. Lee el manifiesto `FUTURE_MACHINE.md` para saber qué slots existen y qué agentes los sirven
2. Detecta desincronización entre slots comparando timestamps y deltas entre niveles
3. Recorre la cadena en orden (upstream → downstream), parando si un nivel no cambió
4. Delega a los agentes que el mod haya registrado en cada slot
5. Ofrece handoffs al terminar

### Modos de entrada

- `status` — presenta el estado actual del pipeline sin editar nada
- `refresh` — ejecuta el protocolo completo de refresh
- `refresh --desde [nodo]` — empieza desde el nodo indicado

### Lo que NO define

- La cadena concreta de agentes (eso es del mod)
- Handoffs concretos (el mod los inyecta)
- Reglas de dominio como "CORPUS_PREVIEW y LORE_F son hermanos" (eso es del mod)

### Frontmatter mínimo

```yaml
name: Pipeline
description: "Orquestador de refresh del ciclo lore → corpus → grafo → universo → obra. Lee el manifiesto de la machine, detecta desincronización y recorre la cadena."
argument-hint: "[status | refresh | refresh --desde corpus|grafo|universo]"
tools: [vscode, execute, read, agent, edit, search, todo]
agents: []  # el mod inyecta los suyos
handoffs: [] # el mod los define según su cadena
```

## Salida mínima esperada

1. `.github/agents/pipeline.agent.md` con contrato genérico
2. ENTREGA con diff respecto al Pipeline de mod/legislativa (qué se generalizó, qué se dejó para el mod)

## Criterio de aceptación

- El agente existe en `.github/agents/` y es funcional con un manifiesto vacío (solo muestra "no hay machine configurada")
- `mod/legislativa` puede heredar el Pipeline SDK y añadir su cadena concreta sin conflicto
- No se hardcodean nombres de agentes, rutas de DRAFTS2 ni vocabulario del caso Feo
