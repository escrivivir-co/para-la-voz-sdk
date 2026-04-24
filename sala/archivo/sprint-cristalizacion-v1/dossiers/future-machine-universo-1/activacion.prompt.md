Qué es\
Una preparación del feature "future-machine" para el mod legislativa, aterrizada sobre el caso real de universo-1. Convertido en backlog, tasks delegables y rutas temporales para que los agentes puedan trabajar sin romper el SDK base.

Qué problema resuelve\
Ahora mismo el lore vive de facto en DRAFTS2, pero parte del SDK espera rutas canónicas como corpus/ o mod/skills/. Esta carga ordena eso con un workaround limpio y prepara la cristalización para que el mod tenga su propia machine de futuros sin tocar el core.

Qué se ha hecho ya

-   Se abrió una carpeta de feature persistente en [future-machine-universo-1].
-   Se dejó un backlog maestro DRY en [BACKLOG_FUTURE_MACHINE_UNIVERSO1.md].
-   Se fijó el plan base en [PLAN_FUTURE_MACHINE_UNIVERSO1.md].
-   Se registraron las decisiones del usuario en [RESPUESTAS_USUARIO_FUTURE_MACHINE_UNIVERSO1.md].
-   Se descompuso el trabajo en tasks para agentes dentro de [tasks].
-   Se inicializaron rutas oficiales faltantes con redirección temporal:\
    [corpus.md],\
    [README.md],\
    [README.md].

Qué NO se ha hecho aún

-   FM-05 (validación de la cadena completa) está pendiente.
-   FM-06 (warning main) está condicional.

> **[Claude Opus 4.6] Nota 19-abr-2026:** FM-02, FM-03 y FM-04 han sido absorbidos por los dossiers hermanos. Ver adenda en el PLAN.

Backlog real, en una línea

-   FM-00 y FM-01: cerradas. ✔️
-   FM-02: **Superseded** — absorbido por 4 dossiers de cristalización (pipeline-operativo, cadena-agentica, grafo-json, finalizacion-lore-plan).
-   FM-03: **Superseded** — `cristalizacion-feature/SKILL.md` + cadena-agentica cubren el scope.
-   FM-04: **Superseded** — cadena-agentica + pipeline-operativo cubren la superficie agéntica.
-   FM-05: **Reescrito** — validación contra la cadena de 5 agentes, no solo Dramaturgo.
-   FM-06: condicional — warning para main solo si aparece fallo real.

Decisión de producto que se está protegiendo\
El trabajo mantiene una línea clara:

-   no duplicar el SDK;
-   no tocar .github;
-   construir solo en mod/;
-   usar universo-1 como prueba de realidad;
-   aceptar que DRAFTS2 sigue siendo la fuente viva mientras exista el workaround.

Mi lectura ejecutiva\
El dossier está en fase de cierre. FM-00/01 completados, FM-02..04 absorbidos por dossiers hermanos. Lo que queda vivo: FM-05 (validación end-to-end de la cadena de 5 agentes sobre universo-1) y FM-06 (condicional).

Siguiente paso recomendado: ejecutar FM-05 cuando los dossiers hermanos tengan al menos su primera task implementada. La cadena no necesita estar completa para una primera validación parcial.

Insight clave de esta sesión: "salvar el lore de DRAFTS2" y "migrar el grafo a JSON" son la misma operación simétrica — promover borrador a formato estructurado.