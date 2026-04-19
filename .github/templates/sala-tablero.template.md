# Tablero de tareas — {{NOMBRE_LORE}}

> **Sprint:** {{NOMBRE_SPRINT}}
> **Última actualización:** {{FECHA}} — orquestador ({{MODELO_ORQUESTADOR}})
> **Agentes activos:** {{N_AGENTES}} slots disponibles (se identifican por alias, no por modelo)
> **Estados:** `libre` · `propuesta:{alias}` · `en-curso:{alias}` · `entregada:{alias}` · `cerrada` · `no-aplica`
>
> **Orquestador:** si acabas de llegar a una ventana nueva, usa `/sala-aleph` o lee `DRAFTS2/sala/activacion-orquestador.md` para levantarte con todo el contexto.

### Glosario de estados

| Estado | Significado |
|--------|-------------|
| `libre` | Disponible. Cualquier agente puede proponerla si las dependencias están resueltas. |
| `propuesta:{alias}` | Un agente la propuso en su `estado.md`. Esperando que Aleph apruebe o redirija. |
| `en-curso:{alias}` | Aleph aprobó. El agente está trabajando. Tiene carpeta temporal en `sala/agente-{alias}/`. |
| `entregada:{alias}` | El agente terminó. Hay entrega en su carpeta. El orquestador debe revisar. |
| `cerrada` | Revisada y aceptada por el orquestador. Copiada al dossier si aplica. |
| `no-aplica` | No se ejecuta. |

---

## Tracks recomendados

```
{{TRACKS_RECOMENDADOS}}
```

---

## Track {{TRACK_1_ID}} — {{TRACK_1_NOMBRE}} ({{TRACK_1_N}} tareas)

| Task | Título | Deps | Estado |
|------|--------|------|--------|
| {{TRACK_1_ID}}-01 | {{TITULO}} | — | `libre` |

> Dossier: `DRAFTS2/{{DOSSIER_1}}/`

<!-- Añade más tracks copiando el bloque anterior -->

---

## Backlog post-sprint

| ID | Título | Prioridad | Notas |
|----|--------|-----------|-------|
| BL-01 | {{TITULO_BACKLOG}} | media | {{NOTAS}} |

---

## Tareas cerradas (referencia)

| Task | Dossier | Estado |
|------|---------|--------|

---

> **⚠️ Aleph:** actualiza esta tabla cada vez que cierres una task. Si no, se desincroniza.

| Track | Total | Cerradas | Libres | En curso | Primeras libres (sin deps) |
|-------|-------|----------|--------|----------|----------------------------|
| {{TRACK_1_ID}} | {{N}} | 0 | **{{N}}** | 0 | {{TASK_ID_SIN_DEPS}} |
| **Total** | **{{N_TOTAL}}** | **0** | **{{N_TOTAL}}** | **0** | — |
