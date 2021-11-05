---
title: Ciclo de vida
replace:
  "DRA": '<abbr title="Desarrolo Rápido de Aplicaciones">DRA</abbr>'
---

# Conceptos básicos

**Ciclo de vida**: etapas por las que pasa el software desde que se concibe
un nuevo proyecto hasta que se deja de usar. Fases:

1. Definición: obtención de requisitos
2. Desarrollo: análisis, diseño, codificación, pruebas e implantación
3. Mantenimiento

Las dos primeras comprenden el **ciclo de desarrollo**.

**Metodología de desarrollo**: define los pasos, productos, técnicas y métodos a seguir.

NOTA: Una metodología puede seguir uno o más ciclos de vida.
Al igual, un ciclo de vida no es exclusivo de una metodología, por lo que varias
metodologías pueden seguir el mismo ciclo de vida.

# Modelos de ciclo de vida

## Ciclo de vida en cascada (waterfall)

Fases en cascada (cada fase se completa antes de pasar a la siguiente):

1. Análisis de requisitos
2. Diseño del sistema
3. Diseño del programa
4. Codificación
5. Pruebas
6. Mantenimiento

Puede haber retroalimentación de una fase a otras anteriores, pero a menudo
se aplica como si fuera estrictamente lineal.

* **Ventajas**:
    * Pautas de trabajo claras
    * Facilita establecer hitos, estimación y seguimiento del progreso
    * Proporciona entregales intermedios que en conjunto es el producto final (documentos de análisis y diseño, etc)
* **Inconvenientes**:
    * Establecer todos los requisitos al inicio puede ser poco realista
    * Es muy rígido
    * Los problemas se detectan al final
    * Nada esta hecho hasta que todo esta hecho
    * Un cambio puede suponer un gran coste

## Ciclo de vida en V

Como el de *cascada* pero divide las fases en dos ramas:

* **actividades de desarrollo** (rama descendente): además de hacer lo propio
de esa fase, genera pruebas que en la rama ascendente sirvan para validar
lo definido en esta fase
* **actividades de prueba** (rama ascendente): además de hacer lo propio de
esa fase, valida los resultados usando las pruebas generadas en la rama descendente

![](img/ciclov.png)

Figura: Ciclo de vida en V

* **Ventajas**: las del cascada + que se consideran las pruebas lo antes posible
* **Inconvenientes**: casi tan rígido como el de cascada

## Ciclo de vida <abbr title="Rapid Application Development">RAD</abbr> o DRA

Combina desarrollo iterativo, construcción de prototipos y uso de herramientas CASE.

DRA pretende ser una versión ultrarapida del modelo en cascada con un enfoque
de construcción basado en componentes para obtener sistemas completamente
funcionales en 60-90 días.

**Fases**:

1. Modelado de gestión
2. Modelado de datos
3. Modelado de proceso
4. Gestión de aplicaciones
5. Pruebas y entrega

**Características**:

* Equipos híbridos
* Herramientas especializadas: control de versiones, componentes reutilizables,
herramientas colaborativas, APIs, etc
* Timeboxing: cada fase de desarrollo dura lo mismo
* Prototipos iterativos y evolucionarios
* Reunión JAD

Ventajas e inconvenientes:

* **Ventajas**:
    * Reutilización
    * Paralelismo en el desarrollos
    * Adecuado para tecnología orientada a objetos
* **Inconvenientes**:
    * En proyectos grandes se necesitan muchos recursos humanos
    * Requiere compromiso de clientes y desarrolladores para llegar a tiempo
    * No adecuado para sistemas no descomponibles modularmente o con elevados riesgos técnicos

## [Modelo de construcción de prototipos](https://es.wikipedia.org/wiki/Modelo_de_prototipos)

En cada iteración se van clarificando los requisitos mediante las **fases**:

1. Escuchar al usuario
2. Construir un prototipo
3. El usuario prueba el prototipo

Ventajas e inconvenientes:

* **Ventajas**: Ideal para obtener requisitos cuando no están claros
* **Inconvenientes**:
    * el usuario puede creer que el trabajo ya esta hecho cuando no es así
    * decisiones de baja calidad tomadas para agilizar el desarrollo del
    prototipo pueden persistir en la implementación final

## Modelo incremental

Como el *cascada* pero incremental.

* **Ventajas**:
    * mayor facilidad para determinar los requerimientos para el siguiente nivel
    * los errores se detectan antes
    * mayor flexibilidad ya que el software se construye de forma que facilite
    la incorporación de nuevos requisitos
