# TASK-02 — Template y manifest de la future-machine

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** FS-01, PS-05 (lore-db-sdk), CS-04 (corpus-sdk), GS-04 (grafo-sdk), US-03 (universos-sdk), COS-04 (cortos-sdk)
> **Entrega esperada:** `.github/templates/future-machine.template.md`

> Cada dossier SDK de capa debe estar cerrado para que el manifest referencie schemas y rutas reales.

## Objetivo

Crear la template instanciable como `{{LORE_DIR}}/FUTURE_MACHINE.md`.

## Debe incluir

1. Tabla de slots y propietarios.
2. Rutas canónicas por capa.
3. Entrypoints de usuario y de refresh.
4. Estado operativo por slot.

## Criterio de aceptación

- Un mod puede instanciar la machine sin reinventar la estructura del cierre de ciclo.