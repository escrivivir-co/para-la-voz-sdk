# TASK-02 — Template y manifest de la future-machine

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** FS-01, PS-05 (lore-db-sdk), CS-04 (corpus-sdk), GS-04 (grafo-sdk), US-03 (universos-sdk), COS-04 (cortos-sdk)
> **Entrega esperada:** `.github/templates/future-machine.template.md`

> Cada dossier SDK de capa debe estar cerrado para que el manifest referencie schemas y rutas reales.

## Lee primero

1. `.github/instructions/future-machine-schema.instructions.md` (FS-01)
2. Sección 0 del PLAN — tabla del pipeline completo (para instanciar el ejemplo)

## Objetivo

Crear la template instanciable como `{{LORE_DIR}}/FUTURE_MACHINE.md`. El manifest es el fichero que `@Pipeline` y `@Portal` leen para saber qué hay.

## Debe incluir

1. Tabla de slots con columnas: slot, agente propietario, ruta canónica, estado
2. Grafo de dependencias upstream/downstream
3. Entrypoints de usuario (start, status, refresh) con refs a los prompts
4. Metadatos: fecha de creación, última actualización, mod que lo instancia

## Criterio de aceptación

- Un mod puede instanciar la machine sin reinventar la estructura del cierre de ciclo
- El manifest funciona como single source of truth para Pipeline y Portal