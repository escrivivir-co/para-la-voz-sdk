# Respuestas del usuario — corpus-legislativa

> **Fecha:** 19-abr-2026
> **Registradas por:** GPT-5.4

## Punto 1 — El corpus del mod no debe seguir escondido en un workaround

- **Contexto:** El usuario pide considerar la migración de la carpeta `corpus/` adjunta y pregunta si tiene sentido absorber esa capa con backward compatibility.
- **Respuesta del usuario (19-abr-2026):** plantea explícitamente migrar el `corpus/` actual en vez de dejarlo como shim.
- **Efecto operativo:** `corpus-legislativa` asume la materialización de `corpus/` como capa real del mod.

## Punto 2 — La abstracción correcta no es volver atrás, sino separar mejor

- **Contexto:** El usuario recuerda que legislativa ya se había alejado del viejo flujo `feed -> Bartleby -> corpus` y pregunta si ahora estamos abstrayendo de vuelta esa desviación hacia el SDK.
- **Respuesta del usuario (19-abr-2026):** pide evaluarlo en el contexto de `mod_legislativa_INDEX` y `future-machine`.
- **Efecto operativo:** Se cristaliza `corpus` como fase propia. `lore-db` sigue siendo upstream de piezas; `corpus` reaparece como capa explícita y portable.

## Punto 3 — Archivero Legislativa conserva compatibilidad, pero se recorta mejor su función

- **Contexto:** El usuario pregunta si esto equivale a devolver al Archivero convertido en "corpuseador".
- **Respuesta del usuario (19-abr-2026):** pregunta abierta sobre si esa es la lectura correcta.
- **Efecto operativo:** La recomendación operativa es conservar el nombre público `@Archivero Legislativa` por compatibilidad, pero explicitar que su dominio es la capa corpus, no la gestión de piezas ni el grafo.