---
title: Pruebas
status: draft
---

# Tipos de pruebas según Métrica v3

Pruebas **unitarias**: compruebas el correcto funcionamiento de una unidad de código

Pruebas de **integración**: compruebas que las unidades de código funcionan
correctamente en grupo.  Se centra principalmente en probar la comunicación
entre los componentes y sus comunicaciones ya sea hardware o software.

Pruebas del **sistema**: Pruebas de integración del sistema de información completo, y permiten probar el sistema en su conjunto y con otros sistemas con los que se relaciona para verificar que las especificaciones funcionales y técnicas se cumplen.

Pruebas de **implantación**: comprueban el funcionamiento correcto del sistema
integrado de hardware y software en el entorno de operación, y permiten al usuario
que, desde el punto de vista de operación, realice la aceptación del sistema
una vez instalado en su entorno real y en base al cumplimiento de los requisitos
no funcionales especificados.

Pruebas de **aceptación**: Valida que el sistema cumpla con el funcionamiento
esperado y permite al usuario que determine su aceptación, desde el punto de
vista de su funcionalidad y rendimiento.

Pruebas de **regresión**: Valida que los cambios sobre un componente no
introducen nuevos errores o un comportamiento no deseado en otros componentes
no modificados.

# Pruebas de caja...

Pruebas de **caja blanca**: el esfuerzo se concentra en encontrar casos de
prueba que permitan comprobar cómo funciona el código en cualquier situación,
lo que supone, como mínimo, recorrer todos sus caminos con un conjunto tan
amplio de datos de prueba como sea necesario. En resumen, se trataría de
recorrer exhaustivamente todos los caminos posibles.

Pruebas de **caja negra**: Se trata al programa desde el punto de vista de las
entradas que recibe y las salidas que produce, sin tener en cuenta su
funcionamiento interno, buscando circunstancias en las que el programa no se
comporte de acuerdo con las especificaciones.

Pruebas de **caja gris**: El tester tiene un conocimiento limitado de los
detalles internos del programa, se utilizan comúnmente en las
pruebas de **penetración**.

# Pruebas estáticas y dinámicas

Pruebas **estáticas**: se realizan sin ejecutar el código de la aplicación.

Pruebas **dinámicas**: requieren la ejecución de la aplicación, permitiendo
medir con mayor precisión el comportamiento de la aplicación desarrollada.

# Funcionales y no funcionales

Pruebas **funcionales**: basadas en la ejecución, revisión y retroalimentación
de las funcionalidades previamente diseñadas para el software (requisitos funcionales).
Pueden ser:

* Pruebas unitarias
* Pruebas de integración
* Pruebas de sistema
* Pruebas de aceptación
* Pruebas de regresión
* Pruebas **alpha**: hay varias definiciones
    * pruebas realizadas por el usuario con el desarrollador como observador en un entorno
controlado
    * pruebas para validar un prototipo antes de implementar la versión real
    * última prueba realizada por los equipos de prueba en el sitio de desarrollo después de la prueba de aceptación y antes de lanzar el software para la prueba beta
* Pruebas **beta**: pruebas realizadas sobre una versión beta por usuarios finales
o betatester.

Pruebas **no funcionales**: su objetivo es la verificación de un requisito
que especifica criterios usados para juzgar la operación de un sistema (requisitos no
funcionales) como por ejemplo la disponibilidad, accesibilidad, usabilidad,
mantenibilidad, seguridad, rendimiento.
Se pueden clasificar según el tipo de requisito que abarcan:

* Pruebas de compatibilidad
* Pruebas de seguridad
* Pruebas de carga
* Pruebas de usabilidad
* Pruebas de rendimiento
* Pruebas de internacionalización y localización
* Pruebas de escalabilidad
* Pruebas de mantenibilidad
* Pruebas de instalabilidad
* Pruebas de portabilidad

# Bibliografía

* PreparaTic27 - Pack3/07/21
* [manuel.cillero.es - Pruebas](https://manuel.cillero.es/doc/metodologia/metrica-3/tecnicas/pruebas/)
* [testermoderno.com - Caja blanca vs Caja negra](https://www.testermoderno.com/caja-blanca-vs-caja-negra/)
* [wikipedia.org - Pruebas de software](https://es.wikipedia.org/wiki/Pruebas_de_software)
* [myservername.com - Pruebas alfa y beta (una guía completa)](https://es.myservername.com/alpha-testing-beta-testing)
* [wikipedia.org - Pruebas de validación](https://es.wikipedia.org/wiki/Pruebas_de_validaci%C3%B3n)
