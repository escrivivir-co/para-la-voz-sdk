# Plan — cortos-legislativa

> **Fecha:** 19-abr-2026
> **Autor:** GPT-5.4
> **Dossier:** `sala/dossiers/cortos-legislativa/`

## 1. Contexto

Tras separar `grafo` de `universos`, queda una tercera fase explícita: **cortos**. Esta fase no debe quedar mezclada con `universos-legislativa`, porque su input persistido, su agente y su output son distintos:

- input persistido: `LORE_F-02_CORTO*.md`
- agente principal: `@Dramaturgo Cortos`
- operación: generar y versionar obras por modelo

Este dossier es la contraparte mod de `cortos-sdk`.

Relación con otros dossiers:

| Dossier | Branch | Qué hace | Relación |
|---------|--------|----------|----------|
| `universos-legislativa` | mod/legislativa | Migra universos y recablea Demiurgo | Upstream directo |
| `cortos-sdk` | main | Contrato portable de obras derivadas | Provee el shape genérico |
| **cortos-legislativa** | mod/legislativa | **Migra cortos y recablea Dramaturgo/Pipeline final** | Este dossier |
| `future-machine-legislativa` | mod/legislativa | Instancia la machine del caso Feo — `slot_obras` | **Downstream:** CL-01 → FL-01 |

## 2. Inventario de assets a migrar

| Asset | Origen | Destino |
|-------|--------|---------|
| corto original | `DRAFTS2/LORE_F-02_CORTO.md` | `lore/derivados/cortos/LORE_F-02_CORTO.md` |
| corto claude-opus-4 | `DRAFTS2/LORE_F-02_CORTO-universo-1-claude-opus-4.md` | `lore/derivados/cortos/LORE_F-02_CORTO-universo-1-claude-opus-4.md` |
| corto claude-opus-4-2 | `DRAFTS2/LORE_F-02_CORTO-universo-1-claude-opus-4-2.md` | `lore/derivados/cortos/LORE_F-02_CORTO-universo-1-claude-opus-4-2.md` |
| corto gemini | `DRAFTS2/LORE_F-02_CORTO-universo-1-gemini-3.1-pro.md` | `lore/derivados/cortos/LORE_F-02_CORTO-universo-1-gemini-3.1-pro.md` |
| corto gpt-5 | `DRAFTS2/LORE_F-02_CORTO-universo-1-gpt-5-4.md` | `lore/derivados/cortos/LORE_F-02_CORTO-universo-1-gpt-5-4.md` |

## 3. Refs a actualizar

| Fichero | Qué cambiar |
|---------|-------------|
| `mod/agents/dramaturgo.agent.md` | Rutas de lectura/escritura de cortos y convención nueva |
| `mod/agents/pipeline.agent.md` | Handoff final y naming de la fase `cortos` |
| `mod/instructions/lore-estado.instructions.md` | Rutas y conteos de obras derivadas si aplica |
| `mod/instructions/legislativa-universo.instructions.md` | Refs a obras generadas si las incluye |

## 4. Anclas

| Artefacto | Ubicación | Estado |
|-----------|-----------|--------|
| Dramaturgo Cortos (mod) | `mod/agents/dramaturgo.agent.md` | Operativo — aún atado a `DRAFTS2/` |
| Pipeline (mod) | `mod/agents/pipeline.agent.md` | Handoff final aún ligado al mapa antiguo |
| Cortos actuales | `DRAFTS2/LORE_F-02_CORTO*.md` | 5 ficheros |

## 5. Restricciones

- **`git mv` obligatorio** para todos los cortos existentes
- Depende de `LP-01b` y de la base `grafo -> universo` ya migrada
- Hay que preservar sufijos de modelo y evitar colisiones

## 6. Propuesta

### 6.1. Migrar cortos existentes (CL-01)

Mover `LORE_F-02_CORTO*.md` a `lore/derivados/cortos/` con `git mv`.

### 6.2. Recablear Dramaturgo Cortos (CL-02)

Actualizar lectura y escritura al mapa `lore/`.

### 6.3. Ajustar Pipeline y refs del tramo final (CL-03)

Cerrar la cadena `grafo -> universos -> cortos` con naming y handoffs coherentes.

### 6.4. Validar versiones y trazabilidad (CL-04)

Verificar que cada fichero mantiene universo fuente + modelo sin perder historial.

## 7. Salida operativa

- Tracking: [BACKLOG.md](./BACKLOG.md)
- Decisiones del PO: [RESPUESTAS.md](./RESPUESTAS.md)
- Tasks: carpeta [tasks](./tasks)