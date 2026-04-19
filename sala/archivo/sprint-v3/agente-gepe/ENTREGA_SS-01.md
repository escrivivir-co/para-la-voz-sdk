# ENTREGA_SS-01

> **Task:** SS-01
> **Alias:** Gepe
> **Modelo:** GPT-5.4
> **Fecha:** 2026-04-19T11:45:27+02:00

## Resumen

Verificación completada sobre los 3 criterios de aceptación de SS-01.
Resultado: 2 criterios pasan de forma verificable y 1 queda pendiente.
Conclusión operativa: la unidad `sala-sdk` está casi cerrada, pero no recomendaría cierre automático de SS-01 sin decisión explícita de Aleph sobre la plantilla rica del dossier.

## Verificación de criterios

### 1. Archivo histórico publicado en `main` — PASA

Evidencia:

- `git ls-tree -r --name-only main -- sala/archivo | grep sprint-extraccion-sala-v2` devuelve múltiples entradas bajo `sala/archivo/sprint-extraccion-sala-v2/`.
- En working tree existe `sala/archivo/sprint-extraccion-sala-v2/` y contiene al menos `CIERRE.md`, `tablero.md` y dossiers archivados.

Lectura: el antecedente histórico de extracción de `sala` ya está publicado en `main`.

### 2. Scaffold rico absorbido en `main` — NO PASA AÚN

Estado observado:

- El path citado por el brief y por `dossier-feature-sdk` (`.github/templates/sala-dossier.template.md`) ya no existe como fichero.
- En su lugar existe la carpeta `.github/templates/sala-dossier/` con `PLAN.md`, `BACKLOG.md`, `RESPUESTAS.md`, `activacion.prompt.md` y `tasks/`.
- Ese scaffold publicado sigue siendo esquelético:
  - `PLAN.md` no incluye `Contexto compartido`.
  - `BACKLOG.md` no incluye `Contexto compartido` ni `Regla DRY del backlog`.
  - La task base no modela `Lee primero`, `Salida mínima esperada` ni el brief rico completo como contrato de plantilla general.
- El contrato rico sí está absorbido en `main`, pero vive hoy sobre todo en:
  - `.github/skills/dossier-feature/SKILL.md`
  - `.github/prompts/dossier.prompt.md`

Lectura: el conocimiento ya salió del mod y está en `main`, pero no quedó absorbido plenamente en la plantilla publicada del dossier. La carga sigue repartida entre prompt + skill, mientras la plantilla real sigue mínima.

### 3. `dossier-feature-sdk` ya no queda huérfano — PASA

Evidencia:

- `sala/dossiers/sala-sdk/PLAN.md` define explícitamente `dossier-feature-sdk` como dossier hijo que cierra la capa persistente de `sala`.
- `sala/dossiers/sala-sdk/RESPUESTAS.md` dice que `sala-sdk` subsume conceptualmente a `dossier-feature-sdk` y lo deja como backlog hijo.
- `sala/dossiers/sala-sdk/PLAN.md` fija el cierre esperado: `/dossier`, el skill, el scaffold y el archivo histórico como unidad visible de `sala-sdk`.

Lectura: conceptualmente y documentalmente, `dossier-feature-sdk` ya está integrado como cierre hijo de `sala-sdk`.

## Veredicto

SS-01 no está bloqueada por el archivo histórico ni por la relación entre dossiers. El único punto abierto es la absorción del scaffold rico en la plantilla publicada del SDK.

Si Aleph considera suficiente que el contrato rico viva en `.github/skills/dossier-feature/SKILL.md` + `.github/prompts/dossier.prompt.md`, puede cerrar SS-01 con nota de excepción por cambio de forma (`.github/templates/sala-dossier/` en lugar de `.github/templates/sala-dossier.template.md`).

Si Aleph quiere cierre estricto contra el criterio literal, entonces SS-01 debería devolverse o abrir fix mínimo para alinear `.github/templates/sala-dossier/` con el scaffold rico.

## Artefactos producidos

- `sala/agente-gepe/ENTREGA_SS-01.md`

## Pasos para Aleph

1. Revisar este veredicto.
2. Decidir si el criterio 2 se acepta como satisfecho por absorción en skill + prompt, o si exige alineación explícita de `.github/templates/sala-dossier/`.
3. Cerrar SS-01 o devolverla con fix acotado según esa decisión.