# Respuestas del usuario — sala-sdk

> **Fecha:** 19-abr-2026
> **Registradas por:** `GPT-5.4`

## Punto 1 — Abrir `sala-sdk` como unidad visible

- **Respuesta del usuario:** Abrir el dossier de `sala` como unidad, igual que los otros, pensando también en la documentación y en poder listar los dossiers y verlo ahí.
- **Efecto operativo:** Se crea `sala/dossiers/sala-sdk/` como dossier paraguas. No sustituye a `dossier-feature-sdk`; lo subsume conceptualmente y lo deja como backlog hijo.

## Punto 2 — Solo estamos preparando backlog

- **Respuesta del usuario:** Al final aquí estamos preparando backlog, no reejecutando toda la implementación.
- **Efecto operativo:** El backlog de `sala-sdk` queda casi cerrado: una task de contexto ya cerrada y una task final de cierre dependiente de DF-03. No se duplican tasks implementativas ya abiertas en DF.

## Punto 3 — El archivo histórico debe vivir en `main`

- **Respuesta del usuario:** El antecedente archivado de `sala` debe poder moverse a `main` para quedar allí archivado.
- **Efecto operativo:** La task final de `sala-sdk` exige publicar `sala/archivo/sprint-extraccion-sala-v2/` en `main` como historia del SDK.

## Punto 4 — `main` debe absorber el máximo de `sala` y `dossier`

- **Respuesta del usuario:** `main` debe absorber el máximo de `sala` y `dossier`; el scaffold rico es para todas las ramas que lo puedan traer.
- **Efecto operativo:** `sala-sdk` deja explícito que el cierre no se limita a publicar prompts e histórico. También exige que el scaffold rico de `dossier` quede absorbido por `main` como base heredable.