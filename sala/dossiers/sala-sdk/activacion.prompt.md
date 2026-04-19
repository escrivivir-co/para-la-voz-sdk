`sala-sdk` es el dossier paraguas de la unidad `sala` en el SDK.

Qué es
Agrupa la superficie ya exportada de `sala` (`/sala-*`, instructions, templates), el cierre pendiente de la capa `dossier`, el scaffold rico que `main` debe absorber y el archivo histórico de la extracción SDK.

Qué problema resuelve
Evita que `sala` quede fragmentada entre archivo + `dossier-feature-sdk` + documentación. Al listar dossiers existe una unidad visible y documentable equivalente al resto de capas SDK, y queda fijado que `main` hereda el scaffold rico en vez de dejarlo en el mod como saber tácito.

Backlog real, en una línea
SS-00 cerrada; SS-01 pendiente tras DF-03 para absorber el scaffold rico, publicar el archivo en `main` y cerrar la unidad.

Siguiente paso recomendado
Ejecutar DF-01, DF-02 y DF-03 en `dossier-feature-sdk`; cuando DF-03 cierre, cerrar SS-01.