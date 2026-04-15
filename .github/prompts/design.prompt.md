---
name: design
description: Invoca al cristalizador para proponer nuevos artefactos VS Code Copilot que cristalicen los patrones del corpus. En cada iteración activa al menos una capacidad Copilot aún no usada en el proyecto.
argument-hint: "[opcional: área de enfoque — agentes | prompts | skills | hooks | mcp | subagents]"
agent: cristalizador
tools: ['search/codebase', 'web/fetch']
---

# /design — Proponer cristalización agéntica

Invoca al cristalizador para generar propuestas de nuevos artefactos VS Code Copilot basadas en el corpus actual.

1. Lee `PROYECTOS/BARTLEBY/corpus/corpus.md` — patrones acumulados
2. Lee `PROYECTOS/BARTLEBY/.github/` — artefactos existentes (agents/, prompts/, skills/, hooks/)
3. Lee la documentación de referencia en `COPILOT/`:
   - `custom-agents.instructions.md`
   - `skill.instructions.md`
   - `hooks.instructions.md`
   - `agents.instructions.md`
   - `mcp.instructions.md`

4. Si el usuario especificó un área de enfoque, prioriza propuestas de ese tipo.
   Si no, el cristalizador decide qué capacidad no-usada priorizar.

5. Genera entre 2 y 4 propuestas concretas, cada una con:
   - Tipo de artefacto
   - Capacidad Copilot nueva que activa
   - Motivación desde el corpus
   - Boceto de implementación (frontmatter + primeras líneas)
   - Prioridad

6. Pregunta al usuario: "¿Implemento alguna de estas propuestas?"

Solo implementa si el usuario lo aprueba explícitamente.
