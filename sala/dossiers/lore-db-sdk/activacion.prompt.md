Extraer la gestión genérica de piezas tipadas al SDK main: schema + Loreador + scaffold `lore/` + init automático.

Qué es\
El SDK hoy no sabe qué es una "pieza". Este dossier extrae el protocolo genérico al SDK: schema de tipos, template de inventario, el agente `@Loreador` (gestor de la lore-db), scaffold `lore/` con init automático. El Loreador reemplaza la propuesta anterior de ampliar @Archivero fuera de su dominio. La capa corpus se cristaliza aparte en `corpus-sdk` / `corpus-legislativa`.

Qué problema resuelve\
Si se crea mod/restitutiva u otro mod, tendrían que reinventar el inventario de piezas desde cero. Con el SDK proveyendo Loreador + protocolo genérico + scaffold `lore/` + templates + init en sala-aleph, cada mod solo define sus tipos concretos, extiende al Loreador, y mergea main.

Backlog real, en una línea\
PS-00 cerrada · PS-01 schema genérico (libre) · PS-02 template index (libre) · PS-03 crear Loreador SDK (libre) · PS-04 documentar SDK (libre) · PS-05 scaffold lore-db + init (libre, dep PS-01+PS-02)

Siguiente paso recomendado\
PS-01 y PS-02 en paralelo — crear el schema genérico y la plantilla de inventario. Luego PS-03 (Loreador) y PS-05 (scaffold).
