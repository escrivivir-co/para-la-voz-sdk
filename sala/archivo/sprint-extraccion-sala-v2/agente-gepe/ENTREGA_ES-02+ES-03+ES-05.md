# ENTREGA ES-02+ES-03+ES-05 — GPT-5.4

## Resumen del resultado

- Generalicé los 7 prompts de sala para promoción a SDK, sustituyendo rutas fijas por `{{SALA_DIR}}` y quitando referencias al lore legislativa.
- Promoví `sala-protocolo.instructions.md` al SDK manteniendo intactas las secciones §1–§6 y verifiqué que `plan-attribution.instructions.md` ya es portable.
- Añadí una sección "Sala de coordinación" a `copilot-instructions.md` del SDK sin duplicar el protocolo operativo.
- Decisión de diseño: `sala-aleph.prompt.md` **sí** es portable si la sala concreta aporta `{{SALA_DIR}}/activacion-orquestador.md` como manual local.

## Ficheros producidos en carpeta

- `candidatos/.github/prompts/sala-entrar.prompt.md` → destino final `.github/prompts/sala-entrar.prompt.md`
- `candidatos/.github/prompts/sala-seguir.prompt.md` → destino final `.github/prompts/sala-seguir.prompt.md`
- `candidatos/.github/prompts/sala-aprobar.prompt.md` → destino final `.github/prompts/sala-aprobar.prompt.md`
- `candidatos/.github/prompts/sala-reconectar.prompt.md` → destino final `.github/prompts/sala-reconectar.prompt.md`
- `candidatos/.github/prompts/sala-salir.prompt.md` → destino final `.github/prompts/sala-salir.prompt.md`
- `candidatos/.github/prompts/sala-archivar.prompt.md` → destino final `.github/prompts/sala-archivar.prompt.md`
- `candidatos/.github/prompts/sala-aleph.prompt.md` → destino final `.github/prompts/sala-aleph.prompt.md`
- `candidatos/.github/instructions/sala-protocolo.instructions.md` → destino final `.github/instructions/sala-protocolo.instructions.md`
- `candidatos/.github/instructions/plan-attribution.instructions.md` → destino final `.github/instructions/plan-attribution.instructions.md`
- `candidatos/.github/copilot-instructions.md` → destino final `.github/copilot-instructions.md`

## Pasos para Aleph

1. Copiar los 7 prompts candidatos a `.github/prompts/`.
2. Copiar las 2 instructions candidatas a `.github/instructions/`.
3. Aplicar la actualización de `.github/copilot-instructions.md` desde el candidato de esta carpeta.
4. Al ejecutar ES-04, decidir si la plantilla de sala incluye también `activacion-orquestador.md` o si ese manual queda explícitamente como artefacto local por sala.
5. Si la revisión pasa, cerrar ES-02, ES-03 y ES-05 de forma atómica en tablero + `estado.md`.

## Observaciones

- No escribí fuera de `DRAFTS2/sala/agente-gepe/`.
- Los candidatos quedaron preparados para copy/paste limpio al SDK; no dependen de `DRAFTS2/` ni de `mod/legislativa`.