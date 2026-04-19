# Tablero de tareas — LoreSDK

> **Sprint:** sprint-v3
> **Última actualización:** 19-abr-2026 — orquestador (Claude Opus 4.6) — aprobación DF-01→Gepe, DF-02→Sony
> **Agentes activos:** 2 en curso, 1 standby (se identifican por alias, no por modelo)
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
Track GEN: Generalización de capa dossier (DF-01, DF-02) — parallelizable, sin deps
Track INT: Integración SDK y cierre (DF-03, SS-01) — secuencial, deps en cascada
```

---

## Track GEN — Generalización de capa dossier (2 tareas)

| Task | Título | Deps | Estado |
|------|--------|------|--------|
| DF-01 | Promover `dossier.prompt.md` a `.github/prompts/` | — | `en-curso:gepe` |
| DF-02 | Promover `cristalizacion-feature/SKILL.md` a `.github/skills/` | — | `en-curso:sony` |

> Dossier: `sala/dossiers/dossier-feature-sdk/`

---

## Track INT — Integración SDK y cierre (2 tareas)

| Task | Título | Deps | Estado |
|------|--------|------|--------|
| DF-03 | Integrar superficie `sala`, scaffold rico en `main`, migrar consumidores | DF-01, DF-02 | `libre` |
| SS-01 | Cerrar unidad `sala-sdk` y publicar archivo histórico | DF-03 | `libre` |

> Dossiers: `sala/dossiers/dossier-feature-sdk/` (DF-03), `sala/dossiers/sala-sdk/` (SS-01)

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
| DF-00 | dossier-feature-sdk | `cerrada` — Claude Opus 4.6 |
| SS-00 | sala-sdk | `cerrada` — GPT-5.4 |

---

> **⚠️ Aleph:** actualiza esta tabla cada vez que cierres una task. Si no, se desincroniza.

| Track | Total | Cerradas | Libres | En curso | Primeras libres (sin deps) |
|-------|-------|----------|--------|----------|----------------------------|
| GEN | 2 | 0 | **0** | 2 | — |
| INT | 2 | 0 | **2** | 0 | DF-03 (bloqueada por DF-01+DF-02), SS-01 (bloqueada por DF-03) |
| **Total** | **4** | **0** | **2** | **2** | — |
