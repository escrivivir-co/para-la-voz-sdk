# /sala-archivar — Archivado de sprint y reset de sala

Prompt de cierre de ciclo. Archiva la sala completa cuando un sprint termina y prepara la estructura para el siguiente lote.

> **Protocolo transversal:** `mod/instructions/sala-protocolo.instructions.md` §6 aplica. Solo se ejecuta cuando el tablero está 100% cerrado.

---

## Uso

```
/sala-archivar {nombre-sprint}
```

**Ejemplos:**
- `/sala-archivar cristalizacion-v1`
- `/sala-archivar sala→sdk`

---

## Pasos (Aleph los ejecuta)

### 1. Verificar precondición (§6.1)

Lee `DRAFTS2/sala/tablero.md`:
- Resumen: 0 libres, 0 en-curso.
- Todos los agentes: `Estado: disponible`.
- Backlog post-sprint registrado (si existe).

**Si no se cumple → parar.** Reportar qué tasks quedan abiertas.

### 2. Archivar sala

```bash
mkdir -p DRAFTS2/sala/archivo/sprint-{nombre}
mv DRAFTS2/sala/tablero.md DRAFTS2/sala/archivo/sprint-{nombre}/
mv DRAFTS2/sala/agente-* DRAFTS2/sala/archivo/sprint-{nombre}/
mv DRAFTS2/sala/activacion-orquestador.md DRAFTS2/sala/archivo/sprint-{nombre}/ 2>/dev/null || true
```

Contenido archivado (read-only a partir de ahora):
- `tablero.md` — registro completo de tracks, cerradas y backlog
- `agente-{alias}/estado.md` — log histórico de cada agente
- Cualquier fichero de activación o referencia de la sala

### 3. Archivar dossiers cerrados

Para cada carpeta de cristalización cuyas tasks estén **todas cerradas**:

```bash
mv DRAFTS2/{dossier}/ DRAFTS2/sala/archivo/sprint-{nombre}/dossiers/
```

Si un dossier tiene tasks transferidas al siguiente sprint, **se mantiene activo** — no se mueve.

### 4. Registrar cierre

Crear `DRAFTS2/sala/archivo/sprint-{nombre}/CIERRE.md`:
```markdown
# Cierre — sprint-{nombre}

- Fecha: {fecha}
- Tasks cerradas: {n}/{total}
- Tasks no-aplica: {n}
- Agentes participantes: {lista}
- Backlog transferido: {BL-ids o "ninguno"}
- Dossiers archivados: {lista}
- Dossiers activos (no archivados): {lista o "ninguno"}
```

### 5. Inicializar nueva sala (opcional)

Si hay un siguiente lote planificado:

1. Crear `DRAFTS2/sala/tablero.md` nuevo con tracks del siguiente sprint.
2. Crear carpetas `agente-{alias}/estado.md` limpias.
3. Crear `DRAFTS2/sala/activacion-orquestador.md` si procede.

Si no hay siguiente lote inmediato, la sala queda vacía (solo `archivo/`).

### 6. Confirmar al PO

```
Sprint {nombre} archivado.
- {n} tasks cerradas, {n} dossiers archivados.
- Backlog transferido: {BL-ids}.
- Sala {limpia | inicializada para sprint {nuevo-nombre}}.
```

---

## Regla de seguridad

**No se borra nada.** Se mueve a `archivo/`. El historial de la sala es evidencia de trabajo y referencia para futuros sprints. Si un dossier archivado necesita reactivarse, se copia de vuelta (nunca se mueve desde archivo).
