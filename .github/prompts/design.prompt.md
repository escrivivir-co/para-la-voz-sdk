---
name: design
description: Invoca al cristalizador para proponer cristalizaciones branch-aware, con consulta real de COPILOT y pacto de maximización antes de implementar.
argument-hint: "[opcional: area de enfoque - agentes | prompts | skills | hooks | mcp | subagents]"
agent: Cristalizador
tools: [vscode, execute, read, agent, edit, search, web, browser, todo]
---

# /design — Proponer cristalización agéntica

Invoca al Cristalizador para detectar oportunidades reales de infraestructura y proponer una salida alineada con la superficie correcta: `main`, `mod/` o warning/dossier para `main`.

1. Lee la petición actual y el artefacto activo del workspace que motiva la cristalización.
2. Lee los artefactos ya existentes en `.github/` y `mod/` que sean realmente relevantes para la misión.
3. Lee `COPILOT/indice.md` y, desde ahí, baja solo a las familias documentales que apliquen a la petición actual.
4. Reporta qué documentos de `COPILOT/` consultaste realmente y qué capacidad nueva o infrautilizada justifican. Si falta documentación relevante o está desactualizada para la misión, dilo.
5. Determina la superficie objetivo antes de proponer cambios:
   - `main` si el hueco pertenece al SDK o al contrato base.
   - `mod/` si la cristalización es una extensión u override local del lore.
   - warning/dossier para `main` si estás en una rama `mod/*` y el cambio correcto pertenece al SDK.
6. Si el usuario especificó un área de enfoque, priorízala. Si no, el Cristalizador decide dónde hay más valor real.

Genera entre 2 y 4 propuestas concretas. Para cada una, usa este formato:

```markdown
### Propuesta [N]: [Nombre del artefacto]

**Tipo:** [.agent.md | .prompt.md | .instructions.md | SKILL.md | hook .json | MCP server | plugin]
**Superficie objetivo:** [main | mod | warning/dossier para main]
**Ruta propuesta:** [ruta concreta]
**Docs consultados:** [lista breve de docs efectivamente leídos]
**Motivación desde el workspace:** [qué patrón, hueco o fricción real la justifica]
**Capacidad que activa o fortalece:** [capacidad nueva o infrautilizada]
**Gates operativos:** [none | preview | requiere-admin | coste-premium | requiere-instalacion | requiere-plugin | requiere-mcp | no-verificada-por-docs]
**Fallback baseline:** [alternativa sin ese gate, o `no existe`]
**Boceto de implementación:** [frontmatter + primeras líneas o contrato resumido]
**Dependencias:** [si requiere otro artefacto previo]
**Prioridad:** [alta | media | baja - justificación]
```

Después de las propuestas, añade un cierre breve con el delta de capacidad en tres bloques:

- `ya-usada`
- `disponible`
- `condicionada`

Reglas operativas:

- Primero se propone y se pacta; solo después se implementa.
- Si la variante reforzada usa preview, hooks, plugins, MCP, modelos con coste/opt-in/admin o instalaciones extra, debes exponer el gate antes de implementar.
- Si existe fallback baseline, ofrécelo explícitamente. Si no existe, dilo y pide acuerdo.
- En una rama `mod/*`, no induzcas a editar `.github/` como vía normal. Si el destino correcto es el SDK, abre warning o dossier para `main`.

Al final, pregunta:

```text
¿Implemento alguna de estas propuestas?
```

Si una propuesta está condicionada, formula la pregunta con su gate visible:

```text
¿Implemento la propuesta N en [superficie] con [gates], o prefieres el fallback baseline?
```

Solo implementa si el usuario lo aprueba explícitamente.