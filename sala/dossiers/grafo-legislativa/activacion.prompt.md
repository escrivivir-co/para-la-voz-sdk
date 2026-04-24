Migración del grafo Zoowoman de DRAFTS2/ a lore/derivados/grafo/.

Qué es\
Dossier mod que mueve los 5 ficheros JSON del grafo + gramática + artefacto + universo markdown legacy desde `DRAFTS2/` a `lore/derivados/`. Actualiza refs de los consumidores del **grafo**. Los universos instanciados van en `universos-legislativa` y los cortos en `cortos-legislativa`.

Qué problema resuelve\
El grafo vive en `DRAFTS2/grafo/` — un directorio de trabajo temporal. Con lore-db ya decidido, el grafo debe vivir en `lore/derivados/grafo/` como derivado canónico del corpus.

Backlog real, en una línea\
GL-00 cerrada · GL-01 migrar grafo JSON (libre, dep LP-01b† + CP-01‡ + GS-01§) · GL-02 migrar artefacto + universo markdown legacy (libre, dep LP-01b† + CP-01‡) · GL-03 actualizar refs de consumidores del grafo (libre, dep GL-01+02) · GL-04 validar integridad (libre, dep GL-03)

Siguiente paso recomendado\
Esperar a LP-01b (piezas + hilo base) y CP-01 (corpus canónico) junto con GS-01 para GL-01. Una vez listo eso, GL-02 y GL-01 pueden ejecutarse; después GL-03 y GL-04.
