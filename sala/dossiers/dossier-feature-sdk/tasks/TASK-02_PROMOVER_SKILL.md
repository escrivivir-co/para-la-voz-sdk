# TASK-02 — Promover cristalizacion-feature/SKILL.md al SDK

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** —
> **Entrega esperada:** `.github/skills/cristalizacion-feature/SKILL.md` generalizado

## Lee primero

1. `mod/skills/cristalizacion-feature/SKILL.md` — versión actual
2. `.github/copilot-instructions.md` — sección Sala (estructura dossiers)
3. `.github/instructions/sala-protocolo.instructions.md` — protocolo transversal

## Objetivo

Copiar `mod/skills/cristalizacion-feature/SKILL.md` a `.github/skills/cristalizacion-feature/SKILL.md`, generalizando.

## Cambios requeridos

1. **Ubicación canónica:** cambiar `mod/skills/cristalizacion-feature/SKILL.md` → `.github/skills/cristalizacion-feature/SKILL.md`.
2. **Rutas de dossiers:** usar `{{SALA_DIR}}/dossiers/` en vez de rutas hardcoded.
3. **R4 (restricción de escritura):** relajar de "Solo `mod/`" a "Los artefactos propuestos van en `mod/`. Si la task es una promoción al SDK, el candidato va en la carpeta del agente y Aleph lo copia a `.github/`."
4. **Refs al ejemplo:** actualizar ruta del dossier de referencia a `{{SALA_DIR}}/archivo/` o eliminar si es demasiado específico.
5. **Consumidores:** cambiar de `@Cristalizador` a "cualquier agente que gestione features".
6. **No añadir** refs a ningún lore específico.

## Salida mínima esperada

1. Fichero candidato en carpeta del agente: `agente-{alias}/candidato-SKILL.md`
2. ENTREGA con lista de cambios respecto al original.

## Criterio de aceptación

- El SKILL funciona sin presuponer ningún mod.
- Grep de `DRAFTS2|legislativa|mod/skills` = 0 hits.
- R4 permite promociones al SDK explícitamente.
