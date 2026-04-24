---
name: pipeline-refresh
description: "Refresca la cadena de derivados del pipeline tras modificar piezas del lore."
argument-hint: "[status | --desde corpus|hilo|artefacto|universo]"
agent: Pipeline
tools: [vscode, execute, read, agent, edit, search, todo]
---

# /pipeline-refresh — Refrescar pipeline

Invoca el protocolo de `@Pipeline` para revisar y, si hace falta, refrescar la cadena de derivados del lore.

## Reglas de uso

1. Si el usuario pide solo diagnóstico, interpreta la invocación como `status`.
2. Si no especifica argumento, ejecuta `refresh` completo.
3. Si proporciona `--desde [nodo]`, empieza en ese punto respetando el protocolo documentado en [../../DRAFTS2/FEAT-06_PIPELINE_REFRESH.md](../../DRAFTS2/FEAT-06_PIPELINE_REFRESH.md).
4. Presenta siempre delta por nivel y ofrece handoffs al terminar.