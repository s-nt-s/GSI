---
title: Microservicios
status: draft
---

# Conceptos básicos


# Microservicios

La arquitectura de microservicios consiste en construir una aplicación como un
conjunto de pequeños servicios, los cuales se ejecutan en su propio
proceso y se comunican con mecanismos ligeros (normalmente una API de recursos HTTP).

Cada servicio se encarga de implementar una funcionalidad completa del negocio,
es desplegado de forma independiente y puede estar programado en distintos
lenguajes y usar diferentes tecnologías de almacenamiento de datos.

## Ventajas e inconvenientes

**Ventajas**:

* Despliegue: los ciclos de desarrollo pueden ser más cortos
* Fiabilidad: los fallos en un microservicio no tienen porque afectar al resto
* Disponibilidad: se puede desplegar una nueva versión de un microservicio sin
reiniciar la aplicación/servidor.
* Escalabilidad: en cada momento se pueden aumentar las instancias de los
microservicios que soporten más carga de trabajo
* Modificabilidad: los microservicio tienen bajo acoplamiento por lo que se pueden
usar distintos frameworks
* Gestión: los equipos grandes pueden dividirse en tareas independientes y pasar
a ser autonomos
* Facilidad para comprender cada microservicio individualmente
* Facilidad para probar y desplegar un microservicio individualmente (pruebas unitarias)

**Inconvenientes**:

* Despliegue:
    * se necesitas más scripts, archivos de configuración, etc.
    * se necesitan perfiles DevOps o CI/CD
    * en algunos casos, no se puede desplegar una funcionalidad de forma independiente
    debido a la interdependencia entre servicios
* Rendimiento: los microservicios emplean colas para comunicarse, mientras que los
módulos monolíticos invocan métodos
* Testeabilidad: las pruebas de integración pueden ser más complejas si los
microservicios emplean diferentes entornos
* Gestión: aumenta el esfuerzo de gestión al tener más logs, runtimes y componentes
* Duplicidades: librerías y componentes pueden estar replicados en varios microservicios
* Mayor dificultad de comprender el sistema de manera global

## Micro-frontends

Tradicionalmente las interfaces de usuario en una arquitectura microservicios
seguían siendo un monolito (por ejemplo, una servidor web MVC que genera un `front`
HTML + JavaScript, mientras que el `backend` es una arquitectura microservicios)
pero existe la alternativa de tratar la interfaz también como microservicios.

A esto se le llama Composite UI o micro-frontends y consiste en dividir la
interfaz en piezas que son generadas por separado como microservicios.

Sus **ventajas** son:

* Evita que el `fronted` pueda ser un cuello de botella
* Escala bien
* Los equipos de desarrollo puedan desarrollar su negocio de extremo
a extremo (desde el backend hasta el frontend).

![Organización de los equipos según el enfoque](img/micro-frontend.png)

Figura 1: Organización de los equipos según el enfoque

Tecnologías que pueden intervenir en el enfoque micro-frontends:

* Custom Elements: conjunto de APIs de JavaScript que permiten definir elementos (etiquetas HTML) personalizados y su comportamiento
* Server Side Includes: conjunto de directivas que se escriben en las páginas HTML y que se evalúan en el servidor web cuando se solicita la página HTML (en especial `<!--#include ... -->`)
* Edge Side Includes: permite a los servidores de edge (como las cachés de Varnish) mezclar y matchear contenido procedente de múltiples direcciones URL (`<esi:include ... />`)

Como **inconveniente** tiene que puede ser dificil mantener la consistencia de
la presentación.

## Comunicación con los microservicios

### Tipos de comunicación

La comunicación realizada puede ser:

* Síncrona (**HTTP-REST**) mediante petición/respuesta (exponiendo las API).
    * Ventajas:
        * interactuá bien con una interfaz web
        * los desarrolladores están familiarizados con HTTP-REST
        * es fácil de depurar
        * facilita ofrecer APIs a terceros
    * Desventajas:
        * No ofrece las ventajas de AMQP
* Asíncrona (**AMQP**) mediante un broker de mensajes como RabbitMQ o Kafka
    * Ventajas:
        * es muy rápido
        * es flexible
        * consume pocos recursos
        * puede priorizar unos mensajes sobre otros en la cola
        * es compatible con XA transactions
        * es tolerante a fallos
        * puede asegurar que el mensaje es entregado una sola vez
        * ofrece pub/sub interface
        * permite segmentación de mensajes y agrupado de mensajes
        * puedes tener un hilo separado para escuchar las respuestas
    * Desventajas:
        * El broker pasa a ser un servicio critico

### API Gateway

En una arquitectura monolitica el servidor gestiona directamente las peticiones
de los clientes, pero en una arquitectura de microservicios podría ser necesario
consultar varios de ellos y combinar sus respuestas. Para alejar esta problemática
del usuario/frontend se emplea la API Gateway.

Físicamente esta conformado por una serie de archivos de configuración (ej YAML)
sobre un servidor web (ej nginx) que indican la forma de diseccionar las solicitudes.

Además puede incluir funciones de:

* autenticación
* cumplimiento de la política de seguridad
* balanceo de carga
* gestión de contratos y acuerdos de nivel de servicio (SLA)
* gestión de caché
* resolución de dependencias

# Bibliografía

* PreparaTic27 - Pack3/02
* PreparaTic27 - Pack3/03
* [docs.microsoft.com - Creación de interfaces de usuario compuestas basadas en microservicios](https://docs.microsoft.com/es-es/dotnet/architecture/microservices/architect-microservice-container-applications/microservice-based-composite-ui-shape-layout)
* [micro-frontends-es.org - Micro Frontends](https://micro-frontends-es.org/)
* [desarrolloweb.com - Especificación Custom Elements, explicaciones y práctica](https://desarrolloweb.com/articulos/desarrollo-custom-elements-javascript-estandar.html)
* [docs.microsoft.com - Diferencias entre el patrón de puerta de enlace de API y la comunicación directa de cliente a microservicio](https://docs.microsoft.com/es-es/dotnet/architecture/microservices/architect-microservice-container-applications/direct-client-to-microservice-communication-versus-the-api-gateway-pattern)
* [techtarget.com - API Gateway](https://searchdatacenter.techtarget.com/es/definicion/API-Gateway-o-puerta-de-enlace-API)
* [stackoverflow.com - Service Oriented Architecture - AMQP or HTTP](https://stackoverflow.com/questions/16838416/service-oriented-architecture-amqp-or-http)
