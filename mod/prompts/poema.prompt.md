---
name: poema
description: Genera un poema que habla la voz del corpus restitutivo de PARA LA VOZ. El tema es opcional — si no se da, el agente escoge desde las tensiones del corpus. El poema nace del corpus, no lo describe.
argument-hint: "[tema opcional]"
agent: voz
tools: [vscode, read, edit]
---

# /poema — Generar desde la voz del corpus

Invoca al agente `voz` para generar un poema desde el corpus acumulado.

## Flujo

1. **Leer** `corpus/corpus.md` completo — la firma de voz está en el patrón acumulado

2. **Si hay argumento** (tema): úsalo como punta del iceberg. El corpus impregna desde dentro.  
   **Si no hay argumento**: elige desde el corpus una tensión activa:
   - Emergencias sin resolver (E.01–E.15)
   - Ausencias estructurales ×4 (estructurales — las que definen el perímetro de la corriente)
   - Evoluciones en curso (especialmente el marcador que varía por registro)
   - Conceptos en estabilización

3. **Anuncia brevemente** qué tensión elegiste (solo si no hay tema) — una frase, no una explicación

4. **Generar el poema**:
   - Verso corto (una idea por verso)
   - Entre 8 y 20 versos
   - Urgencia rítmica, no tipográfica
   - Vocabulario del corpus (no sinónimos)
   - Los 6 marcadores del nick como presión interna
   - Sin metalenguaje (no nombrar: corpus, análisis, emergencia, IA, aplicación)
   - Título opcional — si lo hay, que sea una frase del corpus

5. **Mostrar el poema**

6. **Una nota breve** (solo para usuarios del pipeline que conocen el corpus):  
   *[qué tensión del corpus activó — máx. dos frases]*

7. **Ofrecer handoffs** sin insistir:
   - `@bartleby` — si quieres saber por qué el poema dice lo que dice
   - `@portal-editorial` — si quieres adaptar el poema a otro contexto
