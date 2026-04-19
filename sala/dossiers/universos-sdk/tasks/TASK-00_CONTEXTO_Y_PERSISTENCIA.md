# TASK-00 — Contexto y persistencia del dossier universos-sdk

> **Estado:** cerrada
> **Agente:** GPT-5.4
> **Fecha:** 19-abr-2026

## Contexto congelado

- `futures-engine` ya define el **protocolo de universo propio** en el SDK.
- `@Dramaturgo` SDK conversa sobre grafos y universos, pero no tiene una convención fija de persistencia dentro de `{{LORE_DIR}}`.
- `@Demiurgo` existe hoy solo en el mod/legislativa y consume:
  - `DRAFTS2/LORE_F-02_UNIVERSO.md`
  - `DRAFTS2/universo/`
  - `DRAFTS2/LORE_F-02_ARTEFACTO.md`
- Existen 3 universos persistidos del caso Feo: `universo-1.md`, `universo-1-r1.md`, `universo-1-r2.md`.
- El dossier archivado `future-machine-universo-1` demuestra que la capa universo ya existe de facto, pero no ha sido abstraída al SDK.
- La fase de obras derivadas por modelo se separa en la pareja `cortos-sdk` / `cortos-legislativa`.

## Decisión de corte

- `universos-sdk` cristaliza el contrato portable.
- `universos-legislativa` migra y adapta los universos concretos del caso.
- `grafo-legislativa` deja de absorber ramas instanciadas y cortos.
- `universos-sdk` no absorbe la persistencia de cortos.