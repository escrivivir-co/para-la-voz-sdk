Extraer la gestión genérica de piezas tipadas al SDK main, incluyendo scaffold `lore/` e inicialización automática.

Qué es\
El SDK hoy no sabe qué es una "pieza". El concepto de inventario tipado, schema de tipos, routing y validación existe solo en mod/legislativa. Este dossier extrae el protocolo genérico al SDK y crea `lore/` como base de datos canónica de piezas — con scaffold e init automático como se hizo con `sala/`.

Qué problema resuelve\
Si se crea mod/restitutiva u otro mod, tendrían que reinventar el inventario de piezas desde cero. Con el SDK proveyendo el protocolo genérico + scaffold `lore/` + templates + init en sala-aleph, cada mod solo define sus tipos concretos y mergea main.

Backlog real, en una línea\
PS-00 cerrada · PS-01 schema genérico (libre) · PS-02 template index (libre) · PS-03 ampliar archivero (libre) · PS-04 documentar SDK (libre) · PS-05 scaffold lore-db + init (libre, dep PS-01+PS-02)

Siguiente paso recomendado\
PS-01 y PS-02 en paralelo — crear el schema genérico y la plantilla de inventario. Luego PS-05 para el scaffold.
