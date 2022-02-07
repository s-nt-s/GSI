---
title: Planificacion
status: draft
---

# Métrica v3

|                                         |   | < | < | < | < | < | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12|
|:----------------------------------------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **ESTABLECER COMITÉ DE SEGUIMIENTO**    |Hito|  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Estudio de viabilidad del sistema       | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Establecimiento de recursos             |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Contratación del equipo de recursos     |   |   | X | < | < | < |   |   |   |   |   |   |   |   |   |   |   |   |
| Búsqueda en el CTT                      |   |   | X | < |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Establecimiento de convenidos           |   |   | X | < |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Elaboración de planes específicos       |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Contratación del equipamiento           |   |   |   | X | < |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Elaboración del plan de proyecto        |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |
| **INICIO DEL DESARROLLO**               |   |   |   |   |   |   |Hito|  |   |   |   |   |   |   |   |   |   |   |
| Análisis                                |   |   |   |   |   |   | X | < |   |   |   |   |   |   |   |   |   |   |
| _ Especificación de requisitos          |   |   |   |   |   |   | x | < |   |   |   |   |   |   |   |   |   |   |
| _ Especificación del plan de pruebas    |   |   |   |   |   |   |   | x |   |   |   |   |   |   |   |   |   |   |
| Diseño                                  |   |   |   |   |   |   |   |   | X | < |   |   |   |   |   |   |   |   |
| Construcción                            |   |   |   |   |   |   |   |   |   |   | X | < | < | < |   |   |   |   |
| _ Programación                          |   |   |   |   |   |   |   |   |   |   | x | < |   |   |   |   |   |   |
| _ Pruebas unitarias                     |   |   |   |   |   |   |   |   |   |   |   | x |   |   |   |   |   |   |
| _ Pruebas de integración                |   |   |   |   |   |   |   |   |   |   |   |   | x |   |   |   |   |   |
| _ Pruebas del sistema                   |   |   |   |   |   |   |   |   |   |   |   |   |   | x |   |   |   |   |
| _ Elaboración de Manuales de Usuario    |   |   |   |   |   |   |   |   |   |   |   |   | x | < |   |   |   |   |
| Implantación y Aceptación               |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X | < | < | < |
| _ Instalación de equipamiento           |   |   |   |   |   |   |   |   |   |   |   |   |   |   | x | < |   |   |
| _ Formación de usuarios                 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | x | < |   |   |
| _ Paso al entorno de operación          |   |   |   |   |   |   |   |   |   |   |   |   |   |   | x | < |   |   |
| _ Pruebas de implantación               |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | x |   |
| _ Elaboración del plan de mantenimiento |   |   |   |   |   |   |   |   |   |   |   |   |   |   | x | < | < |   |
| _ Pruebas de aceptación                 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | x |
| **PASO A PRODUCCIÓN**                   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |Hito|
| Seguimiento y control del proyecto      |   |   |   |   |   |   | X | < | < | < | < | < | < | < | < | < | < | < |
| Seguridad                               | X | < | < | < | < | < | < | < | < | < | < | < | < | < | < | < | < | < |
| Gestión de la configuración             | X | < | < | < | < | < | < | < | < | < | < | < | < | < | < | < | < | < |
| Calidad                                 | X | < | < | < | < | < | < | < | < | < | < | < | < | < | < | < | < | < |

# [SCRUM]({filename}/posts/apuntes/B3/01-ciclo_vida.md#scrum)

Se utilizará la metodología SCRUM con un equipo formado por:

* Un Product Owner con dedicación de al menos un 50%
* Un Scrum Master con dedicación de al menos un 50%
* Un development team de entre 5 y 10 miembros a tiempo completo

En caso de ser necesario se contemplará la inclusión de un perfil Product Owner Proxy
para facilitar la iteración con el Produt Owner en caso de que este tenga poca
disponibilidad y alta carga de trabajo.

EL Product Owner podrá ser el Jefe de Área y el Product Owner Proxy el Jefe de servicio.

El desarrollo se realizara en sprints de 2 a 3 semanas que iniciaran con el
Sprint planning y terminará con el Spring review, más un daily scrum por
cada jornada del sprint.

Se designará un Sprint 0 para llevar tareas como el estudio de viabilidad del
sistema, la búsqueda de soluciones en el CTT y de modelos de datos en el CISE,
y la definición del product backlog inicial.

Como orientación inicial se reparte las tareas principales en los siguientes sprints

1. Sprint 1: sub-sistema 1
2. Sprint 1: sub-sistema 2
3. Sprint 1: sub-sistema 3
4. Sprint 1: sub-sistema 4
5. ...

De manera que el desarrollo este finalizado en X meses.

Si para la fase de mantenimiento se detecta una carga de trabajo insuficiente
para continuar con el planteamiento anterior se optará por un esquema clásico
con un equipo reducido de soporte e incidencias.
