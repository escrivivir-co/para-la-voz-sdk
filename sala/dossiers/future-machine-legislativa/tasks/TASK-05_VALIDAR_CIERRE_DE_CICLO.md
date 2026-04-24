# TASK-05 — Validar el cierre de ciclo

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** FL-02, FL-03, FL-04
> **Entrega esperada:** informe de validación del cierre completo

## Objetivo

Comprobar que la machine del mod realmente cierra el ciclo desde la entrada del usuario hasta la operación downstream.

## Checks mínimos

1. `Portal` presenta la machine.
2. `/user-empieza-aqui` ofrece el mapa correcto.
3. `/lore-status` ofrece dashboard coherente con la machine.
4. `Pipeline` aparece como operación de refresh del ciclo.
5. El usuario puede orientarse hacia universo/obra sin salto conceptual.

## Criterio de aceptación

- Existe informe de validación y el mod ya dispone de una future-machine navegable como cierre del ciclo.