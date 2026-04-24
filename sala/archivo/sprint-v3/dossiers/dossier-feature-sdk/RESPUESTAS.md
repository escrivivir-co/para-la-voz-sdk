# Respuestas del usuario — dossier-feature-sdk

> **Fecha:** 19-abr-2026
> **Registradas por:** `GPT-5.4`

## Punto 1 — `dossier` va dentro de `sala`

- **Respuesta del usuario:** Recuperar del archivo de `mod/legislativa` el dossier o dossiers de `sala` para exportarlos bien a `main` y parsearlos al formato nuevo; tratar `dossier` como subcomponente de `sala`, "así sacamos bien sala y dossier, juntos con los mecanismos triggers bien".
- **Efecto operativo:** `dossier-feature-sdk` se reencuadra como continuación de `extraccion-sala-sdk`. El objetivo ya no es promover dos ficheros sueltos, sino cerrar la capa de diseño persistente de `sala` (`/dossier` + SKILL) y alinear la superficie de activación y los consumidores que la usan.

## Punto 2 — El archivo de `sala` es ancla de diseño

- **Respuesta del usuario:** Recuperar el o los dossiers archivados de `sala` antes de seguir estandarizando el formato nuevo.
- **Efecto operativo:** El archivo `sala/archivo/sprint-extraccion-sala-v2/` pasa a ser ancla obligatoria de este dossier. El cleanup en `mod/` deja de ser borrado automático y pasa a ser migración controlada a partir de ese antecedente.

## Punto 3 — El archivo SDK debe quedar también en `main`

- **Respuesta del usuario:** Tiene sentido mover ese antecedente desde la rama del mod a `main` para que quede allí archivado.
- **Efecto operativo:** El cierre de `dossier-feature-sdk` incorpora la publicación de `sala/archivo/sprint-extraccion-sala-v2/` en `main`. No se abre un dossier nuevo solo para eso: queda subsumido en DF-03.

## Punto 4 — `main` debe absorber el máximo de `sala` y `dossier`

- **Respuesta del usuario:** `main` debe absorber el máximo de `sala` y `dossier`; el scaffold rico es para todas las ramas que lo puedan traer.
- **Efecto operativo:** este dossier deja de limitarse a prompt + SKILL. DF-03 debe alinear también el template/contrato del dossier para que el scaffold rico quede en `main` y las ramas hereden base, no una versión empobrecida.
