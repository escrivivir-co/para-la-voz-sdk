Dossier preparado fuera del sprint activo. No está en el tablero actual.

Contrato SDK del Cristalizador como agente core por defecto.

Qué es
Recapitula y moderniza la arquitectura de uso del Cristalizador: default en `main`, override opcional en `mod/`, lectura de `COPILOT/` como observatorio vivo de capacidades y disciplina branch-aware para no escribir en `.github/` desde ramas `mod/*`.

Qué problema resuelve
El agente actual ya contiene la intuición buena, pero no formaliza la herencia `main -> mod`, no pacta con el usuario cuando maximizar implica preview/admin/premium, y no tiene una capa auditable para detectar que `COPILOT/` está desactualizado.

Backlog real, en una línea
CR-00 cerrada · CR-01 refactor agente core (libre) · CR-02 refactor `/design` y ciclo (libre) · CR-03 gobernanza `COPILOT/` y alerta (libre) · CR-04 documentar contrato SDK (libre)

Punto abierto reconocido
La alerta de obsolescencia puede vivir en hook, en chequeo manual del agente o en ambos. Como hooks están en preview y pueden estar deshabilitados, el dossier exige fallback sin dependencia dura de hooks.

Siguiente paso recomendado
Empezar por CR-01. Sin ese refactor del agente core, el resto de piezas solo maquillan el problema.