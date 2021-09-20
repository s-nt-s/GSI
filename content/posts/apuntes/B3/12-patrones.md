---
title: Patrones de diseño
status: draft
---

 Conceptos básicos

**Patrones de diseño**: técnicas para resolver problemas comunes en el desarrollo
de software y otros ámbitos referentes al diseño de interacción o interfaces.

**Antipatrón de diseño**: patrón de diseño que invariablemente conduce a una mala
solución para un problema.

**Patrones de arquitectura**: esquema de organización estructural esencial para
un sistema de software, que consta de subsistemas, sus responsabilidades e
interrelaciones. En comparación con los patrones de diseño, los patrones
arquitectónicos tienen un nivel de abstracción mayor.

# Creacional

## [Modelo vista controlador](https://es.wikipedia.org/wiki/Modelo%E2%80%93vista%E2%80%93controlador)

![](https://upload.wikimedia.org/wikipedia/commons/a/a9/ModelViewControllerDiagram_es.svg)

A veces también es considerado un patrón de arquitectura.

## [Prototype](https://es.wikipedia.org/wiki/Prototipo_(patr%C3%B3n_de_dise%C3%B1o))

![](https://upload.wikimedia.org/wikipedia/commons/e/ee/ProtipoEstructura.png)

## [Builder](https://es.wikipedia.org/wiki/Builder_(patr%C3%B3n_de_dise%C3%B1o))

![](https://refactoring.guru/images/patterns/diagrams/builder/structure.png)

Figura: Ejemplo genérico patrón Builder

![](https://refactoring.guru/images/patterns/diagrams/builder/example-es.png)

Figura: Ejemplo de una construcción paso a paso de automóviles y de los manuales de usuario para esos modelos de automóvil.

## [Factory Method](https://es.wikipedia.org/wiki/Factory_Method_(patr%C3%B3n_de_dise%C3%B1o))

![](https://upload.wikimedia.org/wikipedia/commons/7/73/Factory_Method.png)

## [Abstract Factory](https://es.wikipedia.org/wiki/Abstract_Factory)

![](https://upload.wikimedia.org/wikipedia/commons/b/b7/Diagrama_Abstract_Factory.png)

## [Singleton](https://es.wikipedia.org/wiki/Singleton)

![](https://upload.wikimedia.org/wikipedia/commons/f/fb/Singleton_UML_class_diagram.svg)

## [Multiton](https://en.wikipedia.org/wiki/Multiton_pattern)

Igual que Singleton pero con un `Map<key, Multiton>` para permitir varias instancias.

![](https://upload.wikimedia.org/wikipedia/commons/9/9f/Multiton.svg)

## [Object pool](https://es.wikipedia.org/wiki/Object_pool_(patr%C3%B3n_de_dise%C3%B1o)) o piscina de objetos

El pool es un conjunto de objetos inicializados preparados para su uso,
evitando tener que crear y destruirlos bajo demanda.

Un cliente del pool le pedirá un objeto para realizar las operaciones con el objeto.
Cuando el cliente termina retorna el objeto al pool para que lo retenga hasta que vuelva a necesitar usarse.
Es decir, los objetos no se crean (salvo la primera vez) ni se destruyen, simplemente se van reciclando.

## [Lazy initialization](https://en.wikipedia.org/wiki/Lazy_initialization)

Consiste en retrasar la creación de un objeto, el calculo de un valor o
cualquier otro proceso costoso hasta la primera vez que sea necesitado.

También evita repetir la misma operación si ya ha sido realizada antes.
Es decir, mantiene una cache (por ejemplo usando un `HashMap`) para devolver
el objeto directamente si ya se inicializo anteriormente.

## [RAII](https://es.wikipedia.org/wiki/RAII): adquirir recursos es inicializar

Patrón especialmente pensado para `C++`. Consiste en aprovechar que los destructures
son siempre ejecutados (cuando hay una excepción, cuando se sale de la función, etc)
para usar objetos en las operaciones de incializar y liberar recursos, garantizando
con ello que siempre se liberará cualquier recurso inicializado.

## [Inyección de dependencias](https://es.wikipedia.org/wiki/Inyecci%C3%B3n_de_dependencias)

Se trata de suministrar objetos a una clase en lugar de que sea la propia clase la que cree dichos objetos.
Es decir, extrae la responsabilidad de la creación de instancias de un componente para delegarla en otro.

El framework Spring implementa este patrón.

# Estructural

## [Adapter](https://es.wikipedia.org/wiki/Adaptador_(patr%C3%B3n_de_dise%C3%B1o)), Wrapper o Translator

Transforma una interfaz en otra, de tal modo que una clase que no pueda utilizar la primera haga uso de ella a través de la segunda.

![](https://upload.wikimedia.org/wikipedia/commons/f/fd/Adapter_using_inheritance_UML_class_diagram.svg)

Figura: `Adapter` adapta `Adaptee` para que se pueda usar por clientes que esperan objetos tipo `Target`

## [Bridge](https://es.wikipedia.org/wiki/Bridge_(patr%C3%B3n_de_dise%C3%B1o))

Permite dividir una clase grande, o un grupo de clases estrechamente relacionadas,
en dos jerarquías separadas (abstracción e implementación) que pueden desarrollarse
independientemente la una de la otra.

![](https://refactoring.guru/images/patterns/diagrams/bridge/structure-es.png)

Figura: Ejemplo genérico patrón Bridge

![](https://refactoring.guru/images/patterns/diagrams/bridge/example-es.png)

Figura: Ejemplo mando a distancia, radio y televisión con patrón Bridge

## [Composite](https://es.wikipedia.org/wiki/Composite_(patr%C3%B3n_de_dise%C3%B1o))

Sirve para construir objetos complejos a partir de otros más simples y similares entre sí, gracias a la composición recursiva y a una estructura en forma de árbol.

![](https://refactoring.guru/images/patterns/diagrams/composite/structure-es.png)

Figura: Ejemplo genérico

![](https://refactoring.guru/images/patterns/diagrams/composite/example.png)

Figura: Ejemplo de un gráfico que a su vez se compone de otros gráficos

## [Decorator](https://es.wikipedia.org/wiki/Decorator_(patr%C3%B3n_de_dise%C3%B1o))


## [Facade](https://es.wikipedia.org/wiki/Facade_(patr%C3%B3n_de_dise%C3%B1o))


## [Flyweight](https://es.wikipedia.org/wiki/Flyweight_(patr%C3%B3n_de_dise%C3%B1o))


## [Proxy](https://es.wikipedia.org/wiki/Proxy_(patr%C3%B3n_de_dise%C3%B1o))


## [Module](https://es.wikipedia.org/wiki/M%C3%B3dulo_(patr%C3%B3n_de_dise%C3%B1o))


## [Front controller](https://en.wikipedia.org/wiki/Front_controller)


## [Marker](https://en.wikipedia.org/wiki/Marker_interface_pattern)


## [Twin](https://en.wikipedia.org/wiki/Twin_pattern)

## Otros

* **Extension object**: Adding functionality to a hierarchy without changing the hierarchy.

# Comportamiento


## [Blackboard](https://en.wikipedia.org/wiki/Blackboard_(design_pattern))


## [Chain of Responsibility](https://es.wikipedia.org/wiki/Cadena_de_responsabilidad)


## [Command](https://es.wikipedia.org/wiki/Command_(patr%C3%B3n_de_dise%C3%B1o))


## [Interpreter](https://es.wikipedia.org/wiki/Interpreter_(patr%C3%B3n_de_dise%C3%B1o))


## [Iterator](https://es.wikipedia.org/wiki/Iterador_(patr%C3%B3n_de_dise%C3%B1o))


## [Mediator](https://es.wikipedia.org/wiki/Mediator_(patr%C3%B3n_de_dise%C3%B1o))


## [Memento](https://es.wikipedia.org/wiki/Memento_(patr%C3%B3n_de_dise%C3%B1o))


## [Null object](https://en.wikipedia.org/wiki/Null_object_pattern)


## [Observer](https://es.wikipedia.org/wiki/Observer_(patr%C3%B3n_de_dise%C3%B1o))


## [Publish–subscribe](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)


## [Servant](https://en.wikipedia.org/wiki/Servant_(design_pattern))


## [Specification](https://en.wikipedia.org/wiki/Specification_pattern)


## [State](https://es.wikipedia.org/wiki/State_(patr%C3%B3n_de_dise%C3%B1o))


## [Strategy](https://es.wikipedia.org/wiki/Strategy_(patr%C3%B3n_de_dise%C3%B1o))

## [Template Method](https://es.wikipedia.org/wiki/Patr%C3%B3n_de_m%C3%A9todo_de_la_plantilla)

## [Visitor](https://es.wikipedia.org/wiki/Visitor_(patr%C3%B3n_de_dise%C3%B1o))

# Concurrencia


## [Active object](https://en.wikipedia.org/wiki/Active_object)


## [Balking](https://en.wikipedia.org/wiki/Balking_pattern)

## [Binding properties](https://en.wikipedia.org/wiki/Binding_properties_pattern)

## [Compute kernel](https://en.wikipedia.org/wiki/Compute_kernel)

## [Double-checked locking](https://en.wikipedia.org/wiki/Double-checked_locking)

## [Event-based asynchronous](https://en.wikipedia.org/wiki/Asynchronous_method_invocation)

## [Guarded suspension](https://en.wikipedia.org/wiki/Guarded_suspension)

## [Join](https://en.wikipedia.org/wiki/Join-pattern)


## [Lock](https://es.wikipedia.org/wiki/Cierre_de_exclusi%C3%B3n_mutua)


## [Messaging](https://en.wikipedia.org/wiki/Messaging_pattern)

## [Monitor object](https://es.wikipedia.org/wiki/Monitor_(concurrencia))


## [Reactor](https://es.wikipedia.org/wiki/Reactor_(patr%C3%B3n_de_dise%C3%B1o))


## [Readers–writer lock](https://en.wikipedia.org/wiki/Readers%E2%80%93writer_lock)


## [Scheduling](https://es.wikipedia.org/wiki/Planificador)

## [Thread pool](https://en.wikipedia.org/wiki/Thread_pool)

## [Thread-local storage](https://en.wikipedia.org/wiki/Thread-local_storage)

# Arquitectura

## [Inversión de control](https://es.wikipedia.org/wiki/Inversi%C3%B3n_de_control)

# Otros

## [Circuit Breaker](https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern)

# Bibliografía

* [refactoring.guru - El catálogo de patrones de diseño](### [](https://refactoring.guru/es/design-patterns/catalog))
