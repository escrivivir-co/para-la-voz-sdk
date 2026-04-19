Migración del grafo Zoowoman de DRAFTS2/ a lore/derivados/grafo/.

Qué es\
Dossier mod que mueve los 5 ficheros JSON del grafo + gramática + artefacto + universo markdown + 5 cortos + 3 ramas instanciadas desde `DRAFTS2/` a `lore/derivados/`. Actualiza refs en los 4 agentes consumidores.

Qué problema resuelve\
El grafo vive en `DRAFTS2/grafo/` — un directorio de trabajo temporal. Con lore-db ya decidido, el grafo debe vivir en `lore/derivados/grafo/` como derivado canónico del corpus.

Backlog real, en una línea\
GL-00 cerrada · GL-01 migrar grafo JSON (libre, dep LP-01†) · GL-02 migrar derivados universo (libre, dep LP-01†) · GL-03 actualizar refs agentes (libre, dep GL-01+02) · GL-04 validar integridad (libre, dep GL-03)

Siguiente paso recomendado\
Esperar a LP-01 (estructura `lore/derivados/` creada). Una vez disponible, GL-01 y GL-02 pueden ejecutarse en paralelo.
