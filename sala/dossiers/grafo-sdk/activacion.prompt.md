Extraer el concepto genérico de grafo de bifurcación al SDK main.

Qué es\
El grafo de bifurcación (nodos, arcos, huecos) existe hoy solo en mod/legislativa con una gramática JSON concreta. El skill `futures-engine` y el `@Dramaturgo` ya son genéricos en el SDK. Este dossier extrae el protocolo del grafo al SDK para que cualquier mod pueda definir su propia gramática de bifurcación.

Qué problema resuelve\
Si se crea otro mod, tendría que reinventar la estructura del grafo desde cero. Con el SDK proveyendo schema genérico + template de gramática, cada mod solo define sus tipos de nodo concretos y sus reglas de validación.

Backlog real, en una línea\
GS-00 cerrada · GS-01 schema genérico (libre) · GS-02 template gramática (libre) · GS-03 ampliar dramaturgo (libre) · GS-04 documentar SDK (libre)

Siguiente paso recomendado\
GS-01 y GS-02 en paralelo — crear el schema genérico de grafo y la plantilla de gramática.
