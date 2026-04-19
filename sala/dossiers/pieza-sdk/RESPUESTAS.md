# Respuestas del usuario — pieza-sdk

> **Fecha:** 19-abr-2026
> **Registradas por:** Claude Opus 4.6

## Punto 1 — Separación SDK / mod

- **Contexto:** El usuario quiere abstraer al main la gestión de la base de datos de piezas (hoy en mod/legislativa).
- **Respuesta del usuario:** "Abstraer al main la gestión de la base de datos de piezas. Y luego que mod/legislativa extienda."
- **Efecto operativo:** Dos dossiers: uno para la abstracción al SDK, otro para la extensión del mod.

## Punto 2 — LORE_INDEX como pieza SDK → lore-db

- **Contexto:** `LORE_INDEX.md` hoy es lore-specific pero el concepto de inventario es genérico.
- **Respuesta del usuario (19-abr-2026):** "La db se inicializa desde scaffold de main (como sala-aleph inicializa la sala)."
- **Efecto operativo:**
  - `lore/` es la carpeta canónica — el SDK provee scaffold en main (PS-05)
  - INDEX migra a `lore/INDEX.md` (lo hace LP-01b del otro dossier)
  - El SDK provee template `lore-index.template.md` en `.github/templates/`
  - `/sala-aleph` Paso 0b inicializa la db si no existe INDEX.md
