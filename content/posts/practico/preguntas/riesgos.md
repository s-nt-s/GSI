---
title: Evaluación de riesgos
---

El análisis de riesgos consiste en el estudio de las posibles amenazas así como
los daños que estos puedan producir en los activos de la organización.

Para la evaluación de riesgos se utilizará la metodología Magerit
por ser la más extendida en la Administración. Para facilitar su realización se
utilizará la herramienta MicroPilar del CCN-CERT que que se adaptada al ENS.

Los pasos a seguir serán determinar:

1. los activos relevantes para la organización: servicios, información, etc
2. amenazas: causa potencial de un incidente que puede causar daños
3. vulnerabilidad: defecto o debilidad que habilita o facilita la materialización de una amenaza
4. impacto: consecuencia que sobre un activo tiene la materialización de una amenaza
5. riesgo: estimación del grado de exposición a que una amenaza se materialice

Los activos se clasifican en:

* Esenciales:
    * servicios
    * información
* Subordinados:
    * datos que materializan la información
    * servicios auxiliares que se necesitan para poder organizar el sistema
    * aplicaciones informáticas (software) que permiten manejar los datos
    * equipos informáticos (hardware) que permiten hospedar datos, aplicaciones
    y servicios
    * soportes de información que son dispositivos de almacenamiento de datos
    * equipamiento auxiliar que complementa el material informático
    * redes de comunicaciones que permiten intercambiar datos
    * instalaciones que acogen equipos informáticos y de comunicaciones
    * personas que explota u operan todos los elementos anteriores

| Activo | Amenaza | Vulnerabilidad | Impacto | Riesgo | Dimensión |
|--------|---------|----------------|---------|--------|-----------|
| Subsistema A | Que los organismos no cumplan la obligación | Baja | Alto | Medio | D |
| ^ | Problemas de sincronización | Baja | Medio | Medio | ACID |
| ^ | Código dañino en los datos | Baja | Medio | Medio | CID |
| Subsistema B | Suplantación de identidad del usuario | Baja | Medio | Medio | ACI |
| ^ | Ataques externos | Media | Medio | Medio | D |
| ^ | Corrupción de datos | Baja | Bajo | Medio | AI |
| Información | Manipulación o perdida de datos | Media | Medio | Medio | IDT |
| ^ | Destrucción de la información | Media | Alto | Medio | D |
| Comunicaciones y Hardware |Desastres naturales | Baja | Alto | Medio | IDT |
| ^ | Caídas de las redes | Media | Bajo | Medio | D |
| ^ | Interceptación de información | Media | Medio | Bajo | C |
| Sistemas externos | Interrupción de los servicios | Media | Alto | Alto | D |

# [Ejemplos de amenazas](https://www.ccn-cert.cni.es/documentos-publicos/1791-magerit-libro-ii-catalogo/file.html)

1. Desastres naturales
    1. Fuego
    2. Daños por agua
    3. Desastres naturales
2. De origen industrial
    1. Fuego
    2. Daños por agua
    3. Desastres industriales
    4. Contaminación mecánica
    5. Contaminación electromagnética
    6. Avería de origen físico o lógico
    7. Corte del suministro eléctrico
    8. Condiciones inadecuadas de temperatura o humedad
    9. Fallo de servicios de comunicaciones
    10. Interrupción de otros servicios y suministros esenciales
    11. Degradación de los soportes de almacenamiento de la información
    12. Emanaciones electromagnéticas
3. Errores y fallos no intencionados
    1. Errores de los usuarios
    2. Errores del administrador
    3. Errores de monitorización (log)
    4. Errores de configuración
    5. Deficiencias en la organización
    6. Difusión de software dañino
    7. Errores de [re-]encaminamiento
    8. Errores de secuencia
    9. Escapes de información
    10. Alteración accidental de la información
    11. Destrucción de información
    12. Fugas de información
    13. Vulnerabilidades de los programas (software)
    14. Errores de mantenimiento / actualización de programas (software)
    15. Errores de mantenimiento / actualización de equipos (hardware)
    16. Caída del sistema por agotamiento de recursos
    17. Pérdida de equipos
    18. Indisponibilidad del personal
4. Ataques intencionados
    1. Manipulación de los registros de actividad (log)
    2. Manipulación de la configuración
    3. Suplantación de la identidad del usuario
    4. Abuso de privilegios de acceso
    5. Uso no previsto
    6. Difusión de software dañino
    7. [Re-]encaminamiento de mensajes
    8. Alteración de secuencia
    9. Acceso no autorizado
    10. Análisis de tráfico
    11. Repudio
    12. Interceptación de información (escucha)
    13. Modificación deliberada de la información
    14. Destrucción de información
    15. Divulgación de información
    16. Manipulación de programas
    17. Manipulación de los equipos
    18. Denegación de servicio
    19. Robo
    20. Ataque destructivo
    21. Ocupación enemiga
    22. Indisponibilidad del personal
    23. Extorsión
    24. Ingeniería social (picaresca)
