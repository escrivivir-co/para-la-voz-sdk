# Activación del orquestador — sprint-v4

> **Sprint:** sprint-v4
> **Fecha de inicio:** 2026-04-19
> **Orquestador:** Aleph (Claude Opus 4.6)

## Contexto mínimo

Sprint de refactorización del Cristalizador como agente core del SDK. El dossier `cristalizador-sdk` fue diseñado en sprint-v3 (CR-00 cerrada por GPT-5.4) y contiene 4 tasks de ejecución.

## Dossier activo

- `sala/dossiers/cristalizador-sdk/` — único dossier del sprint

## Estructura del sprint

```
Track CORE: CR-01 → CR-02 ─┐
                 → CR-03 ─┼→ CR-04
```

- **CR-01** (libre): Refactorizar agente core — desbloquea todo
- **CR-02** (libre, dep CR-01): Refactorizar `/design` y ciclo — paralelizable con CR-03
- **CR-03** (libre, dep CR-01): Gobernanza `COPILOT/` y alerta — paralelizable con CR-02
- **CR-04** (libre, dep CR-02+CR-03): Documentar contrato SDK — cierre

## Protocolo

- Transversal: `.github/instructions/sala-protocolo.instructions.md`
- §6 autovalidación: no git, no escribir fuera de carpeta, no tablero/estados ajenos
- Revisión: Aleph revisa entregas; puede delegar como `REV-*`

## Estado

- Tablero: `sala/tablero.md`
- Agentes registrados: ninguno (sala recién inicializada)
- Primera task libre sin deps: CR-01

## Para levantar la sala

1. Los agentes entran con `/sala-entrar`
2. Proponen CR-01 (única task libre sin deps bloqueantes)
3. Aleph aprueba y asigna