* **Inconvenientes**:
    * dificultad para determinar que es el núcleo que formará el primer incremento
    * dificultad de la definición de los incrementos
    * la solución de los incrementos anteriores pueden no ser validas para los posteriores

## [Modelo en espiral](https://es.wikipedia.org/wiki/Desarrollo_en_espiral)

Cada ciclo de la espiral representa una fase del desarrollo (no fijas) que
normalmente tienen 4 pasos:

1. Determinar objetivos, alternativas y restricciones
2. Evaluar alternativas, considerando el análisis de riesgos
3. Desarrollo del siguiente nivel del producto
4. Planificación del siguiente ciclo

![](https://upload.wikimedia.org/wikipedia/commons/e/ec/Spiral_model_%28Boehm%2C_1988%29.svg)

Figura: Modelo en espiral

La dimensión radial en la figura refleja los costes acumulativos en los que incurre
el proyecto, y la dimensión angular el progreso del mismo.
Durante cada fase se puede seleccionar el ciclo de desarrollo
que se desee: cascada, V etc.

* **Ventajas**:
    * Permite adaptar el proceso de desarrollo a las necesidades cambiantes del proyecto y al
conocimiento que se va adquiriendo
    * Permite el manejo de prototipos, enlazándolo con el análisis de riesgos
    * Gestiona los riesgos de forma explícita
* **Inconvenientes**:
    * Requiere de una considerable habilidad para la consideración del riesgo
    * La evaluación de riesgos puede disparar el coste
    * Complejidad del modelo
    * Incertidumbre en el número de iteraciones necesarias

## [Proceso unificado](https://es.wikipedia.org/wiki/Proceso_unificado) (RUP)

El modelo de proceso unificado más conocido es el RUP, fuertemente ligado a UML
y ampliamente utilizado en sistemas orientados a objetos.

**Características**:

* Iterativo e Incremental
* Dirigido por los casos de uso
* Centrado en la arquitectura
* Enfocado en los riesgos

**Fases**:

* Inicio
* Elaboración
* Construcción
* Transición

En cada fase se tiene un *ciclo en cascada* cuyas partes tienen más o menos
peso según en que fase estemos, y puede haber más de una iteración.

![](https://upload.wikimedia.org/wikipedia/commons/f/f5/Fases_y_Flujos_de_trabajo_en_PUR.svg)

Figura: Fases y ciclos del Proceso unificado

## Otros

* **Codificación directa** (code and fix): consiste en no aplicar ningún modelo
de ciclo de vida, es decir, en empezar a codificar a lo loco, sin documentación
ni nada.
* **Modelo evolutivo**: tiene en cuenta la naturaleza evolutiva del software
(se puede combinar con modelos incrementales)
* **Agile Inception**: más que una metodología en si es un conjunto de dinámicas
(Elevator Pitch, caja de producto, etc) para prepararse para implementar una metodología ágil
* [**Modelo concurrente**](https://es.wikipedia.org/wiki/Ingenier%C3%ADa_de_software#Modelo_de_desarrollo_concurrente):
No ordena las actividades de ingeniería de software a una secuencia de sucesos, si no que define una red de actividades, todas las actividades de la red existen simultáneamente con otras
* [**Desarrollo adaptativo de software**](https://es.wikipedia.org/wiki/Desarrollo_adaptativo_de_software) (ASD):
derivado de DRA que sustituye el *modelo en cascada* por una serie repetitiva de ciclos de especulación, colaboración y aprendizaje.
Esta enfocado a la misión, a basado en características, iterativo, planeado de acuerdo al tiempo, guiado por riesgos y tolerante al cambio
* [**Modelo por etapas**](https://es.wikipedia.org/wiki/Desarrollo_por_etapas) (Stage-Wise):
similar al *Modelo de prototipos* pero más enfocado a casos donde no son conocidas
en detalle al inicio del proyecto y por tanto se van desarrollando simultáneamente
con las diferentes versiones del código
* **Modelos basados en transformaciones**: Convierten automáticamente una especificación
formal de un producto software en un programa que satisfaga las especificaciones, utilizando herramientas 4G.
* Ciclo de vida **Sashimi**: variación del ciclo de vida en cascada puro, en el
cual las diferentes etapas pueden ser solapadas, permitiendo aumentar la
eficiencia mediante la retroalimentación entre las etapas
* Ciclo de vida **pinball**: la pelota del Pinball representaría el software a desarrollar,
que pasa iterativamente por fases que ocurren casi en cualquier momento, saltando de una a otra
* **Síntesis automática**:
    * Los Requisitos se expresan en una especificación formal
detallada expresada en notación matemática
    * Los procesos (diseño, implementación y pruebas) se
reemplazan por un proceso basado en transformaciones
donde la especificación formal se refina.
    * La implementación y la documentación es automática.
    * El mantenimiento se realiza *por sustitución*, no mediante *parches*.
* Ciclo de vida **remolino**: Proceso multicíclico no lineal con forma de remolino.
Considera las siguientes dimensiones de iteración:
    * Amplitud: Tamaño de desarrollo
    * Profundidad: Nivel de abstracción o detalle
    * Madurez: Grado de compleción, corrección y elegancia
    * Alternativas: Diferentes soluciones a un problema
    * Alcance: Objetivos del Sistema (requisitos cambiantes)
* Ciclo de vida **agrupamiento**: Opera sobre conjuntos de clases relacionadas con un
objetivo común (el *agrupamiento*) y se divide en varios subciclos, todos ellos con:
    * Especificación
    * Diseño
    * Realización
    * Validación
    * Generalización

# Metodologías ágiles

Surgen del [manifiesto ágil](https://es.wikipedia.org/wiki/Manifiesto_%C3%A1gil) en contraposición a las metodologías tradicionales.
Sus **4 valores** son:

* Individuos e interacciones sobre procesos y herramientas
* Software funcionando sobre documentación extensiva
* Colaboración con el cliente sobre negociación contractual
* Respuesta ante el cambio sobre seguir un plan

y sus **12 principios**:

* Nuestra principal prioridad es satisfacer al cliente a través de la entrega temprana y continua de software con valor
* Aceptamos que los requisitos cambien, incluso en etapas tardías del desarrollo. Los procesos ágiles aprovechan el cambio para proporcionar ventaja competitiva al cliente
* Entregamos software funcional frecuentemente, entre dos semanas y dos meses, con preferencia al período de tiempo más corto posible
* Los responsables del negocio y los desarrolladores trabajamos juntos de forma cotidiana durante todo el proyecto
* Los proyectos se desarrollan en torno a individuos motivados. Hay que darles el entorno y el apoyo que necesitan, y confiarles la ejecución del trabajo
* El método más eficiente y efectivo de comunicar información al equipo de desarrollo y entre sus miembros es la conversación cara a cara
* El software funcionando es la medida principal de progreso
* Los procesos ágiles promueven el desarrollo sostenido. Los promotores, desarrolladores y usuarios debemos mantener un ritmo constante de forma indefinida
* La atención continua a la excelencia técnica y al buen diseño mejora la agilidad
* La simplicidad, o el arte de maximizar la cantidad de trabajo no realizado, es esencial
* Las mejores arquitecturas, requisitos y diseños emergen de equipos auto-organizados
* A intervalos regulares, el equipo reflexiona sobre cómo ser más efectivo para, a continuación, ajustar y perfeccionar su comportamiento en consecuencia

## Historias de usuario

En las metodologías ágiles se suele usar las [historias de usuario](https://es.wikipedia.org/wiki/Historias_de_usuario)
para describir los requisitos (normalmente funcionales).

La historia de usuario debe responder a tres preguntas, ¿Quién se beneficia?, ¿qué se quiere? y ¿cuál es el beneficio?,
por lo que se suele usar la formula `Como (rol) quiero (algo) para poder (beneficio)`.

Sus características forman el acrónimo **INVEST** (Independent, Negociable, Valuable, Estimable, Small, Testable). Las historias demasiado largas (*epic*) han de ser divididas en otras
más pequeñas.

Las historias de usuario deben desarrollarse hasta cumplir con los **criterios de aceptación**,
que definen su calidad bajo el [método SMART](https://en.wikipedia.org/wiki/SMART_criteria)
(Specific, Measurable, Achievable, Relevant, Time-bound).

Estos criterios de aceptación se describen mediante una de estas dos técnicas:

* Técnica de comportamiento: `DADO <condiciones> CUANDO <evento> ENTONCES <resultado>`
* Técnica de escenarios: se define *el trayecto feliz* y los *corner case* restringiéndose
a describir la forma en que el usuario procede y el sistema responde.

| Historias de usuario                         | Casos de uso |
|-|-|
| Más **cortas**, fáciles de estimar           | Más **largos**, difíciles de estimar |
| Se pueden ir **refinando y completando**     | Debería estar **completa desde el principio** |
| **Desechables** tras su implementación       | Perviven en el tiempo |
| No están completas sin las **pruebas de validación** | |
| Los escenarios alternativos se expresan<br/>como condiciones en las pruebas de validación | Los escenarios alternativos se expresan<br/>en la sección de flujos alternativos |
| Pueden especificar requisitos no funcionales | siempre se refieren a requisitos funcionales |

Tabla: Historias de usuario vs. Casos de uso

## SCRUM

Proceso iterativo e incremental, que gira en torno a los conceptos:

* **sprint**: periodo de duración fija (de 1 a 4 semanas) en el que el equipo crea un incremento
del software potencialmente entregable (utilizable)
* **product backlog**: conjunto de...
    1. principalmente requisitos (historias de usuario) de alto nivel priorizados según el ROI
    2. pero SCRUM solo habla de *items* en genérico, es decir, puede haber otro tipo de trabajos
* **sprint backlog**: se compone de:
    1. subconjunto de *product backlog* que será implementado en el *sprint*
    2. otras tareas necesarias (deuda técnica, calidad, etc)
* **sprint goal**: objetivo más importante del *sprint*
* **Burndown chart**: gráfica mide la cantidad de requisitos en el Backlog del
proyecto pendientes al comienzo de cada Sprint. Será una recta descendente
salvo cuando se añadan nuevos requisitos.

Scrum identifica los siguientes **roles** principales:

* **Product Owner**: representa la voz del cliente y sus tareas son:
    * generar y mantener actualizado el **product backlog**
    * proponer los items del *product backlog* que deberían pasar **sprint backlog** de la siguiente iteración
    * maximizar el ROI del equipo de desarrollo
* **Scrum Master**: ejerce de facilitador para el equipo de desarrollo y sus tareas son:
    * proteger al equipo de desarrollo de injerencias externas
    * asegurarse de que Scrum es correctamente implementado
    * gestionar riesgos y problemas que el equipo vaya encontrando
* **Development Team** (desarrolladores, Scrum Team): equipo de 5 a 9 personas
autogestionado y multidiscilinar que desarrolla el producto, cuyas tareas son:
    * convertir el backlog a un producto entregale
    * asegurar la calidad del producto
    * hacer demostraciones del trabajo realizado
    * aplicar mejora continua

A estos roles se les llama **cerdos** porque son los que están comprometidos
con el proyecto, mientras que todos los demás (expertos de negocio, stakeholders, etc)
se les llama **gallinas** porque solo están implicados, es decir, son personas
o entidades que tienen algún interés en el producto y/o que puede ofrecer feedback
valioso.

El flujo de trabajo es el siguiente:

1. **Sprint 0**: sirve para identificar roles y compartir entre todos la misma visión
y objetivos del proyecto
    * se realizan los preparativos organizativos y tecnológicas
    * el **Product Owner** elabora el **product backlog**
    * establecer las definiciones:
        * **ready**: cuando una historia de usuario esta los suficientemente definida para entrar en el **sprint backlog**
        * **done**: cuando una historia de usuario ha sido completada
2. **Sprint Planning Meeting** (<2h para sprint de una semana):
    1. El **Product Owner** explica al **Development Team** el **product backlog**
    y propone ítems para el **Sprint Backlog**
    2. el **Development Team** elige y/o descompone en tareas los ítems que pasan
    al **Sprint Backlog** del siguiente sprint
    3. entre **Product Owner** y **Development Team** se acuerda cual es el **Sprint Goal**
    4. el **Scrum Master** ejerce de facilitador
3. **Sprint**: mientras dura:
    1. no se debería modificar el **Sprint Backlog**
    2. el **Development Team** realiza el **Daily Scrum** de entre 5 y 15 minutos para que:
        * los miembros del equipo se mantengan actualizados unos a otros sobre el trabajo
        * se detecten problemas
        * según algunos autores, se explica:
            * qué tareas se han hecho desde la última reunión
            * qué tareas se van a hacer hasta la próxima
            * que impedimentos se tiene o se prevé encontrar
        * según otros el objetivo se ciñe a analizar el estado del Sprint Goal
        * el **Scrum Master** puede asistir para recoger los problemas detectados
        * el **Product Owner** si asiste solo lo hara de oyente
4. Final del Sprint: consiste en dos reuniones (1h por sprint de una semana)
en las que participa todo el equipo
    1. **Sprint Review**: se presentan los trabajos completados y su duración no debería ser superior a 4 horas para un Sprint de 1 mes
    2. **Sprint Retrospective**: se comparten impresiones sobre el sprint
    recién superado con fin de realizar una mejora continua de la implementación de Scrum
5. Se vuelve a empezar por el paso 2

En algunos casos se añade la **reunión de refinamiento del Product Backlog** previa
al *Sprint Planning Meeting* para su preparación.

## Otros

* **Kanban**: Tablero con tres columnas (To-Do, Doing y Done) en el que se van colocando tareas
según la fase en la que estén. Permite detectar cuellos de botella.
* [**Extreme Programming**](https://es.wikipedia.org/wiki/Programaci%C3%B3n_extrema) (XP):
    * valores: simplicidad, comunicación, retroalimentación, coraje o valentía, respeto.
    * programación por parejas
    * pruebas unitarias conjuntas
    * refactorización de código
    * propiedad del código compartida y rotación interna del equipo
* **FDD​**: Desarrollo basado en funcionalidades
* **TDD**: Desarrollo guiado por pruebas, los requisitos se traducen a pruebas y luego se hace el código que pase la prueba
* **BDD**: Desarrollo guiado por comportamiento. Como TDD pero además de pruebas
que verifican el código también hay pruebas que definen el comportamiento de la
aplicación
* **DSDM**: Método de desarrollo de sistemas dinámicos. Extensión de RAD
* [**Crystal**](https://en.wikiversity.org/wiki/Crystal_Methods): Familia de
metodologías que incluye entre otras Crystal Clear, Crystal Yellow o Crystal Orange
* [**LEAN**](https://es.wikipedia.org/wiki/Lean_software_development)

## Agile a gran escala

Para usar agile en proyectos grandes con varios equipos trabajando a la vez
en subproyectos existen algunas alternativas como:

* [**SAFe** (Scaled agile framework)](https://en.wikipedia.org/wiki/Scaled_agile_framework):​ Estructurado en cuatro niveles (equipo, programa, gran
solución y portfolio). A nivel de equipo se aplican principios Scrum, XP, Kanban y Lean.
A otros niveles existen conceptos como​ Program Increment o ​Agile Release Train​ para
coordinar múltiples equipos que trabajan sobre una misma solución.
* [**Scrum de scrums**](https://en.wikipedia.org/wiki/Scrum_(software_development)#Scrum_of_scrums)
* [**LeSS**​](https://en.wikipedia.org/wiki/Scrum_(software_development)#Large-scale_Scrum)
 (Large-Scale Scrum)

# Bibliografía

* PreparaTic27 - Pack1/037
* PreparaTic27 - Pack1/085
* PreparaTic27 - Pack1/087
* [miniprogramacion.blogspot.com - Modelos basados en Transformaciones](http://miniprogramacion.blogspot.com/2014/12/modelos-basados-en-transformaciones.html)
* [proyectosagiles.org - Beneficios de Scrum](https://proyectosagiles.org/beneficios-de-scrum/)
* [andaira.es - Scrum Roles - Una breve introducción](https://andaira.es/Formacion/Scrum/Scrum-Roles/)
* [youtube.com - Cristian Henao - #1 Que son las metodologias tradicionales en el desarrollo de software](https://www.youtube.com/watch?v=i8CPD1dW88k)
* [youtube.com - Cristian Henao - #2 Que son las metodologias tradicionales en el desarrollo de software](https://www.youtube.com/watch?v=fHKsufzM7qQ)
* [youtube.com - Cristian Henao - #3 SCRUM en 6 minutos](https://www.youtube.com/watch?v=HhC75IonpOU)
* [youtube.com - Ágil Es - Por Cris Rúa - Lo mejor de Scrum y Kanban](https://www.youtube.com/watch?v=Kxz0_rDmRho)
* [javiergarzas.com - Sprint Planning, claves y evitando malas interpretaciones](https://www.javiergarzas.com/2018/01/sprint-planning.html)
* [javiergarzas.com - Los 7 errores más comunes de la Daily Scrum, ¿cómo evitarlos?](https://www.paradigmadigital.com/techbiz/los-7-errores-mas-comunes-la-daily-scrum-evitarlos/)
* [javiergarzas.com - Los ciclos de vida software más raros y que hay vida más allá del cascada y el ágil y el iterativo](https://www.javiergarzas.com/2015/02/los-ciclos-de-vida-software-raros.html)
* [ctr.unican.es - Procesos de Ingeniería del Software](https://www.ctr.unican.es/asignaturas/is1/is1-t02-trans.pdf)
