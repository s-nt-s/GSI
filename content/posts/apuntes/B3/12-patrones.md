---
title: Patrones de diseño
---

# Conceptos básicos

**Patrones de diseño**: técnicas para resolver problemas comunes en el desarrollo
de software y otros ámbitos referentes al diseño de interacción o interfaces.

**Antipatrón de diseño**: patrón de diseño que invariablemente conduce a una mala
solución para un problema.

**Patrones de arquitectura**: esquema de organización estructural esencial para
un sistema de software, que consta de subsistemas, sus responsabilidades e
interrelaciones. En comparación con los patrones de diseño, los patrones
arquitectónicos tienen un nivel de abstracción mayor.

Tipos de patrones:

* **Patrón creacional**: proporcionan mecanismos de creación de objetos que incrementan la flexibilidad y la reutilización del código existente.
* **Patrón estructural**: explican cómo ensamblar objetos y clases en estructuras más grandes, mientras se mantiene la flexibilidad y eficiencia de la estructura.
* **Patrón de comportamiento**: tratan con algoritmos y la asignación de responsabilidades entre objetos.

# Creacional

## Modelo vista controlador

![](https://upload.wikimedia.org/wikipedia/commons/a/a9/ModelViewControllerDiagram_es.svg)

A veces también es considerado un patrón de arquitectura.

## Prototype

![](https://upload.wikimedia.org/wikipedia/commons/e/ee/ProtipoEstructura.png)

## Builder

![](https://refactoring.guru/images/patterns/diagrams/builder/structure.png)

Figura: Ejemplo genérico patrón Builder

![](https://refactoring.guru/images/patterns/diagrams/builder/example-es.png)

Figura: Ejemplo de una construcción paso a paso de automóviles y de los manuales de usuario para esos modelos de automóvil.

## Factory Method

![](https://refactoring.guru/images/patterns/diagrams/factory-method/structure.png)

Figura: Ejemplo genérico patrón Factory Method

![](https://refactoring.guru/images/patterns/diagrams/factory-method/example.png)

Figura: Ejemplo del diálogo multiplataforma.

## Abstract Factory

![](https://refactoring.guru/images/patterns/diagrams/abstract-factory/structure.png)

Figura: Ejemplo genérico patrón Abstract Factory

![](https://refactoring.guru/images/patterns/diagrams/abstract-factory/example.png)

Figura: Ejemplo del diálogo multiplataforma.

## Singleton

![](https://refactoring.guru/images/patterns/diagrams/singleton/structure-es.png)

## Multiton

Igual que Singleton pero con un `Map<key, Multiton>` para permitir varias instancias.

![](https://upload.wikimedia.org/wikipedia/commons/9/9f/Multiton.svg)

## Object Pool o piscina de objetos

El pool es un conjunto de objetos inicializados preparados para su uso,
evitando tener que crear y destruirlos bajo demanda.

Un cliente del pool le pedirá un objeto para realizar las operaciones con el objeto.
Cuando el cliente termina retorna el objeto al pool para que lo retenga hasta que vuelva a necesitar usarse.
Es decir, los objetos no se crean (salvo la primera vez) ni se destruyen, simplemente se van reciclando.

## Lazy initialization

Consiste en retrasar la creación de un objeto, el calculo de un valor o
cualquier otro proceso costoso hasta la primera vez que sea necesitado.

También evita repetir la misma operación si ya ha sido realizada antes.
Es decir, mantiene una cache (por ejemplo usando un `HashMap`) para devolver
el objeto directamente si ya se inicializo anteriormente.

## RAII: adquirir recursos es inicializar

Patrón especialmente pensado para `C++`. Consiste en aprovechar que los destructures
son siempre ejecutados (cuando hay una excepción, cuando se sale de la función, etc)
para usar objetos en las operaciones de incializar y liberar recursos, garantizando
con ello que siempre se liberará cualquier recurso inicializado.

## Inyección de dependencias

Se trata de suministrar objetos a una clase en lugar de que sea la propia clase la que cree dichos objetos.
Es decir, extrae la responsabilidad de la creación de instancias de un componente para delegarla en otro.

El framework Spring implementa este patrón.

# Estructural

## Adapter, Wrapper o Translator

Transforma una interfaz en otra, de tal modo que una clase que no pueda utilizar la primera haga uso de ella a través de la segunda.

![](https://upload.wikimedia.org/wikipedia/commons/f/fd/Adapter_using_inheritance_UML_class_diagram.svg)

Figura: `Adapter` adapta `Adaptee` para que se pueda usar por clientes que esperan objetos tipo `Target`

## Bridge

Permite dividir una clase grande, o un grupo de clases estrechamente relacionadas,
en dos jerarquías separadas (abstracción e implementación) que pueden desarrollarse
independientemente la una de la otra.

![](https://refactoring.guru/images/patterns/diagrams/bridge/structure-es.png)

Figura: Ejemplo genérico patrón Bridge

![](https://refactoring.guru/images/patterns/diagrams/bridge/example-es.png)

Figura: Ejemplo mando a distancia, radio y televisión con patrón Bridge

## Composite

Sirve para construir objetos complejos a partir de otros más simples y similares entre sí, gracias a la composición recursiva y a una estructura en forma de árbol.

![](https://refactoring.guru/images/patterns/diagrams/composite/structure-es.png)

Figura: Ejemplo genérico patrón Composite

![](https://refactoring.guru/images/patterns/diagrams/composite/example.png)

Figura: Ejemplo de un gráfico que a su vez se compone de otros gráficos

## Decorator

Añade dinámicamente funcionalidad a un Objeto. Esto nos permite no tener que crear
sucesivas clases que hereden de la primera incorporando la nueva funcionalidad,
sino otras que la implementan y se asocian a la primera.

![](https://upload.wikimedia.org/wikipedia/commons/2/2a/DecoradorGenerico2.jpg)

## Facade

Proporciona una interfaz simplificada a un grupo complejo de clases.

![](https://refactoring.guru/images/patterns/diagrams/facade/structure.png)

Figura: Estructura patrón Facade

![](https://refactoring.guru/images/patterns/diagrams/facade/example.png)

Figura: Ejemplo de fachada para un sistema complejo de conversión de formatos.

## Flyweight

Elimina o reduce la redundancia entre objetos que contienen información idéntica,
logrando un equilibrio entre flexibilidad y uso de recursos.

A ser básicamente una optimización de uso de RAM, antes de aplicarlo hay que
preguntarse si realmente tenemos un problema de RAM que solucionar, en caso
contrario sería añadir complejidad para nada.

![](https://refactoring.guru/images/patterns/diagrams/flyweight/structure.png)

Figura: El Flyweight tiene el estado intrínseco (la parte del objeto original que se repite),
el Context tiene el estado extrínseco (la parte que nos e repite), el FlyweightFactory
fabrica Flyweight solo cuando no se ha creado uno igual antes.

![](https://refactoring.guru/images/patterns/diagrams/flyweight/example.png)

Figura: Ejemplo de Flyweight que evita repetir la información común de los arboles
(name, color, texture) de un bosque.

## Proxy-pattern

Proporciona un subrogado o intermediario de un objeto para controlar su acceso.

![](https://refactoring.guru/images/patterns/diagrams/proxy/structure.png)

Figura: Estructura patrón Proxy-pattern

![](https://refactoring.guru/images/patterns/diagrams/proxy/example.png)

Figura: `CachedYouTubeClass` es un Proxy-pattern de `ThirdPartyYouTubeLib` que hace lo mismo que `ThirdPartyYouTube` pero con una cache.

## Module-pattern

Implementa el concepto de módulos de software definidos por el
paradigma de programación modular, en un lenguaje de programación que no lo soporta,
o lo soporta parcialmente.

Este patrón se puede considerar una variante del singleton o instancia única,
con un propósito, más específico.

## Front controller

Proporcionar un mecanismo centralizado para manejar solicitudes, es decir,
todas las solicitudes son procesadas por un solo controlador.
Puede referirse al controlador del Modelo vista controlador.

![](https://upload.wikimedia.org/wikipedia/commons/8/8e/Front_Controller.svg)

## Marker-pattern

Proporciona información de tipo en tiempo de ejecución sobre los objetos.
Es una manera de "asociar metadatos" a una clase en un lenguaje de programación
que no tiene soporte para tales metadatos.

Un ejemplo típico es la interfaz `Serializable` de Java que básicamente sirve
para que otras clases, como `ObjectOutputStream` en su método `writeObject(Object)`,
hagan `object instanceof Serializable` y lancen `NotSerializableException` en caso
negativo.

## Twin-pattern

Permite modelar herencia múltiple en lenguajes de programación que no la admiten
directamente.

![](https://upload.wikimedia.org/wikipedia/commons/c/ce/T%C3%B6bbsz%C3%B6r%C3%B6s_%C3%B6r%C3%B6kl%C3%A9s_%28iker_minta_n%C3%A9lk%C3%BCl%29.png)

Figura: Herencia múltiple

![](https://upload.wikimedia.org/wikipedia/commons/2/28/Iker_minta.png)

Figura: Herencia múltiple implementada con patrón Twin-pattern

## Extension object

Agregar funcionalidad a una jerarquía sin cambiar la jerarquía.

![](https://i.stack.imgur.com/GoIQ6.jpg)

Figura: Fuente [stackoverflow.com/a/39346147](https://stackoverflow.com/a/39346147)

# Comportamiento

## Chain of Responsibility

Evita acoplar el emisor de una petición a su receptor dando a más de un objeto
la posibilidad de responder a una petición. Para ello, se encadenan los receptores
y pasa la petición a través de la cadena hasta que es procesada por algún objeto.

![](https://refactoring.guru/images/patterns/diagrams/chain-of-responsibility/structure.png)

Figura: Cada manejador (`ConcreteHandlers`) intenta resolver la petición, y si no
puede se la pasa al manejador de la capa superior.

![](https://refactoring.guru/images/patterns/diagrams/chain-of-responsibility/example-es.png)

Figura: GUI en la que pedir la ayuda de un elemento tiene como resultado obtener
la de dicho elemento si la tiene, y si no la del padre, y si no la del abuelo, y si no...

## Command-pattern

Convierte una solicitud en un objeto independiente que contiene toda la
información sobre la solicitud. Esta transformación te permite parametrizar
los métodos con diferentes solicitudes, retrasar o poner en cola la ejecución
de una solicitud y soportar operaciones que no se pueden realizar.

![](https://refactoring.guru/images/patterns/diagrams/command/structure.png)

Figura: Estructura patrón Command-pattern

![](https://refactoring.guru/images/patterns/diagrams/command/example.png)

Figura: Operaciones que se pueden deshacer en un editor de texto

## Iterator

Permite recorrer elementos de una colección sin exponer su representación subyacente (lista, pila, árbol, etc.).

![](https://refactoring.guru/images/patterns/diagrams/iterator/structure.png)

Figura: Estructura patrón Iterator

![](https://refactoring.guru/images/patterns/diagrams/iterator/example.png)

Figura: Itenrador de perfiles de una red social

## Mediator

Restringe las comunicaciones directas entre los objetos, forzándolos a colaborar
únicamente a través de un objeto mediador.

![](https://refactoring.guru/images/patterns/diagrams/mediator/structure.png)

Figura: Estructura patrón Mediator

![](https://refactoring.guru/images/patterns/diagrams/mediator/example.png)

Figura: GUI que usa un mediador para gestionar una página de login.

## Memento

Permite guardar y restaurar el estado previo de un objeto sin revelar los detalles de su implementación.

![](https://refactoring.guru/images/patterns/diagrams/memento/structure1.png)

Figura: `Originator` puede guardar y restaurar su propio estado guardando
y cargando objetos `Memento`. En `Caretaker` lleva un histórico de estados
que puede usar para ir del esado actual al previo.

![](https://refactoring.guru/images/patterns/diagrams/memento/example.png)

Figura: Patrón Memento + patrón Command-pattern para implementar `undo` en un editor de texto.

## Observer o Publish-subscribe

Define un mecanismo de suscripción para notificar a varios objetos sobre cualquier
evento que le suceda al objeto que están observando.

![](https://refactoring.guru/images/patterns/diagrams/observer/structure.png)

Figura: Estructura patrón Observer

## State-pattern

Implementación de un objeto de manera que su comportamiento cambia si su estado
cambia.

![](https://refactoring.guru/images/patterns/diagrams/state/structure-es.png)

Figura: El objeto `Context` hace esto o aquello según su estado (`ConcreteStates`).

![](https://refactoring.guru/images/patterns/diagrams/state/example.png)

Figura: Reproductor de música que al darle a `play` hará cosas distintas
según su estado.

## Strategy-pattern

Implementa un conjunto de algoritmos de manera que un objeto cliente puede elegir
el que quiera e incluso cambiarlo dinámicamente según sus necesidades.

![](https://refactoring.guru/images/patterns/diagrams/strategy/structure.png)

Figura: Estructura patrón Strategy-pattern

## Template Method

Define el esqueleto de un algoritmo en la superclase pero permite que las subclases
sobrescriban pasos del algoritmo sin cambiar su estructura.

![](https://refactoring.guru/images/patterns/diagrams/template-method/structure.png)

Figura: Estructura patrón Template Method

## Visitor-pattern

Separa algoritmos de los objetos sobre los que operan.

![](https://refactoring.guru/images/patterns/diagrams/visitor/structure-es.png)

Figura: Estructura patrón Visitor-pattern

![](https://refactoring.guru/images/patterns/diagrams/visitor/example.png)

Figura: Cada tipo de `Shape` al aceptar un visitante (`Visitor`) ejecuta
el método `visit***(this)` que corresponda y genera su exportación a XML

## Pizarra o Blackboard

A veces también es considerado un patrón de arquitectura.
Es habitualmente utilizado en sistemas expertos, sistemas multiagente y, en general, sistemas basados en el conocimiento.

Consta de múltiples elementos funcionales, denominados agentes, y un instrumento de control denominado pizarra.
Los agentes suelen estar especializados en una tarea concreta o elemental. Todos ellos cooperan para alcanzar una meta común, si bien, sus objetivos individuales no están aparentemente coordinados.

El comportamiento básico de cualquier agente consiste en examinar la pizarra, realizar su tarea y escribir sus conclusiones en la misma pizarra. De esta manera, otro agente puede trabajar sobre los resultados generados por otro.

## Interpreter

Define una representación para su gramática junto con un intérprete del lenguaje.

Un ejemplo seria un código que evaluá Notación polaca inversa de manera
que se le pase el string `"42 2 1 - +"` t devuelva `43`.

## Null object

Crear un objeto que representa el valor neutral `null`.
La idea es que si tenemos una interfaz `MyObject` con un método `doSomething`
no haga falta validar si una variable `MyObject` es `null` antes de
ejecutar `doSomething` porque en vez de eso tenemos una implementación
`MyObjectNull` que tiene un método `doSomething` que no hace nada.

## Circuit Breaker

Evita que una aplicación intente de manera reiterada una operación que con probabilidad va a fallar.

## Otros

* Servant-pattern
* Specification-pattern

# Concurrencia

## Cierre de exclusión mutua (lock)

Mecanismo de sincronización que limita el acceso a un recurso compartido por
varios procesos o hilos en un ambiente de ejecución concurrente, permitiendo
así la exclusión mutua.

## Monitor object

Estructuras de datos abstractas destinadas a ser usadas sin peligro por más de un hilo de ejecución.
La característica que principalmente los define es que sus métodos son ejecutados con exclusión mutua.

## Reactor

El manejador de servicio demultiplexa los pedidos entrantes y los entrega de forma
sincrónica a los manejadores de pedidos asociados.

## Otros

*  Active object
*  Balking
*  Binding properties
*  Compute kernel
*  Double-checked locking
*  Event-based asynchronous
*  Guarded suspension
*  Join-pattern
*  Messaging-pattern
*  Readers-writer lock
*  Scheduling-pattern
*  Thread pool
*  Thread-local storage

# Arquitectura

## Inversión de control

Principio de diseño de software en el que el flujo de ejecución de un programa se invierte respecto a los métodos de programación tradicionales.

Tradicionalmente el programador especifica la secuencia de decisiones y procedimientos que pueden darse durante el ciclo de vida de un programa mediante llamadas a funciones.
En su lugar, en la inversión de control se especifican respuestas deseadas a sucesos
o solicitudes de datos concretas, dejando que algún tipo de entidad o arquitectura
externa lleve a cabo las acciones de control que se requieran en el orden necesario
y para el conjunto de sucesos que tengan que ocurrir.

La Inversión de control es el concepto central del Framework de Spring y usa la implementación por Inyección de dependencias, ya que implementa un "Contenedor" que se encarga de gestionar las instancias (así como sus creaciones y destrucciones) de los objetos del usuario.

La mayoría de las bibliotecas para el desarrollo de aplicaciones con GUI, como GTK o QT usan inversión de control y están dirigidas por eventos.

## Otros

* Programación por capas
* Arquitectura de microservicios
* Arquitectura de microkernel
* Invocación implícita
* Layer-pattern
* Arquitectura hexagonal
* Arquitectura en pizarra (Blackboard)
* Arquitectura dirigida por eventos
* Peer-to-peer
* Arquitectura orientada a servicios
* Broker-pattern
* Objetos desnudos
* Modelo Vista Controlador
* Presentación Abstracción Control
* Modelo Vista Presentador
* Modelo Vista Modelo de vista
* Almacén operacional de los datos
* Tuberías y Filtros
* Esclavo-Maestro
* Control centralizado y distribuido

# Antipatrones

## Gestión de proyectos

* Humo y espejos (smoke and mirrors): Mostrar cómo será una funcionalidad antes de que esté implementada.
* Mala gestión (bad management)
* Software inflado (software bloat): Permitir que las sucesivas versiones de un sistema exijan cada vez más recursos.

## Diseño de software

* Base de datos como comunicador de procesos (database as an IPC)
* BOMQ (Batch Over MQ): Abuso en el empleo de integración basada en mensajes en tiempo real para transferencias esporádicas de gran tamaño en segundo plano.
* Clase Gorda: Dotar a una clase con demasiados atributos y/o métodos, haciéndola responsable de la mayoría de la lógica de negocio.
* Botón mágico (magic pushbutton): Tender, desarrollando interfaces, a programar la lógica de negocio en los métodos de interacción, implementando los resultados de las acciones del usuario en términos no suficientemente abstractos.
* Carrera de obstáculos (race hazard): Incapacidad de prever las consecuencias de diferentes sucesiones de eventos.
* Entrada chapuza (input kludge): No especificar e implementar el manejo de entradas inválidas.
* Fábrica de combustible (gas factory): Diseñar de manera innecesariamente compleja.
* Gran bola de lodo (big ball of mud): Construir un sistema sin estructura definida.
* Interfaz inflada (interface bloat): Pretender que una interfaz sea tan potente que resulta extremadamente difícil de implementar.
* Inversión de abstracción (abstraction inversion): No exponer las funcionalidades implementadas que los usuarios necesitan, forzando a que se reimplementen a más alto nivel.
* Punto de vista ambiguo (ambiguous viewpoint): Presentar un modelo sin concretar ciertos aspectos, postergando así decisiones conflictivas.
* Re-dependencia (re-coupling): Introducir dependencias innecesarias entre objetos.
* Sistema de cañerías de calefacción (stovepipe system): Construir un sistema difícilmente mantenible, ensamblando componentes poco relacionados.
* Seguridad por ofuscación: Generar sistemas que ocultan o hacen contra intuitivos los funcionamiento de los componentes en la entrada, en la respuesta o en los errores. Convirtiendo las herramientas o servicios de desarrollo en cajas mágicas.
* Integración dependiente continua: Realizar procesos de control para cada paso del desarrollo que dependan de la validación de terceros.

### Orientado a objetos

* Acoplamiento secuencial (sequential coupling): Construir una clase que necesita que sus métodos se invoquen en un orden determinado.
* BaseBean: Heredar funcionalidad de una clase utilidad en lugar de delegar en ella.
* Fallo de clase vacía (empty subclass failure): Clase que no supera el test de la subclase vacía, es decir, que se comporta de manera diferente cuando se invoca desde una subclase que no añade modificación alguna.
* Llamar a super (callsuper): Obligar a las subclases a llamar a un método de la superclase que ha sido sobrescrito.
* Modelo de dominio anémico (anemic domain model): Usar un modelo del dominio sin ninguna lógica de negocio. Esto no es un enfoque orientado a objetos porque cada objeto debería tener tanto propiedades como comportamiento asociado.
* Objeto sumidero (object cesspool): Reutilizar objetos no adecuados realmente para el fin que se persigue.
* Objeto todopoderoso (god object): Concentrar demasiada funcionalidad en una única parte del diseño (clase).
* Poltergeist (informática): Emplear objetos cuyo único propósito es pasar la información a terceros objetos.
* Problema del círculo-elipse (circle-ellipse problem): Crear variables de tipo pensando en los valores de posibles subtipos.
* Problema del yoyó (yo-yo problem): Construir estructuras (ej: de herencia) que son difíciles de comprender debido a su excesiva fragmentación.
* Singletonitis: Abuso de la utilización del patrón singleton.
* YAFL (yet another fucking layer, y otra maldita capa más) o *Código Lasagna*: Añadir capas innecesarias a un programa, biblioteca o framework.

## Programación

* Nomenclatura heroica (heroic naming): Los nombres de interfaces, clases, propiedades, métodos... dan a entender que el conjunto esta correctamente estandarizado con la ingeniería del software pero en realidad oculta una implementación anárquica.
* Acción a distancia (action at a distance): Provocar la interacción no prevista de componentes muy distantes de un sistema.
* Acumular y disparar (accumulate and fire): Establecer una colección de variables globales para ser usadas por un conjunto de subrutinas.
* Ancla del barco (boat anchor): Retener partes del sistema que ya no tienen utilidad.
* Bucle activo (busy spin): Utilizar espera activa cuando existen alternativas.
* Código duro (hard code): Hacer supuestos sobre el entorno del sistema en demasiados lugares de la implementación.
* Complejidad no indispensable (accidental complexity): Dotar de complejidad innecesaria a una solución.
* Código espagueti (spaghetti code): Estructuras de código difícilmente comprensibles.
* Código ravioli (ravioli code): Multitud de objetos muy débilmente conectados.
* Comprobación de tipos en lugar de interfaz (checking type instead of interface): Comprobar que un objeto es de un tipo concreto cuando lo único que se necesita es verificar si cumple un contrato determinado.
* Confianza ciega (blind faith): Descuidar la comprobación de los resultados que produce una subrutina, o bien de la efectividad de un parche o solución a un problema.
* Lava seca (lava flow): Código muerto e información de diseño olvidada que permanecen congelados en un diseño cambiante.
* Lógica super-booleana (superboolean logic): Emplear comparaciones o abstracciones de la lógica booleana innecesarias.
* Manejo de excepciones (exception handling): Emplear el mecanismo de manejo de excepciones del lenguaje para implementar la lógica general del programa.
* Manejo de excepciones inútil (useless exception handling): Introducir condiciones para evitar que se produzcan excepciones en tiempo de ejecución, pero lanzar manualmente una excepción si dicha condición falla.
* Números mágicos (magic numbers): Incluir en los algoritmos números concretos sin explicación aparente.
* Ocultación de errores (error hiding): Capturar un error antes de que se muestre al usuario, y reemplazarlo por un mensaje sin importancia o ningún mensaje en absoluto.
* Packratting: Consumir memoria en exceso debido a no liberar objetos reservados dinámicamente una vez ya han dejado de ser necesarios.
* Programación por excepción (coding by exception): Añadir trozos de código para tratar casos especiales a medida que se identifican.
* Secuencia de bucle por casos (Loop-switch sequence): Programar un conjunto de pasos secuenciales usando un bucle en combinación con una estructura de control por casos.
* Cadenas mágicas (magic strings): Incluir cadenas de caracteres determinadas en el código fuente para hacer comparaciones, como tipos de eventos, etc.
* Código ñoqui (gnocchi code): Incluir código que realmente no hacen nada ni aportan al sistema.

## Metodológicos

* Bala de plata (silver bullet): Asumir que nuestra solución técnica favorita puede resolver un problema mucho mayor.
* Desarrollo conducido por las pruebas/errores (tester/bug driven development): Permitir que un proyecto software avance a base de extraer sus nuevos requisitos de los informes de errores.
* Desfactorización (de-factoring): Eliminar funcionalidad y reemplazarla con documentación.
* Factor de improbabilidad (improbability factor): Asumir que es improbable que un error conocido cause verdaderos problemas.
* Martillo de oro (golden hammer): Asumir que nuestra solución favorita es universalmente aplicable.
* Optimización prematura (premature optimization): Realizar optimizaciones sin disponer de la información suficiente para hacerlo con garantías, sacrificando decisiones de diseño.
* Programación de copiar y pegar (copy and paste programming): Programar copiando y modificando código existente en lugar de crear soluciones genéricas.
* Programación por permutación (programming by permutation): Tratar de aproximarse a una solución modificando el código una y otra vez para ver si acaba por funcionar.
* Reinventar la rueda (reinventing the wheel)
* Reinventar la rueda cuadrada (reinventing the square wheel): Crear una solución pobre cuando ya existe una buena.

## Gestión de la configuración

* Conflicto de extensiones (extension conflict): Problemas con diferentes extensiones que tratan de gestionar las mismas partes del sistema (específico de Mac OS).
* Infierno de dependencias (dependency hell): Escenario de problemas producidos por las versiones de otros productos que se necesitan para hacer funcionar un tercero:
    * Infierno DLL (DLL hell): Específico de Microsoft Windows
    * Infierno JAR (JAR hell): Típicamente causados por la falta de comprensión del modelo de carga de clases

## Otros

* Contenedor mágico (magic container): La implementación de métodos que intentan ser tan flexibles como para adaptar su comportamiento a multitud de circunstancias, sobrepasando el umbral de una mantenibilidad adecuada del mismo.
* Descomposición funcional (functional decomposition): Traducir un programa de un lenguaje estructurado a uno OO usando una sola clase y muchos métodos privados.
* Embudo de excepciones (exception funnel): Atrapar una excepción e ignorarla, sin reportarlo.
* Moneda en punto flotante (floating point currency): Utilizar una representación en punto flotante para valores que representan dinero, lo que puede provocar pérdida de precisión.
* Valor por defecto indefinido (zero means null): Escoger un valor arbitrario para representar la indefinición, sin garantizar que ese valor no puede realmente ocurrir.

# Bibliografía

* [refactoring.guru - El catálogo de patrones de diseño](https://refactoring.guru/es/design-patterns/catalog)
* [w3big.com - Patrones de diseño](http://www.w3big.com/es/design-pattern/default.html)
* [books.studygolang.com - Go Patterns](https://books.studygolang.com/go-patterns/#anti-patterns)
* [java-design-patterns.com - Java Design Patterns](https://java-design-patterns.com/patterns/)
