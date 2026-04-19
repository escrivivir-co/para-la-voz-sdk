Continuación directa de `extraccion-sala-sdk`: la superficie operativa de `sala` ya está exportada al SDK, pero falta exportar su capa de diseño persistente (`/dossier` + `cristalizacion-feature/SKILL.md`).

`dossier` no es un feature lateral. Es la subcomponente de `sala` que abre, mantiene y reactiva tracks en `{{SALA_DIR}}/dossiers/`; después `/sala-*` ejecuta esos tracks. Por eso este dossier se reencuadra como cierre de la extracción de `sala`, no como promoción aislada de dos ficheros.

Hecho: dossier reencuadrado contra el archivo de `extraccion-sala-sdk`, `sala/README.md` y la plantilla viva.
Pendiente: DF-01 (prompt `/dossier` al formato actual), DF-02 (SKILL al formato actual), DF-03 (superficie y triggers de `sala` + publicación del archivo SDK en `main` + migración de consumidores + cleanup controlado).

Decisión de producto: el formato canónico del dossier es `PLAN.md`, `BACKLOG.md`, `RESPUESTAS.md`; el cierre no puede borrar duplicados en `mod/` hasta migrar o puentear consumidores vivos del formato antiguo.

Lectura ejecutiva: [BACKLOG.md](./BACKLOG.md) → [PLAN.md](./PLAN.md) → [RESPUESTAS.md](./RESPUESTAS.md) → tasks/
