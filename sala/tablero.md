# Tablero de tareas — Lore DB Vector Expansion (DocumentMachineSDK)

> **Sprint:** sprint-scrum-backlog-lore-db-vector-expansion-init
> **Última actualización:** 22-abr-2026 — orquestador (GPT-5.4) — inicialización del dossier local y apertura para refinement
> **Agentes activos:** 0 en curso, sin agentes en disco todavía
> **Estados:** `libre` · `propuesta:{alias}` · `en-curso:{alias}` · `entregada:{alias}` · `cerrada` · `no-aplica`
>
> **Orquestador:** si acabas de llegar a una ventana nueva, usa `#sala_aleph activar` o lee `sala/activacion-orquestador.md` para levantarte con todo el contexto.

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

---

## Tracks recomendados

```text
Track REFINE-DM: SBLVX-DM-02 → SBLVX-DM-03 → SBLVX-DM-04
  SBLVX-DM-02 abre el refinement local.
  SBLVX-DM-03 y SBLVX-DM-04 concretan el frente DocumentMachineSDK.
```

---

## Track REFINE-DM — backlog scrum lore db vector expansion (5 tareas)

| Task | Título | Deps | Estado |
|------|--------|------|--------|
| SBLVX-DM-00 | Pre-scrum definitions local | — | `cerrada` |
| SBLVX-DM-01 | Planification local DRY | SBLVX-DM-00 | `cerrada` |
| SBLVX-DM-02 | Aprobar o enmendar plan compartido | SBLVX-DM-01 | `libre` |
| SBLVX-DM-03 | Refinar skill y layout local | SBLVX-DM-02 | `libre` |
| SBLVX-DM-04 | Preparar handoff documental | SBLVX-DM-02, SBLVX-DM-03 | `libre` |

> Dossier: `sala/dossiers/scrum-backlog-lore-db-vector-expansion/`

---

## Revisiones pendientes

| Task | Título | Deps | Estado |
|------|--------|------|--------|
<!-- REV-* tasks: solo-orquestador. -->

---

## Backlog post-sprint

| ID | Título | Prioridad | Notas |
|----|--------|-----------|-------|
| — | — | — | Sesión recién inicializada; sin arrastre previo. |

---

## Tareas cerradas (referencia)

| Task | Dossier | Estado |
|------|---------|--------|
| SBLVX-DM-00 | scrum-backlog-lore-db-vector-expansion | `cerrada` — GPT-5.4 |
| SBLVX-DM-01 | scrum-backlog-lore-db-vector-expansion | `cerrada` — GPT-5.4 |

---

> **⚠️ Aleph:** actualiza esta tabla cada vez que cierres una task. Si no, se desincroniza.

| Track | Total | Cerradas | Libres | En curso | Primeras libres (sin deps) |
|-------|-------|----------|--------|----------|----------------------------|
| REFINE-DM | 5 | **2** | **3** | **0** | SBLVX-DM-02 |
| **Total** | **5** | **2** | **3** | **0** | SBLVX-DM-02 |