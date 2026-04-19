# TASK CU-01 — Crear corto-universo.prompt.md

- **Tipo:** prompt
- **Destino:** `mod/prompts/corto-universo.prompt.md`
- **Estado:** libre
- **Agente sugerido:** cualquiera

## Descripción

Crear el prompt que active al Dramaturgo Cortos para generar un corto literario desde un universo instanciado.

## Criterios de aceptación

1. Fichero existe en `mod/prompts/corto-universo.prompt.md`
2. Usa `@dramaturgo` como agente (o Dramaturgo Cortos)
3. Input esperado: nombre del universo + rama (opcional)
4. Output esperado: fichero `LORE_F-NN_CORTO-{universo}-{modelo}.md`
5. Referencia a `legislativa-universo.instructions.md` para reglas de voz
