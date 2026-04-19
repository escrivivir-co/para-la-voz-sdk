# TASK-00 — Contexto y persistencia

> **Estado:** cerrada
> **Agente recomendado:** GPT-5.4
> **Dependencias:** —
> **Entrega esperada:** dossier `cristalizador-sdk` creado y contexto congelado

## Hallazgos fijados

1. El Cristalizador original del SDK vive en `.github/agents/cristalizador.agent.md` y se invoca por `/design`.
2. El ciclo documental ya lo sitúa como paso final opcional en `.github/templates/guion-ciclo.template.md`.
3. El contrato actual protege `mod/` como territorio de escritura, pero no formaliza con suficiente claridad la herencia `main -> mod` ni el comportamiento branch-aware.
4. `COPILOT/` ya es fuente oficial de capacidades para el agente, pero hoy solo tiene una convención de "sync mensual" y no una señal auditable de frescura.
5. El archivo de `future-machine-universo-1` ya pidió exactamente el comportamiento que ahora se quiere promover: leer `COPILOT/`, maximizar el uso en `mod/` y abrir warning a `main` solo con evidencia.
6. Los hooks de Copilot pueden servir para alertas, pero están en preview y pueden estar deshabilitados; la solución final necesita fallback sin hooks.

## Decisión de alcance

Este dossier se deja preparado para `main`, fuera del sprint activo de `lore-db/grafo`. Su trabajo es recapitular y modernizar el contrato del agente, no abrir todavía la implementación.