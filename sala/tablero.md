# Tablero de tareas — LoreSDK

> **Sprint:** sprint-v4
> **Última actualización:** 19-abr-2026 — orquestador (Claude Opus 4.6) — cierre: CR-02, CR-03
> **Agentes activos:** 0 en curso, 3 disponibles (gepe, gemy, sony)
> **Estados:** `libre` · `propuesta:{alias}` · `en-curso:{alias}` · `entregada:{alias}` · `cerrada` · `no-aplica`
>
> **Orquestador:** si acabas de llegar a una ventana nueva, usa `/sala-aleph` o lee `sala/activacion-orquestador.md` para levantarte con todo el contexto.

### Glosario de estados

| Estado | Significado |
|--------|-------------|
| `libre` | Disponible. Cualquier agente puede proponerla si las dependencias están resueltas. |
| `propuesta:{alias}` | Un agente la propuso en su `estado.md`. Esperando que Aleph apruebe o redirija. |
| `en-curso:{alias}` | Aleph aprobó. El agente está trabajando. Tiene carpeta temporal en `sala/agente-{alias}/`. |
| `entregada:{alias}` | El agente terminó. Hay entrega en su carpeta. El orquestador debe revisar. |
| `entregada-en-revisión:{alias}` | Entrega recibida por Aleph. Revisión delegada como `REV-*`. Esperando veredicto. |
| `cerrada` | Revisada y aceptada por el orquestador. Copiada al dossier si aplica. |
| `no-aplica` | No se ejecuta. |

> **Tareas `REV-*`:** las tareas con prefijo `REV-` son **solo-orquestador**. Agentes regulares las saltan al leer el tablero. Solo agentes designados como revisores por el PO pueden proponerlas.

---

## Tracks recomendados

```
Track CORE: CR-01 → CR-02 (paralelo con CR-03) → CR-04
  CR-01 desbloquea CR-02 y CR-03
  CR-02 + CR-03 son paralelizables
  CR-04 cierra cuando CR-02 y CR-03 estén cerradas
```

---

## Track CORE — Contrato SDK del Cristalizador (4 tareas)

| Task | Título | Deps | Estado |
|------|--------|------|--------|
| CR-01 | Refactorizar el agente core | CR-00 | `cerrada` |
| CR-02 | Refactorizar `/design` y el ciclo | CR-01 | `cerrada` |
| CR-03 | Gobernanza de `COPILOT/` y alerta | CR-01 | `cerrada` |
| CR-04 | Documentar el contrato SDK | CR-02, CR-03 | `libre` |

> Dossier: `sala/dossiers/cristalizador-sdk/`

---

## Revisiones pendientes

| Task | Título | Deps | Estado |
|------|--------|------|--------|
<!-- REV-* tasks: solo-orquestador. Agentes regulares no proponen estas. -->

---

## Backlog post-sprint

| ID | Título | Prioridad | Notas |
|----|--------|-----------|-------|
| — | — | — | Sin items pendientes de sprint anterior |

---

## Tareas cerradas (referencia)

| Task | Dossier | Estado |
|------|---------|--------|
| CR-00 | cristalizador-sdk | `cerrada` — GPT-5.4 |
| CR-01 | cristalizador-sdk | `cerrada` — Gepe (GPT-5.4) — rev: Aleph (Claude Opus 4.6) |
| CR-02 | cristalizador-sdk | `cerrada` — Gepe (GPT-5.4) — rev: Aleph (Claude Opus 4.6) |
| CR-03 | cristalizador-sdk | `cerrada` — Gemy (Gemini 3.1 Pro) — rev: Aleph (Claude Opus 4.6) |

---

> **⚠️ Aleph:** actualiza esta tabla cada vez que cierres una task. Si no, se desincroniza.

| Track | Total | Cerradas | Libres | En curso | Primeras libres (sin deps) |
|-------|-------|----------|--------|----------|----------------------------|
| CORE | 4 | **3** | **1** | **0** | CR-04 (deps: CR-02✓, CR-03✓) |
| **Total** | **4** | **3** | **1** | **0** | CR-04 |
