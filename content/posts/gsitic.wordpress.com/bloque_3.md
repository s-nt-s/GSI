---
Status: published
author: gsitic.wordpress.com
bloque: 3
pdf_code: B3
ebook-meta: -s gsitic.wordpress.com -i 3
lang: es-ES
meta:
  DC.creator: gsitic.wordpress.com
pandoc: --toc-depth 2 --parse-raw --epub-chapter-level 2
porcentaje: 63
source: https://gsitic.wordpress.com/bloque-iii/
summary: Contenido propiedad de [gsitic.wordpress.com](https://gsitic.wordpress.com/bloque-iii/).
title: B3 Desarrollo de sistemas
total: 19
txt-cover: B3 Desarrollo de sistemas
---

# Concepto del ciclo de vida de los sistemas y fases. Modelos de ciclo de vida.

<article><h2>Introducción</h2>
<p>En este tema se va a dar una visión de lo que se llama ciclo de vida del software, así como distintos modelos de representación del mismo.</p>
<p>¿Para qué un ciclo de vida? En un departamento de sistemas de información de una empresa es necesario establecer lo que llamamos un marca de referencia común que pueda ser empleado por todas las personas que participan en el desarrollo de un proyecto informático: directivos, consultores externos e internos, jefes de proyecto, analistas, programadores, usuarios, etc.</p>
<p>En este marco de referencia deben estar claramente definidos los procesos, actividades y tareas a desarrollar.</p>
<p>Veamos primeramente dos definiciones publicadas por dos organismos internacionales:</p>
<ul><li>Norma IEEE 1074: Se entiende por ciclo de vida del software una aproximación lógica a la adquisición, el suministro, el desarrollo, la explotación y el mantenimiento software.</li>
<li>Norma ISO 12207-1: Se entiende por modelo de ciclo de vida un marco de referencia que contiene los procesos, las actividades y las tareas involucradas en el desarrollo, la explotación y el mantenimiento de un producto de software, abarcando la vida del sistema desde la definición de requisitos hasta la finalización de su uso.</li>
</ul><h3>La Evolución del Software</h3>
<p>El concepto de ciclo de vida se utilizó para modelar el proceso de ingeniería del software que, a su vez, apareció como solución a la llamada “crisis del software”.</p>
<p>Veamos un poco de historia. El desarrollo del software ha ido en paralelo con la evolución de los sistemas informáticos, los cuales han ido mejorando notablemente debido al aumento de la potencia del hardware, a la reducción de su tamaño y la disminución de su coste económico.</p>
<p>Siguiendo a Presmann podemos distinguir las siguientes etapas en la evolución del software:</p>
<ul><li>1ª Etapa: Primeros años de la informática (1950-1965). El hardware sufrió numerosos cambios. Se desarrollaba software sin planificación y sin metodologías sistemáticas. En casi todos los sistemas se utilizaba programación en “batch”. La mayoría del software era desarrollado y utilizado por la misma persona.</li>
<li>2ª Etapa: (1965-1975). Aparición de la multiprogramación y de los sistemas multiusuarios. Como consecuencia de la interactividad de los sistemas aparecen nuevos tipos de aplicaciones. Surgen, asimismo, los sistemas de tiempo real. También los primeros gestores de BD.</li>
<li>3ª Etapa: (1975-1985). Aparecen los sistemas distribuidos, redes de área local LAN y de área global WAN. Hay una fuerte presión sobre los desarrolladores de software. Los ordenadores personales impulsan el crecimiento de muchas compañías de software.</li>
<li>4ª Etapa: (1985- ). Tecnologías de cuarta generación. Tecnologías orientadas a objetos.</li>
</ul><h3>Características especiales del Software</h3>
<p>Existen características propias del software que lo diferencian de otros productos:</p>
<ul><li>El software no se fabrica en un sentido clásico, sino que se desarrolla: Si bien existen similitudes con la fabricación del hardware, se trata de actividades fundamentalmente diferentes. Tanto en una como en otra la buena calidad se adquiere mediante un buen diseño pero la fabricación del hardware es muy diferente de la del software y puede introducir problemas de calidad que no existen o son fácilmente corregibles en el software. Ambas actividades requieren la construcción de un produce pero con métodos muy diferentes. Los costes del desarrollo del software están en la ingeniería por lo que no se pueden gestionar como si fueran clásicos proyectos de fabricación.</li>
<li>El software no se “estropea”: El hardware se deteriora con el paso del tiempo y con el uso. Los errores no detectados del software provocarán fallos al principio de su vida. Sin embargo, una vez corregidos deberían desaparecer los fallos y no aparecer nuevos. No obstante la realidad suele ser diferente. El software sufre a lo largo de su vida modificaciones y al introducir estos cambios suelen producirse nuevos fallos que, a su vez, tienen que ser corregidos y así sucesivamente.</li>
<li>La mayor parte del software se construye a medida, en lugar de ensamblar componentes como hace la industria: En la fabricación del hardware, la reutilización de componentes es una parte natural del proceso de ingeniería. En el mundo del software es algo que sólo ha comenzado a lograrse recientemente.</li>
</ul><h3>La “Crisis del Software”</h3>
<p>Desde que se empezó a desarrollar software a gran escala empezaron a ser comunes una serie de problemas:</p>
<ul><li>La planificación resultaba ser muy imprecisa. Los plazos de entrega eran superados en la mayoría de los casos.</li>
<li>El coste final de los proyectos era frecuentemente mucho mayor que el previsto.</li>
<li>La productividad era muy baja.</li>
<li>La calidad el producto entregado era, asimismo, muy baja.</li>
<li>El cliente solía quedar insatisfecho del producto.</li>
<li>El software era difícil de mantener.</li>
</ul><p>Hay que añadir que el conjunto de problemas encontrados en el desarrollo del software no se limitan al software que “no funciona correctamente”. La llamada crisis abarca los problemas asociados a cómo desarrollar software, como mantener el volumen cada vez mayor de software existente y cómo poder mantenernos al corriente de la demanda creciente de software.</p>
<h3>Ingeniería del Software</h3>
<p>La ingeniería del Software surge de la necesidad de sistematizar el desarrollo del software afectado por la llamada “crisis del software”, aplicando principios de ingeniería para poder obtener software de calidad.</p>
<p>¿Qué es software de calidad? Si asumimos que el software cumple con la funcionalidad requerida, para que sea de calidad deberá tener las siguientes características:</p>
<ul><li>El software debe ser mantenible. Deberá estar escrito y documentado de forma tal que las modificaciones se puedan realizar con el menor coste posible. Esto es fundamental ya que la mayor parte del coste asociado del software se produce después de su puesta en funcionamiento.</li>
<li>El software debe ser fiable. Es decir, debe comportarse como esperan los usuarios y no debe fallar más de lo permitido por la especificación.</li>
<li>El software debe ser eficiente.</li>
<li>Debe ofrecer una interfaz de usuario apropiada.</li>
</ul><h2>Concepto del Ciclo de Vida y Fases</h2>
<p>Podemos definir ciclo de vida de un sistema de información como el conjunto de etapas por las que atraviesa el sistema desde su concepción, hasta su retirada de servicio pasando por su desarrollo y explotación.</p>
<p>A veces también se habla de “ciclo de desarrollo”, que es un subconjunto del anterior que empieza en el análisis y finaliza con la entrega del sistema al usuario.</p>
<p>Existen diferentes modelos de ciclo de vida o sea distintas pautas a seguir en el desarrollo de los sistemas de información. Más adelante estudiaremos dos, el llamado modelo clásico o en cascada y el modelo en espiral.</p>
<p>Tres son los objetivos básicos que cualquier modelo de ciclo de vida debe cubrir:</p>
<ul><li>Definir las actividades a realizar y su orden.</li>
<li>Asegurar la consistencia con el resto de los sistemas de información de la organización.</li>
<li>Proporcionar puntos de control para la gestión del proyecto (presupuesto y calendario).</li>
</ul><h3>Procesos del Ciclo de Vida Software</h3>
<p>Según la Norma ISO 12207-1, las actividades a realizar durante el ciclo de vida del software se agrupan en cinco procesos principales, ocho procesos de soporte y cuatro procesos de la organización, así como un proceso especial que permite adaptar el ciclo de vida a cada proyecto en concreto.</p>
<p>A destacar que la norma no recomienda ningún modelo concreto de ciclo de vida, ni de gestión del software, ni detalla cómo realizar ninguna de las actividades.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/proceso_ciclo_vida_software.png?w=825"/></p>
<h3>Procesos Principales</h3>
<p>Son aquellos que resultan útiles a las personas que inician o realizan el desarrollo, la explotación o el mantenimiento del software a lo largo del ciclo de vida. Estas personas son los compradores, los proveedores, el personal de desarrollo, los usuarios y el personal encargado del mantenimiento del software.</p>
<ul><li><strong>Proceso de adquisición</strong>: Contiene las actividades y tareas que el comprador, el cliente o el usuario realizan para adquirir un sistema o un producto software. Aquí están incluidos la preparación y publicación de una solicitud de ofertas, la selección del proveedor del software y la correspondiente gestión de los procesos desde la adquisición hasta la aceptación del producto.</li>
<li><strong>Proceso de suministro</strong>: Contiene las actividades y tareas que el suministrador o proveedor realiza. Comienzan con la preparación de una propuesta para responder a una petición de oferta de un comprador o con la firma de un contrato con el comprador para proporcionarle un producto software. Trata, asimismo de la identificación de los procedimientos y de los recursos necesarios para gestionar y garantizar el éxito del proyecto, incluyendo el desarrollo de los planes del proyecto y la ejecución de dichos planes hasta la entrega del producto software al comprador.</li>
<li><strong>Proceso de desarrollo</strong>: Contiene las actividades de análisis de requisitos, diseño, codificación, integración, pruebas e instalación y aceptación. Vamos a resumir someramente estas actividades:
<ul><li><em>Análisis de requisitos del sistema</em>: Aquí son especificados todos los requisitos del Sistema de Información, funciones y capacidades que debe cumplir, requisitos de seguridad, interfaces, de mantenimiento, etc.</li>
<li><em>Diseño de la arquitectura del sistema</em>: Se identifican los principales componentes hardware y software.</li>
<li><em>Análisis de los requisitos de software</em>: Se establecen dichos requisitos, incluyendo el nivel de calidad que debe cumplir el sistema.</li>
<li><em>Diseño de la arquitectura del software</em>: El diseñador debe transformar el análisis anterior en una arquitectura en la que se puedan identificar sus componentes principales.</li>
<li><em>Diseño detallado del software</em>: Aquí se realiza un diseño detallado de cada componente software, de las BD y manuales de usuario.</li>
<li><em>Codificación y pruebas unitarias</em>: Se desarrollan y se documentan los componentes del punto anterior. Finalmente se realizan las pruebas unitarias de cada uno de ellos para asegurarse de que cumplen los requisitos exigidos.</li>
<li><em>Pruebas de integración</em>: Se integran los componentes del software realizando las correspondientes pruebas.</li>
<li><em>Prueba del software</em>: Las pruebas se planifican y diseñan de forma sistemática para poder detectar el máximo número y variedad de defectos con el mínimo consumo de tiempo y esfuerzo.</li>
<li><em>Integración del sistema</em>: Aquí se realizan las pruebas conjuntas de los elementos hardware y software.</li>
<li><em>Implantación del software desarrollado en el entorno de explotación final</em>. Cuando se sustituya a un software ya existente, puede ser recomendable un período de tiempo en el que convivan los dos sistemas.</li>
<li><em>Proceso de aceptación del software</em>.</li>
</ul></li>
<li><strong>Proceso de explotación</strong>: Comprende la propia explotación del software y el soporte operativo a los usuarios del sistema.</li>
<li><strong>Proceso de mantenimiento</strong>: Aparece cuando, tarde o temprano, el software requiere modificaciones, bien por errores, necesidades de mejora, etc.</li>
</ul><h3>Procesos de Soporte</h3>
<p>Sirven de apoyo al resto de procesos y pueden aplicarse en cualquier punto del ciclo de vida.</p>
<ul><li><strong>Proceso de documentación</strong>: Comprende todas las actividades que permiten desarrollar, distribuir y mantener la documentación necesaria para todas las personas involucradas: consultores, jefes de proyecto, analistas, programadores, usuarios, etc.</li>
<li><strong>Proceso de gestión de la configuración</strong>: Controla las modificaciones y las versiones de los elementos de configuración del software del sistema.</li>
<li><strong>Proceso de aseguramiento de la calidad</strong>: Comprueba que los procesos y los productos software del ciclo de vida cumplen con los requisitos especificados y se ajustan a los plantes establecidos.</li>
<li><strong>Proceso de verificación</strong>: El objetivo es demostrar la consistencia, completitud y corrección del software entre las fases del ciclo de desarrollo de un proyecto (por ejemplo, si el código es coherente con el diseño). Este proceso puede ser responsabilidad de una empresa de servicios y, en este caso se conoce como proceso de verificación independiente.</li>
<li><strong>Proceso de validación</strong>: El objetivo es determinar la corrección del producto final respecto a las necesidades del usuario. Al igual que el anterior, este proceso puede ser ejecutado por una organización de servicios, denominándose proceso de validación independiente.</li>
<li><strong>Proceso de revisión conjunta</strong>: Para evaluar el estado del software y sus productos en una determinada actividad del ciclo de vida o una fase de un proyecto. Las revisiones conjuntas se celebran tanto a nivel de gestión como a nivel técnico del proyecto a lo largo de todo su ciclo de vida. Un mecanismo habitual de revisión son las reuniones y la responsabilidad es generalmente compartida entre un grupo de personas pertenecientes a la organización.</li>
<li><strong>Proceso de auditoría</strong>: Permite determinar, en los hitos preestablecidos, si se han cumplido los requisitos, los planes y, en suma, el contrato.</li>
<li><strong>Proceso de resolución de problemas</strong>: Permite analizar y solucionar los problemas, sean éstos diferencias con los requisitos o con el contrato. Aporta un medio oportuno y documentado para asegurar que los problemas detectados son analizados y solucionados.</li>
</ul><h3>Procesos de la Organización</h3>
<p>Son los utilizados por una organización para llevar a cabo funciones como la gestión, formación del personal o procesos de mejora continua.</p>
<ul><li><strong>Proceso de gestión</strong>: Contiene las actividades y las tareas genéricas que puede emplear una organización que tenga que gestionar sus procesos. Incluye actividades como la planificación, el seguimiento y control, la revisión y evaluación.</li>
<li><strong>Proceso de infraestructura</strong>: Establece la infraestructura necesaria para cualquier otro proceso: hardware, software, herramientas, técnicas, etc para el desarrollo, explotación y mantenimiento.</li>
<li><strong>Proceso de mejora</strong>: Para mejorar los procesos del ciclo de vida del software.</li>
<li><strong>Proceso de formación</strong>: Para mantener al personal con la adecuada formación, lo que conlleva el desarrollo del material de formación, así como la implementación del plan de formación de la organización.</li>
</ul><h3>Proceso de Adaptación</h3>
<p>Sirve para realizar la adaptación básica de la norma ISO 12207-1 respecto a los proyectos software. Como es sabido, las variaciones en las políticas y procedimientos de la organización, los métodos y estrategias de adquisición, el tamaño y complejidad de los proyectos, los requisitos del sistema y los métodos de desarrollo, entre otros, influencian la forma de adquirir, desarrollar, explotar o mantener un sistema.</p>
<p>Dado que los procesos se aplican durante el ciclo de vida del software, y además se utilizan de diferentes formas por las diferentes organizaciones y con distintos puntos de vista y objetivos, es preciso comprender los procesos, las organizaciones y sus relaciones bajo diferentes puntos de vista:</p>
<ul><li>Contrato: El comprador y el proveedor negocian y firman el contrato, empleando los procesos de adquisición y suministro.</li>
<li>Gestión o dirección: El comprador, el proveedor, el desarrollador, el operador y el personal de mantenimiento gestionan sus respectivos procesos en el proyecto software.</li>
<li>Explotación: El operador proporciona el servicio de explotación del software a los usuarios.</li>
<li>Ingeniería: El desarrollador o el personal de mantenimiento llevan a cabo sus respectivas tareas de ingeniería para producir o modificar los productos de software.</li>
<li>Soporte: Los grupos de soporte (el de gestión de la configuración, el de aseguramiento de la calidad, el de auditoría, etc) proporcionan servicios de apoyo a otros grupos en el cumplimiento de tareas únicas y específicas.</li>
</ul><h2>Modelo en Cascada</h2>
<p>Este modelo nació durante los años setenta y supuso un gran avance con respecto a los modelos que habían sido utilizados hasta entonces. Este modelo se compone de una serie de fases que se suceden secuencialmente, generándose en cada una de las fases resultados que constituyen la entrada de la fase siguiente. Estas fases pueden diferir, pero suelen comprender:</p>
<ul><li>Planificación</li>
<li>Especificación de Requisitos</li>
<li>Diseño</li>
<li>Codificación</li>
<li>Pruebas e Integración</li>
<li>Implantación y Aceptación</li>
<li>Mantenimiento</li>
</ul><p>La fase de especificación de requisitos es conocida también como análisis funcional, la fase de diseño se denomina análisis orgánico y la fase de codificación se llama programación.</p>
<p>El número de fases es irrelevante, lo que caracteriza verdaderamente a este modelo es la secuencialidad entre las fases y la necesidad de completar cada una de ellas para pasar a la siguiente. El sistema está terminado cuando se han realizado todas las fases.</p>
<p>El modelo en cascada ayudó a eliminar muchos de los problemas que se planteaban antes de su utilización, además ha sido la base para la normalización y la adopción de estándares. A medida que ha sido utilizado se han detectado en él debilidades e inconsistencias que se han intentado corregir con diversas modificaciones y extensiones al modelo inicial.</p>
<h3>Fases del Modelo en Cascada</h3>
<p>Vamos a analizar cada una de las posibles fases:</p>
<p><strong>Planificación</strong></p>
<p>De esta fase depende en gran medida un desarrollo efectivo en lo referente a costos y plazos de entrega.</p>
<p>Hay que fijar los siguientes puntos:</p>
<ul><li>Ámbito del trabajo a realizar.</li>
<li>Recursos necesarios.</li>
<li>Tareas a realizar.</li>
<li>Referencias a considerar.</li>
<li>Coste aproximado del desarrollo del proyecto.</li>
<li>Formación del equipo de desarrollo.</li>
<li>Ordenación y calendario de las actividades.</li>
</ul><p>La planificación se llevará a cabo con un nivel de detalle adecuado a la complejidad, tamaño y grado de estructuración del proyecto. Para proyectos de gran tamaño la planificación es imprescindible y en ocasiones sirve para determinar el modelo de ciclo de vida a seguir en el proyecto.</p>
<p>La estimación de recursos, costes y calendario se determina a partir de la experiencia acumulada por parte del jefe de proyecto y de la información histórica de otros proyectos realizados dentro o fuera de la organización. Esta es una de las fases más difíciles de realizar, pero en la actualidad se cuenta con técnicas y herramientas automatizadas para el control y la gestión del proceso de producción de los sistemas de información.</p>
<p><strong>Especificación de Requisitos – Análisis Funcional</strong></p>
<p>Una vez terminada la planificación del proyecto, la fase de análisis de requisitos es la primera del proceso de desarrollo del sistema. En esta fase es preciso analizar, entender y documentar el problema que el usuario trata de resolver con el sistema de información o aplicación a desarrollar.</p>
<p>Es necesario especificar en detalle las funciones, objetivos y restricciones del sistema propuesto para que el usuario y los desarrolladores puedan tomar estas especificaciones como punto de partida para acometer el resto del sistema.</p>
<p>El proceso de recogida de requisitos es la tarea más delicada de esta fase en la cual el analista del sistema debe llegar a comprender el dominio de la información y adaptar las necesidades del usuario a unas especificaciones formales listas para poder ser utilizadas por los desarrolladores.</p>
<p>Se trata de definir “qué” debe hacer el sistema identificando la información a procesar, las funciones a realizar, el rendimiento deseado del sistema, las interfaces con otros sistemas o las restricciones de diseño entre otros aspectos. Es fundamental en esta fase la participación e implicación del usuario del sistema.</p>
<p>Para el análisis de las necesidades a cubrir y los requisitos a satisfacer por el sistema, su priorización, comprobar que el sistema se ajusta a las necesidades del usuario y plantear alternativas viables no solo a nivel técnico sino desde el punto de vista de costes y riesgos, hay que utilizar todas aquellas técnicas o elementos a nuestro alcance como, por ejemplo, realización de entrevistas con los usuarios, utilización de información referente al sistema actual si es que existe, utilización de técnicas de diagramación para facilitar la comprensión del sistema, técnicas de análisis coste-beneficio, técnicas de prototipado rápido o técnicas de análisis estructurado.</p>
<p>Las tareas asociadas a esta fase y los resultados que se obtienen serán independientes del entorno tecnológico del sistema de información.</p>
<p><strong>Diseño – Análisis Orgánico</strong></p>
<p>A partir, como siempre, de las especificaciones de la fase anterior y una vez elegida la mejor alternativa, se debe comenzar a crear la solución al problema descrito atendiendo a aspectos de interfaz de usuario, estructura del sistema y de decisiones sobre la implantación posterior.</p>
<p>Esta fase aborda el “cómo”, es decir, deberá diseñar las estructuras de datos, la arquitectura del sistema, los detalles que permitan la codificación posterior y las pruebas a realizar.</p>
<p>Para el diseño del sistema habrá que trasladar las especificación de requisitos a un conjunto de representaciones ya sean gráficas, tabulares o basadas en lenguajes que constituirán la estructura de datos lógica y física, la arquitectura y los procedimientos.</p>
<p>Otras cuestiones que se abordan en esta fase son los requisitos de comunicaciones, algoritmos, seguridad y control. Al igual que en las fases anteriores la de diseño conlleva una documentación en la que se recogen sus resultados. En esta fase hay que tener en cuenta el entorno del sistema referente a hardware y software de base.</p>
<p><strong>Codificación – Programación</strong></p>
<p>En esta fase se traducen las especificaciones de diseño a un lenguaje de programación capaz de ser interpretado y ejecutado por el ordenador. Existen lenguajes de distintos grados de complejidad o eficacia y la utilización de uno u otro determinará la forma de trabajo de esta fase. En todo caso, el lenguaje vendrá determinado por el entorno lógico del sistema.</p>
<p>El programador deberá velar por la claridad de su estilo para facilitar cualquier interpretación posterior de los programas. Asimismo se respetarán los estándares de la organización en cuanto a nomenclatura y formato. Es imprescindible que los programas incorporen comentarios escritos que ayuden a su comprensión y que se acompañen de la documentación externa necesaria que describa su objeto, los algoritmos que incluye, sus entradas y salidas y cualquier otro elemento relevante.</p>
<p>Muchas son las técnicas aplicables a la programación, como, por ejemplo, las técnicas estructuradas ampliamente extendidas desde hace años. Más reciente es la generación automática de código, que a partir de especificaciones formales algunas herramientas CASE (Computed Aided Software Engineering) facilitan con un mayor o menor grado de optimización, según los casos, código en los lenguajes de programación más utilizados.</p>
<p><strong>Pruebas e Integración</strong></p>
<p>Una vez que los programas han sido desarrollados, es preciso llevar a cabo las pruebas necesarias para asegurar la corrección de la lógica interna de los mismos y comprobar que cubren las funcionalidades previstas.</p>
<p>La integración de las distintas partes que componen la aplicación o el sistema es precisa en proyectos complejos o de grandes dimensiones que hayan sido descompuestos por razones de facilidad de gestión y control. La integración debe solucionar posibles problemas de interacción y garantizar el buen funcionamiento del conjunto.</p>
<p>En esta fase se debe proporcionar la documentación que ilustre los procedimientos de usuario en la utilización y funcionamiento del sistema y si fuera preciso se organiza un plan de formación para usuarios con el material didáctico necesario.</p>
<p>Como en las fases anteriores existen técnicas y herramientas para la realización de las tareas de esta fase.</p>
<p><strong>Implantación y Aceptación</strong></p>
<p>En esta fase se trata de conseguir la aceptación final del sistema por parte de los usuarios del mismo y llevar a cabo las actividades necesarias para su puesta en producción.</p>
<p>Para ello se tomarán como punto de partida los componentes del sistema probados de forma unitaria e integrada en la fase anterior y se probarán una vez más esta vez con el fin de verificar que cumplen los requisitos de usuario y que el sistema es capaz de manipular los volúmenes de información requeridos en los tiempos y velocidades deseados, que las interfaces con otros sistemas funcionan, etc.</p>
<p>En estas pruebas participará el usuario que si está conforme deberá aceptar formalmente el sistema.</p>
<p><strong>Mantenimiento</strong></p>
<p>Esta fase comienza una vez que el sistema es entregado al usuario y continúa mientras permanece activa su vida útil. El mantenimiento puede venir propiciado por:</p>
<ul><li>Errores no detectados previamente.</li>
<li>Modificaciones, mejoras o ampliaciones solicitadas por los usuarios.</li>
<li>Adaptaciones requeridas por la evolución del entorno tecnológico o cambios normativos.</li>
</ul><p>En el primer caso se habla de mantenimiento “correctivo” puesto que debe solventar defectos en el sistema. El segundo caso se denomina mantenimiento “perfectivo” puesto que se produce una modificación de los requisitos iniciales aumentando las funcionalidades. El último de los casos se conoce por mantenimiento “adaptativo”, con el paso del tiempo es muy posible que la situación inicial respecto de la cual se concibió el sistema cambie.</p>
<p>Para la realización del mantenimiento se siguen los mismos pasos que para la realización del sistema, pero en el contexto de un sistema existente. Es fundamental que las variaciones producidas en esta fase queden reflejadas en todas las fases anteriores y no simplemente en la fase de codificación. De lo contrario esta práctica conduciría a sistemas intratables al cabo de varias modificaciones sin actualización de la documentación afectada.</p>
<p>La fase de mantenimiento lleva asociada su propia documentación reflejando los cambios, su objeto, la fecha, el autor y cualquier dato que pueda ayudar al control de dichos cambios o a procesos de mantenimiento posteriores.</p>
<h3>La Documentación</h3>
<p>El modelo de ciclo de vida en cascada está regido por la documentación, es decir, la decisión del paso de una fase a la siguiente se toma en función de si la documentación asociada a esa fase está completa o no.</p>
<p>El concepto de documentación debe entenderse en sentido amplio como todos los productos resultantes de las tareas realizadas en cada fase ya sean informes, programas, juegos de pruebas, etc, se podría definir la documentación como aquello que se construye y ha de mantenerse durante la vida del sistema.</p>
<p>A pesar de posibles críticas a esta orientación se recogen a continuación las características que deben incluir los documentos asociados a cada fase. No hay que olvidar que el objetivo final es construir con éxito un sistema de información y que la documentación nos ayudará a conseguirlo pero no es un fin en sí misma.</p>
<p>En la fase de planificación se elaborará documentación que tendrá el carácter de marco básico de referencia del proyecto y deberá incluir:</p>
<ul><li>Descripción y alcance de las tareas que se van a llevar a cabo.</li>
<li>Identificación de los principales métodos, instrumentos y procedimientos de trabajo que se utilizarán.</li>
<li>Procedimientos de seguimiento y control de los trabajos y mecanismos de revisión y aprobación de los mismos.</li>
<li>Calendario de tareas y su ordenación temporal.</li>
<li>Asignación de recursos.</li>
<li>Organización de las personas que intervienen en el proyecto.</li>
</ul><p>En la fase de especificación de requisitos será necesaria la existencia de documentación en el que se recojan las necesidades del usuario respecto al sistema: funcionalidades, rendimientos, limitaciones y restricciones, los interfaces de usuario. La descripción de los requisitos de los usuario debe ser descrita de forma que se pueda verificar su cumplimiento mediante inspecciones o pruebas. Este documento reflejará el punto de vista del analista del sistema respecto de las especificaciones que el usuario ha realizado, si la comprensión por parte del analista no es adecuada el usuario debe rechazar el documento. Este documento es crucial porque sobre sus presupuestos se construirá el sistema de información, por tanto se detallará la naturaleza de la información, su contenido y su estructura lógica. La representación de las operaciones y procesos, sus entradas y salidas y cualquier característica relevante a nivel funcional referente al entorno tecnológico del sistema.</p>
<p>En la documentación asociada a la fase de diseño se profundizará más, llegando a describir los componentes del sistema: estructuras de datos, unidades de tratamiento o módulos de procesamiento e interfaces al máximo nivel de detalle. Se concretará la descripción técnica y cuestiones relacionadas con la implantación del sistema: arquitectura general, fichero y/o BD, pantallas, informes o comunicaciones con otros sistemas.</p>
<p>La fase de codificación debe proporcionar como documentación, el código fuente de todos los módulos incluidas las funciones auxiliares, el código para la creación de estructuras de datos e interfaces externas y cualquier tipo de módulos o rutinas relacionadas con el sistema. Además del código de cada módulo en el soporte físico y formato de representación previamente establecido por el usuario, se acompañará el listado del código con sus comentarios internos y comentarios externos sobre la definición de las estructuras de datos, de los algoritmos, sobre el manejo de excepciones y la gestión de errores.</p>
<p>La fase de pruebas e integración llevará documentación que describa el plan de pruebas a nivel unitario e integrado y los resultados de dichas pruebas. La fase de implantación y aceptación vendrá documentada con el plan de pruebas del sistema a nivel global y sus resultados. Por último si se realizan modificaciones en la fase de mantenimiento deberán reflejarse en la documentación correspondiente que haya podido ser afectada.</p>
<p>La documentación asociada al sistema no estaría completa sin un manual de usuario que contenga la descripción funcional de todos los procedimientos para facilitar la operativa del sistema al usuario. Recogerá los procedimientos de instalación, administración y gestión de la configuración, operaciones especiales, funcionamiento, ayudas incorporadas, tratamiento de errores, comandos y sentencias de control. A veces también puede incluir una guía de referencia rápida con el resumen de todas estas instrucciones.</p>
<h3>Crítica del Modelo</h3>
<p>Las principales críticas al modelo se centran en sus características básicas, es decir, secuencialidad y utilización de los resultados de una fase para acometer la siguiente de modo que el sistema sólo se puede validar cuando está terminado.</p>
<p>Los proyectos reales raramente siguen el flujo secuencial que propone el modelo. Siempre ocurren interacciones y en las últimas fases sobre todo se pueden realizar en paralelo algunas áreas como por ejemplo: codificación y pruebas. Una aplicación del modelo en sentido estricto obligaría a la “congelación” de los requisitos de los usuarios, supuesto este completamente alejado de la realidad. El modelo no contempla la posibilidad de realimentación entre fases.</p>
<p>El modelo en su formulación pura no prevé revisiones o validaciones intermedias por parte del usuario, así los resultados de los trabajos sólo se ven al final de una serie de tareas y fases de tal forma que si se ha producido un error en las primeras fases éste sólo se detectará al final y su corrección tendrá un costo muy elevado, puesto que será preciso rehacer todo el trabajo desde el principio. El modelo no dispone de resultados parciales que permitan validar si el sistema cumple con los requisitos desde las primeras fases, dándose el caso de sistemas perfectamente formalizados y documentados que no cumplen los requisitos del usuario.</p>
<h3>Extensiones al Modelo en Cascada</h3>
<p>Actualmente, después de la experiencia obtenida con la aplicación del modelo en cascada y gracias a avances tecnológicos como por ejemplo lenguajes de cuarta generación o herramientas CASE existen modelos de ciclo de vida alternativos al modelo en cascada. En la práctica se llegan a realizar incluso modelos mixtos. En este punto no se tratarán estos casos, sino que se citarán algunas innovaciones aplicables al modelo en cascada que permiten mejorar algunas de las deficiencias del modelo y aumentar su eficacia:</p>
<ul><li>Utilización de herramientas CASE y otras facilidades. Al hablar de las fases del ciclo de vida se mencionaban las técnicas estructuradas, en principio dichas técnicas no se utilizaban en el modelo en cascada, sin embargo, hoy en día no se plantea la realización de un sistema “artesanalmente”.</li>
<li>Introducción de una fase intermedia entre especificación de requisitos y el diseño denominado diseño rápido que sirva para validar las especificaciones por parte del usuario, estableciéndose un proceso iterativo de modificación de la especificación hasta que el usuario esté satisfecho con la misma.</li>
<li>Técnicas de diseño en grupo. Es deseable que el usuario pueda participar al máximo en la definición de los requisitos puesto que se evitarán errores y confusiones ya en las primeras etapas.</li>
<li>Utilizar técnicas de análisis de riesgos y de coste-beneficio para pasar a la fase siguiente y abandonar planteamientos rígidos de paso a la fase siguiente cuando se ha completado la documentación.</li>
<li>Dotar de autonomía al jefe de proyecto para que de acuerdo con su experiencia y las características del proyecto decida comenzar una fase sin haber terminado la anterior al 100%, pero que le permite, por ejemplo, realizar una maqueta para la validación por parte del usuario.</li>
<li>Codificación y pruebas de los módulos de más alto nivel en primer lugar, seguida de la de los módulos más detallados o de más bajo nivel. Esta aproximación puede propiciar el diálogo entre el analista y el usuario en fases posteriores a la especificación de requisitos estableciendo así un proceso de realimentación entre las fases de Implantación y Especificación de requisitos.</li>
<li>Realización de fases en paralelo como codificación y pruebas. La codificación se puede así ver beneficiada por los resultados de las pruebas y detección de errores.</li>
<li>Reutilización de código ya probado. A veces con pequeñas modificaciones se pueden llegar a utilizar programas existentes.</li>
<li>Revisiones de código. Se trata de inspecciones para localizar lo más pronto posible dentro del ciclo todos los errores de diseño y codificación.</li>
</ul><h2>Modelo en Espiral del Ciclo de Vida</h2>
<h3>Introducción</h3>
<p>A partir de la experiencia de la aplicación del modelo en cascada se desarrolló el modelo en espiral del ciclo de vida del software y se implementó en algunos grandes proyectos.</p>
<p>En este modelo subyace el concepto de que cada ciclo implica una progresión que aplica la misma secuencia de pasos para cada parte del producto y para cada uno de sus niveles de elaboración, desde la concepción global de la operación hasta la codificación de cada programa individual.</p>
<p>El modelo en espiral se ilustra en la siguiente figura. En ella podemos apreciar:</p>
<ul><li><em>La dimensión radial:</em> representa el coste acumulativo en el que se ha incurrido en las etapas realizadas hasta el momento actual.</li>
<li><em>La dimensión angular</em>: representa el progreso hecho en completar cada ciclo de la espiral.</li>
</ul><p><img src="https://gsitic.files.wordpress.com/2018/01/modelo_espiral.png?w=825"/></p>
<p>Describamos a continuación como sería un típico ciclo de espiral. Considerando cada cuadrante de izquierda a derecha en el sentido de las agujas del reloj.</p>
<p><strong>CUADRANTE 1</strong>: Cada ciclo en espiral empieza con la indentificación de:</p>
<ul><li>Los objetivos de la parte del producto que va a ser elaborada (rendimiento, funcionalidad, disponibilidad para acomodarse a nuevos cambios, etc.)</li>
<li>Las alternativas para implementar esta parte del producto (diseño A, diseño B, compra del software ya desarrollado, reutilización de un software ya existente, etc).</li>
<li>Las restricciones impuestas: costes, calendario de realización, interfaces, etc.</li>
</ul><p><strong>CUADRANTE 2</strong>: Aquí se evalúan las opciones relativas a los objetivos y las restricciones.</p>
<p>Este proceso, con frecuencia, identificará áreas de incertidumbre que son fuentes significativas de riesgo. Esto llevaría implícito la formulación de una estrategia económicamente efectiva para resolver las fuentes de riesgo: prototipado, simulación, benchmark, modelos analíticos o combinaciones de éstas y otras técnicas de resolución de riesgos.</p>
<p>Si los riesgos de rendimiento o los riegos del interfase de usuario tienen mucha más importancia que los riesgos de desarrollo de programas o los riesgos de interfase de control interno, entonces el paso siguiente podría ser un paso de desarrollo evolutivo: un esfuerzo mínimo para especificar la naturaleza global del producto, un plan para el siguiente nivel de prototipado y el desarrollo de un prototipo más detallado para continuar la resolución de las mayores fuentes de riesgo.</p>
<p>Si este prototipo es operacionalmente útil y suficientemente robusto para servir como una base de bajo riesgo para el evolución del producto, entonces, los subsiguientes pasos dirigidos por el riesgo (risk-drive) podrían ser una serie de prototipos cada vez más evolucionados, moviéndonos hacia la derecha de la figura. Así, consideraciones de riesgo, pueden llevar a la realización del proyecto utilizando sólo un subconjunto de todos los pasos potenciales en el modelo.</p>
<p><strong>CUADRANTES 3 y 4</strong>: Si los esfuerzos previos de prototipado han resuelto ya todos los riesgos de rendimiento o los riesgos de interface de usuario y dominan los riesgos de desarrollo en programas o los riesgos de control de interface, el paso siguiente sería el desarrollo según el modelo en cascada. Cada nivel de especificación del software en la figura, entonces, seguido por un paso de validación y planificación del siguiente ciclo.</p>
<p>Esta implementación, dirigida por el riesgo, de un subconjunto del modelo en espiral, permite al modelo acomodarse a cualquier mezcla de estrategias de desarrollo de software: orientado por las especificaciones, orientado por la simulación, orientado por transformaciones automáticas o cualquier otro enfoque de desarrollo.</p>
<p>En tales casos, la estrategia mixta apropiada se escoge, considerando, la relación relativa de magnitudes de los riesgos y la efectividad relativa de las distintas alternativas en la resolución de estos riesgos. De forma similar, consideraciones de gestión de riesgo, permiten determinar la cantidad de tiempo y esfuerzo que debe dedicarse a otras actividades del proyecto tales como: planificación, gestión de la configuración, garantía de la calidad, verificación formal, y prueba.</p>
<p>Un aspecto importante del modelo espiral, como en otros muchos modelos, es que cada ciclo se completa por una revisión que involucra a las personas u organizaciones principales relacionadas con el proyecto. Esta revisión cubre todas las actividades desarrolladas durante el ciclo previo, incluyendo los planes para el próximo ciclo y los recursos que se requieren para llevarlos a cabo.</p>
<p>El principal objetivo de la revisión es asegurar que todas las partes implicadas están de acuerdo con el camino a seguir en la siguiente fase.</p>
<p>Los planes para las fases sucesivas pueden incluir también el desarrollo del producto por medio de incrementos sucesivos o la división en componentes que pueden ser desarrollados por distintas personas u organizaciones. En este último caso, aparecen unos ciclos espirales paralelos (uno para cada componente) añadiendo una tercera dimensión al concepto presentado en la figura.</p>
<p>Además, la etapa de revisión y compromiso puede extenderse, desde una simple revisión informal del diseño de un programa a una revisión de los requerimientos principales implicando, en este caso, a clientes, usuarios, desarrolladores y organizaciones de mantenimiento.</p>
<h3>Ejemplo de Aplicación del Modelo en Espiral</h3>
<p>El modelo en espiral se aplicó en un proyecto muy complejo: la definición y desarrollo del Sistema de Productividad de Software (TRW-SPS) un entorno integrado de ingeniería de software de la empresa TRW. El objetivo era mejorar la productividad de las tareas de desarrollo de software realizadas por la empresa.</p>
<p>En primer lugar se realizó un “ciclo 0” de la espiral para determinar la viabilidad de conseguir un incremento significativo de productividad en el desarrollo software.</p>
<p><strong>Ciclo 0: Estudio de viabilidad</strong></p>
<p>Participaron cinco personal, a tiempo parcial, durante un período de dos a tres meses. Durante este ciclo los objetivos y las restricciones se consideraron a un nivel muy alto, expresándoles en términos cualitativos (“mejora significativa”, “coste razonable”, etc).</p>
<p>Se consideraron alternativas en cuatro áreas: gestión de los proyectos, gestión del personal, tecnología e instalaciones.</p>
<p>Como áreas de riesgo, se consideró la posibilidad de que la compañía realizase una inversión importante para encontrarse con:</p>
<ul><li>Mejoras de productividad escasamente significativas.</li>
<li>Mejoras potenciales incompatibles con aspectos de la cultura de la empresa.</li>
</ul><p>El análisis de riesgos condujo a la conclusión de que se podrían obtener significativas mejoras en la productividad, a un coste razonable, por medio de un conjunto integrado de iniciativas.</p>
<p><strong>Ciclo 1: Concepción de la operación</strong></p>
<p>En este ciclo se invirtieron más recursos (12 meses hombre en lugar de los 2 meses hombre del Ciclo 0); se consideraron objetivos más específicos (conseguir el doble de productividad en la producción de software en 5 años a un coste máximo de 10.000$ por persona); surgieron nuevas restricciones como la preferencia por la utilización de productos desarrollados por la propia empresa, en especial la red local de TRW.</p>
<p>Para las áreas de riesgo también se fue más específico que en el Ciclo 0 (“comprobación que la red TRW LAN ofrecía una relación precio/rendimiento dentro de la restricción de 10.0000$ por persona”). Para la resolución de riesgos se realizaron tareas más extensivas, tales como la realización de benchmarks y análisis de un prototipo de la TRW LAN.</p>
<p>La fase de compromisos no se limitó a la aceptación del plan. Se acordó la aplicación del entorno de desarrollo de software producido a un proyecto piloto que implicaba a más de 100 personas. Se decidió la formación de un comité de seguimiento para garantizar la coordinación de las distintas actividades y para evitar que el prototipo de entorno de desarrollo no se optimizase, excesivamente, en función de las características del proyecto en el que se iba a probar. Se recomendó que no solamente se desarrollase el prototipo, sino que también se elaborase una especificación de requerimientos y un diseño siguiendo una orientación orientada al riesgo.</p>
<p><strong>Ciclo 2: Especificación de los requerimientos de alto nivel</strong></p>
<p>Se tomaron las decisiones al comienzo del ciclo al observarse que muchos de los requisitos del sistema dependían de la decisión sobre el SO a utilizar y de si el sistema a elaborar iba a ser un sistema orientado al host o totalmente portable. Se decidió escoger UNIX y un sistema orientado a un host UNIX.</p>
<p><strong>Otros ciclos posteriores</strong></p>
<p>Las etapas posteriores se realizaron según las características generales de la implantación del modelo en este caso:</p>
<ul><li>Desarrollo de especificaciones, postergando la elaboración de los elementos de software de bajo riesgo hasta que no se hubieran estabilizado los elementos de software de alto riesgo.</li>
<li>Incorpora la construcción de prototipos como técnica de reducción de riesgos en cualquiera de las etapas del proyecto.</li>
<li>Permite la “vuelta atrás” a etapas anteriores cuando se encuentran alternativas más atractivas o se identifican nuevas fuentes de riesgo que requieren solución.</li>
</ul><h3>Evaluación del Modelo</h3>
<p><strong>Ventajas</strong></p>
<p>La ventaja principal del modelo en espiral es que su rango de opciones acomoda las buenas características de los otros modelos de desarrollo de software, y su procedimiento dirigido por el riesgo, evita muchas de sus dificultades.</p>
<p>En situaciones apropiadas, el modelo en espiral es equivalente a uno de los modelos de proceso existentes.</p>
<p>Si un proyecto tiene un riesgo bajo en áreas tales como el establecimiento de una interfaz de usuario no adecuada o en el cumplimiento de requerimientos rigurosos de ejecución y si, por el contrario, tiene un alto riesgo en la predicción y control del presupuesto y del calendario de elaboración, entonces estas consideraciones conducen el modelo en espiral a uno equivalente al modelo en cascada.</p>
<p>El modelo en espiral tiene otras ventajas adicionales:</p>
<ul><li>Concentra su atención en opciones que consideran la reutilización de software existente. Los pasos implicados en la identificación y evaluación de alternativas potencian estas opciones.</li>
<li>Permite preparar la evolución del ciclo de vida, crecimiento y cambios del producto software.</li>
<li>Proporciona un mecanismo de incorporación de objetivos de calidad en el desarrollo de producto software. Este mecanismo se deriva del énfasis puesto en la identificación de todos los objetivos y restricciones durante cada una de las vueltas de la espiral.</li>
<li>Es especialmente adecuado para la temprana eliminación de errores y alternativas poco atractivas.</li>
<li>No implica procedimientos separados para el desarrollo y la mejora del software.</li>
<li>Proporciona un marco viable para integrar los desarrollos de sistemas software-hardware. El centrar la atención en la gestión del riesgo y en la eliminación de alternativas no atractivas lo antes posible y con el menor coste es, igualmente, aplicable al software y al hardware.</li>
<li>Se adapta al diseño y programación orientada a objetos y posiblemente con estos métodos es cuando permite obtener mejores resultados: el modelo en espiral potencia la utilización de desarrollos incrementales, y cuando sea necesario, la reelaboración de partes ya desarrolladas. La abstracción, encapsulación, modularidad y jerarquización, elementos fundamentales de los métodos orientados a objeto, facilitan los desarrollos incrementales y hacen menos traumáticas las reelaboraciones.</li>
</ul><p><strong>Dificultades</strong></p>
<p><strong>Adaptar su aplicabilidad al software contratado</strong></p>
<p>El modelo en espiral actualmente trabaja bien en desarrollos de software internos pero necesita un trabajo adicional para adaptarlo al mundo de los contratos de adquisición del software.</p>
<p>Los desarrollos internos de software tienen bastante flexibilidad y libertad para acomodarse a confirmaciones etapa por etapa; para diferir confirmaciones a determinadas opciones; para establecer miniespirales con las que resolver caminos críticos; para ajustar niveles de esfuerzo, o para acomodar prácticas tales como el prototipado, o el desarrollo evolutivo.</p>
<p>En el mundo de la adquisición de software es muy difícil conseguir estos grados de flexibilidad y libertad sin perder responsabilidad y control y es muy difícil definir contratos que no especifiquen por adelantado los productos a obtener.</p>
<p>Recientemente, se ha progresado en el establecimiento de mecanismos de contratación más flexibles pero todavía se necesitan mejoras para conseguir que los compradores se sientan completamente cómodos utilizándolos.</p>
<p><strong>Dependencia de la experiencia en la evaluación de riesgos</strong></p>
<p>El modelo en espiral da un papel relevante a la habilidad de los desarrolladores de software para identificar y gestionar las fuentes de riesgo del proyecto. Un buen ejemplo de esto es la especificación dirigida por el riesgo en el modelo en espiral. En ella se debe llegar a un alto nivel de detalle en los elementos de alto riesgo dejando, los de bajo riesgo, para una elaboración en etapas posteriores.</p>
<p>Otro problema es que la especificación será, en exceso, dependiente de las personas. Por ejemplo, un diseño producido por un experto puede ser implantado por no expertos; en este caso, el experto que no necesita mucha documentación, debe producir suficiente documentación adicional para que los no expertos no se extravíen.</p>
<p>Con una aproximación convencional, dirigida por la documentación, el requerimiento de llevar todos los aspectos de la especificación a un nivel uniforme de detalle elimina algunos problemas potenciales y permite una adecuada revisión de algunos aspectos por revisores inexpertos. No obstante, esto produce pérdidas de tiempo a los expertos que deben buscar los aspectos críticos en medio de un gran volumen de detalles no críticos.</p>
<h3>El Plan de Gestión de Riesgo</h3>
<p>Incluso si una organización no está lista para adoptar el procedimiento completo en espiral, una característica técnica del mismo que puede ser fácilmente adaptada a cualquier modelo de ciclo de vida proporciona muchos de los beneficios de dicho procedimiento. Se trata del Plan de Gestión del Riesgo.</p>
<p>Este plan, básicamente, asegura que en cada proyecto se haga una identificación temprana de sus factores de riesgo más altos; desarrolla una estrategia para resolver los factores de riesgo; identifica y establece una agenda para resolver nuevos factores de riesgo a medida que afloran y, por último, muestra los progresos respecto al plan en revisiones mensuales.</p>
<p>El plan de gestión de riesgo y las técnicas para gestión de riesgo de Software facilitan adaptar concepto del modelo en espiral a los procedimientos de adquisición y desarrollo de software más asentados. Se pueden sacar las siguientes cuatro conclusiones:</p>
<ul><li>El modelo en espiral, por su naturaleza de estar dirigido por el riesgo, es más adaptable a un amplio rango de situaciones que los procedimientos dirigidos por la documentación, tales como el modelo en cascada o los procedimientos dirigidos por el código, tales como el modelo de desarrollo evolutivo. Es particularmente aplicable a sistemas de software muy grandes y complejos.</li>
<li>El modelo en espiral ha tenido éxito en su mayor aplicación realizada hasta ahora: el desarrollo del TRW-SPS. Proporciona la flexibilidad necesaria para acomodar un rango de alternativas técnicas y objetivos de usuario muy dinámico.</li>
<li>El modelo en espiral no está, todavía, tan elaborado como los modelos más establecidos. Por esta razón, el modelo en espiral puede ser aplicado por personal experto, pero necesita elaboración posterior en áreas como contratación, especificaciones, puntos de control, revisiones, calendarios e identificación de áreas de riesgo para ser completamente aplicable en todas las situaciones.</li>
<li>Algunas implementaciones parciales del modelo en espiral como el Plan de Gestión del Riesgo, son compatibles con la mayoría de los modelos de proceso actuales y son muy útiles para superar las mayores fuentes de riesgo de proyectos.</li>
</ul><p>Tabla de los 10 factores de riesgo del software más importantes:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/factores_riesgo.png?w=825"/></p>
<p>Tabla del Plan de Gestión del Riesgo del Software:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/pgrs.png?w=825"/></p>
<h2 class="bio">Bibliografía</h2>
<ul class="bio"><li><a href="https://es.scribd.com/document/100553892/TICB2-Ciclo-de-Vida" rel="noopener" target="_blank">Scribd (Ricardo Costanzi)</a></li>
</ul> </article>

# Gestión del proceso de desarrollo: objetivos, actores y actividades. Técnicas y prácticas de gestión de proyectos.

<article><h2>Introducción a la Gestión del Proceso de Desarrollo</h2>
<p>Los fundamentos de gestión consisten en determinar el tamaño del producto (incluyendo funcionalidad, complejidad y otras características del producto), asignando los recursos apropiados a un producto de ese tamaño, creando un plan para aplicar esos recursos y luego controlando y dirigiendo los recursos para impedir que el proyecto se desvíe. En algunos casos los altos cargos delegan explícitamente estas tareas de gestión a los responsables técnicos, y en otros casos simplemente las dejan vacantes, ocupándose de ellas un responsable o desarrollado motivado.</p>
<h3>Definiciones</h3>
<ul><li><strong>Proceso</strong>. Conjunto de actividades con un objetivo, que transforman un conjunto de entradas en un conjunto de salidas, agregando valor.</li>
<li><strong>Proceso de Software</strong>. Proceso que transforma Requerimientos de Procesamiento de Información en Elementos de Software (componentes computacionales y documentos) que satisfacen los requerimientos de procesamiento de información, ofreciendo servicios a una organización.</li>
<li><strong>Proceso de desarrollo de software</strong>. Proceso cuyo objetivo es generar un nuevo sistema informático que satisfaga un conjunto de requerimientos iniciales de procesamiento de información en una organización.</li>
<li><strong>Procesos de Administración de Proyectos</strong>. Procesos orientados a organizar y guiar al equipo de desarrollo para cumplir los compromisos negociados con el cliente (fechas de entrega y costes).</li>
<li><strong>Procesos de Ingeniería de Software</strong>. Procesos orientados a obtener componentes de software (código y documentos) entregables al cliente, sin errores y con el menor esfuerzo posible.</li>
</ul><h3>Características de la Gestión del Proceso de Desarrollo</h3>
<p>Las características principales de la gestión del proceso de desarrollo son las siguientes:</p>
<ul><li>El producto a desarrollar es intangible.</li>
<li>El producto tiene su propia flexibilidad.</li>
<li>La ingeniería de software no es reconocida como una disciplina de la Ingeniería con el mismo estatus de la mecánica, eléctrica, matemáticas, etc.</li>
<li>El proceso de desarrollo de software no está estandarizado.</li>
</ul><p>De estas características se deduce la importancia de la propia gestión, ya que la Ingeniería de software es una actividad económica importante, que está sujeta a restricciones económicas. No hay que olvidar que los proyectos bien gestionados a veces fallan. Los proyectos mal gestionados siempre fallan.</p>
<h3>Causas de Fallos en los Proyectos</h3>
<p>Dentro de las principales causas por las que puede fallar un proyecto, se encuentra el hecho de que los componentes del proyecto no respetan o no conocen bien las herramientas y las técnicas del análisis y diseño de sistemas, además de esto puede haber una mala gestión y dirección del proyecto.</p>
<p>Además existen una serie de factores que pueden hacer que el sistema sea mal evaluado:</p>
<ul><li>Requerimientos Incompletos.</li>
<li>Usuarios no Involucrados.
<ul><li>Carencia de Recursos.</li>
</ul></li>
<li>Expectativas Irreales.</li>
<li>Falta de soporte ejecutivo.</li>
<li>Cambios de Requerimientos.</li>
<li>Falta de planificación.</li>
<li>Obsoleto antes de ser completado.</li>
<li>Carencia de supervisión por parte de la gerencia de TI.</li>
<li>Desconocimiento de la tecnología.</li>
<li>No resuelve problemas de negocio.</li>
<li>Requerimientos planificados de manera irreal.</li>
<li>Carencia de entrenamiento en Administración de Programas.</li>
<li>Mala Estimación.</li>
</ul><p>Aunque estos factores pueden influir de manera muy trascendente en la mala realización de un proyecto, generalmente están acompañados de otro tipo de problemas. Pero, ¿cuáles de estos errores de gestión de proyectos ocasionan que no se cumplan los requisitos, que se sobrepase los tiempos de entrega o se aumenten repetidas veces los costes?</p>
<p>La respuesta a esta pregunta puede ser hallada en dos fuentes principalmente, deficiencias en las herramientas y las técnicas de análisis del diseño de sistemas o la mala gestión de los proyectos.</p>
<p>En el caso de las necesidades no satisfechas o no identificadas, el error puede aparecer debido a que se omiten datos durante el desarrollo del proyecto, es por esto que es muy importante no saltar ninguna etapa del ciclo de vida del desarrollo de sistemas.</p>
<p>Otra causa de insatisfacción de necesidades es la mala definición de las expectativas de un proyecto en sus orígenes, ya que si no están bien definidos los requerimientos máximos y mínimos que el proyecto debe satisfacer desde el comienzo, los desarrolladores verán afectados su trabajo por el <em>síndrome de las necesidades que crecen</em> el cual les dejará hacer cambios en el proyecto en cualquier momento sin detenerse a pensar si esos cambios serán buenos para el proyecto como un todo, por supuesto todas estas modificaciones acarrearan alteraciones en los costes y en los tiempos de entrega.</p>
<p>El coste de un proyecto puede aumentar durante el desarrollo de este debido a varias causas:</p>
<ul><li>Para comenzar un proyecto generalmente se exige un estudio de viabilidad en el cual no se incluyen datos completamente precisos de la cantidad de recursos que cada tarea consumirá, y es en base a este estudio que se hacen estimaciones de los recursos totales que el proyecto va a necesitar.</li>
<li>El uso de criterios de estimación poco eficientes por parte de los analistas.</li>
<li>El aumento en los tiempos de entrega debido a que los directores del proyecto en ocasiones no gestionan bien los tiempos de entrega de cada tarea del proyecto y cuando tienen un retraso no son capaces de alterar los plazos de entrega finales creyendo que podrán recuperar el tiempo perdido, pero no siempre es posible acelerar otras tareas para ahorrar tiempo en la entrega final.</li>
</ul><p>Para evitar todos estos problemas, se debe tener al mando del proyecto un director que conozca las herramientas de diseño y análisis de sistemas y tenga una buena formación en las funciones de dirección.</p>
<h2>Objetivos de la Gestión del Proceso Desarrollo</h2>
<p>Los objetivos de la gestión son al final objetivos de calidad, es el primer paso de cualquier metodología de mejora, estos se pueden definir respondiendo la pregunta…</p>
<p>¿Cuáles son los puntos que queremos mejorar en la gestión?</p>
<p>Seguramente habrá muchos puntos que son susceptibles de mejora, sin embargo hay que considerar solo unos pocos y sobre todo aquellos que sean los que más nos interesa modificar.</p>
<p>Al establecer los objetivos debemos procurar definirlos de manera clara, concreta y deben ser cuantificables.</p>
<p>Básicamente estos podrían ser:</p>
<ul><li>Reducir la diferencia entre la fecha real y la fecha acordada.</li>
<li>Reducir la diferencia entre el esfuerzo real y el esfuerzo acordado.</li>
<li>Reducir el número de errores funcionales y no funcionales de los sistemas en entornos de producción (tendencia a cero errores).</li>
<li>Aumentar la productividad de los equipos de desarrollo (Relación productos-esfuerzo global de proyectos).</li>
</ul><p>En mejora de procesos hay tres cosas que esperamos que ocurran:</p>
<p>En la figura se muestra como en principio se establecen objetivos de fecha y costo que no se cumplen. La mayor parte del trabajo no está dentro del objetivo (a la izquierda de la gráfica). En la parte de abajo lo que ocurre es que el objetivo que se establece se acerca más a la realidad del desempeño del equipo de trabajo que desarrolla las tareas, volviendo más certera la estimación.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/modelos_de_calidad.png?w=825"/></p>
<p>En la siguiente figura lo que esperamos que se transforme es el control. Aquí se muestra como (en la parte de arriba) una parte importante de los resultados, a pesar de estar centrados en los objetivos, se sale de los objetivos. Disminuir (abajo) esta curva significa que nuestro proceso está bajo control.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/modelos_de_calidad_2.png?w=825"/></p>
<p>En la siguiente figura, con más certeza en la información para fijar objetivos y con más control en nuestros procesos, podemos mejorar la efectividad con objetivos más agresivos y con altas posibilidades de cumplirlos.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/modelos_de_calidad_efectividad.png?w=825"/></p>
<h3>El Modelo CMM (Capacity Maturity Model)</h3>
<p>Existen diferentes modelos de calidad entre los cuales se encuentran: CMM, SPICE, Bootstrap y Thrillium, los cuales se concentran en evaluar la capacidad de los procesos de software y la madurez de las organizaciones de software. Estos modelos constituyen un marco de referencia que permite calificar a las organizaciones de desarrollo de software.</p>
<p>Está comprobado que ISO9000 no es adecuado para evaluar capacidad de procesos de software, es por eso que el mismo ISO creó el proyecto SPICE.</p>
<p>El modelo CMM ubica a las organizaciones en uno de cinco niveles de madurez según se muestra en la figura:</p>
<ul><li>En el nivel 1 la organización es reactiva, los administradores se dedican a resolver crisis inmediatas y los tiempos calendario y los costes son excedidos básicamente porque no están basados en estimaciones reales. Cuando hay metas calendario agresivas, regularmente la funcionalidad y calidad del producto son comprometidos a fin de cumplir con las fechas. No existe un proceso definido y cuando un proyecto sale bien, no hay manera de reproducir su forma de trabajo en proyectos subsecuentes.</li>
<li>En el nivel 2 ya hay un proceso definido, se tienen identificadas las entradas y salidas de cada etapa y se establecen controles en las entradas y salidas de cada etapa.</li>
<li>En el nivel 3 se define el cómo de cada etapa, habiendo probado en la VIDA REAL las técnicas y descubierto la mejor forma de aplicarlas. Se identifican los controles internos necesarios para cada etapa.</li>
<li>En el nivel 4 se aplican los controles internos de cada etapa y se llevan a cabo mediciones y estimaciones en base a información estadística.</li>
<li>Finalmente en el nivel 5 se lleva a cabo un proceso de mejora continua REAL en el que se hace reingeniería de procesos.</li>
</ul><p><img src="https://gsitic.files.wordpress.com/2018/04/modelo_cmm.png?w=825"/></p>
<h2>Actividades de Gestión</h2>
<p>Son las actividades que permiten asegurar que el software se lleva a cabo a tiempo y de acuerdo a la planificación. Así como de acuerdo a los requerimientos del software:</p>
<ul><li>Planificación de las actividades del equipo de desarrollo dentro del proyecto.</li>
<li>Obtener los recursos (tanto físicos como humanos) necesarios para la ejecución del proyecto.</li>
<li>Organizar funciones y responsabilidades de las personas dentro del equipo de desarrollo.</li>
<li>Revisar cumplimento de planes y compromisos.</li>
<li>Supervisar/auditar la ejecución de las actividades dentro del desarrollo y revisar las características necesarias de los productos que se generan dentro del proyecto.</li>
<li>Administrar/controlar los cambios en los productos generados dentro del proceso de desarrollo.</li>
<li>Medir y registrar el desempeño durante la ejecución del proyecto.</li>
<li>Anticipar posibles problemas durante la ejecución del proyecto y prevenirlos.</li>
<li>Evaluar y retroalimentar el desempeño de los miembros del equipo de desarrollo.</li>
</ul><p>Estas actividades se pueden agrupar como se muestra en el diagrama general de grupos de procesos:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/diagrama_grupos_procesos.png?w=825"/></p>
<p>Todos los proyectos, que se gestionan como tales, tienen una serie de fases comunes, no tanto porque se realicen tareas iguales, sino porque el objetivo de cada fase con relación al producto a obtener es común a cualquier proyecto.</p>
<p>Así tenemos dos grandes fases: Planificación y Ejecución. Estas fases se subdividen en otras menores. Veamos cada una de ellas por separado.</p>
<h3>Iniciación</h3>
<p>El origen de un proyecto suele ser difuso. Normalmente alguien identifica un problema o una necesidad. Este problema-necesidad hace muy interesante el nacimiento de un proyecto, ya que podemos observar como ante el problema que se plantea unos gerentes lo ven como un impedimento para alcanzar sus metas, mientras otros, pensando que el mismo problema también la tienen sus competidores, lo ven como una oportunidad para dar una solución correcta y posicionarse mejor en el mercado.</p>
<p>Ya sea visto como problema u oportunidad, lo primero que hay que hacer es obtener una descripción clara de éste. La pregunta clave a responder es: <em>¿Cuál es el problema, o dónde está la oportunidad?</em> Evidentemente aquí hay que trabajar con los usuarios, directores de empresa y clientes, pues ellos son los que conocen su negocio y será de ellos de quien tendremos que obtener la información para responder a esta pregunta.</p>
<p>La definición del problema suele ocupar muy poco tiempo, por esto muchas veces no se le da la importancia central que tiene. Hay que tener en cuenta que todo el proyecto se basará en esta definición y es mejor que quede clara. La definición del problema debe ser revisada por todos los implicados en el problema: usuarios, directivos y clientes.</p>
<p>Normalmente al definir el problema debemos hurgar en la organización, sus objetivos y fines. También debemos, una vez clarificado el problema, identificar los beneficios que se obtendrán si lo solucionamos. Hay que evitar “las soluciones en busca de un problema”, es decir cuando alguien ha visto una aplicación en marcha, o un sistema, y quiere algo similar. Muchas veces se esconde la idea intuitiva de que aquello resolverá un problema o generará una oportunidad. Lo mejor es sacar a flote el problema o la oportunidad y entonces definirlo en términos claros.</p>
<p>También es peligrosa la situación en la que los únicos interesados en el problema y su solución son los implicados en el proyecto. Muchas veces los técnicos desean aplicar nuevas técnicas o herramientas y organizan un proyecto en torno a éstas.</p>
<p>En todo caso lo que se debe hacer es buscar en la empresa, identificando alguna aplicación que no sea compleja y que sea útil a los objetivos de la misma.</p>
<p>Los siguientes puntos nos dan una idea de la forma de pensar, así como las tareas a realizar durante esta fase:</p>
<ul><li>Estudiar el sistema actual.</li>
<li>Discutir y analizar lo que se desea obtener.</li>
<li>Clarificar las áreas de la empresa que se verán afectadas.</li>
<li>Definir el problema y sus componentes, aclarando: qué es fundamental, qué es deseable y qué es opcional.</li>
<li>Visualizar el producto o sistema a proporcionar, así como su adaptación a la organización.</li>
<li>Identificar al responsable del proyecto.</li>
<li>Crear una declaración clara de lo que se va a hacer.</li>
<li>Obtener el sí de los implicados: “Sí, tenemos exactamente ese problema”.</li>
</ul><p>En todas las fases y en esta de forma especial se debe estimar los costes previsibles del proyecto y, sobre todo, el coste de la siguiente fase, la planificación.</p>
<p>En muchas organizaciones, una vez definido el problema, éste se añade a la lista de los problemas pendientes de resolución. Así un comité de dirección selecciona el próximo problema a resolver, o sistema a desarrollar.</p>
<h3>Planificación</h3>
<p>El objetivo de toda planificación es la de clarificar el problema a solucionar, definir el producto a obtener, o servicio a proporcionar, estimar los costes económicos en que va a incurrir, así como los recursos humanos y de cualquier otro tipo que se requieran para alcanzar la meta.</p>
<p>La función principal es la de atender a las necesidades que aparecerán a lo largo del desarrollo, anticipando el curso de las tareas a realizar, la secuencia en que se llevarán a cabo, los recursos y el momento en que serán necesarios. Hay que tener en cuenta que normalmente hay más bienes o servicios que desearíamos obtener, que recursos disponibles para obtenerlos, por lo que las empresas deben seleccionar entre varias&nbsp; alternativas. Así una mala definición de un proyecto puede provocar que la empresa comprometa sus recursos en un bien del que hubiera podido prescindir en favor de un sustituto más económico.</p>
<p>La planificación del proyecto es la fase en la que se deberán identificar todas las cosas necesarias para poder alcanzar el objetivo marcado. En esta fase se han de concretar los tres cimientos sobre los que se apoyará el desarrollo de todo el proyecto, estos son:</p>
<ul><li>Calidad: viene dadas por las especificaciones.</li>
<li>Coste económico: valorado en el presupuesto.</li>
<li>Duración: asignada en el calendario de trabajo.</li>
</ul><p>Así como en la fase anterior nos centrábamos en identificar el problema, aquí tenemos que identificar diferentes soluciones y los costes asociados a cada una de ellas.</p>
<p>Aunque muchos autores separan el análisis de la aplicación de la propia planificación, por entenderse que la primera es una técnica, mientras que la planificación es una tarea de gestión, cronológicamente se han de realizar de forma simultánea, aunque, se debería partir de una especificación seria del problema, antes de planificar las tareas, costes y recursos necesarios para desarrollar la aplicación.</p>
<p>Otro asunto es que cada trabajo que se realiza se debe planificar antes de acometerlo. Así, antes de realizar el análisis se deberá hacer una planificación de los trabajos asociados a éste, pero difícilmente se podrá realizar la planificación de todo el proyecto.</p>
<p>Las tareas a realizar para planificar el proyecto, las podemos agrupar en:</p>
<ul><li>Estimar el tamaño de la aplicación a desarrollar.</li>
<li>Estimar el coste en recursos humanos.</li>
<li>Identificar las tareas a realizar.</li>
<li>Asignar recursos a cada tarea.</li>
<li>Crear un calendario de las tareas.</li>
<li>Realizar un estudio económico.</li>
<li>Reunir todo en un documento, Estudio de viabilidad.</li>
</ul><p>Estas tareas se realizan de forma secuencial o iterativa entre ellas. Esta sería una iteración de las tareas:</p>
<pre>Establecer las restricciones del proyecto
hacer las suposiciones iniciales de los parámetros del proyecto
<strong>while</strong> el proyecto no termina o ha sido cancelado <strong>loop</strong>
Describe la planificación de tiempos del proyecto
Inicia las actividades de acuerdo a la planificación
Espera (a que se lleve a cabo el desarrollo)
Revisa el progreso del proyecto
Revisa los parámetros estimados del proyecto
Actualiza la planificación del proyecto
Renegocia las restricciones del proyecto y los tiempos de entrega
<strong>if</strong> (aparecen problemas) <strong>then</strong>
inicia una revisión técnica y sus posibles soluciones
<strong>end if</strong>
<strong>end loop</strong></pre>
<p>Las actividades en un proyecto deben ser organizadas para producir resultados tangibles para que la administración pueda juzgar el progreso.</p>
<p>Los “Milestones” son los puntos finales de alguna actividad. Los “deliverables” son los resultados del proyecto que serán entregados a los clientes. El proceso de “cascada” permite una definición precisa de los “milestones”.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/milestones.png?w=825"/></p>
<h3>Ejecución</h3>
<p>En esta fase, se trata de llevar a cabo el plan previo. Se verá fuertemente influida por la planificación. Una mala planificación, llevará a una mala ejecución, ya que si se planifica que costará menos tiempo del real, los usuarios presionarán a los desarrolladores, con lo que éstos trabajarán en peores condiciones, del mismo modo, si se planifica un coste inferior, los administradores de la empresa presionarán al personal del proyecto, con lo que éstos trabajarán con más estrés.</p>
<p>Esta fase se caracteriza fundamentalmente porque en ella se ha de organizar el equipo de desarrollo, los mecanismos de comunicación, la asignación de roles y de responsabilidades a cada persona. Tareas fundamentales son:</p>
<ul><li>Identificar las necesidades de personal, que aunque ya venían de la fase de planificación, habrá que ajustarla a las disponibilidades actuales.</li>
<li>Establecimiento de la estructura organizativa.</li>
<li>Definir responsabilidades y autoridad.</li>
<li>Organizar el lugar de trabajo. En muchas ocasiones el comienzo de un proyecto tiene tareas como instalación de equipamientos, acondicionamiento de locales, …</li>
<li>Puesta en funcionamiento del equipo. Cuando las personas que van a trabajar en un proyecto no se conocen, es oportuno organizar reuniones más o menos informales para que se conozcan, esto evitará malentendidos y conflictos durante la ejecución del proyecto.</li>
<li>Divulgación de los estándares de trabajo y sistemas de informes. Al comenzar el proyecto, las personas están más receptivas que cuando se encuentran en un trabajo rutinario o cuando el objetivo se transforma en algo obsesivo. Ésta es una razón de peso para introducir los nuevos métodos de trabajo. Es posible que sea el cliente el que marque los estándares.</li>
</ul><h3>Control</h3>
<p>En este momento, ya tenemos el proyecto con su calendario, etc, las especificaciones claras, los recursos y personas en situación de trabajo. Las personas deben llevar a término cada una de las tareas que se les ha asignado en el momento que se le haya indicado. El objetivo principal en esta fase es; establecer visibilidad adecuada del progreso real del proyecto, de manera que la administración pueda tomar acciones efectivas cuando la ejecución del proyecto de software se desvía significativamente de los planes.</p>
<p>Por su parte el responsable del proyecto debe realizar las siguientes actividades:</p>
<ul><li>Revisar cumplimiento de planes y compromisos.</li>
<li>Tomar medidas del rendimiento.</li>
<li>Revisar los informes que le llegan de los empleados.</li>
<li>Mantener reuniones para identificar los problemas antes de que aparezcan.</li>
<li>Administrar / controlar los cambios en los productos generados dentro del proceso de desarrollo.</li>
<li>En caso de desviaciones poner en práctica las acciones correctivas necesarias.</li>
<li>Coordinar las tareas.</li>
<li>Motivar y liderar a los empleados.</li>
<li>Recompensar y disciplinar.</li>
</ul><h3>Cierre</h3>
<p>Ésta fase es la opuesta a la de puesta en marcha. En ésta se trata primero dar por finalizado el proyecto y entregar el producto, o dejar de producir el servicio encomendado.</p>
<p>Las actividades a realizar son las siguientes:</p>
<ul><li>Hacer entrega definitiva del producto al cliente.</li>
<li>Revisar las desviaciones del proyecto, identificar causas e indicar formas diferentes de actuación en futuros proyectos.</li>
<li>Reasignar el personal a los nuevos proyectos o reintegrarlos en los departamentos de partida.</li>
<li>Es interesante documentar las relaciones entre los empleados para futuros proyectos.</li>
</ul><h3>Gestión de Riesgos</h3>
<p>Gestión de riesgos concierne con la identificación de riesgos y la escritura de planes para minimizar el efecto de estos en el proyecto.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/gestion_de_riesgos.png?w=825"/></p>
<p>Un riesgo se relaciona con la probabilidad de que ocurra alguna circunstancia adversa al proyecto:</p>
<ul><li>Los riesgos de un proyecto afectan a la planificación o a los recursos.</li>
<li>Los riesgos del producto afectan a la calidad o al desempeño del software por desarrollarse.</li>
<li>Los riesgos del negocio son aquellos que afectan a la organización que desarrolla el software.</li>
</ul><p><strong>Identificación de los Riesgos</strong></p>
<p>Identifica riesgos en el proyecto, en el producto y en el negocio:</p>
<ul><li>Riesgos en la tecnología.</li>
<li>Riesgos en la gente.</li>
<li>Riesgos organizacionales.</li>
<li>Riesgos en los Requerimientos.</li>
<li>Riesgos de estimación.</li>
</ul><p><strong>Análisis de Riesgos</strong></p>
<p>Calculo de la posibilidad de que ocurran estos riesgos y de sus consecuencias:</p>
<ul><li>Determina la probabilidad y la seriedad de cada riesgo.</li>
<li>Las probabilidades pueden variar entre muy alta, alta, moderada, baja o muy baja.</li>
<li>Los efectos de los riesgos pueden ser: catastróficos, serios, tolerables o insignificantes.</li>
</ul><p><strong>Planificación de Riesgos</strong></p>
<p>Trazar planes para evitar o minimizar el efecto de los riesgos. Considera cada riesgo y desarrolla una estrategia para manejarlo:</p>
<ul><li>Estrategias de evasión: La probabilidad de que el riesgo que presente se minimizara.</li>
<li>Estrategias de minimización: El impacto del riesgo en el producto o en el proyecto se reducirá.</li>
<li>Planes de contingencia: Si el riesgo se presenta, el plan de contingencia se encarga de tratar este riesgo.</li>
</ul><p><strong>Monitorización de Riesgos</strong></p>
<p>Monitorizar los riesgos durante el proyecto:</p>
<ul><li>Determina regularmente cada riesgo identificado y decide si es probable o no que se presente.</li>
<li>Determina si los efectos que produciría el riesgo ha cambiado.</li>
<li>Cada riesgo clave debe discutirse en las reuniones de avance del proyecto.</li>
</ul><h2>Desarrollo en Fases</h2>
<p>El proceso de desarrollo de software no es solamente escribir líneas de código, compilar y ejecutar. Lo anterior es sólo una etapa (importante) de dicho proceso. En un proceso, se debe definir quién hace qué cosa cuando y cómo para alcanzar un cierto objetivo. En la ingeniería de software el objetivo principal es construir un producto de software o mejorar alguno ya construido, tomando en cuenta los requerimientos de los clientes (usuarios). Un proceso, provee de una guía para el desarrollo eficiente de un software de calidad. Tal proceso es una guía para todos los participantes en el desarrollo (usuarios, desarrolladores, responsables de proyecto, etc.) y permite construir software más ordenado y con un tiempo de vida relativamente largo.</p>
<p>Para realizar un proyecto, empezaremos por ver cuales son los objetivos que queremos alcanzar y luego pensaremos qué cosas tenemos que hacer para alcanzar estos fines. Esta descomposición pasará por identificar las fases de nuestro proyecto y el esfuerzo a aplicar en cada una de ellas. A su vez estas fases se descompondrán en tareas. También tendremos que marcar unos puntos (hitos) de control que nos permitan saber si el proceso va de acuerdo a lo previsto.</p>
<p>Normalmente todas las fases y tareas terminan en la generación de uno o varios documentos. A éstos se les llama <em>entregables</em>. Este nombre se debe a que pasan de manos del desarrollador a manos del controlador del proyecto o cliente. En los proyectos informáticos se suele asociar los hitos a la consecución de un entregable.</p>
<h3>Descomposición en Actividades del Proyecto (WBS)</h3>
<p>Empezaremos por ver la herramienta que se utiliza a la hora de descomponer y documentar el trabajo de un proyecto, como un conjunto de tareas. Habitualmente se le conoce como WBS (Work Breakdown Structure) que literalmente significa estructura de descomposición del trabajo. Es un método de representar de forma jerárquica los componentes de un proceso o producto. Puede ser utilizado para documentar la descomposición de un proceso, la descomposición de un producto, o de forma híbrida.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/wbs.png?w=825"/></p>
<h3>Entregables de un Proyecto Informático</h3>
<p>Los entregables son: “Productos que, en un cierto estado, se intercambian entre los clientes y los desarrolladores a lo largo de la ejecución del proyecto informático”.</p>
<p>Los entregables se clasifican como relativos al objetivo y relativos a la gestión del proyecto. Son relativos al objetivo todos aquellos documentos que hacen referencia exclusivamente al sistema de información y al subsistema informático en desarrollo. Pertenecen a este conjunto los requisitos del sistema, la especificación del sistema, la documentación del diseño, el código fuente, los programas ejecutables, los manuales de usuario, etc.</p>
<p>Los entregables relativos a la gestión del proyecto hacen referencia a aquellos documentos que se refieren a la situación en que se encuentra un proyecto, previsiones de costes, gastos realizados, informe sobre entornos de trabajo, etc, siendo su objetivo el poder controlar el proyecto. Pertenecen a esta clase la planificación del proyecto, los presupuestos, los documentos de control de la planificación o de la calidad, los estudios de riesgos durante el desarrollo, etc.</p>
<p>Se deberá definir de forma clara el conjunto mínimo de entregables necesario para dar por terminada cada fase de desarrollo. Aunque algunos entregables se desarrollan a lo largo de varias tareas.</p>
<p>Los entregables nos proveen de:</p>
<ul><li>Un conjunto de componentes que formarán el producto una vez finalizado el desarrollo.</li>
<li>Los medios para medir el progreso y la calidad del producto en desarrollo.</li>
<li>Los documentos necesarios para la siguiente etapa.</li>
</ul><h3>Entregables más Usuales</h3>
<p>Dado que como hemos visto los entregables juegan un papel central en el desarrollo de un subsistema informático, vamos a listar los más importantes:</p>
<ul><li>Estudio de viabilidad:
<ul><li>Descripción breve del sistema propuesto y sus características.</li>
<li>Descripción breve de las necesidades del negocio en el sistema propuesto.</li>
<li>Propuesta de organización del equipo de desarrollo y definición de responsabilidades.</li>
<li>Estudio de los costes, que contendrán estimaciones groseras de planificación y fechas, tentativas, de entrega de los productos.</li>
<li>Estudio de los beneficios que producirá el sistema.</li>
</ul></li>
<li>Análisis:
<ul><li>Captura de requisitos:
<ul><li>Análisis del sistema actual (si existe).</li>
<li>Requisitos nuevos de los usuarios.</li>
<li>Descripción del sistema propuesto.</li>
</ul></li>
<li>Especificación del sistema:
<ul><li>Descripción del sistema (DFD’s, etc.).</li>
<li>Requisitos de datos.</li>
<li>Requisitos de telecomunicaciones.</li>
<li>Requisitos de hardware.</li>
<li>Plan de pruebas de integración.</li>
</ul></li>
<li>Diseño:
<ul><li>Descripción detallada del sistema, contendrá:
<ul><li>Programas, módulos reutilizables y objetos.</li>
<li>Ficheros y bases de datos.</li>
<li>Transacciones.</li>
<li>Diccionario de datos.</li>
<li>Procedimientos.</li>
<li>Carga del sistema y tiempos de respuesta.</li>
<li>Interfaces, tanto humanos como de máquinas.</li>
</ul></li>
<li>Descripción de los controles del sistema propuestos.</li>
<li>Diseños alternativos recomendados.</li>
<li>Estándares de programación y diseño de programas, recomendados.</li>
<li>Técnicas de implementación recomendadas: codificación propia, compra de paquetes, contratación externa, etc.</li>
<li>Plan de pruebas de programas.</li>
</ul></li>
<li>Codificación:
<ul><li>Documentación del diseño final del sistema y de cada programa.</li>
<li>Diagramas definitivos del sistema y de los programas.</li>
<li>Descripción detallada de la lógica de cada programa.</li>
<li>Descripción de las Entradas y Salidad (ficheros, pantallas, listados, etc.).</li>
<li>Listado de los programas, conteniendo comentarios.</li>
<li>Cadenas de ejecución si es necesario (JCL, scripts, etc).</li>
<li>Resultado de las pruebas de cada unidad.</li>
<li>Resultado de las pruebas de cada programa.</li>
<li>Resultado de las pruebas de la integración.</li>
<li>Guía para los operadores del sistema.</li>
<li>Programa de entrenamiento de los operadores.</li>
<li>Manual de usuario del sistema.</li>
</ul></li>
<li>Pruebas:
<ul><li>Plan de pruebas del sistema (actualizado).</li>
<li>Informe de los resultados de las pruebas.</li>
<li>Descripción de las pruebas, el resultado esperado, resultado obtenido y acciones a tomar para corregir las desviaciones.</li>
</ul></li>
<li>Instalación:
<ul><li>Planes detallados de contingencias de explotación, caídas del sistema y recuperación.</li>
<li>Plan de revisión post-instalación.</li>
<li>Informe de la instalación.</li>
<li>Carta de aceptación del sistema.</li>
</ul></li>
<li>Mantenimiento:
<ul><li>Listado de fallos detectados en el sistema.</li>
<li>Listado de mejoras solicitadas por los usuarios (si no dan lugar a nuevos proyectos).</li>
<li>Traza detallada de los cambios realizados en el sistema.</li>
<li>Actas de las revisiones regulares del sistema y aceptación de los niveles de soporte.</li>
</ul></li>
</ul></li>
</ul><p>A todos estos documentos hay que añadir en todas las fases documentos con la estimación y planificación de la próxima fase y del resto del proyecto. También habrá que ir actualizando el índice de todo el material relacionado.</p>
<h3>Descomposición en Fases del Desarrollo de una Aplicación</h3>
<p>La descomposición por fases (actividades) se basa en referencias históricas de la empresa que asocian una cantidad media de horas de trabajo a una actividad concreta, de modo que dado un proyecto concreto podemos estimar la cantidad de esfuerzo que se dedicará a esa actividad. En ésta se ha de tener en cuenta el tipo de proyecto, el lenguaje de desarrollo y la madurez de la organización.</p>
<p>Podemos plantear la descomposición desde el enfoque de entregables y asociar las tareas a la producción de un entregable concreto. Este enfoque tiene la ventaja de que la culminación de una tarea indica que ha concluido un producto y viceversa. Dado que, como veremos, no es aconsejable el tener tareas que duren más de una semana, se plantean problemas con algunos entregables que cuestan más.</p>
<p>El planteamiento de descomponer por procesos o actividades puede resultar más natural en algunos casos. Es más fácil conseguir tareas acotadas en el tiempo. Tiene la desventaja de que el proyecto no será tan fácil de controlar ya que en muchos casos será la palabra de los realizadores la única constancia de que la tarea está terminada o al “90%”.</p>
<p>En cualquier caso, los proyectos se planifican con dos horizontes, el de la próxima fase y el del proyecto completo. En el horizonte de la próxima fase se realiza con mayor nivel de detalle, mientras que según se alejan las fases se aplica un menor nivel de detalle.</p>
<p>La descomposición del proyecto con mayor nivel de refinamiento no puede basarse en datos recogidos de forma analítica, sino que hace falta una aportación personal de los miembros del equipo de trabajo, tanto para identificar tareas como para asignarles esfuerzos. Se suele aconsejar el trabajo en grupo donde todos puedan aportar sus conocimientos y experiencias previas.</p>
<p>Hay que tener en cuenta que si identificamos las tareas y se las imponemos a los desarrolladores, éstos funcionarán en una situación de sumisión lo que puede tener efectos perniciosos tanto para los plazos de entrega como para la calidad del software. Por otra parte el dejar que sean los propios desarrolladores los que identifiquen tareas y recursos, dentro de un marco razonable (puntos de función) les llevará a una situación de compromiso personal, pasando a interiorizar los objetivos y como consecuencia obtendremos mejores resultados.</p>
<p>La tarea fundamental de los desarrolladores es escuchar a los clientes o usuarios y traducir sus requisitos a un lenguaje comprensible por la máquina, de modo que el subsistema informático se adapte a las necesidades expresadas. Así para cualquier tarea podremos encontrar las siguientes subtareas:</p>
<ul><li>Documentarse, Buscar o Investigar.</li>
<li>Organizar, Escribir Documentos.</li>
<li>Verificar, Comprobar.</li>
<li>Revisar, Actualizar Documentos.</li>
<li>Entregar, Finalizar.</li>
</ul><p>Además de lo anterior hay que tener en cuenta que al ir desarrollando el sistema obtenemos información que nos será útil a la hora de identificar nuevas tareas. Así, el análisis estructurado nos provee de una descomposición del proyecto por productos: transacciones, archivos, entradas, salidas, etc. El Diseño de programas nos descompone el sistema por módulos, el Diseño de BD descompone por tablas, archivos, etc, y los diseños de interfaz de pantallas, listados, mensajes, etc. Así, por ejemplo, una entrada puede ser que requiera de una reunión con el usuario, un estudio de ésta y la posterior presentación y aprobación de la propuesta a desarrollar.</p>
<h3>Tareas Usuales de un Proyecto Informático</h3>
<ul><li>Estudio de viabilidad:
<ul><li>Analizar el sistema propuesto y escribir una descripción.</li>
<li>Definir y documentar posibles tipos de sistemas.</li>
<li>Hacer un análisis de coste de sistemas similares.</li>
<li>Hacer una estimación del tamaño del sistema, la planificación y los costes (tener en cuenta los entregables más importantes).</li>
<li>Definir cualitativa y cuantitativamente los beneficios del sistema propuesto.</li>
<li>Realizar una planificación inicial del plazo de recuperación de la inversión.</li>
<li>Realización de una estimación detallada de costes, planificación, recursos, etc, de la siguiente fase (Análisis).</li>
<li>Asignar director del proyecto.</li>
<li>Composición del documento de estudio de viabilidad.</li>
<li>Presentación del documento de viabilidad a la dirección para su aprobación.</li>
</ul></li>
<li>Análisis:
<ul><li>Captura de requisitos:
<ul><li>Definir el ámbito del sistema propuesto.
<ul><li>Funciones</li>
<li>Usuarios</li>
<li>Restricciones</li>
</ul></li>
<li>Entrevista a todos los usuarios propuestos y actuales:
<ul><li>Determinar:
<ul><li>Utilización del sistema actual.</li>
<li>Deficiencias del sistema actual.</li>
<li>Requisitos nuevos del sistema.</li>
</ul></li>
<li>Documentar:
<ul><li>Descripción del sistema actual.</li>
<li>Deficiencias del sistema actual.</li>
</ul></li>
</ul></li>
<li>Producir el documento de requisitos del nuevo sistema:
<ul><li>Incluir:
<ul><li>Requisitos del usuario priorizados.</li>
<li>Resoluciones sobre las deficiencias del sistema actual.</li>
</ul></li>
</ul></li>
<li>Producir una lista de los beneficios tangibles e intangibles (un refinamiento de la lista del estudio de viabilidad).</li>
<li>Realización de una estimación detallada de costes, planificación, recursos, etc, de la siguiente fase (Especificación del sistema).</li>
<li>Producir una estimación revisada de costes, planificación, recursos, etc, para el resto del proyecto.</li>
<li>Producir el documento de definición de requisitos, esta tarea incluye la construcción de un prototipo.</li>
<li>Realizar una revisión final del documento de requisitos.</li>
<li>Toma la decisión de continuar o no con el proyecto.</li>
<li>Definir las responsabilidades en la próxima fase para el director, miembros del equipo de desarrollo y otros.</li>
</ul></li>
<li>Especificación del sistema:
<ul><li>Definir el tipo de sistema propuesto: Transformar las restricciones físicas, ambientales y operacionales a características del sistema. Por ejemplo: ¿Sistema basado en transacciones? ¿Distribuido o centralizado?¿Estaciones de trabajo o terminales?</li>
<li>Esquematizar el sistema propuesto: Transformar los requerimientos del usuario de la fase anterior en unas especificaciones funcionales (DFD, Organigramas, etc).</li>
<li>Construir el diccionario de datos (DD): Describir todos los elementos del DFD incluyendo funciones y datos; asegurarse de que todas las relaciones inter-funcionales y entre datos sean documentadas. Si existe DD de la empresa, hacerlo compatible con el que estamos realizando.</li>
<li>Revisar y expandir el análisis de coste beneficio: Actualizarlo con la información nueva y verificar que los beneficios esperados se mantienen y que el plazo de recuperación de una inversión sigue siendo aceptable.</li>
<li>Realización de una estimación detallada de costes, planificación, recursos, etc, de la siguiente fase (Diseño del sistema).</li>
<li>Producir una estimación revisada de costes, planificación, recursos, etc, para el resto del proyecto.</li>
<li>Producir el documento de especificación del sistema.</li>
<li>Realizar una revisión final del documento de especificación del sistema.</li>
<li>Tomar la decisión de continuar o no con el proyecto.</li>
<li>Definir las responsabilidades en la próxima fase para el director, miembros del equipo de desarrollo y otros.</li>
</ul></li>
</ul></li>
<li>Diseño:
<ul><li>Producir el diseño global del sistema, contendrá:
<ul><li>Definir los programas y sus principales funciones.</li>
<li>Definir los principales flujos de datos entre programas y funciones.</li>
<li>Diseñar el esquema de datos lógico y físico.</li>
<li>Definir las fronteras con paquetes software, si existen.</li>
<li>Definir los entornos de hardware y software, proponiendo alternativas.</li>
</ul></li>
<li>Localización de paquetes software: Buscar paquetes software apropiados que puedan implementar parte, o toda la funcionalidad requerida del sistema de forma rentable y que, si se implementa, ofrezca un entorno compatible con los objetivos de la organización. (Puede realizarse antes del diseño, o de forma simultánea a la tarea anterior).</li>
<li>Desarrollar un diseño detallado del sistema, para cada alternativa de diseño planteada:
<ul><li>Crear una descripción narrativa detallada del diseño para todo el sistema y cada una de sus partes (programas, funciones y datos).</li>
<li>Actualizar el diccionario de datos.</li>
<li>Definir los componentes hardware específicos (Capturadores de datos, sistemas de comunicación, etc) y sus funciones.</li>
<li>Validar el diseño con las especificaciones del sistema.</li>
<li>Documentar el entorno hardware y software necesarios para esta alternativa.</li>
</ul></li>
<li>Revisar y expandir el análisis de coste beneficio para cada alternativa:
<ul><li>Actualizar con la información nueva.</li>
<li>Verificar que los beneficios esperados se mantienen y que el plazo de recuperación de la inversión sigue siendo aceptable.</li>
</ul></li>
<li>Evaluar las alternativas de diseño, para cada alternativa, documentar:
<ul><li>Requerimientos de usuario que se alcanzan con esta alternativa.</li>
<li>Nivel de aceptación esperado de los usuarios.</li>
<li>Realización de una estimación detallada de costes, planificación, recursos, etc, de la siguiente fase (Codificación) con esta alternativa.</li>
<li>Producir una estimación revisada de costes, planificación, recursos, etc, para el resto del proyecto.</li>
<li>Alternativa recomendada.</li>
</ul></li>
<li>Desarrollo de un plan de test del sistema:
<ul><li>Crear datos de entrada del test.</li>
<li>Producir el listado de los resultados esperados.</li>
<li>Producir el listado de los criterios de test.</li>
<li>Desarrollar la planificación de test del sistema.</li>
</ul></li>
<li>Desarrollar un plan de test diferenciado para cada alternativa.</li>
<li>Identificar las necesidades de entrenamiento y documentación de los usuarios. Definir las guías de:
<ul><li>Documentación completa de usuario.</li>
<li>Manuales de operador.</li>
<li>Documentos y planificación de formación para usuarios y operadores.</li>
</ul></li>
<li>Producir el documento de diseño del sistema.</li>
<li>Realizar una revisión final del documento de diseño del sistema.</li>
<li>Tomar la decisión de continuar o no con el proyecto.</li>
<li>Recomendar una alternativa.</li>
<li>Definir las responsabilidades de la próxima fase para el director, miembros de los equipo de programación y test, así como de otros implicados.</li>
</ul></li>
<li>Codificación:
<ul><li>Producir un plan de trabajo:
<ul><li>Creación de la lista detallada de tareas necesarias para realizar la codificación y test de todos los componentes del sistema.</li>
<li>Producir una planificación para las tareas anteriores con las fechas más tempranas y más tardías, así como la asignación de responsabilidades.</li>
<li>Instaurar los procedimientos para recoger los progresos y estados del proyecto.</li>
<li>Instaurar los procedimientos para recoger tiempos, si resulta apropiado.</li>
<li>Obtener la aprobación del plan de trabajo por parte de la dirección.</li>
</ul></li>
<li>Realización del diseño detallado de cada programa:
<ul><li>Diseñar detalladamente los diagramas:
<ul><li>De estructura de los programas.</li>
<li>De estructura de los ficheros.</li>
<li>Pantallas, informes, y otras composiciones.</li>
<li>Esquemas de la base de datos.</li>
<li>Composición de las tablas y sus diseños.</li>
</ul></li>
<li>Pseudocódigo de la lógica del programa (Dependerá de los métodos de diseño utilizados).</li>
</ul></li>
<li>Codificar, documentar y pasar los test en cada programa:
<ul><li>Codificar el programa.</li>
<li>Realizar las pruebas de unidad, hasta que los programas se adapten a las especificaciones descritas en las etapas anteriores.</li>
<li>Actualizar todo lo necesario en el sistema y en el DD de la organización.</li>
</ul></li>
<li>Realizar el test de integración:
<ul><li>Poner todos los programas probados en la librería de pruebas de integración.</li>
<li>Realizar el test de integración de cada programa.</li>
<li>Documentar todos los resultados del test de integración.</li>
</ul></li>
<li>Terminar los manuales de operador y usuario, así como los de formación.</li>
<li>Realización de una estimación detallada de costes, planificación, recursos, etc, de la siguiente fase (Prueba del sistema).</li>
<li>Producir una estimación revisada de costes, planificación, recuros, etc, para el resto del proyecto.</li>
<li>Confeccionar el documento de diseño de programas y codificación.</li>
<li>Realizar revisiones del documento de diseño de programas y codificación.</li>
<li>Obtener los resultados finales de la integración completa del sistema y de las pruebas de integración.</li>
<li>Definir las responsabilidades en la próxima fase para el director, miembros del equipo de test, así como de otros implicados.</li>
</ul></li>
<li>Pruebas:
<ul><li>Realizar el test del sistema:
<ul><li>Hacer el test de sistema de acuerdo al documento de test del sistema.</li>
<li>Verificar la operatividad de los manuales de usuario y operador, utilizándolas en los cursos de formación de los usuarios y operadores que realicen el test del sistema.</li>
<li>Verificar los documentos de entrenamiento de usuarios y operadores, utilizándolos en los cursos de formación de los usuarios y operadores que realicen el test del sistema.</li>
<li>Documentar completamente los resultados del test del sistema.</li>
</ul></li>
<li>Revisar la planificación de instalación:
<ul><li>Disponibilidad de los recursos.</li>
<li>Revisión de los factores de contingencia que puedan afectar a la instalación:
<ul><li>Procesos especiales de final de mes y fin de año.</li>
<li>Vacaciones y fiestas.</li>
</ul></li>
<li>Disponibilidad de soporte por parte de otros proveedores.</li>
<li>Revisión final del calendario de instalación.</li>
</ul></li>
<li>Esbozar el plan de contingencia ante caídas del sistema:
<ul><li>Criterios para las caídas.</li>
<li>Identificación de recursos para contingencias.</li>
<li>Horario para recuperaciones o abandonos.</li>
</ul></li>
<li>Desarrollar un acuerdo de nivel de servicio:
<ul><li>Criterios de rendimiento de usuario, precisión y volumen.</li>
<li>Criterios de apoyo de los proveedores:
<ul><li>Tiempo medio entre fallos.</li>
<li>Tiempo medio de reparación.</li>
</ul></li>
<li>Criterios de calidad del sistema.</li>
<li>Frecuencia con la que se medirán los criterios.</li>
</ul></li>
<li>Producir los documentos de test en la entrega.</li>
<li>Revisión y aprobación de los documentos de entrega.</li>
<li>Aprobación de la documentación del sistema.
<ul><li>Documentación de programas.</li>
<li>Manuales de operador.</li>
<li>Manuales de usuario.</li>
<li>Manuales de formación.</li>
<li>Documentación de ayuda.</li>
</ul></li>
<li>Aprobación del plan de instalación.</li>
<li>Aprobación de los planes de contingencia, recuperación y caídas.</li>
<li>Finalización del sistema completamente probado:
<ul><li>Documento de finalización del desarrollo del sistema.</li>
<li>Documento de finalización de los usuarios.</li>
<li>Documento de finalización del CPD.</li>
<li>Documento de finalización de garantía de calidad.</li>
<li>Documento de finalización de finanzas.</li>
</ul></li>
</ul></li>
<li>Instalación:
<ul><li>Instalación de hardware y software nuevo.</li>
<li>Formar a los primeros usuarios y operadores.</li>
<li>Desarrollar los planes de contingencia, recuperación y caída.</li>
<li>Desarrollar los procedimientos de mantenimiento y versiones.</li>
<li>Establecer procedimientos para:
<ul><li>Versiones regulares.</li>
<li>Versiones de emergencia.</li>
<li>Versión por configuración, si existen diferentes tipos de hardware.</li>
</ul></li>
<li>Llevar a cabo cualquier conversión de datos necesaria.</li>
<li>Llevar a cabo la instalación del sistema nuevo a producción:
<ul><li>Instalación completa desde cero.</li>
<li>Instalación en paralelo.</li>
<li>Instalación por fases.</li>
</ul></li>
<li>Planificar y programar las revisiones post-instalación. Establecer los criterios de:
<ul><li>Rendimiento del sistema.</li>
<li>Calidad del sistema.</li>
<li>Satisfacción del usuario.</li>
<li>Calidad y facilidad de Gestión de: manuales de usuario y operador, formación de usuarios y operadores e información y datos producidos.</li>
<li>Fluidez de la instalación.</li>
<li>Costes de desarrollo, instalación, operaciones y mantenimiento. Establecer planificación y calendario de las revisiones, asegurando la disponibilidad del personal y documentación.</li>
</ul></li>
<li>Llevar a cabo las revisiones post-instalación:
<ul><li>Crear el informe de la revisión post-instalación.</li>
<li>Obtener la aprobación firmada de los informes de:
<ul><li>Usuarios finales del sistema.</li>
<li>Operadores del sistema.</li>
<li>Auditoria y garantía de la calidad.</li>
<li>Desarrollo de sistemas.</li>
<li>Soporte de sistemas y mantenimiento.</li>
<li>Finanzas.</li>
</ul></li>
<li>Obtener la carta de aprobación del sistema.</li>
</ul></li>
<li>Establecer el calendario para otras revisiones post-instalación si es necesario.</li>
</ul></li>
<li>Mantenimiento:
<ul><li>Implementar los cambios del sistema:
<ul><li>Utilizar los procedimientos de implementación de versiones.</li>
<li>Implementar versiones de emergencias.</li>
</ul></li>
<li>Asegurarse de que el sistema continúa solucionando las necesidades de los usuarios:
<ul><li>Utilizar los acuerdos de niveles de soporte, en estos acuerdos se establecen los requerimientos de soporte y objetivos de funcionamiento:
<ul><li>Revisiones regulares de requerimientos del nivel de acuerdo.</li>
<li>Revisiones regulares de como el sistema está alcanzando sus objetivos.</li>
</ul></li>
<li>Llevar a cabo revisiones regulares del sistema:
<ul><li>Utilizar los procedimientos y contenido de las revisiones post-instalación.</li>
</ul></li>
</ul></li>
</ul></li>
</ul><p>Estas tareas se han enumerado a modo de lista de comprobación, de forma que serán los desarrolladores los encargados de identificar las tareas apropiadas a cada proyecto así como los recursos necesarios, teniendo en cuenta la estimación previa del esfuerzo.</p>
<h2>Tareas y Funciones de los Distintos Agentes</h2>
<p>Son personas y organizaciones que participan activamente en el proyecto o cuyos intereses pueden ser afectados positiva o negativamente tanto por el resultado de la ejecución del proyecto como por su terminación exitosa.</p>
<p>Los principales <em>agentes</em> en cada proyecto pueden ser:</p>
<ul><li>Jefe de proyecto. Responsable de la planificación y ejecución el proyecto.</li>
<li>Equipo de desarrollo. Encargado de realizar el proyecto.</li>
<li>Cliente. Es el que arriesga su dinero en el desarrollo, es decir, el que pagará por el sistema.</li>
<li>Usuarios. Personas que utilizarán el sistema a nivel operativo y que normalmente pertenecen al cliente. Nos dan pistas sobre el problema a nivel de funcionamiento. Son responsables de que el sistema funcione de manera eficiente.</li>
</ul><h3>El Jefe de Proyecto</h3>
<p>La misión del jefe de proyecto es:</p>
<ul><li>Con el cliente:
<ul><li>Dejarlo satisfecho.</li>
<li>Incrementar su competitividad y/o desempeño interno a través de la solución que se le entregue.</li>
</ul></li>
<li>Con el negocio:
<ul><li>Lograr rentabilidad.</li>
<li>Aprovechar recursos al máximo.</li>
</ul></li>
<li>Con los recursos humanos:
<ul><li>Crecimiento profesional.</li>
<li>Satisfacción interna y externa.</li>
</ul></li>
</ul><p>Al jefe de proyecto se le concede una amplia autoridad sobre los recursos del proyecto y puede adquirir nuevos recursos ya sea dentro o fuera de la organización. Todo el personal del proyecto está bajo su autoridad mientras dure el proyecto. Debe combinar conocimiento técnico en la materia además de habilidades de dirección para poder dirigir a todo el personal del proyecto.</p>
<p>Las interacciones que tiene el jefe de proyecto dentro de su organización son:</p>
<ul><li>Con su equipo de trabajo.</li>
<li>Con el ejecutivo de cuenta.</li>
<li>Con el departamento de calidad.</li>
</ul><p>Las interacciones que tiene el jefe de proyecto con el cliente son:</p>
<ul><li>Con el usuario operativo.</li>
<li>Con el departamento de sistemas.</li>
<li>Con el experto funcional del negocio.</li>
<li>Con otras áreas.</li>
</ul><h3>Responsabilidades del Jefe de Proyecto</h3>
<ul><li>Conocer los criterios de negociación acordados con el cliente.</li>
<li>Notificar al ejecutivo de cuenta los cambios al alcance para que los renegocie adecuadamente.</li>
<li>Evaluar el desempeño de cada persona en base al cumplimiento de los compromisos acordados.</li>
<li>Informar a la dirección de manera justificada y en tiempo sobre la planificación de la asignación y liberación de recursos.</li>
<li>Informar los requerimientos de formación, evaluaciones y vacaciones de los miembros del equipo de trabajo al director.</li>
<li>Informar de avances e incidentes del proyecto.</li>
<li>Asegurar que el proyecto sea rentable y productivo.</li>
<li>Dar seguimiento al plan de trabajo y corregir desviaciones a tiempo.</li>
<li>Asegurar la obtención de los recursos materiales indispensables para desarrollar el proyecto.</li>
</ul><h3>Autoridad del Jefe de Proyecto</h3>
<ul><li>Organizar al equipo de trabajo como sea más conveniente y productivo.</li>
<li>Definir las expectativas de crecimiento para los miembros del equipo de trabajo.</li>
<li>Implementar las medidas necesarias para que las expectativas de cada persona se cumplan.</li>
<li>Prescindir de los servicios de un miembro del equipo de trabajo, si hay motivos para apoyar esta decisión.</li>
</ul><h2>Bibliografia</h2>
<ul><li><a href="https://es.scribd.com/document/93243574/TICB2-Gestion-Del-Proceso-de-Desarrollo" rel="noopener" target="_blank">Scribd (tfandos)</a></li>
</ul> </article>

# Planificación del desarrollo. Técnicas de planificación. Metodologías de desarrollo. La metodología Métrica.

<article><h2>Técnicas de Planificación</h2>
<h3>Introducción a la Planificación del Desarrollo</h3>
<p>El objetivo de la Planificación del proyecto Software es proporcionar un marco de trabajo que permita al gestor hacer estimaciones razonables de recursos, costos y planificación temporal. Estas estimaciones se hacen dentro de un marco de tiempo limitado al comienzo de un proyecto de software, y deberían actualizarse regularmente a medida que progresa el proyecto. Además las estimaciones deberían definir los escenarios del mejor caso, y peor caso, de modo que los resultados del proyecto pueden limitarse.</p>
<p>El Objetivo de la planificación se logra mediante un proceso de descubrimiento de la información que lleve a estimaciones razonables.</p>
<p>Existen diversos tipos de planes:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/planes.png?w=825"/></p>
<p>Aunque hay que tener en cuenta que la planificación conlleva una serie de problemas añadidos:</p>
<ul><li>Es difícil estimar la longitud y dificultad de las tareas, por lo que la estimación del coste es más difícil.</li>
<li>La productividad no es proporcional al número de personas trabajando en una tarea.</li>
<li>Incluir personal en un proyecto en avance, retrasa el proyecto por sobrecargas en la comunicación.</li>
<li>Lo inesperado siempre sucede. Es necesario considerar siempre contingencias.</li>
</ul><h3>Herramientas Básicas Usadas en la Planificación</h3>
<p>Aunque desde la antigüedad se han realizado proyectos de gran envergadura como por ejemplo la construcción de edificios públicos, guerras, viajes, etc, no es hasta principios de este siglo cuando aparece el conocido diagrama de Gantt en el que se refleja de forma esquemática las tareas, su duración y las fechas en que se deberán realizar. Trabajando sobre este diagrama el director de proyecto realizaba planificaciones y seguimiento de un proyecto.</p>
<p>Dada la evolución tecnológica los seres humanos cada vez abordamos proyectos más complejos, pero por otra parte creamos técnicas más evolucionadas, completas y automáticas para gestionar estos proyectos. La construcción del misil Polaris, así como la solución de los problemas en la gestión de la producción de Dunlop llevaron al desarrollo de las técnicas conocidas como PERT (Técnica para la Evaluación y Revisión de Programas) y CMP (Método del Camino Crítico) que aportan a la programación de proyectos técnicas matemáticas.</p>
<p>Estas técnicas surgieron de la necesidad de obtener algoritmos automatizables que ayudasen a los gestores de proyectos complejos en la construcción de calendarios (programas). En el siguiente punto veremos mediante un ejemplo como se aplica en el CPM.</p>
<p><em>Diagrama de Gantt.</em></p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/diagrama_gantt.png?w=825"/></p>
<h3>Aplicación de la Técnica CPM</h3>
<p>El CPM se realiza sobre un proyecto en cuatro etapas, a continuación se describe cada una de ellas.</p>
<p><strong>Etapa 1. Identificar las Tareas</strong></p>
<p>Se deben identificar cada una de las tareas que forman parte del desarrollo del proyecto.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/identificar_tareas.png?w=825"/></p>
<p>Si queremos realizar el proceso de forma manual, rellenaremos una ficha por cada actividad identificada. El formato de la ficha será el que se muestra en la figura.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/especificacion_tarea.png?w=825"/></p>
<p><strong>Etapa 2. Añadir Recursos y Tiempos</strong></p>
<p>A cada actividad se le asignarán recursos (personas, material, equipos, etc) y tiempo estimado para su realización, completando la ficha.</p>
<p><strong>Etapa 3. Ordenar las Tareas</strong></p>
<p>En esta etapa se tienen que organizar las tareas en base al orden técnico de ejecución. Así sabemos que hay que hacer las especificaciones antes de diseñar el programa. Nos podemos plantear las siguientes preguntas para ordenar las tareas:</p>
<ul><li>¿Qué se puede hacer ahora?</li>
<li>¿Qué debe haberse hecho antes de esto?</li>
<li>¿Qué podría hacerse a la vez?</li>
<li>¿Qué debe seguir a lo que hacemos ahora?</li>
</ul><p>Si se trata de calcular el Camino Crítico de forma manual será interesante pinchar todas las tareas en un tablero de corcho, señalando mediante cuerdas la ordenación de las tareas. Esta representación es conocida como <em>red de procedencia</em>, aunque su apariencia es diferente al gráfico PERT en algunos programas informáticos se describe erróneamente con este nombre.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/red_procedencia.png?w=825"/></p>
<p>Si tenemos un diagrama complejo, y queremos realizar los cálculos de forma manual se puede utilizar el método que se describe a continuación.</p>
<p>Este diagrama se compone de nodos y arcos, similares a las pegatinas comentadas anteriormente. Los nodos representan a las tareas y la información necesaria para calcular sus fecha de realización. Los arcos indican las precedencias entre tareas.</p>
<p>Vamos a representar cada nodo (tarea) como se ve en la figura.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/nodo_tarea.png?w=825"/></p>
<p>Donde:</p>
<ul><li>DESCRIPCIÓN DE LA ACTIVIDAD es el nombre que le hemos dado a la actividad. Por ejemplo: Codificación Programa A.</li>
<li>Etiqueta actividad es un número arbitrario y que identifica unívocamente a cada actividad.</li>
<li>Duración es el tiempo que calculamos que se tardará en completar la tarea, teniendo en cuenta el esfuerzo y los recursos asignados a la tarea. Por ejemplo una tarea que estimamos requerirá seis días-hombre de esfuerzo, si se realiza entre tres personas podría tener una duración de dos días.</li>
<li>Inicio temprano es la fecha en que se podrá comenzar la tarea si no se retrasa ninguna otra.</li>
<li>Final temprano es, en el caso de iniciarse la tarea en el inicio temprano, lo antes que puede finalizar, respetando su duración.</li>
<li>Inicio tardío es la fecha más retrasada en la que puede comenzar la tarea para que se pueda completar el proyecto en la fecha marcada como final del proyecto.</li>
<li>Final tardío es la fecha más retrasada en la que puede terminar la tarea para que se pueda completar el proyecto en la fecha marcada como final del proyecto.</li>
<li>Máximo tiempo disponible es el tiempo máximo que puede durar una tarea en caso de comenzar en su Inicio temprano y concluir en su Final tardío.</li>
<li>Holgura es la diferencia entre el Máximo tiempo disponible y su Duración.</li>
</ul><p><strong>Etapa 4. Cálculo del Camino Crítico</strong></p>
<p>Una vez tenemos todas las tareas con sus respectivas duraciones y las precedencias pasamos a dibujar una red en la que aparezca para cada tarea una caja similar a la vista en el punto anterior con casi todos los campos vacíos. Entre ellas aparecerán los arcos indicando precedencias, tendremos algo similar a la figura.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/camino_critico.png?w=825"/></p>
<p>Ahora calculamos las fechas tempranas. Para esto seguimos los siguientes pasos:</p>
<ul><li>En aquellas tareas que no tienen ningún predecesor se le asigna a <em>Inicio temprano</em> el valor 0.</li>
<li>Si la tarea tiene predecesoras y todas estas tienen calculado su <em>Final temprano</em> se toma como <em>Inicio temprano</em> el máximo de todos ellos.</li>
<li>El <em>Final temprano</em> de cada tarea se calcula como el <em>Inicio temprano</em> más la <em>Duración</em>.</li>
</ul><p>Repetiremos estos pasos hasta que todas las tareas tengan sus fechas tempranas.</p>
<p>Para calcular las fechas tardías procederemos con los pasos que se describen a continuación:</p>
<ul><li>Se obtiene la fecha de finalización de proyecto más tardía. Esta puede venir dada por algún tipo de razones externas o puede que se nos pida que el proyecto termine lo antes posible, en este caso la fecha de finalización más tardía será el máximo de los “<em>Final temprano</em>” de todas las tareas.</li>
<li>A aquellas tareas que no sean predecesoras de ninguna otra se les asigna como <em>Final tardío</em> la fecha de finalización más tardía del punto 4.</li>
<li>El <em>Inicio tardío</em> se calcula restando al <em>Final tardío</em> la <em>Duración</em>.</li>
<li>En aquellas tareas que son predecesoras de otras se calcula el <em>Final tardío</em> como el mínimo de los <em>Inicio tardío</em> de las tareas de que es predecesora.</li>
</ul><p>Los otros dos campos de cada tarea: Máximo tiempo disponible y Holgura se calculan mediante las siguientes fórmulas:</p>
<pre>Máximo tiempo disponible = Final tardío - Inicio temprano
Holgura = Máximo tiempo disponible - Duración</pre>
<p><strong>Obtención del Camino Crítico</strong></p>
<p>Llamamos camino crítico de una planificación al conjunto de tareas que tienen <em>Holgura</em> cero. Siempre que se solicita que el proyecto tenga la duración mínima tendremos un camino crítico.</p>
<p>Se le llama camino crítico porque suele ser un camino que parte de una tarea que no tiene predecesoras y atraviesa el grafo por tareas con holgura cero hasta terminar en una tarea que no es predecesora de ninguna otra. Puede darse el caso de que con el “camino crítico” se puedan construir varias secuencias, partiendo de tareas sin predecesoras y se alcancen tareas sin sucesoras.</p>
<p>A las tareas del camino crítico se les llama tareas críticas y esto se debe a que un retraso en cualquiera de ellas lleva a un retraso del final del proyecto.</p>
<h3>Diferencia Fundamental entre el CPM y el PERT</h3>
<p>Aunque en principio son similares los algoritmos de ambos métodos, la asignación de duraciones de las tareas en el PERT es algo más elaborada. En lugar de realizarse una sola estimación se realizan tres estimaciones:</p>
<ul><li>“tm” tiempo medio que se estima para la actividad.</li>
<li>“to” tiempo optimista, el que resultaría de ir todo muy bien.</li>
<li>“tp” tiempo pesimista, el que resultaría si todo fuese mal en esta tarea.</li>
</ul><p>A la tares se le asigna como duración el resultado de:</p>
<pre>Duración = (to + 4 tm + tp) / 6</pre>
<p>Por otra parte el grafo se construye de forma dual a la vista. Los arcos modelan las actividades o tareas, mientras que los nodos modelan la relación de precedencia de las tareas. Así un nodo indica que los arcos que llegan a él anteceden a los que salen de él.</p>
<h3>Uso de Aplicaciones para la Planificación Control de Proyectos</h3>
<p>Como hemos indiciado estos algoritmos se hicieron pensando en el uso de sistemas de cómputo automático, así que no es de extrañar que existan muchas aplicaciones que den soporte a éstos. Entre las más conocidas que funcionan sobre PC están el CA-SuperProject y el Microsoft Project.</p>
<h2>Metodologías de Desarrollo: La Metodología Métrica 3</h2>
<h3>Introducción a la Metodología Métrica 3</h3>
<p>Antes de describir una metodología, es necesario aclarar ciertas cuestiones, tales como:</p>
<ul><li>¿Qué es una metodología?</li>
<li>¿Para qué sirve?</li>
</ul><p>Por que la respuesta a estas preguntas va a ser crucial para poder entender y evaluar toda la exposición siguiente sobre la metodología Métrica 3.</p>
<p><strong>¿Qué es una Metodología?</strong></p>
<p>Según el Diccionario de la Lengua Española de la Real Academia, metodología es “Ciencia del método” o “Conjunto de métodos que se siguen en una investigación científica o en una exposición doctrinal”. Aunque existe otra un poco más certera; “Modo de decir o hacer con orden una cosa”, parece que esto aclara algo más, lo que veremos en el tema es un modo o manera concreto (Métrica 3) de hacer con orden una cosa (desarrollo de sistemas de información).</p>
<p>El desarrollo de sistemas de información es una tarea de resolución de problemas, en la que el problema a resolver consiste en traducir:</p>
<ul><li>La situación-problema a un sistema de representación útil para nuestros propósitos (análisis de requisitos).</li>
<li>La representación resultante de la fase anterior en otra que vaya acercando los objetos, conceptos y relaciones a una forma inteligible por nuestro dominio objetivo (máquinas, personas, otros sistemas de información); de esta manera realizaremos el diseño, desde el cual, en un proceso de traducción final, codificaremos los programas de ordenador, las instrucciones para los usuarios, las interfaces con otros sistemas, etc.</li>
</ul><p><strong>¿Para qué sirve?</strong></p>
<ul><li>En primer lugar como guía; nos dice lo que tenemos que hacer, cómo, cuándo y quién tiene que hacerlo; además, lo hace de manera completa; podremos saltarnos los pasos que consideremos convenientes siempre que comprendamos la estructura del método y podamos evaluar la conveniencia de utilizar atajos.</li>
<li>En segundo lugar, determina los puntos del proceso en los que debemos detenernos y comprobar cómo vamos, algo bastante importante y que evita la propagación de los errores a través del proceso.</li>
<li>En tercer lugar, permite que los conocimientos adquiridos en el desarrollo de sistemas de información se plasmen en el método que la organización utiliza para ello mediante su continua revisión y adaptación y pasen a ser patrimonio de la organización y no solo de las personas que llevan a cabo la tarea.</li>
</ul><p><strong>Objetivos</strong></p>
<p>La metodología MÉTRICA Versión 3 ofrece a las Organizaciones un instrumento útil para la sistematización de las actividades que dan soporte al ciclo de vida del software dentro del marco que permite alcanzar los siguientes objetivos:</p>
<ul><li>Proporcionar o definir Sistemas de Información que ayuden a conseguir los fines de la Organización mediante la definición de un marco estratégico para el desarrollo de los mismos.</li>
<li>Dotar a la Organización de productos software que satisfagan las necesidades de los usuarios dando una mayor importancia al análisis de requisitos.</li>
<li>Mejorar la productividad de los departamentos de Sistemas y Tecnologías de la Información y las Comunicaciones, permitiendo una mayor capacidad de adaptación a los cambios y teniendo en cuenta la reutilización en la medida de lo posible.</li>
<li>Facilitar la comunicación y entendimiento entre los distintos participantes en la producción de software a lo largo del ciclo de vida del proyecto, teniendo en cuenta su papel y responsabilidad, así como las necesidades de todos y cada uno de ellos.</li>
<li>Facilitar la operación, mantenimiento y uso de los productos software obtenidos.</li>
</ul><p><strong>Características</strong></p>
<ul><li>La nueva versión de MÉTRICA contempla el desarrollo de Sistemas de Información para las distintas tecnologías que actualmente están conviviendo y los aspectos de gestión que aseguran que un Proyecto cumple sus objetivos en términos de calidad, coste y plazos.</li>
<li>Su punto de partida es la versión anterior de MÉTRICA de la cual se han conservado la adaptabilidad, flexibilidad y sencillez, así como la estructura de actividades y tareas, si bien las fases y módulos de MÉTRICA versión 2.1 han dado paso a la división en Procesos, más adecuada a la entrada-transformación-salida que se produce en cada una de las divisiones del ciclo de vida de un proyecto. Para cada tarea se detallan los participantes que intervienen, los productos de entrada y de salida así como las técnicas y prácticas a emplear para su obtención.</li>
<li>En la elaboración de MÉTRICA Versión 3 se han tenido en cuenta los métodos de desarrollo más extendidos, así como los últimos estándares de ingeniería del software y calidad, además de referencias específicas en cuanto a seguridad y gestión de proyectos. También se ha tenido en cuenta la experiencia de los usuarios de las versiones anteriores para solventar los problemas o deficiencias detectados.</li>
</ul><p><strong>Estructura</strong></p>
<p>En una única estructura la metodología MÉTRICA Versión 3 cubre distintos tipos de desarrollo: estructurado y orientado a objetos, facilitando a través de interfaces la realización de los procesos de apoyo u organizativos: Gestión de Proyectos, Gestión de Configuración, Aseguramiento de Calidad y Seguridad.</p>
<p>La automatización de las actividades propuestas en la estructura de MÉTRICA Versión 3 es posible ya que sus técnicas están soportadas por una amplia variedad de herramientas de ayuda al desarrollo.</p>
<p>Cada Proceso detalla las Actividades y Tareas a realizar.</p>
<p>Para cada tarea se indican:</p>
<ul><li>Las técnicas y prácticas a utilizar.</li>
<li>Los responsables de realizarla.</li>
<li>Sus productos de entrada y salida.</li>
</ul><p>La estructura de procesos es la siguiente:</p>
<ul><li>Planificación (PSI)</li>
<li>Desarrollo
<ul><li>Estudio de Viabilidad (EVS)</li>
<li>Análisis (ASI)</li>
<li>Diseño (DSI)</li>
<li>Construcción (CSI)</li>
<li>Implantación y Aceptación (IAS)</li>
</ul></li>
<li>Mantenimiento (MSI)</li>
</ul><p>Las interfaces son las siguientes:</p>
<ul><li>Gestión de la Configuración.</li>
<li>Aseguramiento de la Calidad.</li>
<li>Gestión de Proyectos.</li>
<li>Seguridad.</li>
</ul><p><img src="https://gsitic.files.wordpress.com/2018/04/metrica_v3.png?w=825"/></p>
<h3>Planificación de Sistemas de Información (PSI)</h3>
<p><strong>Descripción y Objetivos</strong></p>
<p>El Plan de Sistemas de Información tiene como objetivo la obtención de un marco de referencia para el desarrollo de sistemas de información que responda a los objetivos estratégicos de la organización. Este marco de referencia consta de:</p>
<ul><li>Una descripción de la situación actual, que constituirá el punto de partida del Plan de Sistemas de Información. Dicha descripción incluirá un análisis técnico de puntos fuertes y riesgos, así como el análisis de servicio a los objetivos de la organización.</li>
<li>Un conjunto de modelos que constituya la arquitectura de información.</li>
<li>Una propuesta de proyectos a desarrollar en los próximos años, así como la prioridad de realización de cada proyecto.</li>
<li>Una propuesta de calendario para la ejecución de dichos proyectos.</li>
<li>La evaluación de los recursos necesarios para los proyectos a desarrollar en el próximo año, con el objetivo de tenerlos en cuenta en los presupuestos. Para el resto de proyectos, bastará con una estimación de alto nivel.</li>
<li>Un plan de seguimiento y cumplimiento de todo lo propuesto mediante unos mecanismos de evaluación adecuados.</li>
</ul><p>La perspectiva del plan debe ser estratégica y operativa, no tecnológica.</p>
<p>Es fundamental que la alta dirección de la organización tome parte activa en la decisión del Plan de Sistemas de Información con el fin de posibilitar su éxito. La dirección debe convencer a sus colaboradores más directos de la necesidad de realización del plan; de su apoyo de forma constructiva, mentalizándose de que la ejecución del mismo requerirá la utilización de unos recursos de los cuales son responsables.</p>
<p>La presentación del Plan de Sistemas de Información y la constitución del equipo supone el arranque del proyecto y es fundamental que las más altas instancias de la organización estén implicadas en ambos, dando el apoyo necesario y aportando todo tipo de medios. Explicar el plan a las personas de la organización y a las unidades organizativas afectadas sobre las que recaerá el Plan, el apoyo de los altos directivos y la calificación de los recursos de las distintas unidades implicadas, serán factores críticos de éxito del Plan de Sistemas de Información.</p>
<p>El nivel de detalle con el que se hará el estudio de la situación actual dependerá de la existencia de documentación actual, de si hay personas que conozcan dicha documentación y de la predisposición a una sustitución total o parcial por sistemas de información nuevos. En cualquier caso, como paso previo para detectar aspectos importantes que puedan afectar a la organización, es necesario investigar sus puntos fuertes, áreas de mejora, riesgos y amenazas posibles y hacer un diagnóstico de los mismos.</p>
<p>Para la elaboración del Plan de Sistemas de Información se estudian las necesidades de información de los procesos de la organización afectados por el Plan, con el fin de definir los requisitos generales y obtener modelos conceptuales de información. Por otra parte se evalúan las opciones tecnológicas y se propone un entorno.</p>
<p>Tras analizar las prioridades relacionadas con las distintas variables que afectan a los sistemas de información, se elabora un calendario de proyectos con una planificación lo más detallada posible de los más inmediatos. Además, se propone una sistemática para mantener actualizado el Plan de Sistemas de Información para incluir en él todos los cambios necesarios, garantizando el cumplimiento adecuado del mismo.</p>
<p>A continuación se incluye un gráfico que representa la secuencia de actividades del proceso PSI.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/procesos_psi.png?w=825"/></p>
<p>Aunque los resultados de la actividad <em>Estudio de Información Relevante (PSI 3)</em> deberán tenerse en cuenta para la definición de requisitos que se efectúa en la actividad Identificación de Requisitos (PSI <em>4),</em> ambas podrán realizarse en paralelo, junto con el <em>Estudio de los Sistemas de Información Actuales (PSI 5)</em>.</p>
<p><strong>Actividad PSI 1: Inicio del Plan de Sistemas de Información</strong></p>
<p>El objetivo de esta actividad es determinar la necesidad del Plan de Sistemas de Información y llevar a cabo el arranque formal del mismo, con el apoyo del nivel más alto de la organización. Como resultado, se obtiene una descripción general del Plan de Sistemas de Información que proporciona una definición inicial del mismo, identificando los objetivos estratégicos en los que apoya, así como el ámbito general de la organización al que afecta, lo que permite implicar a las direcciones de las áreas afectadas por el Plan de Sistemas de Información. Además, se identifican los factores críticos de éxito y los participantes en el Plan de Sistemas de Información, nombrando a los máximos responsables.</p>
<p>A continuación se incluye una table resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/psi1.png?w=825"/></p>
<p><strong>Actividad PSI 2: Definición y Organización del PSI</strong></p>
<p>En esta actividad se detalla el alcance del plan, se organiza el equipo de personas que lo va a llevar a cabo y se elabora un calendario de ejecución. Todos los resultados o productos de esta actividad constituirán un marco de actuación del proyecto más detallado que en PSI 1 en cuanto a objetivos, procesos afectados, participantes, resultados y fechas de entrega.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/psi2.png?w=825"/></p>
<p><strong>Actividad PSI 3: Estudio de la Información Relevante</strong></p>
<p>El objetivo de esta actividad es recopilar y analizar todos los antecedentes generales que puedan afectar a los procesos y a las unidades organizativas implicadas en el Plan de Sistemas de Información, así como a los resultados del mismo. Pueden ser de especial interés los estudios realizados con anterioridad al Plan de Sistemas de Información, relativos a los sistemas de información de su ámbito, o bien a su entorno tecnológico, cuyas conclusiones deben ser conocidas por el equipo de trabajo del Plan de Sistemas de Información.</p>
<p>La información obtenida en esta actividad se tendrá en cuenta en la elaboración de los requisitos.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/psi3.png?w=825"/></p>
<p><strong>Actividad PSI 4: Identificación de Requisitos</strong></p>
<p>El objetivo final de esta actividad va a ser la especificación de los requisitos de información de la organización, así como obtener un modelo de información que los complemente. Para conseguir este objetivo, se estudia el proceso o procesos de la organización incluidos en el ámbito del Plan de Sistemas de Información. Para ello es necesario llevar a cabo sesiones de trabajo con los usuarios, analizando cada proceso tal y como debería ser, y no según su situación actual, ya que ésta puede estar condicionada por los sistemas de información existentes.</p>
<p>Del mismo modo, se identifican los requisitos de información, y se elabora un modelo de información que represente las distintas entidades implicadas en el proceso, así como las relaciones entre ellas. Por último, se clasifican los requisitos identificados según su prioridad, con el objetivo de incorporarlos al catálogo de requisitos del Plan de Sistemas de Información.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/psi4.png?w=825"/></p>
<p><strong>Actividad PSI 5: Estudio de los Sistemas de Información Actuales</strong></p>
<p>El objetivo de esta actividad es obtener una valoración de la situación actual al margen de los requisitos del catálogo, apoyándose en criterios relativos a facilidad de mantenimiento, documentación, flexibilidad, facilidad de uso, etc. En esta actividad se debe tener en cuenta la opinión de los usuarios, ya que aportarán elementos de valoración, como por ejemplo, su nivel de satisfacción con cada sistema de información. Se seleccionan los sistemas de información actuales que son objeto del análisis y se lleva a cabo el estudio de los mismos con la profundidad y el detalle que se determine conveniente en función de los objetivos definidos para el Plan de Sistemas de Información. Este estudio permite, para cada sistema, determinar sus carencias y valorarlos.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/psi5.png?w=825"/></p>
<p><strong>Actividad PSI 6: Diseño del Modelo de Sistemas de Información</strong></p>
<p>El objetivo de esta actividad es identificar y definir los sistemas de información que van a dar soporte a los procesos de la organización afectados por el Plan de Sistemas de Información. Para ello, en primer lugar, se analiza la cobertura que los sistemas de información actuales dan a los requisitos recogidos en el catálogo elaborado en las actividades Estudio de la Información Relevante (PSI 3) e Identificación de Requisitos (PSI 4). Esto permitirá efectuar un diagnóstico de la situación actual, a partir del cual se seleccionan los sistemas de información actuales considerados válidos, identificando las mejoras a realizar en los mismos. Por último, se definen los nuevos sistemas de información necesarios para cubrir los requisitos y funciones de los procesos no soportados por los sistemas actuales seleccionados. Teniendo en cuenta los resultados anteriores, se elabora el modelo de sistemas de información válido para dar soporte a los procesos de la organización incluidos en el ámbito del Plan de Sistemas de Información.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/psi6.png?w=825"/></p>
<p><strong>Actividad PSI 7: Definición de la Arquitectura Tecnológica</strong></p>
<p>En esta actividad se propone una arquitectura tecnológica que dé soporte al modelo de información y de sistemas de información incluyendo, si es necesario, opciones. Para esta actividad se tienen en cuenta especialmente los requisitos de carácter tecnológico, aunque es necesario considerar el catálogo completo de requisitos para entender las necesidades de los procesos y proponer los entornos tecnológicos que mejor se adapten a las mismas.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/psi7.png?w=825"/></p>
<p><strong>Actividad PSI 8: Definición del Plan de Acción</strong></p>
<p>En el Plan de Acción, que se elabora en esta actividad, se definen los proyectos y acciones a llevar a cabo para la implantación de los modelos de información y de sistemas de información, determinados en las actividades Identificación de Requisitos (PSI 4) y Diseño del Modelo de Sistemas de Información (PSI 6), con la arquitectura tecnológica propuesta en la actividad Definición de la Arquitectura Tecnológica (PSI 7), el conjunto de estos tres modelos constituye la arquitectura de información. Dentro del Plan de Acción se incluye un calendario de proyectos, con posibles alternativas, y una estimación de recursos, cuyo detalle será mayor para los más inmediatos. Para la elaboración del calendario se tienen que analizar las distintas variables que afecten a la prioridad de cada proyecto y sistema de información. El orden definitivo de los proyectos y acciones debe pactarse con los usuarios, para llegar a una solución de compromiso que resulte la mejor posible para la organización. Por último, se propone un plan de mantenimiento para el control y seguimiento de la ejecución de los proyectos, así como para la actualización de los productos finales del Plan de Sistemas de Información.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/psi8.png?w=825"/></p>
<p><strong>Actividad PSI 9: Revisión y Aprobación del PSI</strong></p>
<p>Esta actividad tiene como objetivo contrastar con los responsables de la dirección del Plan de Sistemas de Información la arquitectura de información y el plan de acción elaborados anteriormente, para mejorar la propuesta si se considera necesario y por último, obtener su aprobación final.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/psi9.png?w=825"/></p>
<h3>Estudio de Viabilidad del Sistema (EVS)</h3>
<p><strong>Descripción y Objetivos</strong></p>
<p>Mientras que el Plan de Sistemas de Información tiene como objetivo proporcionar un marco estratégico que sirva de referencia para los Sistemas de Información de un ámbito concreto de una organización, el objetivo del Estudio de Viabilidad del Sistema es el análisis de un conjunto concreto de necesidades para proponer una solución a corto plazo, que tenga en cuenta restricciones económica, técnicas, legales y operativas. Las solución obtenida como resultado del estudio puede ser la definición de uno o varios proyectos que afecten a uno o varios sistemas de información y a existentes o nuevos. Para ello, se identifican los requisitos que se ha de satisfacer y se estudia, si procede, la situación actual.</p>
<p>A partir del estado inicial, la situación actual y los requisitos planteados, se estudian las alternativas de solución. Dichas alternativas pueden incluir soluciones que impliquen desarrollos a medida, soluciones basadas en la adquisición de productos software del mercado o soluciones mixtas. Se describe cada una de las alternativas, indicando los requisitos que cubre.</p>
<p>Una vez descritas cada una de las alternativas planteadas, se valora su impacto en la organización, la inversión a realizar en cada caso y los riesgos asociados. Esta información se analiza con el fin de evaluar las distintas alternativas y seleccionar la más adecuada, definiendo y estableciendo su planificación. Si en la organización se ha realizado con anterioridad un Plan de Sistemas de Información que afecte al sistema objeto de este estudio, se dispondrá de un conjunto de productos que proporcionarán información a tener en cuenta en todo el proceso.</p>
<p>Las actividades que engloba este proceso se recogen en la siguiente figura, en la que se indican las actividades que pueden ejecutarse en paralelo y las que precisan para su realización resultados originados en actividades anteriores.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/evs.png?w=825"/></p>
<p><strong>Actividad EVS 1: Establecimiento del Alcance del Sistema</strong></p>
<p>En esta actividad se estudia el alcance de la necesidad planteada por el cliente o usuario, o como consecuencia de la realización de un PSI, realizando una descripción general de la misma. Se determinarán los objetivos, se inicia el estudio de los requisitos y se identifican las unidades organizativas afectadas estableciendo su estructura.</p>
<p>Se analizan las posibles restricciones, tanto generales como específica, que puedan condicionar el estudio y la planificación de las alternativas de solución que se propongan. Si la justificación económica es obvia, el riesgo técnico bajo, se esperan pocos problemas legales y no existe ninguna alternativa razonable, no es necesario profundizar en el estudio de viabilidad del sistema, analizando posibles alternativas y realizando una valoración y evaluación de las mismas, sino que éste se orientará a la especificación de requisitos, descripción del nuevo sistema y planificación. Se detalla la composición del equipo de trabajo necesario para este proceso y su planificación. Finalmente, con el fin de facilitar la implicación activa de los usuarios en la definición del sistema, se identifican sus perfiles, dejando claras sus tareas y responsabilidades.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/evs1.png?w=825"/></p>
<p><strong>Actividad EVS 2: Estudio de la Situación Actual</strong></p>
<p>La situación actual es el estado en el que se encuentran los sistemas de información existentes en el momento en el que se inicia su estudio. Teniendo en cuenta el objetivo del estudio de la situación actual, se realiza una valoración de la información existente acerca de los sistemas de información afectados. En función de dicha valoración, se especifica el nivel de detalle con que se debe llevar a cabo el estudio. Si es necesario, se constituye un equipo de trabajo específico para su realización y se identifican los usuarios participantes en el mismo.</p>
<p>Si se decide documentar la situación actual, normalmente es conveniente dividir el sistema actual en subsistemas. Si es posible se describirá cada uno de los subsistemas, valorando qué información puede ser relevante para la descripción. Como resultado de esta actividad se genera un diagnóstico, estimando la eficiencia de los sistemas de información existentes e identificando los posibles problemas y las mejoras.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/evs2.png?w=825"/></p>
<p><strong>Actividad EVS 3: Definición de Requisitos del Sistema</strong></p>
<p>Esta actividad incluye la determinación de los requisitos generales, mediante una serie de sesiones de trabajo con los usuarios participantes, que hay que planificar y realizar. Una vez finalizadas, se analiza la información obtenida definiendo los requisitos y sus prioridades, que se añaden al catálogo de requisitos que servirá para el estudio y valoración de las distintas alternativas de solución que se propongan.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/evs3.png?w=825"/></p>
<p><strong>Actividad EVS 4: Estudio de Alternativas de Solución</strong></p>
<p>Este estudio se centra en proponer diversas alternativas que respondan satisfactoriamente a los requisitos planteados, considerando también los resultado obtenidos en el Estudio de la Situación Actual (EVS 2), en el caso de que se haya realizado. Teniendo en cuenta el ámbito y funcionalidad que debe cubrir el sistema, puede ser conveniente realizar, previamente a la definición de cada alternativa, una descomposición del sistema en subsistemas. En la descripción de las distintas alternativas de solución propuestas, se debe especificar si alguna de ellas está basada, total o parcialmente, en un producto existente en el mercado. Si la alternativa incluye un desarrollo a medida, se debe incorporar en la descripción de la misma un modelo abstracto de datos y un modelo de procesos, y en orientación a objetos, un modelo de negocio y un modelo de dominio.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/evs4.png?w=825"/></p>
<p><strong>Actividad EVS 5: Valoración de las Alternativas</strong></p>
<p>Una vez descritas las alternativas se realiza una valoración de las mismas, considerando el impacto en la organización, tanto desde el punto de vista tecnológico y organizativo como de operación, y los posibles beneficios que se esperan contrastados con los costes asociados. Se realiza también un análisis de los riesgos, decidiendo cómo enfocar el plan de acción para minimizar los mismos y cuantificando los recursos y plazos precisos para planificar cada alternativa.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/evs5.png?w=825"/></p>
<p><strong>Actividad EVS 6: Selección de la Solución</strong></p>
<p>Antes de finalizar el Estudio de Viabilidad del Sistema, se convoca al Comité de Dirección para la presentación de las distintas alternativas de solución, resultantes de la actividad anterior. En dicha presentación, se debaten las ventajas de cada una de ellas, incorporando las modificaciones que se consideren oportunas, con el fin de seleccionar la más adecuada. Finalmente, se aprueba la solución o se determina su inviabilidad.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/evs6.png?w=825"/></p>
<h3>Análisis del Sistema de Información (ASI)</h3>
<p><strong>Descripción y Objetivos</strong></p>
<p>El objetivo de este proceso es la obtención de una especificación detallada del sistema de información que satisfaga las necesidades de información de los usuarios y sirva de base para el posterior diseño del sistema. Al ser MÉTRICA Versión 3 una metodología que cubre tanto desarrollos estructurados como orientados a objetos, las actividades de ambas aproximaciones están integradas en una estructura común.</p>
<p>En la primera actividad, Definición del Sistema (ASI 1), se lleva a cabo la descripción inicial del sistema de información, a partir de los productos generados en el proceso Estudio de Viabilidad del Sistema (EVS). Se delimita el alcance del sistema, se genera un catálogo de requisitos generales y se describe el sistema mediante unos modelos iniciales de alto nivel. También se identifican los usuarios que participan en el proceso de análisis, determinando sus perfiles, responsabilidades y dedicaciones necesarias. Así mismo se elabora el plan de trabajo a seguir.</p>
<p>La definición de requisitos del nuevo sistema se realiza principalmente en la actividad. Establecimiento de Requisitos (ASI 2). El objetivo de esta actividad es elaborar un catálogo de requisitos detallado, que permita describir con precisión el sistema de información, y que además sirva de base para comprobar que es completa la especificación de los modelos obtenidos en las actividades Identificación de Subsistemas de Análisis (ASI 3), Análisis de Casos de Uso (ASI 4), Análisis de Clases (ASI 5), Elaboración del Modelo de Datos (ASI 6), Elaboración del Modelo de Procesos (ASI 7) y Definición de Interfaces de Usuario (ASI 8).</p>
<p>Hay que hacer constar que estas actividades pueden provocar la actualización del catálogo, aunque no se refleja como producto de salida en las tareas de dichas actividades, ya que el objetivo de las mismas no es crear el catálogo sino definir modelos que soporten los requisitos.</p>
<p>Para la obtención de requisitos en la actividad Establecimiento de Requisitos (ASI 2) se toman como punto de partida el catálogo de requisitos y los modelos elaborados en la actividad Definición del Sistema (ASI 1), completándolos mediante sesiones de trabajo con los usuarios. Estas sesiones de trabajo tienen como objetivo reunir la información necesaria para obtener la especificación detallada del nuevo sistema. Las técnicas que ayudan a la recopilación de esta información pueden variar en función de las características del proyecto y los tipos de usuario a entrevistar. Entre ellas podemos citar la reuniones, entrevistas, <em>Join Application Design (JAD)</em>, etc.&nbsp; Durante estas sesiones de trabajo se propone utilizar la especificación de los casos de uso como ayuda y guía en el establecimiento de requisitos. Esta técnica facilita la comunicación con los usuarios y en el análisis orientado a objetos constituye la base de la especificación. A continuación se identifican las facilidades que ha de proporcionar el sistema, y las restricciones a que está sometido en cuanto a rendimiento, frecuencia de tratamiento, seguridad y control de accesos, etc. Toda esta información se incorpora al catálogo de requisitos.</p>
<p>En la actividad Identificación de Subsistemas de Análisis (ASI 3), se estructura el sistema de información en subsistemas de análisis, para facilitar la especificación de los distintos modelos y la traza de requisitos. En paralelo, se generan los distintos modelos que sirven de base para el diseño. En el caso de análisis estructurado, se procede a la elaboración y descripción detallada del modelo de datos y de procesos, y en el caso de un análisis orientado a objetos, se elaboran el modelo de clases y el de interacción de objetos, mediante el análisis de los casos de uso. Se especifican, asimismo, todas las interfaces entre el sistema y el usuario, tales como formatos de pantallas, diálogos, formatos de informes y formularios de entrada.</p>
<p>En la actividad Análisis de Consistencia y Especificación de Requisitos (ASI 9), se realiza la verificación y validación de los modelos, con el fin de asegurar que son:</p>
<ul><li>Completos, puesto que cada modelo obtenido contiene toda la información necesaria recogida en el catálogo de requisitos.</li>
<li>Consistentes, ya que cada modelo es coherente con el resto de los modelos.</li>
<li>Correctos, dado que cada modelo sigue unos criterios de calidad predeterminados en relación a la técnica utilizada, calidad de diagramas, elección de nombre, normas de calidad, etc.</li>
</ul><p>En la actividad Especificación del Plan de Pruebas (ASI 10), se establece el marco general del plan de pruebas, iniciándose su especificación, que se completará en el proceso Diseño del Sistema de Información (DSI).</p>
<p>La participación activa de los usuarios es una condición imprescindible para el análisis del sistema de información, ya que dicha participación constituye una garantía de que los requisitos identificados son comprendidos e incorporados al sistema y, por tanto, de que éste será aceptado. Para facilitar la colaboración de los usuarios, se pueden utilizar técnicas interactivas, como diseño de diálogos y prototipos, que permiten al usuario familiarizarse con el nuevo sistema y colaborar en la construcción y perfeccionamiento del mismo. En el siguiente gráfico se muestra la relación de actividades del proceso Análisis del Sistema de Información, tanto para desarrollos estructurados como para desarrollos orientados a objetos, distinguiendo las que se pueden realizar en paralelo de aquellas que han de realizarse secuencialmente.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/asi.png?w=825"/></p>
<p><strong>Actividad ASI 1: Definición del Sistema</strong></p>
<p>Esta actividad tiene como objetivo efectuar una descripción del sistema, delimitando su alcance, estableciendo las interfaces con otros sistemas e identificando a los usuarios representativos. Las tareas de esta actividad se pueden haber desarrollado ya en parte en el proceso de Estudio de Viabilidad del Sistema (EVS), de modo que se parte de los productos obtenidos en dicho proceso para proceder a su adecuación como punto de partida para definir el sistema de información.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/asi1.png?w=825"/></p>
<p><strong>Actividad ASI 2: Establecimiento de Requisitos</strong></p>
<p>En esta actividad se lleva a cabo la definición, análisis y validación de los requisitos a partir de la información facilitada por el usuario, completándose el catálogo de requisitos obtenido en la actividad Definición del Sistema (ASI 1). El objetivo de esta actividad es obtener un catálogo detallado de los requisitos, a partir del cual se pueda comprobar que los productos generados en las actividades de modelización se ajustan a los requisitos de usuario.</p>
<p>Esta actividad se descompone en un conjunto de tareas que, si bien tienen un orden, exige continuas realimentaciones y solapamientos, entre sí y con otras tareas realizadas en paralelo. No es necesaria la finalización de una tarea para el comienzo de la siguiente. Lo que se tiene en un momento determinado es un catálogo de requisitos especificado en función de la progresión del proceso de análisis.</p>
<p>Se propone como técnica de obtención de requisitos la especificación de los casos de uso de la orientación a objetos, siendo opcional en el caso estructurado. Dicha técnica ofrece un diagrama simple y una guía de especificación en las sesiones de trabajo con el usuario.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/asi2.png?w=825"/></p>
<p><strong>Actividad DSI 3: Identificación de Subsistemas de Análisis</strong></p>
<p>El objetivo de esta actividad, común tanto para análisis estructurado como para análisis orientado a objetos, es facilitar el análisis del sistema de información llevando a cabo la descomposición del sistema en subsistemas. Se realiza en paralelo con el resto de las actividades de generación de modelos del análisis. Por tanto, se asume la necesidad de una realimentación y ajuste continuo con respecto a la definición de los subsistemas, sus dependencias y sus interfaces.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/asi3.png?w=825"/></p>
<p><strong>Actividad ASI 4: Análisis de los Casos de Uso</strong></p>
<p>El objetivo de esta actividad, que sólo se realiza en el caso de <strong>Análisis Orientado a Objetos</strong>, es identificar las clases cuyos objetos son necesarios para realizar un caso de uso y describir su comportamiento mediante la interacción de dichos objetos. Esta actividad se lleva a cabo para cada uno de los casos de uso contenidos en un subsistema de los definidos en la actividad Identificación de Subsistemas de Análisis (ASI 3).</p>
<p>Las tareas de esta actividad no se realizan de forma secuencial sino en paralelo, con continuas realimentaciones entre ellas y con las realizadas en las actividades Establecimiento de Requisitos (ASI 2), Identificación de Subsistemas de Análisis (ASI 3), Análisis de Clases (ASI 5) y Definición de Interfaces de Usuario (ASI 8).</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/asi4.png?w=825"/></p>
<p><strong>Actividad ASI 5: Análisis de Clases</strong></p>
<p>El objetivo de esta actividad que sólo se realiza en el caso de <strong>Análisis Orientado a Objetos</strong> es describir cada una de las clases que ha surgido, identificando las responsabilidades que tienen asociadas, sus atributos, y las relaciones entre ellas. Para esto, se debe tener en cuenta la normativa establecida en la tarea Especificación de Estándares y Normas (ASI 1.3), de forma que el modelo de clases cumpla estos criterios, con el fin de evitar posibles inconsistencias en el diseño. Teniendo en cuenta las clases identificadas en la actividad Análisis de los Casos de Uso (ASI 4), se elabora el modelo de clases para cada subsistema. A medida que avanza el análisis, dicho modelo se va completando con las clases que vayan apareciendo, tanto del estudio de los casos de uso, como de la interfaz de usuario necesaria para el sistema de información.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/asi5.png?w=825"/></p>
<p><strong>Actividad ASI 6: Elaboración del Modelo de Datos</strong></p>
<p>El objetivo de esta actividad que se lleva a cabo únicamente en el caso de <strong>Análisis Estructurado</strong> es identificar las necesidades de información de cada uno de los procesos que conforman el sistema de información, con el fin de obtener un modelo de datos que contemple todas las entidades, relaciones, atributos y reglas de negocio necesarias para dar respuesta a dichas necesidades.</p>
<p>El modelo de datos se elabora siguiendo un enfoque descendente (<em>top-down</em>). A partir del modelo conceptual de datos, obtenido en la tarea Determinación del Alcance del Sistema (ASI 1.1), se incorporan a dicho modelo todas las entidades que vayan apareciendo, como resultado de las funcionalidades que se deban cubrir y de las necesidades de información del usuario. Es necesario tener en cuenta el catálogo de requisitos y el modelo de procesos, productos que se están generando en paralelo en las actividades Establecimiento de Requisitos (ASI 2), Identificación de Subsistemas de Análisis (ASI 3) y Elaboración del Modelo de Procesos (ASI 7). Una vez construido el modelo conceptual y definidas sus entidades, se resuelven las relaciones complejas y se completa la información de entidades, relaciones, atributos y ocurrencias de las entidades, generando el modelo lógico de datos. Como última tarea en la definición del modelo, se asegura la normalización hasta la tercera forma normal para obtener el modelo lógico de datos normalizado. Finalmente, si procede, se describen las necesidades de migración y carga inicial de los datos.</p>
<p>Esta actividad se realiza en paralelo, y con continuas realimentaciones, con otras tareas realizadas en las actividades Establecimiento de Requisitos (ASI 2), Identificación de Subsistemas de Análisis (ASI 3), Elaboración del Modelo de Procesos (ASI 7) y Definición de Interfaces de Usuario (ASI 8).</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/asi6.png?w=825"/></p>
<p><strong>Actividad ASI 7: Elaboración del Modelo de Procesos</strong></p>
<p>El objetivo de esta actividad, que se lleva a cabo únicamente en el caso de <strong>Análisis Estructurado</strong>, es analizar las necesidades del usuario para establecer el conjunto de procesos que conforma el sistema de información. Para ello, se realiza una descomposición de dichos procesos siguiendo un enfoque descendente (<em>top-down</em>), en varios niveles de abstracción, donde cada nivel proporciona una visión más detallada del proceso definido en el nivel anterior. Con el fin de facilitar el desarrollo posterior, se debe llegar a un nivel de descomposición en el que los procesos obtenidos sean claros y sencillos, es decir, buscar un punto de equilibrio en el que dichos procesos tengan significado por sí mismos dentro del sistema global y a su vez la máxima independencia y simplicidad.</p>
<p>Esta actividad se lleva a cabo para cada uno de los subsistemas identificados en la actividad Identificación de Subsistemas de Análisis (ASI 3). Las tareas de esta actividad se realizan en paralelo y con continuas realimentaciones con otras tareas ejecutadas en las actividades Establecimiento de Requisitos (ASI 2), Elaboración del Modelo de Datos (ASI 6) y Definición de Interfaces de Usuario (ASI 8).</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/asi7.png?w=825"/></p>
<p><strong>Actividad ASI 8: Definición de Interfaces de usuario</strong></p>
<p>En esta actividad se especifican las interfaces entre el sistema y el usuario: formatos de pantallas, diálogos, e informes, principalmente. El objetivo es realizar un análisis de los procesos del sistema de información en los que se requiere una interacción del usuario, con el fin de crear una interfaz que satisfaga todos los requisitos establecidos, teniendo en cuenta los diferentes perfiles a quiénes va dirigido. Al comienzo de este análisis es necesario seleccionar el entorno en el que es operativa la interfaz, considerando estándares internacionales y de la instalación, y establecer las directrices aplicables en los procesos de diseño y construcción. El propósito es construir una interfaz de usuario acorde a sus necesidades, flexible, coherente, eficiente y sencilla de utilizar, teniendo en cuenta la facilidad de cambio a otras plataformas, si fuera necesario. Se identifican los distintos grupos de usuarios de acuerdo con las funciones que realizan, conocimientos y habilidades que poseen, y características del entorno en el que trabajan. La identificación de los diferentes perfiles permite conocer mejor las necesidades y particularidades de cada uno de ellos.</p>
<p>Asimismo, se determina la naturaleza de los procesos que se llevan a cabo (en lotes o en línea). Para cada proceso en línea se especifica qué tipo de información requiere el usuario para completar su ejecución realizando, para ello, una descomposición en diálogos que refleje la secuencia de la interfaz de pantalla tipo carácter o pantalla gráfica. Finalmente, se define el formato y contenido de cada una de las interfaces de pantalla especificando su comportamiento dinámico. Se propone un flujo de trabajo muy similar para desarrollos estructurados y orientados a objetos, coincidiendo en la mayoría de las tareas, si bien es cierto que en orientación a objetos, al identificar y describir cada escenario en la especificación de los casos de uso, se hace un avance muy significativo en la toma de datos para la posterior definición de la interfaz de usuario. Como resultado de esta actividad se genera la especificación de interfaz de usuario, como producto que engloba los siguientes elementos:</p>
<ul><li>Principios generales de la interfaz.</li>
<li>Catálogo de perfiles de usuario.</li>
<li>Descomposición funcional en diálogos.</li>
<li>Catálogo de controles y elementos de diseño de interfaz de pantalla.</li>
<li>Formatos individuales de interfaz de pantalla.</li>
<li>Modelo de navegación de interfaz de pantalla.</li>
<li>Formatos de impresión.</li>
<li>Prototipo de interfaz interactiva.</li>
<li>Prototipo de interfaz de impresión.</li>
</ul><p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/asi8.png?w=825"/></p>
<p><strong>Actividad ASI 9: Análisis de Consistencia y Especificación de Requisitos</strong></p>
<p>El objetivo de esta actividad es garantizar la calidad de los distintos modelos generados en el proceso de Análisis del Sistema de Información, y asegurar que los usuarios y los Analistas tienen el mismo concepto del sistema.</p>
<p>Para cumplir dicho objetivo, se llevan a cabo las siguientes acciones:</p>
<ul><li>Verificación de la calidad técnica de cada modelo.</li>
<li>Aseguramiento de la coherencia entre los distintos modelos.</li>
<li>Validación del cumplimiento de los requisitos.</li>
</ul><p>Esta actividad requiere una herramienta de apoyo para realizar el análisis de consistencia. También se elabora en esta actividad la Especificación de Requisitos Software (ERS), como producto para la aprobación formal, por parte del usuario, de las especificaciones del sistema. La Especificación de Requisitos Software se convierte en la línea base para los procesos posteriores del desarrollo del software, de modo que cualquier petición de cambio en los requisitos que pueda surgir posteriormente, debe ser evaluada y aprobada.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/asi9-1.png?w=825"/><img src="https://gsitic.files.wordpress.com/2018/04/asi9-2.png?w=825"/></p>
<p><strong>Actividad ASI 10: Especificación del Plan de Pruebas</strong></p>
<p>En esta actividad se inicia la definición del plan de pruebas, el cual sirve como guía para la realización de las pruebas, y permite verificar que el sistema de información cumple las necesidades establecidas por el usuario, con las debidas garantías de calidad. El plan de pruebas es un producto formal que define los objetivos de la prueba de un sistema, establece y coordina una estrategia de trabajo, y provee del marco adecuado para elaborar una planificación paso a paso de las actividades de prueba. El plan se inicia en el proceso Análisis del Sistema de Información (ASI), definiendo el marco general, y estableciendo los requisitos de prueba de aceptación, relacionados directamente con la especificación de requisitos.</p>
<p>Dicho plan se va completando y detallando a medida que se avanza en los restantes procesos del ciclo de vida del software, Diseño del Sistema de Información (DSI), Construcción del Sistema de Información (CSI) e Implantación y Aceptación del Sistema (IAS). Se plantean los siguientes niveles de prueba:</p>
<ul><li>Pruebas unitarias.</li>
<li>Pruebas de integración.</li>
<li>Pruebas del sistema.</li>
<li>Pruebas de implantación.</li>
<li>Pruebas de aceptación.</li>
</ul><p>En esta actividad también se avanza en la definición de las pruebas de aceptación del sistema. Con la información disponible, es posible establecer los criterios de aceptación de las pruebas incluidas en dicho nivel, al poseer la información sobre los requisitos que debe cumplir el sistema, recogidos en el catálogo de requisitos.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/asi10.png?w=825"/></p>
<p><strong>Actividad ASI 11: Aprobación del Análisis del Sistema de Información</strong></p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/asi11.png?w=825"/></p>
<h3>Diseño del Sistema de Información (DSI)</h3>
<p><strong>Descripción y Objetivos</strong></p>
<p>El objetivo del proceso de Diseño del Sistema de Información (DSI) es la definición de la arquitectura del sistema y del entorno tecnológico que le va a dar soporte, junto con la especificación detallada de los componentes del sistema de información. A partir de dicha información, se generan todas las especificaciones de construcción relativas al propio sistema, así como la descripción técnica del plan de pruebas, la definición de los requisitos de implantación y el diseño de los procedimientos de migración y carga inicial, éstos últimos cuando proceda.</p>
<p>Al ser MÉTRICA Versión 3 una metodología que cubre tanto desarrollos estructurados como orientados a objetos, las actividades de ambas aproximaciones están integradas en una estructura común. Las actividades de este proceso se agrupan en dos grandes bloques:</p>
<ul><li>En un primer bloque de actividades, que se llevan a cabo en paralelo, se obtiene el diseño de detalle del sistema de información. La realización de estas actividades exige una continua realimentación. En general, el orden real de ejecución de las mismas depende de las particularidades del sistema de información y, por lo tanto, de generación de sus productos.<br/>
En la actividad Definición de la Arquitectura del Sistema (DSI 1), se establece el particionamiento físico del sistema de información, así como su organización en subsistemas de diseño, la especificación del entorno tecnológico, y sus requisitos de operación, administración, seguridad y control de acceso. Se completan los catálogos de requisitos y normas, en función de la definición del entorno tecnológico, con aquellos aspectos relativos al diseño y construcción que sea necesario contemplar. Asimismo, se crea un catálogo de excepciones del sistema, en el que se registran las situaciones de funcionamiento secundario o anómalo que se estime oportuno considerar y, por lo tanto, diseñar y probar. Este catálogo de excepciones se utiliza como referencia en la especificación técnica de las pruebas del sistema.<br/>
El particionamiento físico del sistema de información permite organizar un diseño que contemple un sistema de información distribuido, como por ejemplo la arquitectura cliente/servidor, siendo aplicable a arquitecturas multinivel en general. Independientemente de la infraestructura tecnológica, dicho particionamiento representa los distintos niveles funcionales o físicos del sistema de información. La relación entre los elementos del diseño y particionamiento físico, y a su vez, entre el particionamiento físico y el entorno tecnológico, permite una especificación de la distribución de los elementos del sistema de información y, al mismo tiempo, un diseño orientado a la movilidad a otras plataformas o la reubicación de subsistemas.<br/>
El sistema de información se estructura en subsitemas de diseño. Éstos a su vez se clasifican como de soporte o específicos, al responder a propósitos diferentes.
<ul><li>Los subsistemas de soporte contienen los elementos o servicios comunes al sistema y a la instalación, y generalmente están originados por la interacción con la infraestructura técnica o la reutilización de otros sistemas, con un nivel de complejidad técnica mayor.</li>
<li>Los subsistemas específicos contienen los elementos propios del sistema de información, generalmente con una continuidad de los subsistemas definidos en el proceso de Análisis del Sistema de Información (ASI).</li>
</ul></li>
</ul><p>También se especifica en detalle el entorno tecnológico del sistema de información, junto con su planificación de capacidades (capacity planning), y sus requisitos de operación, administración, seguridad y control de acceso.<br/>
El diseño detallado del sistema de información, siguiendo un enfoque estructurado, comprende un conjunto de actividades que se llevan a cabo en paralelo a la Definición de la Arquitectura del Sistema (DSI 1). El alcance de cada una de estas actividades se resume a continuación:</p>
<p>* Diseño de la Arquitectura de Soporte (DSI 2), que incluye el diseño detallado de los subsistemas de soporte, el establecimiento de las normas y requisitos propios del diseño y construcción, así como la identificación y definición de los mecanismos genéricos de diseño y construcción.<br/>
* Diseño de la Arquitectura de Módulos del Sistema (DSI 5), donde se realiza el diseño de detalle de los subsistemas específicos del sistema de información y la revisión de la interfaz de usuario.<br/>
* Diseño Físico de Datos (DSI 6), que incluye el diseño y optimización de las estructuras de datos del sistema, así como su localización en los nodos de la arquitectura propuesta.</p>
<p>En el caso de Diseño Orientado a Objetos, conviene señalar que el diseño de la persistencia de los objetos se lleva a cabo sobre bases de datos relacionales, y que el diseño detallado del sistema de información se realiza en paralelo con la actividad de Diseño de la Arquitectura de Soporte (DSI 2), y se corresponde con las siguientes actividades:</p>
<p>* Diseño de Casos de Uso Reales (DSI 3), con el diseño detallado del comportamiento del sistema de información para los casos de uso, el diseño de la interfaz de usuario y la validación de la división en subsistemas.<br/>
* Diseño de Clases (DSI 4), con el diseño detallado de cada una de las clases que forman parte del sistema, sus atributos, operaciones, relaciones y métodos, y la estructura jerárquica del mismo. En el caso de que sea necesario, se realiza la definición de un plan de migración y carga inicial de datos.</p>
<p>Una vez que se tiene el modelo de clases, se comienza el diseño físico en la actividad Diseño Físico de Datos (DSI 6), común con el enfoque estructurado.<br/>
Una vez finalizado el diseño de detalle, se realiza su revisión y validación en la actividad Verificación y Aceptación de la Arquitectura del Sistema (DSI 7), con el objeto de analizar la consistencia entre los distintos modelos y conseguir la aceptación del diseño por parte de los responsables de las áreas de Explotación y Sistemas.</p>
<ul><li>El segundo bloque de actividades complementa el diseño del sistema de información. En él se generan todas las especificaciones necesarias para la construcción del sistema de información:
<ul><li>Generación de Especificaciones de construcción (DSI 8), fijando las directrices para la construcción de los componentes del sistema, así como de las estructuras de datos.</li>
<li>Diseño de la Migración y Carga Inicial de Datos (DSI 9), en el que se definen los procedimientos de migración y sus componentes asociados, con las especificaciones de construcción oportunas.</li>
<li>Especificación Técnica del Plan de Pruebas (DSI 10), que incluye la definición y revisión del plan de pruebas, y el diseño de las verificaciones de los niveles de prueba establecidos. El catálogo de excepciones permite, de una forma muy ágil, establecer un conjunto de verificaciones relacionadas con el propio diseño o con la arquitectura del sistema.</li>
<li>Establecimiento de Requisitos de Implantación (DSI 11), que hace posible concretar las exigencias relacionados con la propia implantación del sistema, tales como formación de usuarios finales, infraestructura, etc.</li>
</ul></li>
</ul><p>Finalmente, en la actividad de Presentación y Aprobación del Diseño del Sistema de Información (DSI 12), se realiza una presentación formal y aprobación de los distintos productos del diseño.</p>
<p>En el siguiente gráfico se muestra la relación de actividades del proceso Diseño del Sistema de Información (DSI), tanto para Desarrollos Estructurados como para Desarrollos Orientados a Objetos.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/dsi.png?w=825"/></p>
<p><strong>Actividad DSI 1: Definición de la Arquitectura del Sistema</strong></p>
<p>En esta actividad se define la arquitectura general del sistema de información, especificando las distintas particiones físicas del mismo, la descomposición lógica en subsistemas de diseño y la ubicación de cada subsistema en cada partición, así como la especificación detallada de la infraestructura tecnológica necesaria para dar soporte al sistema de información.</p>
<p>El particionamiento físico del sistema de información se especifica identificando los nodos y las comunicaciones entre los mismos, con cierta independencia de la infraestructura tecnológica que da soporte a cada nodo.</p>
<p>Con el fin de organizar y facilitar el diseño, se realiza una división del sistema de información en subsistemas de diseño, como partes lógicas coherentes y con interfaces claramente definidas. Se establece una distinción entre subsistemas específicos del sistema de información (en adelante, subsistemas específicos) y subsistemas de soporte, con la finalidad de independizar, en la medida de los posible, las funcionalidades a cubrir por el sistema de información de la infraestructura que le da soporte.</p>
<p>En la mayoría de los casos, los subsistemas específicos provienen directamente de las especificaciones de análisis y de los subsistemas de análisis, mientras que los subsistemas de soporte provienen de la necesidad de interacción del sistema de información con la infraestructura y con el resto de los sistemas, así como de la reutilización de módulos o subsistemas ya existentes en la instalación.</p>
<p>Debido a que la definición de los subsistemas de soporte puede exigir la participación de distintos perfiles técnicos, se propone el diseño de ambos tipos de subsistemas en actividades distintas, aunque en paralelo.</p>
<p>Una vez identificados y definidos los distintos subsistemas de diseño, se determina su ubicación óptima de acuerdo a la arquitectura propuesta. La asignación de dichos subsistemas a cada nodo permite disponer, en función de la carga de proceso y comunicación existente entre los nodos, de la información necesaria para realizar una estimación de las necesidades de infraestructura tecnológica que da soporte al sistema de información. Este factor es especialmente crítico en arquitecturas multinivel o cliente/servidor, donde las comunicaciones son determinantes en el rendimiento final del sistema. Se propone crear un catálogo de excepciones en el que se especifiquen las situaciones anómalas o secundarias en el funcionamiento y ejecución del sistema de información, y que se irá completando a medida que se avance en el diseño detallado de los subsistemas.</p>
<p>En esta actividad también se establecen los requisitos, normas y estándares originados como consecuencia de la adopción de una determinada solución de arquitectura o infraestructura, que serán aplicables tanto en este proceso como en la Construcción del Sistema de Información (CSI). Se detallan a su vez, de acuerdo a las particularidades de la arquitectura del sistema propuesta, los requisitos de operación, seguridad y control, especificando los procedimientos necesarios para su cumplimiento.</p>
<p>Como resultado de esta actividad, se actualizan los catálogos de requisitos y normas, y se generan los siguientes productos:</p>
<ul><li>Diseño de la Arquitectura del Sistema, como producto que engloba el particionamiento físico del sistema de información y la descripción de subsistemas de diseño.</li>
<li>Entorno Tecnológico del Sistema, que a su vez comprende la especificación del entorno tecnológico, las restricciones técnicas y la planificación de capacidades.</li>
<li>Catálogo de Excepciones.</li>
<li>Procedimientos de Operación y Administración del Sistema.</li>
<li>Procedimientos de Seguridad y Control de Acceso.</li>
</ul><p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/dsi1.png?w=825"/></p>
<p><strong>Actividad DSI 2: Diseño de la Arquitectura de Soporte</strong></p>
<p>En esta actividad se lleva a cabo la especificación de la arquitectura de soporte, que comprende el diseño de los subsistemas de soporte identificados en la actividad de Definición de la Arquitectura del Sistema (DSI 1), y la determinación de los mecanismos genéricos de diseño. Estos últimos sirven de guía en la utilización de diferentes estilos de diseño, tanto en el ámbito global del sistema de información, como en el diseño de detalle.</p>
<p>El diseño de los subsistemas de soporte, conceptualmente, es similar al diseño de los subsistemas específicos, aunque debe cumplir con unos objetivos claros de reutilización. De esta manera, se consigue simplificar y abstraer el diseño de los subsistemas específicos de la complejidad del entorno tecnológico, dotando al sistema de información de una mayor independencia de la infraestructura que le da soporte. Con este fin, se aconseja la consulta de los datos de otros proyectos existentes, disponible en el Histórico de Proyectos. Si esto no fuera&nbsp; suficiente, se puede contar en esta actividad con la participación de perfiles técnicos, con una visión global de la instalación.</p>
<p>Esta actividad se realiza en paralelo al diseño detallado, debido a que existe una constante realimentación, tanto en la especificación de los subsistemas con sus interfaces y dependencias, como en la aplicación de esqueletos o patrones en el diseño.</p>
<p>Los productos resultantes de esta actividad son:</p>
<ul><li>Diseño Detallado de los Subsistemas de Soporte.</li>
<li>Mecanismos Genéricos de Diseño y Construcción.</li>
</ul><p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/dsi2.png?w=825"/></p>
<p><strong>Actividad DSI 3: Diseño de Casos de Uso Reales</strong></p>
<p>Esta actividad, que se realiza solo en el caso de <strong>Diseño Orientado a Objetos</strong>, tiene como propósito especificar el comportamiento del sistema de información para un caso de uso, mediante objetos o subsistemas de diseño que interactúan, y determinar las operaciones de las clases e interfaces de los distintos subsistemas de diseño.</p>
<p>Para ello, una vez identificadas las clases participantes dentro de un caso de uso, es necesario completar los escenarios que se recogen del análisis, incluyendo las clases de diseño que correspondan y teniendo en cuenta las restricciones del entorno tecnológico, esto es, detalles relacionados con la implementación del sistema. Es necesario realizar los comportamientos de excepción para dichos escenarios. Algunos de ellos pueden haber sido identificados en el proceso de análisis, aunque no se resuelven hasta este momento. Dichas excepciones se añadirán al catálogo de excepciones para facilitar las pruebas.</p>
<p>Algunos de los escenarios detallados requerirán una nueva interfaz de usuario. Por este motivo es necesario diseñar el formato de cada una de las pantallas o impresos identificados.</p>
<p>Es importante validar que los subsistemas definidos en la tarea Identificación de Subsistemas de Diseño (DSI 1.5) tienen la mínima interfaz con otros subsistemas. Por este motivo, se elaboran los escenarios al nivel de subsistemas y, de esta forma, se delimitan las interfaces necesarias para cada uno de ellos, teniendo en cuenta toda la funcionalidad del sistema que recogen los casos de uso. Además, durante esta actividad pueden surgir requisitos de implementación, que se recogen en el catálogo de requisitos.</p>
<p>Las tareas de esta actividad se realizan en paralelo con las de Diseño de Clases (DSI 4).</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/dsi3.png?w=825"/></p>
<p><strong>Actividad DSI 4: Diseño de Clases</strong></p>
<p>El propósito de esta actividad, que se realiza sólo en el caso de <strong>Diseño Orientado a Objetos</strong>, es transformar el modelo de clases lógico, que proviene del análisis, en un modelo de clases de diseño. Dicho modelo recoge la especificación detallada de cada una de las clases, es decir, sus atributos, operaciones, métodos, y el diseño preciso de las relaciones establecidas entre ellas, bien sean de agregación, asociación o jerarquía. Para llevar a cabo todos estos puntos, se tienen en cuenta las decisiones tomadas sobre el entorno tecnológico y el entorno de desarrollo elegido para la implementación.</p>
<p>Se identifican las clases de diseño, que denominamos clases adicionales, en función del estudio de los escenarios de los casos de uso, que se está realizando en paralelo en la actividad Diseño de Casos de Uso Reales (DSI 3), y aplicando los mecanismos genéricos de diseño que se consideren convenientes por el tipo de especificaciones tecnológicas y de desarrollo. Entre ellas se encuentran clases abstractas, que integran características comunes con el objetivo de especializarlas en clases derivadas. Se diseñan las clases de interfaz de usuario, que provienen del análisis. Como consecuencia del estudio de los escenarios secundarios que se está realizando, pueden aparecer nuevas clases de interfaz.</p>
<p>También hay que considerar que, por el diseño de las asociaciones y agregaciones, pueden aparecer nuevas clases, o desaparecer incluyendo sus atributos y métodos en otras, si se considera conveniente por temas de optimización.</p>
<p>La jerarquía entre las clases se va estableciendo a lo largo de esta actividad, a medida que se van identificando comportamientos comunes en las clases, aunque haya una tarea propia de diseño de la jerarquía. Otro de los objetivos del diseño de las clases es identificar para cada clase, los atributos, las operaciones que cubren las responsabilidades que se identificaron en el análisis, y la especificación de los métodos que implementan esas operaciones, analizando los escenarios del Diseño de Casos de Uso Reales (DSI 3). Se determina la visibilidad de los atributos y operaciones de cada clase, con respecto a las otras clases del modelo.</p>
<p>Una vez que se ha elaborado el modelo de clases, se define la estructura física de los datos correspondiente a ese modelo, en la actividad Diseño Físico de Datos (DSI 6).</p>
<p>Además, en los casos en que sea necesaria una migración de datos de otros sistemas o una carga inicial de información, se realizará su especificación a partir del modelo de clases y las estructuras de datos de los sistemas origen.</p>
<p>Como resultado de todo lo anterior se actualiza el modelo de clases del análisis, una vez recogidas las decisiones de diseño.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/dsi4.png?w=825"/></p>
<p><strong>Actividad DSI 5: Diseño de la Arquitectura de Módulos del Sistema</strong></p>
<p>El objetivo de esta actividad, que sólo se realiza en el caso de <strong>Diseño Estructurado</strong>, es definir los módulos del sistema de información, y la manera en que van a interactuar unos con otros, intentando que cada módulo trate total o parcialmente un proceso específico y tenga una interfaz sencilla.</p>
<p>Para cada uno de los subsistemas específicos, identificados en la tarea Identificación de los Subsistemas de Diseño (DSI 1.5), se diseña la estructura modular de los procesos que lo integran, tomando como punto de partida los modelos obtenidos en la tarea Validación de los Modelos (ASI 9.3) del proceso de Análisis del Sistema de Información (ASI) y el catálogo de requisitos. Dicha estructura se irá completando con los módulos que vayan apareciendo como consecuencia del diseño de la interfaz de usuario, así como de la optimización del diseño físico de datos.</p>
<p>Durante el diseño de los módulos, se pueden identificar características o comportamientos comunes relacionados con accesos a las bases de datos o ficheros, lógica de tratamiento, llamadas a otros módulos, gestión de errores, etc. que determinen la necesidad de realizar su implementación como subsistemas de soporte.</p>
<p>Además, se analizan los comportamientos de excepción asociados a los diferentes módulos y a las interfaces entre los mismos, intentando independizar en la medida de lo posible aquéllos que presenten un tratamiento común. Dichas excepciones se incorporan al catálogo de excepciones.</p>
<p>En esta actividad, se consideran los estándares y normas establecidas para el diseño, aplicando, cuando proceda, los mecanismos genéricos de diseño identificados en la tarea Identificación de Mecanismos Genéricos de Diseño (DSI 2.2).</p>
<p>Las tareas de esta actividad no se realizan de forma secuencial, sino en paralelo, con continuas realimentaciones entre ellas y con las realizadas en las actividades Definición de la Arquitectura del Sistema (DSI 1), Diseño de la Arquitectura de Soporte (DSI 2) y Diseño Físico de Datos (DSI 6).</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/dsi5.png?w=825"/></p>
<p><strong>Actividad DSI 6: Diseño Físico de Datos</strong></p>
<p>En esta actividad se define la estructura física de datos que utilizará el sistema, a partir del modelo lógico de datos normalizado o modelo de clases, de manera que teniendo presentes las características específicas del sistema de gestión de datos concreto a utilizar, los requisitos establecidos para el sistema de información, y las particularidades del entorno tecnológico, se consiga una mayor eficiencia en el tratamiento de los datos.</p>
<p>También se analizan los caminos de acceso a los datos utilizados por cada módulo/clase del sistema en consultas y actualizaciones, con el fin de mejorar los tiempos de respuesta y optimizar los recursos de máquina.</p>
<p>Las tareas de esta actividad se realizan de forma iterativa y en paralelo con las realizadas en las actividades Definición de la Arquitectura del Sistema (DSI 1), donde se especifican los detalles de arquitectura e infraestructura y la planificación de capacidades, Diseño de la Arquitectura de Soporte (DSI 2), dónde se determinan y diseñan los servicios comunes que pueden estar relacionados con la gestión de datos (acceso a bases de datos, ficheros, áreas temporales, sincronización de bases de datos, etc.), Diseño de Casos de Uso Reales y de Clases (DSI 3 y 4), para desarrollo orientado a objetos, y Diseño de la Arquitectura de Módulos del Sistema (DSI 5), para desarrollo estructurado, dónde se especifica la lógica de tratamiento y las interfaces utilizadas.</p>
<p>En el caso de diseño orientado a objetos, esta actividad también es necesaria. La obtención del modelo físico de datos se realiza aplicando una serie de reglas de transformación a cada elemento del modelo de clases que se está generando en la actividad Diseño de Clases (DSI 4).</p>
<p>Asimismo, en esta actividad hay que considerar los estándares y normas establecidos para el diseño aplicando, cuando proceda, los mecanismos genéricos de diseño identificados en la tarea Identificación de Mecanismos Genéricos de Diseño (DSI 2.2).</p>
<p>A continuación se incluye una table resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/dsi6.png?w=825"/></p>
<p><strong>Actividad DSI 7: Verificación y Aceptación de la Arquitectura del Sistema</strong></p>
<p>El objetivo de esta actividad es garantizar la calidad de las especificaciones del diseño del sistema de información y la viabilidad del mismo, como paso previo a la generación de las especificaciones de construcción.</p>
<p>Para cumplir dicho objetivo, se llevan a cabo las siguientes acciones:</p>
<ul><li>Verificación de la calidad técnica de cada modelo o especificación.</li>
<li>Aseguramiento de la coherencia entre los distintos modelos.</li>
<li>Aceptación del diseño de la arquitectura por parte de Explotación y Sistemas.</li>
</ul><p>Esta actividad es compleja, por lo que es aconsejable utilizar herramientas de apoyo para la realización de sus tareas.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/dsi7.png?w=825"/></p>
<p><strong>Actividad DSI 8: Generación de Especificaciones de Construcción</strong></p>
<p>En esta actividad se generan las especificaciones para la construcción del sistema de información, a partir del diseño detallado.</p>
<p>Estas especificaciones definen la construcción del sistema de información a partir de las unidades básicas de construcción (en adelante, componentes), entendiendo como tales unidades independientes y coherentes de construcción y ejecución, que se corresponden con un empaquetamiento físico de los elementos del diseño de detalle, como pueden ser módulos, clases o especificaciones de interfaz.</p>
<p>La división del sistema de información en subsistemas de diseño proporciona, por continuidad, una primera división en subsistemas de construcción, definiendo para cada uno de ellos los componentes que lo integran. Si se considera necesario, un subsistema de diseño se podrá dividir a su vez en sucesivos niveles para mayor claridad de las especificaciones de construcción.</p>
<p>Las dependencias entre subsistemas de diseño proporcionan información para establecer las dependencias entre los subsistemas de construcción y, por lo tanto, definir el orden o secuencia que se debe seguir en la construcción y en la realización de las pruebas.</p>
<p>También se generan las especificaciones necesarias para la creación de las estructuras de datos en los gestores de bases de datos o sistemas de ficheros.</p>
<p>El producto resultante de esta actividad es el conjunto de las especificaciones de construcción del sistema de información, que comprende:</p>
<ul><li>Especificación del entorno de construcción.</li>
<li>Descripción de subsistemas de construcción y dependencias.</li>
<li>Descripción de componentes.</li>
<li>Plan de integración del sistema de información.</li>
<li>Especificación detallada de componentes.</li>
<li>Especificación de la estructura física de datos.</li>
</ul><p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/dsi8.png?w=825"/></p>
<p><strong>Actividad DSI 9: Diseño de la Migración y Carga Inicial de Datos</strong></p>
<p>Esta actividad sólo se lleva a cabo cuando es necesaria una carga inicial de información, o una migración de datos de otros sistemas, cuyo alcance y estrategia a seguir se habrá establecido previamente.</p>
<p>Para ello, se toma como referencia el plan de migración y carga inicial de datos, que recoge las estructuras físicas de datos del sistema o sistemas origen implicadas en la conversión, la prioridad en las cargas y secuencia a seguir, las necesidades previas de depuración de la información, así como los requisitos necesarios para garantizar la correcta implementación de los procedimientos de migración sin comprometer el funcionamiento de los sistemas actuales.</p>
<p>A partir de dicho plan, y de acuerdo a la estructura física de los datos del nuevo sistema, obtenida en la actividad Diseño Físico de Datos (DSI 6), y a las características de la arquitectura y del entorno tecnológico propuesto en la actividad Definición de la Arquitectura del Sistema (DSI 1), se procede a definir y diseñar en detalle los procedimientos y procesos necesarios para realizar la migración.</p>
<p>Se completa el plan de pruebas específico establecido en el plan de migración y carga inicial, detallando las pruebas a realizar, los criterios de aceptación o rechazo de la prueba y los responsables de la organización, realización y evaluación de resultados.</p>
<p>Asimismo, se determinan las necesidades adicionales de infraestructura, tanto para la implementación de los procesos como para la realización de las pruebas.</p>
<p>Como resultado de esta actividad, se actualiza el plan de migración y carga inicial de datos con la información siguiente:</p>
<ul><li>Especificación del entorno de migración.</li>
<li>Definición de procedimientos de migración.</li>
<li>Diseño detallado de módulos.</li>
<li>Especificación técnica de las pruebas.</li>
<li>Planificación de la migración y carga inicial.</li>
</ul><p>Es importante considerar que una carga inicial de información no tiene el mismo alcance y complejidad que una migración de datos, de modo que las tareas de esta actividad se deben llevar a cabo en mayor o menor medida en función de las características de los datos a cargar.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/dsi9.png?w=825"/></p>
<p><strong>Actividad DSI 10: Especificación Técnica del Plan de Pruebas</strong></p>
<p>En esta actividad se realiza la especificación de detalle del plan de pruebas del sistema de información para cada uno de los niveles de prueba establecidos en el proceso Análisis del Sistema de Información:</p>
<ul><li>Pruebas unitarias.</li>
<li>Pruebas de integración.</li>
<li>Pruebas del sistema.</li>
<li>Pruebas de implantación.</li>
<li>Pruebas de aceptación.</li>
</ul><p>Para ello se toma como referencia el plan de pruebas, que recoge los objetivos de la prueba de un sistema, establece y coordina una estrategia de trabajo, y provee del marco adecuado para planificar paso a paso las actividades de prueba. También puede ser una referencia el plan de integración del sistema de información propuesto, opcionalmente, en la tarea Definición de Componentes y Subsistemas de Construcción (DSI 8.2).</p>
<p>El catálogo de requisitos, el catálogo de excepciones y el diseño detallado del sistema de información, permiten la definición de las verificaciones que deben realizarse en cada nivel de prueba para comprobar que el sistema responde a los requisitos planteados. La asociación de las distintas verificaciones a componentes, grupos de componentes y subsistemas, o al sistema de información completo, determina las distintas verificaciones de cada nivel de prueba establecido.</p>
<p>Las pruebas unitarias comprenden las verificaciones asociadas a cada componente del sistema de información. Su realización tiene como objetivo verificar la funcionalidad y estructura de cada componente individual.</p>
<p>Las pruebas de integración comprenden verificaciones asociadas a grupos de componentes, generalmente reflejados en la definición de subsistemas de construcción o en el plan de integración del sistema de información. Tienen por objetivo verificar el correcto ensamblaje entre los distintos componentes.</p>
<p>Las pruebas del sistema, de implantación y de aceptación corresponden a verificaciones asociadas al sistema de información, y reflejan distintos propósitos en cada tipo de prueba:</p>
<ul><li>Las pruebas del sistema son pruebas de integración del sistema de información completo. Permiten probar el sistema en su conjunto y con otros sistemas con los que se relaciona para verificar que las especificaciones funcionales y técnicas se cumplen.</li>
<li>Las pruebas de implantación incluyen las verificaciones necesarias para asegurar que el sistema funcionará correctamente en el entorno de operación al responder satisfactoriamente a los requisitos de rendimiento, seguridad y operación, y coexistencia con el resto de los sistemas de la instalación, y conseguir la aceptación del sistema por parte del usuario de operación.</li>
<li>Las pruebas de aceptación van dirigidas a validar que el sistema cumple los requisitos de funcionamiento esperado, recogidos en el catálogo de requisitos y en los criterios de aceptación del sistema de información, y conseguir la aceptación final del sistema por parte del usuario.</li>
</ul><p>Las pruebas unitarias, de integración y del sistema se llevan a cabo en el proceso Construcción del Sistema de Información (CSI), mientras que las pruebas de implantación y aceptación se realizan en el proceso implantación y Aceptación del Sistemas (IAS).</p>
<p>Como resultado de esta actividad se actualiza el plan de pruebas con la información siguiente:</p>
<ul><li>Especificación del entorno de pruebas.</li>
<li>Especificación técnica de niveles de prueba.</li>
<li>Planificación de las pruebas.</li>
</ul><p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/dsi10.png?w=825"/></p>
<p><strong>Actividad DSI 11: Establecimiento de Requisitos de Implantación</strong></p>
<p>En esta actividad se completa el catálogo de requisitos con aquéllos relacionados con la documentación que el usuario requiere para operar con el nuevo sistema, y los relativos a la propia implantación del sistema en el entorno de operación.</p>
<p>La incorporación de estos requisitos permite ir preparando, en los proceso de Construcción del Sistema de Información (CSI) e Implantación y Aceptación del Sistema (IAS), los medios y recursos necesarios para que los usuarios, tanto finales como de operación, sean capaces de utilizar el nuevo sistema de forma satisfactoria.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/dsi11.png?w=825"/></p>
<p><strong>Actividad DSI 12: Aprobación del Diseño del Sistema de Información</strong></p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/dsi12.png?w=825"/></p>
<h3>Construcción del Sistema de Información</h3>
<p><strong>Descripción y Objetivos</strong></p>
<p>En este proceso se genera el código de los componentes del Sistema de Información, se desarrollan todos los procedimientos de operación y seguridad y se elaboran todos los manuales de usuario final y de explotación con el objetivo de asegurar el correcto funcionamiento del Sistema para su posterior implantación.</p>
<p>Para conseguir dicho objetivo, en este proceso se realizan las pruebas unitarias, las pruebas de integración de los subsistemas y componentes y las pruebas del sistema, de acuerdo al plan de pruebas establecido.</p>
<p>Asimismo, se define la formación de usuario final y, si procede, se construyen los procedimientos de migración y carga inicial de datos.</p>
<p>Al ser MÉTRICA Versión 3 una metodología que cubre tanto desarrollos estructurados como orientados a objetos, las actividades de ambas aproximaciones están integradas en una estructura común.</p>
<p>El producto Especificaciones de Construcción del Sistema de Información, obtenido en la actividad de Generación de Especificaciones de Construcción (DSI 8), es la base para la construcción del sistema de información. En dicho producto se recoge la información relativa al entorno de construcción del sistema de información, la especificación detallada de los componentes y la descripción de la estructura física de datos, tanto bases de datos como sistemas de ficheros. Opcionalmente, incluye un plan de integración del sistema de información, en el que se especifica la secuencia y organización de la construcción de los distintos componentes.</p>
<p>En la actividad Preparación del Entorno de Generación y Construcción (CSI 1), se asegura la disponibilidad de la infraestructura necesaria para la generación del código de los componentes y procedimientos del sistema de información.</p>
<p>Una vez configurado el entorno de construcción, se realiza la codificación y las pruebas de los distintos componentes que conforman el sistema de información, en las actividades:</p>
<ul><li>Generación del Código de los Componentes y Procedimientos (CSI 2), que se hace según las especificaciones de construcción del sistema de información, y conforme al plan de integración del sistema de información.</li>
<li>Ejecución de las Pruebas Unitarias (CSI 3), donde se llevan a cabo las verificaciones definidas en el plan de pruebas para cada uno de los componentes.</li>
<li>Ejecución de las Pruebas de Integración (CSI 4), que incluye la ejecución de las verificaciones asociadas a los subsistemas y componentes, a partir de los componentes verificados individualmente, y la evaluación de los resultados.</li>
</ul><p>Una vez construido el sistema de información y realizadas las verificaciones correspondientes, se lleva a cabo la integración final del sistema de información en la actividad Ejecución de las Pruebas del Sistema (CSI 5), comprobando tanto las interfaces entre subsistemas y sistemas externos como los requisitos, de acuerdo a las verificaciones establecidas en el plan de pruebas para el nivel de pruebas del sistema.</p>
<p>En la actividad Elaboración de los Manuales de Usuario (CSI 6), se genera la documentación de usuario final o explotación, conforme a los requisitos definidos en el proceso Diseño del Sistema de Información.</p>
<p>La formación necesaria para que los usuarios finales sean capaces de utilizar el sistema de forma satisfactoria se especifica en la actividad Definición de la Formación de Usuarios Finales (CSI 7).</p>
<p>Si se ha establecido la necesidad de realizar una migración de datos, la construcción y pruebas de los componentes y procedimientos relativos a dicha migración y a la carga inicial de datos se realiza en la actividad Construcción de los Componentes y Procedimientos de Migración y Carga Inicial de Datos (CSI 8).</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/csi.png?w=825"/></p>
<p><strong>Actividad CSI 1: Preparación del Entorno de Generación y Construcción</strong></p>
<p>El objetivo de esta actividad es asegurar la disponibilidad de todos los medios y facilidades para que se pueda llevar a cabo la construcción del sistema de información. Entre estos medios, cabe destacar la preparación de los puestos de trabajo, equipos físicos y lógicos, gestores de bases de datos, bibliotecas de programas, herramientas de generación de código, bases de datos o ficheros de prueba, entre otros.</p>
<p>Las características del entorno de construcción y sus requisitos de operación y seguridad, así como las especificaciones de construcción de la estructura física de datos, se establecen en la actividad Generación de Especificaciones de Construcción (DSI 8), y constituyen el punto de partida para la realización de esta actividad.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/csi1.png?w=825"/></p>
<p><strong>Actividad CSI 2: Generación del Código de los Componentes y Procedimientos</strong></p>
<p>El objetivo de esta actividad es la codificación de los componentes del sistema de información, a partir de las especificaciones de construcción obtenidas en el proceso Diseño del Sistema de Información (DSI), así como la construcción de los procedimientos de operación y seguridad establecidos para el mismo.</p>
<p>En paralelo a esta actividad, se desarrollan las actividades relacionadas con las pruebas unitarias y de integración del sistema de información. Esto permite una construcción incremental, en el caso de que así se haya especificado en el plan de pruebas y en el plan de integración del sistema de información.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presenta actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/csi2.png?w=825"/></p>
<p><strong>Actividad CSI 3: Ejecución de las Pruebas Unitarias</strong></p>
<p>En esta actividad se realizan las pruebas unitarias de cada uno de los componentes del sistema de información, una vez codificados, con el objeto de comprobar que su estructura es correcta y que se ajustan a la funcionalidad establecida.</p>
<p>En el plan de pruebas se ha definido el entorno necesario para la realización de cada nivel de prueba, así como las verificaciones asociadas a las pruebas unitarias, la coordinación y secuencia a seguir en la ejecución de las mismas y los criterios de registro y aceptación de los resultados.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/csi3.png?w=825"/></p>
<p><strong>Actividad CSI 4: Ejecución de las Pruebas de Integración</strong></p>
<p>El objetivo de las pruebas de integración es verificar si los componentes o subsistemas interactúan correctamente a través de sus interfaces, tanto internas como externas, cubren la funcionalidad establecida, y se ajustan a los requisitos especificados en las verificaciones correspondientes.</p>
<p>La estrategia a seguir en las pruebas de integración se establece en el plan de pruebas, donde se habrá tenido en cuenta el plan de integración del sistema de información, siempre y cuando se haya especificado en la tarea Definición de Componentes y Subsistemas de Construcción (DSI 8.2).</p>
<p>Esta actividad se realiza en paralelo a las actividades Generación del Código de los Componentes y Procedimientos (CSI 2) y Ejecución de las Pruebas Unitarias (CSI 3). Sin embargo, es necesario que los componentes objeto de las pruebas de integración se hayan verificado de manera unitaria.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/csi4.png?w=825"/></p>
<p><strong>Actividad CSI 5: Ejecución de las Pruebas del Sistema</strong></p>
<p>El objetivo de las pruebas del sistema es comprobar la integración del sistema de información globalmente, verificando el funcionamiento correcto de las interfaces entre los distintos subsistemas que lo componen y con el resto de sistemas de información con los que se comunica.</p>
<p>En la realización de estas pruebas es importante comprobar la cobertura de los requisitos, dado que su incumplimiento puede comprometer la aceptación del sistema por el equipo de operación responsable de realizar las pruebas de implantación del sistema, que se llevarán a cabo en el proceso Implantación y Aceptación del Sistema.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/csi5.png?w=825"/></p>
<p><strong>Actividad CSI 6: Elaboración de los Manuales de Usuario</strong></p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/csi6.png?w=825"/></p>
<p><strong>Actividad CSI 7: Definición de la Formación de Usuarios Finales</strong></p>
<p>En esta actividad se establecen las necesidades de formación del usuario final, con el objetivo de conseguir la explotación eficaz del nuevo sistema.</p>
<p>Para la definición de la formación hay que tener en cuenta las características funcionales y técnicas propias del sistema de información, así como los requisitos relacionados con la formación del usuario final, establecidos en la tarea Especificación de Requisitos de Implantación (DSI 11.2).</p>
<p>El producto resultante de esta actividad es la especificación de la formación de usuarios finales, que consta de los siguientes elementos:</p>
<ul><li>Esquema de formación.</li>
<li>Materiales y entornos de formación.</li>
</ul><p>En el proceso Implantación y Aceptación del Sistema (IAS), se unifican las especificaciones de formación de cada sistema de información implicado en la implantación y se elabora un único plan de formación que esté alineado con el plan de implantación del sistema.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/csi7.png?w=825"/></p>
<p><strong>Actividad CSI 8: Construcción de los Componentes y Procedimientos de Migración y Carga Inicial de Datos</strong></p>
<p>El objetivo de esta actividad es la codificación y prueba de los componentes y procedimientos de migración y carga inicial de datos, a partir de las especificaciones recogidas en el plan de migración y carga inicial de datos obtenidos en el proceso Diseño del Sistema de Información.</p>
<p>Previamente a la generación del código, se prepara la infraestructura tecnológica necesaria para realizar la codificación y las pruebas de los distintos componentes y procedimientos asociados, de acuerdo a las características del entorno de migración especificado en el plan de migración y carga inicial de datos.</p>
<p>Finalmente, se llevan a cabo las verificaciones establecidas en la especificación técnica del plan de pruebas propio de la migración.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/csi8.png?w=825"/></p>
<p><strong>Actividad CSI 9: Aprobación del Sistema de Información</strong></p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/csi9.png?w=825"/></p>
<h3>Implantación y Aceptación del Sistema</h3>
<p><strong>Descripción y Objetivos</strong></p>
<p>Este proceso tiene como objetivo principal la entrega del sistema en su totalidad, y la realización de todas las actividades necesarias para el paso a producción del mismo.</p>
<p>En primer lugar, se revisa la estrategia de implantación que ya se determinó en el proceso Estudio de Viabilidad del Sistema (EVS). Se estudia su alcance y, en función de sus características, se define un plan de implantación y se especifica el equipo que lo va a llevar a cabo. Conviene señalar la participación del usuario de operación en las pruebas de implantación, del usuario final en las pruebas de aceptación, y del responsable de mantenimiento.</p>
<p>Las actividades previas al inicio de la producción incluyen la preparación de la infraestructura necesaria para configurar el entorno, la instalación de los componentes, la activación de los procedimientos manuales y automáticos asociados y, cuando proceda, la migración o carga inicial de datos. Para ello se toman como punto de partida los productos software probados, obtenidos en el proceso Construcción del Sistema de Información (CSI) y su documentación asociada. Se realizan las pruebas de implantación y de aceptación del sistema en su totalidad. Responden a los siguientes propósitos:</p>
<ul><li>Las pruebas de implantación cubren un rango muy amplio, que va desde la comprobación de cualquier detalle de diseño interno hasta aspectos tales como las comunicaciones. Se debe comprobar que el sistema puede gestionar los volúmenes de información requeridos, se ajusta a los tiempos de respuesta deseados y que los procedimientos de respaldo, seguridad e interfaces con otros sistemas funcionan correctamente. Se debe verificar también el comportamiento del sistema bajo las condiciones más extremas.</li>
<li>Las pruebas de aceptación se realizan por y para los usuarios. Tienen como objetivo validar formalmente que el sistema se ajusta a sus necesidades.</li>
</ul><p>Asimismo, se llevan a cabo las tareas necesarias para la preparación del mantenimiento, siempre y cuando se haya decidido que éste va a efectuarse. En cualquier caso, es necesario que la persona que vaya a asumir el mantenimiento conozca el sistema, antes de su incorporación al entorno de producción.</p>
<p>Además hay que determinar los servicios (y niveles para cada uno) que requiere el sistema que se va a implantar, y el acuerdo que se adquiere una vez que se inicie la producción. Hay que distinguir entre servicios de gestión de operaciones (servicios por lotes, seguridad, comunicaciones, etc.) y servicios al cliente (servicio de atención a usuario, mantenimiento, etc.) que se deben negociar en cuanto a recursos, horarios, coste, etc. Se fija el nivel con el que se prestará el servicio como indicador de la calidad del mismo.</p>
<p>Conviene señalar que la implantación puede ser un proceso iterativo que se realiza de acuerdo al plan establecido para el comienzo de la producción del sistema en su entorno de operación. Para establecer este plan se tiene en cuenta:</p>
<ul><li>El cumplimiento de los requisitos de implantación definidos en la actividad Establecimiento de Requisitos (ASI 2) y especificados en la actividad Establecimiento de Requisitos de Implantación (DSI 11).</li>
<li>La estrategia de transición del sistema antiguo al nuevo.</li>
</ul><p>Finalmente, se realizan las acciones necesarias para el inicio de la producción. En el siguiente gráfico se muestra la relación de actividades de este proceso.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/ias.png?w=825"/></p>
<p><strong>Actividad IAS 1: Establecimiento del Plan de Implantación</strong></p>
<p>En esta actividad se revisa la estrategia de implantación para el sistema, establecida inicialmente en el proceso Estudio de Viabilidad del Sistema (EVS). Se identifican los distintos sistemas de información que forman parte del sistema objeto de la implantación. Para cada sistema se analizan las posibles dependencias con otros proyectos, que puedan condicionar el plan de implantación.</p>
<p>Una vez estudiado el alcance y los condicionantes de la implantación, se decide si ésta se puede llevar a cabo. Será preciso establecer, en su caso, la estrategia que se concretará de forma definitiva en el plan de implantación.</p>
<p>Se constituye el equipo de implantación, determinando los recursos humanos necesarios para la propia instalación del sistema, para las pruebas de implantación y aceptación, y para la preparación del mantenimiento. Se identifican, para cada uno de ellos, sus perfiles y niveles de responsabilidad.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/ias1.png?w=825"/></p>
<p><strong>Actividad IAS 2: Formación Necesaria para la Implantación</strong></p>
<p>En esta actividad se prepara y se imparte la formación al equipo que participará en la implantación y aceptación del sistema. Se realiza también el seguimiento de la formación de los usuarios finales, cuya impartición queda fuera del ámbito de MÉTRICA Versión 3. De esta forma, se asegura que la implantación se va a llevar a cabo correctamente.</p>
<p>Se determina la formación necesaria para el equipo de implantación, en función de los distintos perfiles y niveles de responsabilidad identificados en la actividad anterior. Para ello, se establece un plan de formación que incluye los esquemas de formación correspondientes, los recursos humanos y de infraestructura requeridos para llevarlo a cabo, así como una planificación que queda reflejada en el plan de formación.</p>
<p>La formación para que los usuarios finales sean capaces de utilizar el sistema de manera satisfactoria ha sido establecida, previamente, en la actividad Definición de la Formación de Usuarios Finales (CSI 7). En esta actividad, se analizan los esquemas de formación definidos según los diferentes perfiles, y se elabora un plan de formación que esté alineado con el plan de implantación.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/ias2.png?w=825"/></p>
<p><strong>Actividad IAS 3: Incorporación del Sistema al Entorno de Operación</strong></p>
<p>En esta actividad se realizan todas las tareas necesarias para la incorporación del sistema al entorno de operación en el que se van a llevar a cabo las pruebas de implantación y aceptación del sistema.</p>
<p>Mientras que las pruebas unitarias, de integración y del sistema se pueden ejecutar en un entorno distinto de aquel en el que finalmente se implantará, las pruebas de implantación y aceptación del sistema deben ejecutarse en el entorno real de operación. El propósito es comprobar que el sistema satisface todos los requisitos especificados por el usuario en las mismas condiciones que cuando se inicie la producción.</p>
<p>Por tanto, como paso previo a la realización de dichas pruebas y de acuerdo al plan de implantación establecido, se verifica que los recursos necesarios están disponibles para que se pueda realizar, adecuadamente, la instalación de todos los componentes que integran el sistema, así como la creación y puesta a punto de las bases de datos en el entorno de operación. Asimismo, se establecen los procedimientos de explotación y uso de las bases de datos de acuerdo a la normativa existente en dicho entorno.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/ias3.png?w=825"/></p>
<p><strong>Actividad IAS 4: Carga de Datos al Entorno de Operación</strong></p>
<p>Teniendo en cuenta que los sistemas de información que forman parte del sistema a implantar pueden mejorar, ampliar o sustituir a otros ya existentes en la organización, puede ser necesaria una carga inicial y/o una migración de datos cuyo alcance dependerá de las características y cobertura de cada sistema de información implicado. Por tanto, la necesidad de una migración de datos puede venir determinada desde el proceso Estudio de Viabilidad del Sistema (EVS), en la actividad Selección de la Solución (EVS 6). Allí se habrá establecido la estrategia a seguir en la sustitución, evaluando las opciones del enfoque de desarrollo e instalación más apropiados para llevarlo a cabo.</p>
<p>En cualquier caso, en la actividad Diseño de la Migración y Carga Inicial de Datos (DSI 9) se habrán definido y planificado los procesos y procedimientos necesarios para llevar a cabo la migración, realizándose su codificación en la actividad Construcción de los Componentes y Procedimientos de Migración y Carga Inicial de Datos (CSI 8).</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/ias4.png?w=825"/></p>
<p><strong>Actividad IAS 5: Pruebas de Implantación del Sistema</strong></p>
<p>La finalidad de las pruebas de implantación es doble:</p>
<ul><li>Comprobar el funcionamiento correcto del mismo en el entorno de operación.</li>
<li>Permitir que el usuario determine, desde el punto de vista de operación, la aceptación del sistema instalado en su entorno real, según el cumplimiento de los requisitos especificados.</li>
</ul><p>Para ello, el responsable de implantación revisa el plan de pruebas de implantación y los criterios de aceptación del sistema, previamente elaborados. Las pruebas las realizan los técnicos de sistemas y de operación, que forman parte del grupo de usuarios técnicos que ha recibido la formación necesaria para llevarlas a cabo.</p>
<p>Una vez ejecutadas estas pruebas, el equipo de usuario técnicos informa de las incidencias detectadas al responsable de implantación, el cual analiza la información y toma las medidas correctoras que considere necesarias para que el sistema dé respuesta a las especificaciones previstas, momento en el que el equipo de operación lo da por probado.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/ias5.png?w=825"/></p>
<p><strong>Actividad IAS 6: Pruebas de Aceptación del Sistema</strong></p>
<p>Las pruebas de aceptación tienen como fin validar que el sistema cumple los requisitos básicos de funcionamiento esperado y permitir que el usuario determine la aceptación del sistema. Por este motivo, estas pruebas son realizadas por el usuario final que, durante este periodo de tiempo, debe plantear todas las deficiencias o errores que encuentre antes de dar por aprobado el sistema definitivamente.</p>
<p>Los Directores de los Usuarios revisan los criterios de aceptación, especificados previamente en el plan de pruebas del sistema, y dirigen las pruebas de aceptación final que llevan a cabo los usuarios expertos. A su vez, éstos últimos deben elaborar un informe que los Directores de los Usuarios analizan y evalúan para determinar la aceptación o rechazo del sistema.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/ias6.png?w=825"/></p>
<p><strong>Actividad IAS 7: Preparación del Mantenimiento del Sistema</strong></p>
<p>El objetivo de esta actividad es permitir que el equipo que va a asumir el mantenimiento del sistema esté familiarizado con él antes de que el sistema pase a producción. Para conseguir este objetivo, se ha considerado al responsable de mantenimiento como parte integrante del equipo de implantación. Por lo tanto, se habrá tenido en cuenta su perfil al elaborar el esquema de formación correspondiente.</p>
<p>Una vez que el responsable de mantenimiento ha recibido la formación necesaria y adquirido una visión global del sistema que se va a implantar, se le entregan los productos que serán objeto del mantenimiento. De esta manera, obtiene de una forma gradual un conocimiento profundo del funcionamiento y facilidades que incorpora el sistema, que van a permitirle acometer los cambios solicitados por los usuarios con&nbsp; mayor facilidad y eficiencia. Se reduce, en consecuencia, el esfuerzo invertido en el mantenimiento.</p>
<p>Es importante resaltar que la existencia de una configuración del software permite reducir el esfuerzo requerido y mejora la calidad general del software a mantener, aunque no garantiza un mantenimiento libre de problemas. Una pobre configuración del software puede tener un impacto negativo sobre su facilidad de mantenimiento.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/ias7.png?w=825"/></p>
<p><strong>Actividad IAS 8: Establecimiento del Acuerdo de Nivel de Servicio</strong></p>
<p>Antes de la aprobación definitiva del sistema por parte del Comité de Dirección es conveniente:</p>
<ul><li>Determinar los servicios que requiere el mismo.</li>
<li>Especificar los niveles de servicio con los que se va a valorar la calidad de esa prestación.</li>
<li>Definir qué compromisos se adquieren con la entrega del sistema.</li>
</ul><p>Para ello, en primer lugar, se negocia entre los máximos responsables del usuario y de operación qué servicios y de qué tipo se van a prestar. Una vez acordados, se detallan los niveles de servicio definiendo sus propiedades funcionales y de calidad. Se establece cuáles de ellas son cuantificables y qué indicadores se van a aplicar. Es importante señalar que los niveles de servicio son específicos para cada uno de los subsistemas que componen el sistema de información, y dependen del entorno de operación y de la localización geográfica en que se implante un sistema de información concreto, pudiendo haber servicios básicos para todo el sistema o específicos para un subsistema de información concreto.</p>
<p>Por último, se establece formalmente el acuerdo de nivel de servicio, considerando los recursos necesarios, plazos de restablecimiento del servicio, coste y mecanismos de regulación que están asociados a cada servicio especificado anteriormente.</p>
<p>Según el ámbito y el alcance de los tipos de servicio que se vayan a prestar, se determinan los productos del ciclo de vida del software necesarios para poder establecer el acuerdo de nivel de servicio.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/ias8.png?w=825"/></p>
<p><strong>Actividad IAS 9: Presentación y Aprobación del Sistema</strong></p>
<p>Una vez que se han efectuado las pruebas de implantación y de aceptación, y que se ha fijado el acuerdo de nivel de servicio, el Comité de Dirección debe formalizar la aprobación del sistema. Para esto, se lleva a cabo una presentación general del sistema al Comité de Dirección y se espera la confirmación de su aprobación.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/ias9.png?w=825"/></p>
<p><strong>Actividad IAS 10: Paso a Producción</strong></p>
<p>Esta actividad tiene como objetivo establecer el punto de inicio en que el sistema pasa a producción, se traspasa la responsabilidad al equipo de mantenimiento y se empiezan a dar los servicios establecidos en el acuerdo de nivel de servicio, una vez que el Comité de Dirección ha aprobado el sistema.</p>
<p>Para ello es necesario que, después de haber realizado las pruebas de implantación y de aceptación del sistema, se disponga del entorno de producción perfectamente instalado en cuanto a hardware y software de base, componentes del nuevo sistema y procedimientos manuales y automáticos.</p>
<p>En función del entorno en el que se hayan llevado a cabo las pruebas de implantación y aceptación del sistema, habrá que instalar los componentes del sistema total o parcialmente. También se tendrá en cuenta la necesidad de migrar todos los datos o una parte de ellos.</p>
<p>Una vez que el sistema ya está en producción, se le notifica al responsable de mantenimiento, al responsable de operación y al Comité de Dirección.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/ias10.png?w=825"/></p>
<h3>Mantenimiento de Sistemas de Información</h3>
<p><strong>Descripción y Objetivos</strong></p>
<p>El objetivo de este proceso es la obtención de una nueva versión de un sistema de información desarrollado con MÉTRICA Versión 3 o Versión 2, a partir de las peticiones de mantenimiento que los usuarios realizan con motivo de un problema detectado en el sistema, o por la necesidad de una mejora del mismo.</p>
<p>En este apartado se realiza el registro de las peticiones de mantenimiento recibidas, con el fin de llevar el control de las mismas y de proporcionar, si fuera necesario, datos estadísticos de peticiones recibidas o atendidas en un determinado periodo, sistemas que se han visto afectados por los cambios, en qué medida y el tiempo empleado en la resolución de dichos cambios. Es recomendable, por lo tanto, llevar un catálogo de peticiones de mantenimiento sobre los sistemas de información, en el que se registren una serie de datos que nos permitan disponer de la información antes mencionada.</p>
<p>En el momento en el que se registra la petición, se procede a diagnosticar de qué tipo de mantenimiento se trata. Atendiendo a los fines, podemos establecer los siguientes tipos de mantenimiento:</p>
<ul><li><strong>Correctivo</strong>: son aquellos cambios precisos para corregir errores del producto software.</li>
<li><strong>Evolutivo</strong>: son las incorporaciones, modificaciones y eliminaciones necesarias en un producto software para cubrir la expansión o cambio en las necesidades del usuario.</li>
<li><strong>Adaptativo</strong>: son las modificaciones que afectan a los entornos en los que el sistema opera, por ejemplo, cambios de configuración del hardware, software de base, gestores de base de datos, comunicaciones, etc.</li>
<li><strong>Perfectivo</strong>: son las acciones llevadas a cabo para mejorar la calidad interna de los sistemas en cualquiera de sus aspectos: reestructuración del código, definición más clara del sistema y optimización del rendimiento y eficiencia.</li>
</ul><p>Estos dos últimos tipos quedan fuera del ámbito de MÉTRICA Versión 3 ya que requieren actividades y perfiles distintos de los del proceso de desarrollo.</p>
<p>Una vez registrada la petición e identificado el tipo de mantenimiento y su origen, se determina de quién es la responsabilidad de atender la petición. En el supuesto de que la petición sea remitida, se registra en el catálogo de peticiones de mantenimiento y continúa el proceso. La petición puede ser denegada. En este caso, se notifica al usuario y acaba el proceso.</p>
<p>Posteriormente, según se trate de un mantenimiento correctivo o evolutivo, se verifica y reproduce el problema, o se estudia la viabilidad del cambio propuesto por el usuario. En ambos casos se estudia el alcance de la modificación. Hay que analizar las alternativas de solución identificando, según el tipo de mantenimiento de que se trate, cuál es la más adecuada. El plazo y urgencia de la solución a la petición se establece de acuerdo con el estudio anterior.</p>
<p>La definición de la solución incluye el estudio del impacto de la solución propuesta para la petición en los sistemas de información afectados. Mediante el análisis de dicho estudio, la persona encargada del Proceso de Mantenimiento valora el esfuerzo y coste necesario para la implementación de la modificación.</p>
<p>Las tareas de los procesos de desarrollo que va a ser necesario realizar son determinadas en función de los componentes del sistema actual afectados por la modificación. Estas tareas pertenecen a actividades de los procesos Análisis, Diseño, Construcción e Implantación.</p>
<p>Por último, y antes de la aceptación del usuario, es preciso establecer un plan de pruebas de regresión que asegure la integridad del sistema de información afectado.</p>
<p>La mejor forma de mantener el coste de mantenimiento bajo control es una gestión del proceso de Mantenimiento efectiva y comprometida. Por lo tanto, es necesario registrar de forma disciplinada los cambios realizados en los sistemas de información y en su documentación. Esto repercutirá directamente en la mayor calidad de los sistemas actuales.</p>
<p>La estructura propuesta para el Proceso de Mantenimiento de MÉTRICA Versión 3 comprende las siguientes actividades:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/msi.png?w=825"/></p>
<p><strong>Actividad MSI 1: Registro de la Petición</strong></p>
<p>El objetivo de esta actividad es establecer un sistema estandarizado de registro de información para las peticiones de mantenimiento, con el fin de controlar y canalizar los cambios propuestos por un usuario o cliente, mejorando el flujo de trabajo de la organización y proporcionando una gestión efectiva del mantenimiento. Es importante asignar responsabilidades para evitar la realización de cambios que beneficien a un usuario, pero que produzca un impacto negativo sobre otros muchos. Por tanto, es necesario, que todas las peticiones de mantenimiento sean presentadas de una forma estandarizada, que permita su clasificación y facilite la identificación del tipo de mantenimiento requerido.</p>
<p>Una vez que la petición ha sido registrada, que ha determinado el tipo de mantenimiento y los sistemas de información a los que inicialmente puede afectar, se comprueba su viabilidad, de acuerdo a las prestaciones de mantenimiento establecidas para dichos sistemas de información.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/msi1.png?w=825"/></p>
<p><strong>Actividad MSI 2: Análisis de la Petición</strong></p>
<p>En esta actividad se lleva a cabo el diagnóstico y análisis del cambio para dar respuesta a las peticiones de mantenimiento que han sido aceptadas en la actividad anterior.</p>
<p>Se analiza el alcance de la petición en lo referente a los sistemas de información afectados, valorando hasta qué punto pueden ser modificados en función del ciclo de vida estimado para los mismos y determinando la necesidad de desviar la petició hacia el proceso Estudio de Viabilidad del Sistema (EVS) o Análisis del Sistema de Información (ASI), en función del impacto sobre los sistemas de información afectados.</p>
<p>El enfoque de este estudio varía según el tipo de mantenimiento, teniendo en cuenta que en el caso de un mantenimiento correctivo que implique un error crítico debe abordarse el cambio de forma inmediata sin profundizar en el origen del mismo. No obstante, una vez reanudado el servicio, es imprescindible analizar el problema y determinar cuál es la solución definitiva.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/msi2.png?w=825"/></p>
<p><strong>Actividad MSI 3: Preparación de la Implementación de la Modificación</strong></p>
<p>Una vez finalizado el estudio previo de la petición y aprobada su implementación, se pasa a identificar de forma detallada cada uno de los elementos afectados por el cambio mediante el análisis de impacto. Este análisis tiene como objetivo determinar qué parte del sistema de información se ve afectada, y en qué medida, dejando claramente definido y documentado qué componentes hay que modificar, tanto de software como de hardware. Con el resultado de este análisis se dispone de los datos cuantitativos sobre los que aplicar los indicadores establecidos. Esto permitirá fijar un plan de acción, valorando la necesidad de realizar un reajuste de dichos indicadores, con el fin de cumplir el plazo máximo de entrega.</p>
<p>Una vez aceptado el plan de acción, se activan los correspondientes procesos de desarrollo para llevar a cabo la implementación de la solución. Al mismo tiempo, se especifican las pruebas de regresión con el fin de evitar el efecto onda en el sistema, una vez realizados los cambios.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/msi3.png?w=825"/></p>
<p><strong>Actividad MSI 4: Seguimiento y Evaluación de los Cambios hasta la Aceptación</strong></p>
<p>Se realiza el seguimiento de los cambios que se están llevando a cabo en los procesos de desarrollo, de acuerdo a los puntos de control del ciclo de vida del cambio establecidos en el plan de acción. Durante este seguimiento, se comprueba que sólo se han modificado los elementos que se ven afectados por el cambio y que se han realizado las pruebas correspondientes, especialmente las pruebas de integración y del sistema. Del resultado obtenido se hace una evaluación del cambio para la posterior aprobación.</p>
<p>Una vez finalizado el cambio en desarrollo, se realizan las pruebas de regresión especificadas en la actividad anterior, comprobando que ningún sistema no modificado, pero con posibilidades de verse afectado, ha variado su comportamiento habitual. Se informa si ha habido incidencias con el fin de que se resuelvan del modo más conveniente. Se evalúan las pruebas.</p>
<p>La aprobación de la petición se realiza al finalizar las pruebas de regresión, y después de comprobar que todo lo que ha sido modificado o puede verse afectado por el cambio, funciona correctamente. Con el cierre de la petición se podrán incluir en el catálogo, si se considera oportuno, parte de la información obtenida durante el proceso de mantenimiento que pueda facilitar posteriores análisis.</p>
<p>A continuación se incluye una tabla resumen con las tareas de la presente actividad:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/msi4.png?w=825"/></p>
<h3>Bibliografia</h3>
<ul><li><a href="https://es.scribd.com/document/357349084/TICB2-Planificacion-Del-Desarrollo" rel="noopener" target="_blank">Scribd (Ibiza Ales)</a></li>
</ul> </article>

# Estrategias de determinación de requerimientos: Entrevistas, Derivación de sistemas existentes, Análisis y Prototipos. La especificación de requisitos software.

<article><h2>Introducción a la Ingeniería de Requerimientos</h2>
<p>En la actualidad, son muchos los procesos de desarrollo de software que existen. Con el paso de los años, la Ingeniería del Software ha introducido y popularizado una serie de estándares para medir y certificar la calidad, tanto del sistema a desarrollar, como del proceso de desarrollo en sí. Se han publicado muchos libros y artículos relacionados con este tema, con el modelado de procesos del negocio y la reingeniería. Un número creciente de herramientas automatizadas han surgido para ayudar a definir y aplicar un proceso de desarrollo de software efectivo.</p>
<p>Hoy en día la economía global depende más de sistemas automatizados que en épocas pasadas. Esto ha llevado a los equipos de desarrollo a enfrentarse con una nueva década de procesos y estándares de calidad.</p>
<p>Sin embargo, ¿cómo explicamos la alta incidencia de fallos en los proyectos de software? ¿Por qué existen tantos proyectos de software víctimas de retrasos, presupuestos mal dimensionados y con problemas de calidad? ¿Cómo podemos tener una producción o una economía de calidad, cuando nuestras actividades diarias dependen de la calidad de un sistema que no la tiene?</p>
<p>Tal vez suene ilógico pero, a pesar de los avances que ha dado la tecnología, aún existen procesos de producción informales, parciales y en algunos casos no confiables.</p>
<p>La Ingeniería de Requerimientos cumple un papel primordial en el proceso de producción de software, ya que enfoca un área fundamental: la definición de lo que se desea producir. Su principal tarea consiste en la generación de especificaciones correctas que describan con claridad, sin ambigüedades, en forma consistente y compacta, el comportamiento del sistema. De esta manera, se pretende minimizar los problemas relacionados al desarrollo de sistemas.</p>
<p>Existe una gran cantidad de proyectos de software que no llegan a cumplir sus objetivos. En nuestro país somos partícipes de este problema a diario, en donde se ha vuelto común la compra de sistemas extranjeros, para luego “personalizarlos” supuestamente a la medida de las empresas.</p>
<p>Tal “personalización” termina retrasando (la mayoría de las veces) el proyecto en meses, o incluso en años. La problemática del año 2000 trajo como consecuencia una serie de cambios apresurados en los sistemas existentes, cambios que no fueron bien planificados.</p>
<p>El reemplazo de plataformas y tecnologías obsoletas, la compra de sistemas completamente nuevos, las modificaciones de todos o de casi todos los programas que forman un sistema, entre otras razones, llevan a desarrollar proyectos en calendarios sumamente ajustados y en algunos casos irreales. Esto ocasiona que se omitan muchos pasos importantes en el ciclo de vida de desarrollo, entre estos, la definición de los requerimientos.</p>
<p>En 1995 se realizó un estudio (informe CHAOS) sobre el resultado general de los proyectos de software. El estudio fue demoledor y esto a pesar de las herramientas existentes para el desarrollo de software (ver figura).</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/informe_chaos.png?w=825"/></p>
<h2>La Ingeniería de Requerimientos</h2>
<h3>¿Qué son Requerimientos?</h3>
<p>Normalmente, un concepto de la Ingeniería de Software tiene diferentes significados. De las muchas definiciones que existen para requerimiento, a continuación se presenta la definición que aparece en el glosario de la IEEE:</p>
<ol><li>Una condición o necesidad de un usuario para resolver un problema o alcanzar un objetivo.</li>
<li>Una condición o capacidad que debe estar presente en un sistema o componentes de sistema para satisfacer un contrato, estándar, especificación u otro documento formal.</li>
<li>Una representación documentada de una condición o capacidad como en 1 o 2.</li>
</ol><p>Los requerimientos pueden dividirse en requerimientos funcionales y requerimientos no funcionales:</p>
<ul><li>Los requerimientos funcionales definen las funciones que el sistema será capaz de realizar. Describen las transformaciones que el sistema realiza sobre las entradas para producir salidas.</li>
<li>Los requerimientos no funcionales tienen que ver con características que de una u otra forma puedan limitar el sistema, como por ejemplo, el rendimiento (en tiempo y espacio), interfaces de usuario, fiabilidad (robustez del sistema, disponibilidad de equipo), mantenimiento, seguridad, portabilidad, estándares, etc.</li>
</ul><h3>Características de los Requerimientos</h3>
<p>Las características de un requerimiento son sus propiedades principales. Un conjunto de requerimientos en estado de madurez deben presentar una serie de características tanto individualmente como en grupo. A continuación se presentan las más importantes:</p>
<ul><li><strong>Necesario</strong>: Un requerimiento es necesario si su omisión provoca una deficiencia en el sistema a construir, y además su capacidad, características físicas o factor de calidad no pueden ser reemplazados por otras capacidades del producto o del proceso.</li>
<li><strong>Conciso</strong>: Un requerimiento es conciso si es fácil de leer y entender. Su redacción debe ser simple y clara para aquellos que vayan a consultarlo en un futuro.</li>
<li><strong>Completo</strong>: Un requerimiento está completo si no necesita ampliar detalles en su redacción, es decir, si se proporciona la información suficiente para su comprensión.</li>
<li><strong>Consistente</strong>: Un requerimiento es consistente si no es contradictorio con otro requerimiento.</li>
<li><strong>No ambiguo</strong>: Un requerimiento no es ambiguo cuando tiene una sola interpretación. El lenguaje usado en su definición, no debe causar confusiones al lector.</li>
<li><strong>Verificable</strong>: Un requerimiento es verificable cuando puede ser cuantificado de manera que permita hacer uso de los siguientes métodos de verificación: inspección, análisis, demostración o pruebas.</li>
</ul><h3>Dificultades para definir los Requerimientos</h3>
<ul><li>Los requerimientos no son obvios y vienen de muchas fuentes.</li>
<li>Son difíciles de expresar en palabras (el lenguaje es ambiguo).</li>
<li>Existen muchos tipos de requerimientos y diferentes niveles de detalle.</li>
<li>La cantidad de requerimientos en un proyecto puede ser difícil de manejar.</li>
<li>Nunca son iguales. Algunos son más difíciles, más arriesgados, más importantes o más estables que otros.</li>
<li>Los requerimientos están relacionados unos con otros, y a su vez se relacionan con otras partes del proceso.</li>
<li>Cada requerimiento tiene propiedades únicas y abarcan áreas funcionales específicas.</li>
<li>Un requerimiento puede cambiar a lo largo del ciclo de desarrollo.</li>
<li>Son difíciles de cuantificar, ya que cada conjunto de requerimientos es particular para cada proyecto.</li>
</ul><h3>Definiciones par la Ingeniería de Requerimientos</h3>
<ul><li><em>Ingeniería de Requerimientos vs Administración de Requerimientos</em>: El proceso de recopilar, analizar y verificar las necesidades del cliente para un sistema es llamado Ingeniería de Requerimientos (IR). La meta de la IR es entregar una especificación de requerimientos de software correcta y completa. Los requerimientos son solicitudes que hace el usuario hacia el equipo de trabajo para la realización de alguna tarea. Los requerimientos que son aceptados, son definidos entre el cliente, los usuarios y el equipo de desarrollo, para identificar claramente los límites del sistema. Los requerimientos de los usuarios que han sido definidos, serán administrados para atenderlos y darles un adecuado seguimiento. La administración de requerimientos permite adicionalmente tener un control económico de los mismos.
<ul><li>La determinación tiene que ver con: Alcance, requerimientos funcionales, requerimientos no funcionales, complejidad.</li>
<li>La administración tiene que ver con: Actividades a realizar, responsables, productos a entregar, costo, tiempos.</li>
</ul></li>
<li>Ingeniería de Requerimientos es la disciplina para desarrollar una especificación completa, consistente y no ambigua, la cual servirá como base para acuerdos comunes entre todas las partes involucradas y en dónde se describen las funciones que realizará el sistema.</li>
<li>Ingeniería de Requerimientos es el proceso por el cual se transforman los requerimientos declarados por los clientes, ya sean hablados o escritos, a especificaciones precisas, no ambigua, consistentes y completas del comportamiento del sistema, incluyendo funciones, interfaces, rendimiento y limitaciones.</li>
<li>Es el proceso mediante el cual se intercambian diferentes puntos de vista para recopilar y modelar lo que el sistema va a realizar. Este proceso utiliza una combinación de métodos, herramientas y actores, cuyo producto es un modelo del cual se genera un documento de requerimientos.</li>
<li>Ingeniería de Requerimientos es un enfoque sistémico para recolectar, organizar y documentar los requerimientos del sistema. Es también el proceso que establece y mantiene acuerdos sobre los cambios de requerimientos, entre los clientes y el equipo del proyecto.</li>
<li>Una posible visión de la ingeniería de requerimientos es considerarla como un proceso de construcción de una especificación de requerimientos en el que se avanza desde especificaciones iniciales, que no poseen las propiedades idóneas, hasta especificaciones finales completas, formales y acordadas entre todos los participantes.</li>
</ul><p>Tres enfoques (dimensiones) desde los que se debe abordar la IR para lograr las especificaciones finales de los requerimientos de un sistema (ver figura):</p>
<ul><li>Por un lado están los factores psicológicos y congnitivos que afectan al grado de conocimiento sobre el sistema que se desea desarrollar, es decir, llegar a conocer la totalidad de los requerimientos que debe satisfacer el sistema. Habitualmente, este enfoque se cubre con actividades encaminadas a la adquisición de los requerimientos (elicitación).</li>
<li>Por otro lado, está el grado de formalismo de la representación del conocimiento sobre dichos requerimientos, teniendo en cuenta que un mayor grado de formalismo no implica necesariamente un mayor conocimiento. El formalismo se logra en las actividades encaminadas al análisis de requerimientos.</li>
<li>Por último, están los aspectos sociales, ya que al ser un proceso en el que participan personas con diferentes puntos de vista, es necesario llegar a un punto de acuerdo, normalmente mediante algún tipo de negociación. Las actividades de validación permiten a la IR resolver los posibles conflictos.</li>
</ul><p><img src="https://gsitic.files.wordpress.com/2018/01/requisitos.png?w=825"/></p>
<h3>Importancia de la Ingeniería de Requerimientos</h3>
<p>Los principales beneficios que se obtienen de la Ingeniería de Requerimientos son:</p>
<ul><li>Permite gestionar las necesidades del proyecto en forma estructurada: Cada actividad de la IR consiste de una serie de pasos organizados y bien definidos.</li>
<li>Mejora la capacidad de predecir cronogramas de proyectos, así como sus resultados: La IR proporciona un punto de partida para controles subsecuentes y actividades de mantenimiento, tales como estimación de costos, tiempo y recursos necesarios.</li>
<li>Disminuye los costos y retrasos del proyecto: Muchos estudios han demostrado que reparar errores por un mal desarrollo no descubierto a tiempo, es sumamente caro, especialmente aquellas decisiones tomadas durante la IR.</li>
<li>Mejora la calidad del software: La calidad en el software tiene que ver con cumplir un conjunto de requerimientos (funcionalidad, facilidad de uso, confiabilidad, desempeño, etc.).</li>
<li>Mejora la comunicación entre equipos: La especificación de requerimientos representa una forma de consenso entre clientes y desarrolladores. Si este consenso no ocurre, el proyecto no será exitoso.</li>
<li>Evita rechazos de usuarios finales: La ingeniería de requerimientos obliga al cliente a considerar sus requerimientos cuidadosamente y revisarlos dentro del marco del problema, por lo que se le involucra durante todo el desarrollo del proyecto.</li>
</ul><h3>Personal Involucrado</h3>
<p>Realmente, son muchas las personas involucradas en el desarrollo de los requerimientos de un sistema. Es importante saber que cada una de esas personas tienen diversos intereses y juegan roles específicos dentro de la planificación del proyecto. El conocimiento de cada papel desempeñado asegura que se involucren a las personas correctas en las diferentes fases del ciclo de vida, y en las diferentes actividades de la IR.</p>
<p>No conocer estos intereses puede ocasionar una comunicación poco efectiva entre clientes y desarrolladores, que a la vez traería impactos negativos tanto en tiempo como en presupuesto. Los roles más importantes pueden clasificarse como sigue:</p>
<ul><li><em>Usuarios finales</em>: Son las personas que usarán el sistema desarrollado. Ellos están relacionados con la usabilidad, la disponibilidad y la fiabilidad del sistema. Están familiarizados con los procesos específicos que debe realizar el software, dentro de los parámetros de su ambiente laboral. Serán quienes utilicen las interfaces y los manuales de usuario.</li>
<li><em>Usuarios líderes</em>: Son los individuos que comprenden el ambiente del sistema o el dominio del problema en donde será empleado el software desarrollado. Ellos proporcionan al equipo técnico los detalles y requerimientos de las interfaces del sistema.</li>
<li><em>Personal de mantenimiento</em>: Para proyectos que requieran un mantenimiento eventual, estas personas son las responsables de la administración de cambios, de la implementación y resolución de anomalías. Su trabajo consiste en revisar y mejorar los procesos del producto ya finalizado.</li>
<li><em>Analistas y programadores</em>: Son los responsables del desarrollo del producto en sí. Ellos interactúan directamente con el cliente.</li>
<li><em>Personal de pruebas</em>: Se encargan de elaborar y ejecutar el plan de pruebas para asegurar que las condiciones presentadas por el sistema son las adecuadas. Son quienes van a validar si los requerimientos satisfacen las necesidades del cliente.</li>
</ul><p>Otras personas que pueden estar involucradas, dependiendo de la magnitud del proyecto, pueden ser: administradores de proyecto, documentadores, diseñadores de BD, entre otros.</p>
<h3>Las Dimensiones de los Requerimientos</h3>
<p>Los calificativos que se aplican al término requerimiento muestran distintos ortogonales que a menudo son considerados aisladamente. Aquí se ven agrupados en tres dimensiones (ver figura).</p>
<ul><li><strong>Ámbito</strong>: Esta dimensión indica en qué ámbito se debe entender el requerimiento. En general, un ámbito de sistema indica que el requerimiento debe cumplirse a nivel de sistema, entendiendo por sistema un conjunto de hardware y software.</li>
<li><strong>Característica que define</strong>: Esta dimensión clasifica los requerimientos en función de la naturaleza de la característica del sistema que se especifica. En [Pohl 1997] aparece una completa clasificación denominada RSM (Requirements Specification Model, Modelo de Especificación de Requerimientos), cuyas principales clases son: requerimientos funcionales, requerimientos de datos y requerimientos no funcionales. Es conveniente separar de los requerimientos funcionales a los requerimientos de datos o de almacenamiento de información, que establecen qué información debe almacenar el sistema por ser relevante para las necesidades y objetivos de clientes y usuarios.</li>
<li><strong>Audiencia</strong>: Esta dimensión indica la audiencia a la que está dirigido el requisito, es decir, las personas que deben ser capaces de entenderlo. En general, se pueden distinguir dos tipos de audiencia:
<ul><li>Los clientes y usuarios, que no tienen porqué tener formación en ingeniería del software (especificación de requerimientos mediante lenguaje natural).</li>
<li>Los desarrolladores de software (especificación de requerimientos utilizando técnicas estructuradas, orientadas a objetos o formales).</li>
</ul></li>
</ul><p>En la literatura se suele referir a los requerimientos orientados a clientes y usuarios como requerimientos-C, requisito de usuario o requisito de cliente; y, a los requerimientos orientados al desarrollador como requerimientos-D o requerimientos software.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/requerimientos.png?w=825"/></p>
<h3>Puntos a considerar durante la Ingeniería de Requerimientos</h3>
<ul><li>Objetivos del negocio y ambiente de trabajo: Aunque los objetivos del negocio están definidos frecuentemente en términos generales, son usados para descomponer el trabajo en tareas específicas. En ciertas situaciones la IR se enfoca en la descripción de las tareas y en el análisis de sistemas similares. Esta información proporciona la base para especificar el sistema que será construido, aunque frecuentemente se añadan al sistema tareas que no encajan con el ambiente de trabajo planificado. El nuevo sistema cambiará el ambiente de trabajo, sin embargo, es muy difícil anticipar los efectos actuales sobre la organización. Los cambios no ocurren solamente cuando un nuevo software es implementado y puesto en producción, también ocurren cuando cambia el ambiente que lo rodea (nuevas soluciones a problemas, nuevo equipo para instalar, etc.). La necesidad de cambio es sustentada por el enorme costo de mantenimiento, aunque existen diversas razones que dificultan el mantenimiento del software, la falta de atención a la IR es la principal.</li>
<li>Frecuentemente la especificación inicial es también la especificación final, lo que obstaculiza la comunicación y el proceso de aprendizaje de las personas involucradas. Ésta es una de las razones por las cuales existen sistemas inadecuados.</li>
<li>Punto de vista de los clientes. Muchos sistemas tienen diferentes tipos de clientes. Cada grupo de clientes tiene necesidades diferentes y, diferentes requerimientos tienen diferentes grados de importancia para ellos. Por otro lado, pocas veces tenemos que los clientes son los usuarios, trayendo como consecuencia que los clientes soliciten procesos que causan conflictos con los solicitados por el usuario. Diferentes puntos de vistas también pueden tener consecuencias negativas, tales como datos redundantes, inconsistentes y ambiguos.</li>
<li>El tamaño y complejidad de los requerimientos ocasiona desentendimiento, dificultad para enfocarse en un solo aspecto a la vez y dificultad para visualizar relaciones existentes entre requerimientos.</li>
<li>Barreras de comunicación: La ingeniería de requerimientos depende de una intensa comunicación entre clientes y analistas de requerimientos. Sin embargo, existen problemas que no pueden ser resueltos mediante la comunicación. Para remediar esto, se deben abordar nuevas técnicas operacionales que ayuden a superar estas barreras y así ganar experiencia dentro del marco del sistema propuesto.</li>
<li>Evolución e integración del sistema: Pocos sistemas son construidos desde cero. En la práctica, los proyectos se derivan de sistemas ya existentes. Por lo tanto, los analistas de requerimientos deben comprender esos sistemas, que por lo general son una integración de componentes de varios proveedores. Para encontrar una solución a problemas de este tipo, es muy importante hacer planeamientos entre los requerimientos y la fase de diseño. Esto minimizará la cantidad de fallos directos en el código.</li>
<li>Documentación de requerimientos: Los documentos de ingeniería de requerimientos son largos. La mayoría están compuestos de cientos o miles de páginas, donde cada página contiene muchos detalles que pueden tener efectos profundos en el resto del sistema. Normalmente, las personas se encuentran con dificultades para comprender documentos de este tamaño, sobre todo si lo leen cuidadosamente. Es casi imposible leer un documento de especificación de gran tamaño, pues difícilmente una persona puede memorizar los detalles del documento. Esto causa problemas y errores que no son detectados hasta después de haberse construido el sistema.</li>
</ul><h2>Metodología de la Ingeniería de Requerimientos</h2>
<h3>Objetivo de la Metodología</h3>
<p>El objetivo de esta metodología es la definición de las tareas a realizar, los productos a obtener y las técnicas a emplear durante la actividad de elicitación de requerimientos de la fase de ingeniería de requerimientos del desarrollo de software.</p>
<p>En esta metodología se distinguen dos tipos de productos: los productos entregables y los productos no entregables o internos. Los productos entregables son aquellos que se entregan oficialmente al cliente como parte del desarrollo en fechas previamente acordadas, mientras que los no entregables son productos internos al desarrollo que no se entregan al cliente.</p>
<p>El único producto entregable definido en esta metodología es el Documento de Requerimientos del Sistema (DRS). La estructura de este documento es la siguiente: tareas recomendadas, productos entregables (en este caso el DRS), y por último, se describen algunas de las técnicas recomendadas para obtener productos. También se incluye como apéndice un ejemplo de aplicación de esta metodología.</p>
<h3>Tareas Recomendadas</h3>
<p>Las tareas recomendadas para obtener los productos descritos en esta metodología son las siguientes:</p>
<ul><li><strong>Tarea 1</strong>: Obtener información sobre el dominio del problema y el sistema actual.</li>
<li><strong>Tarea 2</strong>: Preparar y realizar las reuniones de elicitación/negociación.</li>
<li><strong>Tarea 3</strong>: Identificar/revisar los objetivos del sistema.</li>
<li><strong>Tarea 4</strong>: Identificar/revisar los requerimientos de almacenamiento de información.</li>
<li><strong>Tarea 5</strong>: Identificar/revisar los requerimientos funcionales.</li>
<li><strong>Tarea 6</strong>: Identificar/revisar los requerimientos no funcionales.</li>
<li><strong>Tarea 7</strong>: Priorizar objetivos y requerimientos.</li>
</ul><p>El orden recomendado de realización para estas tareas e: 1 … 7, aunque las tareas 4, 5 y 6 pueden realizarse simultáneamente o en cualquier orden que se considere oportuno (ver figura). La tarea 1 es opcional y depende del conocimiento previo que tenga el equipo de desarrollo sobre el dominio del problema y el sistema actual.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/tareas_recomendadas.png?w=825"/></p>
<h3>Tarea 1: Obtener información sobre el dominio del problema y el sistema actual</h3>
<p><strong>Objetivos</strong></p>
<ul><li>Conocer el dominio del problema.</li>
<li>Conocer la situación actual.</li>
</ul><p><strong>Descripción</strong></p>
<p>Antes de mantener las reuniones con los clientes y usuarios e identificar los requerimientos es fundamental conocer el dominio del problema y los contexto organizacional y operacional, es decir, la situación actual.</p>
<p>Enfrentarse a un desarrollo sin conocer las características principales ni el vocabulario propio de su dominio suele provocar que el producto final no sea el esperado por clientes ni usuarios.</p>
<p>Por otro lado, mantener reuniones con clientes y usuarios sin conocer las características de su actividad hará que probablemente no se entiendan sus necesidades, y que su confianza inicial hacia el desarrollo se vea deteriorada enormemente.</p>
<p>Esta tarea es opcional, ya que puede que no sea necesario realizarla si el equipo de desarrollo tiene experiencia en el dominio del problema y el sistema actual es conocido.</p>
<p><strong>Productos internos</strong></p>
<ul><li>Información recopilada: libros, artículos, folletos comerciales, desarrollos previos sobre el mismo dominio, etc.</li>
<li>Modelos del sistema actual.</li>
</ul><p><strong>Productos entregables</strong></p>
<ul><li>Introducción, participantes en el proyecto (principalmente clientes y desarrolladores), y descripción del sistema actual como parte del DRS.</li>
</ul><p><strong>Técnicas recomendadas</strong></p>
<p>Obtener información de fuentes externas al negocio del cliente: folletos, informes sobre el sector, publicaciones, consultas con expertos, etc.</p>
<ul><li>En el caso de que se trate de un dominio muy específico puede ser necesario recurrir a fuentes internas al propio negocio del cliente, en cuyo caso pueden utilizarse las técnicas auxiliares de elicitación de requerimientos como el estudio de documentación, observación in situ, cuestionarios, inmersión o apredizaje, etc.</li>
<li>Modelado del sistema actual.</li>
</ul><h3>Tarea 2: Preparar y realizar las sesiones de elicitación/negociación</h3>
<p><strong>Objetivos</strong></p>
<ul><li>Identificar a los usuarios participantes.</li>
<li>Conocer las necesidades de clientes y usuarios.</li>
<li>Resolver posibles conflictos.</li>
</ul><p><strong>Descripción</strong></p>
<p>Teniendo en cuenta la información recopilada en la tarea anterior, en esta tarea se deben preparar y realizar las reuniones con los clientes y usuarios participantes con objeto de obtener sus necesidades y resolver posibles conflictos que se hayan detectado en iteraciones previas al proceso.</p>
<p>Esta tarea es especialmente crítica y ha de realizarse con especial cuidado, ya que generalmente el equipo de desarrollo no conoce los detalles específicos de la organización para la que se va a desarrollar el sistema y, por otra parte, los clientes y posibles usuarios no saben qué necesita saber el equipo de desarrollo para llevar a cabo su labor.</p>
<p><strong>Productos internos</strong></p>
<ul><li>Notas tomadas durante las reuniones, transcripciones o actas de reuniones, formularios, grabaciones en cinta o vídeo de las reuniones o cualquier otra documentación que se considere oportuna.</li>
</ul><p><strong>Productos entregables</strong></p>
<ul><li>Participantes en el proyecto, en concreto los usuarios participantes, como parte del DRS.</li>
<li>Objetivos, requerimientos o conflictos, que se hayan identificado claramente durante las sesiones de elicitación, como parte del DRS.</li>
</ul><p><strong>Técnicas recomendadas</strong></p>
<ul><li>Técnicas de elicitación de requerimientos.</li>
<li>Técnicas de negociación como WinWin.</li>
</ul><h3>Tarea 3: Identificar/revisar los objetivos del sistema</h3>
<p><strong>Objetivos</strong></p>
<ul><li>Identificar los objetivos que se esperan alcanzar mediante el sistema software a desarrollar.</li>
<li>Revisar, en el caso de que haya conflictos, los objetivos previamente identificados.</li>
</ul><p><strong>Descripción</strong></p>
<p>A partir de la información obtenida en la tarea anterior, en esta tarea se deben identificar qué objetivos se esperan alcanzar una vez que el sistema software a desarrollar se encuentre en explotación o revisarlos en función de los conflictos identificados. Puede que los objetivos hayan sido proporcionados antes de comenzar el desarrollo.</p>
<p><strong>Productos internos</strong></p>
<ul><li>No hay productos internos en esta tarea.</li>
</ul><p><strong>Productos entregables</strong></p>
<ul><li>Objetivos del sistema como parte del DRS.</li>
</ul><p><strong>Técnicas recomendadas</strong></p>
<ul><li>Análisis de factores críticos de éxito o alguna técnica similar de identificación de objetivos.</li>
<li>Especificación de los objetivos del sistema.</li>
</ul><h3>Tarea 4: Identificar/revisar los requerimientos de almacenamiento de información</h3>
<p><strong>Objetivos</strong></p>
<ul><li>Identificar los requerimientos de almacenamiento de información que deberá cumplir el sistema software a desarrollar.</li>
<li>Revisar, en el caso de que haya conflictos, los requerimientos de almacenamiento de información previamente identificados.</li>
</ul><p><strong>Descripción</strong></p>
<p>A partir de la información obtenida en las tareas 1 y 2, y teniendo en cuenta los objetivos identificados en la tarea 3 y el resto de los requerimientos, en esta tarea se debe identificar (o revisar si existen conflictos) qué información relevante para el cliente deberá gestionar y almacenar el sistema software a desarrollar.</p>
<p>Inicialmente se partirán de conceptos generales para posteriormente ir detallándolos hasta obtener todos los datos relevantes.</p>
<p><strong>Productos internos</strong></p>
<ul><li>No hay productos internos en esta tarea.</li>
</ul><p><strong>Productos entregables</strong></p>
<ul><li>Requerimientos de almacenamiento de información como parte del DRS.</li>
</ul><p><strong>Técnicas recomendadas</strong></p>
<ul><li>Definición de requerimientos de almacenamiento de información</li>
</ul><h3>Tarea 5: Identificar/revisar los requerimientos funcionales</h3>
<p><strong>Objetivos</strong></p>
<ul><li>Identificar los actores del sistema de software a desarrollar.</li>
<li>Identificar los requerimientos funcionales (casos de uso) que deberá cumplir el sistema software a desarrollar.</li>
<li>Revisar, en el caso de que haya conflictos, los requerimientos funcionales previamente identificados.</li>
</ul><p><strong>Descripción</strong></p>
<p>A partir de la información obtenida en las tareas 1 y 2, y teniendo en cuenta los objetivos identificados en la tarea 3 y el resto de los requerimientos, en esta tarea se debe identificar (o revisar si existen conflictos) qué debe hacer el sistema a desarrollar con la información identificada en la tarea anterior.</p>
<p>Inicialmente se identificarán los actores que interactuarán con el sistema, es decir aquellas personas u otros sistema que serán los orígenes o destinos de la información que consumirá o producirá el sistema a desarrollar y que forman su entorno.</p>
<p>A continuación se identificarán los casos de uso asociados a los actores, los pasos de cada caso de uso, y posteriormente se detallarán los casos de uso con las posibles excepciones hasta definir todas las situaciones posibles.</p>
<p><strong>Productos internos</strong></p>
<ul><li>No hay productos internos en esta tarea.</li>
</ul><p><strong>Productos entregables</strong></p>
<ul><li>Requerimientos funcionales como parte del DRS.</li>
</ul><p><strong>Técnicas recomendadas</strong></p>
<ul><li>Casos de uso.</li>
<li>Definición de actores.</li>
<li>Definición de los requerimientos funcionales.</li>
</ul><h3>Tarea 6: Identificar/revisar los requerimientos no funcionales</h3>
<p><strong>Objetivos</strong></p>
<ul><li>Identificar los requerimientos no funcionales del sistema software a desarrollar.</li>
</ul><p><strong>Descripción</strong></p>
<p>A partir de la información obtenida en las tareas 1 y 2, y teniendo en cuenta los objetivos identificados en la tarea 3 y el resto de los requerimientos, en esta tarea se deben identificar (o revisar si existen conflictos), los requerimientos no funcionales, normalmente de carácter técnico o legal.</p>
<p>Algunos tipos de requerimientos que se suelen incluir en esta sección son los siguientes:</p>
<ul><li><strong>Requerimientos de comunicaciones del sistema</strong>: Son requerimientos de carácter técnico relativos a las comunicaciones que deberá soportar el sistema software a desarrollar. Por ejemplo: el sistema deberá utilizar el protocolo TCP/IP para las comunicaciones con otros sistemas.</li>
<li><strong>Requerimientos de interfaz de usuario</strong>: Este tipo de requerimientos especifica las características que deberá tener el sistema en su comunicación con el usuario. Por ejemplo: la interfaz de usuario del sistema deberá ser consistente con los estándares definidos en IBM’s Common User Access. Se debe ser cuidadoso con este tipo de requerimientos, ya que, en esta fase de desarrollo todavía no se conocen bien las dificultades que pueden sufrir&nbsp; ala hora de diseñar e implementar las interfaces, por esto no es conveniente entrar en detalles demasiado específicos.</li>
<li><strong>Requerimientos de fiabilidad</strong>: Los requerimientos de fiabilidad deben establecer los factores que se requieren para la fiabilidad del software en tiempo de explotación. La fiabilidad mide la probabilidad del sistema de producir una respuesta satisfactoria a las demandas del usuario. Por ejemplo: la tasa de fallos del sistema no podrá ser superior a 2 fallos por semana.</li>
<li><strong>Requerimientos de entorno de desarrollo</strong>: Este tipo de requerimientos especifican si el sistema debe desarrollarse con un producto específico. Por ejemplo: el sistema deberá desarrollarse con Oracle 7 como servidor y clientes Visual Basic 4.</li>
<li><strong>Requerimientos de portabilidad</strong>: Los requerimientos de portabilidad definen qué características deberá tener el software para que sea fácil utilizarlo en otra máquina o bajo otro sistema operativo. Por ejemplo: el sistema deberá funcionar en los sistemas operativos Windows 95, Windows 98 y Windows NT 4.0, siendo además posible el acceso al sistema a través de Internet usando cualquier navegador compatible con HTML 4.0.</li>
</ul><p><strong>Productos internos</strong></p>
<ul><li>No hay productos internos en esta tarea.</li>
</ul><p><strong>Productos entregables</strong></p>
<ul><li>Requerimientos no funcionales del sistema como parte del DRS.</li>
</ul><p><strong>Técnicas recomendadas</strong></p>
<ul><li>Definición de requerimientos no funcionales</li>
</ul><h3>Productos Entregables</h3>
<p>El único producto entregable que se contempla en esta metodología es el Documento de Requerimientos del Sistema (DRS).</p>
<p><strong>Documento de Requerimientos del Sistema</strong></p>
<p>La estructura del DRS puede verse en la siguiente figura. En las siguientes secciones se describe con detalle cada sección del DRS.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/drs.png?w=825"/></p>
<p><strong>Portada</strong></p>
<p>La portada del DRS debe tener el formato que puede verse en la siguiente figura:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/portada.png?w=825"/></p>
<p>Los elementos que deben aparecer son los siguientes:</p>
<ul><li><strong>Nombre del proyecto</strong>: el nombre del proyecto al que pertenece el DRS.</li>
<li><strong>Versión</strong>: la versión del DRS que se entrega al cliente. La versión se compone de dos números X e Y. El primero indica la versión, y se debe incrementar cada vez que se hace una nueva entrega formal al cliente. Cuando se incremente el primer número, el segundo debe volver a comenzar en cero. El segundo número indica cambios dentro de la misma versión aún no entregada,y se debe incrementar cada vez que se publica una versión con cambios respecto a la última que se publicó y que no se vaya a entregar formalmente todavía. Este tipo de versiones pueden ser internas al equipo de desarrollo o ser entregadas al cliente a título orientativo.</li>
<li><strong>Fecha</strong>: fecha de la publicación de la versión.</li>
<li><strong>Equipo de desarrollo</strong>: nombre de la empresa o equipo de desarrollo.</li>
<li><strong>Cliente</strong>: nombre del cliente, normalmente otra empresa.</li>
</ul><p><strong>Lista de cambios</strong></p>
<p>El documento debe incluir una lista de cambios en la que se especifiquen, para cada versión del documento, los cambios producidos en el mismo con un formato similar al que puede verse en la siguiente figura. Para cada cambio realizado se debe incluir el número de orden, la fecha, una descripción y los autores.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/lista_cambios.png?w=825"/></p>
<p><strong>Índice</strong></p>
<p>El índice del DRS debe indicar la página en la que se comienza cada sección, subsección o apartado del documento. En la medida de los posible, se sangrarán las entradas del índice para ayudar a comprender la estructura del documento.</p>
<p><strong>Listas de figuras y tablas</strong></p>
<p>El DRS deberá incluir listas de las figuras y tablas que aparezcan en el mismo. Dichas listas serán dos índices que indicarán el número, la descripción y la página en que aparece cada figura o tabla del DRS.</p>
<p><strong>Introducción</strong></p>
<p>Esta sección debe contener una descripción breve de las principales características del sistema software que se va a desarrollar, la situación actual que genera la necesidad del nuevo desarrollo, la problemática que se acomete, y cualquier otra consideración que sitúe al posible lector en el contexto oportuno para comprender el resto del documento.</p>
<p><strong>Participantes en el proyecto</strong></p>
<p>Esta sección debe contener una lista con todos los participantes en el proyecto, tanto desarrolladores como clientes y usuarios. Para cada participante se deberá indicar su nombre, el papel que desempeña en el proyecto, la organización a la que pertenece y cualquier otra información adicional que se considere oportuna.</p>
<p><strong>Descripción del sistema actual</strong></p>
<p>Esta sección debe contener una descripción del sistema actual en el caso de que se haya acometido su estudio. Para describir el sistema actual puede utilizarse cualquier técnica que se considere oportuno.</p>
<p><strong>Objetivos del sistema</strong></p>
<p>Esta sección debe contener una lista con los objetivos que se esperan alcanzar cuando el sistema software a desarrollar esté en explotación.</p>
<p><strong>Catálogo de requerimientos del sistema</strong></p>
<p>Esta sección se divide en subsecciones en las que se describen los requerimientos del sistema.</p>
<p>Cada uno de los grandes grupos de requerimientos (de almacenamiento de información, funcionales y no funcionales) podrá dividirse para ayudar a la legibilidad del documento, por ejemplo dividiendo cada subsección en requerimientos asociados a un determinado objetivo, requerimientos con características comunes, etc.</p>
<p><strong>Requerimientos de almacenamiento de información</strong></p>
<p>Esta subsección debe contener la lista de requerimientos de almacenamiento de información que se hayan identificado.</p>
<p><strong>Requerimientos funcionales</strong></p>
<p>Esta subsección debe contener la lista de requerimientos funcionales que se hayan identificado, dividiéndose en los siguientes apartados que se describen a continuación:</p>
<ul><li><strong>Diagrama de casos de uso</strong>: Este apartado debe contener los diagramas de casos de uso del sistema que se hayan realizado.</li>
<li><strong>Definición de los actores</strong>: Este apartado debe contener una lista con los actores que se hayan identificado.</li>
<li><strong>Casos de uso del sistema</strong>: Este apartado debe contener los casos de uso que se hayan identificado.</li>
</ul><p><strong>Requerimientos no funcionales</strong></p>
<p>Esta subsección debe contener la lista de los requerimientos no funcionales del sistema que se hayan identificado.</p>
<p><strong>Matriz de rastreabilidad objetivos/requerimientos</strong></p>
<p>Esta sección debe contener una matriz objetivo-requisito, de forma que para cada objetivo se pueda conocer con qué requerimientos está asociado. El formato de la matriz de rastreabilidad puede verse en la siguiente figura:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/matriz_rastreabilidad.png?w=825"/></p>
<p><strong>Conflictos pendientes de resolución</strong></p>
<p>Esta sección, que se incluirá en el caso de que no se opte por registrar los conflictos en un documento aparte, deberá contener los conflictos identificados durante el proceso y que aún están pendientes de resolución.</p>
<p><strong>Glosario de términos</strong></p>
<p>Esta sección, que se incluirá si se considera oportuno, deberá contener una lista ordenada alfabéticamente de los términos específicos del dominio del problema, acrónimos y abreviaturas que aparezcan en el documento y que se considere que su significado deba ser aclarado. Cada término deberá acompañarse de su significado.</p>
<p><strong>Apéndices</strong></p>
<p>Los apéndices se usarán para proporcionar información adicional a la documentación obligatoria del documento. Sólo deben aparecer si se consideran oportunos y se identificarán con letras ordenadas alfabéticamente: A, B, C, etc.</p>
<h3>Técnicas</h3>
<p>A continuación, se describen algunas de las técnicas que se proponen en esta metodología para obtener los productos de las tareas que se han descrito. Las técnicas más habituales en la elicitación de requerimientos son las entrevistas, el Joint Application Development (JAD) o Desarrollo Conjunto de Aplicaciones, el brainstorming o tormenta de ideas y la utilización de escenarios, más conocidos como casos de uso.</p>
<p>Estas técnicas, que se describen en los siguientes apartados, se suelen completar con otras técnicas complementarias como la observación in situ, el estudio de documentación, los cuestionarios, la inmersión en el negocio del cliente o haciendo que los ingenieros de requerimientos sean aprendices del cliente.</p>
<p><strong>Entrevistas</strong></p>
<p>Las entrevistas son la técnica de elicitación más utilizada, y de hecho son practicamente inevitables en cualquier desarrollo ya que son una de las formas de comunicación más naturales entre personas. En las entrevistas se pueden identificar tres fases: preparación, realización y análisis.</p>
<ul><li><strong>Preparación de entrevistas</strong>: Las entrevistas no deben improvisarse, por lo que conviene realizar las siguientes tareas previas:
<ul><li><strong>Estudiar el dominio del problema</strong>: Conocer las categorías y conceptos de la comunidad de clientes y usuarios es fundamental para poder entender las necesidades de dicha comunidad y su forma de expresarlas, y para generar en los clientes y usuarios la confianza de que el ingeniero de requerimientos entiende sus problemas. Para conocer el dominio del problema se puede recurrir a técnicas de estudio de documentación, a bibliografía sobre el tema, documentación de proyectos similares realizados anteriormente, la inmersión dentro de la organización para la que se va a desarrollar o a periodos de aprendizaje por parte de los ingenieros de requerimientos.</li>
<li><strong>Seleccionar a las personas a las que se va a entrevistar</strong>: Se debe minimizar el número de entrevistas a realizar, por lo que es fundamental seleccionar a las personas a entrevistar. Normalmente se comienza por los directivos (que pueden ofrecer una visión global), y se continúa con los futuros usuarios (que pueden aportar información más detallada) y con el personal técnico (que aporta detalles sobre el entorno operacional de la organización). Conviene también estudiar el perfil de los entrevistados, buscando puntos en común con el entrevistador que ayuden a romper el hielo.</li>
<li><strong>Determinar el objetivo y contenido de las entrevistas</strong>: Para minimizar el tiempo de la entrevista es fundamental fijar el objetivo que se pretende alcanzar y determinar previamente su contenido. Previamente a su realización, se pueden enviar cuestionarios (que los futuros entrevistados deben rellenar y devolver) y un pequeño documento de introducción al proyecto de desarrollo (de forma que el entrevistado conozca los temas que se van a tratar, y el entrevistador recoja información para preparar la entrevista). Es importante que los cuestionarios, si se usan, se preparen cuidadosamente teniendo en cuenta quién los va a responder y no incluir conceptos que se asuman conocidos cuando puedan no serlo.</li>
<li><strong>Planificar las entrevistas</strong>: La fecha, hora, lugar y duración de la entrevista deben fijarse teniendo en cuenta siempre la agenda del entrevistado. En general, se deben buscar sitios agradables donde no se produzcan interrupciones y que resulten naturales a los entrevistados.</li>
</ul></li>
<li><strong>Realización de entrevistas</strong>: Dentro de la realización de las entrevistas se distinguen tres etapas:
<ul><li><strong>Apertura</strong>: El entrevistador debe presentarse e informar al entrevistado sobre la razón de la entrevista, qué se espera conseguir, cómo se utilizará la información, la mecánica de las preguntas, etc. Si se va a utilizar algún tipo de notación gráfica o matemática que el entrevistado no conozca debe explicarse antes de utilizarse. Es fundamental causar buena impresión en los primeros minutos.</li>
<li><strong>Desarrollo</strong>: La entrevista en sí no debería durar más de dos horas, distribuyendo el tiempo en un 20% para el entrevistador y un 80% para el entrevistado. Se deben evitar los monólogos y mantener el control por parte del entrevistador, contemplando la posibilidad de que una tercera persona tome notas durante la entrevista o grabar la entrevista en cinta de vídeo o audio, siempre que el entrevistado esté de acuerdo. Durante esta fase se pueden emplear distintas técnicas:
<ul><li><strong>Preguntas abiertas</strong>: También denominadas de libre contexto, estas preguntas no pueden responderse con un “sí” o un “no”, permiten una mayor comunicación y evitan la sensación de interrogatorio. Por ejemplo, “¿Qué se hace para registrar un pedido?”, “Dígame qué se debe hacer cuando un cliente pide una factura” o “¿Cómo se rellena un albarán?”. Estas preguntas se suelen utilizar al comienzo de la entrevista, pasando posteriormente a preguntas más concretas. En general, se debe evitar la tendencia de anticipar una respuesta a las preguntas que se formulan.</li>
<li><strong>Utilizar palabras apropiadas</strong>: Se deben evitar tecnicismos que no conozca el entrevistado y palabras o frases que puedan perturbar emocionalmente la comunicación.</li>
<li><strong>Mostrar interés en todo momento</strong>: Es fundamental cuidar la comunicación no verbal durante la entrevista: tono de voz, movimiento, expresión facial, etc. Por ejemplo, para animar a alguien a hablar puede asentirse con la cabeza, decir “ya entiendo”, “sí”, repetir algunas respuestas dadas, hacer pausas, poner una postura de atención, etc. Debe evitarse bostezar, reclinarse en el sillón, mirar hacia otro lado, etc.</li>
</ul></li>
<li><strong>Terminación</strong>: Al terminar la entrevista se debe recapitular para confirmar que no ha habido confusiones en la información recogida, agradecer al entrevistado su colaboración y citarle para una nueva entrevista si fuera necesario, dejando siempre abierta la posibilidad de volver a contactar para aclarar dudas que surjan al estudiar la información o al contrastarla con otros entrevistados.</li>
</ul></li>
<li><strong>Análisis de las entrevistas</strong>: Una vez realizada la entrevista es necesario leer las notas tomadas, pasarlas a limpio, reorganizar la información, contrastarla con otras entrevistas o fuentes de información, etc. Una vez elaborada la información, se puede enviar al entrevistado para confirma los contenidos. También es importante evaluar la propia entrevista para determinar los aspectos mejorables.</li>
</ul><p><strong>Joint Application Development (JAD)</strong></p>
<p>La técnica denominada JAD (Joint Application Development, Desarrollo Conjunto de Aplicaciones), desarrollada por IBM en 1977, es una alternativa a las entrevistas individuales que se desarrolla a lo largo de un conjunto de reuniones en grupo durante un periodo de 2 a 4 días. En estas reuniones se ayuda a los clientes y usuarios a formular problemas y explorar posibles soluciones, involucrándolos y haciéndolos sentirse partícipes del desarrollo.</p>
<p>Esta técnica se basa en cuatro principios: dinámica de grupo, el uso de ayudas visuales para mejorar la comunicación (diagramas, transparencias, multimedia, herramientas CASE, etc.), mantener un proceso organizado y racional y una filosofía de documentación WYSIWYG (What You See Is What You Get, lo que se ve es lo que se obtiene), por la que durante las reuniones se trabaja directamente sobre los documentos a generar.</p>
<p>El JAD tienen dos grandes pasos, el JAD/Plan (cuyo objetivo es elicitar y especificar requerimientos) y el JAD/Design (en el que se aborda el diseño del software). En este documento sólo se verá con detalle el primero de ellos. Debido a las necesidades de organización que requiere y a que no suele adaptarse bien a los horarios de trabajo de los clientes y usuarios, esta técnica no suele emplearse con frecuencia, aunque cuando se aplica suele tener buenos resultados, especialmente para elicitar requerimientos en el campo de los sistemas de información.</p>
<p>En comparación con las entrevistas individuales, presenta las siguientes ventajas:</p>
<ul><li>Ahorra tiempo al evitar que las opiniones de los clientes se contrasten por separado.</li>
<li>Todo el grupo, incluyendo los clientes y los futuros usuarios, revisa la documentación generada, no sólo los ingenieros de requerimientos.</li>
<li>Implica más a los clientes y usuarios en el desarrollo.</li>
</ul><p>El JAD queda definida a través de los siguientes elementos:</p>
<ul><li><strong>Participantes del JAD</strong>: Se pueden distinguir seis clases de participantes o roles en el JAD:
<ul><li><strong>Jefe del JAD</strong>: Es el responsable de todo el proceso y asume el control durante las reuniones. Debe tener dotes de comunicación y liderazgo. Algunas habilidades importantes que debe tener son: entender y promover la dinámica de grupo, iniciar y centrar discusiones, reconocer cuándo la reunión se está desviando del tema y reconducirla, manejar las distintas personalidades y formas de ser de los participantes, evitar que decaiga la reunión aunque sea larga y difícil, etc.</li>
<li><strong>Analista</strong>: Es el responsable de la producción de los documentos que se deben generar durante las sesiones JAD. Debe tener la habilidad de organizar bien las ideas y expresarlas claramente por escrito. En el caso de que se utilicen herramientas software durante las sesiones, debe ser capaz de manejarlas eficientemente.</li>
<li><strong>Patrocinador ejecutivo</strong>: Es el que tiene la decisión final de que se lleve a cabo el desarrollo. Debe proporcionar a los demás participantes información sobre la necesidad del nuevo sistema y los beneficios que se espera obtener de él.</li>
<li><strong>Representantes de los usuarios</strong>: Durante el JAD/Plan suelen ser directivos con una visión global del sistema. Durante el JAD/Design suelen incorporarse futuros usuarios finales.</li>
<li><strong>Representantes de sistemas de información</strong>: Son personas expertas en sistemas de información que deben ayudar a los usuarios a comprender qué es o no factible con la tecnología actual y el esfuerzo que implica.</li>
<li><strong>Especialistas</strong>: Son personas que pueden proporcionar información detallada sobre aspectos muy concretos, tanto desde el punto de vista de los usuarios porque conocen muy bien el funcionamiento de una parte de la organización, como desde el punto de vista de los desarrolladores porque conocen perfectamente ciertos aspectos técnicos de la instalación hardware de la organización.</li>
</ul></li>
<li><strong>Fases del JAD</strong>: Dentro de la técnica del JAD se distinguen tres fases:
<ul><li><strong>Adaptación</strong>: Es responsabilidad del jefe del JAD, ayudado por uno o dos analistas, adaptar la técnica del JAD para cada proyecto. La adaptación debe comenzar por definir el proyecto a alto nivel, para lo cual pueden ser necesarias entrevistas previas con algunos clientes y usuarios. También suele ser necesario recabar información sobre la organización para familiarizarse con el dominio del problema, por ejemplo utilizando técnicas complementarias como el estudio de documentación o la observación in situ. Una vez obtenida una primera idea de los objetivos del proyecto, es necesario seleccionar a los participantes,citarles para las reuniones y proporcionarles una lista con los temas que se van a tratar en las reuniones para que las puedan preparar. El jefe del JAD debe decidir la duración y el número de sesiones a celebrar, definir el formato de la documentación sobre la que se trabajará y preparar transparencias introductorias y todo el material audiovisual que considere oportuno.</li>
<li><strong>Celebración de las sesiones JAD</strong>: Durante las sesiones, los participantes exponen sus ideas y se discuten, analizan y refinan hasta alcanzar un acuerdo. Los pasos que se recomienda seguir para este proceso son los siguientes:
<ul><li><strong>Presentación</strong>: Se presenta y se da la bienvenida a todos los participantes por parte del patrocinador ejecutivo y del jefe del JAD. El patrocinador ejecutivo expone brevemente las necesidades que han llevado al desarrollo y los beneficios que se esperan obtener. El jefe del JAD explica la mecánica de las sesiones y la planificación prevista.</li>
<li><strong>Definir objetivos y requerimientos</strong>: El jefe del JAD promueve la discusión para elicitar los objetivos o requerimientos de alto nivel mediante preguntas como: “¿Por qué se construye el sistema?”, “¿Qué beneficios se esperan del nuevo sistema?”, “¿Cómo puede beneficiar a la organización en el futuro?”, “¿Qué restricciones de recursos disponibles, normas o leyes afectan al proyecto?”, “¿Es importante la seguridad de los datos?”. A medida que se van elicitando requerimientos, el analista los escribe en transparencias o en algún otro medio que permita que permanezcan visibles durante la discusión.</li>
<li><strong>Delimitar el ámbito del sistema</strong>:&nbsp; Una vez obtenido un número importante de requerimientos, es necesario organizarlos y llegar a un acuerdo sobre el ámbito del nuevo sistema. En el caso de los sistemas de información, es útil identificar a los usuarios potenciales (actores) y determinar qué tareas les ayudará a realizar (casos de uso).</li>
<li><strong>Documentar temas abiertos</strong>: Aquellas cuestiones que hayan surgido durante la sesión que no se han podido resolver, deben documentarse para las siguientes sesiones y ser asignadas a una persona responsable de su solución para una fecha determinada.</li>
<li><strong>Concluir la sesión</strong>: El jefe del JAD concluye la sesión revisando con los demás participantes la información elicitada y las decisiones tomadas. Se da la oportunidad a todos los participantes de expresar cualquier consideración adicional, fomentando por parte del jefe del JAD el sentimiento de propiedad y compromiso de todos los participantes sobre los requerimientos elicitados.</li>
</ul></li>
<li><strong>Conclusión</strong>: Una vez terminadas las sesiones es necesario transformar las transparencias, notas y demás documentación generada en documentos formales. Se distinguen tres pasos:
<ul><li><strong>Completar la documentación</strong>: Los analistas recopilan la documentación generada durante las sesiones en documentos conformes a las normas o estándares vigentes en la organización para la que se desarrolla el proyecto.</li>
<li><strong>Revisar la documentación</strong>: La documentación generada se envía a todos los participantes para que la comenten. Si los comentarios son lo suficientemente importantes, se convoca otra reunión para discutirlos.</li>
<li><strong>Validar la documentación</strong>: Una vez revisados todos los comentarios, el jefe del JAD envía el documento al patrocinador ejecutivo para su aprobación. Una vez aprobado el documento se envían copias definitivas a cada uno de los participantes.</li>
</ul></li>
</ul></li>
</ul><p><strong>Brainstorming</strong></p>
<p>El brainstorming o tormenta de ideas es una técnica de reuniones en grupo cuyo objetivo es la generación de ideas en un ambiente libre de críticas o juicios. Las sesiones de brainstorming suelen estar formadas por un número de cuatro a diez participantes, uno de los cuales es el jefe de sesión, encargado más de comenzar la sesión que de controlarla. Como técnica de elicitación de requerimientos, el brainstorming puede ayudar a generar una gran variedad de vistas del problema, y a formularlo de diferentes formas, sobre todo al comienzo del proceso de elicitación cuando los requerimientos son todavía muy difusos.</p>
<p>Frente al JAD, el brainstorming tiene la ventaja de que es muy fácil de aprender y requiere poca organización, de hecho, hay propuestas de realización de brainstorming por vídeoconferencia a través de internet. Por otro lado, al ser un proceso poco estructurado, puede no producir resultados con la misma calidad o nivel de detalle que otras técnicas.</p>
<p>El brainstorming se puede describir a través de los siguientes elementos:</p>
<ul><li><strong>Fases del brainstorming</strong>: En elbrainstorming se distinguen las siguientes fases:
<ul><li><strong>Preparación</strong>: La preparación para una sesión de brainstorming requiere que se seleccione a los participantes y al jefe de la sesión, citarlos y preparar la sala donde se llevará a cabo la sesión. Los participantes en una sesión de brainstorming para elicitación de requerimientos son normalmente clientes, usuarios, ingenieros de requerimientos, desarrolladores y, si es necesario, algún experto en temas relevantes para el proyecto.</li>
<li><strong>Generación</strong>: El jefe abre la sesión exponiendo un enunciado general del problema a tratar, que hace de semilla para que se vayan generando ideas. Los participantes aportan libremente nuevas ideas sobre el problema semilla, bien por un orden establecido por el jefe de la sesión, bien aleatoriamente. El jefe es siempre el responsable de dar la palabra a un participante. Este proceso continúa hasta que el jefe decide parar, bien porque no se están generando suficientes ideas, en cuyo caso la reunión se pospone, bien porque el número de ideas sea suficiente para pasar a la siguiente fase. Durante esta fase se deben observar las siguientes reglas:
<ul><li>Se prohíbe la crítica de ideas, de forma que los participantes se sientan libres de formular cualquier idea.</li>
<li>Se fomentan las ideas más avanzadas, que aunque no sean factibles, estimulan a los demás participantes a explorar nuevas soluciones más creativas.</li>
<li>Se debe generar un gran número de ideas, ya que cuantas más ideas se presenten más probable será que se generen mejores ideas.</li>
<li>Se debe alentar a los participantes a combinar o completar las ideas de otros participantes. Para ello, es necesario, al igual que en la técnica del JAD, que todas las ideas generadas estén visibles para todos los participante en todo momento. Una posibilidad es utilizar como semilla objetivos del sistema e ir identificando requerimientos.</li>
</ul></li>
<li><strong>Consolidación</strong>: En esta fase se deben organizar y evaluar las ideas generadas durante la fase anterior. Se suelen seguir tres pasos:
<ul><li><strong>Revisar ideas</strong>: Se revisan las ideas generadas para clarificarlas. Es habitual identificar ideas similares, en cuyo caso se unifican en un solo enunciado.</li>
<li><strong>Descartar ideas</strong>: Aquellas ideas que los participantes consideren excesivamente avanzadas se descartan.</li>
<li><strong>Priorizar ideas</strong>: Se priorizan las ideas restantes, identificando las absolutamente esenciales, las que estarían bien pero que no son esenciales, y las que podrían ser apropiadas para una próxima versión del sistema a desarrollar.</li>
</ul></li>
<li><strong>Documentación</strong>: Después de la sesión, el jefe produce la documentación oportuna conteniendo las ideas priorizadas y comentarios generados durante la consolidación.</li>
</ul></li>
</ul><p><strong>Casos de uso</strong></p>
<p>Los casos de uso son una técnica para la especificación de requerimientos funcionales propuesta inicialmente en Jacobson y que actualmente forma parte de UML.</p>
<p>Un caso de uso es la descripción de una secuencia de interacciones entre el sistema y uno o más actores en la que se considera al sistema como una caja negra y en la que los actores obtienen resultados observables en la siguiente figura:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/caso_de_uso.png?w=825"/></p>
<p>Los actores son personas u otros sistemas que interactúan con el sistema cuyos requerimientos se están describiendo.</p>
<p>Los casos de uso presentan ciertas ventajas sobre la descripción meramente textual de los requerimientos funcionales, ya que facilitan la elicitación de requerimientos y son fácilmente comprensibles por los clientes y usuarios. Además, pueden servir de base a las pruebas del sistema y a la documentación para los usuarios.</p>
<p>A pesar de ser una técnica ampliamente aceptada, existen múltiples propuestas para su utilización concreta. En esta metodología se propone la utilización de los casos de uso como técnica tanto de elicitación como de especificación de los requerimientos funcionales del sistema.</p>
<p><strong>Diagramas de casos de uso</strong></p>
<p>Los casos de uso tienen una representación gráfica en los denominados diagramas de casos de uso. En estos diagramas, los actores se representan en forma de pequeños monigotes, y los casos de uso se representan por elipses contenidos dentro de un rectángulo que representa al sistema. La participación de los actores en los casos de uso se indica por una flecha entre el actor y el caso de uso que apunta en la dirección en la que fluye la información. Un ejemplo de este tipo de diagramas se vio en la imagen anterior.</p>
<p>Los diagramas de casos de uso sirven para proporcionar una visión global del conjunto de casos de uso de un sistema así como de los actores y los casos de uso en los que éstos intervienen. Las interacciones concretas entre los actores y el sistema no se muestran en este tipo de diagramas.</p>
<p><strong>Relaciones entre casos de uso</strong></p>
<p>A veces conviene establecer relaciones entre distintos casos de uso para simplificar su descripción. Las dos relaciones posibles y su semántica, cuya representación gráfica puede verse en el siguiente ejemplo son las siguientes:</p>
<ul><li><strong>includes</strong>: Se dice que un caso de uso A incluye el caso de uso B, cuando B es una parte del caso de uso A, es decir, la secuencia de interacciones de B forma parte de la secuencia de interacciones de A. El caso de uso B se realiza siempre dentro del caso de uso A. Además, siempre que ocurre A ocurre también B, por lo que se dice que B es un caso de uso abstracto. Un caso de uso es abstracto si no puede ser realizado por sí mismo, por lo que sólo tiene significado cuando se utiliza para describir alguna funcionalidad que es común a otros casos de uso. Por otra parte, un caso de uso será concreto si puede ser iniciado por un actor y realizado por sí mismo. Se suele utilizar esta relación cuando se detectan subsecuencias de interacciones comunes a varios casos de uso. Dichas subsecuencias comunes se extren como “factor común” de los casos de uso que las contienen. Posteriormente son incluido por los casos de uso de los que se han “extraído”. De esta forma se evita repetir las mismas subsecuencias de interacciones una y otra vez en varios casos de uso.</li>
<li><strong>extends</strong>: Un caso de uso A extiende a otro caso de uso B cuando A es una subsecuencia de interacciones de B, que ocurre en una determinada circunstancia. En cierta forma, A completa la funcionalidad de B. El caso de uso A puede realizarse o no cuando se realiza el caso de uso B, según las circunstancias. Por otro lado, el caso de uso A puede ser un caso de uso abstracto o concreto, en cuyo caso puede ocurrir sin necesidad de que ocurra el caso de uso B.</li>
</ul><p><img src="https://gsitic.files.wordpress.com/2018/01/casos_de_uso_1.png?w=825"/></p>
<p><strong>Organización de casos de uso</strong></p>
<p>En la mayoría de sistemas, el número de casos de uso es lo suficientemente elevado como para que sea oportuno organizarlos de alguna forma en lugar de tener una lista plana por la que no es fácil navegar. Una posible forma de organizar los casos de uso es recurrir a los paquetes. De esta forma, los casos de uso pueden organizarse en niveles, facilitando así su comprensión.</p>
<p>Cada paquete contiene a otros paquetes o a varios casos de uso.</p>
<p>En el caso de que los casos de uso se agrupen por criterios funcionales, los paquetes que los agrupan pueden estereotiparse como subsistemas, tal como puede verse en la siguiente figura:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/casos_de_uso_2.png?w=825"/></p>
<h2>Prototipado</h2>
<p>Los prototipos permiten al desarrollador crear un modelo del software que debe ser construido.</p>
<p>Un prototipo es la primera versión de un nuevo tipo de producto, en el que se han incorporado sólo algunas características del sistema final, o no se han realizado completamente.</p>
<p>Es un modelo o maqueta del sistema que se construye para comprender mejor el problema y sus posibles soluciones. Esto permite:</p>
<ul><li>Evaluar mejor los requerimientos.</li>
<li>Probar opciones de diseño.</li>
</ul><p>El uso principal es la ayuda a los clientes y los desarrolladores para entender los requerimientos del sistema. El prototipo puede ser usado para entrenamiento antes de que el sistema final sea entregado. El prototipo también puede ser utilizado para pruebas.</p>
<p>Las características de los prototipos son:</p>
<ul><li>Funcionalidad limitada.</li>
<li>Poca fiabilidad.</li>
<li>Características de operación pobres.</li>
</ul><p>Hay que tener en cuenta que el prototipo representa aproximadamente un 10% del presupuesto del proyecto, y&nbsp; normalmente supone pocos días de desarrollo.</p>
<p>Al igual que todos los enfoques orientados al proceso de desarrollo del software, el prototipado comienza con la captura de requerimientos. Desarrolladores y clientes se reúnen y definen los objetivos globales del software, identifican todos los requerimientos que son conocidos, y señalan áreas en las que será necesaria la profundización en las definiciones. Después de esto, tiene lugar un “diseño rápido”. El diseño rápido se centra en una representación de aquellos aspectos del software que serán visibles al usuario (por ejemplo, entradas y formatos de las salidas). El diseño rápido lleva a la construcción de un prototipo. El prototipo es evaluado por el cliente y el usuario, y utilizado para refinar los requerimiento del software a ser desarrollado. Un proceso de iteración tiene lugar a medida que el prototipo es perfeccionado para satisfacer las necesidades del cliente y permitir al mismo tiempo una mejor comprensión del problema por parte del desarrollador.</p>
<p>Existen principalmente dos tipos de prototipos:</p>
<ul><li><strong>Prototipo rápido (concept prototype)</strong>: El prototipado rápido es un mecanismo para lograr la validación inicial. Se utiliza para validar requerimientos en una etapa previa al diseño específico. En este sentido, el prototipo puede ser visto como una aceptación tácita de que los requerimientos no son totalmente conocidos o entendidos antes del diseño y la implementación. El prototipo rápido puede ser usado como un medio para explorar nuevos requerimientos y así ayudar a controlar su constante evolución.</li>
<li><strong>Prototipo evolutivo</strong>: Desde una perspectiva diferente, todo el ciclo de vida de un producto puede ser visto como una serie incremental de detallados prototipos acumulativos. Tradicionalmente, el ciclo de vida está dividido en dos fases distintas: desarrollo y mantenimiento. La experiencia ha demostrado que esta distinción es arbitraria y va en contra de la realidad, ya que, la mayor parte del costo del software ocurre después de que el producto se ha entregado. El desarrollo evolutivo del ciclo de vida del software considera a la primera entrega como un prototipo inicial en uso. Modificaciones y mejoras subsecuentes resultan en nuevas entregas de prototipos más maduros. Este proceso continúa hasta que se haya desarrollado el producto final (véase la figura). La adopción de esta óptica elimina la distinción arbitraria entre desarrollo y mantenimiento, resultando en un importante cambio de mentalidad que afecta las estrategias para la estimación de costos, enfoques de desarrollo y adquisición de productos.</li>
</ul><p><img src="https://gsitic.files.wordpress.com/2018/01/prototipo_evolutivo.png?w=825"/></p>
<h3>Herramientas para el prototipado</h3>
<ul><li>Lenguajes dinámicos de alto nivel. Los más usados son:
<ul><li>Smalltalk (basado en objetos, sistemas interactivos)</li>
<li>Java (basado en objetos, sistemas interactivos)</li>
<li>Prolog (lógico, procesamiento simbólico)</li>
<li>LISP (basado en listas, procesamiento simbólico)</li>
</ul></li>
<li>Lenguajes de cuarta generación (4GLs) (programación de BBDD):
<ul><li>La mayoría de aplicaciones de gestión son interactivas e implican la manipulación de una BD y la producción de salidas que involucran organizar y dar formato a esos datos.</li>
<li>Lenguaje de programación de BBDD (y su entorno de desarrollo), que contiene conocimiento de la BD y operaciones para manipulación de la misma.</li>
<li>Lenguaje no procedimental.</li>
<li>Reducen claramente los costos del desarrollo.</li>
<li>Muy usados en prototipado evolutivo.</li>
<li>Muchos 4GLs permiten el desarrollo de interfaces de BBDD basadas en navegadores web.</li>
<li>General SQL o código en lenguaje “de bajo nivel” como COBOL.</li>
<li>Menos eficientes que los lenguajes de programación convencionales. Por ejemplo, un programa en 4GL reescrito en C++ tiene un 50% menos de requerimientos de memoria y es 10 veces más rápido.</li>
<li>Reducen claramente los costos del desarrollo, aunque no sucede lo mismo con el mantenimiento de los mismos, ya que:
<ul><li>Son programas no estructurados difíciles de mantener.</li>
<li>No están estandarizados ni son uniformes, y por tanto, los usuarios pueden tener que reescribir totalmente los programas debido a que el lenguaje ha quedado obsoleto.</li>
</ul></li>
</ul></li>
<li>Ensamblaje de componentes y aplicaciones.</li>
</ul><p>El desarrollo de prototipos con reutilización comprende dos niveles:</p>
<ul><li>El nivel de aplicación, en el que una aplicación completa se integra con el prototipo. Por ejemplo: si el prototipo requiere procesamiento de textos, se puede integrar un sistema estándar de procesamiento de textos (MS Office).</li>
<li>El nivel de componente, en el que los componentes se integran en un marco de trabajo estándar.</li>
</ul><p>Dentro del nivel de componentes se usan diversos tipos de lenguajes de programación, cada uno de ellos adecuado para tareas diversas:</p>
<ul><li>Visual Basic, TCL/TK, Python, Perl, …
<ul><li>Lenguajes de alto nivel sin tipos, con facilidades gráficas.</li>
<li>Desarrollo rápido de aplicaciones pequeñas y relativamente sencillas, construidas por una persona o conjunto de personas.</li>
<li>No existe una arquitectura explícita del sistema.</li>
</ul></li>
<li>CORBA, DCOM, JavaBeans.
<ul><li>Junto con un marco arquitectónico, es más apropiado para sistemas grandes.</li>
<li>Programación distribuida.</li>
</ul></li>
</ul><h2 class="bio">Bibliografía</h2>
<ul class="bio"><li><a href="https://es.scribd.com/document/245032580/TICB2-Estrategias-Determinacion-Requerimientos" rel="noopener" target="_blank">Scribd (Alfredo Márquez)</a></li>
</ul> </article>

# Análisis estructurado. Diagramas de flujo de datos. Diagramas de estructura. Diccionario de datos. Flujogramas.

<article><h2>Análisis Estructurado</h2>
<h3>Concepto</h3>
<p>Cuando los analistas comienzan a trabajar sobre un proyecto de sistema de información, tienen que profundizar en un área de la Organización, de la cual tienen poco conocimiento. Del trabajo del analista se espera que se produzca una mejora en el sistema.</p>
<p>Así que el analista debe ser capaz de:</p>
<ul><li>Aprender los detalles y procedimientos del sistema en uso.</li>
<li>Prever necesidades futuras de la Organización en función del crecimiento, cambios futuros en el sector, introducción de nuevas tecnologías, etc.</li>
<li>Documentar detalles del sistema actual para su comprensión y discusión por otros profesionales de la organización.</li>
<li>Evaluar la efectividad y eficiencia del sistema actual y sus procedimientos.</li>
<li>Recomendar modificaciones del sistema actual, o proponer un nuevo sistema completo, justificándolo en cada caso.</li>
<li>Documentar las características del nuevo sistema con un nivel de detalle que permita comprender a otros sus componentes.</li>
<li>Fomentar la participación de gerentes y empleados en todo el proceso.</li>
</ul><p>A todas estas tareas, se les une la de cumplir los plazos establecidos. De modo que una de las claves del éxito será la de estructurar el proceso para el desarrollo del nuevo sistema.</p>
<h3>Análisis Estructurado ¿Para qué?</h3>
<p>Por la propia naturaleza los sistemas de información, éstos no están bien estructurados, no siguen leyes como las ciencias, dependen de muchas circunstancias para su funcionamiento (personas, influencias políticas de la organización, restricciones, etc). El analista debe luchar contra estas circunstancias y determinar los requerimientos de los sistemas de información.</p>
<p>Ante esta realidad, surgen preguntas como: ¿Deben dos analistas desarrollar una lista idéntica de requerimientos cuando estudian de forma independiente la misma situación? ¿Para una situación dada tenemos un único diseño correcto posible? La respuesta es que dos analistas que examinan de forma independiente una situación, sin herramientas y técnicas preestablecidas, recopilan información diferente que describa el sistema y por lo tanto en determinación de requerimientos diferentes.</p>
<p>Esto obliga a normalizar, a estructurar el análisis de sistemas de información.</p>
<p>Podemos definir análisis estructurado como:</p>
<p><em>El método para el análisis de sistemas manuales o automatizados, que conduce al desarrollo de especificaciones para sistemas nuevos o para efectuar modificaciones a los ya existentes.</em></p>
<p>El análisis estructurado permite al analista conocer un proceso (actividad) en una forma lógica y manejable al mismo tiempo que proporciona la base para asegurar que no se omite ningún detalle pertinente.</p>
<p>Por otra parte una de las claves del éxito de un buen análisis será el que exista una buena comunicación entre usuarios y analistas, esto obliga a disponer de un lenguaje común, sencillo y fiable de modo que permita minimizar costes y errores, y maximizar calidad.</p>
<h3>¿Qué debemos estructurar?</h3>
<p>El objetivo que persigue el análisis estructurado es organizar las tareas asociadas con la determinación de requerimientos para obtener la comprensión completa y exacta para una situación dada. A partir de aquí se determinan los requerimientos que serán la base de un sistema nuevo o modificado.</p>
<p>La palabra <em>estructura</em> significa:</p>
<ol><li>El método intenta estructurar el proceso de determinación de los requerimientos comenzando con la documentación del sistema existente.</li>
<li>El proceso intenta incluir todos los detalles relevantes que describen al sistema en uso.</li>
<li>Fácil verificar cuando se han omitido datos relevantes.</li>
<li>La identificación de los requerimientos será similar entre varios analistas e incluirá las mejores soluciones y estrategias para las oportunidades de desarrollo de sistemas.</li>
<li>Los documentos de trabajo generados para documentar los sistemas existentes y propuestos son dispositivos de comunicación eficientes.</li>
</ol><h3>Componentes del análisis estructurado</h3>
<p>El análisis estructurado hace uso de los siguientes componentes:</p>
<ol><li>Símbolos gráficos. Iconos y convenciones para identificar y describir los componentes de un sistema junto con las relaciones entre esos componentes.</li>
<li>Diccionario de datos. Descripción de todos los datos utilizados en el sistema.</li>
<li>Descripciones de procesos y procedimientos. Declaraciones formales que emplean técnicas y lenguajes que permiten a los analistas describir actividades importantes que forman parte del sistema.</li>
<li>Reglas. Estándares para describir y documentar el sistema en forma correcta y completa.</li>
</ol><p>El método de análisis estructurado es sinónimo de análisis de flujo de datos que es una herramienta para documentar el sistema existente o actual y determinar los requerimientos de información de forma estructurada.</p>
<h3>¿Qué es análisis de flujo de datos?</h3>
<p>Los analistas desean conocer las respuestas a cuatros preguntas: ¿Qué procesos integran el sistema? ¿Qué datos emplea cada proceso? ¿Qué datos son almacenados? ¿Qué datos entran y salen del sistema?</p>
<p>Como vemos el elemento fundamental en una Organización (sistema de información), van a ser los datos. Los datos son las guías de las actividades de la Organización, inician eventos, son procesados para dar información útil al personal, etc.</p>
<p>Seguir el flujo de datos por todos los procesos de la organización, además de ser la finalidad del análisis de flujo de datos, proporciona a los analistas información de cómo se alcanzan los objetivos en la Organización.</p>
<p>El análisis de flujo de datos estudia el empleo de los datos en cada actividad. Se basa en los diagramas de flujo de datos que muestra de forma gráfica la relación entre procesos y datos, y en los diccionarios de datos que describen de manera formal los datos del sistema y los sitios donde son utilizados.</p>
<h3>La estrategia de los flujos de datos</h3>
<p>El análisis puede pensarse de tal manera que se estudien actividades del sistema desde el punto de vista de los datos, donde se originan, cómo se utilizan o cambian, hacia dónde van. Los componentes de la estrategia de flujo de datos abarcan tanto la determinación de los requerimientos como el diseño de sistemas. Una notación bien establecida facilita la documentación del sistema actual y su análisis por todos los participantes en el proceso de determinación de requerimientos.</p>
<h3>Herramientas para el análisis de flujo de datos</h3>
<p>Las herramientas tienen el objetivo de ayudar a entender las características del sistema. Por lo tanto no deben de ser un fin, sino un medio para el estudio del sistema.</p>
<p>Las herramientas utilizadas en el análisis de flujo de datos son:</p>
<ol><li><em>Diagrama de flujo de datos.</em><br/>
Una herramienta gráfica empleada para describir y analizar el movimiento de datos a través de un sistema, incluyendo procesos, almacenamiento de datos y retrasos del sistema. Los diagramas de flujo de datos es la herramienta más importante y la base sobre la cual se desarrollan otros componentes.<br/>
La transformación de datos de entrada en salida por medio de procesos puede describirse en forma lógica e independiente de los componentes físicos. Estos diagramas reciben el nombre de diagramas lógicos de flujo de datos, en contraste de los diagramas físicos del flujo de datos que muestran la implantación y movimiento real de datos entre personas, departamentos y estaciones de trabajo.</li>
<li><em>Diccionario de datos.</em><br/>
El diccionario de datos contiene las características lógicas de los sitios donde se almacenan los datos del sistema, incluyendo nombre, descripción, alias, contenidos y organización, así como los procesos donde se emplea los datos y los sitios donde se necesita el acceso inmediato a la información. Servirán para identificar los requerimientos de las bases de datos durante el diseño del sistema.</li>
<li><em>Diagrama entidad-relación.</em><br/>
Este diagrama es una descripción de la relación entre entidades (personas, lugares, eventos y objetos) de un sistema y el conjunto de información relacionado con la entidad. No considera el almacenamiento físico de datos.</li>
<li><em>Gráfica de estructura</em> (Especificación de procesos).<br/>
Herramienta de diseño que muestra con símbolos la relación entre módulos de procesamiento y el software de la computadora. Incluye el análisis de las transformaciones entrada transformación salida y el análisis de transacciones.</li>
</ol><h3>Ventajas del análisis de flujo de datos</h3>
<p>Los analistas deben trabajar con los usuarios para hacerles comprender el funcionamiento del sistema actual y el sistema futuro, para ello se hace aconsejable utilizar un lenguaje común, sencillo y fiable, estas son las características de los diagramas de flujo de datos. Los usuarios pueden hacer sugerencias para modificar los diagramas con la finalidad de describir las actividades con mayor exactitud, y permitirá evitar los errores desde el inicio pudiendo prevenir una posible falla del sistema.</p>
<h2>Diagrama de Flujo de Datos (DFD)</h2>
<p>El objetivo del diagrama de flujo de datos es la obtención de un modelo lógico de procesos que represente el sistema, con independencia de las restricciones físicas del entorno. Así se facilita su comprensión por los usuarios y los miembros del equipo de desarrollo.</p>
<p>El sistema se divide en distintos niveles de detalle, con el objetivo de:</p>
<ul><li>Simplificar la complejidad del sistema, representando los diferentes procesos de que consta.</li>
<li>Facilitar el mantenimiento del sistema.</li>
</ul><h3>Descripción</h3>
<p>Un diagrama de flujo de datos es una técnica muy apropiada para reflejar de una forma clara y precisa los procesos que conforman el sistema de información. Permite representar gráficamente los límites del sistema y la lógica de los procesos, estableciendo qué funciones hay que desarrollar. Además, muestra el flujo o movimiento de los datos a través del sistema y sus transformaciones como resultado de la ejecución de los procesos.</p>
<p>Esta técnica consiste en la descomposición sucesiva de los procesos, desde un nivel general, hasta llegar al nivel de detalle necesario para reflejar toda la semántica que debe soportar el sistema en estudio.</p>
<p>El diagrama de flujo de datos se compone de los siguientes elementos:</p>
<ul><li><strong>Entidad externa</strong>: representa un ente ajeno al sistema que proporciona o recibe información del mismo. Puede hacer referencia a departamentos, personas, máquinas, recursos u otros sistemas. El estudio de las relaciones entre entidades externas no forma parte del modelo.<br/>
Puede aparecer varias veces en un mismo diagrama, así como en los distintos niveles del DFD para mejorar la claridad del diagrama.</li>
<li><strong>Proceso</strong>: representa una funcionalidad que tiene que llevar a cabo el sistema para transformar o manipular datos. El proceso debe ser capaz de generar los flujos de datos de salida a partir de los de entrada, más una información constante o variable al proceso.<br/>
El proceso nunca es el origen ni el final de los datos, puede transformar un flujo de datos de entrada en varios de salida y siempre es necesario como intermediario entre una entidad externa y un almacén de datos.</li>
<li><strong>Almacén de datos</strong>: representa la información en reposo utilizada por el sistema independientemente del sistema de gestión de datos (por ejemplo un fichero, base de datos, archivador, etc). Contiene la información necesaria para la ejecución del proceso.<br/>
El almacén no puede crear, transformar o destruir datos, no puede estar comunicado con otro almacén o entidad externa y aparecerá por primera vez en aquel nivel en que dos o más procesos accedan a él.</li>
<li><strong>Flujo de datos</strong>: representa el movimiento de los datos, y establece la comunicación entre los procesos y los almacenes de datos o las entidades externas.<br/>
Un flujo de datos entre dos procesos sólo es posible cuando la información es síncrona, es decir, el proceso destino comienza cuando el proceso origen finaliza su función.<br/>
Los flujos de datos que comunican procesos con almacenes pueden ser de los siguientes tipos:<br/>
– <em>De consulta</em>: representan la utilización de los valores de uno o más campos de un almacén o la aprobación de que los valores de los campos seleccionados cumplen unos criterios determinados.<br/>
– <em>De actualización</em>: representan la alteración de los datos de un almacén como consecuencia de la creación de un nuevo elemento, por eliminación o modificación de otros ya existentes.<br/>
– <em>De diálogo</em>: es un flujo entre un proceso y un almacén que representa una consulta y una actualización.</li>
</ul><p>Existen sistemas que precisan de información orientada al control de datos y requieren flujos y procesos de control, así como los mecanismos que desencadenan su ejecución. Para que resulte adecuado el análisis de estos sistemas, se ha ampliado la notación de los diagramas de flujo de datos incorporando los siguientes elementos:</p>
<ul><li><strong>Proceso de control</strong>: representa procesos que coordinan y sincronizan las actividades de otros procesos del diagrama de flujo de datos.</li>
<li><strong>Flujo de control</strong>: representa el flujo entre un proceso de control y otro proceso. El flujo de control que sale de un proceso de control activa al proceso que lo recibe y el que entre le informa de la situación de un proceso. A diferencia de los flujos tradicionales, que pueden considerarse como procesadores de datos porque reflejan el movimiento y transformación de los mismos, los flujos de control no representan datos con valores, sino que en cierto modo, se trata de eventos que activan los procesos (señales o interrupciones).</li>
</ul><p><strong>Descomposición o explosión por niveles</strong></p>
<p>Los diagramas de flujo de datos han de representar el sistema de la forma más clara posible, por ello su construcción se basa en el principio de descomposición o explosión en distintos niveles de detalle.</p>
<p>La descomposición por niveles se realiza de arriba abajo (top-down), es decir, se comienza en el nivel más general y se termina en el más detallado, pasando por los niveles intermedios necesarios. De este modo se dispondrá de un conjunto de particiones del sistema que facilitarán su estudio y desarrollo.</p>
<p>La explosión de cada proceso de un DFD origina otro DFD y es necesario comprobar que se mantiene la consistencia de información entre ellos, es decir, que la información de entrada y de salida de un proceso cualquiera se corresponde con la información de entrada y de salida del diagrama de flujo de datos en el que se descompone.</p>
<p>En cualquiera de las explosiones puede aparecer un proceso que no necesite descomposición. A éste se le denomina Proceso primitivo y sólo se detalla en él su entrada y su salida, además de una descripción de lo que realiza. En la construcción hay que evitar en lo posible la descomposición desigual, es decir, que un nivel contenga un proceso primitivo, y otro que necesite ser particionado en uno o varios niveles más.</p>
<p>El modelo de procesos deberá contener:</p>
<ul><li>Un diagrama de contexto (Nivel 0).</li>
<li>Un diagrama 0 (Nivel 1).</li>
<li>Tantos diagramas 1, 2, 3, …, n como funciones haya en el diagrama 0 (Nivel 2).</li>
<li>Tantos niveles intermedios como sea necesario.</li>
<li>Varios DFD en el último nivel de detalle.</li>
</ul><p>El diagrama de contexto tiene como objetivo delimitar el ámbito del sistema con el mundo exterior definiendo sus interfaces. En este diagrama se representa un único proceso que corresponde al sistema en estudio, un conjunto de entidades externas que representan la procedencia y destino de la información y un conjunto de flujos de datos que representan los caminos por los que fluye dicha información.</p>
<p>A continuación, este proceso se descompone en otro DFD, en el que se representan los procesos principales o subsistemas. Un subsistema es un conjunto de procesos cuyas funcionalidades tienen algo en común. Éstos deberán ser identificados en base a determinados criterios, como por ejemplo: funciones organizativas o administrativas propias del sistema, funciones homogéneas de los procesos, localización geográfica de los mismos, procesos que actualicen los mismos almacenes de datos, etc.</p>
<p>Cada uno de los procesos principales se descompone a su vez en otros que representan funciones más simples y se sigue descomponiendo hasta que los procesos estén suficientemente detallados y tengan una funcionalidad concreta, es decir, sean procesos primitivos.</p>
<p>Como resultado se obtiene un modelo de procesos del sistema de información que consta de un conjunto de diagramas de flujo de datos de diferentes niveles de abstracción, de modo que cada uno proporciona una visión más detallada de una parte definida en el nivel anterior.</p>
<p>Además de los diagramas de flujo de datos, el modelo de procesos incluye la especificación de los flujos de datos, de los almacenes de datos y la especificación detallada de los procesos que no precisan descomposición, es decir los procesos de último nivel o primitivos. En la especificación de un proceso primitivo se debe describir, de una manera más o menos formal, cómo se obtienen los flujos de datos de salida a partir de los flujos de datos de entrada y características propias del proceso.</p>
<p>Dependiendo del tipo de proceso se puede describir el procedimiento asociado utilizando un lenguaje estructurado o un pseudocódigo, apoyándose en tablas de decisión o árboles de decisión.</p>
<p>A continuación se muestra un ejemplo gráfico que representa la descomposición jerárquica de los diagramas de flujo de datos.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/diagrama_contexto.png?w=825"/></p>
<h3>Notación</h3>
<p><strong>Entidad externa</strong></p>
<p>Se representa mediante una elipse con un identificador y un nombre significativo en su interior.</p>
<p>Si la entidad externa aparece varias veces en un mismo diagrama, se representa con una línea inclinada en el ángulo superior izquierdo.</p>
<div class="tiled-gallery type-rectangular tiled-gallery-unresized" data-carousel-extra='{"blog_id":139753180,"permalink":"https:\/\/gsitic.wordpress.com\/2018\/04\/24\/biii5-analisis-estructurado-diagramas-de-flujo-de-datos-diagramas-de-estructura-diccionario-de-datos-flujogramas\/","likes_blog_id":139753180}' data-original-width="825" itemscope="itemscope" itemtype="http://schema.org/ImageGallery"> <div class="gallery-row" data-original-height="235" data-original-width="825"> <div class="gallery-group images-1" data-original-height="235" data-original-width="402"> <div class="tiled-gallery-item tiled-gallery-item-large" itemprop="associatedMedia" itemscope="itemscope" itemtype="http://schema.org/ImageObject"> <a href="https://gsitic.wordpress.com/2018/04/24/biii5-analisis-estructurado-diagramas-de-flujo-de-datos-diagramas-de-estructura-diccionario-de-datos-flujogramas/entidad_externa/" itemprop="url"> <img src="https://gsitic.files.wordpress.com/2018/04/entidad_externa.png?w=398&amp;h=231"/></a> </div> </div> <div class="gallery-group images-1" data-original-height="235" data-original-width="423"> <div class="tiled-gallery-item tiled-gallery-item-large" itemprop="associatedMedia" itemscope="itemscope" itemtype="http://schema.org/ImageObject"> <a href="https://gsitic.wordpress.com/2018/04/24/biii5-analisis-estructurado-diagramas-de-flujo-de-datos-diagramas-de-estructura-diccionario-de-datos-flujogramas/entidad_externa_repetida/" itemprop="url"> <img src="https://gsitic.files.wordpress.com/2018/04/entidad_externa_repetida.png?w=419&amp;h=231"/></a> </div> </div> </div> </div>
<p><strong>Proceso</strong></p>
<p>Se representa por un rectángulo subdividido en tres casillas donde se indica el nombre del proceso, un número identificativo y la localización.</p>
<p>Si el proceso es de último nivel, se representa con un asterisco en el ángulo inferior derecho separado con una línea inclinada.</p>
<div class="tiled-gallery type-rectangular tiled-gallery-unresized" data-carousel-extra='{"blog_id":139753180,"permalink":"https:\/\/gsitic.wordpress.com\/2018\/04\/24\/biii5-analisis-estructurado-diagramas-de-flujo-de-datos-diagramas-de-estructura-diccionario-de-datos-flujogramas\/","likes_blog_id":139753180}' data-original-width="825" itemscope="itemscope" itemtype="http://schema.org/ImageGallery"> <div class="gallery-row" data-original-height="246" data-original-width="825"> <div class="gallery-group images-1" data-original-height="246" data-original-width="413"> <div class="tiled-gallery-item tiled-gallery-item-large" itemprop="associatedMedia" itemscope="itemscope" itemtype="http://schema.org/ImageObject"> <a href="https://gsitic.wordpress.com/2018/04/24/biii5-analisis-estructurado-diagramas-de-flujo-de-datos-diagramas-de-estructura-diccionario-de-datos-flujogramas/proceso/" itemprop="url"> <img src="https://gsitic.files.wordpress.com/2018/04/proceso.png?w=409&amp;h=242"/></a> </div> </div> <div class="gallery-group images-1" data-original-height="246" data-original-width="412"> <div class="tiled-gallery-item tiled-gallery-item-large" itemprop="associatedMedia" itemscope="itemscope" itemtype="http://schema.org/ImageObject"> <a href="https://gsitic.wordpress.com/2018/04/24/biii5-analisis-estructurado-diagramas-de-flujo-de-datos-diagramas-de-estructura-diccionario-de-datos-flujogramas/proceso_ultimo/" itemprop="url"> <img src="https://gsitic.files.wordpress.com/2018/04/proceso_ultimo.png?w=408&amp;h=242"/></a> </div> </div> </div> </div>
<p>El nombre del proceso debe ser lo más representativo posible. Normalmente estará constituido por un verbo más un sustantivo.</p>
<p>El número identificativo se representa en la parte superior izquierda e indica el nivel del DFD en que se está. Hay que resaltar que el número no indica orden de ejecución alguno entre los procesos ya que en un DFD no se representa una secuencia en el tratamiento de los datos. El número que identifica el proceso es único en el sistema y debe seguir el siguiente estándar de notación:</p>
<ul><li>El proceso del diagrama de contexto se numera como cero.</li>
<li>Los procesos del siguiente nivel se enumeran desde 1 y de forma creciente hasta completar el número de procesos del diagrama.</li>
<li>En los niveles inferiores se forma con el número del proceso en el que está incluido seguido de un número que lo identifica en ese contexto.</li>
</ul><p>La localización expresa el nombre del proceso origen de la descomposición que se esté tratando.</p>
<p><strong>Almacén de datos</strong></p>
<p>Se representa por dos líneas paralelas cerradas en un extremo y una línea vertical que las une. En la parte derecha se indica el nombre del almacén de datos y en la parte izquierda el identificador de dicho almacén en el DFD.</p>
<p>Si un almacén aparece repetido dentro de un DFD se puede representar con dos líneas verticales.</p>
<div class="tiled-gallery type-rectangular tiled-gallery-unresized" data-carousel-extra='{"blog_id":139753180,"permalink":"https:\/\/gsitic.wordpress.com\/2018\/04\/24\/biii5-analisis-estructurado-diagramas-de-flujo-de-datos-diagramas-de-estructura-diccionario-de-datos-flujogramas\/","likes_blog_id":139753180}' data-original-width="825" itemscope="itemscope" itemtype="http://schema.org/ImageGallery"> <div class="gallery-row" data-original-height="95" data-original-width="825"> <div class="gallery-group images-1" data-original-height="95" data-original-width="404"> <div class="tiled-gallery-item tiled-gallery-item-large" itemprop="associatedMedia" itemscope="itemscope" itemtype="http://schema.org/ImageObject"> <a href="https://gsitic.wordpress.com/2018/04/24/biii5-analisis-estructurado-diagramas-de-flujo-de-datos-diagramas-de-estructura-diccionario-de-datos-flujogramas/almacen_datos-2/" itemprop="url"> <img src="https://gsitic.files.wordpress.com/2018/04/almacen_datos.png?w=400&amp;h=91"/></a> </div> </div> <div class="gallery-group images-1" data-original-height="95" data-original-width="421"> <div class="tiled-gallery-item tiled-gallery-item-large" itemprop="associatedMedia" itemscope="itemscope" itemtype="http://schema.org/ImageObject"> <a href="https://gsitic.wordpress.com/2018/04/24/biii5-analisis-estructurado-diagramas-de-flujo-de-datos-diagramas-de-estructura-diccionario-de-datos-flujogramas/almacen_datos_repetido/" itemprop="url"> <img src="https://gsitic.files.wordpress.com/2018/04/almacen_datos_repetido.png?w=417&amp;h=91"/></a> </div> </div> </div> </div>
<p><strong>Flujo de datos</strong></p>
<p>Se representa por una flecha que indica la dirección de los datos, y que se etiqueta con un nombre representativo.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/flujo_datos.png?w=825"/></p>
<p>La representación de los flujos de&nbsp;datos entre procesos y almacenes es la siguiente:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/representacion_flujo_datos.png?w=825"/></p>
<p><strong>Proceso de control</strong></p>
<p>Se representa por un rectángulo, con trazo discontinuo, subdividido en tres casillas donde se indica el nombre del proceso, un número identificativo y la localización.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/proceso_control.png?w=825"/></p>
<p><strong>Flujo de control</strong></p>
<p>Se representa por una flecha con trazo discontinuo que indica la dirección de flujo y que se etiqueta con un nombre representativo.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/flujo_control.png?w=825"/></p>
<p><strong>Ejemplo</strong></p>
<p>La figura es un diagrama de flujos de un Sistema Gestor de Pedidos. En él están representados todos los elementos que pueden intervenir en un Diagrama de Flujo de Datos.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/ejemplo_dfd.png?w=825"/></p>
<h3>Consistencia de los diagramas de flujo de datos</h3>
<p>Una vez construidos los diagramas de flujo de datos que componen el modelo de procesos del sistema de información, es necesario comprobar y asegurar su validez. Para ello, se debe estudiar cada diagrama comprobando que es legible, de poca complejidad y si los nombres asignados a sus elementos ayudan a su comprensión sin ambigüedades.</p>
<p>Además, los diagramas deben ser consistentes. En los diagramas hay que comprobar que en un DFD resultado de una explosión:</p>
<ul><li>No falten flujos de datos de entrada o salida que acompañaban al proceso del nivel superior.</li>
<li>No aparezca algún flujo que no estuviese ya asociado al proceso de nivel superior.</li>
<li>Todos los elementos del DFD resultante deben estar conectados directa o indirectamente con los flujos del proceso origen.</li>
</ul><p>A continuación se incluyen ejemplos de la consistencia o inconsistencia de los diagramas de flujo de datos.</p>
<p>Sea el diagrama de contexto de la figura. Los flujos A, C y D, entran al sistema, y el flujo B sale de él.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/ejemplo1_diagrama_contexto.png?w=825"/></p>
<p><strong>Ejemplo de consistencia de diagramas de flujo de datos</strong></p>
<p>En la explosión del sistema en el diagrama de nivel 1, aparecen todos los flujos, y en su sentido correcto: A y C entran al subsistema o proceso 1, B sale del proceso 2, y D entra en el proceso 3. Se observa que el proceso 3, origina dos flujos de salida: E que va al proceso 1, y F al proceso 2.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/consistencia1.png?w=825"/></p>
<p>La descomposición del proceso 1, muestra los flujos A, C y E correctamente, como entradas a las funciones del diagrama.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/consistencia2.png?w=825"/></p>
<p>Los demás flujos están enlazados con los almacenes A1 y A2 del mismo modo que en el diagrama anterior.</p>
<p><strong>Ejemplo de inconsistencia de diagramas de flujo de datos</strong></p>
<p>Partiendo del mismo diagrama de contexto utilizado en el anterior ejemplo, los flujos A, C y D, que entran al sistema, y el flujo B, que sale de él, deben aparecer en la primera descomposición, el diagrama de nivel 1. En la figura se aprecia que falta el flujo D, y hay un flujo G que o bien falta en el nivel anterior, sobra en este.</p>
<p>Por otro lado, en el proceso 3 no entra ningún flujo, no es posible por tanto que transforme datos saliendo los flujos E y F y además está desconectado del nivel anterior.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/inconsistencia1.png?w=825"/></p>
<p>En el siguiente paso, la inconsistencia más clara es la falta del flujo C, que entra al proceso 1, y sin embargo no aparece en su explosión.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/inconsistencia2.png?w=825"/></p>
<p>Además, hay otra inconsistencia respecto al almacén A1: en el diagrama del nivel anterior, el proceso 1 se conectaba con un flujo de entrada-salida a este almacén, cosa que no se refleja en el diagrama de este proceso, en el que sólo aparece uno de entrada.</p>
<p><strong>Ejemplo de construcción</strong></p>
<p>El caso en estudio es un modelo de procesos de un sistema de información de Conocimientos de técnicos. Según estos conocimientos, los técnicos podrán ser asignados a determinados proyectos de la organización.</p>
<p>El sistema recogerá la información referente a los técnicos, procedente de la Dirección técnica de la organización y de los proyectos, procedente de cualquier sección o Unidad de Negocio en las que está dividida dicha organización.</p>
<p>Las entidades externas son pues Dirección Técnica y Unidad de Negocio, que introducen los datos al sistema y hacen peticiones de consultas e informes sobre los técnicos y sus conocimientos. El diagrama de contexto será el siguiente:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/ejemplo_diagrama_contexto.png?w=825"/></p>
<p>Los flujos de entrada son: Datos Técnicos, con datos de los técnicos introducidos por la Dirección Técnica, así como posibles peticiones de información sobre ellos; y Datos Unidad, que proviene de la Unidad de Negocio, conteniendo datos referentes a la unidad, de proyectos y clientes, así como posibles peticiones de consultas sobre los mismos.</p>
<p>Los flujos de salida son: Información Técnicos, que contendrá datos de técnicos, de consulta o informes, para uso de la Dirección Técnica y Consultas Unidad, con datos requeridos por la Unidad de Negocio.</p>
<p>El sistema de Conocimientos se descompone en el diagrama de nivel 1, conteniendo do subsistemas. El subsistema 1 recogerá las funciones a realizar con los datos de los técnicos de la organización (actualizaciones, consultas, informes, etc), por lo que se denomina Tratar Técnicos. El subsistema 2 contendrá las funciones asociadas al procesamiento de datos de proyectos, por lo que se le da el nombre Tratar Proyectos.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/ejemplo_dfd_2.png?w=825"/></p>
<p>En el diagrama se encuentran cuatro almacenes, tres de los cuales son accedidos por funciones de los dos subsistemas: A1 Conocimientos, A2 Proyectos y A3 Técnicos. El cuarto, A4 Clientes, sólo es accedido por el subsistema Tratar Proyectos.</p>
<p>Los flujos sin nombre indican que hay entrada y/o salida de todos los datos del almacén. En este diagrama siguen apareciendo las entidades externas para la mayor comprensión del mismo.</p>
<p>A partir de ahora, se centrará el ejemplo en la descomposición del subsistema 1 Tratar Técnicos, hasta llegar a su nivel más detallado.</p>
<p>En el diagrama resultado de la explosión de Tratar Técnicos, se incluyen cuatro procesos o funciones para el tratamiento completo de éstos.</p>
<p>El flujo de entrada Datos Técnicos se compone tanto de los datos profesionales de los técnicos, como de datos de peticiones de información sobre los mismos, por lo cual se ha dividido en dos: Datos Profesionales, que es entrada del proceso 1.1 Validad datos Técnicos y Peticiones Información Técnicos, que entra en la función 1.4 Informar.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/ejemplo_dfd_3.png?w=825"/></p>
<p>Para la validación, el proceso 1.1 Validar Datos Técnicos obtiene información del almacén A3 Técnicos y genera una salida, el flujo Datos Técnicos Correctos, que lleva los datos válidos a la función 1.2 Actualizar Almacenes Técnicos. Esta función se encarga de actualizar los almacenes A3 Técnicos y A1 Conocimientos, pero también emite un flujo al proceso 1.3 Asignar a Proyectos. Éste se encarga de hacer asignaciones de técnicos en el almacén A2 Proyectos.</p>
<p>La función 1.4 Informar, recibe las peticiones de información sobre técnicos, las procesa utilizando los almacenes necesarios y genera el flujo Información Técnicos que irá a la entidad Dirección Técnica, según muestran los primeros diagramas.</p>
<p>Obsérvese que para mayor claridad no se ha incluido ya ninguna entidad externa, y además, se ha repetido el almacén A3 Técnicos, evitando que el cruce de flujos oscurezca la lectura del diagrama.</p>
<p>En este momento, todos los procesos se consideran primitivos, excepto el proceso 1.4 Informar, del que se obtiene su descomposición. Sus funciones han de obtener Informes Técnicos y Consultas Técnicos, flujos que componen Información Técnicos que aparecía en el nivel anterior.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/ejemplo_dfd_4.png?w=825"/></p>
<p>Por otro lado, también aparece dividido el flujo de entrada Peticiones Información Técnicos, diferenciando la entrada al proceso de consultas o al de emisión de informes.</p>
<p>Por último, se puede apreciar que los almacenes son los mismos que se conectaban con el proceso en el nivel anterior y los flujos son de entrada a las funciones.</p>
<p>(Nota.- Esta notación es la más habitual, pero MÉTRICA Versión 3 no exige su utilización).</p>
<h2>Diagrama de Estructura</h2>
<p>El objetivo de este diagrama es representar la estructura modular del sistema o de un componente del mismo y definir los parámetros de entrada y salida de cada uno de los módulos.</p>
<p>Para su realización se partirá del modelo de procesos obtenido como resultado de la aplicación de la técnica de diagrama de flujo de datos (DFD).</p>
<h3>Descripción</h3>
<p>Un diagrama de estructura se representa en forma de árbol con los siguientes elementos:</p>
<ul><li><strong>Módulo</strong>: división del software clara y manejable con interfaces modulares perfectamente definidas. Un módulo puede representar un programa, subprograma o rutina dependiendo del lenguaje a utilizar. Admite parámetros de llamada y retorno. En el diseño de alto nivel hay que ver un módulo como una <em>caja negra</em>, donde se contemplan exclusivamente sus entradas y sus salidas y no los detalles de la lógica interna del módulo. Para que se reduzca la complejidad del cambio ante una determinada modificación, es necesario que los módulos cumplan las siguientes condiciones:
<ul><li>Que sean de pequeño tamaño.</li>
<li>Que sean independientes entre sí.</li>
<li>Que realicen una función clara y sencilla.</li>
</ul></li>
<li><strong>Conexión</strong>: representa una llamada de un módulo a otro.</li>
<li><strong>Parámetro</strong>: información que se intercambia entre los módulos. Pueden ser de dos tipos en función de la clase de información a procesar:
<ul><li><em>Control</em>: son valores de condición que afectan a la lógica de los módulos llamados. Sincronizan la operativa de los módulos.</li>
<li><em>Datos</em>: información compartida entre módulos y que es procesada en los módulos llamados.</li>
</ul></li>
</ul><p>Otros componentes que se pueden representar en el diagrama de estructura son:</p>
<ul><li><strong>Módulo predefinido</strong>: es aquel módulo que está disponible en la biblioteca del sistema o de la propia aplicación, y por tanto no es necesario codificarlo.</li>
<li><strong>Almacén de datos</strong>: es la representación física del lugar donde están almacenados los datos del sistema.</li>
<li><strong>Dispositivo físico</strong>: es cualquier dispositivo por el cual se puede recibir o enviar información que necesite el sistema.</li>
</ul><p><strong>Estructuras del diagrama</strong></p>
<p>Existen ciertas representaciones gráficas que permiten mostrar la secuencia de las llamadas entre módulos. Las posibles estructuras son:</p>
<ul><li><strong>Secuencial</strong>: un módulo llama a otros módulos una sola vez y, se ejecutan de izquierda a derecha y de arriba a abajo.<br/><img src="https://gsitic.files.wordpress.com/2018/04/estructura_secuencial.png?w=825"/></li>
<li><strong>Repetitiva</strong>: cada uno de los módulos inferiores se ejecuta varias veces mientras se cumpla una condición.<br/><img src="https://gsitic.files.wordpress.com/2018/04/estructura_repetitiva.png?w=825"/></li>
<li><strong>Alternativa</strong>: cuando el módulo superior, en función de una decisión, llama a un módulo u otro nivel de los de nivel inferior.<br/><img src="https://gsitic.files.wordpress.com/2018/04/estructura_alternativa.png?w=825"/></li>
</ul><p><strong>Principios del diseño estructurado</strong></p>
<p>El diagrama de estructura se basa en tres principios fundamentales:</p>
<ul><li>La descomposición de los módulos, de manera que los módulos que realizan múltiples funciones se descompongan en otros que sólo realicen una. Los objetivos que se persiguen con la descomposición son:
<ul><li>Reducir el tamaño del módulo.</li>
<li>Hacer el sistema más fácil de entender y modificar y por lo tanto facilitar el mantenimiento del mismo.</li>
<li>Minimizar la duplicidad de código.</li>
<li>Crear módulos útiles.</li>
</ul></li>
<li>La jerarquía entre los módulos, de forma que los módulos de niveles superiores coordinen a los de niveles inferiores. Al dividir los módulos jerárquicamente, es posible controlar el número de módulos que interactúan con cualquiera de los otros.</li>
<li>La independencia de los módulos, de manera que cada módulo se ve como una caja negra, y únicamente es importante su función y su apariencia externa, y no los detalles de su construcción.</li>
</ul><p><strong>Estrategias de diseño</strong></p>
<p>Dependiendo de la estructura inicial del diagrama de flujo de datos sobre el que se va a realizar el diseño, existen dos estrategias para obtener el diagrama de estructura. El uso de una de las dos estrategias no implica que la otra no se utilice, eso dependerá de las características de los procesos representados en DFD. Estas estrategias son:</p>
<ul><li>Análisis de transformación.</li>
<li>Análisis de transacción.</li>
</ul><p><em>Análisis de Transformación</em></p>
<p>El análisis de transformación es un conjunto de pasos que permiten obtener, a partir de un DFD con características de transformación, la estructura del diseño de alto nivel del sistema. Un DFD con características de transformación es aquél en el que se pueden distinguir:</p>
<ul><li>Flujo de llegada o entrada.</li>
<li>Flujo de transformación o centro de transformación que contiene los procesos esenciales del sistema y es independiente de las características particulares de la entrada y la salida.</li>
<li>Flujo de salida.</li>
</ul><p>Los datos que necesita el sistema se recogen por los módulos que se encuentren en las ramas de la izquierda, de modo que los datos que se intercambian en esa rama serán ascendentes. En las ramas centrales habrá movimiento de información compartida, tanto ascendente como descendente. En las ramas de la derecha, la información será de salida y, por lo tanto, descendente.</p>
<p>Los pasos a realizar en el análisis de transformación son:</p>
<ol><li>Identificar el centro de transformación. Para ello será necesario delimitar los flujos de llegada y salida de la parte del DFD que contiene las funciones esenciales del sistema.</li>
<li>Realizar el “primer nivel de factorización” o descomposición del diagrama de estructura. Habrá que identificar tres módulos subordinados a un módulo de control del sistema:
<ul><li>Módulo controlador del proceso de información de entrada.</li>
<li>Módulo controlador del centro de transformación.</li>
<li>Módulo controlador del proceso de la información de salida.</li>
</ul></li>
<li>Elaborar el “segundo nivel de factorización”. Se transforma cada proceso del DFD en un módulo del diagrama de estructura.</li>
<li>Revisar la estructura del sistema utilizando medidas y guías de diseño.</li>
</ol><p>A continuación se muestra un gráfico explicativo de dicha estrategia de diseño:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/estrategia_disec3b1o.png?w=825"/></p>
<p><em>Análisis de Transacción</em></p>
<p>El análisis de transacción se aplica cuando en un DFD existe un proceso que en función del flujo de llegada, determina la elección de uno o más flujos de información.</p>
<p>Se denomina <em>centro de transacción</em> al proceso desde el que parten los posibles caminos de información. Los pasos a realizar en el análisis de transacción son:</p>
<ol><li>Identificar el centro de transacción. Se delimita la parte del DFD en la que a partir de un camino de llegada se establecen varios caminos de acción.</li>
<li>Transformar el DFD en la estructura adecuada al proceso de transacciones. El flujo de transacciones se convierte en una estructura de programa con una bifurcación de entrada y una de salida.</li>
<li>Factorizar la estructura de cada camino de acción. Cada camino se convierte en una estructura que se corresponde con las características específicas del flujo (de transacción o de transformación).</li>
<li>Refinar la estructura del sistema utilizando medidas y guías de diseño.</li>
</ol><p>A continuación se muestra un gráfico explicativo de dicha estrategia de diseño:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/analisis_transaccion.png?w=825"/></p>
<p><strong>Evaluación del diseño</strong></p>
<p>Una vez que hayan sido elaborados los diagramas de estructura, habrá que evaluar el diseño estudiando distintos criterios y medidas. Se utilizan dos métricas que miden la calidad estructural de un diseño:</p>
<ul><li>Acoplamiento.</li>
<li>Cohesión.</li>
</ul><p>El <strong><em>acoplamiento</em> </strong>se puede definir como el grado de interdependencia existente entre los módulos, por tanto, depende del número de parámetros que se intercambian. El objetivo es que el acoplamiento sea el mínimo posible, es decir, conseguir que los módulos sean lo más independientes entre sí.</p>
<p>Es deseable un bajo acoplamiento, debido a que cuantas menos conexiones existan entre dos módulos, menor será la posibilidad de que aparezcan efectos colaterales al modificar uno de ellos. Además, se mejora el mantenimiento, porque al cambiar un módulo por otro, hay menos riesgo de actualizar la lógica interna de los módulos asociados. Los diferentes grados de acoplamiento son:</p>
<ul><li><em>De datos</em>: los módulos se comunican mediante parámetros que constituyen elementos de datos simples.</li>
<li><em>De marca</em>: es un caso particular del acoplamiento de datos, donde la comunicación entre módulos es a través de estructuras de datos.</li>
<li><em>De control</em>: aparece cuando uno o varios de los parámetros de comunicación son de control, es decir variables que controlan las decisiones de los módulos subordinados o superiores.</li>
<li><em>Externo</em>: los módulos están ligados a componentes externos (dispositivos E/S, protocolos de comunicaciones, etc).</li>
<li><em>Común</em>: varios módulos hacen referencia a un área común de datos. Los módulos asociados al área común de datos pueden modificar los valores de los elementos de datos o estructuras de datos que se incluyen en dicha área.</li>
<li><em>De contenido</em>: ocurre cuando un módulo cualquiera accede o hace uso de los datos de una parte de otro módulo.</li>
</ul><p>La <strong><em>cohesión</em> </strong>es una medida de la relación funcional de los elementos de un módulo, es decir, la sentencia o grupo de sentencias que lo componen, las llamadas a otros módulos o las definiciones de los datos. Un módulo con alta cohesión realiza una tarea concreta y sencilla.</p>
<p>El objetivo es intentar obtener módulos con una cohesión alta o media. Los distintos niveles de cohesión, de mayor a menor, son:</p>
<ul><li><em>Funcional</em>: todos los elementos que componen el módulo están relacionados en el desarrollo de una única función.</li>
<li><em>Secuencial</em>: un módulo empaqueta en secuencia varios módulos con cohesión funcional.</li>
<li><em>De comunicación</em>: todos los elementos de procesamiento utilizan los mismos datos de entrada y de salida.</li>
<li><em>Procedimental</em>: todos los elementos de procesamiento de un módulo están relacionados y deben ejecutarse en un orden determinado. En este tipo existe paso de controles.</li>
<li><em>Temporal</em>: un módulo contiene tareas relacionadas por el hecho de que todas deben realizarse en el mismo intervalo de tiempo.</li>
<li><em>Lógica</em>: un módulo realiza tareas relacionadas de forma lógica (por ejemplo un módulo que produce todas las salidas independientemente del tipo).</li>
<li><em>Casual</em>: un modulo realiza un conjunto de tareas que tienen poca o ninguna relación entre sí.</li>
</ul><p>Un buen diseño debe ir orientado a conseguir que los módulos realicen una función sencilla e independiente de las demás (máxima cohesión), y que la dependencia con otros módulos sea mínima (acoplamiento mínimo), lo cual facilita el mantenimiento del diseño.</p>
<h3>Notación</h3>
<p><strong>Módulo</strong></p>
<p>Se representa mediante un rectángulo con su nombre en el interior.</p>
<p>Un módulo predefinido se representa añadiendo dos líneas verticales y paralelas en el interior del rectángulo.</p>
<div class="tiled-gallery type-rectangular tiled-gallery-unresized" data-carousel-extra='{"blog_id":139753180,"permalink":"https:\/\/gsitic.wordpress.com\/2018\/04\/24\/biii5-analisis-estructurado-diagramas-de-flujo-de-datos-diagramas-de-estructura-diccionario-de-datos-flujogramas\/","likes_blog_id":139753180}' data-original-width="825" itemscope="itemscope" itemtype="http://schema.org/ImageGallery"> <div class="gallery-row" data-original-height="299" data-original-width="825"> <div class="gallery-group images-1" data-original-height="299" data-original-width="417"> <div class="tiled-gallery-item tiled-gallery-item-large" itemprop="associatedMedia" itemscope="itemscope" itemtype="http://schema.org/ImageObject"> <a href="https://gsitic.wordpress.com/2018/04/24/biii5-analisis-estructurado-diagramas-de-flujo-de-datos-diagramas-de-estructura-diccionario-de-datos-flujogramas/modulo_1/" itemprop="url"> <img src="https://gsitic.files.wordpress.com/2018/04/modulo_1.png?w=413&amp;h=295"/></a> </div> </div> <div class="gallery-group images-1" data-original-height="299" data-original-width="408"> <div class="tiled-gallery-item tiled-gallery-item-large" itemprop="associatedMedia" itemscope="itemscope" itemtype="http://schema.org/ImageObject"> <a href="https://gsitic.wordpress.com/2018/04/24/biii5-analisis-estructurado-diagramas-de-flujo-de-datos-diagramas-de-estructura-diccionario-de-datos-flujogramas/modulo_2/" itemprop="url"> <img src="https://gsitic.files.wordpress.com/2018/04/modulo_2.png?w=404&amp;h=295"/></a> </div> </div> </div> </div>
<p><strong>Conexión</strong></p>
<p>Se representa mediante una línea terminada en punta de flecha cuya dirección indica el módulo llamado. Para llamadas a módulos estáticos se utiliza trazo continuo y para llamadas a módulos dinámicos trazo discontinuo.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/conexion.png?w=825"/></p>
<p><strong>Parámetros</strong></p>
<p>La representación varía según su tipo: control (flags) o datos.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/parametros.png?w=825"/></p>
<p><strong>Almacén de datos</strong></p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/almacen_datos1.png?w=825"/></p>
<p><strong>Dispositivo físico</strong></p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/dispositivo_fisico.png?w=825"/></p>
<p>(Nota.- Esta notación es la más habitual, pero MÉTRICA Versión 3 no exige su utilización).</p>
<p><strong>Ejemplo</strong></p>
<p>En el siguiente ejemplo muestra un proceso de emisión de cheques para el pago de nóminas de los empleados de una empres. En él se diferencian los cálculos relativos a los trabajadores empleados por horas y los que poseen contrato. La lectura del fichero de empleados y la impresión de los cheques son módulos ya disponibles en las librerías del sistema, es decir, módulos predefinidos.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/ejemplo_diagrama_estructura.png?w=825"/></p>
<h2>Diccionario de Datos</h2>
<h3>Documentación del sistema</h3>
<p>Hasta el momento hemos descrito las técnicas utilizadas en el desarrollo de sistemas, pero el desarrollo de modelos no queremos hacerlo sobre hojas sueltas, con el peligro de extraviarlas, y tener dificultad en mantenerlo. Por el contrario, necesitamos organizar el seguimiento de los modelos, principalmente por dos razones:</p>
<ul><li>Dar significado a los componentes del modelo, ayudando a gestionar la complejidad del sistema.</li>
<li>Soportar el mantenimiento, ya que cualquier trabajo puede pasar de una persona a otra.</li>
</ul><p>A esta forma de seguimiento organizado del trabajo producido durante el análisis y diseño del sistema se llama documentación del sistema.</p>
<p>La documentación del sistema es tanto una herramienta de comunicación, como de comunicación porque contiene un almacén de todo el trabajo hecho cada día y lo pone a disposición de todas las personas que trabajan en un proyecto grande. También es una herramienta de dirección, porque asegura una alta eficiencia, ya que todas las personas tienen acceso a lo último realizado. Dado que un proyecto se divide en fases, se establece la documentación que se debe aportar en cada fase, lo que ayuda a conocer la situación en cada momento del proyecto.</p>
<p>Para que sea útil, la documentación debe ser estructural y fácil de usar. La documentación en un primer momento se divide en informes de proyecto y una descripción del sistema.</p>
<p><strong>Informes del proyecto</strong></p>
<p>Los informes del proyecto incluyen la información requerida por la dirección del proyecto. Los informes incluyen un resumen de la fase actual, unas recomendaciones para la siguiente fase y un plan con los recursos propuestos.</p>
<p>La información específica de la fase depende de la fase del proyecto, por ejemplo el informe de viabilidad incluirá los costes esperados del proyecto, y una recomendación para seguir o abandonarlo.</p>
<p><strong>Diccionario del sistema</strong></p>
<p>El Diagrama de Flujo de Datos describe el sistema. El diagrama E/R, describe los datos del sistema. El componente descripción del proceso describe los procesos del DFD y el Diccionario de datos que describe los datos del sistema (flujos y almacenes de datos). Los usuarios del sistema y como lo utilizan se incluyen en la descripción del usuario.</p>
<p><strong>Descripción de procesos</strong></p>
<p>La descripción de procesos incluyen una entrada por cada proceso del diagrama de flujo de datos. Cada entrada del proceso incluye el número de DFD para él, junto con la descripción del proceso. Como ejemplo la descripción de un proceso de alto nivel, incluye el número y nombre del proceso, los nombres de los flujos de datos de entrada y salida y una descripción del proceso.</p>
<p>Para la descripción de procesos en los niveles inferiores de DFD, se usará un método de descripción de procesos, no así en los DFD de alto nivel que basta una descripción narrativa del proceso.</p>
<h3>Diccionario de Datos</h3>
<p>El diccionario de datos es una lista organizada de todos los datos pertenecientes al sistema, con una serie de definiciones precisas y rigurosas para que tanto el analista como el usuario comprendan entradas, salidas, elementos de los almacenamientos y cálculos intermedios.</p>
<p>En el diccionario de datos incluimos almacenes de datos, flujos de datos, estructuras de datos, elementos de datos y en algunos casos el modelo E/R.</p>
<p>El diccionario de datos (DD) define los datos en cuanto que:</p>
<ol><li>Describe el <em>significado</em> de los flujos de datos y los almacenes que muestran los DFDs.</li>
<li>Describe la <em>composición</em> de la estructura de datos que se mueven a lo largo de los flujos.</li>
<li>Describe la composición de la estructura de datos en los almacenes.</li>
<li>Describe los detalles de las relaciones entre almacenes que aparecen en un diagrama entidad/relación.</li>
</ol><p>Los analistas utilizan los diccionarios de datos por cuatro razones:</p>
<ol><li>Para manejar los detalles en sistemas grandes ya que es imposible de recordar todo lo referente a un sistema.</li>
<li>Para comunicar un significado común para todos los elementos del sistema. Esto es muy importante cuando trabajan varios analistas y no pueden reunirse todos los días para comunicarse.</li>
<li>Para documentar las características del sistema.</li>
<li>Localizar errores en el sistema.</li>
</ol><p><strong>Contenido de un Diccionario de Datos</strong></p>
<p>El DD contiene las siguientes:</p>
<ol><li>Definiciones lógicas de datos:
<ul><li>Elemento de Dato (Atributos de la Entidad).</li>
<li>Estructura de Dato.</li>
<li>Flujos de Datos.</li>
<li>Almacenes de Datos.</li>
</ul></li>
<li>Definiciones lógicas de procesos.</li>
<li>Definición lógica de entidad externa.</li>
</ol><p>Los elementos de dato se agrupan para formar una estructura de dato.</p>
<ol><li><em>Elemento de dato</em>: Ninguna unidad más pequeña tiene significado para los analistas o usuarios. Son los bloques básicos para todos los demás datos del sistema, por sí solo no lleva ningún significado al usuario. Son los atributos de las entidades.<br/>
Por ejemplo: nº factura, fecha expedición, cantidad adeudada.</li>
<li><em>Estructura de dato</em>: es un grupo de datos elementales que en conjunto describen un componente del sistema.<br/>
Por ejemplo: Factura.</li>
</ol><p>Los flujos de datos, almacenes de datos son estructuras de datos.</p>
<p><strong>Notación del Diccionario de Datos</strong></p>
<ol><li><em>Notación del elemento dato</em>: Cada uno está identificado con un nombre, una descripción, un alias, una longitud, un intervalo de valores. Veamos las reglas a seguir para cada elemento.
<ul><li>Nombre de los datos: se deben asignar nombres que sean significativos, es decir, que tengan significado en el contexto del desarrollo del sistema.<br/>
Por ejemplo: Fecha-Factura. Un nombre no debe ser mayor de 30 caracteres y tampoco debe contener espacios en blanco.</li>
<li>Descripción de los datos: indica de manera breve lo que éste representa en el sistema, y debe escribirse de forma comprensible para el lector y pensando que quien lo lea no sabe nada con respecto al sistema.</li>
<li>Alias: es cuando el mismo dato recibe varios nombres, según quien haga uso del dato.<br/>
Ejemplo: factura puede tener como alias documento de pago o nota de pago etc.<br/>
No so alias los siguientes casos: factura autorizada, factura verificada.</li>
<li>Longitud: indica la cantidad de espacio necesario para cada dato sin considerar la forma en que serán almacenados.</li>
<li>Valores de los datos: si los valores de los datos están restringidos a un intervalo específico, debe reflejarse en la entrada del DD.<br/>
Por ejemplo: Talla unidad [centímetros], rango [1-200].</li>
</ul></li>
<li><em>Descripción de las estructuras de datos</em>: Las estructuras de datos se construyen sobre cuatro relaciones de componentes (datos o estructuras) que son:
<ul><li>Relación secuencial: Define los componentes (datos o estructuras) que siempre se incluyen en una estructura de datos en particular, es decir, también se llama concatenación de dos o más datos.</li>
<li>Relación de selección: Define alternativas para datos o estructuras incluidas en una estructura de datos.</li>
<li>Relación de iteración: Define la repetición de un componente cero o más veces.</li>
<li>Relación opcional: Es un caso especial de la iteración, es decir, una o ninguna relación.</li>
</ul></li>
<li><em>Descripción de los flujos de datos</em>: Representamos los flujos de datos siempre y cuando el flujo no sea un único atributo. Está formado por una o más estructuras previamente definidas. Del flujo nos interesa el contenido, fuente, destino, volumen.
<ul><li>Nombre del flujo de datos: se deben asignar nombres que sean significativos, es decir, que tengan significado en el contexto del desarrollo del sistema.<br/>
Por ejemplo: factura.</li>
<li>Fuente: indica cual es el proceso fuente de la información. Se indicará el número del proceso.</li>
<li>Destino: indica cual es el proceso destino de la información. Se indicará el número del proceso.</li>
<li>Definición: explica el contenido del flujo de datos.</li>
<li>Contenido: describe cuales son las estructuras de datos incluidas.</li>
</ul></li>
<li><em>Descripción de los almacenamientos de datos</em>: Representamos los almacenamientos de datos. Se documenta su contenido, flujos de entrada, flujos de salida.
<ul><li>Nombre de almacenamiento de datos: se asignan nombres que sean significativos, es decir, que tengan significado en el contexto del desarrollo del sistema.<br/>
Ejemplo: histórico facturas.</li>
<li>Flujos de entrada: indica cuales son los&nbsp; flujos que alimentan el almacenamiento de datos.</li>
<li>Flujos de salida: indica cuales son los flujos que extraen información del almacenamiento de datos.</li>
<li>Definición: describe el contenido del almacenamiento de datos.</li>
<li>Contenido: especifica el contenido del almacenamiento.</li>
</ul></li>
<li><em>Descripción de los procesos</em>: Representamos los procesos del sistema. Se documenta su contenido, flujos de entrada, flujos de salida.
<ul><li>Nombre de proceso: se asignan nombres que sean significativos, es decir, que tengan significado en el contexto del desarrollo del sistema.<br/>
Por ejemplo: verificar_crédito.</li>
<li>Entradas: indica cuales son los procesos, almacenamientos de datos que ejercen de fuente de datos.</li>
<li>Flujos de salida: indica cuales son los procesos, almacenamientos de datos que ejercen de destino de datos.</li>
<li>Definición: indica la misión del proceso.</li>
<li>Descripción: describe el proceso. Para ello utilizaremos: Forma narrativa, árboles de decisión, tablas de decisión, lenguaje estructurado.</li>
</ul></li>
<li><em>Descripción de las entidades externas</em>: Representamos las entidades externas del sistema. Se documenta a quien representa, flujos de datos relacionados, volumen, etc.
<ul><li>Nombre de entidad externa: se asignan nombres que sean significativos, que representen a la entidad.<br/>
Por ejemplo: clientes.</li>
<li>Flujos de datos asociados: indica cuales son los flujos (entrada/salida) asociados.</li>
<li>Definición: indica quienes son la entidad.</li>
<li>Volumen: número de componentes de la entidad.</li>
</ul></li>
</ol><p><strong>Sintaxis del Diccionario de Datos</strong></p>
<p>Conocida la forma de describir los datos y estructuras de datos, explicados en el apartado anterior, a continuación se va a establecer una sintaxis estandarizada que nos permitirá expresar dichos significados:</p>
<ul><li><strong>=</strong> está compuesto por</li>
<li><strong>+</strong> y</li>
<li><strong>()</strong> opcional, puede o no puede estar presente</li>
<li><strong>[]</strong> selección entre varias alternativas</li>
<li><strong>{}</strong> iteración, repetir los mismo varias veces</li>
<li><strong>**</strong> comentario</li>
<li><strong>@</strong> clave principal de un almacenamiento</li>
<li><strong>|</strong> separador de alternativas en selección</li>
</ul><p><strong>Ejemplo:</strong></p>
<p><em>Datos elementales</em></p>
<p>Son datos, que dentro del contexto del usuario, no tiene sentido descomponerlo. Es importante verificar: Valores permitidos y unidad de medida.</p>
<pre>peso_persona =* *
                * unidad: kilo ; rango: 1..150 *
sexo = * Masculino o Femenino *
       * valores: [ M | F ] *</pre>
<p><em>Datos opcionales</em></p>
<pre>Dirección_cliente = (dirección_entrega) + dirección_facturación)
Dirección_cliente = [ dirección_entrega | dirección_facturación |
                      dirección entrega + dirección_facturación ]
Dirección_cliente = dirección_entrega + (dirección_facturación)</pre>
<p><em>Iteración</em></p>
<p>Repetición de uno o más datos elementales o grupo de datos. ‘Cero o más ocurrencias’.</p>
<pre>pedido = nombre_cliente + dirección_entrega + { producto }</pre>
<p><em>Selección</em></p>
<p>‘Una y solo una de las alternativas’.</p>
<pre>sexo = [ Masculino | Femenino ]</pre>
<p><em>Dominio (No Yourdon)</em></p>
<p>Consiste definir una única vez cada tipo de Dato Elemental y referenciarlo para cada representación del tipo.</p>
<pre>fecha = * *
          * unidad: días ; rango : 0..36500 *
fec_nacimiento = fecha
fec_factura = fecha</pre>
<p><em>Alias (Sinónimo)</em></p>
<p>No se debe confundir con el dominio. Es un nombre alternativo para un dato elemental.</p>
<pre>fecha_contable = fecha
fecha_efectiva = * alias de: fecha_contable *
Nombre = Tratamiento + Nombre_pila + Primer_apellido + Segundo_apellido
Tratamiento = [ Sr. | Sra. | Srta. | D. | Dr. ]
Nombre_pila = {carácter}
Primer_apellido = {carácter}
Segundo_apellido = {carácter}
carácter = [ A-Z | a-z | - ]</pre>
<p><strong>Definición de un Diccionario de Datos</strong></p>
<p><strong>Definición de datos secuenciales</strong></p>
<p>Una definición se realiza mediante el símbolo = que significa <em>se define como</em> por lo tanto una expresión como A = B + C, se podría leer igual que de forma matemática, es decir, <em>A está compuesto de B y C</em>, pero para completarla se debería añadir: el significado de dicho dato en el contexto de la aplicación, el rango y tipo de valores que cada dato puede tomar.</p>
<p>Por ejemplo: En un sistema informático de un hospital:</p>
<pre>Datos_del_Paciente = nombre_completo +
                     *nombre completo del paciente *
                     *tipo: array de caracteres*
                     dirección +
                     *dirección completa del paciente*
                     *tipo: array de caracteres*
                     peso +
                     *peso del paciente*
                     *unidad: kilogramos; rango: 1-200*
                     talla +
                     *talla del paciente*
                     *unidad: centímetros; rango: 20-250*
                     fecha_ingreso +
                     *fecha de entrada en el hospital *
                     *tipo: fecha*</pre>
<p><strong>Definición de datos opcionales</strong></p>
<p>Es aquel dato que puede o no formar parte de la composición de un dato compuesto.</p>
<p>Ejemplo: La dirección de un cliente puede ser:</p>
<ul><li>Única: tanto la dirección comercial como de administración están en el mismo lugar que producción o almacén.</li>
<li>Dos direcciones: tiene el almacén y producción separado físicamente de la administración.</li>
</ul><p>Esta situación en un DD se trataría así:</p>
<pre>Cliente = nombre_completo + dni_cliente + dirección_comercial +
          (dirección_mercancías)</pre>
<p><strong>Definición de selección</strong></p>
<p>Sólo una de entre varias posibilidades será posible. Esta se define mediante [].</p>
<p>Ejemplo: Un cliente puede ser una empresa o un particular, por lo tanto los tipos de datos son distintos según sea uno u otro.</p>
<pre>cliente = [nombre_cliente | nombre_empresa] + [dni_cliente | cif_cliente] +
          dirección_comercial + (dirección_mercancías)</pre>
<p><strong>Definición de iteración</strong></p>
<p>La iteración se expresa mediante {} y sirve para indicar la repetición de una cierta ocurrencia dentro de una definición.</p>
<p>Ejemplo:</p>
<pre>Factura = fecha_factura + nombre_cliente + numero_factura +
          {linea_factura} + total_factura</pre>
<p>El dato línea_factura es un componente de la estructura de datos factura que puede tener una o varias ocurrencias, ya que una factura puede tener muchas líneas de facturación de artículos.</p>
<p><strong>Alias (Sinónimos)</strong></p>
<p>Son nombres que dentro del Sistema de información tienen el mismo significado, entonces lo que se hace es declarar los sinónimos por medio del símbolo =.</p>
<p>Ejemplo:</p>
<pre>Acreedor = cliente
           ** definido ya anteriormente.</pre>
<p>Hemos visto el contenido del Diccionario de Datos, que deberá mostrarse al usuario siempre conjuntamente con las técnicas:</p>
<ul><li>Diagrama de Flujo de Datos (DFD).</li>
<li>Modelo Entidad/Relación (DER).</li>
<li>Especificación de Procesos (EP).</li>
</ul><p><strong>Implementación del Diccionario de Datos</strong></p>
<p>Varias posibilidades para la implementación de los DD, cada una con sus características y ventajas.</p>
<ul><li>Repositorio de datos:
<ul><li>Herramientas automáticas integradas dentro de un entorno CASE.</li>
<li>Dispone de más posibilidades de las vistas.</li>
</ul></li>
<li>Diccionario de datos SGBD o SO modernos.
<ul><li>Dan soporte automático para definiciones de datos, validar su consistencia, producir algunos informes.</li>
</ul></li>
<li>Procesador de textos convencional.</li>
<li>Totalmente manual.</li>
</ul><p><strong>Ejemplo:</strong></p>
<p><em>Dato Elemental</em></p>
<pre>Nombre     : Estado_Civil
Descripción: Código de una letra para indicar el estado civil de cada
             empleado.
Long y tipo: 1 carácter alfabético.
Sinónimos  : ESTADO (Personal)
             CIVIL (Nóminas)
Valores    : <strong>S</strong> Soltero&nbsp; &nbsp; <strong>D</strong> Divorciado
             <strong>C</strong> Casado&nbsp; &nbsp;  <strong>S</strong> Separado
             <strong>V</strong> Viudo&nbsp; &nbsp;   <strong>O</strong> Otros</pre>
<p><em>Estructura de dato</em></p>
<pre>Nombre     : Empleado
Descripción: Datos necesarios de un empleado
Componentes: Nombre_empleado +
             Num_empleado +
             Datos_personales =
                                Fecha_nacimiento +
                                Estado_Civil +
                                Num_hijos [ 0 - ] +
                               (Num_tfno)
             Dirección =
                         Calle +
                         Número +
                         (Población) +
                         Codigo_Postal +
                         Provincia</pre>
<p><em>Flujo de datos</em></p>
<pre>Nombre           : Pago_aceptado
Ref              : 11.1 - 11.2
Fuente           : 11.1 Aceptar pago
Destino          : 11.2 Validar pago
Descripción      : Pago recibido y sellado pero no validado
Estruct. de datos: Cheque +
                   Recibo_Caja +
                   (Letra_Pago) +
                   Metodo_Pago
Volumen          : 5000 por día
Comentarios      : La letra de pago está omitida en el 10% de los casos</pre>
<p><em>Almacenamiento de datos</em></p>
<pre>Nombre          : Historia_Pedidos
Ref             : P4
Flujo de Entrada: 9 - D4&nbsp; &nbsp;Pedido
Flujo de Salida : D4 - 10&nbsp; &nbsp; Detalles pedido
                  D4 - 11&nbsp; &nbsp; Detalle ventas
                  D4 - 9&nbsp; &nbsp;  Demanda anterior
Descripción     : Todos los pedidos aceptados en los últimos 6 meses
Contenido       : Pedido =
                           Id_pedido +
                           Detalle_cliente +
                           Detalle_libro</pre>
<p><strong>Descripción lógica de un proceso</strong></p>
<p>Para el proceso V<em>erificar_Crédito</em> la plantilla correspondiente sería la siguiente:</p>
<p><em>Procesos</em></p>
<pre>Nombre     : Verificar_crédito
Ref        : 3
Definición : Decidir donde van los pedidos sin pago previo,
             o si debe pedirle el pago al cliente.
Entradas   : 1 - 3&nbsp; &nbsp; Pedidos
             D3 - 3&nbsp; &nbsp;Historia de pagos
Salidas    : 3 - C&nbsp; &nbsp; Pedido de pago previo
             3 - D3&nbsp; &nbsp;Nuevo balance de orden
             3 - 6&nbsp; &nbsp; Pedidos con crédito ok
Descripción: Recuperar historia de pago.
             Si el cliente es nuevo, enviar pedido de pago previo.
             Si el cliente corriente (promedio de dos pedidos mensuales)
             , OK con el pedido, a menos que el balance esté vencido con
             más de dos meses. Para clientes anteriores (no corrientes)
             , OK, a menos que tengan cualquier balance vencido.</pre>
<p>Hemos visto que para describir la lógica de un proceso, utilizaremos varias alternativas como son: narrativa, árboles de decisión, tablas de decisión y lenguaje estructurado.</p>
<p>Cuando utilizamos narrativa podemos encontrarnos con:</p>
<ul><li>frases oscuras (no solo, pero no obstante, sin embargo, …)</li>
<li>rangos con huecos indefinidos (‘ hasta 20 unidades sin descuento, más de 20 unidades al 50%’).</li>
<li>Frases con y/o (‘los clientes que nos compran más de 1 millón al año y tienen una buena historia de pago o que han tenido tratos con nosotros por más de 20 años deberán recibir trato preferencial’).</li>
<li>Adjetivos indefinidos (‘buena historia de pagos’, ‘trato preferencial’).</li>
</ul><p>Estas razones obligan a pensar en otras alternativas:</p>
<ul><li><strong>Árbol de decisión</strong>: Pueden resultar una técnica no válida en situaciones complejas con gran número de condiciones e implicaciones ya que no asegura que se hayan considerados todas.<br/>
Se debe utilizar cuando el número de acciones sea pequeño y no sean posibles todas las combinaciones.</li>
<li><strong>Tablas de decisión</strong>: Son más precisas dado que permiten reflejar todas la combinaciones posibles. Pero son más difíciles de entender para el usuario. Deben simplificarse una vez construidas y se convertirán en árboles de decisión.<br/>
Se debe utilizar siempre que se dude que el árbol muestra toda la lógica.
<pre>* Primera orden &gt; 12 días ---------- Hacer pedido
* Total ordenes &lt; menor que X
* Primera orden &lt;= 12 días ---------- Esperar
* Total ordenes &lt; mayor o igual que X ---------- Calcular
* Hacer pedido
* No descuento ---------- Hacer pedido</pre>
</li>
</ul><p><strong>Descripción lógica de una entidad externa</strong></p>
<p>Para la entidad <em>Proveedores</em> la plantilla correspondiente sería la siguiente:</p>
<p><em>Entidad Externa</em></p>
<pre>Nombre         : Proveedores
Ref            : p
Definición     : Proveedores actuales de la empresa
Flujos de Datos: 7 - p&nbsp; &nbsp; &nbsp;Pedidos
                 p - 3&nbsp; &nbsp; &nbsp;Albarán
                 p - 11&nbsp; &nbsp;&nbsp;Facturas
Volumen        : Actualmente 25. Se espera llegar a 40.</pre>
<h2>Bibliografia</h2>
<ul><li><a href="ftp://dlsi.ua.es/people/jaime/apuntes/aesi_cap3.pdf" rel="noopener" target="_blank">dlsi (Jaime)</a></li>
<li><a href="https://administracionelectronica.gob.es/pae_Home/pae_Documentacion/pae_Metodolog/pae_Metrica_v3.html#.Wtj023puZph" rel="noopener" target="_blank">PAe</a></li>
</ul> </article>

# Modelización conceptual. El modelo Entidad/Relación extendido (E/R): elementos. Reglas de modelización. Validación y construcción de modelos de datos.

<article><h2>Modelo Conceptual de Datos</h2>
<p>A la hora de determinar una BD debemos establecer un proceso partiendo del acotamiento de una parcela del mundo exterior (micromundo o universo del discurso), aquél que nos interesa representar en los datos. En este proceso se debe aprender, comprender y conceptualizar dicho mundo exterior transformándolo en un conjunto de ideas y definiciones que supongan una imagen fiel del comportamiento del mundo real. A esta imagen del mundo exterior la llamaremos <strong>Modelo Conceptual</strong>.</p>
<p>Una vez definido el modelo conceptual, éste se ha de transformar en una descripción de datos, atributos y relaciones que denominaremos Esquema Conceptual de datos. Por último, este esquema conceptual habrá que traducirlo a estructuras almacenables en soportes físicos. Por tanto es necesario distinguir entre Bases de Datos, que será el banco, el almacén de los valores (ocurrencias) de los datos. Los modelos de Datos, que son las herramientas para diseñar los datos y sus relaciones de forma que puedan soportar los valores correspondientes. Y finalmente los Sistemas Gestores de Bases de Datos (SGBD), que serán los encargados de las acciones que llevemos a cabo con las bases de datos, permitiendo también cumplimentar a los usuarios, mostrándoles los datos de acuerdo a sus necesidades. Con todo ello, se puede definir un Modelo de Datos como: Un grupo de herramientas conceptuales para describir los datos, sus relaciones, su semántica y sus limitaciones; de tal forma, que facilita la interpretación de nuestro mundo real y su representación en forma de datos, en nuestro sistema informático.</p>
<p>Definido el modelo de datos, pasamos a analizarlo. Para ello, partiremos de las propiedades que podemos diferenciar en dos tipos:</p>
<ul><li><strong>Estáticas</strong>: Son las propiedades invariantes en el tiempo. Quedan especificadas en el Modelo de Datos por ESTRUCTURAS. Esta se define mediante el ESQUEMA, con el lenguaje de definición de datos (DDL). El esquema, a su vez está constituido por Estructura y Restricciones. La Estructura queda definida por los Objetos del Modelo y las Restricciones inherentes, conformando un conjunto de reglas de definición de dichas Estructuras. Los objetos y Restricciones de la Estructura dependen de cada Modelo, pero en general son:
<ul><li>Entidades.</li>
<li>Atributos.</li>
<li>Dominio.</li>
<li>Relaciones.</li>
<li>Representación.</li>
<li>Restricciones: Hay tres tipos de restricciones:
<ul><li><em> Restricciones inherentes</em>: vienen impuestas por la propia naturaleza del Modelo introduciendo rigideces en la modelización.</li>
<li><em>Restricciones opcionales o de usuario</em>: restricciones propiamente dichas en el Esquema, son definidas por el usuario, pero el Modelo de Datos las reconoce y suministra herramientas para manejarlas.</li>
<li><em>Restricciones libres de usuarios</em>: son responsabilidad del usuario y el Modelo de Datos ni las reconoce, ni las maneja.</li>
</ul></li>
</ul></li>
<li><strong>Dinámicas</strong>: Son las propiedades que varían con el tiempo. En el modelo de datos son las OPERACIONES. Se define como un conjunto de Operaciones con el Lenguaje de Manipulación de Datos (DML). Las operaciones sobre un Modelo de Datos pueden ser de:
<ul><li>Selección. Localización de los datos deseados.</li>
<li>Acción. Realización de una acción sobre los datos seleccionados. Dicha acción puede ser:
<ul><li>Recuperación (obtención de los datos seleccionados).</li>
<li>Actualización, que a su vez pueden ser:
<ul><li>Modificación.</li>
<li>Inserción.</li>
<li>Borrado.</li>
</ul></li>
</ul></li>
</ul></li>
</ul><p>Generalmente, toda operación de Actualización va precedida de una Recuperación, aunque no necesariamente.</p>
<h2>Modelo Entidad/Relación Extendido</h2>
<p>Se trata de una técnica cuyo objetivo es la representación y definición de todos los datos que se introducen, almacenan, transforman y producen dentro de un sistema de información, sin tener en cuenta las necesidades de la tecnología existente, ni otras restricciones.</p>
<p>Dado que el modelo de datos es un medio para comunicar el significado de los datos, las relaciones entre ellos y las reglas de negocio de un sistema de información, una organización puede obtener numerosos beneficios de la aplicación de esta técnica, pues la definición de los datos y la manera en que éstos operan son compartidos por todos los usuarios.</p>
<p>Las ventajas de realizar un modelo de datos son, entre otras:</p>
<ul><li>Comprensión de los datos de una organización y del funcionamiento de la organización.</li>
<li>Obtención de estructuras de datos independientes del entorno físico.</li>
<li>Control de los posibles errores desde el principio, o al menos, darse cuenta de las deficiencias lo antes posible.</li>
<li>Mejora del mantenimiento.</li>
</ul><p>Aunque la estructura de datos puede ser cambiante y dinámica, normalmente es mucho más estable que la estructura de procesos. Como resultado, una estructura de datos estable e integrada proporciona datos consistentes que puedan ser fácilmente accesibles según las necesidades de los usuarios, de manera que, aunque se produzcan cambios organizativos, los datos permanecerán estables.</p>
<p>Este diagrama se centra en los datos, independientemente del procesamiento que los transforma y sin entrar en consideraciones de eficiencia. Por ello, es independiente del entorno físico y debe ser una fiel representación del sistema de información objeto del estudio, proporcionando a los usuarios toda la información que necesiten y en la forma en que la necesiten.</p>
<h3>Descripción</h3>
<p>El modelo entidad/relación extendido describe con un alto nivel de abstracción la distribución de datos almacenados en un sistema. Existen dos elementos principales: las entidades y las relaciones. Las extensiones al modelo básico añaden además los atributos de las entidades y la jerarquía entre éstas. Estas extensiones tienen como finalidad aportar al modelo una mayor capacidad expresiva.</p>
<p>Los elementos fundamentales del modelo son los siguientes:</p>
<p><strong>Entidad</strong></p>
<p>Es aquel objeto, real o abstracto, acerca del cual se desea almacenar información en la base de datos. La estructura genérica de un conjunto de entidades con las mismas características se denomina tipo de entidad.</p>
<p>Existen dos clases de entidades:</p>
<ul><li>Regulares: tienen existencia por sí mismas.</li>
<li>Débiles: cuya existencia depende de otra entidad.</li>
</ul><p>Las entidades deben cumplir las siguientes tres reglas:</p>
<ul><li>Tienen que tener existencia propia.</li>
<li>Cada ocurrencia de un tipo de entidad debe poder distinguirse de las demás.</li>
<li>Todas las ocurrencias de un tipo de entidad deben tener los mismos atributos.</li>
</ul><p><strong>Relación</strong></p>
<p>Es una asociación o correspondencia existente entre una o varias entidades. La relación puede ser regular, si asocia tipos de entidad regulares, o débil, si asocia un tipo de entidad débil con un tipo de entidad regular. Dentro de las relaciones débiles se distinguen la <strong>dependencia en existencia</strong> y la <strong>dependencia en identificación</strong>.</p>
<p>Se dice que la dependencia es en existencia cuando las ocurrencias de un tipo de entidad débil no pueden existir sin la ocurrencia de la entidad regular de la que dependen. Se dice que la dependencia es en identificación cuando, además de lo anterior, las ocurrencias del tipo de entidad débil no se pueden identificar sólo mediante sus propios atributos, sino que se les tiene que añadir el identificador de la ocurrencia de la entidad regular de la cual dependen.</p>
<p>Además, se dice que una relación es <strong>exclusiva</strong> cuando la existencia de una relación entre dos tipos de entidades implica la no existencia de las otras relaciones.</p>
<p>Una relación se caracteriza por:</p>
<ul><li><strong>Nombre</strong>: que lo distingue unívocamente del resto de relaciones del modelo.</li>
<li><strong>Tipo de correspondencia</strong>: es el número máximo de ocurrencias de cada tipo de entidad que pueden intervenir en una ocurrencia de la relación que se está tratando. Conceptualmente se pueden identificar tres clases de relaciones:
<ul><li><em>Relaciones 1:1</em>: Cada ocurrencia de una entidad se relaciona con una y sólo una ocurrencia de la otra entidad.</li>
<li><em>Relaciones 1:N</em>: Cada ocurrencia de una entidad puede estar relacionada con cero, una o varias ocurrencias de la otra entidad.</li>
<li><em>Relaciones M:N</em>: Cada ocurrencia de una entidad puede estar relacionada con cero, una o varias ocurrencias de la otra entidad y cada ocurrencia de la otra entidad puede corresponder a cero, una o varias ocurrencias de la primera.</li>
</ul></li>
<li><strong>Cardinalidad</strong>: representa la participación en la relación de cada una de las entidades afectadas, es decir, el número máximo y mínimo de ocurrencias de un tipo de entidad que pueden estar interrelacionadas con una ocurrencia de otro tipo de entidad. La cardinalidad máxima coincide con el tipo de correspondencia.<br/>
Según la cardinalidad, una relación es obligatoria, cuando para toda ocurrencia de un tipo de entidad existe al menos una ocurrencia del tipo de entidad asociado, y es opcional cuando, para toda ocurrencia de un tipo de entidad, puede existir o no una o varias ocurrencias del tipo de entidad asociado.</li>
</ul><p><strong>Dominio</strong></p>
<p>Es un conjunto nominado de valores homogéneos. El dominio tiene existencia propia con independencia de cualquier entidad, relación o atributo.</p>
<p><strong>Atributo</strong></p>
<p>Es una propiedad o característica de un tipo de entidad. Se trata de la unidad básica de información que sirve para identificar o describir la entidad. Un atributo se define sobre un dominio. Cada tipo de entidad ha de tener un conjunto mínimo de atributos que identifiquen unívocamente cada ocurrencia del tipo de entidad. Este atributo o atributos se denomina identificador principal. Se pueden definir restricciones sobre os atributos, según las cuales un atributo puede ser:</p>
<ul><li>Univaluado, atributo que sólo puede tomar el valor para todas y cada una de las ocurrencias del tipo de entidad al que pertenece.</li>
<li>Obligatorio, atributo que tiene que tomar al menos un valor para todas y cada una de las ocurrencias del tipo de entidad al que pertenece.</li>
</ul><p>Además de estos elementos, existen extensiones del modelo entidad/relación que incorporan determinados conceptos o mecanismos de abstracción para facilitar la representación de ciertas estructuras del mundo real:</p>
<ul><li>La <strong>generalización</strong>, permite abstraer un tipo de entidad de nivel superior (supertipo) a partir de varios tipos de entidad (subtipos); en estos casos los atributos comunes y relaciones de los subtipos se asignan al supertipo. Se pueden generalizar por ejemplo los tipos <em>profesor</em> y <em>estudiante</em> obteniendo el <em>supertipo</em> persona.</li>
<li>La <strong>especialización</strong> es la operación inversa a la generalización, en ella un supertipo se descompone en uno o varios subtipos, los cuales heredan todos los atributos y relaciones del supertipo, además de tener los suyos propios. Un ejemplo es el caso del tipo <em>empleado</em>, del que se pueden obtener los subtipos <em>secretaria</em>, <em>técnico</em> e <em>ingeniero</em>.</li>
<li><strong>Categorías</strong>. Se denomina categoría al subtipo que aparece como resultado de la unión de varios tipos de entidad. En este caso, hay varios supertipos y un sólo subtipo. Si por ejemplo se tienen los tipos <em>persona</em> y <em>compañía</em> y es necesario establecer una relación con <em>vehículo</em>, se puede crear <em>propietario</em> como un subtipo unión de los dos primeros.</li>
<li>La <strong>agregación</strong>, consiste en construir un nuevo tipo de entidad como composición de otros y su tipo de relación y así poder manejarlo en un nivel de abstracción mayor. Por ejemplo, se tienen los tipos de entidad <em>empresa</em> y <em>solicitante de empleo</em> relacionados mediante el tipo de relación <em>entrevista</em>; pero es necesario que cada <em>entrevista</em> se corresponda con una determinada <em>oferta de empleo</em>. Como no se permite la relación entre tipos de relación, se puede crear un tipo de entidad compuesto por <em>empresa</em>, <em>entrevista</em> y <em>solicitante de empleo</em> y relacionarla con el tipo de entidad <em>oferta de empleo</em>. El proceso inverso se denomina desagregación.</li>
<li>La <strong>asociación</strong>, consiste en relacionar dos tipos de entidades que normalmente son de dominios independientes, pero coyunturalmente se asocian.</li>
</ul><p>La existencia de supertipos y subtipos, en uno o varios niveles, da lugar a una <strong>jerarquía</strong>, que permitirá representar una restricción del mundo real.</p>
<p>Una vez construido el modelo entidad/relación, hay que analizar si se presentan redundancias. Para poder asegurar su existencia se deben estudiar con mucho detenimiento las cardinalidades mínimas de las entidades, así como la semántica de las relaciones.</p>
<p>Los atributos redundantes, los que se derivan de otros elementos mediante algún cálculo, deben ser eliminados del modelo entidad/relación o marcarse como redundantes.</p>
<p>Igualmente, las relaciones redundantes deben eliminarse del modelo, comprobando que al eliminarlas sigue siendo posible el paso, tanto en un sentido como en el inverso, entre las dos entidades que unían.</p>
<h3>Notación</h3>
<p><strong>Entidad</strong></p>
<p>La representación gráfica de un tipo de entidad regular es un rectángulo con el nombre del tipo de entidad. Un tipo de entidad débil se representa con dos rectángulos concéntricos con su nombre en el interior.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/entidad.png?w=825"/></p>
<p><strong>Relación</strong></p>
<p>Se representa por un rombo unido a las entidades relacionadas por dos líneas retas a los lados. El tipo de correspondencia se representa gráficamente con una etiqueta <em>1:1</em>, <em>1:N</em> o <em>M:N</em>, cerca de alguno de los vértices del rombo, o bien situando cada número o letra cerca de la entidad correspondiente, para mayor claridad.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/relacion.png?w=825"/></p>
<p>La representación gráfica de las cardinalidades se realiza mediante una etiqueta del tipo <em>(0,1)</em>, (<em>1,1)</em>, <em>(0,n)</em> o <em>(1,n)</em>, que se coloca en el extremo de la entidad que corresponda. Si se representan las cardinalidades, la representación del tipo de correspondencia es redundante.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/relacion1.png?w=825"/></p>
<p><em>Relaciones del tipo M:N (Muchos a Muchos):</em></p>
<p>Si existe un concepto que puede sustituir la relación, tiene sentido como entidad y aporta una mejor comprensión al modelo (para usuarios y analistas) es conveniente deshacerlas mediante esta entidad y las relaciones uno a muchos adecuadas.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/muchos_a_muchos.png?w=825"/></p>
<p><em>Relaciones entre Tres o Más Entidades</em></p>
<p>Las relaciones entre tres o más entidades se reclasificarán mediante una entidad relacionada con cada una de ellas, si existe un concepto que puede ser representado como una entidad, y aporta mayor comprensión al problema.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/relaciones_tres_o_mas.png?w=825"/></p>
<p><em>Relaciones potencialmente redundantes</em></p>
<p>Pueden serlo o no, depende del significado de las relaciones y de las cardinalidades.</p>
<p>Deben ser eliminadas.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/relaciones_redundantes.png?w=825"/></p>
<p><em>Relaciones Recursivas o Autorrelaciones</em></p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/relaciones_recursivas.png?w=825"/></p>
<p><strong>Atributo</strong></p>
<p>Un atributo se representa mediante una elipse, con su nombre dentro, conectada por una línea al tipo de entidad o relación.</p>
<p>En lugar de una elipse puede utilizarse un círculo con el nombre dentro, o un círculo más pequeño con el nombre del atributo a un lado. También pueden representarse en una lista asociada a la entidad. El identificador aparece con el nombre marcada o subrayado, o bien con su círculo en negro.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/atributo.png?w=825"/></p>
<p><strong>Exclusividad</strong></p>
<p>En la representación de las relaciones exclusivas se incluye un arco sobre las líneas que conectan el tipo de entidad a los dos o más tipos de relación.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/exclusividad.png?w=825"/></p>
<p><strong>Jerarquía (tipos y subtipos)</strong></p>
<p>La representación de las jerarquías se realiza mediante un triángulo invertido, con la base paralela al rectángulo que representa el supertipo y conectando a éste y a los subtipos. Si la división en subtipos viene determinada en función de los valores de un atributo discriminante, éste se representará asociado al triángulo que representa la relación.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/jerarquia.png?w=825"/></p>
<p>En el triángulo se representará: con una letra <strong>d</strong> el hecho de que los subtipos sean disjuntos, con un círculo o una <strong>O</strong> si los subtipos pueden solaparse y con un <strong>U</strong> el caso de uniones por categorías. La presencia de una jerarquía total se representa con una doble línea entre el supertipo y el triángulo.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/tipos_y_subtipos.png?w=825"/></p>
<p><strong>Ejemplo</strong></p>
<p>Modelo entidad-relación extendido para un sistema de gestión de técnicos y su asignación a proyectos dentro de una empresa u organización.</p>
<p>Como se aprecia en el diagrama, TÉCNICO es un subtipo de EMPLEADO, generado por especialización, pues era necesario para establecer la relación <em>Trabaja en</em> con PROYECTO, ya que no todos los empleados de la empresas, como los administrativos, son susceptibles de trabajar en un proyecto. La entidad TÉCNICO tendrá los atributos de EMPLEADO más el atributo <em>nivel</em>.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/ejemplo.png?w=825"/></p>
<p>Los tipos de correspondencia son <em>1:N</em> entre DEPARTAMENTO y EMPLEADO, pues un departamento tienen 1 o varios empleados. Entre TÉCNICO y PROYECTO es <em>M:N</em>, pues un técnico puede trabajar en 1 o varios proyectos, y en un proyecto trabajan 1 o varios técnicos.</p>
<p>Por otro lado, se han incluido atributos que caracterizan la relación <em>Trabaja en</em>, como son <em>fecha de asignación</em> y <em>fecha de cese</em>, ya que un técnico no siempre estará trabajando en un proyecto, sino en determinado periodo. (Nota.- Esta notación es la más habitual, pero MÉTRICA Versión 3 no exige su utilización).</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/cardinalidad.png?w=825"/></p>
<h2>Normalización</h2>
<p>La teoría de la normalización tiene por objetivo la eliminación de dependencias entre atributos que originen anomalías en la actualización de los datos, y proporcionar una estructura más regular para la representación de las tablas, constituyendo el soporte para el diseño de bases de datos relacionales.</p>
<p>Como resultado de la aplicación de esta técnica se obtiene un modelo lógico de datos normalizado.</p>
<h3>Descripción</h3>
<p>La teoría de la normalización, como técnica formal para organizar los datos, ayuda a encontrar fallos y a corregirlos, evitando así introducir anomalías en las operaciones de manipulación de datos.</p>
<p>Se dice que una relación está en una determinada forma normal si satisface un cierto conjunto de restricciones sobre los atributos. Cuanto más restricciones existan, menor será el número de relaciones que las satisfagan, así, por ejemplo, una relación en tercera forma normal estará también en segunda y en primera forma normal.</p>
<p>Antes de definir las distintas formas normales se explican, muy brevemente, algunos conceptos necesarios para su comprensión.</p>
<p><strong>Dependencia funcional</strong></p>
<p>Un atributo <em>Y</em> se dice que depende funcionalmente de otro <em>X</em> si, y sólo si, a cada valor de <em>X</em> le corresponde un único valor de <em>Y</em>, lo que se expresa de la siguiente forma: <em>X&nbsp;→ Y</em> (también se dice que <em>X</em> determina o implica a <em>Y</em>).</p>
<p><em>X</em> se denomina implicante o determinante e <em>Y</em> es el implicado.</p>
<p><strong>Dependencia funcional completa</strong></p>
<p>Un atributo <em>Y</em> tiene dependencia funcional completa respecto de otro <em>X</em>, si depende funcionalmente de él en su totalidad, es decir, no depende de ninguno de los posibles atributos que formen parte de <em>X</em>.</p>
<p><strong>Dependencia transitiva</strong></p>
<p>Un atributo depende transitivamente de otro si, y sólo si, depende de él a través de otro atributo. Así, <em>Z</em> depende transitivamente de <em>X</em>, si:</p>
<pre>X&nbsp;→ Y
Y ---/→ X
Y&nbsp;→ Z</pre>
<p>Se dice que <em>X</em> implica a <em>Z</em> a través de <em>Y</em>.</p>
<p>Una vez definidas las anteriores dependencias, se pueden enunciar las siguientes formas normales:</p>
<p><em>Primera Forma Normal (1FN)</em></p>
<p>Una entidad está en 1FN si no tiene grupos repetitivos, es decir, un atributo sólo puede tomar un único valor de un dominio simple.</p>
<p>Una vez identificados los atributos que no dependen funcionalmente de la clave principal, se formará con ellos una nueva entidad y se eliminarán de la antigua. La clave principal de la nueva entidad estará formada por la concatenación de uno o varios de sus atributos más la clave principal de la antigua entidad.</p>
<p><em>Segunda Forma Normal (2FN)</em></p>
<p>Una entidad está en 2FN si está en 1FN y todos los atributos que no forman parte de las claves candidatas (atributos no principales) tienen dependencia funcional completa respecto de éstas, es decir, no hay dependencias funcionales de atributos no principales respecto de una parte de las claves. Cada uno de los atributos de una entidad depende de toda la clave.</p>
<p>Una vez identificados los atributos que no dependen funcionalmente de toda la clave, sino sólo de parte de la misma, se formará con ellos una nueva entidad y se eliminarán de la antigua. La clave principal de la nueva entidad estará formada por la parte de la antigua de la que dependen funcionalmente.</p>
<p><em>Tercera Forma Normal (3FN)</em></p>
<p>Una entidad está en 3FN si está en 2FN y todos sus atributos no principales dependen directamente de la clave primaria, es decir, no hay dependencias funcionales transitivas de atributos no principales respecto de las claves.</p>
<p>Una vez identificados los atributos que dependen de otro atributo distinto de la clave, se formará con ellos una nueva entidad y se eliminarán de la antigua. La clave principal de la nueva entidad será el atributo del cual dependen. Este atributo en la entidad antigua, pasará a ser una clave ajena.</p>
<h3>Notación</h3>
<p>Una herramienta muy útil para visualizar las dependencias funcionales es el grafo o diagrama de dependencias funcionales, mediante el cual se representa un conjunto de atributos y las dependencias funcionales existentes entre ellos.</p>
<p>En el grafo aparecen los nombre de los atributos unidos por flechas, las cuales indican las dependencias funcionales completas que existen entre ellos, partiendo del implicante hacia el implicado. Cuando el implicante de una dependencia no es un único atributo, es decir, se trata de un implicante compuesto, los atributos que lo componen se encierran en un recuadro y la flecha parte de éste, no de cada atributo.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/dependencia_funcional.png?w=825"/></p>
<p>En la figura se presenta un ejemplo de cómo se visualizan las dependencias. Se puede observar que COD_LIBRO determina funcionalmente el TITULO del libro y la EDITORIAL, como indica la correspondiente flecha; de forma análoga, NUM_SOCIO determina NOMBRE, DOMICILIO y TEL. del socio (suponiendo que sólo se proporciona un teléfono); mientras que ambos atributos en conjunto COD_LIBRO y NUM_SOCIO (lo que se indica mediante el recuadro que los incluye) determinan FECHA_PRESTAMO y FECHA_DEV.</p>
<h3>Ejemplo</h3>
<p>Sea una entidad TÉCNICOS de un grupo de empresas, con los siguientes atributos:</p>
<ul><li>cod_empresa</li>
<li>cod_técnico</li>
<li>nombre_técnico</li>
<li>cod_categoría</li>
<li>categoría</li>
<li>nombre_empresa</li>
<li>fecha_alta</li>
<li>fecha_baja</li>
<li>cod_conoc</li>
<li>titulo_conoc</li>
<li>área_conoc</li>
<li>grado</li>
<li>cod_proyecto</li>
<li>nombre_proyecto</li>
<li>f_inicio</li>
<li>f_fin</li>
<li>f_asignación</li>
<li>f_cese</li>
<li>cod_cliente</li>
<li>nombre_cliente</li>
</ul><p>La entidad TÉCNICOS tiene la clave principal compuesta por <em>cod_empresa</em> y <em>cod_técnico</em>, ya que, al ser varias empresas, el código de técnico no será único, sino que puede coincidir con otros de otras empresas.</p>
<p><em>Primera Forma Normal (1FN)</em></p>
<p>Evidentemente no se cumple la primera forma normal, ya que un técnico tendrá más o de un conocimiento (lenguajes, sistemas, operativos, bases de datos, etc), es decir habrá varios valores de <em>cod_conoc</em>, por lo que este atributo y los asociados a conocimientos no dependen funcionalmente de la clave principal.</p>
<p>Los atributos <em>cod_conoc</em>, <em>título_conoc</em>, <em>área_conoc</em> y <em>grado</em> identificados como no dependientes, formarán la nueva entidad CONOCIMIENTOS y desaparecerán de la entidad TÉCNICOS. La clave de la nueva entidad será <em>cod_conoc</em> concatenada con <em>cod_empresa</em> y <em>cod_técnico</em>.</p>
<p>Por otro lado, en este sistema un técnico puede trabajar en más de un proyecto a tiempo parcial, por lo que <em>cod_proyecto</em> tampoco depende funcionalmente de la clave principal de TÉCNICOS.</p>
<p>Se obtiene entonces la entidad PROYECTOS con los atributos de los proyectos, y su clave compuesta de <em>cod_proyecto</em> concatenada con <em>cod_empresa</em> y <em>cod_técnico</em> de la antigua entidad.</p>
<p>Esta situación se completará con dos tipos de relaciones: <em>Poseen</em>, cuyo tipo de correspondencia es <em>1:N</em> entre TÉCNICOS y CONOCIMIENTOS y <em>Están asignados</em>, también del tipo <em>M:N</em> entre TÉCNICOS y PROYECTOS, tal y como muestra el diagrama siguiente:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/diagrama_1fn.png?w=825"/></p>
<p>Como se aprecia en la figura, se ha trasladado el atributo <em>grado</em> de la entidad CONOCIMIENTOS a la relación <em>Poseen</em>, pues es un atributo que determina la relación entre las dos entidades. También han sido trasladado los atributos que caracterizan la relación <em>Están asignados</em>, como son <em>f_asignación</em> y <em>f_cese</em>, ya que un técnico no siempre estará trabajando en un proyecto, sino en determinado periodo.</p>
<p><em>Segunda Forma Normal (2FN)</em></p>
<p>En la entidad TÉCNICOS se observa que el atributo <em>nombre_empresa</em> no tiene una dependencia funcional completa con la clave, sino que la tiene sólo de una parte de la misma: <em>cod_empresa</em>.</p>
<p>El atributo identificado formará parte de una nueva entidad, EMPRESAS, siendo eliminado de la antigua. La clave principal de la nueva entidad será <em>cod_empresa</em>.</p>
<p>Para representar la segunda forma normal en el modelo de datos, deberá añadirse un tipo de relación, <em>Se componen</em>, y el tipo de correspondencia <em>1:N</em>.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/diagrama_2fn.png?w=825"/></p>
<p><em>Tercera Forma Normal (3FN)</em></p>
<p>En la entidad TÉCNICOS de la figura se puede observar que para un <em>cod_técnico</em> hay un único <em>cod_categoría</em>, es decir, el segundo depende funcionalmente del primero; para un <em>cod_categoría</em> hay una única <em>categoría</em>, es decir, que este atributo depende funcionalmente del <em>cod_categoría</em>; y por último, para un <em>cod_categoría</em> hay varios valores de <em>cod_técnico</em>. Así pues, la categoría depende transitivamente del <em>cod_técnico</em>, por lo que la entidad TÉCNICOS no está en 3FN.</p>
<p>Una vez identificado el atributo categoría que depende de otro atributo distinto de la clave, <em>cod_categoría</em>, se formará con él una nueva entidad y se quitará de la antigua. La clave principal de la nueva entidad será el atributo del cual depende <em>cod_categoría</em> y en la entidad antigua pasará a ser una clave ajena.</p>
<p>Del mismo modo, puede observarse que la entidad PROYECTOS tampoco está en 3FN, pues el <em>nombre_cliente</em> depende de <em>cod_cliente</em>, que no forma parte de la clave de la entidad.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/diagramas_3fn.png?w=825"/></p>
<p>Así pues, aparecen dos entidades nuevas en el modelo: CATEGORÍAS y CLIENTES, y sus respectivas relaciones y tipos de correspondencias: <em>Están clasificados 1:N</em> y <em>Tiene contratados 1:N</em>.</p>
<h2>Optimización</h2>
<p>El objetivo de esta técnica es reestructurar el modelo físico de datos con el fin de asegurar que satisface los requisitos de rendimiento establecidos y conseguir una adecuada eficiencia del sistema.</p>
<h3>Descripción</h3>
<p>La optimización consiste en una desnormalización controlada del modelo físico de datos que se aplica para reducir o simplificar el número de accesos a la base de datos.</p>
<p>Para ello, se seguirán alguna de las recomendaciones que a continuación se indican:</p>
<ul><li>Introducir elementos redundantes.</li>
<li>Dividir entidades.</li>
<li>Combinar entidades si los accesos son frecuentes dentro de la misma transacción.</li>
<li>Redefinir o añadir relaciones entre entidades para hacer más directo el acceso entre entidades.</li>
<li>Definir claves secundarias o índices para permitir caminos de acceso alternativos.</li>
</ul><p>Con el fin de analizar la conveniencia o no de la desnormalización, se han de considerar, entre otros, los siguientes aspectos:</p>
<ul><li>Los tiempos de respuesta requeridos.</li>
<li>La tasa de actualizaciones respecto a la de recuperaciones.</li>
<li>Las veces que se accede conjuntamente a los atributos.</li>
<li>La longitud de los mismos.</li>
<li>El tipo de aplicaciones (en línea / por lotes).</li>
<li>La frecuencia y tipo de acceso.</li>
<li>La prioridad de los accesos.</li>
<li>El tamaño de las tablas.</li>
<li>Los requisitos de seguridad: accesibilidad, confidencialidad, integridad y disponibilidad que se consideren relevantes.</li>
</ul><h2>Reglas de Obtención del Modelo Físico a partir del Lógico</h2>
<p>El objetivo de esta técnica es obtener un modelo físico de datos a paritr del modelo lógico de datos normalizado. Para ello es necesario aplicar un conjunto de reglas que conserven la semántica del modelo lógico.</p>
<h3>Descripción</h3>
<p>Cada uno de los elementos del modelo lógico se tiene que transformar en un elemento del modelo físico. En algunos casos la transformación es directa porque el concepto se soporta igual en ambos modelos, pero otras veces no existe esta correspondencia, por lo que es necesario buscar una transformación que conserve lo mejor posible la semántica, teniendo en cuenta los aspectos de eficiencia que sean necesarios en cada caso.</p>
<p><strong>Transformación de entidades</strong></p>
<p>Una entidad se transforma en una tabla.</p>
<p><strong>Transformación de atributos de entidades</strong></p>
<p>Cada atributo se transforma en una columna de la tabla en la que se transformó la entidad a la que pertenece. El identificador único se convierte en clave primaria.</p>
<p>Si existen restricciones asociadas a los atributos, éstas pueden recogerse con algunas cláusulas del lenguaje lógico, que se convertirán en disparadores cuando éstos sean soportados por el sistema gestor de base de datos.</p>
<p><strong>Transformación de relaciones</strong></p>
<p>Según el tipo de correspondencia:</p>
<ul><li><strong>Relaciones 1:N</strong>: se propaga el identificador de la entidad de cardinalidad máxima <em>1</em> a la que es <em>N</em>, teniendo en cuenta que:
<ul><li>Si la relación es de asociación, la clave propagada es clave ajena en la tabla a la que se ha propagado.</li>
<li>Si la relación es de dependencia, la clave primaria de la tabla correspondiente a la entidad débil está formada por la concatenación de los identificadores de ambas entidades.</li>
</ul></li>
<li><strong>Relaciones 1:1</strong>: es un caso particular de las <em>1:N</em> y por tanto se propaga la clave en las dos direcciones. Se debe analizar la situación, intentando recoger la mayor semántica posible, y evitar valores nulos.</li>
</ul><p>Las relaciones de agregación se transforman del mismo modo que las <em>1:N</em>.</p>
<p><strong>Transformación de relaciones exclusivas</strong></p>
<p>Después de haber realizado la transformación según las relaciones <em>1:N</em>, se debe tener en cuenta que si los identificadores propagados se han convertido en claves ajenas de la tabla originada por la entidad común a las relaciones, hay que comprobar que una y sólo una de esas claves es nula en cada ocurrencia. En otro caso, estas comprobaciones se deben hacer en las tablas resultantes de transformar las relaciones.</p>
<p><strong>Transformación de la jerarquía</strong></p>
<p>Existen varias posibilidades que deben ser evaluadas por el diseñador a fin de elegir la que mejor se ajuste a los requisitos. Las opciones para tratar la transformación de la jerarquía son:</p>
<ul><li><strong>Opción a</strong>: Consiste en crear una tabla para el supertipo que tenga de clave primaria el identificador y una tabla para cada uno de los subtipos que tengan el identificador del supertipo como clave ajena.<br/>
Esta solución es apropiada cuando los subtipos tienen muchos atributos distintos y se quieren conservar los atributos comunes en una tabla. También se deben implantar las restricciones y aserciones adecuadas. Es la solución que mejor conserva la semántica.</li>
<li><strong>Opción b</strong>: Se crea una tabla para cada subtipo, los atributos comunes aparecen en todos los subtipos y la clave primaria para cada tabla es el identificador del supertipo.<br/>
Esta opción mejora la eficiencia en los accesos a todos los atributos de un subtipo, sean los comunes al supertipo o los específicos.</li>
<li><strong>Opción c</strong>: Agrupar en una tabla todos los atributos de la entidad supertipo y de los subtipos. La clave primaria de esta tabla es el identificador de la entidad. Se añade un atributo que indique a qué subtipo pertenece cada ocurrencia (el atributo discriminante de la jerarquía). Esta solución puede aplicarse cuando los subtipos se diferencien en pocos atributos y las relaciones entre los subtipos y otras entidades sean las mismas. Para el caso de que la jerarquía sea total, el atributo discriminante no podrá tomar valor nulo (ya que toda ocurrencia pertenece a alguna de las entidades subtipo).</li>
</ul><h3>Notación</h3>
<p><strong>Tabla</strong></p>
<p>La representación gráfica de una tabla es un rectángulo con una línea horizontal que lo divide en dos. La parte superior, de ancho menor, se etiqueta con el nombre de la tabla.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/tabla.png?w=825"/></p>
<p><strong>Relación</strong></p>
<p>La relación entre tablas se representa gráficamente mediante una línea que las une. En ella pueden aparecer en sus extremos diversos símbolos para indicar la cardinalidad de la relación, como se muestra a continuación:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/relacion2.png?w=825"/></p>
<p><em>Ejemplo.</em></p>
<p>Sea el diagrama entidad-relación del ejemplo realizado para la Normalización sobre conocimientos de técnicos informáticos y su asignación a proyectos.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/diagrama_entidad_relacion.png?w=825"/></p>
<p>El modelo físico de la figura muestra que cada una de las entidades se ha convertido en una tabla, cuyo contenido coincide con los atributos de la entidad. Pero hay dos tablas más: POSEEN, que surge de la relación del mismo nombre y ASIGNACIONES, que se origina a partir de la relación <em>Están asignados</em>.</p>
<p>La tabla POSEEN está formada por su atributo <em>grado</em>, más <em>cod_empresa</em>, <em>cod_tecnico</em> y <em>cod_conoc</em>. La tabla ASIGNACIONES se forma con los atributos clave <em>cod_empres</em>a, <em>cod_tecnico</em> y <em>cod_proyecto</em> y los propios <em>f_asignación</em> y <em>f_cese</em>.</p>
<p>La relación entre EMPRESAS y TÉCNICOS era <em>1:N</em>, y la cardinalidad de la figura así lo muestra, pues la empresa siempre estará compuesta de uno o varios técnicos. Lo mismo sucede entre CLIENTES y PROYECTOS: un cliente siempre tendrá 1 o varios proyectos contratados.</p>
<p>El caso de CATEGORÍAS y TÉCNICOS es <em>(0,n)</em>. Cada técnico es de una categoría y una categoría corresponde, por regla general, a varios técnicos, pero puede existir alguna en la que no encaje ningún técnico (contable, secretaria de dirección, etc.).</p>
<p>La situación del subconjunto TÉCNICOS-POSEEN-CONOCIMIENTOS tienen algo más de complejidad. Un técnico posee normalmente varios conocimientos, pero debe poseer al menos uno para que tenga sentido su situación. La cardinalidad es pues <em>(1,n)</em> entre TÉCNICOS y POSEEN. En el otro lado, lo natural es que un conocimiento sea poseído por varios técnicos, sin embargo puede existir algún conocimiento que no sea poseído por ningún técnico, por lo que la cardinalidad es <em>(0,n)</em> y dibujada desde la tabla CONOCIMIENTOS a POSEEN.</p>
<p>Por último, en el subconjunto TÉCNICOS-ASIGNACIONES-PROYECTOS, se dispone de: una cardinalidad <em>(0,n)</em>, pues a un proyecto estarán asignados uno o más técnicos, pero puede haber algún técnico que, en un momento dado, no esté asignado aún a ningún proyecto y una cardinalidad <em>(1,n)</em>, pues un proyecto siempre tendrá asignado al menos a un técnico, o varios.</p>
<p>(Nota.- La notación utilizada para el ejemplo es la más habitual, pero MÉTRICA Versión 3 no exige su utilización).</p>
<h2>Reglas de Transformación</h2>
<p>El objetivo de esta técnica es obtener un modelo físico de datos a partir del modelo de clases. Para ello es necesario aplicar un conjunto de reglas de transformación que conserven la semántica del modelo de clases.</p>
<h3>Descripción</h3>
<p>Cada uno de los elementos del modelo de clases se tiene que transformar en un elemento del modelo físico. En algunos casos la transformación es directa porque el concepto se soporta igual en ambos modelos, pero otras veces no existe esta correspondencia, por lo que es necesario buscar una transformación que conserve lo mejor posible la semántica, teniendo en cuenta los aspectos de eficiencia que sean necesarios en cada caso.</p>
<p><strong>Transformación de clases</strong></p>
<p>Una clase se transforma en una tabla. Lo habitual es que en los modelos con herencia pueden surgir excepciones cuando se apliquen las reglas de transformación propias de la herencia. Además, es posible que dos clases se transformen en una sola tabla cuando el comportamiento de una de ellas sea irrelevante en la base de datos.</p>
<p><strong>Transformación de atributos de clases</strong></p>
<p>Cada atributo se transforma en una columna de la tabla en la que se transformó la clase a la que pertenece. El identificador único se convierte en clave primaria. Además, se deben tener en cuenta las reglas de transformación que se aplican a la herencia de clases.</p>
<p>Si existen restricciones asociadas a los atributos, éstas pueden recogerse con algunas cláusulas del lenguaje lógico, que se convertirán en disparadores cuando éstos sean soportados por el sistema gestor de base de datos.</p>
<p><strong>Transformación de relaciones</strong></p>
<p>Según el tipo de correspondencia:</p>
<ul><li><strong>Relaciones M:N</strong>: se transforman en una tabla, cuya clave primaria es la concatenación de los identificadores de las clases asociadas, siendo cada uno de ellos clave ajena de la propia tabla. Si la relación tienen atributos, éstos se transforman en columnas de la tabla.</li>
<li><strong>Relaciones 1:N</strong>: existen varias posibilidades:
<ul><li>Propagar el identificador de la clase de cardinalidad máxima <em>1</em> a la que es <em>N</em>, teniendo en cuenta que:
<ul><li>Si la relación es de asociación, la clave propagada es clave ajena en la tabla a la que se ha propagado.</li>
<li>Si la relación es de dependencia, la clave primaria de la tabla correspondiente a la clase débil está formada por la concatenación de los identificadores de ambas clases.</li>
</ul></li>
<li>La relación se transforma en una tabla de clave primaria sólo el identificador de la clase de cardinalidad máxima <em>N</em> si:
<ul><li>La relación tiene atributos propios y se desea que aparezcan como tales.</li>
<li>Se piensa que en un futuro la relación puede convertirse en <em>M:N</em>.</li>
<li>El número de ocurrencias relacionadas de la clase que propaga su clave es muy pequeño (y por tanto pueden existir muchos valores nulos).</li>
</ul></li>
<li>Al igual que en el caso de relaciones <em>M:N</em>, las claves propagadas son claves ajenas de la nueva tabla creada.</li>
</ul></li>
<li><strong>Relaciones 1:1</strong>: es un caso particular de las <em>1:N</em> y se puede tanto crear una tabla o propagar la clave, si bien, en este último caso, la clave se propaga en las dos direcciones. Para decidir qué solución adoptar, se debe analizar la situación, intentando recoger la mayor semántica posible, y evitar valores nulos.<br/>
Las relaciones de agregación se transforman del mismo modo que las <em>1:N</em>.</li>
</ul><p><strong>Transformación de relaciones exclusivas</strong></p>
<p>Después de haber realizado la transformación según las relaciones <em>1:N</em>, se debe tener en cuenta que si se han propagado los atributos de las clases, convirtiéndose en claves ajenas de la tabla que provenía de la clase común a las relaciones, hay que comprobar que una y sólo una de esas claves es nula en cada ocurrencia. En caso de no propagarse las claves, estas comprobaciones se deben hacer en las tablas resultantes de transformar las relaciones.</p>
<p><strong>Transformación de la herencia</strong></p>
<p>Existen varias posibilidades que deben ser evaluadas por el diseñador a fin de elegir la que mejor se ajuste a los requisitos. Las opciones para tratar la transformación de la herencia son:</p>
<ul><li><strong>Opción a</strong>: Consiste en crear una tabla para la superclase que tenga de clave primaria el identificador y una tabla para cada una de las subclases que tengan el identificador de la superclase como clave ajena.<br/>
Esta solución es apropiada cuando las subclases tienen muchos atributos distintos, y se quieren conservar los atributos comunes en una tabla. También se deben implantar las restricciones y/o aserciones adecuadas. Es la solución que mejor conserva la semántica.</li>
<li><strong>Opción b</strong>: Se crea una tabla para cada subclase, los atributos comunes aparecen en todas las subclases y la clave primaria para cada tabla es el identificador de la superclase.<br/>
Esta opción mejora la eficiencia en los accesos a todos los atributos de una subclase (los heredados y los específicos).</li>
<li><strong>Opción c</strong>: Agrupar en una tabla todos los atributos de la clase y sus subclases. La clave primaria de esta tabla es el identificador de la clase. Se añade un atributo que indique a qué subclase pertenece cada ocurrencia (el atributo discriminante de la jerarquía).<br/>
Esta solución puede aplicarse cuando las subclases se diferencien en pocos atributos y las relaciones que asocian a las subclases con otras clases, sean las mismas. Para el caso de que la jerarquía sea total, el atributo discriminante no podrá tomar valor nulo (ya que toda ocurrencia pertenece a alguna subclase).</li>
</ul><h2>Técnicas Matriciales</h2>
<p>Las técnicas matriciales tienen como objetivo representar las relaciones existentes entre distintos tipos de entidades, objetos o cualquier otro elemento del sistema.</p>
<p>Se utilizan, principalmente, para analizar la consistencia entre los modelos generados durante el desarrollo, comprobar la trazabilidad con los requisitos especificados por el usuario, etc.</p>
<h3>Descripción</h3>
<p>Las técnicas matriciales son útiles para representar las relaciones entre elementos comunes de los distintos modelos, tales como entidades/procesos, procesos/diálogos, datos/localización geográfica, y asegurar que los modelos son coherentes entre sí.</p>
<p>Las siguientes son algunas de las matrices empleadas en&nbsp; MÉTRICA Versión 3:</p>
<ul><li>Procesos/localización geográfica: permite representar la localización geográfica de los procesos de una organización.</li>
<li>Almacenes de datos/entidades del modelo lógico de datos normalizado: establece las relaciones existentes entre los almacenes de datos y las entidades, y permite verificar que cada almacén de datos definido en el modelo de procesos se corresponde con una o varias entidades del modelo lógico de datos normalizado.</li>
<li>Atributos de interfaz/atributos de entidades del modelo lógico de datos normalizado: permite verificar que los atributos que aparecen en cada diálogo de la interfaz de usuario forman parte del modelo lógico de datos normalizado.</li>
<li>Entidades/procesos: permite representar el tratamiento lógico de los procesos sobre los datos del sistema y verificar que cada entidad del modelo lógico de datos normalizado es accedida por algún proceso primitivo representado en el DFD.</li>
<li>Diálogos/procesos: permite representar los diálogos asociados a un proceso interactivo y verificar que cada proceso interactivo tiene asociado al menos un diálogo.</li>
<li>Objetos Diagrama de interacción / clases, atributos al modelo de clases: permite verificar que cada mensaje entre objetos se corresponde con un método de una clase.</li>
<li>Mensajes Diagrama de interacción / métodos, atributos del modelo de clases: permite verificar que una clase tiene capacidad para proporcionar los datos que se soliciten en los mensajes que recibe.</li>
<li>Evento, acción, actividad de clases / métodos de clases: permite verificar que todo evento, actividad o acción de una clase se corresponde con un método de esa clase.</li>
<li>Clases/elementos del modelo físico de datos: permite verificar que cada elemento del modelo físico de datos se corresponde con un elemento del modelo de clases.</li>
<li>Dependencias entre subsistemas/subsistemas: permite representar para cada subsistema, los subsistemas que dependen de él.</li>
<li>Esquemas físicos de datos / nodos: permite representar la localización física de los datos en los nodos de la arquitectura del sistema, así como verificar que cada esquema del modelo físico de datos está asociado con un nodo del particionamiento físico del sistema de información.</li>
</ul><h3>Notación</h3>
<p>Dados dos tipos de elementos A y B, su representación será una matriz bidimensional NxM, siendo N el número de elementos de A, y M el número de elementos de B.</p>
<p>En el cruce de una fila y una columna (C), se tendrá el modo en que se relacionan un elemento concreto de A y uno de B.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/notacion_matriz.png?w=825"/></p>
<h2>Bibliografia</h2>
<ul><li><a href="https://eclap.jcyl.es/web/jcyl/ECLAP/es/Plantilla66y33/1259395037582/_/_/_" rel="noopener" target="_blank">Junta de Castilla y León (SOP_INF_T09_FINAL)</a></li>
<li><a href="https://administracionelectronica.gob.es/pae_Home/pae_Documentacion/pae_Metodolog/pae_Metrica_v3.html#.WtYfDnpuZpg" rel="noopener" target="_blank">PAe</a></li>
</ul> </article>

# Diseño de bases de datos.La arquitectura ANSI/SPARC. El modelo lógico relacional. Normalización. Diseño lógico. Diseño físico. Problemas de concurrencia de acceso. Mecanismos de resolución de conflictos.

<article><h2>Introducción</h2>
<p>El diseño lógico es la etapa del proceso de diseño de una BD en la que se obtiene la representación de la estructura de la BD en términos de almacenamiento (tablas). La obtención de esta estructura implica la aplicación de unas reglas de transformación de los elementos previamente existentes en el modelo conceptual de la BD, reglas que se van a describir en este tema.</p>
<p>Por su parte, el diseño físico es la etapa que incluye las acciones de configuración y ajuste del almacenamiento físico y de la seguridad de la BD. El diseño físico es una tarea compleja y dependiente del SGBD utilizados y del uso concreto que se pretenda hacer de la BD diseñada, por lo que en este tema se van a describir la problemática general que se aborda en esta etapa y los criterios de toma de decisiones en esas etapas para resolver un problema.</p>
<p>Finalmente, el tema describirá la necesidad del uso concurrente de las BD y los conflictos que ese uso plantea, así como los mecanismos que los SGBD utilizan para resolverlos.</p>
<h2>Diseño Lógico</h2>
<p>El diseño lógico es la etapa de creación de la BD en la que se va a traducir el modelo conceptual obtenido en la etapa de diseño conceptual en modelo lógico y un esquema lógico expresado de un modo comprensible para un SGBD. Si consideramos que el SGBD es relacional, es esquema lógico estará expresado en tablas y columnas (o relaciones y atributos).</p>
<p>El diseño lógico se puede dividir en dos etapas:</p>
<ul><li><strong>Diseño lógico estándar</strong>: En esta etapa se obtiene un modelo lógico estándar y un esquema lógico estándar, independientes del SGBD comercial en el que se vaya a implementar la BD. El modelo lógico estándar puede expresarse empleando varias técnicas, entre las que cabe citar el Diagrama de Estructura de Datos (DED) y el modelo relacional. El esquema lógico estándar se obtiene utilizando un Lenguaje de Definición de Datos (DDL) estándar, habitualmente el SQL-92 (que es el estándar ISO).</li>
<li><strong>Diseño lógico específico</strong>: Utilizando el esquema lógico estándar que se ha obtenido, se estudia su implementación en un SGBD comercial (Oracle, DB2, Sybase, etc). Para ello, habrá de analizarse la compatibilidad del modelo lógico estándr con el modelo lógico específico del SGBD elegido, y proponer un modo de solucionar aquellos aspectos del modelo lógico estándar que no recoge el modelo lógico específico. Una vez realizada esa tarea, se obtiene un esquema lógico específico usando el Lenguaje de Definición de Datos propio del SGBD (normalmente, será un lenguaje SQL con algunas peculiaridades propias de cada SGBD). A la etapa del diseño lógico específico también se la conoce como etapa de implementación de la BD.</li>
</ul><h3>Diseño lógico estándar</h3>
<p>Tal y como se ha comentado en el punto anterior, el diseño lógico estándar consiste en convertir el modelo conceptual de BD en un esquema lógico estándar, independiente del SGBD que se vaya a utilizar. El esquema lógico estándar será la expresión del modelo lógico estándar utilizando un Lenguaje de Definición de Datos independiente del SGBD (SQL habitualmente).</p>
<p>Las técnicas de modelado conceptual son diferentes de las técnicas de modelado lógico, por lo que habrá que convertir cada elemento presente en el modelo conceptual en elementos expresables en la técnica de modelado lógico que hayamos seleccionado.</p>
<p>En las BD relacionales, es habitual usar el modelo E/R para el modelado conceptual y el modelo relacional para el modelado lógico. En este apartado vamos a estudiar la conversión de los elementos del E/R al modelo relacional.</p>
<p><strong>Transformación de dominios</strong></p>
<p>Un dominio del modelo E/R se transforma en un dominio en el modelo relacional utilizando la sentencia SQL:</p>
<pre>CREATE DOMAIN</pre>
<p><strong>Transformación de entidades</strong></p>
<p>Cada entidad del modelo E/R se transformará en una tabla (relación) en el modelo relacional. La tabla tendrá el mismo nombre que la entidad de la que proviene. Vemos un ejemplo a continuación y una entidad de un modelo E/R (conceptual).</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/entidad_er.png?w=825"/></p>
<p>Transformando la entidad al modelo relacional, obtendremos lo siguiente:</p>
<pre>EMPRESA (CIF, Nombre, Dirección)</pre>
<p>Para obtener el esquema lógico estándar, la tabla se definirá usando la sentencia SQL CREATE TABLE.</p>
<pre>CREATE TABLE EMPRESA (
     CIF         Código_CIF,
     Nombre      Nombres,
     Dirección   Direccines,
     PRIMARY KEY (CIF)
)</pre>
<p><strong>Transformación de atributos</strong></p>
<p>Cada atributo de una entidad se transformará en una columna de la tabla (relación) del modelo relacional. Los atributos de las entidades pueden ser de cuatro tipos:</p>
<ul><li><strong>Identificadores</strong>: Se transforman en una columna que es la clave primaria de la tabla. En SQL, la condición de clave primaria se representará colocando la cláusula PRIMARY KEY al lado del nombre de la columna en la que se ha convertido el atributo (dentro de la sentencia CREATE TABLE con la que se crea la tabla en la que está incluida la columna).</li>
<li><strong>Identificadores alternativos</strong>: Se transforman en una columna a la que se le añade la restricción UNIQUE, lo cual significa que no puede haber valores repetidos en esa columna.</li>
<li><strong>Atributos no identificadores</strong>: Se transforman en una columna de la tabla.</li>
<li><strong>Atributos multivaluados</strong>: En el modelo relacional una instancia de una relación sólo toma un valor para cada atributo. Por ello, será obligatorio crear una nueva tabla que contenga a la clave primaria de la tabla anterior y al atributo multivaluado, siendo la clave primaria de la nueva tabla la concatenación de los dos atributos y marcándose la clave primaria de la tabla anterior como clave foránea en la nueva tabla.</li>
</ul><p><strong>Transformación de interrelaciones</strong></p>
<p>En el modelo relacional, la única unidad de modelado son las tablas, por lo que las interrelaciones del modelo E/R deben transformarse en tablas del modelo relacional (se produce una cierta pérdida de semántica).</p>
<p>El modo de transformar las interrelaciones en tablas depende del tipo de interrelación considerada. Los tipos de transformaciones existentes son:</p>
<p><strong>Transformación de interrelaciones N:M</strong></p>
<p>Una interrelación N:M se va a convertir en una tabla del modelo relacional. La nueva tabla tendrá como columnas a la concatenación de los atributos identificadores de las entidades que estaban unidas por la interrelación.</p>
<p>Una interrelación en el modelo E/R:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/interrelacic3b3n.png?w=825"/></p>
<pre>EMPRESA (CIF, Dirección, ...)
VENDE (CIF, Codigo_producto)
PRODUCTO (Codigo_producto, ...)</pre>
<p>Si la interrelación tiene atributos en el modelo E/R, cada atributo de la interrelación pasará a ser una columna de la nueva tabla.</p>
<p>Los atributos identificadores de las entidades unidas mediante la interrelación serán claves primarias en las tablas del modelo relacional que representen a sus entidades. Por tanto, esos mismos atributos serán considerados claves foráneas en la tabla que representa a la interrelación.</p>
<p>La condición de calve ajena de una columna se expresará mediante la cláusula FOREIGN KEY en SQL.</p>
<pre>CREATE TABLE VENDE (
     CIF         Codigo_CIF,
     Producto    Codigo_Producto,
     ...,
     PRIMARY KEY (Codigo_CIF, Codigo_Producto),
     FOREIGN KEY (Codigo_CIF) REFERENCES Empresa,
     FOREIGN KEY (Codigo_Producto) REFERENCES Producto
)</pre>
<p>Las cardinalidades mínimas de cada entidad participante en la interrelación se van a expresas en el esquema lógico estándar usando la sentencia de SQL.</p>
<pre>CREATE ASSERTION</pre>
<p><strong>Transformación de interrelaciones 1:N</strong></p>
<p>Las relaciones 1:N se pueden transformar de dos maneras:</p>
<ul><li>No crear ninguna tabla que represente a la interrelación y añadir a la tabla que representa a la entidad con cardinalidad n el conjunto de atributos que son clave primaria de la entidad con cardinalidad 1. Este es el modo habitual de realizar la transformación.</li>
<li>Convirtiendo la interrelación en una tabla, siendo la clave primaria de la tabla el conjunto de atributos identificadores del lado n de la relación. Esta opción se utiliza en los siguientes casos:
<ul><li>Cuando se cree que en un futuro la relación se va a transformar en una de tipo N:M (y por tanto, será necesario tener una tabla que represente a esa relación).</li>
<li>Cuando la interrelación tiene atributos en el modelo relacional.</li>
<li>Cuando la interrelación es optativa para las ocurrencias de las entidades situadas en el lado 1 de la relación (cardinalidad 0:1) y el porcentaje de ocurrencias interrelacionadas es bajo, lo cual va a significar que en las columnas absorbidas en la tabla n van a existir muchos valores nulos.</li>
</ul></li>
</ul><p><strong>Transformación de interrelaciones 1:1</strong></p>
<p>Se realizan del mismo modo que las interrelaciones 1:N, pero teniendo en cuenta que si se decide no crear una tabla que represente a la interrelación, la elección de la tabla a la que se le añaden los atributos del otro extremo es optativa, si bien se suele seguir el siguiente criterio:</p>
<ul><li>Si una de las dos entidades de la interrelación tiene cardinalidad (0,1) y la otra entidad tiene cardinalidad (1,1), entonces se propagan los atributos identificadores de la tabla (1,1) a la tabla (0,1), evitándose los valores nulos.</li>
<li>Si las dos tablas tienen cardinalidad (1,1), se puede escoger cualquiera de los dos extremos para propagar la clave. En este caso, la elección puede depender de criterios como las frecuencias de acceso a las tablas.</li>
<li>Si los dos extremos participan con una cardinalidad (0,1), crear una tabla que represente a la interrelación. El identificador de la tabla podrá ser el identificador de cualquiera de los dos extremos, y los atributos que sean clave primaria en uno de los dos extremos, serán clave foránea en la nueva tabla.</li>
</ul><p><strong>Transformación de interrelaciones con un grado superior a 2</strong></p>
<p>El mecanismo de transformación es igual al de las tablas N:M, se crea una tabla que representa a la relación, y su clave primaria será la concatenación de los atributos identificadores de todas las entidades a las que interrelaciona (lógicamente, tres o más).</p>
<p><strong>Transformación de interrelaciones de dependencia y existencia</strong></p>
<p>El modelo relacional no distingue tipos de relaciones, por lo que las interrelaciones de dependencia y existencia se han de convertir en relaciones del mismo modo que las interrelaciones 1:N. Habitualmente, se propaga la clave de la tabla que representa a la entidad débil a la tabla que representa al entidad fuerte.</p>
<p><strong>Transformación de restricciones de entidades o atributos</strong></p>
<p>En el modelo E/R pueden estar expresadas restricciones de usuario. Estas restricciones se recogen en el esquema lógico estándar del siguiente modo:</p>
<ul><li>Si la restricción indica un rango de valores, se usa la cláusula BETWEEN.</li>
<li>Si la restricción implica que un determinado atributo o conjunto de atributos sólo puede tomar un valor de entre los pertenecientes a una lista, se emplea la cláusula IN.</li>
<li>Si la restricción es de otro tipo, se puede utilizar la sentencia CHECK para comprobar el cumplimiento de la condición fijada, o la sentencia CREATE ASSERTION si la restricción afecta a más de una tabla.</li>
</ul><pre>CREATE TABLE Decreto
(
     Num_Decreto         Numeros_Decreto,
     Fecha_Aprobacion    Fecha,
     Fecha_Publicacion   Fecha,
     ...,
     CHECK (Fecha_Aprobacion &lt; Fecha_Publicacion)
)</pre>
<p><strong>Transformación de dependencias de identificación y existencia</strong></p>
<p>La transformación de estas dependencias se realizarán del mismo modo que el de las relaciones 1:M, es decir, no escribiendo ninguna relación que las represente y propagando la clave de la tabla que representa a la entidad fuerte de la tabla que representa a la entidad débil, en la cual jugará el papel de clave foránea.</p>
<p>Para dicha clave foránea, no se admitirán los valores nulos, y se añadirá la condición de borrado y modificación en cascada (la eliminación o modificación de una ocurrencia de la entidad fuerte obligará a la eliminación o modificación de las ocurrencias de las entidades débiles que tiene asociadas).</p>
<p>Si la dependencia es en identificación, entonces la clave primaria de la tabla que representa a la entidad débil se formará mediante la concatenación de la clave primaria de la entidad débil y de la clave propagada que proviene de la entidad fuerte.</p>
<p><strong>Transformación de restricciones en las interrelaciones</strong></p>
<p>Se utilizarán los mismos mecanismos que se han comentado para la transformación de restricciones de las entidades o de sus atributos (usando las condiciones CHECK o CREATE ASSERTION si la restricción afecta una interrelación o a varias).</p>
<p><strong>Transformación de generalizaciones (Relaciones ISA)</strong></p>
<p>Hay tres estrategias para llevar a cabo esta transformación:</p>
<ul><li>Transformar la entidad y sus subtipos en una sola tabla, la cual tendrá como atributos la concatenación de los atributos de la entidad y de los subtipos. En el ejemplo:</li>
</ul><pre>EMPLEADO_PUBLICO (DNI, Nombre, Relacion_laboral, Inicio_contrato, Toma_posesion)</pre>
<ul><li>Crear una tabla para la entidad generalizadora y una tabla por cada subtipo. Cada tabla tendrá como atributos los de su entidad o subtipo correspondiente. Ésta es la opción que mejor mantiene la semántica del modelo E/R. En el ejemplo:</li>
</ul><pre>EMPLEADO_PUBLICO (DNI, Nombre)
INTERINO (DNI, Inicio_Contrato)
FUNCIONARIO (DNI, Toma_Posesion)</pre>
<ul><li>Crear una tabla para cada subtipo. Cada tabla tendrá como columnas los atributos del subtipo al que representa y los atributos comunes (los que posee la entidad generalizadora). En el ejemplo:</li>
</ul><pre>INTERINO (DNI, Nombre, Inicio_Contrato)
FUNCIONARIO (DNI, Nombre, Toma_Posesion)</pre>
<p>Mostramos la figura de una relación ISA en el modelo E/R:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/relacion_isa.png?w=825"/></p>
<p><strong>Transformación de la dimensión temporal</strong></p>
<p>Se distinguen dos casos:</p>
<ul><li>Si la dimensión temporal aparece en el modelo E/R como una entidad, se transformará del mismo modo que el resto de las entidades.</li>
<li>Si la dimensión temporal aparece en forma de atributos de una interrelación, estos atributos se ubicarán en la tabla que les corresponda al transformar la interrelación (bien en la tabla de la interrelación o bien en la tabla hacia la que se hayan propagado claves). Ahora bien, debe considerarse que estos atributos de tipo fecha pueden tener que formar parte de la clave primaria de la tabla en la que se ubiquen en función de la semántica de la situación que se representa.</li>
</ul><p><strong>Transformación de atributos derivados</strong></p>
<p>Los atributos derivados se transformarán en columnas de la entidad a la que pertenezcan (como el resto de los atributos). Además, se establecerá un disparador o un procedimiento almacenado que calcule el valor del atributo cada vez que se inserta una nueva fila en la tabla o cada vez que se modifique en una fila el valor de alguno de los atributos a partir de los cuales se calcula el atributo derivado.</p>
<p><strong>Normalización del esquema obtenido</strong></p>
<p>Finalizada la transformación del esquema conceptual en un esquema lógico, debe aplicarse a dicho esquema lógico un proceso de normalización, evitándose así las anomalías de inserción, modificación y borrado que provoca la redundancia.</p>
<h3>Diseño lógico específico</h3>
<p>Partiendo del esquema lógico obtenido en el apartado anterior, se elabora un esquema adaptado al sistema gestor de BD que se va a utilizar, creándose las tablas del esquema utilizando el Lenguaje de Definición de Datos propio del cada sistema. En las BDR, el Lenguaje de Definición de Datos (LMD) es el SQL, si bien existen pequeñas variaciones entre el SQL usado en cada sistema, que normalmente incluye pequeñas modificaciones o extensiones del lenguaje SQL (que es el estándar ISO).</p>
<p>En el paso del modelo lógico estándar al modelo lógico específico de cada SGBD puede encontrarse que el modelo lógico específico soporta todos los conceptos del modelo lógico estándar (del modelo relacional) o, por el contrario, que existen determinados aspectos del modelo lógico estándar que el modelo lógico específico no soporta. En este último caso, habrá que realizar un trabajo complementario de adaptación (bien añadiendo programación complementaria en el diccionario de datos del SGBD o bien haciendo que la puesta en práctica de esas restricciones no soportadas por el modelo lógico del SGBD, la lleve a cabo el código de los programas que utilicen los datos de la BD).</p>
<p>Algunos de los aspectos del modelo lógico estándar que pueden tener que adaptarse son los siguientes:</p>
<ul><li><strong>Dominios</strong>: El DDL del SGBD puede no incluir ninguna sentencia que nos permita crear dominios (los únicos dominios que reconoce automáticamente son los asociados a los tipos de datos predefinidos en el propio SGBD). En este caso, habrá que elegir una de las dos opciones siguientes:
<ul><li>Cuando se especifique la columna (dentro de la sentencia CREATE TABLE), escoger el tipo de datos predefinido que mejor se ajuste, fijar la longitud y añadir alguna restricción CHECK.</li>
<li>Crear una tabla de dominio, que contendrá una sola columna, y en la que cada fila será uno de los valores posibles del dominio. Una vez creada esta tabla, crear un procedimiento almacenado que comprueba que los valores que se intentan insertar en la columna son compatibles con el dominio que queremos establecer. La tabla de dominio será estática, es decir, sólo podrá ser modificada por el administrador de la BD. Lógicamente, la opción de construir una tabla de dominio sólo será validad si el dominio a construir es finito.</li>
</ul></li>
<li><strong>Clave Primaria</strong>: Si el SGBD no incluye una cláusula PRIMARY KEY, debe conservarse la semántica dando los siguientes pasos:
<ul><li>Añadir la restricción NOT NULL en los atributos que formen parte de la clave primaria (debe recordarse que una clave primaria no admite valores nulos).</li>
<li>Añadir la restricción UNIQUE al conjunto de atributos de la clave primaria (ya que una clave primaria no admite valores repetidos).</li>
<li>Añadir a la tabla un índice construido sobre las columnas que forman parte de la clave primaria. Este índice se debe crear al crear la tabla y se debe destruir cuando la tabla sea eliminada.</li>
<li>Documentar el esquema con un comentario que indique cuál es la clave primaria.</li>
</ul></li>
<li><strong>Clave ajena</strong>: Si el SGBD no incluye una cláusula FOREIGN KEY, debe conservarse la semántica dando los siguientes pasos:
<ul><li>Añadir la restricción NOT NULL en los atributos de la clave ajena que no admitan nulos (cuando la cardinalidad mínima de la interrelación original fuera de al menos uno).</li>
<li>Hacer que los programas que trabajen con la BD implementen las restricciones de clave ajena (integridad referencial).</li>
<li>Documentar el esquema con un comentario que indique que una columna o conjunto de columnas son clave ajena.</li>
</ul></li>
</ul><p>El resto de los aspectos del modelo lógico estándar no recogidos por el modelo lógico específico del SGBD suelen modelarse empleando procedimientos almacenados o triggers.</p>
<p>Finalizada la etapa del diseño lógico específico, habremos creado un esquema lógico específico en el SGBD. Esto quiere decir que ya tendremos una BD operativa en la que se podrán insertar, eliminar o modificar datos y sobre la cual podremos realizar consultas.</p>
<h2>Diseño Físico</h2>
<p>El diseño físico es la última etapa del proceso de creación de una BD. El objetivo de esta fase es obtener un esquema interno de la BD que cumpla lo mejor posible los objetivos de funcionamiento de la BD que los usuarios esperan. Más concretamente, se trata de:</p>
<ul><li>Disminuir el tiempo de respuesta de la BD (tanto el tiempo medio como la respuesta ante los picos de carga)</li>
<li>Disminuir el espacio de almacenamiento utilizado</li>
<li>Incrementar la Seguridad de la BD</li>
</ul><p>Estos objetivos del diseño físico no siempre son compatibles entre sí. Por ejemplo, para reducir el tiempo de respuesta de las consultas a una BD, puede ser necesario incrementar la redundancia de los datos (tener los mismos datos almacenados en varias tablas a la vez). Obviamente, esto incrementará el espacio de almacenamiento utilizado. Un buen diseño físico debe tener en cuenta para cada BD las necesidades de uso, establecer unos objetivos concretos, y, cuando estos objetivos sean contradictorios, priorizarlos y alcanzar un nivel de compromiso aceptable entre ellos.</p>
<p>Para llevar a cabo esta etapa, es preciso contar con información precisa sobre muchos aspectos de la BD que se va a crear y de la plataforma en la que se va a trabajar. El diseño físico comienza a realizarse cuando se ha recopilado información suficiente sobre:</p>
<ul><li>Los recursos software de los que se dispone</li>
<li>Los recursos hardware de los que se dispone</li>
<li>El esquema lógico específico de la BD</li>
<li>Políticas de seguridad de los datos</li>
<li>Estudio detallado de las aplicaciones que va a utilizar la BD y de las transacciones que van a generar.</li>
</ul><p>El nivel físico de las BD no está estandarizado, por lo que la realización del diseño físico es dependiente del SGBD que se esté utilizando. Cada SGBD relacional definirá su propia estructura de archivos, índices, buffers de memoria, roles de seguridad y objetos de gestión del nivel físico, manipulándose este nivel a través de una extensión del lenguaje SQL estándar específica de cada sistema gestor.</p>
<p>De los dicho en los párrafos anteriores se pueden extraer las siguientes conclusiones:</p>
<p>Al contrario que en el diseño lógico general, el enfoque del diseño físico no puede ser formal, sino casuístico, adaptado a cada SGBD y a cada BD utilizados. No hay recetas universalmente válidas, sino “buenas ideas” (heurísticas) asentadas en conceptos de almacenamiento, arquitectura de computadores, redes o algoritmia. Al no haber una estandarización del nivel físico, esas ideas deben ser puestas en práctica en cada caso concreto, probadas, evaluadas y, si es necesario, refinadas hasta alcanzar la situación final deseada. A este proceso de mejora del diseño físico se le conoce como ajuste de la BD o tunning.</p>
<p>Por último, es preciso comentar que no todos los SGBD tienen el mismo grado de flexibilidad en su nivel físico. En función del grado de manejo que permitan para el diseño físico, podemos distinguir tres tipos de SGBD:</p>
<ul><li><strong>Rígidos</strong>: El SGBD fija una estructura interna que apenas admite configuración. Esto asegura la independencia físico/lógica de la BD, pero es poco adaptable a cada situación concreta, lo que puede suponer una pérdida de eficiencia.</li>
<li><strong>Flexibles</strong>: El SGBD permite que sea el Administrador de BD el que diseñe toda la estructura interna. El diseño de toda la estructura interna es un trabajo extenso y complejo, y la toma de decisiones del administrador puede afectar a la independencia físico/lógica de los datos. Sin embargo, también es el enfoque más adaptable a cada necesidad concreta, con lo que es la alternativa con la que se podría obtener un mayor grado de eficiencia en el uso de la BD.</li>
<li><strong>Semiflexibles</strong>: El SGBD proporciona una estructura inicial configurable a través de un conjunto de parámetros. La modificación de estos parámetros por parte del Administrador de BD permite ir mejorando esa estructura interna, y por ende, el rendimiento de la BD. Ésta opción ofrece un buen compromiso entre eficiencia e independencia físico/lógica, siendo habitual en los SGBD.</li>
</ul><h3>Metodología de trabajo para la obtención del diseño físico</h3>
<p>Podemos dividir la etapa del diseño físico en tres fases:</p>
<ul><li>Diseño de la representación física.
<ul><li>Análisis de las transacciones.</li>
<li>Selección del modo de almacenamiento en memoria secundaria.</li>
<li>Creación de índices secundarios.</li>
<li>Realización de Agrupamientos de tablas.</li>
<li>Realización de procesos de desnormalización.</li>
<li>Estimación de la necesidad de espacio en disco.</li>
</ul></li>
<li>Diseñar los mecanismos de seguridad.
<ul><li>Diseñar las vistas de los usuarios.</li>
<li>Diseñar las reglas de acceso.</li>
</ul></li>
<li>Monitorizar y ajustar el sistema.</li>
</ul><p><strong>Análisis de las transacciones</strong></p>
<p>Para realizar un buen diseño físico es necesario conocer las consultas y las transacciones que se van a ejecutar sobre la BD. Esto incluye tanto información cualitativa, como cuantitativa. Para cada transacción, hay que especificar:</p>
<ul><li>La frecuencia con que se va a ejecutar.</li>
<li>Las relaciones y los atributos a los que accede la transacción, y el tipo de acceso: consulta, inserción, modificación o eliminación. Los atributos que se modifican no son buenos candidatos para construir estructuras de acero.</li>
<li>Los atributos que se utilizan en los predicados WHERE de las sentencias SQL. Estos atributos pueden ser candidatos para construir estructuras de acceso dependiendo del tipo de predicado que se utilice.</li>
<li>Si es una consulta, los atributos involucrados en el join de dos o más relaciones. Estos atributos pueden ser candidatos para construir estructuras de acceso.</li>
<li>Las restricciones temporales impuestas sobre la transacción. Los atributos utilizados en los predicados de la transacción pueden ser candidatos para construir estructuras de acceso.</li>
</ul><p><strong>Selección de la organización del almacenamiento en memoria secundaria</strong></p>
<p>Las BD van a almacenar la información en dispositivos de almacenamiento secundarios (discos o cintas), los cuales se caracterizan por tener mayor capacidad que la memoria principal y por la no volatilidad de los datos. Sin embargo, son mucho más lentos que la memoria principal a la hora de recuperar información, por lo que es preciso realizar un estudio detallado sobre el modo de organizar la información en ellos, de modo que consigamos un rendimiento en tiempo de acceso ajustado a cada necesidad de uso de la BD.</p>
<p>Las alternativas de organización consisten básicamente en la elección del tipo de fichero o estructura de datos más adecuado para cada caso. En este apartado nos limitaremos a estudiar las ventajas y las desventajas de las más habituales, pero sin entrar en una descripción detallada de esas estructuras.</p>
<p><strong>Ficheros secuenciales</strong></p>
<p>Organizados de tal manera que cada registro es adyacente al siguiente registro. Esta relación de adyacencia puede ser física (direcciones físicas consecutivas) o lógica (haciendo que cada registro contenga un puntero al siguiente registro).</p>
<p>Los ficheros secuenciales no permiten el acceso directo a los datos, por lo que el acceso a los registros se realiza en el mismo orden en el que fueron introducidos en el fichero.</p>
<p><strong>Ficheros secuenciales indexados ISAM</strong></p>
<p>Es una estructura de fichero indexado en el que los registros se agrupan en bloques, y en el interior de dichos bloques están organizados secuencialmente.</p>
<p>El índice que se crea sobre el fichero contiene apuntadores a las direcciones de inicio de cada bloque, y el acceso a datos a través del índice se realiza de la siguiente manera:</p>
<ol><li>Se localiza el índice de la clave que cumpla la condición de búsqueda.</li>
<li>Se accede al bloque apuntado por el nodo que contenía a la clave anterior.</li>
<li>Una vez dentro del bloque, el registro deseado se busca secuencialmente.</li>
</ol><p>La organización de ficheros ISAM mantiene el equilibrio entre el tamaño de los índices y el tiempo de acceso a los registros.</p>
<p>Como el tamaño de los bloques está limitado, en estos ficheros hay una zona de desbordamiento en que se van a almacenar los registros que no se pueden guardar en el bloque que les corresponde cuando éste ya está lleno.</p>
<p>El uso de la zona de desbordamiento disminuye el rendimiento del sistema, puesto que se accede a ella tras buscar al registro en el bloque en el que le correspondería estar, y porque la búsqueda en la zona de desbordamiento es secuencial. Cuando el área de desbordamiento es muy grande, se reorganiza el fichero, realizándose una nueva división de bloques, ubicando a todos los registros en los bloques y reorganizando el índice de apuntadores a bloques.</p>
<p><strong>Árboles-B</strong></p>
<p>Estructura de indexación en forma de árbol equilibrado. El hecho de ser equilibrados (misma altura en todas sus ramas) permite minimizar el número de accesos a disco cuando se realiza una búsqueda: las búsquedas rápidas son una característica que distingue a los árboles-B.</p>
<p>En cuanto al almacenamiento, los árboles-B consiguen una gestión del espacio razonablemente buena, ya que si el árbol es de orden n, cada nodo debe tener al menos n/2 claves (es decir, como mucho se desaprovecha la mitad del espacio de almacenamiento del índice, lo cual es fácilmente asumible con los recursos de almacenamiento de que se dispone hoy en día).</p>
<p><strong>Ficheros de acceso aleatorio empleando técnicas de Hashing</strong></p>
<p>En estos ficheros se accede directamente a los registros mediante el valor de su clave (siendo la clave uno o más de los campos del registro). Para ello, se dispone de una función “hash” o de mapeado que permite calcular la dirección del registro a partir del valor de la clave. Este sistema es el que más rápido permite realizar una búsqueda de un registro concreto, pero sólo funciona para resolver consultas exactas (con todo el valor de la clave). Si la búsqueda es por rango o por patrón (por ejemplo, LIKE ‘%a’), no se puede aplicar la función hash.</p>
<p><strong>Criterios de elección entre las estructuras</strong></p>
<p>La elección de una estructura de organización dependerá del uso que se realice de los datos almacenados. La siguiente table recoge las situaciones en las que se suele preferir cada estructura:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/criterio_organizacion.png?w=825"/></p>
<p>La elección entre un fichero ISAM y un árbol-B se realiza considerando los siguientes factores:</p>
<ul><li>Frecuencia de las actualizaciones de los datos: Si la frecuencia de las actualizaciones es alta, debe elegirse un árbol-B, ya que los ficheros ISAM se irán degradando al irse añadiendo registros a la zona de desbordamiento.</li>
<li>Elevado número de consultas recurrentes: Si se realizan muchas consultas simultáneas sobre los datos indexados, el fichero ISAM debe ser la estructura elegida, ya que al ser su índice estático, no se bloquea (facilita el acceso concurrente).</li>
<li>Si se deben tener en cuenta los dos factores o no se conoce bien el entorno de explotación de la BD (existen dudas sobre el número de usuarios, la frecuencia de acceso a datos, etc), la estructura elegida será el árbol-B, ya que es la más adaptable de las dos y sus aspectos desfavorables respecto a los ficheros ISAM tienen poca repercusión en el funcionamiento del sistema.</li>
</ul><p><strong>Creación de los índices secundarios</strong></p>
<p>Las BD relacionales indexan a cada tabla por su clave primaria, creándose automáticamente el índice de clave primaria en el mismo momento en el que se crea la tabla. Sin embargo, es frecuente añadir índices adicionales a las tablas, para que hagan más rápidas las consultas que se realizan sobre determinados campos de esas tablas.</p>
<p>La introducción de un índice secundario en una tabla repercute negativamente en los tiempos de ejecución de la inserción o eliminación de registros, y supone un incremento del espacio de almacenamiento necesario para la tabla. El administrador de BD debe ponderar en cada caso las pérdidas y ganancias de introducción de un nuevo índice, para así determinar si su creación es interesante. Algunas situaciones que hacen interesante la indexación son:</p>
<ul><li>Atributos de la relación a los que se accede con mucha frecuencia.</li>
<li>Claves foráneas de la relación sobre las que es habitual realizar joins.</li>
</ul><p>Algunas situaciones que desaconsejan la introducción de índices secundarios son:</p>
<ul><li>Tablas con pocas filas: el recorrido secuencial de las tablas sería muy breve, y la reducción del tiempo de acceso obtenida de la introducción del índice es muy escasa.</li>
<li>Atributos cuyo valor se modifica muy a menudo: Los índices utilizan como clave de búsqueda los valores de los atributos indexados. Si la modificación de esos valores es muy frecuente, habrá que reconstruir el índice cada poco tiempo, lo cual puede suponer un coste elevado si la tabla tiene muchas filas.</li>
<li>Atributos con valores poco selectivos: Los atributos en los que es muy habitual la repetición de su valor en distintas filas de la tabla no son buenos candidatos para la indexación. Después de recorrer el índice y localizar su clave de búsqueda, tendríamos todavía muchos registros con el mismo valor de clave, y habría que recorrer secuencialmente esos registros para encontrar el que se busca; en este caso, la introducción del índice no supondría ningún beneficio importante desde el punto de vista del tiempo de acceso. Por ejemplo, si tenemos una tabla de personas y deseamos buscar una persona en concreto, no tiene sentido indexar por un campo ‘Sexo’, ya que aproximadamente la mitad de los registros de la tabla tendrían el valor ‘hombre’ y la otra mitad el valor ‘mujer’.</li>
</ul><p><strong>Realización de agrupamientos de tablas (clustering)</strong></p>
<p>El clustering o agrupación de tablas es una técnica consistente en almacenar un grupo de tablas en una misma área de memoria secundaria. De este modo, los accesos simultáneos a las tablas agrupadas no obligan al SGBD a la búsqueda de los datos en zonas lejanas del almacenamiento secundario, lo que reduce el tiempo de resolución de esos accesos.</p>
<p>El clustering será una técnica a considerar si esos accesos simultáneos son frecuentes.</p>
<p><strong>Realización de procesos de desnormalización</strong></p>
<p>El proceso de desnormalización consiste en introducir redundancias en un esquema lógico previamente normalizado (típicamente en 3FN o en FN de Boyce-Codd). Aunque ésta es una decisión de nivel lógico, se suele tomar por motivos de eficiencia de la BD (repetir datos en varias tablas evita navegar entre ellas para encontrarlos), es decir, la decisión viene motivada por cuestiones de implementación.</p>
<p>La desnormalización ralentiza las actualizaciones de datos, hace perder flexibilidad al esquema lógico (puede afectarnos si decidimos añadir nuevas tablas, por ejemplo) y complica la implementación de la BD y su documentación. Por tanto, es una alternativa que sólo se debe utilizar cuando el resto de las técnicas de diseño físico no nos proporcionan un rendimiento de las consultas de la BD que sea aceptable.</p>
<p>Entre las acciones de desnormalización que se&nbsp; pueden realizar, se pueden destacar:</p>
<ul><li>Introducir atributos derivados: Los atributos derivados son aquellos cuyo valor se puede obtener realizando un conjunto de operaciones sobre atributos ya existentes en la BD. La introducción de un atributo derivado ayuda a obtener ese valor rápidamente en una consulta, puesto que no hay que realizar las acciones de cálculo del mismo, pero incrementa los costes de almacenamiento y de actualización de las tuplas de la BD (cada vez que se modifique el valor de un atributo que interviene en su cálculo, habrá que recalcular el valor del atributo derivado).</li>
<li>Fusionar tablas involucradas en relaciones uno a uno: Si el acceso conjunto a ambas tablas es muy habitual, puede ser interesante crear una nueva tabla cuyos atributos sean la concatenación de los atributos de las dos tablas, lo cual puede reducir su tiempo de acceso. Sin embargo, este cambio perjudicará a las operaciones join que se realicen entre cualquiera de esas dos tablas y una tercera, ya que las filas de la nueva tabla que se han de leer ocuparán más en memoria (la tabla fusionada tiene más campos), por lo que se recuperarán menos registros en cada lectura, lo cual obligará a un número de accesos a disco superior.</li>
<li>Introducir atributos duplicados en relaciones 1:N: Consiste en añadir atributos no clave de la tabla con cardinalidad 1 en la tabla con cardinalidad N. Así, cuando se realiza una operación de join entre las dos tablas que sólo involucra a los atributos duplicados, no será necesario recorrer la tabla con cardinalidad 1.</li>
</ul><p><strong>Determinación del espacio de almacenamiento necesario</strong></p>
<p>Una vez obtenido el esquema de implementación definitivo, el administrador de la BD debe determinar el espacio de almacenamiento necesario para la BD. La cantidad de espacio que se determine será una estimación basada en el estudio de la cantidad de datos ya existente y que hay que cargar en la BD y en las estimaciones de crecimiento futuro de la BD.</p>
<p>La estimación del espacio puede verse afectada también por el nivel de seguridad que se desee para el almacenamiento de datos y por el grado de disponibilidad de la BD. Por ejemplo, si uno de los requisitos de la BD es que su disponibilidad sea 24×7 (24 horas al día, 7 días a la semana), es posible que se necesite usar una estructura de almacenamiento secundario en forma de RAID 1+0 o 0+1, lo que duplicaría el espacio de almacenamiento necesario para la BD.</p>
<h3>Diseño de los mecanismos de seguridad de los datos</h3>
<p><strong>Creación de las vistas de los usuarios</strong></p>
<p>Las vistas son un elemento de la BD que permiten a los usuarios ver los datos de una determinada forma (corresponden al nivel externo en la arquitectura ANSI/SPARC). El uso de las vistas permite:</p>
<ul><li>Reducir la complejidad del esquema lógico global, manteniendo un esquema único para todos los usuarios y adaptando ese esquema a las necesidades que tenga cada tipo de usuario.</li>
<li>Mejorar el nivel de seguridad de la BD, ya que los usuarios no verán más datos de las tablas que aquellos que están incluidos en la vista.</li>
</ul><p><strong>Fijar las reglas de acceso de los usuarios</strong></p>
<p>En esta fase, se establecen los perfiles de usuario, donde cada perfil es el conjunto de acciones que cada tipo de usuario va a poder hacer sobre cada elemento o conjunto de elementos de la BD (tablas, filas, unidades lógicas de almacenamiento, etc.)</p>
<h3>Monitorización y ajuste del sistema</h3>
<p>El diseño físico no se debe concebir como un proceso secuencial que finaliza cuando se ha encontrado una configuración válida. Las BD pueden sufrir variaciones a lo largo del tiempo, tanto en su tamaño, como en su esquema&nbsp; lógico global o en el uso que se desee hacer de ellas, lo que obligará a una monitorización continua de su rendimiento (para comprobar si se va degradando) y a la introducción de ajustes que permitan adaptarse a los cambios sufridos por la BD o solventar las pérdidas de eficiencia que se hayan producido.</p>
<p>Cada proceso de ajuste supone en cierta medida una reconstrucción del diseño físico que se haya realizado, por lo cual esta etapa de diseño volvería a comenzar de nuevo.</p>
<h2>La gestión de la concurrencia</h2>
<p>Veamos la gestión de la concurrencia en los SGBD. Para ello, empezaremos introduciendo la necesidad de dicha gestión y el concepto de transacción, pasando posteriormente a abordar los problemas que plantea la concurrencia (Lectura Fantasma, Lectura Sucia, etc.) y los mecanismos de resolución existentes.</p>
<h3>Necesidad de gestión de la concurrencia</h3>
<p>Los SGBD deben poder mantener la integridad de los datos que almacenan. Durante la vida de una BD, existen secuencias de acciones de escritura y lectura que pueden originar que la BD quede en un estado inconsistente si no se ejecutan todas las acciones de esa secuencia.</p>
<p>Para evitar este tipo de problemas, los SGBD utilizan las transacciones, que son unidades lógicas de proceso que se componen de una secuencia de acciones cuya ejecución es atómica, o se ejecutan todas o no se ejecuta ninguna. En un punto intermedio de una transacción, el estado del BD puede ser inconsistente, siendo siempre consistente al principio y al final de la transacción.</p>
<p>El elemento del SGBD encargado de conseguir este objetivo es el Gestor de Transacciones (transaction manager), el cual gestiona las peticiones de los usuarios en forma de transacciones.</p>
<p>Además, los SGBD que existen en la actualidad ofrecen la posibilidad de ser usados en modo multiusuario, lo que implica que múltiples usuarios pueden trabajar a la vez con el sistema como si fuera un recurso dedicado, sin apercibirse de la presencia de otros usuarios. Para lograr este efecto, los tiempos de respuesta del SGBD a todos los usuarios deben ser reducidos, lo que obliga a realizar una ejecución concurrente (simultánea) de las transacciones de cada usuario.</p>
<p>La ejecución atómica que caracteriza a las transacciones no garantiza que las pertenecientes a un programa de un usuario no puedan interferir en las transacciones que pertenecen a otros programas y que se están ejecutando al mismo tiempo. Conseguir que las transacciones no interfieran con el funcionamiento de otras transacciones se conoce como aislamiento de la transacción (isolation), y el conjunto de problemas que plantea conseguir ese aislamiento en un entorno multiusuario es conocido como el problema de la gestión de la concurrencia.</p>
<p>Además, durante el transcurso de una transacción, pueden producirse problemas en el SGBD que no permitan que la transacción concluya con éxito, lo que, en virtud del principio de “todo o nada” que acompaña a las transacciones, obliga al SGBD a estar preparado para deshacer las acciones que una transacción no concluida ha realizado sobre una BD. Es el problema de la recuperación y se gestiona añadiendo una nueva propiedad a las transacciones, que es la persistencia, y que consiste en que las modificaciones de datos que se realizan durante una transacción no se almacenan en la BD hasta que la transacción ha finalizado con éxito.</p>
<p>Resumiendo, una transacción ha de tener las siguientes propiedades:</p>
<ul><li><strong>Atomicidad</strong>: Las acciones de una transacción se ejecutan todas o ninguna.</li>
<li><strong>Consistencia</strong>: La BD se encuentra en un estado consistente antes de la ejecución de la transacción y debe estar en un estado consistente cuando la transacción termine.</li>
<li><strong>Aislamiento</strong>: La ejecución de una transacción no debe interferir en la ejecución de otras transacciones, la transacción debe ejecutarse como si estuviera aislada.</li>
<li><strong>Persistencia</strong>: Los efectos de una transacción no son permanentes en la BD hasta que la transacción ha finalizado con éxito.</li>
</ul><h3>Manejo de transacciones en el SGBD</h3>
<p>El gestor de transacciones es el componente funcional del SGBD que planifica y controla la ejecución de transacciones concurrentes en un BD.</p>
<p>Un gestor de transacciones se puede dividir conceptualmente en los siguientes elementos:</p>
<ul><li>Un contenedor de entrada: Al que llegan las transacciones que se deben ejecutar.</li>
<li>Un planificador (scheduler): Que determina el orden en el que las transacciones de la cola van a ser ejecutadas. Cuando el planificador da paso a una transacción, ésta es enviada al gestor de datos, desde el cual se realizarán las operaciones de la transacción sobre la BD.</li>
<li>Un contenedor de salida: Al que llega la transacción cuando ha terminado de ejecutarse. Si la transacción ha finalizado correctamente, el gestor de transacciones realizará una operación commit, haciendo las modificaciones de la transacción persistentes en la BD.</li>
</ul><p>Si la transacción no ha finalizado correctamente debido a algún problema, el gestor de transacciones ejecuta una operación abort y envía la transacción a un gestor de recuperación, el cual deshace las operaciones de la transacción y devuelve los datos al estado en que estaban antes de iniciarse la transacción. La transacción abortada será devuelta al contenedor de salida para volver a ser ejecutada.</p>
<p>Con el fin de incrementar el rendimiento de las BD en un entorno multiusuario, las transacciones no se ejecutan secuencialmente una detrás de otra. El modelo de ejecución secuencial de las transacciones podría originar una situación en la que un programa corto se quedase bloqueado a la espera de la finalización de un programa largo.</p>
<p>En este caso, el usuario del programa debería sufrir un gran tiempo de espera para la realización de un conjunto reducido de operaciones, con lo que no percibiría a la BD como un recurso dedicado.</p>
<p>Para evitar estas situaciones, las transacciones se despachan concurrentemente, es decir, sus acciones se van a llevar a cabo de forma entrelazada. Sin embargo, el entrelazado de acciones de las transacciones puede originar conflictos, algunos de los cuales van a ser comentados en el punto siguiente.</p>
<p>La siguiente figura representa a un gestor de transacciones:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/gestor_transacciones.png?w=825"/></p>
<h3>Problemas de la concurrencia</h3>
<p><strong>El problema de la actualización perdida</strong></p>
<p>Problema de concurrencia que ocurre cuando:</p>
<p>Dos transacciones T1 y T2 trabajan en paralelo e intentan modificar el valor del mismo objeto de la BD. Ambas transacciones leen el valor del objeto antes de que la otra lo actualice.</p>
<p>En este caso, cada una de las transacciones modificará el valor del objeto en memoria y tratará posteriormente de escribirlo en la BD. El valor que se almacenará en la BD será el que tiene el objeto en la transacción que escriba más tarde, ya que el valor que ha escrito la primera transacción se sobrescribirá. Así, la actualización realizada por la transacción que ha escrito primero quedará sin efecto.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/actualizacion_perdida.png?w=825"/></p>
<p><strong>El problema de la lectura sucia</strong></p>
<p>Se produce cuando:</p>
<p>Una transacción T1 lee un valor de un objeto que ha sido modificado por otra transacción T2 y que todavía no se ha hecho persistente en la BD.</p>
<p>La transacción T2, que había modificado los datos no termina correctamente. En este caso, la transacción T1 está trabajando con un valor que es inconsistente.</p>
<p>Debe recordarse que los datos pueden encontrarse en un estado inconsistente en el transcurso de una transacción, por lo que la transacción primera puede haber leído dichos datos inconsistentes, utilizándolos para completar su secuencia de acciones.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/lectura_sucia.png?w=825"/></p>
<p><strong>El problema de la lectura fantasma o lectura no repetible</strong></p>
<p>Puede aparecer cuando:</p>
<p>Una transacción T1 está leyendo un conjunto de datos al tiempo que una transacción T2 los está modificando.</p>
<p>La transacción T1 lee algunos de los datos antes de que sean modificados por T2 y otros después de ser modificados por T2.</p>
<p>El resultado de la operación que realiza T1 se ve afectado por el hecho de combinar datos no actualizados por T2 con datos actualizados por T2.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/lectura_fantasma.png?w=825"/></p>
<p>En este caso, el valor ‘s’ es la agregación de los valores x, y, z. La acción de la transacción T2 no modifica el valor de esa agregación, sin embargo, la lectura de valores con diferentes versiones ha provocado que T1 ofrezca un valor de s que es equivalente a x+y+x-10.</p>
<h3>Mecanismos de resolución de conflictos</h3>
<p>Como ya hemos comentado en el punto anterior, la labor fundamental de un gestor de transacciones es manejar las transacciones que generan los programas de los usuarios de tal modo que se mantenga la consistencia de la BD. En un entorno multiusuario, el gestor de transacciones deberá conseguir mantener la consistencia cuando se ejecutan entrelazadamente las acciones que componen las transacciones de los distintos programas.</p>
<p>Este orden de ejecución lo establece el planificador (scheduler) del gestor de transacciones, llamándose plan de ejecución a cada posible secuencia de ejecución de un conjunto de acciones. Lógicamente, existen múltiples planes de ejecución posibles, siendo interesantes los planes que cumplen la condición de serializabilidad; un plan de ejecución A es serializable para un conjunto de transacciones T si existe un plan de ejecución secuencial A’ que es equivalente a A.</p>
<p>O dicho de un modo menos formal, un plan es serializable si el resultado de la ejecución entrelazada de las acciones de esas transacciones es equivalente al resultado de ejecutar las transacciones en serie.</p>
<p>Sin embargo, la comprobación “a priori” de la serializabilidad de un plan es muy costosa (problema NP-completo), por lo que el gestor de transacción no trata de determinar si un plan de ejecución es serializable; en lugar de eso, el gestor de transacciones emplea diversos mecanismos de ejecución de las acciones que o eliminan los conflictos debidos a la concurrencia o permiten recuperar el estado consistente de la BD cuando se producen.</p>
<p>Podemos considerar los métodos de resolución de conflictos divididos en dos tipos:</p>
<ul><li><strong>Métodos pesimistas</strong>: Basados en la suposición de que los conflictos entre transacciones concurrentes ocurren con alta frecuencia, lo que obliga a realizar una serie de acciones para manejar esos conflictos.</li>
<li><strong>Métodos optimistas</strong>: Basados en la suposición de que los conflictos entre transacciones se producen con escasa frecuencia.</li>
</ul><p><strong>Métodos pesimistas</strong></p>
<p><strong>Concepto de bloqueo y técnicas basadas en bloqueos</strong></p>
<p>Este mecanismo de resolución de conflictos se basa en el concepto de bloqueo, que consiste en que cuando una transacción T1 necesita realizar alguna acción sobre un objeto de la BD, debe solicitar al SGBD una reserva de ese objeto, no pudiendo ejecutar la acción hasta que la reserva no se ha producido. El SGBD sólo concederá esa reserva si otra transacción T2 no mantiene el mismo objeto reservado (en otras palabras, mientras una transacción tenga a un objeto de la BD reservado, el acceso al resto de las transacciones puede considerarse bloqueado).</p>
<p>En un momento dado, bien durante su transcurso o bien a su finalización, la transacción terminará las acciones que necesite hacer sobre el objeto de la BD, deshaciendo la reserva y quedando el objeto disponible para otras transacciones.</p>
<p>Las acciones de bloqueo o desbloqueo no tienen porqué ejecutarse inmediatamente antes y después de la acción durante la cual queremos que el objeto esté bloqueado. En el transcurso de una transacción se hacen múltiples lecturas y escrituras, pudiendo realizarse varias de ellas sobre el mismo objeto. Si se bloquease y desbloquease antes y después de cada acción, se incurrirá en un coste de gestión de los bloqueos muy alto, lo que repercutirá en el rendimiento de la BD (en sus tiempos de respuesta). Por tanto, una política de gestión de bloqueos debe llegar a un buen compromiso entre dos aspectos de signo contrario:</p>
<ul><li>Tiempo que el objeto (los datos) están bloqueados: Cuanto mayor sea, más largo es el tiempo durante el cual otras transacciones no pueden realizar sus acciones sobre el conjunto de datos, lo que supone que han de estar a la espera del desbloqueo, retardándose su finalización.</li>
<li>Tiempo empleado en gestionar los bloqueos: Realizar muchas operaciones de bloqueo/desbloqueo repercute en el rendimiento de la BD, ya que hay que almacenar esos bloqueos, comprobar su compatibilidad, etc.</li>
</ul><p>Así pues, la solución consisten en encontrar la manera de ejecutar un número elevado de acciones entre dos bloqueos, consiguiendo a la vez que la distancia entre bloqueos sea razonablemente pequeña.</p>
<p>Considerando el tipo de acción que se impide, podemos distinguir dos clases de bloqueo:</p>
<ul><li>Bloqueo de escritura (write-lock o wlock): Impide que otras transacciones modifiquen un dato.</li>
<li>Bloqueo de lectura (read-lock o rlock): Impide que otras transacciones lean un dato.</li>
</ul><p>La distinción entre bloqueos de escritura y bloqueos de lectura se establece porque interesa que el gestor de transacciones pueda hacer un manejo diferenciado de cada tipo:</p>
<ul><li>Un bloqueo de lectura realizado por una transacción es compatible con un bloqueo de lectura de otra transacción. Dicho de otro modo, no existe ningún problema porque dos transacciones lean un objeto a la vez (y evitar esperas innecesarias supone incrementar el rendimiento de la BD).</li>
<li>Un bloqueo de escritura es incompatible con cualquier otro tipo de bloqueo, ya que no se puede permitir que una transacción lea un dato cuando otra transacción lo está modificando (como ya vimos en los problemas de la concurrencia) y, desde luego, un objeto no puede ser sobrescrito a la vez.</li>
</ul><p>Así pues, se puede establecer la siguiente tabla de compatibilidades entre bloqueos de lectura y escritura:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/bloqueos.png?w=825"/></p>
<p>Los SGBD también permiten manejar diferentes granularidades de los bloqueos: Un bloqueo sobre distintas clases de objetos de la BD, como por ejemplo, una fila, un conjunto de filas o una tabla. De este modo las transacciones pueden efectuar reservas del tamaño estrictamente necesario, no bloqueando innecesariamente partes de los objetos que pueden ser utilizadas simultáneamente por otras transacciones (ejemplo, una transacción puede necesitar hacer un bloqueo de escritura sobre las primeras n filas de una tabla, lo cual no debe impedir que otras transacciones realicen acciones de lectura o escritura sobre las n+1 restantes).</p>
<p>Cuanto menor sea el tamaño de los objetos bloqueados (granularidad más fina), menor será el número de esperas que los bloqueos originarán. Sin embargo, una granularidad fina genera más situaciones de interbloqueo que una granularidad gruesa, por lo que será necesario hacer una selección cuidados del nivel de granularidad empleado.</p>
<p>EL PROBLEMA DEL INTERBLOQUEO</p>
<p>El uso de técnicas basada en bloqueo para la gestión de transacciones concurrentes pueden conducir al problema denominado interbloqueo (o deadlock o abrazo mortal). El interbloqueo es una situación que se produce cuando dos transacciones se quedan esperando indefinidamente por un recurso que la otra transacción tiene bloqueada, de tal manera que ninguna de las dos accede nunca al recurso que la otra ha reservado.</p>
<p>Por tanto, el gestor de transacciones deberá implantar mecanismos que le permitan detectar esas situaciones de interbloqueo y resolverlas, existiendo tres tipos de estrategias de resolución:</p>
<ul><li>La <strong>predicción</strong>: Consiste en la no generación de transacciones que puedan producir interbloqueo. Esto obligaría a analizar todas las transacciones a priori, lo cual produciría una gran sobrecarga en el sistema (todos los algoritmos de predicción son exponenciales, y por tanto no utilizables en un sistema con altas exigencias de rendimiento como es una BD).</li>
<li>La <strong>prevención</strong>: Basada en que las transacciones puedan renunciar a un bloqueo que hayan realizado previamente. Para ello, se detectan los casos en los que una transacción T1 tenga reservado un ítem y una transacción T2 intenta hacer un tipo de bloqueo sobre ese ítem que es incompatible con el bloqueo de T1, aplicando técnicas de prevención, de entre las que se pueden destacar:
<ul><li>Wait-Die: Si T2 es más antigua, se le hace esperar. En caso contrario, T2 se cancela.</li>
<li>Kill-Wait: Si T2 es más antigua, se cancela. En caso contrario, se hace esperar a T2.</li>
</ul></li>
<li>La <strong>eliminación</strong>: Es el modo más sencillo de los tres. Consiste en eliminar una de las transacciones bloqueadas, continuando la otra transacción su camino. El gestor de transacciones volvería entonces a generar la transacción eliminada y la reintroduciría en la cola de transacciones, siendo lo más probable que la otra transacción haya terminado o haya avanzado hasta un punto en el que no se repita la situación de interbloqueo.</li>
</ul><p>EL PROTOCOLO DE BLOQUEO EN DOS FASES</p>
<p>Es una implementación muy extendida de uno de los principios de la resolución de conflictos basada en bloqueos (técnica pesimista). El protocolo de bloque en dos fases define un conjunto de reglas sobre la aplicación de bloqueos que pueden ser utilizadas por el gestor de transacciones para gestionar las transacciones concurrentes.</p>
<p>Estas reglas son:</p>
<ol><li>En una transacción sólo se va a escribir sobre un objeto una vez.</li>
<li>Si una transacción necesita leer y escribir, realizará en primer lugar el bloqueo de escritura. De esta manera, basta con realizar una única operación de desbloqueo en la transacción (un desbloqueo genérico que termina con el bloqueo de lectura y escritura).</li>
<li>Antes de realizarse las acciones de lectura o escritura, deben hacerse los bloqueos correspondientes, los cuales deben permanecer hasta que las acciones hayan finalizado.</li>
<li>Los bloqueos del mismo tipo sólo se realizan una vez por transacción.</li>
<li>En una transacción, una vez que se hace el primer desbloqueo, no se vuelve a hacer ningún bloqueo sobre ningún objeto. Esta norma caracteriza al bloqueo en dos fases, en la que se distingue una fase de crecimiento, donde van apareciendo nuevos bloqueos, y una fase de decrecimiento, que se inicia a partir del primer desbloqueo y dura hasta el final de la transacción, y en cuyo transcurso el número de bloqueos siempre decrece. Gráficamente, el comportamiento de este protocolo puede representarse así (evolución del número de bloqueos de una transacción con el algoritmo 2PL):</li>
</ol><p><img src="https://gsitic.files.wordpress.com/2018/01/evolucion_numero_bloqueos.png?w=825"/></p>
<p>Entre las ventajas del protocolo de bloqueo en dos fases o 2PL, podemos citar do:</p>
<ul><li>Es un protocolo seguro, es decir, nunca se van a producir las situaciones anómalas de concurrencia estudiadas en el punto anterior.</li>
<li>Es un protocolo sencillo, fácil de implantar.</li>
</ul><p>Entre sus desventajas, podemos citar:</p>
<ul><li>Los bloqueos tienden a ser grandes, lo que va a provocar incompatibilidades habituales con otras transacciones, derivándose de ello una pérdida de rendimiento.</li>
<li>Este protocolo permite la aparición de interbloqueo.</li>
</ul><p><strong>Time-Stamping</strong></p>
<p>El time-stamping trata de conseguir la serializabilidad de los planes de ejecución haciendo que, cuando varias transacciones tengan que acceder a objetos comunes, lo hagan en distintos momentos. Este objetivo se consigue asignando una marca temporal distinta (time-stamp) a cada transacción.</p>
<p>Cuando una transacción intenta acceder a un objeto para leerlo o modificarlo, se comprueba previamente si ya ha sido accedido por otra transacción más joven. Existen tres modalidades de time-stamping:</p>
<p>TIME-STAMPING BÁSICO</p>
<ol><li>Se almacena en cada objeto el time-stamp de la última transacción que lo ha leído (TSR) y el de la última que lo ha grabado (TSW).</li>
<li>Cuando una transacción T intenta leer un objeto, si su time-stamp es mayor o igual que el TSR del objeto, podrá leerlo, debiendo ser cancelada en caso contrario.</li>
<li>Si una transacción T intenta escribir un objeto, se pueden producir las siguientes situaciones:</li>
</ol><pre>TS (T) &gt;= TSW(Objeto):
     Si TS(T) &gt;= TSR(Objeto), podrá escribir.
                              Si no, T tendrá que se cancelada
Si TS(T) &lt;= TSW(Objeto):
     Si TS(T) &gt;= TSR(Objeto), T puede seguir adelante saltándose la
                              grabación, ya que la versión que habría
                              grabado no sería la última y no habrá
                              sido leída por ninguna transacción
                              (regla de escritura de Thomas).
                              En caso contrario, T deberá ser cancelada.</pre>
<p>El time-stamping básico no asegura que se eviten las anomalías de concurrencia, pero si que impide los efectos de las anomalías de la Actualización Perdida y los de la Lectura Sucia (ya que si la transacción no puede hacer un commit, tampoco podrán hacerlo las que hayan leído o escrito los objetos que ella ha actualizado).</p>
<p>TIME-STAMPING DINÁMICO</p>
<p>Consiste en asignar un time-stamp a las transacciones cuando tratan de acceder a un objeto que ha sido leído o actualizado por otra transacción que no ha terminado todavía. De este modo, se evitan algunas de las cancelaciones de transacciones que se producen en el time-stamp básico. Su funcionamiento es el siguiente:</p>
<p>Cuanto T1 intenta leer o actualizar un objeto actualizado por T2 o intenta actualizar un objeto que T2 ya ha leído:</p>
<ol><li>Si T1 y T2 no tienen todavía time-stamp, se les asigna a cada una un time-stamp, cumpliéndose que TS(T1) &gt; TS(T2).</li>
<li>Si una de las dos no tiene time-stamp, se le asigna, respetándose de nuevo que TS(T1) &gt; TS(T2).</li>
<li>Si T1 y T2 tiene ya time-stamp y TS(T1) &gt; TS(T2), entonces continúa normalmente la ejecución de las dos transacciones. En caso contrario, se cancelará la transacción T1.</li>
</ol><p>Al igual que el time-stamping básico, el time-stamping dinámico no asegura que se eviten las anomalías de concurrencia, pero si que impide los efectos de las anomalías de la Actualización Perdida y la Lectura Sucia. Además, es más eficiente que el time-stamping estático, ya que el número de cancelaciones que produce es menor.</p>
<p>TIME-STAMPING MULTIVERSIÓN</p>
<p>Basada en almacenar versiones de los ítems de la BD, permite el acceso simultáneo a un ítem por parte de transacciones diferentes, de forma que los accesos de cada transacción a los ítems que necesita se hace siempre usando versiones consistentes de esos ítems.</p>
<p><strong>Métodos optimistas</strong></p>
<p>Basados en la suposición de que los conflictos entre transacciones se producen con escasa frecuencia. Por tanto, se acepta como válido cualquier plan de ejecución de transacciones, y es tras finalizar la ejecución del plan y antes de realizar el commit (los datos todavía no son persistentes en la BD) cuando se comprueba si se ha producido algún conflicto entre transacciones o se ha incumplido alguna condición de consistencia. Si estos problemas han aparecido, las transacciones afectadas se deshacen (abort) y vuelven a situarse en la entrada del gestor de transacciones para su ejecución.</p>
<p>En los métodos optimistas se puede considerar la ejecución de una transacción dividida en tres fases:</p>
<ul><li><strong>La fase de lectura</strong>: En ella se produce la ejecución de las acciones de la transacción. Todos los objetos de la BD que se necesitan son leídos y escritos de un buffer de memoria local al programa, y por tanto las acciones no afectan al resto de las transacciones en ejecución.</li>
<li><strong>La fase de validación</strong>: Se comprueba si las modificaciones introducidas por la transacción pueden ser hechas persistentes en la BD sin incumplir la condición de serializabilidad de la transacción.</li>
<li><strong>La fase de escritura</strong>: Si la comprobación realizada durante la fase de validación es positiva, las acciones de la transacción se ejecutan sobre la BD. Si la comprobación es negativa, la transacción es abortada.</li>
</ul><p>TÉCNICA OPTIMISTA BÁSICA</p>
<p>La técnica optimista básica determina el conjunto de transacciones que se han validado utilizando una técnica de time-stamping. Durante la fase de validación se analiza si hay algún ítem común y del mismo nivel de granularidad entre el conjunto de ítems leídos por una transacción T1 y el conjunto de ítems que han escrito las transacciones cuyo time-stamp se ha asignado entre el instante de inicio y el instante de finalización de la fase de lectura de la transacción. Si no existe esa coincidencia, se añade un time-stamp a la transacción T1.</p>
<p>Esta técnica exige que haya como mucho una transacción en la fase de validación en cada instante de tiempo, por lo que la fase de validación actúa como cuello de botella del sistema de gestión de transacciones.</p>
<p><strong>Métodos de control de concurrencia basados en la semántica</strong></p>
<p>Son métodos que, además de la sintaxis, utilizan la semántica de las acciones a realizar para determinar si un plan de ejecución es o no serializable. Es decir, no se limitan a comprobar si los accesos de las transacciones son de lectura o escritura, sino que analizan que van a escribir concretamente las acciones de las transacciones y determinan si esas acciones pueden generar un conflicto o no.</p>
<h2 class="bio">Bibliografía</h2>
<ul class="bio"><li><a href="https://es.scribd.com/document/356635763/Ticb2-Diseno-de-Bbdd-II" rel="noopener" target="_blank">Scribd (Ibiza Ales)</a></li>
</ul> </article>

# Tipos abstractos de datos y estructuras de datos. Grafos. Tipos de algoritmos: ordenación y búsqueda. Estrategias de diseño de algoritmos. Organizaciones de ficheros.

<article><h2>Tablas, listas y árboles</h2>
<h3>Tipos abstractos de datos</h3>
<p>Al escribir un programa para resolver un problema, el enfoque tradicional consistía en pasar de la realidad a una implantación en el lenguaje de programación utilizado, lo que conducía, inevitablemente, a que la forma de “ver” los datos estuviera muy influida por la máquina donde se ejecutaba el programa. Con el tiempo y la experiencia acumulada surgió otro enfoque mejor para afrontar esta situación, que consistía en establecer un nivel intermedio, donde se modela lo esencial de la realidad, mediante técnicas de abstracción, sin comprometerse con detalles de implantación. Estas técnicas de abstracción han evolucionado en el sentido de alejar los elementos que aparecen en los sistemas de software de las nociones propias de las máquinas sobre las que se implantan dichos sistemas, aproximándolos a las nociones propias de los dominios en que se presentan las situaciones modeladas.</p>
<p>La principal de estas técnicas está basada en los <strong>Tipos Abstractos de Datos (TAD)</strong>.</p>
<p>Esta técnica está centrada en las abstracciones de datos, consiste en:</p>
<ul><li>Identificar los distintos tipos de datos que intervienen en el sistema y la función principal de dicho sistema.</li>
<li>Caracterizar cada tipo de datos en función de las operaciones que se puedan realizar con los objetos de los distintos tipos (haciendo abstracción de sus representaciones concreta).</li>
<li>Componer el sistema utilizando objetos de los tipos definidos junto con sus operaciones características.</li>
<li>Implantar cada uno de los tipos utilizados.</li>
</ul><p>Estas características son la base conceptual de los TAD. De forma sintetizada, puede decirse que:</p>
<p><em>Un TAD es una estructura algebraica, a saber, un conjunto de objetos estructurados de alguna forma y con ciertas operaciones definidas sobre ellos.</em></p>
<p>Piénsese, por ejemplo, en una calculadora; los elementos que maneja son cantidades numéricas y las operaciones definidas son operaciones aritméticas. Otro ejemplo posible es el TAD matriz matemática; los elementos que maneja son las matrices y las operaciones son las que nos permiten crearlas, sumarlas, invertirlas, etc. Otro tipo de TAD es cualquier tipo de cola de espera: en el autobús, cine, la compra, etc. Los elementos de las colas son las personas y las operaciones más usuales son entrar o salir de la cola, pero no son las únicas. Desde un punto de vista abstracto podemos pensar en operaciones como crear un elemento de la cola, comprobar si la cola está vacía, si está llena, etc.</p>
<p>Es conveniente observar que las operaciones de un TAD son de diferentes clases. Algunos nos deben permitir crear objetos nuevos, otras determinar su estado, construir otros objetos a partir de algunos ya existentes, etc.</p>
<p>Puesto que los TAD deben ser lo más independientes posibles de los detalles de implantación, es obvio que no deben tener ninguna dependencia con respecto al lenguaje de programación elegido para implantarlos. Aun así, ciertos lenguajes no incorporan ciertas estructuras de datos necesarias para implantar algunos tipos de TAD.</p>
<p><strong>El concepto de algoritmo</strong></p>
<p>Un <strong>algoritmo</strong> es <em>un conjunto de pasos o instrucciones que se deben seguir para realizar una determinada tarea</em>.</p>
<p>Estas instrucciones deben cumplir las siguientes características:</p>
<ul><li><strong>FINITUD</strong>: Debe ser <em>un conjunto finito de instrucciones</em> y que se realicen en un <em>tiempo finito</em>.</li>
<li><strong>PRECISIÓN</strong>: Debe indicar el <em>orden de realización de cada instrucción o paso de forma inequívoca</em>.</li>
<li><strong>DEFINICIÓN</strong>: Debe tener un <em>número finito (0 … N) de datos de entrada</em> y un <em>número finito (0 … M) de datos de salida (resultados)</em>. Frente a un mismo conjunto de datos de partida se debe llegar siempre a un mismo conjunto de resultados.</li>
</ul><p>Otra cualidad deseable en un buen algoritmo, aunque no imprescindible para ser considerado como tal, es que sea <em>óptimo</em>, es decir, que sea la forma más fácil y rápida de hacer una determinada tarea, si bien es cierto que en muchas ocasiones facilidad y rapidez son dos cualidades contrapuestas.</p>
<p>De forma gráfica, la siguiente figura engloba las principales características de un algoritmo.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/algoritmo.png?w=825"/></p>
<p><strong>Coste de un algoritmo</strong></p>
<p>Normalmente, si se escribe un programa para resolver un problema, se hace para que éste sea utilizado muchas veces, por lo que resulta conveniente caracterizarlos según su tiempo de ejecución y la calidad de la respuesta. Cuando estudiamos algoritmos es muy importante caracterizar la solución obtenida de cada algoritmo antes de estar seguros de que dos algoritmos son equivalentes (para un mismo valor de entrada dan exactamente el mismo resultado) o son similares (pueden dar resultados diferentes, pero desde el punto de vista del problema que estamos resolviendo somos indiferentes a cualquiera de los resultados).</p>
<p>Por esta razón, uno de los criterios más importantes para seleccionar un algoritmo es evaluar el tiempo que tarda en ejecutarse, que llamaremos <strong>coste del algoritmo</strong> o <strong>tiempo de ejecución</strong>. Para analizar el coste de un algoritmo adoptamos un modelo que nos dice que recursos usados por la implantación del algoritmo son importantes para su desempeño. La complejidad de un algoritmo bajo un modelo computacional es la cantidad de recursos, en tiempo o espacio, que el algoritmo usa para resolver el problema.</p>
<p>Desafortunadamente, por lo general es imposible predecir el comportamiento exacto de un algoritmo, ya que existe la influencia de muchos factores, de aquí que se trate de extraer las características principales de un algoritmo. Así, se definen ciertos parámetros y ciertas medidas que son las más importantes en el análisis y se ignoran detalles relativos a la implantación.</p>
<p>Así, el análisis es una aproximación, no es perfecto, pero lo importante es que se pueden comparar diferentes algoritmos para determinar cuál es mejor para un propósito determinado.</p>
<p>La metodología que generalmente se utiliza para predecir el tiempo de ejecución de algoritmos se basa en el <strong>comportamiento asintótico</strong>, en este método se ignoran los factores constantes y se concentra en el comportamiento del algoritmo cuando el tamaño de la entrada tiende a infinito. Es totalmente análogo al estudio de los límites de una función cuando su variable independiente tienen a infinito, por ejemplo:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/coste_algoritmo.png?w=825"/></p>
<p>De hecho, es muy usual evaluar el coste de un algoritmo como una función matemática del número de entradas del algoritmo (N), siendo un algoritmo de mayor coste que otro cuando para un mismo N la función que expresa el coste da un resultado superior. Así pues, los costes o tiempos de ejecución más usuales de los algoritmos, de menor a mayor, son:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/coste_algoritmo2.png?w=825"/></p>
<p>Por otra parte, conviene considerar dos casos límite, el <strong>mejor caso</strong> y el <strong>peor caso</strong>. Puede ocurrir que al realizar una operación se parta de unos datos iniciales del TAD que hagan que al aplicar el algoritmo éste se ejecute de la manera más rápida posible, y puede ocurrir también lo contrario, encontrarnos con el caso en que se ejecute de la forma más lenta. Por ejemplo, si queremos ordenar unos datos, parece lógico pensar que el mejor caso será cuando los datos ya estén ordenados, y el peor caso cuando ningún dato inicial esté en el orden que tendrá cuando se haya ejecutado la ordenación.</p>
<p>De forma estadística se supone que se parte de un caso medio. Por otra parte, hay algoritmos cuya diferencia de coste entre los casos mejor y peor es muy grande, y otros en los que, debido a la naturaleza del algoritmo, la diferencia es muy pequeña o incluso inexistente.</p>
<p>Si un algoritmo crece de manera proporcional a N, se dice que es de orden N. En general, el tiempo de ejecución es proporcional, esto es, multiplica por una constante a alguno de los costos anteriormente propuestos, además de la suma de algunos términos más pequeños.</p>
<p><strong>Implantación tradicional frente a los TAD</strong></p>
<p>Según Nicklaus Wirth, un programa responde a la ecuación:</p>
<pre>(Ec. 1)&nbsp; &nbsp;Programa = Datos + Algoritmos</pre>
<p>El enfoque tradicional se ciñe bastante bien a esta concepción. En la ecuación de Wirth la parte <em>Algoritmo</em> la podemos expresar como:</p>
<pre>(Ec. 2)&nbsp; &nbsp;Algoritmo = Algoritmo de datos + Algoritmo de control</pre>
<p>Se entiende como <em>Algoritmo de datos</em> a la parte del algoritmo encargada de manipular las estructuras de datos del problema, y <em>Algoritmo de control</em> a la parte restante (la que representa en sí el método de solución del problema, también llamada <em>lógica de negocio</em>, independiente hasta cierto punto de las estructuras de datos seleccionadas).</p>
<p>Con los TAD se identifican ciertas operaciones o partes del algoritmo que manipulan los datos. Además de proporcionar una estructura de datos, por lo que podemos sustituir el sumando “<em>Datos</em>” de la ecuación anterior por el sumando “<em>Estructura de Datos</em>“. De esta forma, podemos entonces escribir:</p>
<pre>(Ec. 3)&nbsp; &nbsp;Programa = Estructura de Datos + Algoritmo de Datos
                     + Algoritmos de Control</pre>
<p>Definiendo:</p>
<pre>(Ec. 4)&nbsp; &nbsp;Implantación del TAD = Estructura de Datos + Algoritmos de Datos</pre>
<p>Se establece la <em>ecuación fundamental</em> que describe el enfoque de desarrollo con Tipos Abstractos de Datos:</p>
<pre><strong>(Ec. 5)&nbsp; &nbsp;Programa = Implantación del TAD + Algoritmo de Control</strong></pre>
<p>A la hora de crear un Tipo Abstracto de Datos, la ecuación a seguir es (Ec. 4), es decir, determinar como es la <strong>estructura de datos</strong> y cuales son los algoritmos de control para manera los datos, en otras palabras, las <strong>operaciones sobre los datos</strong> que se pueden hacer, o interesa hacer, sobre la mencionada estructura de datos.</p>
<p><strong>Operaciones de los TAD</strong></p>
<p>Las operaciones en los TAD pueden servir para crear nuevos objetos abstractos, para obtener información acerca de ellos, y algunas para construir nuevos elementos a partir de otros ya existentes. De esta forma las operaciones las podemos clasificar de esta manera:</p>
<ul><li>Operaciones de CREACIÓN: Se utilizan para definir y/o crear el TAD y sus elementos.</li>
<li>Operaciones de TRANSFORMACIÓN: Se utilizan para realizar algún tipo de transformación en los componentes del TAD. Por ejempo: asignación de valor, ordenaciones, permutaciones, balanceados, etc.</li>
<li>Operaciones de ANÁLISIS: Se utilizan para obtener información concerniente a cualquiera de los componentes del TAD o de su estructura. Por ejemplo: búsquedas, recorridos, obtención de algún dato del TAD (valor de un componente, cantidad de elementos, profundidad, número de niveles, etc.)</li>
</ul><p><strong>Implantación y tipos de TAD</strong></p>
<p>Cuando ya se tiene bien diseñado un Tipo Abstracto de Dato, el siguiente paso es decidir una implantación. Esto supone elegir algunas de las estructuras de datos que nos proporcione el lenguaje de programación utilizado para representar cada uno de los objetos abstractos y, por otro lado, escribir una rutina (Procedimiento o función) en tal lenguaje que simule el funcionamiento de cada una de las operaciones especificadas para el TAD.</p>
<p>La selección de las estructuras de datos determina la complejidad del algoritmo que implanta una operación y su elección es, por esta razón, de gran importancia. Existen estructuras de datos muy dependientes de un lenguaje de programación y debido a esto deben tratar de evitarse cuando el TAD se quiere que sea portable.</p>
<p>Existen muchos tipos de TAD, pero los más utilizados son:</p>
<ul><li>Tablas</li>
<li>Listas</li>
<li>Árboles</li>
</ul><h3>Tablas</h3>
<p>Una <strong>tabla</strong> o <em>matriz</em>, es un TAD que representa una estructura homogénea de datos donde se cumple:</p>
<ul><li>Todos sus c<em>omponentes son del mismo tipo</em>.</li>
<li>Tiene un <em>número predefinido</em> de componentes que no puede variarse en tiempo de ejecución.</li>
<li>Los elementos de la tabla contienen <em>una clave</em> que los identifica de forma unívoca. El conjunto de claves forman un conjunto de <em>índices</em> para localizar los elementos.</li>
<li>Se permite el <em>acceso directo</em> a cualquiera de los elementos de la tabla a través de los índices.</li>
</ul><p>La operación fundamental en el uso de una tabla es <em><strong>localizar la posición</strong></em> de sus elementos con una clave conocida “a priori”. Dicho de otra forma, lo más usual es que se quiera conocer el contenido del i-esimo (índice i) elemento de una tabla. Es menos frecuente la operación inversa, dado un valor saber los índices de los elementos cuyo contenido coincide con el valor dado; aunque también resulta útil en ocasiones esta operación.</p>
<p><strong>Tipos</strong></p>
<p>Recordando la (Ec. 4) de Wirth, desde el punto de vista de la <em>Estructura de Datos</em> de una tabla, la principal característica de su estructura es la <em>dimensión</em>.</p>
<p>Se habla entonces de:</p>
<ul><li>Tabla <strong>Monodimensional</strong>:
<ul><li>Se refiere a tablas de una dimensión con un determinado número (N) de elementos. La declaración de estas tablas responde a la sintaxis genérica:
<ul><li>
<pre>Nombre_Tabla = matriz[1..N] de Tipo_Elemento;</pre>
</li>
</ul></li>
</ul></li>
<li>Tabla <strong>Multidimensional</strong>:
<ul><li>Se refiere a tablas de más de una dimensión (d), con un determinado número de elementos para cada dimensión (N1, N2, …, Nd). Su declaración es:
<ul><li>
<pre>Nombre_Tabla = matriz[1..N1, ... 2..Nd] de Tipo_Elemento;</pre>
</li>
</ul></li>
</ul></li>
</ul><p>Aunque cada dimensión puede tener diferente número de elementos, todas las dimensiones tienen el mismo tipo de elemento, no pudiéndose declarar diferentes tipos de elementos según las diferentes dimensiones de la matriz, pues supondría violar la primera característica de las tablas.</p>
<p><strong>Operaciones</strong></p>
<p>Desde el punto de las <em>operaciones</em> (Algoritmo de Datos), las operaciones básicas en una tabla son:</p>
<ul><li><strong>Definir/Crear</strong> la tabla: Se refiere a la forma que cada lenguaje debe tener para definir la estructura de una tabla y crear una variable del tipo de la tabla definida.</li>
<li><strong>Insertar/Eliminar</strong> elementos de la tabla: Aunque cuando se define una tabla se indica “a priori” el número de elementos que tiene, eso no quiere decir que desde el principio esos elementos tengan un valor significativo para el uso que se les piensa dar. Es muy común al crear una tabla asignar a todos sus elementos un valor especial (nulo) que indique que en caso de que el elemento tenga ese valor, a todos los efectos, desde un punto de vista abstracto, es como si ese elemento no existiese.</li>
<li><strong>Buscar</strong> elementos de la tabla: Esta operación es fundamental en el uso de tablas. Existen distintas formas de hacer búsquedas en una tabla, y según los valores de los componentes y el tipo de búsqueda ésta será más o menos eficiente (rápida).</li>
<li><strong>Ordenar</strong> los elementos de la tabla: Esta operación resulta muy útil a la hora de realizar búsqueda. Veremos más adelante que resulta mucho más efectivo realizar búsquedas sobre tablas donde se ha establecido algún tipo de orden sobre otras donde no lo hay.</li>
<li><strong>Contar</strong> los elementos de la tabla: Calcular el número de elementos que hay en la tabla en un momento dado. La acción de preguntar si una tabla está llena o vacía (de elementos significativos) son casos particulares de la operación de contar. También pueden considerarse recuentos más especializados, como contar el número de elementos con un determinado valor, o con valor superior a uno dado, etc.</li>
</ul><p>Hay varios algoritmos que implantan las operaciones de búsqueda y ordenación en una tabla (las más complejas y utilizadas). Las operaciones de definición, creación y recuento resultan muy sencillas de implantar.</p>
<p><strong>Representación</strong></p>
<p>La forma más simple de representación abstracta de una tabla es:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/representacion_tbla.png?w=825"/></p>
<p>Para índices que van desde 0 a (N-1) y siendo ei el contenido del elemento i de la tabla.</p>
<p>Es muy común la siguiente representación, más intuitiva, de una tabla:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/representacion_tabla2.png?w=825"/></p>
<p>En la figura anterior se representa una tabla de una dimensión con N elementos, cuyos índices van desde 0 hasta (N-1), y cuyo contenido se refiere a nombres de persona. Para representar tablas multidimensionales, basta con utilizar una representación como la indicada para cada dimensión de la tabla.</p>
<p><strong>Implantación</strong></p>
<p>Puesto que una de las características de las tablas es la invariabilidad del número de componentes, prácticamente todos los lenguajes de programación implantan las tablas usando memoria estática (en oposición a la memoria dinámica). Una vez que el programa ha sido preparado para ser ejecutado (compilado y enlazado), la posición y el espacio de memoria que utilizará la tabla en la ejecución del programa ya está fijado y no puede de ninguna forma cambiarse o utilizarse para otros fines que no sea almacenar los elementos de la tabla.</p>
<p>Hay otros tipos de TAD cuya implantación se realiza frecuentemente con memoria dinámica, cuyo significado fundamental es que, en oposición a la memoria estática, el tamaño y la posición del espacio de memoria utilizado si puede cambiar en tiempo de ejecución, pudiéndose utilizar para otros fines.</p>
<h3>Listas</h3>
<p>Una <strong>lista</strong> es una estructura de datos que cumple:</p>
<ul><li>Todos sus <em>componente son del mismo tipo</em>.</li>
<li>Cada <em>elemento</em> o <em>nodo va seguido de otro</em> del mismo tipo o de ninguno.</li>
<li>Sus componentes se almacenan según <em>cierto orden</em>.</li>
</ul><p>Nótese las diferencias con respecto a las tablas:</p>
<ul><li>Los elementos de las tablas no se almacenan según un orden. En las listas siempre hay un orden.</li>
<li>No existe unos conjuntos de índices asociados a cada posición, tal como ocurre con las tablas. Por tanto, en las listas será precio ir recorriendo los elementos hasta encontrar el buscado.</li>
</ul><p><strong>Tipos</strong></p>
<p>Una manera de clasificar las listas es por la forma de acceder al siguiente elemento:</p>
<ul><li><strong>Lista densa</strong>: La propia estructura determina cuál es el siguiente elemento de la lista. Por ejemplo, aplicando ciertos “trucos” se puede usar una tabla para implementar una lista, de forma que el siguiente elemento de la lista fuera dado por el orden del índice (no confundir con el orden de los elementos del array). Nótese sin embargo que, puesto que un array es estático, la memoria reservada para implementar esta “lista” también será estática.</li>
<li><strong>Lista enlazada</strong>: Cada elemento contiene la información necesaria para llegar al siguiente. La posición del siguiente elemento de la estructura la determina el elemento actual. Es necesario almacenar al menos la posición de memoria del primer elemento. Además es dinámica, es decir, su tamaño cambia durante la ejecución del programa.</li>
<li>Dentro de las listas enlazadas podemos distinguir, según la cantidad de enlaces por nodo, entre:
<ul><li><strong>Lista simplemente enlazada</strong>: Cada elemento conoce qué elemento es el que le sucede en el orden, pero no cual le precede.</li>
<li><strong>Lista doblemente enlazada</strong>: Cada elemento conoce qué elemento le precede y cual le sucede en el orden.</li>
<li><strong>Lista con enlaces múltiples</strong>: Son aquellas listas en donde cada elemento, aparte de conocer los elementos que le preceden o suceden, también tiene uno o varios enlaces al primer elemento de otra lista, siendo éstas sublistas de la anterior.</li>
</ul></li>
</ul><p>También podemos clasificar las listas en función de que los elementos se coloquen en la lista por orden de llegada y se acceda a ellos por su posición. Los ejemplos más usuales de este tipo de listas son:</p>
<ul><li><strong>PILAS</strong> (Estructuras LIFO. Last In First Out): El último elemento en entrar es el primero en salir.</li>
<li><strong>COLAS</strong> (Estructuras FIFO. First In First Out): El primer elemento en entrar es el primero en salir.</li>
</ul><p><strong>Operaciones</strong></p>
<p>Las operaciones básicas a realizar en una lista son las mismas que en las tablas, si bien, la forma en que se realizan en las listas difiere notablemente entre ambos TAD, sobre todo en lo concerniente a las operaciones de Inserción, Eliminación, Búsqueda y Ordenación.</p>
<p>A la hora de insertar o eliminar elementos de una lista, puede distinguirse entre insertar o eliminar el primer elemento de la lista, un elemento intermedio o el último elemento. En todos los casos resulta de capital importancia reordenar los diferentes enlaces entre los elementos de forma correcta, pues realizar mal un enlace o perderlo supone la imposibilidad definitiva de acceder a parte de la lista, o incluso a toda ella.</p>
<p><strong>Representación</strong></p>
<p>La representación más habitual de una lista se hace colocando sus elementos entre paréntesis, separados por comas, según muestra el siguiente ejemplo:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/listas1.png?w=825"/></p>
<p>Siendo e1, e2, …, en los elementos de la lista.</p>
<p>Puesto que los componentes de una lista se almacenan según cierto orden, es muy importante notar que:</p>
<pre>L1 = (e1, e2, ..., en) es una lista distinta de L2 = (en, e1, ..., e2)</pre>
<p>De forma gráfica presentamos las siguientes listas:</p>
<p><em>Simplemente enlazada:</em></p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/lista_simple_enlazada.png?w=825"/></p>
<p><em>Doblemente enlazada:</em></p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/lista_doble_enlazada.png?w=825"/></p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/lista_enlace_multiple.png?w=825"/></p>
<p>En estas representaciones las flechas indican los enlaces entre los componentes de las listas. El punto negro de la flecha indica el elemento origen y la punta de flecha el elemento destino, de tal forma que el origen conoce el destino, pero el destino no conoce su elemento origen. Por esta razón es por lo que las listas doblemente enlazadas precisan “dos” enlaces, uno en cada sentido. En la lista <strong>L1&nbsp;</strong>el elemento de contenido “Juan” sabe que le sigue el elemento “Pedro”, y éste sabe que le sigue “Inés”, pero “Pedro” no sabe que le precede “Juan”.</p>
<p>El símbolo <strong>X</strong> o aspa que aparece en algunos elementos indican que no tienen enlace a ningún sitio, se entiende que es un enlace nulo. Obsérvese que todas las listas tienen que tener un “punto de entrada”, es decir, una referencia al primer elemento de la lista. Estas referencias, en nuestro ejemplo, son <strong>L1, L2 </strong>y<strong> L3</strong>.</p>
<p>También conviene fijarse de forma especial en las listas con enlaces múltiples. Mientras que en las listas simples y dobles únicamente hay una forma de “recorrer” la lista, desde el primer elemento hasta el último”, en las listas con múltiples enlaces surgen varias formas de recorrerlas, según nos decidamos a avanzar por uno de los múltiples enlaces a otras <em>sublistas</em> que puede tener cada elemento.</p>
<p><strong>Implantación</strong></p>
<p>Las listas son un tipo de TAD cuya implantación puede realizarse de múltiples maneras. Según el tamaño, manejo o rendimiento que queramos que tengan ciertas operaciones, como búsquedas, ordenaciones, inserciones, etc, las listas pueden implementarse con arrays, ficheros secuenciales o punteros. Estructuras de datos todas ellas muy comunes en la mayoría de los lenguajes de programación.</p>
<p>También conviene observar que para implantar listas puede usarse tanto memoria estática (arrays) como memoria dinámica (punteros). Si bien es poco frecuente usar los arrays, pues en esencia son tablas. Para implementar una lista simple usando tablas hace falta recurrir a algún tipo de “truco”, por ejemplo, almacenar en el contenido de los elementos del array dos datos, el contenido de los elementos de la lista y el “puntero” al siguiente elemento.</p>
<p>Veamos un ejemplo de lista implementada con array:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/listas2.png?w=825"/></p>
<p>Nótese como junto al nombre de las personas, usamos el carácter especial (#) para separar los nombres de los valores numéricos que hacen de puntero, indicando qué índice de la tabla contiene el siguiente elemento de la lista. Para indicar el valor nulo usamos un valor de índice imposible, en este caso el negativo (-1). Hay que sobreentender que el puntero de comienzo de la lista es siempre el índice cero del array.</p>
<p>Si se eliminasen algunos elementos de la lsita, por ejemplo a Inés y a Pedro, supondría reorganizar los apuntadores, de forma que tendríamos: Juan#3, Inés#(-1); Pedro#(-1); Ana#(-1). Desde un punto de vista abstracto la lista sólo tiene ahora dos elementos Juan y Ana, sin embargo esto no quiere decir que el array haya disminuido su tamaño al dejar de apuntar a los elementos Inés y Pedro; simplemente estamos diciendo que hemos dejado de apuntarlos, pero el array sigue teniendo el mismo espacio reservado en memoria, y este espacio no está disponible para otro uso más que para almacenar los elementos del array. Esto es debido a que un array se implementa con memoria estática.</p>
<p>Usando memoria dinámica (punteros) no se tendría esta desventaja. Bajo esta circunstancia, si se elimina de la lista un elemento, el espacio de memoria que ocupaba queda disponible para ser usado para otras finalidades.</p>
<h3>Árboles</h3>
<p>Como dice David Harel en su libro “The Spirit of Computing”:</p>
<p>“Una de las estructuras de datos más importantes y prominentes que existen es el <strong>árbol</strong>. No es un árbol en el sentido botánico de la palabra, sino uno de naturaleza más abstracta. Todos hemos visto usar tales árboles para describir conexiones familiares. Los dos tipos más comunes de árboles familiares son el – árbol de antecesores – , que empieza en un individuo y va hacia atrás a través de padres, abuelos, etc, y el – árbol de descendientes – , que va hacia adelante a través de hijos, nietos, etc”.</p>
<p>Un árbol es un TAD cuya estructura corresponde con el siguiente gráfico:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/arbol.png?w=825"/></p>
<p>En donde podemos ya notar las principales características de los árboles. Cada uno de las diferentes “circunferencias” representa un elemento o nodo del TAD tipo árbol. El nodo 1 suele ser llamada <em>nodo de nivel 0</em> (también nodo raíz por su similitud con un árbol real). Es importante percatarse de que sólo puede haber un nodo de nivel 0 en cada árbol.</p>
<p>Los nodos 2, 3 y 4 son llamados nodos de nivel 1, por estar todos ellos al mismo “nivel” al ser todos “hijos” del nodo 1. Este razonamiento se puede ir aplicando a los sucesivos niveles, hablándose de nodos nietos (o hijos si nos referimos al nivel inmediatamente superior).</p>
<p>Por la similitud con un árbol en el sentido botánico, también se dice que los nodos que no tienen hijos son nodos hoja y los nodos que sí tienen hijos, salvo la raíz, son llamados nodos rama o nodos internos. Con el ejemplo del árbol anterior (<strong>A1</strong>), vamos a mostrar los principales conceptos usados al hablar de árboles:</p>
<ul><li><strong>Antecesor Directo</strong> o <strong>Padre</strong>: El nodo 4 es el Antecesor Directo o Padre de los nodos 7, 8 y 9.</li>
<li><strong>Antecesor</strong> o <strong>Ancestro</strong>: El nodo 1 es el Antecesor de todos los otros nodos.</li>
<li><strong>Sucesor Directo</strong> o <strong>Hijo</strong>: El nodo 5 es el Sucesor Directo o Hijo del nodo 2.</li>
<li><strong>Sucesor</strong> o <strong>Descendiente</strong>: Todos los nodos son Sucesores o Descendientes del nodo 1.</li>
<li><strong>Nodo de Nivel Cero</strong> o <strong>Raíz</strong>: En nuestro ejemplo es el nodo 1.</li>
<li><strong>Nodo Interno</strong> o Rama: En nuestro ejemplo son los nodos 2, 3 y 4.</li>
<li><strong>Nodo Hoja</strong>: En nuestro ejemplo son los nodos 5, 6, 7, 8 y 9.</li>
<li><strong>Nivel de un Nodo</strong>: El nodo 1 tiene nivel 0. Los nodos 2, 3 y 4 nivel 1. Los nodos 5, 6, 7, 8 y 9 nivel 2.</li>
<li><strong>Grado de un Nodo</strong>: Es el número de descendientes directos que tiene un nodo. El grado del nodo 2 es 1.</li>
<li><strong>Grado del Árbol</strong>: Es el mayor de los grados de los nodos que los componen. En nuestro caso es 3.</li>
<li><strong>Altura del Árbol</strong>: Es el mayor de los niveles del árbol. En nuestro caso es 2.</li>
<li><strong>Longitud de Camino de un Nodo</strong>: Número de enlaces o arcos que hay que atravesar para ir de la raíz a un nodo. La longitud de camino del nodo raíz es la unidad. Por ejemplo, el nodo 5 tiene longitud de camino 3.</li>
</ul><p><strong>Tipos</strong></p>
<p>En función de la estructura que define un árbol, se pueden establecer distintos tipos de árboles atendiendo a ciertos aspectos en la <em>forma</em> de árbol. Según ésto es muy corriente hablar de los siguientes tipos de árboles:</p>
<ul><li><strong>Árbol BINARIO</strong> o <strong>Árbol B</strong>: Es el árbol cuyo máximo número de nodos hijos que tiene cualquier nodo es dos.</li>
</ul><p><img src="https://gsitic.files.wordpress.com/2018/01/arbol2.png?w=825"/></p>
<ul><li><strong>Árbol MULTIRAMA</strong>: Son aquellos en los que no hoy límite para el número de nodos hijo. El número de niveles no crece tanto como en los binarios. Es el caso de nuestro árbol de ejemplo <strong>A1</strong>.</li>
<li><strong>Árbol BALANCEADO</strong>: Son aquellos árboles en los cuales se cumple que <em>entre todos sus nodos hoja no hay una diferencia de nivel superior a la unidad</em>. Veamos algunos ejemplos de árboles binarios balanceados (también denominados árboles AVL) y no-balanceados.</li>
</ul><p>Balanceados:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/arbol3.png?w=825"/></p>
<p>No Balanceados:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/arbol4.png?w=825"/></p>
<p>Es de observar que una lista realmente es un árbol en el que cada nodo únicamente tiene un hijo, y se considera al primer nodo de la lista el nodo raíz del árbol (tal como se muestra en el árbol (3) de la figura.</p>
<p>Una lista de más de dos elementos se corresponde a la estructura de un árbol con un grado de no-balanceo máximo (sólo hay un nodo hoja). Se suele decir en estos casos que la lista es un <em>árbol totalmente degenerado</em>.</p>
<p><strong>Operaciones</strong></p>
<p>Las operaciones básicas que se pueden realizar sobre los árboles son:</p>
<ul><li><strong>Definir/Crear</strong> el árbol: Se refiere a la forma que cada lenguaje debe tener para definir la estructura de tipo árbol y crear una variable de este tipo.</li>
<li><strong>Recorrer</strong> los diferentes caminos del árbol: Esta es una operación que resulta muy importante en los árboles, pues es sobre la que se apoyan las demás operaciones. Vamos a ver que existen dos formas de recorrer un árbol, en ambas, por convenio, se asume que siempre nos desplazaremos de <em>izquierda</em> a <em>derecha</em> en horizontal, al igual que la lectura de un libro. Respecto a la dimensión vertical, nos moveremos de arriba hacia abajo o viceversa. Existen dos forma de recorrer un árbol:
<ul><li>Recorrido en <strong>AMPLITUD</strong>: Se trata de recorrer consecutivamente los nodos que se encuentran en el mismo nivel (siempre de izquierda a derecha). La dimensión que prima en el recorrido es la horizontal. Tomando como ejemplo el árbol <strong>A1</strong> de nuestro ejemplo, el recorrido en amplitud nos daría la siguiente secuencia de nodos: (1, 2,3,4,5,6,7,8,9).</li>
<li>Recorrido en <strong>PROFUNDIDAD</strong>: La dimensión que prima al recorrer el árbol es la <em>vertical</em>. Siempre se tenderá a alejarse del nodo raíz mientras se pueda. Sin embargo, a diferencia del recorrido en amplitud, existen diferentes formas de recorrido en profundidad, estas formas son:
<ul><li>Profundidad en <strong>PREORDEN</strong>: Se empieza por el nodo raíz y se tiende a alejarse lo máximo posible de él. Moviéndose en vertical de arriba hacia abajo. En nuestro ejemplo obtendríamos la secuencia: <em>(1,2,5,3,6,4,7,8,9)</em>.</li>
<li>Profundidad en <strong>POSTORDEN</strong>: Se comienza por el nodo hoja más a la izquierda y se mantiene la máxima distancia que se pueda con el nodo raíz. En nuestro ejemplo se obtiene la secuencia: <em>(5,2,6,3,7,8,9,4,1)</em>.</li>
<li>Profundidad en <strong>INORDEN</strong>: Como el recorrido postorden pero cuidando que no aparezcan, siempre que sea posible, dos nodos del mismo padre (nodos hermanos) de forma consecutiva en la secuencia de recorrido. En nuestro ejemplo se tendría: <em>(5,2,1,6,3,7,4,8,9)</em>. Para los árboles binarios, en este tipo de recorrido, jamás pueden aparecer consecutivos dos nodos hermanos.</li>
</ul></li>
</ul></li>
<li><strong>Insertar/Eliminar</strong> elementos en el árbol: Al igual que en las listas, hay que distinguir entre insertar el nodo raíz, un nodo interno o un nodo hoja. También resulta muy importante nunca cambiar de forma incorrecta o perder un enlace, pues supondría la imposibilidad de acceder a parte o a todo el árbol.</li>
<li><strong>Ordenar</strong> los elementos del árbol: Ordenar un árbol no implica cambiar su estructura, sino modificar el contenido de los nodos para que sigan algún tipo de orden deseado. Las posibles ordenaciones de un árbol son aquellas que hacen que al hacer el recorrido de un árbol se obtenga una secuencia ordenada según algún criterio. Por ejemplo, nuestro árbol de ejemplo está ordenado en amplitud, pues al hacer un recorrido de este tipo se obtiene la secuencia ordenada <em>(1,2,3,4,5,6,7,8,9)</em>. El mismo árbol ordenado en profundidad preorden sería: <em>(1,2,3,4,5,6,7,8,9)</em>.</li>
</ul><p><img src="https://gsitic.files.wordpress.com/2018/01/arbol6.png?w=825"/></p>
<ul><li><strong>Buscar</strong> elementos en el árbol: Consiste en localizar el/los nodo/s que contiene un dato igual al dato dado como referencia. Es muy importante darse cuenta de que según esté el árbol ordenado o no, si está balanceado o no, y dependiendo del recorrido que se haga, las búsquedas pueden ser más o menos efectivas (rápidas).</li>
<li><strong>Contar</strong> los elementos del árbol: Básicamente consiste en recorrer el árbol en cualquiera de sus formas e ir contando los elementos. Existen sin embargo variantes de esta contabilidad. Por ejemplo, podría solicitarse el número de nodos que tiene el nivel N de un árbol, lo cual exigiría un recorrido en amplitud teniendo en cuenta siempre el nivel donde se está en cada momento. Otra posible cuenta sería conocer el número de nodos que hay desde la raíz hasta el nodo hoja de menor nivel, etc.</li>
<li><strong>Balancear</strong> el árbol:&nbsp; Consiste en hacer que un árbol no-balanceado pase a ser balanceado. Esta operación sí que supone un cambio en la estructura del árbol, suponiendo siempre el cambio de nodo raíz y la variación de niveles de ciertos nodos. Veamos un ejemplo de balanceo de un árbol binario:</li>
</ul><p><img src="https://gsitic.files.wordpress.com/2018/01/arbol61.png?w=825"/></p>
<p><strong>Representación</strong></p>
<p>Ya hemos visto una primera forma de representar un árbol muy intuitiva y clarificadora, usando circunferencias para representar los nodos o elementos del árbol y líneas para representar los enlaces.</p>
<p>No obstante, sin tocar en absoluto la estructura del árbol, conviene considerar la forma de enlazar los nodos del árbol, pues al igual que con las listas, los nodos del árbol pueden estar simplemente enlazados o doblemente enlazados. Esta diferencia afecta en la facilidad o dificultad de implementar ciertas operaciones sobre los árboles, sobre todo las diferentes operaciones de recorrido del árbol. Cuando se quiere especificar en un gráfico el tipo de enlaces del árbol, se utiliza una forma parecida a las listas, veamos un ejemplo de un mismo árbol simplemente enlazado y doblemente enlazado.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/arbol7.png?w=825"/></p>
<p><strong>Implantación</strong></p>
<p>Al igual que las listas, con los árboles, según diversas consideraciones sobre el tamaño, manejo o rendimiento que queramos que tengan ciertas operaciones, tales como recorridos, ordenaciones, inserciones, etc. los árboles pueden implantarse con arrays, ficheros secuenciales o punteros. Estructuras de datos todas ellas muy comunes en la mayoría de los lenguajes de programación.</p>
<p>Lo más habitual es que se utilice memoria dinámica, es decir, punteros, para la implantación de todo tipo de árboles, aunque en ciertas ocasiones pueden considerarse la implantación con memoria estática mediante arrays.</p>
<h2>Algoritmos: Ordenación, Búsqueda, Recursión, Grafos</h2>
<p>La búsqueda de un elemento es, con diferencia, la operación más utilizada en los TAD, y la más importante. Por otra parte, la ordenación de los elementos del TAD puede resultar de gran ayuda a la hora de realizar búsquedas, así pues, la ordenación de los elementos del TAD es la segunda operación más útil. Se pueden distinguir dos tipos dentro de estos algoritmos:</p>
<ul><li>Algoritmos <strong>Recursivos</strong>: Los algoritmos recursivos son aquellos que se basan en el uso de rutinas de programación que se llaman a sí mismas.</li>
<li>Algoritmos <strong>Iterativos</strong>: Se consideran algoritmos iterativos a todos aquellos que no son recursivos.</li>
</ul><h3>Ordenación</h3>
<p>La finalidad de los algoritmos de ordenación es organizar ciertos datos (estos datos pueden estar contenidos en diferentes estructuras, ya sean TAD o en ficheros) en un orden creciente o decreciente mediante una regla prefijada (numérica, alfabética, …).</p>
<p>Atendiendo al tipo de elemento que se quiera ordenar puede ser:</p>
<ul><li><strong>Ordenación interna</strong>: Los datos se encuentran en memoria (ya sean tablas, listas, árboles, etc).</li>
<li><strong>Ordenación externa</strong>: Los datos están en un dispositivo de almacenamiento externo (ficheros), y su ordenación es más lenta que la interna.</li>
</ul><p>En este apartado vamos a estudiar los métodos de ordenación interna para los TAD vistos en apartados anteriores, esto es, para ordenar tablas, listas y árboles. Inicialmente nos centraremos en los TAD tabla y lista (simple o doble) y más adelante comentaremos el caso de listas múltiples y árboles.</p>
<p>Además, aquí consideraremos métodos de ordenación iterativa, es decir, no recursivos. Cuando estudiemos la recursividad veremos ejemplos de ordenaciones de tipo recursivo.</p>
<p>Los principales algoritmos de ordenación interna de tipo iterativo son:</p>
<ul><li>Selección</li>
<li>Burbuja</li>
<li>Inserción Directa</li>
<li>Inserción Binaria</li>
<li>Shell</li>
<li>Intercalación</li>
</ul><p><strong>Selección</strong></p>
<p>Este método consiste en buscar el elemento más pequeño del TAD y ponerlo en la primera posición; luego, entre los restantes, se busca el elemento más pequeño y se coloca en segundo lugar, y así sucesivamente hasta colocar el último elemento.</p>
<p>La idea de esta ordenación es independiente del tipo de TAD a la que se aplique, lo único que puede variar son ciertos aspectos o detalles en la forma explícita de hacer la ordenación según se implemente el TAD con memoria estática (arrays) o memoria dinámica (punteros).</p>
<p>Por ejemplo, si tenemos el array{40,21,4,9,10,35}, o la lista (40,21,4,9,10,35), los pasos a seguir son:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/seleccion.png?w=825"/></p>
<p><strong>Burbuja</strong></p>
<p>Consiste en comparar pares de elementos adyacentes e intercambiarlos entre sí hasta que estén todos ordenados. Utilizando como ejemplo la tabla anterior {40,21,4,9,10,35}:</p>
<p>Primera pasada: Se comienza por el primer elemento.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/burbuja1.png?w=825"/></p>
<p>Segunda pasada: Se comienza por el segundo elemento.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/burbuja2.png?w=825"/></p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/burbuja3.png?w=825"/></p>
<p><strong>Inserción directa</strong></p>
<p>En este método lo que se hace es tener una sublista ordenada de elementos de la lista, o array, e ir insertando el resto en el lugar adecuado para que la sublista no pierda el orden. La sublista ordenada se va haciendo cada vez mayor, de modo que al final la lista entera queda ordenada. Utilizando como ejemplo la tabla anterior {40,21,4,9,10,35}:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/insercion_directa.png?w=825"/></p>
<p><strong>Inserción binaria</strong></p>
<p>Es el mismo método que la inserción directa, excepto que la búsqueda del orden de un elemento en la sublista ordenada se realiza mediante una búsqueda binaria, lo que en principio supone un ahorro de tiempo. No obstante, dado que para la inserción sigue siendo necesario un desplazamiento de los elementos, el ahorro, en la mayoría de los casos, no se produce, si bien hay compiladores que realizan optimizaciones que lo hacen ligeramente más rápido.</p>
<p><strong>Shell</strong></p>
<p>Es una mejora del método de inserción directa, utilizado cuando la tabla tiene un gran número de elementos. En este método no se compara a cada elemento con el de su izquierda, como en el de inserción, sino con el que está a un cierto número de lugares (llamado salto) a su izquierda. Este salto es constante, y su valor inicial es N/2 (siendo N el número de elementos, y siendo división entera). Se van dando pasadas hasta que en una pasada no se intercambie ningún elemento de sitio. Entonces el salto se reduce a la mitad, y se vuelven a dar pasadas hasta que no se intercambie ningún elemento, y así sucesivamente hasta que el salto vale 1.&nbsp;Utilizando como ejemplo {40,21,4,9,10,35}:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/shell.png?w=825"/></p>
<p>Con sólo 6 intercambios se ha ordenado el array, cuando por inserción se necesitaban muchos más.</p>
<p><strong>Intercalación</strong></p>
<p>No es propiamente un método de ordenación, consiste en la unión de dos tablas o listas ordenadas de modo que la unión esté también ordenada. Para ello, basta con recorrer los TAD de izquierda a derecha e ir cogiendo el menor de los dos elementos, de forma que sólo aumenta el contador del array del que sale el elemento siguiente para el array-suma. Si quisiéramos sumar las tablas {1,2,4} y {3,5,6}, los pasos serían:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/intercalacion.png?w=825"/></p>
<h3>Búsqueda</h3>
<p>Como se ha mencionado anteriormente la búsqueda es la operación más importante en el procesamiento de la información, y permite la recuperación de datos previamente almacenados. El tipo de búsqueda se puede clasificar como interna o externa, según el lugar en el que esté almacenada la información (en memoria o en dispositivos externos). Todos los algoritmos de búsqueda tienen dos finalidades:</p>
<ul><li>Determinar si el elemento buscado se encuentra en el conjunto en el que se busca.</li>
<li>Si el elemento está en el conjunto, hallar la posición en la que se encuentra.</li>
</ul><p>En este apartado nos centraremos en la búsqueda interna iterativa. Como principales algoritmos en tablas y listas tenemos las búsquedas:</p>
<ul><li>Secuencial</li>
<li>Binario o Dicotómica</li>
<li>Utilizando tablas Hash</li>
</ul><p><strong>Búsqueda Secuencial</strong></p>
<p>Esta búsqueda consiste en recorrer y examinar cada uno de los elementos hasta encontrar el o los elementos buscados, o hasta que se han mirado todos los elementos.</p>
<p>Por ejemplo, para la lista (10,12,4,10,9) donde queremos encontrar el elemento cuyo contenido es 10, la idea del algoritmo sería:</p>
<p>Utilizando como ejemplo la tabla anterior {40,21,4,9,10,35}:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/busqueda_secuencial.png?w=825"/></p>
<p>Puesto que queremos encontrar todas las ocurrencias del valor 10, es necesario recorrer siempre toda la lista o tabla, así pues habrá que recorrer los N elementos, lo cual hace que el coste del algoritmo sea N, y su orden O(N).</p>
<p>Si sólo queremos encontrar la primera ocurrencia que se produzca, si tenemos la certeza de que no puede haber elementos repetidos, se puede parar la búsqueda en cuanto se produzca la primera ocurrencia, con lo cual el algoritmo es más eficiente. En este caso, el número medio de comparaciones que hay que hacer antes de encontrar el elemento buscado es de (N+1)/2. Aún así, el orden sigue siendo O(N).</p>
<p><strong>Búsqueda binaria o dicotómica</strong></p>
<p>Para utilizar este algoritmo, se precisa que la tabla o lista considerada esté ordenada. La búsqueda binaria consiste en dividir la tabla por su elemento medio en dos subtablas más pequeñas, y comparar el elemento con el del centro. Si coinciden, la búsqueda se termina. Si el elemento es menor, debe estar (si está) en la primera subtabla, y si es mayor está en la segunda.</p>
<p>Por ejemplo, para buscar el elemento 3 en {1,2,3,4,5,6,7,8,9} se realizarían los siguientes pasos:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/busqueda_binaria.png?w=825"/></p>
<p>Si al final de la búsqueda todavía no lo hemos encontrado, y la subtabla a dividir está vacía {}, quiere decir que el elemento no se encuentra en la tabla.</p>
<p>En general, este método realiza {log2 (N+1)} comparaciones antes de encontrar el elemento, o antes de descubrir que no está. Este número es muy inferior que el necesario para la búsqueda lineal para casos grandes.</p>
<p>Este método también se puede implementar de forma recursiva, siendo la función recursiva la que divide la tabla o lista.</p>
<p><strong>Búsqueda utilizando Tablas Hash</strong></p>
<p>Este método no es realmente un método de búsqueda, sino una forma de mejorar la velocidad de búsqueda al utilizar algún otro método.</p>
<p>Consiste en asignar a cada elemento un índice mediante una transformación del elemento. Esta correspondencia se realiza mediante una función de conversión, llamada función hash. La correspondencia más sencilla es la identidad, esto es, al número 0 se le asigna el índice 0, al elemento 1 el índice 1, y así sucesivamente.</p>
<p>Pero si los números a almacenar son demasiado grandes esta función es inservible. Por ejemplo, se quiere guardar en un array la información de 1000 usuarios de una empresa, y se elige el número de DNI como elemento identificativo. Es inviable hacer un array de 100.000.000 elementos, sobre todo porque se desaprovecha demasiado espacio. Por eso, se realiza una transformación al número de DNI para que nos de un número menor, de 3 cifras pues hay 1000 usuarios, y utilizar este resultado de la función hash como índice de un array de 1000 elementos para guardar a los empleados.</p>
<p>Así, dado un DNI a buscar, bastaría con realizar la transformación según la función hash a un número de 3 cifras; usar este número como índice de búsqueda del array de 1000 elementos, con cualquiera de los métodos anteriores, y obtener el contenido del array dado por la posición cuyo índice es el resultado de la función hash.</p>
<p>La función de hash ideal debería ser biyectiva, esto es, que a cada elemento le corresponda un índice, y que a cada índice le corresponda un elemento, pero no siempre es fácil encontrar esa función, e incluso a veces es inútil, ya que puede no saberse “a priori” el número de elementos a almacenar.</p>
<p>La función de hash depende de cada problema y de cada finalidad, y se pueden utilizar con números o cadenas, pero las más utilizadas son:</p>
<ul><li><em>Restas sucesivas</em>: Esta función se emplea con claves numéricas entre las que existen huecos de tamaño conocido, obteniéndose direcciones consecutivas.</li>
<li><em>Aritmética modular</em>: El índice de un número es resto de la división de ese número entre un número N prefijado, preferentemente primo. Los número se guardarán en las direcciones de memoria de 0 a N-1. Este método tiene el problema de que cuando hay (N+1) elementos, al menos un índice es señalado por dos elementos (teorema del palomar). A este fenómeno se le llama colisión.</li>
<li><em>Mitad del cuadrado</em>: Consiste en elevar al cuadrado la clave y coger las cifras centrales. Este método también presenta problemas de colisión.</li>
<li><em>Truncamiento</em>: Consiste en ignorar parte del número y utilizar los elementos restantes como índice. También se produce colisión.</li>
<li><em>Plegamiento</em>: Consiste en dividir el número en diferentes partes, y operar con ellas (normalmente con suma o multiplicación). También se produce colisión.</li>
</ul><p>Ahora se nos presenta el problema de qué hacer con las colisiones, es decir, el <strong>Tratamiento de Colisiones</strong>. ¿Qué pasa cuando a dos elementos diferentes les corresponde el mismo índice?. Pues bien, hay tres posibles soluciones:</p>
<ul><li>Cuando el índice correspondiente a un elemento ya está ocupado, se le asigna el primer índice libre a partir de esa posición. Este método es poco eficaz, porque al nuevo elemento se le asigna un índice que podrá estar ocupado por un elemento posterior a él, y la búsqueda se ralentiza, ya que no se sabe la posición exacta del elemento.</li>
<li>También se pueden reservar unos cuantos lugares al final del array para alojar a las colisiones. Este método también tiene un problema: ¿Cuánto espacio se debe reservar? Además, sigue la lentitud de búsqueda si el elemento a buscar es una colisión.</li>
<li>Lo mejor es en vez de crear un array de números, crear un array de punteros, donde cada puntero señala el principio de una lista enlazada. Así, cada elemento que llega a un determinado índice se pone en el último lugar de la lista de ese índice. El tiempo de búsqueda se reduce considerablemente, y no hace falta poner restricciones al tamaño del array, ya que se pueden añadir nodos dinámicamente a la lista.</li>
</ul><h3>Recursividad</h3>
<p><strong>Definición de recursividad</strong></p>
<p>La <strong>recursividad</strong> es una característica que permite que una determinada acción se pueda realizar en función de invocar la misma acción pero en un caso más sencillo, hasta llegar a un punto (caso base) donde la realización de la acción sea muy sencilla. Esta forma de ver las cosas es útil para resolver problemas definibles en sus propios términos. En cierta medida, es análogo al principio de inducción.</p>
<p>Para desarrollar algoritmos recursivos hay que partir del supuesto de que ya hay un algoritmo que resuelve una versión más sencilla del problema. A partir de esta suposición debe hacerse lo siguiente:</p>
<ul><li>Identificar subproblemas atómicos de resolución inmediate. Los denominados <em>casos base</em>.</li>
<li>Descomponer el problema en subproblemas resolubles mediante el algoritmo preexistente; la solución de estos subproblemas debe aproximarnos a los casos base.</li>
</ul><p>No existen problemas intrínsecamente recursivos o iterativos; cualquier proceso iterativo puede expresarse de forma recursiva y viceversa. Si bien ciertos problemas se prestan mucho mejor que otros al uso de la recursividad.</p>
<p>En el mundo de las matemáticas, un clásico ejemplo de recursividad lo tenemos en el cálculo del factorial de un número, a saber:</p>
<pre>Factorial del número natural n (incluido el 0) = n!
     (1) si n = 0 entonces: 0! = 1
     (2) si n &gt; 0 entonces: n! = n · (n-1)!</pre>
<p>Aunque en este estudio de los TAD hemos evitado el uso de lenguajes de programación específicos, por ser una de las características de los tipos abstractos de datos la independencia de su implantación; en esta ocasión recurriremos al lenguaje C para poner un ejemplo muy claro e ilustrativo de cómo implementar un algoritmo recursivo. El siguiente programa es un ejemplo del cálculo del factorial de un número n:</p>
<pre>int factorial(int n)
{
     if (n == 0) return 1;&nbsp; &nbsp;         // Caso base
     return (n * <strong>factorial(n-1)</strong>);&nbsp; &nbsp;  // Llamada a sí mismo
}</pre>
<p>La función factorial es llamada pasándole un determinado entero y devuelve otro numero entero. Como se observa, en cada llamada recursiva se reduce el valor de n, llegando el caso en el que n es 0 y no efectúa más llamadas recursivas.</p>
<p>Aunque la función factorial se preste muy bien al uso de la recursividad, no quiere decir esto, tal como hemos mencionado anteriormente, que no pueda ser implementado de forma iterativa. De hecho el factorial puede obtenerse con facilidad sin necesidad de emplear funciones recursivas, es más, el uso del programa anterior es muy ineficiente (con un número n grande, al ejecutarse en una computadora, consumiría mucha más memoria y tiempo que si se usase un algoritmo iterativo), pero es un ejemplo muy claro.</p>
<p><strong>Uso de la recursión</strong></p>
<p>La pregunta que surge de manera natural es: <em>¿Cuándo utilizar la recursividad?</em>. No se debe utilizar si la solución iterativa es sencilla y clara. En otros casos, obtener una solución iterativa es mucho más complicado que una solución recursiva, y entonces se planteará si merece la pena transformar la solución recursiva en una iterativa.</p>
<p>Por otra parte, hay TAD que, debido a sus características, sus operaciones se adaptan muy bien al uso de la recursión. Casi todos los algoritmos basados en los esquemas de vuelta atrás y divide y vencerás son recursivos. Otras estructuras que se adaptan muy bien a la recursividad son los grafos, y cuando se habla de grafos se está incluyendo a las listas y a los árboles.</p>
<p>Si nos centramos en el mundo de la programación, algunos lenguajes de programación no admiten el uso de recursividad. Es obvio que en este caso se requerirá una solución no recursiva (iterativa). Aunque parezca mentira, es en general mucho más sencillo escribir un programa recursivo que su equivalente iterativo. Y desde luego siempre resulta más económico en cantidad de líneas de código.</p>
<p><strong>Ordenaciones y búsquedas recursivas</strong></p>
<p>Ya hemos visto en apartados anteriores como se realizan ordenaciones y búsquedas iterativas en TAD tipo tabla y lista. Veamos ahora algoritmos de naturaleza recursiva para realizar estas operaciones.</p>
<p>La <strong>Ordenación Rápida (Quicksort)</strong> es un algoritmo de ordenación ilustrativo del uso de la recursividad en ordenaciones. Este método se basa en la táctica “divide y vencerás”, que consiste en ir subdividiendo el TAD considerado, en nuestro caso una tabla o lista en partes más pequeñas, y ordenar éstas.</p>
<p>Para hacer esta división, se toma el valor como pivote, y se mueven todos los elementos menores que este pivote a su izquierda, y los mayores a su derecha. A continuación se aplica el mismo método a cada una de las dos partes en las que queda dividido el array.</p>
<p>Normalmente se toma como pivote el primer elemento del array, y se realizan dos búsquedas: una de izquierda a derecha, buscando un elemento mayor que el pivote, y otra de derecha a izquierda, buscando un elemento menor que el pivote. Cuando se han encontrado los dos, se intercambian, y se sigue realizando la búsqueda hasta que las dos búsquedas se encuentran. Por ejemplo, para dividir el array {21,40,4,9,10,35}, los pasos serían:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/quicksort.png?w=825"/></p>
<p>Respecto a los árboles, la idea fundamental que hace posible el uso de la recursividad es que realmente un árbol puede considerarse como un nodo raíz del que cuelgan otros árboles, llamados subárboles. Véase la siguiente figura como ejemplo de esta idea de un árbol binario:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/recursivo2.png?w=825"/></p>
<p>Para realizar cualquier exploración, recorrido o búsqueda en un árbol binario (o cualquier árbol genérico) bastaría con aplicar la misma operación a cada uno de sus subárboles, hasta llegar al caso base, que sería la búsqueda o recorrido en un subárbol formado por el nodo raíz y nodos hojas, pues en este caso la búsqueda o recorrido es muy fácil, basta seguir los enlaces del nodo raíz para visitar los nodos hojas. Una vez hecho esto el algoritmo recursivo consiste en hacer lo mismo, esto es, seguir los enlaces del nodo raíz, pero tomando como nodo raíz el nodo padre de los nodos caso base. Se repite el proceso hasta llegar al nodo raíz del árbol completo.</p>
<p>En nuestro ejemplo, los casos bases se darían al llegar a los nodos B y C. Ambos nodos son casos base pues únicamente tienen nodos hojas. Una vez visto sus enlaces y sus nodos hojas se realizaría la misma operación pero tomando el nodo padre de B y C, el nodo A, y tratando a los nodos B y C como si fuesen hojas.</p>
<p>Veremos en el siguiente apartado sobre grafos que un TAD tipo árbol no es más que un tipo particular de grafo. Y con respecto a estos, comprobaremos que sus operaciones, entre las que está la búsqueda y la ordenación, son de índole profundamente recursiva.</p>
<h3>Grafos</h3>
<p>Un grafo es un objeto matemático que se utiliza para representar circuitos, redes, caminos, etc. Los grafos son muy utilizados en computación, ya que permiten resolver problemas muy complejos.</p>
<p>Supongamos el siguiente ejemplo. Disponemos de una serie de ciudades y de carreteras que las unen. De cada ciudad saldrán varias carreteras, por lo que para ir de una ciudad a otra se podrán tomar diversos caminos. Cada carretera tendrá un coste asociado (por ejemplo, la longitud de la misma). Gracias a la representación por grafos podremos elegir el camino más corto que conecta dos ciudades, determinar si es posible llegar de una ciudad a otra, si desde cualquier ciudad existe un camino que llegue a cualquier otra, etc. Para tener una idea visual de lo expuesto, supongamos que representamos las ciudades como circunferencias y los caminos por líneas que unen las distintas circunferencias (ciudades):</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/grafos1.png?w=825"/></p>
<p>Una primera cosa que salta a la vista es que tanto una lista como un árbol no son más que un caso particular de grafo, en donde hemos puesto ciertas restricciones.</p>
<p>Veamos los grafos correspondientes a una lista y un árbol binario:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/grafos2.png?w=825"/></p>
<p><strong>Componentes de un grafo</strong></p>
<p>Así pues, un grafo consta de:</p>
<ul><li><strong>Vértices</strong> (o nodos): Los vértices son objetos que contienen información. Para representarlos se suelen utilizar puntos o circunferencias con el contenido del nodo escrito dentro. En nuestro ejemplo serían las circunferencias que representan las ciudades.</li>
<li><strong>Aristas</strong>: Son las conexiones entre vértices. Para representarlos se utilizan líneas. Es frecuente añadir junto a la línea el nombre de los nodos origen y destino y el peso de la arista en algún tipo de unidad.</li>
</ul><p><strong>Definición formal de grafo</strong></p>
<p>Conviene decir que la definición de un grafo no depende de su representación. Desde un punto de vista matemático puramente formal, la definición de grafo es la siguiente:</p>
<p><em>Un grafo G es un par (V(G), A(G)), donde V(G) es un conjunto no vacío de elementos llamados vértices, y A(G) es una familia finita de pares no ordenados de elementos de V(G) llamados aristas.</em></p>
<p>Al ser una familia de aristas se permite la posibilidad de aristas múltiples en el grafo, es decir, la existencia de más de una arista con el mismo par de vértices como origen y destino. También se permite la existencia de aristas bucles, con inicio y destino el mismo vértice.</p>
<p>Por ejemplo, según lo dicho y utilizando la forma de representación indicada en el apartado anterior, se puede observar que el conjunto de vértices <em>V(G){a, b, c, d, e, f}</em> y el de aristas <em>A(G)</em> formado por los pares <em>{a, b}, {a, b}, {b, c}, {a, d}, {d, e}, {d, e}, {b, f}, {b, f}, {c, e}, {a, a}, {b, b} y {c, c}</em> determinan el grafo de la figura siguiente:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/grafo3.png?w=825"/></p>
<p><strong>Conceptos fundamentales sobre grafos</strong></p>
<p>Algunos conceptos fundamentales al hablar de grafos son:</p>
<ul><li>Un <strong>CAMINO</strong> o <strong>CIRCUITO</strong> entre dos vértices es una lista de vértices en la que dos elementos sucesivos están conectados por una arista del grafo.</li>
</ul><p>Desde un punto de vista formal, cualquier secuencia finita de aristas de G de la forma (v0v1), (v1v2), (v2v3), …, (vm-1vm) será denominada <em>camino</em> o <em>circuito</em> de G. Es frecuente que cuando entre dos vértices, por ejemplo los vértices “v” y “w”, existe uno o más caminos, sehable de cualquiera de estos caminos como un camino “vw”.</p>
<ul><li>Se habla de <strong>GRAFO CONEXO</strong> si existe un camino desde cualquier nodo del grafo hasta cualquier otro. Si no es conexo constará de varias <em>componentes conexas</em>. Formalmente, un grafo G es <em>conexo</em> si para cualquier par de vértices “v”, “w” de G existe un camino de “v” a “w” (“vw”).</li>
<li>Un <strong>PUENTE</strong> o <strong>ARISTA PUENTE</strong> será cualquier arista de un grafo conexo que mediante su eliminación deje al grafo dividido en dos componentes conexas.</li>
</ul><p>En el grafo de la figura siguiente la arista {c, f} será una arista puente que dejará el grafo G dividido en las componentes conexas formada por los vértices {f} y {a, b, c, d, e}.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/grafo4.png?w=825"/></p>
<ul><li>Un <strong>CAMINO SIMPLE</strong> es un camino desde un nodo a otro en que ningún nodo se repite (no se pasa dos veces). Si el camino simple tiene como primer y último elemento al mismo nodo se denomina <em>ciclo</em>.</li>
</ul><p>Cuando el grafo no tiene ciclos tenemos un árbol. Varios árboles independientes forman un <em>bosque</em>.</p>
<ul><li>Un <strong>ÁRBOL DE EXPANSIÓN</strong> de un grafo es una reducción del grafo en el que solo entran a formar parte el número mínimo de aristas que forman un árbol y conectan a todos los nodos. Por ejemplo:</li>
</ul><p><img src="https://gsitic.files.wordpress.com/2018/01/grafo5.png?w=825"/></p>
<ul><li>Según el número de aristas que contiene, se habla de <strong>GRAFO COMPLETO</strong> si cuenta con todas las aristas posibles (es decir, todos los nodos están conectados con todos), <strong>GRAFO DISPERSO</strong> si tiene relativamente pocas aristas y <strong>GRAFO DENSO</strong> si le faltan pocas para ser completo.</li>
<li>Las aristas son la mayor parte de la veces bidireccionales, es decir, si una arista conecta dos nodos A y B se puede recorrer tanto en sentido hacia B como en sentido hacia A. Estos son llamados <strong>GRAFOS NO DIRIGIDOS</strong>. Sin embargo, en ocasiones tenemos que las uniones son unidireccionales. Estas uniones se suelen dibujar con una flecha y definen un <strong>GRAFO DIRIGIDO</strong>.</li>
<li>Se habla de <strong>GRAFO PONDERADO</strong> cuando las aristas llevan un coste asociado (un entero denominado <strong>peso</strong>).</li>
<li>Una <strong>RED</strong> es un grafo dirigido y ponderado.</li>
</ul><p><strong>Exploración de grafos</strong></p>
<p>Cuando se habla de la exploración de un grafo nos referimos a la exploración de todos los vértices (con algún tipo de fin, por ejemplo, un recuento) o hasta que se encuentra uno determinado, es decir, una búsqueda.</p>
<p>El orden en que los vértices éstos son “visitados” decide radicalmente el tiempo de ejecución del algoritmo.</p>
<p>Supongamos el siguiente grafo de ejemplo:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/grafo6.png?w=825"/></p>
<p>A la hora de explorar el grafo de la figura anterior, nos encontramos con dos métodos distintos:</p>
<ul><li>Exploración o búsqueda en <strong>Anchura</strong> o <strong>Amplitud</strong>: Lo que prima en la exploración es la dimensión horizontal, de manera que por cada vértice del nodo visitamos primeramente todos los nodos enlazados directamente con él (vecinos), y una vez hecho esto realizamos la misma operación con estos nodos vecinos visitados.</li>
<li>Exploración o búsqueda en <strong>Profundidad</strong>: Lo que prima en la exploración es la dimensión vertical. Una vez visitado uno de los nodos vecinos de un nodo, antes de visitar a cualquiera de los demás vecinos del nodo, se vuelve a realizar la misma operación con el nodo vecino recién visitado.</li>
</ul><p>Suponiendo que el orden en que están almacenados los nodos en la estructura de datos correspondiente es A-B-C-D-E-F-G-H-I-J-K (en orden alfabético), tenemos que:</p>
<ul><li>En un recorrido en anchura el orden sería: <em>A-B-C-D-E-G-H-I-J-K-F</em></li>
<li>El orden que seguiría el recorrido en profundidad será: <em>A-B-E-I-F-C-G-J-K-H-D</em></li>
</ul><p><strong>Implantación de la exploración de grafos</strong></p>
<p>En el ejemplo anterior, es destacable que el nodo D es el último en explorarse en la búsqueda en profundidad pese a ser adyacente al nodo de origen (A). Esto es debido a que primero se explora la rama del nodo C, que también conduce al nodo D.</p>
<p>Es decir, hay que tener en cuenta que es fundamental el orden en que los nodos están almacenados en las estructuras de datos. Si, por ejemplo, el nodo D estuviera antes que el C, en la búsqueda en profundidad se tomaría primero la rama del D (con lo que el último en visitarse sería el C), y en la búsqueda en anchura se exploraría antes H que el G.</p>
<p>Otro punto a observar es que, cuando hemos hablado en el apartado anterior de exploraciones en anchura y en profundidad, aparecen las siguientes frases “una vez hecho esto realizamos la misma operación” y “se vuelve a realizar la misma operación”. Esto está sugiriendo de forma muy clara que las exploraciones en grafos, tanto en anchura como en profundidad tienen una fuerte naturaleza recursiva. De hecho, es frecuente que se implanten ambos algoritmos usando recursividad.</p>
<p>Esto no quiere decir que no puedan implementarse exploraciones de grafos de forma iterativa. Usando algoritmos iterativos, la diferencia principal entre implementar una exploración en anchura frente a una en profundidad está en la estructura de datos usada, de forma que:</p>
<ul><li>Las <em>exploraciones</em> o <em>búsquedas en anchura</em> iterativas usa una estructura de datos tipo <em>cola</em>, pues las características de este tipo de estructura FIFO (primero en entrar, primero en salir) se adaptan muy bien a este tipo de recorrido.</li>
<li>Las <em>exploraciones</em> o <em>búsquedas en profundidad</em> iterativas usa una estructura de datos tipo <em>pila</em>, pues las características de este tipo de estructura LIFO (último en entrar, primero en salir) se adaptan muy bien a este tipo de recorridos.</li>
</ul><h2>Organizaciones de Ficheros</h2>
<p>Todas las aplicaciones necesitan almacenar y recuperar información. En una computadora, cuando se ejecuta una aplicación (un proceso), la información almacenada en la memoria principal electrónica del computador; este es un tipo de memoria volátil, de forma que cuando la aplicación termina la información se pierde. Esto es inaceptable para muchas aplicaciones, que pueden requerir que la información permanezca disponible durante largos periodos de tiempo.</p>
<p>Con respecto a la memoria principal de las computadoras, se trata de un tipo de memoria electrónicas cuyas principales características son:</p>
<ul><li>La memoria principal tiene poca capacidad de almacenamiento. No se pueden manipular grandes cantidades de datos, ya que puede haber casos en los que no quepan en la memoria principal.</li>
<li>La memoria principal es volátil.</li>
<li>Acceso rápido a la información.</li>
</ul><p>Otro problema es que varios procesos pueden necesitar acceder a una misma información de forma concurrente. Como los espacios de memoria de los procesos son privados, un proceso no puede acceder a los datos en el espacio de memoria de otro. La solución es hacer que la información sea independiente de los procesos.</p>
<p>Por tanto, hay tres requisitos esenciales para almacenar la información en discos magnéticos u otros dispositivos en una unidades llamadas <strong>ficheros</strong> o <strong>archivos</strong>.</p>
<p><em>Un fichero es una abstracción de un mecanismo que permite almacenar información en un dispositivo y leerla posteriormente. Podemos definir un fichero como una colección de información que tiene un nombre.</em></p>
<p>Los ficheros pueden ser leídos y escritos por cualquier proceso: son una forma de almacenamiento denominada <strong>memoria secundaria</strong>. Sus principales cualidades son:</p>
<ul><li>Capacidad de almacenamiento sólo limitada por el soporte físico de que se disponga.</li>
<li>La información está almacenada permanentemente.</li>
<li>Acceso lento a la información, ya que tiene que ser transportada desde el dispositivo externo hasta la memoria principal para su tratamiento. Existe un área de memoria principal destinada a recibir esta información procedente del dispositivo secundario. Esta área se denomina <em>Buffer</em>.</li>
</ul><p>Gráfico de Memoria Principal y Memoria Secundaria:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/memorias.png?w=825"/></p>
<p>En la figura anterior representamos de manera muy esquemática la forma de operar de un procesador, siendo:</p>
<ul><li><strong>U.C. U</strong>nit <strong>C</strong>ontrol (Unidad de Control). Circuito principal de control del procesador.</li>
<li><strong>A.L.U. A</strong>ritmetic <strong>L</strong>ogic <strong>U</strong>nit (Unidad Aritmético Lógica). Circuito especializado en operaciones aritméticas.</li>
<li><strong>E</strong>: Datos de <strong>E</strong>ntrada.</li>
<li><strong>S</strong>: Datos de <strong>S</strong>alida.</li>
</ul><p>La información almacenada en ficheros debe ser <strong>persistente</strong>, es decir, no debe verse afectada por la creación y finalización de los procesos. La gestión de ficheros es tarea del SO, y la parte del mismo que realiza dicha gestión se conoce como <strong>sistema de ficheros</strong>.</p>
<h3>Estructura de un Fichero</h3>
<p>De la definición vista de fichero, se deduce que existen diferentes tipos de ficheros en función de:</p>
<ul><li>La información contenida</li>
<li>El método de organización de la información</li>
</ul><p>Una primera clasificación de los ficheros se puede hacer según el método usado para codificar la información:</p>
<ul><li><strong>Ficheros de texto</strong>: Se guarda la información en caracteres, tal y como se mostraría en pantalla.</li>
<li><strong>Ficheros binarios</strong>: Se guarda la información en binario, tal y como está en memoria.</li>
</ul><p>Otra clasificación de los ficheros es según la forma que tiene su estructura. Las formas más usuales son:</p>
<ul><li>Organizar un fichero como <strong>una secuencia de bytes</strong>. De esta forma, el sistema operativo no conoce el significado del contenido de los ficheros, lo que simplifica la gestión de los mismos. Serán los programas de aplicación los que deberán de conocer la estructura de los ficheros que utilizan. Este enfoque es el empleado por MS-DOS y UNIX.</li>
<li>Un esquema más estructurado es considerar un fichero como <strong>una secuencia de registros de longitud fija</strong>, cada uno de los cuales presenta una estructura determinada. La idea es que las operaciones de lectura devuelvan un registro y las escrituras modifiquen o añadan un registro. El SO CP/M usa registros de 128 bytes.</li>
<li>Una tercera forma es organizar el fichero en forma de <strong>árbol de registros</strong>, que no tienen por qué tener la misma longitud. Cada registro tiene un campo clave por el que está ordenado el árbol de forma que las operaciones de búsqueda por clave se realizan rápidamente. Este esquema se emplea en grandes computadores (mainframes) orientados al proceso de grandes cantidades de información.</li>
</ul><h3>Conceptos básicos sobre Ficheros</h3>
<p>Veamos ahora una serie de conceptos básicos:</p>
<ul><li><strong>Registro lógico</strong>: Un registro es una colección de información relativa a una entidad particular. Por tanto, el registro va a contener a todos aquellos campos lógicamente relacionados, referentes a una determinada entidad, y que pueden ser tratados globalmente por un programa. Por ejemplo la información de un determinado alumno, que contiene los campos DNI, nombre, apellidos, fecha de nacimiento, etc.</li>
<li><strong>Clave de un registro lógico</strong>: Una clave es un campo o conjunto de campos de datos que identifica al registro lógico y lo diferencia del resto de registros lógicos del fichero. Por tanto, esta clave debe ser distinta para cada registro.</li>
<li><strong>Registro activo</strong>: El registro lógico que va a procesarse en la siguiente operación del fichero.</li>
<li><strong>Apuntador</strong>: Marca interna que siempre apunta al registro lógico activo. Se incrementa automáticamente cada vez que se procesa un registro (se lee o se escribe).</li>
<li><strong>Marca de fin de fichero</strong>: Una marca situada al final de cada fichero, para no acceder más allá del último registro lógico existente, ya que el tamaño del fichero no está limitado y no se conoce a priori. Existe una función lógica, <strong>eof (end of file)</strong>, que toma el valor verdadero cuando llegamos al final del fichero y falso en caso contrario.</li>
<li><strong>Factor de bloqueo</strong>: Factor de bloqueo es el número de registros lógicos que puede contener un registro físico.</li>
<li><strong>Registro físico o bloque</strong>: Un registro físico o bloque es la cantidad más pequeña de datos que pueden transferirse en una operación de E/S entre la memoria principal del ordenador y los dispositivos periféricos o viceversa. El tamaño del bloque o registro físico dependerá de las características del ordenador. En la mayoría de los casos el tamaño del bloque suele ser mayor que el de registro lógico. La adaptación consiste en empaquetar en cada bloque tantos registros lógicos como se pueda. El empaquetamiento puede ser de tipo <em>fuerte</em> o <em>débil</em>, según que se permita o no aprovechar el sobrante de un bloque, situando registros a caballo entre dos bloques contiguos. La siguiente figura ilustra ambas formas de empaquetamiento.</li>
</ul><p><img src="https://gsitic.files.wordpress.com/2018/01/empaquetamiento.png?w=825"/></p>
<p>Una vez visto lo que es un registro lógico y teniendo ya en mente la idea de fichero, podemos dar una definición más precisa de lo que es un archivo o fichero.</p>
<p><em>Un fichero es una colección de registros lógicos relacionados entre sí con aspectos en común y organizados para un propósito específico. Los datos en los archivos deben estar organizados de tal forma que puedan ser recuperados fácilmente, actualizados o borrados y almacenados en el archivo con todos los cambios realizados.</em></p>
<p>Dese un punto de vista puramente estructural:</p>
<p><em>Un fichero es una estructura de datos compuesta que agrupa una secuencia de cero o más tuplas, denominadas registros, y que a su vez se pueden componer de otras estructuras de datos a las que se les suele llamar campos.</em></p>
<h3>Operaciones sobre Ficheros</h3>
<p>Una vez visto lo que es un fichero y los principales conceptos al hablar de ellos, pasemos ahora a estudiarlos desde un punto de vista operativo. Básicamente se trata de responder: ¿qué operaciones se pueden realizar sobre un fichero? La respuesta es:</p>
<ul><li><strong>Creación</strong>: Para poder realizar cualquier operación sobre un fichero es necesario que haya sido creado previamente, almacenando sobre el soporte seleccionado la información requerida para su posterior tratamiento, como por ejemplo el nombre del dispositivo, el nombre del fichero, etc. Con anterioridad a la creación de un archivo se requiere diseñar la estructura del mismo mediante los campos del registro, longitud y tipo de los mismos.</li>
<li><strong>Apertura</strong>: Para poder trabajar con la información almacenada en un fichero, éste debe estar abierto, permitiendo así el acceso a los datos, dando la posibilidad de realizar sobre ellos las operaciones de lectura y escritura necesarias.</li>
<li><strong>Cierre</strong>: Una vez finalizadas las operaciones efectuadas sobre el fichero, éste debe permanecer cerrado para limitar el acceso a los datos y evitar así un posible deterioro o pérdida de información. Para cerrar un fichero previamente debe estar abierto.</li>
<li><strong>Actualización</strong>: Esta operación permite la puesta al día de los datos del fichero mediante la escritura de nuevos registros (alta) y la eliminación (baja) o modificación de los ya existentes. La actualización puede afectar a parte o la totalidad de los registros del fichero. Cuando se escribe un nuevo registro en el fichero se debe comprobar que no existe previamente. La baja de un registro puede ser lógica o física.
<ul><li>Una <em>baja lógica</em> supone el no borrado del registro en el archivo. Esta baja lógica se manifiesta en un determinado campo del registro con una bandera, indicador o “flag”, o bien con la escritura o rellenado de espacios en blanco en el registro específico.</li>
<li>Una <em>baja física</em> implica el borrado y desaparición del registro, de modo que se crea un nuevo archivo que no incluye al registro dado de baja.</li>
</ul></li>
<li><strong>Consulta</strong>: Tiene como fin visualizar la información contenida en el fichero, bien de un modo completo, bien de modo parcial.</li>
<li><strong>Borrado o destrucción</strong>: Es la operación inversa a la creación de un fichero. Consiste en la supresión de un fichero del soporte o dispositivo de almacenamiento. El espacio utilizado por el archivo borrado puede ser utilizado por otros archivos. Para borrar un fichero tiene que estar cerrado.</li>
<li><strong>Ordenación o clasificación</strong>: Consiste en lograr una nueva disposición sobre el soporte de los registros de un archivo, con una secuencia de ubicación determinada por el valor de uno o varios campos.</li>
<li><strong>Compactación o empaquetamiento</strong>: Esta operación permite la reorganización de los registros de un fichero eliminando los huecos libres intermedios existentes entre ellos normalmente ocasionados por la eliminación de registros.</li>
</ul><h3>Organización de un Sistema de Ficheros</h3>
<p>Los discos magnéticos son la base sobre la que se sustentan los sistemas de ficheros. Para mejorar la eficiencia, la transferencia de información entre memoria y los discos se realiza en unidades denominadas bloques. Cada bloque está formado por uno o varios sectores de disco. El tamaño de sector de un disco suele ser de 512 bytes.</p>
<p>El diseño de un sistema de ficheros plantea dos problemas diferentes:</p>
<ul><li>Definir cómo el sistema de ficheros aparece al usuario.</li>
<li>Diseñar los algoritmos y estructuras de datos necesarias para implementar este sistema de ficheros lógico en los dispositivos físicos de almacenamiento secundario.</li>
</ul><p>Un sistema de ficheros se puede estructurar en diferentes capas o niveles, se puede ver en la siguiente figura:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/estructura_ficheros.png?w=825"/></p>
<p>El nivel de control de E/S se compone de los manejadores de dispositivo (<em>device drivers</em>) y los manejadores de interrupciones (<em>interrupt handlers</em>), que son necesarios para transmitir la información entre la memoria y los discos. Los manejadores de dispositivos reciben instrucciones de bajo nivel, del tipo “escribir o leer el bloque nº x”, y generan el conjunto de instrucciones dependientes del hardware que son enviadas al controlador de disco.</p>
<p>El sistema de ficheros básico transmite las instrucciones de bajo nivel al manejador de dispositivo adecuado para leer y escribir bloques físicos en disco. Cada bloque físico se identifica por su dirección numérica en el disco, que viene dado por el dispositivo, cilindro, superficie y sector.</p>
<p>El módulo de organización de ficheros tiene conocimiento sobre los ficheros, los bloques lógicos que lo componen y los bloques físicos. Mediante el tipo de esquema de asignación de bloques y la localización del fichero, el módulo de organización de ficheros traslada las direcciones de disco lógicas en direcciones de disco físicas. Cada bloque de disco lógico tiene un número (de 0 a N) que no suele coincidir con la dirección de los bloques físicos, por lo que es necesario un mecanismo de traducción. Este módulo también incluye el gestor de espacio libre, que controla los bloques libres para que puedan ser usados posteriormente.</p>
<p>Por último,el sistema de ficheros lógicos proporciona la estructura de directorio conocida por los programas de usuario. También es responsable de proporcionar seguridad y protección al sistema de ficheros.</p>
<p>Por otra parte, para crear un nuevo fichero, un programa de aplicación realiza una llamada al sistema sobre el sistema de ficheros lógico. Este lee el directorio correspondiente en memoria, le añade una nueva entrada y lo escribe en disco. En este proceso, el sistema de ficheros lógico ha solicitado al módulo de organización de ficheros la dirección física del directorio, que se envía al sistema de ficheros básico y al control de E/S. Cuando el directorio ha sido actualizado, el sistema de ficheros lógico lo puede usar para realizar operaciones de E/S.</p>
<p>Para optimizar los accesos, el SO tiene en memoria una tabla de ficheros abiertos que contiene información sobre todos los ficheros abiertos en un momento dado, como nombre, permisos, atributos, direcciones de disco, etc. La primera referencia a un fichero suele ser una operación de apertura, que hace que se realice una búsqueda en la estructura de directorio y se localice la entrada para el fichero que se quiere abrir. Esta entrada se copia en la tabla de ficheros abiertos y el índice de dicha entrada (denominado descriptor de fichero) se devuelve al programa de aplicación, que lo usa para realizar las operaciones sobre el fichero. De esta forma, todas las operaciones relacionadas con el entrada de directorio del fichero se realizan en la tabla de ficheros abiertos en memoria. Cuando un fichero se cierra, la entrada modificada se copia a disco.</p>
<h3>Organización y Acceso a Ficheros</h3>
<p>Se entiende por <strong>Organización de un fichero</strong> a la manera en la que los datos son estructurados y almacenados internamente en el fichero y sobre el soporte de almacenamiento. El tipo de organización de un fichero se establece durante la fase de creación del mismo. Los requisitos que determinan la organización de un fichero son del tipo: tamaño del fichero, frecuencia de utilización o uso, etc.</p>
<p>La organización de un fichero es muy dependiente del soporte físico en que se almacene. Hay dos tipos de soportes:</p>
<ul><li>Soportes <strong>Secuenciales</strong>: Los registros están dispuestos físicamente uno a continuación de otro. Para acceder a un determinado registro se necesita pasar por todos los anteriores a él.</li>
<li>Soportes <strong>Direccionables</strong>: Permiten localizar a un registro directamente por su información (clave) sin tener que pasar por todos los anteriores.</li>
</ul><p>Los tipos de organizaciones de ficheros fundamentales son:</p>
<ul><li>Organización <strong>Secuencial</strong>.</li>
<li>Organización <strong>Directa</strong> o <strong>Aleatoria</strong>.</li>
<li>Organización <strong>Indexada</strong>.</li>
</ul><p>En cuanto al acceso, se entiende por tal al procedimiento necesario que debemos seguir para situarnos sobre un registro concreto con la intención de realizar una operación sobre él. Según las características del soporte empleado y la organización se consideran dos tipos de acceso:</p>
<ul><li>El <strong>acceso secuencial</strong> implica el acceso a un archivo según el orden de almacenamiento de sus registros, uno tras otro. Se puede dar en dispositivos secuenciales y direccionables.</li>
<li>El <strong>acceso directo</strong> implica el acceso a un registro determinado, sin que ello implique la consulta de los registros precedentes. Obviamente, sólo puede darse en soportes direccionables.</li>
</ul><p><strong>Organización Secuencial</strong></p>
<p>Son aquellos ficheros caracterizados porque los registros se escriben o graban sobre el soporte de almacenamiento en posiciones de memoria físicamente contiguas, en la misma secuencia u orden en que han sido introducidos, sin dejar huecos o espacios libres entre ellos.</p>
<p>Todos los dispositivos de memoria auxiliar soportan la organización secuencial. El <em>acceso a los datos</em> almacenados en estos ficheros siempre es <em>secuencial</em> independientemente del soporte utilizado. Los registros organizados secuencialmente tienen un registro especial, el último, que tiene una marca de fin de archivo.</p>
<p>Sus ventajas son:</p>
<ul><li>Rapidez en el acceso a un bloque de registros que se encuentran almacenados en posiciones de memoria físicamente contiguas.</li>
<li>No deja espacios vacíos entre registro y registro, optimizado al máximo la memoria ocupada.</li>
</ul><p>Sus inconvenientes son:</p>
<ul><li>El acceso a registros individuales es muy lento.</li>
<li>Se tiene que procesar todo el fichero para operaciones de inserción y borrado de registros.</li>
</ul><p><strong>Organización Directa o Aleatoria</strong></p>
<p>Estos ficheros se caracterizan porque los registros se sitúan en el fichero y se accede a ellos a través de una clave, que indica la posición del registro dentro del fichero y la posición de memoria donde está ubicado.</p>
<p>Estos ficheros se almacenan en <em>soportes direccionables</em>. Además, los registros han de tener un identificativo o clave, el cual indica la posición de cada registro en el fichero.</p>
<p>Como principales ventajas genéricas de este tipo de organización, tenemos que:</p>
<ul><li>Cada posición solamente puede ser ocupada por un registro, pues no podemos tener en el fichero más de un registro con el mismo valor de clave.</li>
<li>El acceso a cualquier registro se hace de una forma directa e inmediata mediante su clave.</li>
<li>La actualización de un registro es inmediata, sin que se deban utilizar archivos auxiliares para copia.</li>
<li>Se puede utilizar el acceso secuencial, aunque suponga generalmente una pérdida de tiempo.</li>
</ul><p>Dentro de la organización directa, según el algoritmo utilizado en la gestión de la clave, se pueden distinguir entre:</p>
<ul><li>Organización directa con <strong>Clave Directa</strong>: La dirección de almacenamiento del registro está indicado por la propia clave.
<ul><li>Sus ventajas son:
<ul><li>Cada posición solamente puede ser ocupada por un registro, pues no podemos tener en el fichero más de un registro con el mismo valor de clave.</li>
<li>Es muy rápido el acceso a los registros individuales.</li>
</ul></li>
<li>Sus inconvenientes son:
<ul><li>Deja gran cantidad de huecos dentro del fichero, con el consecuente desaprovechamiento del soporte de almacenamiento. Esto es debido a que este sistema precisa que el soporte donde se almacena la información tenga una mínima unidad de asignación (denominado <em>cluster</em>) a la cual acceder directamente siguiendo unas coordenadas de localización. Estas unidades no pueden ser usadas para almacenar información de distintos ficheros. Si los cluster en que divide el disco son grandes, y los ficheros a almacenar pequeños, habrá muchos cluster que se quedarán a medio llenar, con el consecuente desaprovechamiento de espacio.</li>
<li>Una consulta total del fichero puede suponer un gran inconveniente, pues hay que analizar todas las posiciones de memoria, aunque algunas posiciones estén vacías. Para comprender este hecho hagamos el siguiente símil. Supongamos que tenemos un libro con todos sus capítulos correctamente ordenados pero sin índice que nos identifique la página de inicio de cada capítulo, para leer el libro entero lo único que hay que hacer es comenzar por la primera página, sin embargo, si queremos leer un capítulo en concreto, tendríamos también que empezar desde el principio hasta encontrarlo. Esto sería el análogo a un fichero secuencial. Supongamos ahora un libro con todos los capítulos desordenados, pero con un índice al comienzo del libro que nos indica la página de comienzo de cada capítulo; es decir, el análogo al de un fichero de acceso directo. Leer cada capítulo por separado es ahora muy fácil, basta con buscar el comienzo en el índice, sin embargo, si necesitamos leer el libro entero, de principio a fin, necesitamos constantemente mirar el índice para ir viendo la secuencia de los capítulos, lo cual es muy ineficiente (por no decir pesado). Esto sería el análogo a leer completamente un fichero de acceso directo.</li>
</ul></li>
</ul></li>
<li>Organización directa con <strong>Clave Indirecta</strong>: La dirección de almacenamiento se obtiene a partir de la clave, después de realizar algún tipo de transformación. Este tipo de transformación se denomina algoritmo <em>Hashing</em>&nbsp;y suele ser de tipo matemático.
<ul><li>En este tipo de algoritmo se pueden dar dos situaciones no deseadas (denominadas&nbsp; &nbsp; <em>colisiones</em>) que son:
<ul><li>Hay direcciones que no corresponden a ninguna clave y, por tanto, zonas de disco sin utilizar.</li>
<li>Hay direcciones que corresponden a más de una clave. En este caso se dice que las claves son sinónimas para esa transformación.</li>
</ul></li>
<li>Hay dos formas de resolver el problema de los sinónimos o colisiones:
<ul><li>Buscar secuencialmente en el archivo hasta encontrar una posición libre donde escribir el registro o aplicando a la dirección obtenida un segundo método de direccionamiento. Estos procedimientos son lentos y degradan el archivo.</li>
<li>Reservar una zona de desbordamiento o de sinónimos en donde se escribirán los registros que no se pueden escribir en la dirección que le corresponde según la transformación.</li>
</ul></li>
</ul></li>
</ul><p><strong>Organización Indexada</strong></p>
<p>Al fichero le acompaña un fichero de índice que tiene la función de permitir el acceso directo a los registros del fichero de datos. El índice se puede organizar de diversas formas, las más típicas son:</p>
<ul><li><strong>Secuencial</strong></li>
<li><strong>Multinivel</strong></li>
<li><strong>Árbol</strong></li>
</ul><p>A través del índice podremos procesar un fichero de forma secuencial o de forma directa según la clave de indexación, y esto independientemente de como esté organizado el fichero por sí mismo.</p>
<p>El índice debe estar organizado en función de alguno de los campos de los registros de datos. Se pueden tener tantos índices como se quiera variando la clave (o campo) que se emplee. El índice está formado por registros (entradas) que contienen:</p>
<ul><li>Clave de organización.</li>
<li>Puntero(s) al fichero de datos, en concreto al registro que corresponda.</li>
</ul><p>Los índices se pueden clasificar en dos tipos, según cada entrada señale a la dirección de un registro del fichero de datos (<em>índice total o denso</em>), o bien apunte a un grupo de registros del fichero de datos que debe estar ordenado (<em>índice escaso o no denso</em>). En el caso de índices totales, el fichero puede estar desordenado. Véase la siguiente figura como ejemplo:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/indexacion.png?w=825"/></p>
<p>Con el segundo tipo se podría procesar directamente el fichero de datos de forma secuencial. Los índices totales o densos no suelen utilizarse de forma simple, sino combinados con índices escasos o más cortos, de esta manera pueden almacenarse en memoria principal obteniendo así una mayor rapidez de acceso.</p>
<h3>Implantación de Ficheros</h3>
<p>El aspecto básico de la implantación de ficheros consiste en determinar qué bloques de disco están asociados a cada fichero. El problema que se plantea es cómo asignar el espacio libre en disco a los ficheros de forma que ese espacio sea usado de forma eficiente y los ficheros puedan ser accedidos rápidamente. Hay que tener en cuenta que el tamaño de los ficheros es variable, por lo que habrá que diseñar algún mecanismo de almacenamiento dinámico tanto para los ficheros como para el espacio libre.</p>
<p>Existen tres métodos básicos de asignación:</p>
<ul><li>Asignación <strong>Contigua</strong>.</li>
<li>Asignación <strong>Enlazada</strong>.</li>
<li>Asignación <strong>Indexada</strong>.</li>
</ul><p><strong>Asignación Contigua</strong></p>
<p>El esquema de asignación más simple consiste en almacenar cada fichero como una secuencia adyacente de bloques en disco. La asignación contigua de un fichero se define por la dirección del primer bloque y el tamaño del fichero, es decir, simplemente responder a las preguntas ¿dónde empezar? y ¿hasta cuando seguir?.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/asignacion_contigua.png?w=825"/></p>
<p>Las ventajas de este método son:</p>
<ul><li>Fácil implementación, ya que únicamente hay que conocer la dirección en disco del primer bloque del fichero y el número de bloques que ocupa.</li>
<li>Eficiencia, ya que la lectura de un fichero se puede realizar en una sola operación. El acceso a un fichero almacenado de forma contigua es sencillo y rápido, siempre y cuando pretendamos leer todo el fichero y no tengamos que hacer búsquedas de parte de su contenido. En este tipo de operaciones se pierde toda la ventaja que proporciona esta forma de asignación. Para este tipo de operaciones veremos que es mucho más ventajosa la asignación.</li>
</ul><p>Para el acceso secuencial, el sistema de ficheros no tiene más que recordar la dirección del último bloque referenciado. El acceso directo del bloque <em>i</em> de un fichero que comienza en el bloque <em>b</em> se realiza, simplemente, accediendo al bloque <em>b+i</em>.</p>
<p>Un inconveniente de este esquema de asignación es que no se puede implantar a no ser que se conozca el tamaño de los ficheros en su momento de creación. Si esta información no está disponible, el SO no sabe cuánto espacio en disco debe reservar. Otra desventaja es la fragmentación externa que se produce en el disco, que se origina debido a que entre los ficheros quedan porciones de disco libre que no tienen el tamaño suficiente para ser asignadas a un nuevo fichero. La gravedad de este problema depende del espacio de almacenamiento disponible y del tamaño medio de los ficheros. La compactación de disco es una solución, pero es costos y de poder hacerse sería cuando el sistema estuviese parado.</p>
<p>El problema de conocer el tamaño de los ficheros en tiempo de creación se resuelve haciendo que los ficheros sean inmutables. Esto significa que cuando un fichero se crea no se puede modificar. Una modificación implica borrar el fichero original y crear uno nuevo. Por otro lado, los ficheros se han de leer de una sola vez en memoria, por lo que la eficiencia es muy alta, pero a cambio se exigen unos requisitos mínimos de memoria muy elevados. Por último, la fragmentación de disco se soluciona teniendo discos de gran capacidad de almacenamiento.</p>
<p><strong>Asignación Enlazada</strong></p>
<p>Otro esquema consiste en mantener una lista enlazada con los bloques que pertenecen a un fichero, de forma que una palabra del bloque sería un índice al bloque siguiente. Con este método se elimina el problema de la fragmentación, y, al igual que en la asignación contigua, cada entrada de directorio únicamente contiene la dirección del primer bloque del fichero. Los fichero pueden crecer de forma dinámica mientras que exista espacio libre en disco y no es necesario compactar los discos. Un inconveniente es que, mientras que el acceso secuencial es fácil de realizar, el acceso aleatorio es muy lento.</p>
<p>Otro inconveniente viene dado por el espacio requerido por los punteros. Si un puntero requiere 4 bytes y los bloques son de 512 bytes, significa que: (4 / 512) = 0,0078 –&gt; se pierde un 0,78% (casi un 1%) de espacio útil por bloque. Una solución a este problema consiste en no asignar bloques individuales, sino conjuntos de bloques denominados <em>clusters</em>. De esta forma el porcentaje de espacio perdido por los punteros se reduce. Además, se mejora el rendimiento de los discos porque se lee más información en una misma operación de lectura, y se reduce la lista de bloques libres. El coste de este método es que se produce un incremento de la fragmentación interna (espacio no ocupado en un bloque o cluster).</p>
<p>Otro problema de este método es la fiabilidad, ya que si un bloque se daña, se puede perder el resto del fichero. Peor aún, sise altera el contenido del puntero, se puede acceder a la lista de bloques libres o a bloques de otros ficheros como si fuesen bloques propios.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/asignacion_enlazada.png?w=825"/></p>
<p>Un problema más sutil viene dado por el hecho de que la cantidad de información útil para el usuario que contiene cada bloque no es potencia de dos, ya que el puntero al bloque siguiente, que estará constituido por varias palabras, ocupará parte del bloque, es decir, no se puede utilizar todo el bloque para información útil, siempre habrá que dejar mínimo espacio para el puntero. Esto puede originar una pérdida de eficiencia porque los programas normalmente leen y escriben en bloques cuyo tamaño es potencia de dos. Esta desventaja del esquema de lista encadenada desaparece si el puntero de cada bloque de disco se almacena en una tabla o índice de memoria. Así cada bloque únicamente contiene datos útiles.</p>
<p>Además, aunque el acceso aleatorio implica seguir una cadena, ésta está toda en memoria, por lo que la búsqueda es mucho más eficiente que en el esquema anterior. De igual modo, es suficiente que cada entrada de directorio contenga únicamente la dirección del primer bloque para localizar todo el fichero. Este esquema es empleado por el SO MS-DOS. Para que este esquema funcione, la tabla debe permanecer entera en memoria todo el tiempo. Si el disco es grande, el gasto de memoria principal puede ser considerable.</p>
<p><strong>Asignación Indexada</strong></p>
<p>El último método para determinar qué bloques pertenecen a un fichero consiste en asociar a cada fichero un nodo índice (<em>index-node o&nbsp;</em><em>i-node</em>), que incluye información sobre los atributos del fichero y las direcciones de los bloques de disco que pertenecen al mismo.</p>
<p>Las direcciones de los primeros bloques se almacenan en el propio nodo índice, de forma que, para ficheros pequeños, toda la información necesaria para su localización siempre está en memoria cuando son abiertos. Para ficheros de mayor tamaño, una de las direcciones del nodo índice es la dirección de un bloque simple indirecto, que contiene a su vez direcciones de otros bloques del fichero. Si no es suficiente, existen dos direcciones, una para un bloque doble indirecto, que contiene direcciones de bloques simples directos, y otra para un bloque triple indirecto, que contiene direcciones de bloques dobles indirectos.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/asignacion_indexada.png?w=825"/></p>
<p>Una ventaja es que permite el acceso directo a cualquier bloque del fichero. Además, los accesos a un fichero, una vez abierto, no implican accesos adicionales a disco a no ser que sean necesarios bloques indirectos.</p>
<p>Un inconveniente es que añadir o borrar bloques en medio del fichero implica tener que reorganizar los punteros en el bloque de índices, lo cual constituye una operación costosa.</p>
<h3>Directorios</h3>
<p>Los sistemas de ficheros pueden contener grandes volúmenes de información, por lo que los SO proporcionan mecanismos para estructurarlos. Esta estructuración se suele realizar a dos niveles.</p>
<p>En primer lugar, el sistema de ficheros se divide en particiones, que se pueden considerar como discos virtuales. Un disco puede contener una o varias particiones, y una partición puede estar repartida. En segundo lugar, cada partición contiene una tabla de contenidos de la información que contiene. Esta tabla se denomina directorio, y su función principal es hacer corresponder un nombre de un fichero con una entrada en la tabla. Cada entrada contiene, como mínimo, el nombre del fichero.</p>
<p>A continuación se pueden almacenar los atributos y direcciones del fichero en disco, o un puntero a otra estructura de datos que contiene dicha información. Esta estructura de datos se suele conocer con el nombre <strong>nodo índice</strong>.</p>
<p>Mostramos los atributos y direcciones a una estructura de datos:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/directorios.png?w=825"/></p>
<p>Cuando se abre un fichero el SO busca en el directorio correspondiente hasta que encuentra el nombre del fichero, toma la información que necesita y la introduce en una tabla residente en la memoria principal. Las siguientes referencias al fichero utilizarán la información que ya está en memoria.</p>
<h3>Implantación de Directorios</h3>
<p>Para acceder a un fichero, ya sea para lectura o escritura, previamente hay que abrir el fichero. Esta operación implica que el SO, a partir de la ruta de acceso, debe localizar la entrada de directorio correspondiente. Esta entrada proporciona la información necesaria para localizar los bloques de disco del fichero. Esta información, según el tipo de sistema, puede ser la dirección en disco del fichero completo (asignación contigua), el número del primer bloque (los dos métodos basados en listas encadenadas) o el número de nodo índice. En todo caso, la principal función del sistema de directorios es asociar el nombre en ASCII de un fichero con la información precisa para localizar los datos. Los atributos de los ficheros se pueden almacenar en la misma entrada de directorio. Si usan nodos índice, es posible almacenar los atributos en el nodo índice.</p>
<p>A continuación se exponen brevemente la implantación de directorios en varios SO: CP/M, MS-DOS y UNIX. No vamos a mencionar nada de las características de cada SO, simplemente mencionamos estos SO para ver distintas filosofías de implementar directorios.</p>
<p><strong>Directorios en CP/M</strong></p>
<p>En CP/M solamente existe un directorio, por lo que el sistema de ficheros únicamente tiene que buscar el nombre de un fichero en dicho directorio. Si un fichero ocupa más de 16 bloques se le asignan más entradas de directorio.</p>
<p>Los campos de una entrada de directorio en CP/M son los siguientes:</p>
<ul><li>El código de usuario (1 byte) permite conocer el propietario del fichero.</li>
<li>El nombre y la extensión del fichero (8 y 3 bytes, respectivamente).</li>
<li>Si un fichero ocupa más de 16 bloques, el campo magnitud (1 byte) indica el orden que ocupa esa entrada.</li>
<li>El contador de bloques (1 byte) indica cuántos bloques están en uso de los 16 posibles.</li>
<li>Los últimos 16 campos contienen las direcciones de bloques de disco del fichero. Como el último bloque puede no estar lleno, es imposible conocer con exactitud el tamaño en bytes de un fichero.</li>
</ul><p><img src="https://gsitic.files.wordpress.com/2018/01/cpm.png?w=825"/></p>
<p><strong>Directorios en MS-DOS</strong></p>
<p>MS-DOS tiene un sistema de ficheros jerárquico. Cada entrada de directorio tiene 32 bytes, y contiene, entre otros datos, el nombre del fichero, la extensión, los atributos y el número del primer bloque en disco del fichero. Este número es un índice a una tabla de asignación denominada FAT (<em>File Allocation Table</em>). Un directorio puede contener otros directorios, lo que origina la estructura jerárquica del sistema de ficheros.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/msdos.png?w=825"/></p>
<p><strong>Directorios en UNIX</strong></p>
<p>La estructura de una entrada de directorio en un sistema UNIX tradicional es muy simple, y contiene únicamente el nombre del fichero y el número de su nodo índice. Toda la información sobre el fichero reside en el propio nodo índice.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/unix.png?w=825"/></p>
<h2>Formatos de Información y Ficheros</h2>
<p>Independientemente de la plataforma con que se trabaje, la información obtenida se genera con un ordenador y se suele almacenar en un fichero, con la intención de recuperarla más tarde cuando sea necesaria, o compartirla con los demás a través de algún medio de transmisión de datos. En consecuencia, es conveniente conocer los formatos de archivo más indicados para almacenar los distintos tipos de información que deben contener.</p>
<p>En este apartado vamos a estudiar los ficheros desde un punto de vista operativo, es decir, según el uso o función que se le da al fichero. Podría decirse que desde el punto de vista del usuario, al que le interesa guardar datos en un archivo y tenerlo localizado de alguna forma en su ordenador independientemente de cómo esté organizado el fichero o cual sea su estructura.</p>
<h3>Formatos de Información</h3>
<p>La mayoría de aplicaciones suelen guardar la información que producen en formatos de fichero propios, de modo que podemos editarlos posteriormente con la garantía que se respetarán todas las peculiaridades de los datos y el nivel de edición que poseían en el momento de guardarlos, ahora, cuando compartimos información debemos ser muy cuidadosos con la elección del tipo de fichero ya que no debemos asumir que todo el mundo posee nuestras mismas herramientas ni nuestro mismo sistema.</p>
<p>No se trata de analizar en profundidad las características de todos los tipos de archivo, sino indicar algunas referencias generales sobre los más usados que nos ayuden a decidir el formato adecuado en cada ocasión.</p>
<p><strong>Ficheros con Información de Texto</strong></p>
<p>Si queremos almacenar o compartir un fichero de texto tenemos dos formatos básicos independientes de la plataforma, es decir, son legibles con un editor de texto sobre cualquier SO:</p>
<ul><li><strong>TXT</strong>, para ficheros de texto plano.</li>
<li><strong>RTF</strong>, Rich Text Format (Formato de texto enriquecido) cuando sea necesario incluir en el texto algunos elementos de realce como cursivas o negrita.</li>
</ul><p><strong>Ficheros con Información de Imagen</strong></p>
<p>Hay gran variedad de formatos de archivos gráficos, la mayoría compatibles con cualquier plataforma. Entre los más habituales se encuentran:</p>
<ul><li><strong>JPG</strong> para imágenes de tono continuo en mapa de bits. Es un formato comprimido pues prescinde de los datos de color de la imagen que no están en el espectro visible.</li>
<li><strong>GIF</strong> usado especialmente con animaciones y gráficos con regiones transparentes. Tiene algunos problemas legales con los términos de su licencia.</li>
<li><strong>PNG</strong> tiene similares características al GIF aunque se trata de un formato más evolucionado y de mayor calidad, con muy buenos ratios de compresión y soporte para multitransparencia. Posee una licencia libre.</li>
<li><strong>TIFF</strong> se utiliza para almacenar imágenes sin pérdida de calidad, por lo que genera tamaños de archivo mayores que el resto pese a que incorpora un algoritmo de compresión.</li>
<li><strong>SVG</strong> para ilustraciones vectoriales.</li>
</ul><p><strong>Ficheros con Información&nbsp; Compuesta</strong></p>
<p>Cuando se trata de compartir documentos que integran texto con imágenes o gráficos, o la composición y aspecto son fundamentales por tratarse de formularios estandarizados o similares, tenemos dos alternativas:</p>
<ul><li>PS es un documento PostScript o formato de impresión capaz de ser visualizado con alguna aplicación auxiliar e impreso sin problemas, directamente. Mantienen la misma calidad de resolución que el documento original.</li>
<li>PDF es una versión del anterior, desarrollada por la compañía Adobe que se usa frecuentemente para compartir documentación en Internet.</li>
</ul><p><strong>Ficheros con Información Comprimida</strong></p>
<p>Para aliviar las dificultades de transmitir archivos de gran tamaño a través de las redes o ahorrar espacio en disco, se desarrollaron distintos algoritmos de compresión capaces de reducir la cantidad de memoria ocupada por un fichero. Los formatos más usados son <strong>ZIP</strong>, <strong>RAR</strong>.</p>
<h3>Tipos de Fichero según su uso</h3>
<p>Se pueden clasificar en:</p>
<ul><li>Ficheros <strong>Permanentes</strong>: Contienen los datos relevantes para una aplicación. Su vida es larga y no pueden generarse de forma inmediata. Entre estos se puede distinguir entre:
<ul><li>Ficheros <strong>maestros</strong>: contienen el estado actual de los datos suceptibles de ser modificados en la aplicación. Ejemplo: el fichero de clientes de un banco.</li>
<li>Ficheros <strong>constantes</strong>: contienen datos fijos para la aplicación. Ejemplo: el fichero de códigos postales.</li>
<li>Ficheros <strong>históricos</strong>: contienen datos que fueron actuales en tiempos anteriores. Ejemplo: el fichero de clientes que se han dado de baja.</li>
</ul></li>
<li>Ficheros <strong>Temporales</strong>: Contienen datos relevantes para un proceso o programa. Su vida es corta y se utilizan para actualizar los ficheros permanentes.
<ul><li>Ficheros de <strong>movimientos</strong>: almacenan resultados de un programa que han de ser utilizados por otro, dentro de la misma tarea. Ejemplo: el fichero de movimientos de una cuenta bancaria.</li>
<li>Ficheros de <strong>maniobras</strong>: almacenan datos que un programa no puede conservar en memoria principal por falta de espacio. Ejemplo: editores, compiladores y programas de cálculo numérico.</li>
<li>Ficheros de <strong>resultados</strong>: se utilizan para almacenar datos elaborados que van a ser transferidos a un dispositivo de salida. Ejemplo: un fichero de impresión.</li>
</ul></li>
</ul><h3>Denominación de Ficheros</h3>
<p>Los ficheros tienen asignados un nombre a través del cual los usuarios se refieren a ellos. Sin embargo, las reglas de denominación de ficheros difieren dependiendo del SO. Muchos SO dividen el nombre de los ficheros en dos partes separadas por un punto. La primera parte sería el nombre propiamente dicho. La segunda parte se suele denominar <em>extensión</em>&nbsp; y suele aportar información sobre el contenido del fichero.</p>
<p>Las reglas básicas de denominación de ficheros en los SO MS-DOS, UNIX y Windows NT son:</p>
<ul><li><strong>MS-DOS</strong>: El nombre de un fichero se compone de un máximo de 8 caracteres, seguidos, opcionalmente, por un punto y una extensión de tres caracteres como máximo. Las mayúsculas y minúsculas son consideradas iguales. Por ejemplo: <em>archivo12.doc</em>.</li>
<li><strong>UNIX</strong>: El nombre de un fichero se compone de un máximo de 256 caracteres. Se distinguen las mayúsculas de las minúsculas. Un fichero puede tener más de una extensión. Por ejemplo: <em>image.tar.z</em>.</li>
<li><strong>Windows NT</strong>: El nombre de un fichero se compone de un máximo de 256 caracteres. Las mayúsculas y minúsculas no son distinguibles y los ficheros pueden tener más de una extensión.</li>
</ul><p>En muchos casos, las extensiones son&nbsp; meras convenciones y no relacionadas con el contenido de los ficheros. Por otro lado, muchas aplicaciones requieren que los ficheros que utilizan tengan unas extensiones concretas.</p>
<h2 class="bio">Bibliografía</h2>
<ul class="bio"><li><a href="https://es.scribd.com/document/356393030/TICB1-Estructuras-de-Datos" rel="noopener" target="_blank">Scribd (Ibiza Ales)</a></li>
</ul> </article>

# Diseño de programas. Diseño estructurado. Análisis de transformación y de transacción. Cohesión y acoplamiento.

<article><h2>Introducción al Diseño Estructurado</h2>
<h3>Conceptos Generales Sobre el Diseño</h3>
<p>Definición: “Diseño es el proceso de aplicar distintas técnicas y principios con el propósito de definir un dispositivo, proceso, o sistema, con los suficientes detalles como para permitir su realización física”.</p>
<p>El objetivo del diseñador es producir un modelo de una entidad que se construirá más adelante. El proceso por el cual se desarrolla el modelo combina:</p>
<ul><li>La intuición y los criterios en base a la experiencia de construir entidades similares.</li>
<li>Un conjunto de principios y/o heurísticas que guían la forma en la que se desarrolla el modelo.</li>
<li>Un conjunto de criterios que permiten discernir sobre la calidad.</li>
<li>Un proceso de iteración que conduce finalmente a una representación del diseño final.</li>
</ul><p>La actividad de Diseño se dedica a asignar porciones de la especificación estructurada (también conocida como modelo esencial) a procesadores adecuados (sean máquinas o humanos) y a labores apropiadas (o tareas, particiones, etc) dentro de cada procesador. Dentro de cada labor, la actividad de diseño se dedica a la creación de una jerarquía apropiada de módulos de programas y de interfaces entre ellos para implantar la especificación creada en la actividad de análisis. Además, la actividad de diseño se ocupa de la transformación de modelos de datos de entidad/relación en un diseño de base de datos.</p>
<h3>¿Qué es Diseño Estructurado?</h3>
<p>Definición: “Diseño estructurado es el proceso de decidir qué componentes, y la interconexión entre los mismos, para solucionar un problema bien especificado”.</p>
<p>El diseño es una actividad que comienza cuando el analista de sistemas ha producido un conjunto de requerimientos funcionales lógicos para un sistema, y finaliza cuando el diseñador ha especificado los componentes del sistema y las relaciones entre los mismos.</p>
<p>Frecuentemente analista y diseñador son la misma persona, sin embargo es necesario que se realice un cambio de enfoque mental al pasar de una etapa a la otra. <em>Al abordar la etapa de diseño, la persona debe quitarse el sombrero de analista y colocarse el sombrero de diseñador</em>.</p>
<p>Una vez que se han establecido los requisitos del software (en el análisis), el diseño del software es la primera de tres actividades técnicas: <em>diseño</em>, <em>codificación</em> y <em>prueba</em>. Cada actividad transforma la información de forma que finalmente se obtiene un software para computadora válido.</p>
<p>En la figura se muestra el flujo de información durante la fase de desarrollo. Los requisitos del sistema, establecidos mediante los <em>modelos de información</em>, <em>funcional</em> y <em>de comportamiento</em>, alimentan el proceso del diseño. Mediante alguna metodología (en nuestro caso, estructurada basada en el flujo de información) se realiza el diseño estructural, procedimiental y de datos.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/flujo_informacion_fase_desarrollo.png?w=825"/></p>
<p>El <em>diseño de datos</em> transforma el modelo del campo de información, creado durante el análisis, en las estructuras de datos que se van a requerir para implementar el software.</p>
<p>El <em>diseño estructural</em> define las relaciones entre los principales elementos estructurales del programa. El objetivo principal del diseño estructural es desarrollar una estructura de programa modular y representar las relaciones de control entre los módulos.</p>
<p>El <em>diseño procedimental</em> transforma los elementos estructurales en una descripción procedimental del software. El diseño procedimental se realiza después de que se ha establecido la estructura del programa y de los datos. Define los algoritmos de procesamiento necesarios.</p>
<p>Concluido el diseño se genera el código fuente y para integrar y validar el software, se llevan a cabo pruebas de testeo.</p>
<p>Las fases del diseño, codificación y prueba absorben el 75% o más del coste de la ingeniería del software (excluyendo el mantenimiento). Es aquí donde se toman <em>decisiones</em> que afectarán finalmente al éxito de la implementación del programa y, con igual importancia, a la facilidad de mantenimiento que tendrá el software. Estas decisiones se llevan a cabo durante el diseño del software, haciendo que sea un paso <em>fundamental</em> de la fase de desarrollo.</p>
<p>La importancia del diseño del software se pueden sentar con una única palabra: <em>calidad</em>. El diseño es el proceso en el que se asienta la calidad del desarrollo del software. El diseño produce las representaciones del software de las que puede evaluarse su calidad. El diseño sirve como base para todas las posteriores etapas del desarrollo y de la fase de mantenimiento. Sin diseño nos arriesgamos a construir un sistema inestable, un sistema que falle cuando se realicen pequeños cambios, un sistema que pueda ser difícil de probar, un sistema cuya calidad no pueda ser evaluada hasta más adelante en el proceso de ingeniería de software, cuando quede poco tiempo y se haya gastado ya mucho dinero.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/con_disec3b1o_sin_disec3b1o.png?w=825"/></p>
<h3>Objetivos del Diseño Estructurado</h3>
<p><em>El diseño estructurado, tiende a transformar el desarrollo de software de una práctica artesanal a una disciplina de ingeniería.</em></p>
<ul><li>Eficiencia</li>
<li>Mantenibilidad</li>
<li>Modificabilidad</li>
<li>Flexibilidad</li>
<li>Generalidad</li>
<li>Utilidad</li>
</ul><p><em>“Diseño” significa planear la forma y método de una solución</em>. Es el proceso que&nbsp; determina las características principales del sistema final, establece los límites en performance y calidad que la mejor implementación puede alcanzar, y puede determinar a qué costos se alcanzará.</p>
<p>El diseño se caracteriza usualmente por un gran número de decisiones técnicas individuales. En orden de transformar el desarrollo de software en una disciplina de ingeniería, se debe sistematizar tales decisiones, hacerlas más explícitas y técnicas, y menos implícitas y artesanales.</p>
<p>Un ingeniero no busca simplemente <em>una</em> solución, busca la <em>mejor</em> solución, dentro de las <em>limitaciones</em> reconocidas, y realizando <em>compromisos</em>&nbsp;requeridos en el trabajo del mundo real.</p>
<p>En orden de convertir el diseño de sistemas de computadoras en una disciplina de ingeniería, previo a todo, debemos definir <em>objetivos técnicos claros</em> para los programas de computadora. Es esencial además comprender las <em>restricciones</em> primarias que condicionan las soluciones posibles.</p>
<p>Para realizar decisiones concisas y deliberadas, debemos identificar los <em>puntos de decisión</em>.</p>
<p>Finalmente necesitamos una <em>metodología</em> que nos asista en la <em>toma de decisiones</em>.</p>
<p>Dadas estas cosas: objetivos, restricciones, decisiones reconocidas, y una metodología efectiva, podemos obtener soluciones de ingeniería, y no artesanales.</p>
<p><strong><em>Diseño estructurado y calidad del software</em></strong></p>
<p>Un concepto importante a clarificar es el de <em>calidad</em>. Desafortunadamente, muchos diseñadores se conforman con un sistema que “funcione” sin reparar en un <em>buen</em> sistema.</p>
<p>Una corriente de pensamiento estima que un programa es bueno si sus algoritmos son astutos y no obvios a otro programador; esto refleja la “inteligencia” del programador.</p>
<p>Otra escuela de pensamiento asocia calidad con incremento de la velocidad de ejecución y disminución de los requerimientos de memoria central. Estos son aspectos de un concepto más amplio: <em>eficiencia</em>. En general, se busca diseños que hagan un uso inteligente de los <em>recursos</em>. Estos recursos no incluyen solamente procesador y memoria, también incluyen almacenamiento secundario, tiempo de periféricos de entrada/salida, tiempo de líneas de teleproceso, tiempo de personal y más.</p>
<p>Otra medida de calidad es la <em>confiabilidad</em>. Es importante notar que si bien la confiabilidad del software puede ser vista como un problema de depuración de errores en los programas, es también un problema de diseño. La confiabilidad se expresa en como MTBF (mean time between fairules: tiempo medio entre fallas).</p>
<p>Un concepto muy relacionado a la confiabilidad y de suma importancia es el de <em>mantenibilidad</em>. Podemos definir la mantenibilidad como:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/mantenibilidad.png?w=825"/></p>
<p>donde:</p>
<ul><li>MBTF: tiempo medio entre fallas.</li>
<li>MTTR: tiempo medio de reparación (mean time to repair).</li>
</ul><p>Diremos que un sistema es mantenible si permite la detección, análisis, rediseño y corrección de errores fácilmente.</p>
<p>En tanto la mantenibilidad afecta la viabilidad del sistema en un entorno relativamente constante, la <em>modificabilidad</em> influye en los costos de mantener un sistema viable en condiciones de cambio de requerimientos. La modificabilidad es la posibilidad de realizar modificaciones y extensiones a partes del sistema, o agregar nuevas partes con facilidad (no corrección de errores).</p>
<p>En estudios realizados se determinó que las organizaciones abocadas al procesamiento de datos invierten aproximadamente un 50% del presupuesto en mantenimiento de los sistemas, involucrando esto corrección de errores y modificaciones, razón por la cual la mantenibilidad y la modificabilidad son dos objetivos primarios en el diseño de software.</p>
<p>La <em>flexibilidad</em> representa la facilidad de que el mismo sistema pueda realizar variaciones sobre una misma temática, sin necesidad de modificaciones.</p>
<p>La <em>generalidad</em> expresa el alcance sobre un determinado tema.</p>
<p>Flexibilidad y generalidad son dos objetivos importantes en el diseño de sistemas del tipo de propósitos generales.</p>
<p>La <em>utilidad</em> o facilidad de uso es un factor importante que influye en el éxito del sistema y su aceptación por parte del usuario. Un sistema bien diseñado pero con interfaces muy “duras” tiende a ser resistido por los usuarios.</p>
<p>Finalmente diremos que eficiencia, mantenibilidad, modificabilidad, flexibilidad, generalidad y utilidad, con componentes de la <em>calidad</em> objetiva de un sistema.</p>
<p>En términos simples también diremos que nuestro objetivo primario es obtener sistemas de <em>costo mínimo</em>. Es decir, es nuestro interés obtener sistemas económicos para desarrollar, operar, mantener y modificar.</p>
<h3>Restricciones, compromisos y decisiones del Diseño</h3>
<p>Podemos ver los objetivos técnicos del diseño como constituyendo una “función objetivo” de un problema de optimización, la cual se desea maximizar, sujeta a ciertas restricciones.</p>
<p>Como regla, las restricciones sobre un proceso de diseño de un sistema, caen en dos categorías: <em>restricciones de desarrollo</em> y <em>restricciones operacionales</em>.</p>
<p>Las <strong>restricciones de desarrollo</strong> son limitaciones al consumo de recursos durante el período de desarrollo, y pueden ser expresadas en términos generales o descomponerla en sus partes como ser tiempo de máquina y horas/hombre. Dentro de las restricciones de desarrollo, entran también las <em>restricciones de planificación</em>. Estas se refieren a metas y plazos a ser cumplidos (“el módulo X debe terminarse para Febrero”).</p>
<p>Las <strong>restricciones operacionales</strong> pueden ser expresadas en términos técnicos, como ser máximo tamaño de memoria disponible, máximo tiempo de respuesta aceptable, etc.</p>
<p>El carácter de muchas decisiones de diseño no fija límites rígidos, si no un intervalo de tolerancia, dentro del cual el diseñador puede moverse a costa de variaciones en otros aspectos del sistema. Por ejemplo se puede priorizar eficiencia, en detrimento de facilidad de mantenimiento, o velocidad de ejecución contra tamaño de memoria utilizada.</p>
<p>La esencia del diseño en el mundo real y las decisiones inherentes al mismo es obtener una solución de <em>compromiso</em>.</p>
<p>El diseño total es el resultado acumulativo de un gran número de <em>decisiones técnicas</em> incrementales.</p>
<h3>Principios utilizados por el Diseño Estructurado</h3>
<p><strong>Abstracción</strong></p>
<p>La noción psicológica de abstracción permite concentrarse en un problema al mismo nivel de generalización, independientemente de los detalles irrelevantes de bajo nivel. El uso de la abstracción también permite trabajar con conceptos y términos que son familiares al entorno del problema, sin tener que transformarlos a una estructura no familiar.</p>
<p>Cada paso de un proceso de ingeniería de software es un refinamiento del nivel de abstracción de la solución de software.</p>
<p>Conforme nos movemos por diferentes niveles de abstracción, trabajamos para crear <em>abstracciones</em> de datos y de procedimientos. Una <em>abstracción procedural</em> es una determinada secuencia de instrucciones que tienen una función limitada y específica.</p>
<p>Una <em>abstracción de datos</em> es una determina colección de datos que describen un objeto.</p>
<ul><li><strong>Rumbaugh: O.O. Modeling and Design</strong><br/><em>La abstracción es el exámen selectivo de ciertos aspectos de un problema</em>. El objetivo de la abstracción es aislar aquellos aspectos que son importantes para algún propósito y suprimir aquellos aspectos que no son importantes. La abstracción debe realizarse siempre con un propósito, ya que el propósito determina que es y que no es relevante. Muchas abstracciones son posibles sobre una misma cosa, dependiendo de cual sea su propósito.</li>
<li><strong>Alan Cameron Will (Object Expert Jan/Feb 1996)</strong><br/><em>La abstracción, para mí, es cercana a palabras como “teórico”, “esotérico”, “académico”, e “impráctico”. Pero en un sentido en particular, significa la separación de los aspectos más importantes de un determinado problema, del detalle. Este el el único camino que tengo para abordar con mi mente finita cualquier tema complejo</em>.</li>
</ul><p><strong>Refinamiento sucesivo</strong></p>
<p>El <em>refinamiento sucesivo</em> es una primera estrategia de diseño descendente propuesta por Niclaus Wirth. La arquitectura de un programa se desarrolla en niveles sucesivos&nbsp; de refinamiento de los detalles procedimentales. Se desarrolla una jerarquía descomponiendo una declaración macroscópica de una función de una forma sucesiva, hasta que se llega a las sentencias del lenguaje de programación.</p>
<p><strong>Modularidad</strong></p>
<p>La arquitectura implica modularidad, el software se divide en componentes con nombres y ubicaciones determinados, que se denominan <em>módulos</em>, y que se integran para satisfacer los requisitos del problema.</p>
<p><strong>Arquitectura del software</strong></p>
<p>La <em>arquitectura del software</em> se refiere a dos características importantes del software de computadoras:</p>
<ul><li>la estructura jerárquica de los componentes procedimientales (módulos)</li>
<li>la estructura de datos</li>
</ul><p><strong>Jerarquía de control</strong></p>
<p>La <em>jerarquía de control</em>, también denominada <em>estructura de programa</em>, representa la organización (frecuentemente jerárquica) de los componentes del programa (módulos) e implica una jerarquía de control. No representa aspectos procedimentales del software, tales como secuencias de procesos, o la repetición de operaciones.</p>
<p><strong>Estructura de datos</strong></p>
<p>La <em>estructura de datos</em> es una representación de la relación lógica existente entre los elementos individuales de datos. Debido a que la estructura de la información afectará invariablemente al diseño procedimental final, la estructura de datos es tan importante como la estructura del programa en la representación de la arquitectura del software.</p>
<p><strong>Procedimientos del software</strong></p>
<p>La estructura del programa define la jerarquía de control, independientemente de las decisiones y secuencias de procesamiento. El procedimiento del software se centra sobre los detalles de procesamiento de cada módulo individual.</p>
<p>El procedimiento debe proporcionar una especificación precisa del procesamiento, incluyendo la secuencia de sucesos, los puntos concretos de decisiones, la repetición de operaciones, e incluso la organización/estructura de los datos.</p>
<p><strong>Ocultamiento de la información</strong></p>
<p>El principio de <em>ocultamiento de la información</em> sugiere que los módulos se han de caracterizar por decisiones de diseño que los oculten unos a otros. Los módulos deben especificarse y diseñarse de forma que la información (procedimientos y datos) contenida dentro de un módulo sea accesible a otros módulos únicamente a través de las <em>interfaces</em> formales establecidas para cada módulo.</p>
<h2>Conceptos Básicos de Diseño Estructurado</h2>
<h3>Estrategia del Diseño Estructurado</h3>
<p>Cuando se trata con un problema de diseño de reducida envergadura, por ejemplo un sistema que pueda ser desarrollado en un par de semanas,no se tienen mayores problemas, y el desarrollador puede tener todos los elementos del problema “en mente” a la vez. Sin embargo cuando se trabaja en proyectos de gran escala, es difícil que una sola persona sea capaz de llevar todas las tareas y tener en mente todos los elementos a la vez.</p>
<p>El diseño exitoso se basa en un viejo principio conocido desde los días de Julio César: <em>Divide y conquistarás</em>.</p>
<p>Específicamente, diremos que el costo de implementación de un sistema de computadora podrá minimizarse cuando pueda separarse en partes:</p>
<ul><li><em>manejablemente pequeñas</em></li>
<li><em>solucionables separadamente</em></li>
</ul><p>Por supuesto la interpretación de manejablemente pequeña varía de persona en persona. Por otro lado muchos intentos de particionar sistemas en pequeñas partes arribaron incrementos en los tiempos de implementación. Esto se debe fundamentalmente al segundo punto: solucionables separadamente. En muchos sistemas para implementar la parte A, debemos conocer algo sobre la B, y para implementar algo de B, debemos conocer algo de C.</p>
<p>De manera similar, podemos decir que el costo de <em>mantenimiento</em> puede ser minimizado cuando las partes de un sistema son:</p>
<ul><li><em>fácilmente relacionables con la aplicación</em></li>
<li><em>manejablemente pequeñas</em></li>
<li><em>corregibles separadamente</em></li>
</ul><p>Muchas veces la persona que realiza la modificación no es quien diseñó el sistema. Es importante que las partes de un sistema sean manejablemente pequeñas en orden de simplificar el mantenimiento. Un trabajo de encontrar y corregir un error en una “pieza” de código de 1000 líneas es muy superior a hacerlo con piezas de 20 líneas. No solo disminuye el tiempo de localizar la falla sino que si la modificación es muy engorrosa, puede reescribirse la pieza completamente. Este concepto de “módulos descartables” ha sido utilizado con éxito muchas veces.</p>
<p>Por otra parte, para minimizar los costos de mantenimiento debemos lograr que cada pieza sea independiente de otra. En otras palabras debemos ser capaces de realizar modificaciones al módulo A sin introducir efectos indeseados en el módulo B.</p>
<p>Finalmente, diremos que el costo de <em>modificación</em> de un sistema puede minimizarse si sus partes son:</p>
<ul><li><em>fácilmente relacionables con la aplicación</em></li>
<li><em>modificables separadamente</em></li>
</ul><p>En resumen, podemos afirmar lo siguiente: los costos de implementación, mantenimiento y modificación, generalmente serán minimizados cuando <em>cada pieza del sistema corresponda a exactamente una pequeña, bien definida pieza del dominio del problema, y cada relación entre las piezas del sistema corresponde a relaciones entre piezas del dominio del problema</em>.</p>
<p>En la siguiente figura apreciamos este concepto.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/dominio_problema.png?w=825"/></p>
<h3>Particionamiento y Organización</h3>
<p>Un buen diseño estructurado es un ejercicio de particionamiento y organización de los componentes de un sistema.</p>
<p>Entenderemos por particionamiento, la subdivisión de un problema en subproblemas más pequeños, de tal forma que cada subproblema corresponda a una pieza del sistema. La cuestión es: ¿Dónde y cómo debe dividirse el problema? ¿Qué aspectos del problema deben pertenecer a la misma pieza del sistema, y cuales a distintas piezas? El diseño estructurado responde estas preguntas con dos principios básicos:</p>
<ul><li><em>Partes del problema altamente interrelacionadas deberán pertenecer a la misma pieza del sistema</em>.</li>
<li><em>Partes sin relación entre ellas, deben pertenecer a diferentes piezas del sistema sin relación directa</em>.</li>
</ul><p>Otro aspecto importante del diseño estructurado es la organización del sistema. Debemos decidir como se interrelacionan las partes, y que parte está en relación con cual.</p>
<p>El objetivo es organizar el sistema de tal forma que no existan piezas más grandes de lo estrictamente necesario para resolver los aspectos del problema que ella abarca. Igualmente importante, es el evitar la introducción de relaciones en el sistema, que no existe en el dominio del problema.</p>
<h3>El concepto de Cajas Negras</h3>
<p>Una caja negra es un sistema (o un componente) con entradas conocidas, salidas conocidas, y generalmente transformaciones conocidas, pero del cual no se conoce el contenido en su interior.</p>
<p>En la vida diaria existe innumerable cantidad de ejemplos de uso cotidiano: una radio, un televisor, un automóvil, son cajas negras que usamos a diario sin conocer (en general) como funciona en su interior. Solo conocemos como controlarlos (entradas) y las respuestas que podemos obtener de los artefactos (salidas).</p>
<p>El concepto de caja negra utiliza el principio de <em>abstracción</em>.</p>
<p>Este concepto es de suma utilidad e importancia en la ingeniería en general, y por ende en el desarrollo de software. Lamentablemente muchas veces para poder hacer un uso efectivo de determinado módulo, el diseñador debe revisar su contenido ante posibles contingencias como ser comportamientos no deseados ante determinados valores. Por ejemplo es posible que una rutina haya sido desarrollada para aceptar un determinado rango de valores y falla si se la utiliza con valores fuera de dicho rango, o produce resultados inesperados. Una buena documentación en tales casos, es de utilidad pero no transforma al módulo en una verdadera caja negra. Podríamos hablar en todo caso de “cajas blancas”.</p>
<p>Los módulos de programas de computadoras pueden variar en un amplio rango de aproximación al ideal de caja negra. En la mayoría de los casos podemos hablar de “cajas grises”.</p>
<h2>La Estructura de los Programas de Computadora</h2>
<h3>Diagramas de Flujo y Diagramas de Estructura</h3>
<p>Normalmente los procedimientos se representan con <em>diagramas de flujo</em> (no confundir con diagramas de flujo de datos) los cuales modelan la secuencia de operaciones que realiza el programa a través del tiempo.</p>
<p>Un <em>diagrama de estructura</em> en cambio no modela la secuencia de ejecución sino la <em>jerarquía de control</em> existente entre los módulos que conforman el programa, independientemente del factor tiempo. Existe un módulo raíz de máximo nivel, del cual dependen los demás, en una estructura arborescente.</p>
<h3>Notación de los Diagramas de Flujo de Control</h3>
<p><img src="https://gsitic.files.wordpress.com/2018/04/notacion_diagramas_flujo_control.png?w=825"/></p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/construcciones_estructuradas.png?w=825"/></p>
<h3>Notación de los Diagramas de Estructura</h3>
<p><img src="https://gsitic.files.wordpress.com/2018/04/notacion_diagramas_estructura.png?w=825"/></p>
<h3>Ejemplo comparativo entre Diagramas de Procesamiento y de Estructura</h3>
<p><img src="https://gsitic.files.wordpress.com/2018/04/diagrama_flujo.png?w=825"/><img src="https://gsitic.files.wordpress.com/2018/04/diagrama_estructura.png?w=825"/></p>
<h2>Acoplamiento</h2>
<h3>Introducción</h3>
<p>Muchos aspectos de la modularización pueden ser comprendidos solo si se examinan módulos en relación con otros. En principio veremos el concepto de <em>independencia</em>: diremos que dos módulos son totalmente independientes si ambos pueden funcionar completamente sin la presencia del otro. Esto implica que no existen interconexiones entre los módulos, y que se tiene un valor cero en la escala de “dependencia”.</p>
<p>En general veremos que a mayor número de interconexiones entre dos módulos, se tiene una menor independencia.</p>
<p>El concepto de independencia funcional es una derivación directa del de modularidad y de los conceptos de abstracción y ocultamiento de la información.</p>
<p>La cuestión aquí es: ¿cuánto debe conocerse acerca de un módulo para poder comprender otro módulos? Cuanto más debamos conocer acerca del módulo B para poder comprender el módulo A, menos independientes serán A y B.</p>
<p>La simple cantidad de conexiones entre módulos, no es una medida completa de la independencia funcional. La dependencia funcional se mide con dos criterios cualitativos: <em>acoplamiento</em> y <em>cohesión</em>. Estudiaremos en principio el primero de ellos.</p>
<p>Módulos altamente “acoplados” estarán unidos por fuertes interconexiones, módulos débilmente acoplados tendrán pocas y débiles interconexiones, en tanto que los módulos “desacoplados” no tendrán interconexiones entre ellos y serán independientes.</p>
<blockquote><p>El <em>acoplamiento</em> es un concepto abstracto que nos indica el grado de interdependencia entre módulos.</p></blockquote>
<p>En la práctica podemos materializarlo como la probabilidad de que en la codificación, depuración, o modificación de un determinado módulo, el programador necesite tomar conocimiento acerca de partes de otro módulo. Si dos módulos están fuertemente acoplados, existe una alta probabilidad de que el programador necesite conocer uno de ellos en orden de intentar realizar modificaciones al otro.</p>
<p>Claramente, el costo total del sistema se verá fuertemente influenciado por el grado de acoplamiento entre módulos.</p>
<h3>Factores que influencian el Acoplamiento</h3>
<p>Los cuatro factores principales que influyen en el acoplamiento entre módulos son:</p>
<ul><li><em>Tipo de conexión entre módulos</em>: los sistemas normalmente conectados, tienen menor acoplamiento que aquellos que tienen conexiones patológicas.</li>
<li><em>Complejidad de la interface</em>: está determinada por la cantidad, accesibilidad y estructura de la información que define la interface.</li>
<li><em>Tipo de flujo de información en la conexión</em>: los sistemas con acoplamiento de datos tienen menor acoplamiento que los sistema con acoplamiento de control y estos a su vez menos que los que tienen acoplamiento híbrido.</li>
<li><em>Momento en que se produce el ligado de la Conexión</em>: conexiones ligadas a referentes fijos en tiempo de ejecución, resultan con menor acoplamiento que cuando el ligado tiene lugar en tiempo de carga, el cual tiene a su vez menor acoplamiento que cuando el ligado se realiza en tiempo de ligado (link-edición), el cual tiene menos acoplamiento que el que se realiza en tiempo de compilación, todos los que a su vez tiene menos acoplamiento que cuando el ligado se realiza en tiempo de codificación.</li>
</ul><h3>Acoplamiento en Entorno Común (common-environment coupling)</h3>
<p>Siempre que dos o más módulos interactúan con un entorno de datos común, se dice que dichos módulos están en <em>acoplamiento por entorno común</em>.</p>
<p>Ejemplos de entorno común pueden ser áreas de datos globales como la DATA DIVISION de COBOL, un archivo en disco.</p>
<p>El acoplamiento de entorno común es una forma de acoplamiento de segundo orden, distinto de los tratados anteriormente. La severidad del acoplamiento dependerá de la cantidad de módulos que acceden simultáneamente al entorno común. En el caso extremo de solo dos módulos donde uno utiliza como entrada los datos generados por el otro hablaremos de un acoplamiento de <em>entrada/salida</em>.</p>
<p>El punto es que el acoplamiento por entorno común no es necesariamente malo y deba ser evitado a toda costa. Por el contrario existen ciertas circunstancias en que es una opción válida.</p>
<h3>Desacoplamiento</h3>
<p>El concepto de acoplamiento invita a un concepto recíproco: <em>desacoplamiento</em>.</p>
<p>Desacoplamiento es cualquier método sistemático o técnica para hacer más independientes a los módulos de un programa.</p>
<p>Cada tipo de acoplamiento generalmente sugiere un método de desacoplamiento. Por ejemplo, el acoplamiento causado por ligado, puede desacoplarse cambiando los parámetros apropiados.</p>
<p>El desacoplamiento desde el punto de vista funcional, rara vez puede realizarse, excepto en los comienzos de la fase del diseño.</p>
<p>Como regla general, una disciplina de diseño que favorezca el acoplamiento de entrada/salida y el acoplamiento de control por sobre el acoplamiento por contenido y el acoplamiento híbrido, y que busque limitar el alcance del acoplamiento por entorno común es el enfoque más efectivo.</p>
<p>Otras técnicas para reducir el acoplamiento son:</p>
<ul><li>Convertir las referencias implícitas en explícitas. Lo que puede verse con mayor facilidad es más fácil de comprender.</li>
<li>Estandarización de las conexiones.</li>
<li>Uso de “buffers” para los elementos comunicados en una conexión. Si un módulo puede ser diseñado desde el comienzo asumiendo que un buffer mediará cada corriente de comunicación, las cuestiones temporización, velocidad, frecuencia, etc, dentro de un módulo no afectarán al diseño de otros.</li>
<li>Localización. Utilizado para reducir el acoplamiento por entorno común. Consiste en dividir el área común en regiones para que los módulos solo tengan acceso a aquellos datos que les son de su estricta incumbencia.</li>
</ul><h2>Cohesión</h2>
<h3>Introducción: Relación Funcional</h3>
<p>Hemos visto que la determinación de módulos en un sistema no es arbitraria. La manera en la cual dividimos físicamente un sistema en piezas (particularmente en relación con la estructura del problema) puede afectar significativamente la complejidad estructural del sistema resultante, así como el número total de referencias intermodulares.</p>
<p>Adaptar el diseño del sistema a la estructura del problema (o estructura de la aplicación, o dominio del problema) es una filosofía de diseño sumamente importante. A menudo encontramos que elementos de procesamiento del dominio del problema altamente relacionados, son trasladados en código altamente interconectado. Las estructuras que agrupan elementos del problema altamente interrelacionados, tienden a ser modularmente efectivas.</p>
<p>Imaginemos que tengamos una magnitud para medir el grado de relación funcional existente entre pares de módulos. En términos de tal medida, diremos que el sistema más modularmente efectivo será aquel cuya suma de relación funcional entre pares de elementos que pertenezcan a diferentes módulos sea mínima. Entre otras cosas, esto tiende a minimizar el número de conexiones intermodulares requeridas y el acoplamiento intermodular.</p>
<blockquote><p>Esta relación funcional intramodular se conoce como <em>cohesión</em>. La cohesión es la medida cualitativa de cuan estrechamente relacionados están los elementos internos de un módulo.</p></blockquote>
<p>Otros términos utilizados frecuentemente son “fuerza modular”, “ligazón” y “funcionalidad”.</p>
<p>En la práctica un elemento de procesamiento simple aislado, puede estar funcionalmente relacionado en diferentes grados a otros elementos. Como consecuencia, diferentes diseñadores, con diferentes “visiones” o interpretaciones de un mismo problema, pueden obtener diferentes estructuras modulares con diferentes niveles de cohesión y acoplamiento. A esto se suma el inconveniente de que muchas veces es difícil evaluar el grado de relación funcional de un elemento respecto de otro.</p>
<p>La cohesión modular puede verse como el cemento que amalgama junto a los elementos de procesamiento dentro de un mismo módulo. Es el factor más crucial en el diseño estructurado, y el de mayor importancia en un diseño modular efectivo.</p>
<p>Este concepto representa la técnica principal que posee un diseñador para mantener su diseño lo más semánticamente próximo al problema real, o dominio del problema.</p>
<p>Claramente los conceptos de cohesión y acoplamiento están íntimamente relacionados. Un mayor grado de cohesión implica uno menor de acoplamiento. Maximizar el nivel de cohesión intramodular en todo el sistema resulta en una minimización del acoplamiento intermodular.</p>
<h3>Niveles de Cohesión</h3>
<p>Diferentes principios asociativos fueron desenvolviéndose a través de los años por medio de la experimentación, argumentos teóricos, y la experiencia práctica de muchos diseñadores.</p>
<p>Existen siete niveles de cohesión distinguibles por siete principios asociativos. Estos se listan a continuación en orden creciente del grado de cohesión, de menor a mayor relación funcional:</p>
<ul><li>Cohesión Casual (la peor)</li>
<li>Cohesión Lógica (sigue a la peor)</li>
<li>Cohesión Temporal (de moderada a pobre)</li>
<li>Cohesión de Procedimiento (moderada)</li>
<li>Cohesión de Comunicación (moderada a buena)</li>
<li>Cohesión Secuencial</li>
<li>Cohesión Funcional (la mejor)</li>
</ul><p>Podemos visualizar el grado de cohesión como un espectro que va desde un máximo a un mínimo.</p>
<p><strong>Cohesión Casual (la peor)</strong></p>
<p>La <em>cohesión casual</em> ocurre cuando existe poca o ninguna relación entre los elementos de un módulo.</p>
<p>La cohesión casual establece un punto cero en la escala de cohesión.</p>
<p>Es muy difícil encontrar módulos puramente casuales. Puede aparecer como resultado de la modularización de un programa ya escrito, en el cual el programador encuentra una determinada secuencia de instruccciones que se repiten de forma aleatoria, y decide por lo tanto agruparlas en una rutina.</p>
<p>Otro factor que influenció muchas veces la confección de módulos casualmente cohesivos, fue la mala práctica de la programación estructurada, cuando los programadores mal entendían que modularizar consistía en cambiar las sentencias GOTO por llamadas a subrutinas.</p>
<p>Finalmente diremos que si bien en la práctica es difícil encontrar módulos casualmente cohesivos en su totalidad, es común que tengan elementos casualmente cohesivos. Tal es el caso de operaciones de inicialización y terminación que son puestas juntas en un módulo superior.</p>
<p>Debemos notar que si bien la cohesión casual no es necesariamente perjudicial (de hecho es preferible un casualmente cohesivo a uno lineal), dificulta las modificaciones y mantenimiento del código.</p>
<p><strong>Cohesión Lógica (sigue a la peor)</strong></p>
<p>Los elementos de un módulo están <em>lógicamente</em> asociados si puede pensarse en ellos como pertenecientes a la misma clase lógica de funciones, es decir, aquellas que pueden pensarse como juntas lógicamente.</p>
<p>Por ejemplo, se puede combinar en un módulo simple todos los elementos de procesamiento que caen en la clase de “entradas”, que abarca todas las operaciones de entrada.</p>
<p>Podemos tener un módulo que lea desde consola una tarjeta con parámetros de control, registros con transacciones erróneas de un archivo en cinta, registros con transacciones válidas de otro archivo en cinta, y los registros maestros anterior de un archivo en disco. Este módulo que podría llamarse “Lecturas”, y que agrupa todas las operaciones de entrada, es lógicamente cohesivo.</p>
<p>La cohesión lógica es más fuerte que la casual, debido a que representa un mínimo de asociación entre el problema y los elementos del módulo. Sin embargo podemos ver que un módulo lógicamente cohesivo no realiza una función específica, sino que abarca una serie de funciones.</p>
<p><strong>Cohesión Temporal (de moderada a pobre)</strong></p>
<p><em>Temporal cohesión</em> significa que todos los elementos de procesamiento de una colección ocurren en el mismo periodo de tiempo durante la ejecución del sistema. Debido a que dicho procesamiento debe o puede realizarse en el mismo periodo de tiempo, los elementos asociados temporalmente pueden combinarse en un único módulo que los ejecute a la misma vez.</p>
<p>Existe una relación entre cohesión lógica y la temporal, sin embargo, la primera no implica una relación de tiempo entre los elementos de procesamiento. La cohesión temporal es más fuerte que la cohesión lógica, ya que implica un nivel de relación más: el factor tiempo. Sin embargo la cohesión temporal aún es pobre en nivel de cohesión y acarrea inconvenientes en el mantenimiento y modificación del sistema.</p>
<p>Un ejemplo común de cohesión temporal son las rutinas de inicialización (start-up) comúnmente encontradas en la mayoría de los programas, donde se leen parámetros de control, se abren archivos, se inicializan variables contadores y acumuladores, etc.</p>
<p><strong>Cohesión de Procedimiento (moderada)</strong></p>
<p>Elementos de procesamiento relacionados <em>proceduralmente</em> son elementos de una unidad procedural común. Estos se combinan en un módulo de cohesión procedural. Una unidad procedural común puede ser un proceso de iteración (loop) y de decisión, o una secuencia lineal de pasos. En este último caso la cohesión es baja y es similar a la cohesión temporal, con la diferencia que la cohesión temporal no implica una determinada secuencia de ejecución de los pasos.</p>
<p>Al igual que en los casos anteriores, para decir que un módulo tiene <em>solo</em> cohesión procedural, los elementos de procesamiento deben ser elementos de alguna iteración, decisión, o secuencia, pero no deben estar vinculados con ningún principio asociativo de orden superior.</p>
<p>La cohesión procedural asocia elementos de procesamiento sobre la base de sus relaciones algorítmicas o procedurales.</p>
<p>Este nivel de cohesión comúnmente se tiene como resultado de derivar una estructura modular a partir de modelos de procedimiento como ser diagramas de flujo, o diagramas Nassi-Shneiderman.</p>
<p><strong>Cohesión de Comunicación (moderada a buena)</strong></p>
<p>Ninguno de los niveles de cohesión discutidos previamente están fuertemente vinculados a una estructura de problema en particular. <em>Cohesión de Comunicación</em> es el menor nivel en el cual encontramos una relación entre los elementos de procesamiento que es intrínsecamente <em>dependiente del problema.</em></p>
<p>Decir que un conjunto de elementos de procesamiento están vinculados por comunicación significa que <em>todo los elementos operan sobre el mismo conjunto de datos de entrada o de salida</em>.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/cohesion_comunicacion.png?w=825"/></p>
<p>En el diagrama de la figura podemos observar que los elementos de procesamiento 1, 2 y 3 están asociados por comunicación sobre la corriente de datos de entrada, en tanto que 2, 3 y 4 se vinculan por los datos de salida.</p>
<p>Los diagramas de flujo de datos (DFD) son un medio objetivo para determinar si los elementos en un módulo están asociados por comunicación.</p>
<p>Las relaciones por comunicación presentan un grado de cohesión aceptable.</p>
<p>La cohesión por comunicación es común en aplicaciones comerciales. Ejemplos típicos pueden ser:</p>
<ul><li>un módulo que imprima o grabe un archivo de transacciones</li>
<li>un módulo que reciba datos de diferentes fuentes y los transforme y ensamble en una línea de impresión</li>
</ul><p><strong>Cohesión Secuencial</strong></p>
<p>El siguiente nivel de cohesión en la escala es la asociación <em>secuencial</em>. En ella, los datos de salida (resultados) de un elemento de procesamiento sirven como datos de entrada al siguiente elemento de procesamiento.</p>
<p>En términos de un diagrama de flujo de datos de un problema, la cohesión secuencial combina una cadena lineal de sucesivas transformaciones de datos.</p>
<p>Este es claramente un principio asociativo relacionado con el dominio del problema.</p>
<p><strong>Cohesión Funcional (la mejor)</strong></p>
<p>En el límite superior del espectro de relación funcional encontramos la cohesión funcional. En un módulo completamente funcional, cada elemento de procesamiento, es parte integral de, y esencial para, la realización de una función simple.</p>
<p>En términos prácticos podemos decir que cohesión funcional es aquella que no es secuencial, por comunicación, por procedimiento, temporal, lógica o casual.</p>
<p>Los ejemplos más claros y comprensibles provienen del campo de las matemáticas. Un módulo para realizar el cálculo de raíz cuadrada ciertamente será altamente cohesivo, y probablemente, completamente funcional. Es improbable que haya elementos superfluos más allá de los absolutamente esenciales para realizar la función matemática, y es improbable que elementos de procesamiento puedan ser agregados sin alterar el cálculo de alguna forma.</p>
<p>En contraste, un módulo que calcule la raíz cuadrada y coseno, es improbable que sea enteramente funcional (deben realizarse dos funciones ambiguas).</p>
<p>En adición a estos ejemplos matemáticos obvios, usualmente podemos reconocer módulos funcionales que son elementales en naturaleza. Un módulo llamado LEER-REGISTRO-MAESTRO o TRATAR-TRANS-TIPO3, presumiblemente serán funcionalmente cohesivos, en cambio TRATAR-TODAS-TRANS presumiblemente realizará más de una función y será lógicamente cohesivo.</p>
<h3>Criterios para establecer el grado de cohesión</h3>
<p>Una técnica útil para determinar si un módulo está acotado funcionalmente, es escribir una frase que describa la función (propósito) del módulo y luego examinar dicha frase. Puede hacerse la siguiente prueba:</p>
<ol><li>Si la frase resulta ser una sentencia compuesta, contiene una coma, o contiene más de un verbo, probablemente el módulo realiza más de una función: por tanto, probablemente tienen vinculación secuencial o de comunicación.</li>
<li>Si la frase contiene palabras relativas al tiempo, tales como “primero”, “a continuación”, “entonces”, “después”, “cuando”, “al comienzo”, etc, entonces probablemente el módulo tiene una vinculación secuencial o temporal.</li>
<li>Si el predicado de la frase no contiene un objeto específico sencillo a continuación del verbo, probablemente el módulo esté acotado lógicamente. Por ejemplo <em>editar todos los datos</em> tiene una vinculación lógica; <em>editar sentencia fuerte</em> puede tener vinculación funcional.</li>
<li>Palabras tales como “inicializar”, “limpiar”, etc, implican vinculación temporal.</li>
</ol><p>Los módulos acotados funcionalmente siempre se pueden describir en función de sus elementos usando una sentencia compuesta. Pero si no se puede evitar el lenguaje anterior, siendo aún una descripción completa de la función del módulo, entonces probablemente el módulo no esté acotado funcionalmente.</p>
<p>Es importante notar que no es necesario determinar el nivel preciso de cohesión. En su lugar, lo importante es intentar conseguir una cohesión alta y saber reconocer la cohesión baja, de forma que se pueda modificar el diseño del software para que disponga de una mayor independencia funcional.</p>
<p><strong>Árbol de valuación</strong></p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/arbol_de_evaluacion.png?w=825"/></p>
<h2>Análisis de Transformación</h2>
<h3>Introducción</h3>
<blockquote>
<p>El <em>Análisis de Transformación, o diseño centrado en la transformación</em>, es una estrategia para derivar diseños estructurados que son bastante buenos (con respecto a su modularidad) y que necesitan solo una modesta reestructuración para llegar al diseño final.</p>
</blockquote>
<p>Es una forma particular de la estrategia descendente (top-down),&nbsp; que toma ventaja de la perspectiva global. Aplicado rigurosamente, el análisis de transacción conduce a estructuras que son altamente factorizadas. Produce un número variable de módulos en los niveles intermedios de la jerarquía, los cuales representan composición de funciones básicas. Siempre se trata de evitar que los módulos intermedios realicen cualquier “trabajo” excepto el de control y coordinación de sus subordinados.</p>
<p>El propósito de la estrategia es el de identificar las funciones de procesamiento primarias del sistema, las entradas de alto nivel de dichas funciones, y las salidas de alto nivel. Se crean módulos de alto nivel dentro de la jerarquía que realizan cada una de estas tareas: creación de entradas de alto nivel, transformación de entradas en salidas de alto nivel, y procesamiento de dichas salidas.</p>
<blockquote><p>El análisis de transformación es un modelo de <em>flujo de información</em> más que un modelo procedural.</p></blockquote>
<p>La estrategia de análisis de transformación consiste de <strong>cuatro pasos</strong> principales:</p>
<ol><li>Plantear el problema como un diagrama de flujo de datos.</li>
<li>Identificar los elementos de datos aferentes y eferentes.
<ul><li><em>Datos Aferentes</em>.<br/>
Son aquellos elementos de datos de alto nivel que habiendo sido removidos de sus entradas físicas, todavía pueden considerarse entradas al sistema.</li>
<li><em>Datos Eferentes</em>.<br/>
Son elementos de datos que desde sus salidas física a través de los flujos, hasta que no puedan seguir siendo considerados como datos de salida del sistema.</li>
</ul></li>
<li>Factorización del primer nivel.</li>
<li>Factorización de las ramas aferente, eferente y de transformación.</li>
</ol><h2>Análisis de Transacción</h2>
<h3>Introducción</h3>
<p>En el anterior capítulo exploramos la estrategia del análisis de transformación como la estrategia principal para el diseño de programas y sistemas bien estructurados. En verdad, el análisis de transformación, servirá de guía en el diseño de la mayoría de los sistemas. Sin embargo hay numerosas situaciones en las cuales estrategias adicionales pueden utilizarse para suplementar, y aún reemplazar, el enfoque básico del análisis de transformación.</p>
<p>Una de estas estrategias suplementarias principales se conoce como <em>Análisis de Transacción</em>.</p>
<p>El análisis de transacción es sugerido por un DFD del siguiente tipo:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/04/analisis_transaccic3b3n.png?w=825"/></p>
<p>En este DFD existe una transformación que bifurca la corriente de datos de entrada en varias corrientes de salida discretas. En muchos sistemas tal transformación puede ocurrir dentro de la transformación <em>central</em>. En otros, podremos encontrarla tanto en las ramas aferentes como eferentes del diagrama de estructura.</p>
<p>La frase análisis de transacción sugiere que construiremos un sistema alrededor del concepto de “transacción”, y para muchos la palabra transacción está asociada con sistemas administrativos. Esto si bien es cierto, es común encontrar centros de transacción en los sistemas administrativos, también pueden encontrarse en otro tipo de sistemas como los de tiempo real, aplicaciones de ingeniería, etc.</p>
<p>Un factor importante es como definimos el término transacción. En el sentido más general podemos decir:</p>
<blockquote><p><em>Una transacción es cualquier elemento de datos, control, señal, evento, o cambio de estado, que causa, dispara o inicia alguna acción o secuencia de acciones.</em></p></blockquote>
<p>Acorde a esta definición, un gran número de situaciones encontradas en aplicaciones de procesamiento de datos comunes pueden ser consideradas transacciones. Por ejemplo cualquiera de los siguientes casos pueden considerarse transacciones:</p>
<ul><li>El operador presiona el botón de inicio de un dispositivo de entrada.</li>
<li>Algún tipo de datos de entrada que designe un ingreso en el inventario.</li>
<li>Un carácter de escape desde una terminal, indicando la necesidad e un procesamiento especial.</li>
<li>Una interrupción de hardware ante un índice fuera de los rangos definidos dentro de un programa de aplicación.</li>
<li>Un cuelgue o descuelgue de teléfono para un sistema de control de llamadas telefónicas.</li>
</ul><h2 class="bio">Bibliografía</h2>
<ul class="bio"><li><a href="http://exa.unne.edu.ar/informatica/anasistem2/public_html/apuntes/de1.pdf" rel="noopener" target="_blank">Universidad Tecnológica Nacional – F.R.R.</a></li>
</ul> </article>

# Pruebas. Planificación y documentación. Utilización de datos de prueba. Pruebas de software, hardware, procedimientos y datos.

<article><h2>Documentación y Pruebas en el Desarrollo Tradicional del Software</h2>
<h3>Documentación y Desarrollo de Software</h3>
<p>En general se habla mucho de la documentación, pero no se hace, no se le asigna presupuesto, no se la mantiene y casi nunca está al día en los proyectos de desarrollo de software. Lo importante es la disponibilidad de la documentación que se necesita en el momento en que se la necesita.</p>
<p>Muchas veces se hace porque hay que hacerla y se escribe, con pocas ganas, largos textos, a la vez que se está convencido de estar haciendo un trabajo inútil. A veces se peca por exceso y otras por defecto. Ocurre mucho en la Web y con productos RAD. En ocasiones se olvida que el mantenimiento también debe llegar a la documentación.</p>
<p>La documentación se suele clasificar en función de las personas o grupos a los cuales está dirigida:</p>
<ul><li>Documentación para los desarrolladores.</li>
<li>Documentación para los usuarios.</li>
<li>Documentación para los administradores o soporte técnico.</li>
</ul><p>La documentación para desarrolladores es aquélla que se utiliza para el propio desarrollo del producto y, sobre todo, para su mantenimiento futuro. Se documenta para comunicar estructura y comportamiento del sistema o de sus partes, para visualizar y controlar la arquitectura del sistema, para comprender mejor el mismo y para controlar el riesgo, entre otras cosas. Obviamente, cuanto más complejo es el sistema, más importante es la documentación.</p>
<p>En este sentido, todas las fases de un desarrollo deben documentarse: requerimientos, análisis, diseño, programación, pruebas, etc. Una herramienta muy útil en este sentido es una notación estándar de modelado, de modo que mediante ciertos diagramas se puedan comunicar ideas entre grupos de trabajo.</p>
<p>Hay decenas de notaciones, tanto estructuradas como orientadas a objetos. Un caso particular es el de UML. De todas maneras, los diagramas son muy útiles, pero siempre y cuando se mantengan actualizados, por lo que más vale calidad que cantidad.</p>
<p>La documentación para desarrolladores a menudo es llamada <strong>modelo</strong>, pues es una simplificación de la realidad para comprender mejor el sistema como un todo.</p>
<p>Otro aspecto a tener en cuenta cuando se documenta o modela, es el del nivel de detalle. Así como cuando construimos planos de un edificio podemos hacer planos generales, de arquitectura, de instalaciones y demás, también al documentar el software debemos cuidar el nivel de detalle y hacer diagramas diferentes en función del usuario de la documentación, concentrándonos en un aspecto a la vez.</p>
<p>De toda la documentación para los desarrolladores, nos interesa especialmente en esta obra aquella que se utiliza para documentar la programación, y en particular hemos analizado la que se usa para documentar desarrollos orientados a objetos.</p>
<p>La documentación para usuarios es todo aquello que necesita el usuario para la instalación, aprendizaje y uso del producto. Puede consistir en guías de instalación, guía del usuario, manuales de referencia y guía de mensajes.</p>
<p>En el caso de los usuarios que son programadores, esta documentación se debe acompañar con ejemplos de uso recomendados o de muestra y una reseña de efectos no evidentes de las bibliotecas.</p>
<p>Más allá de todo esto, debemos tener en cuenta que la estadística demuestra que los usuarios no leen los manuales a menos que nos les quede otra opción. Las razones pueden ser varias, pero un análisis de la realidad muestra que se recurre a los manuales solamente cuando se produce un error o se desconoce cómo lograr algo muy puntual, y recién cuando la ayuda en línea no satisface las necesidades del usuario. Por lo tanto, si bien es cierto que debemos realizar manuales, la existencia de un buen manual nunca nos libera de hacer un producto amigable para el usuario, que incluso contenga ayuda en línea. Es incluso deseable proveer un software tutorial que guíe al usuario en el uso del sistema, con apoyo multimedia, y que puede llegar a ser un curso on-line.</p>
<p>Buena parte de la documentación para los usuarios puede empezar a generarse desde que comienza el estudio de requisitos del sistema. Esto está bastante en consonancia con las ideas de <em>extreme programming</em> y con metodologías basadas en casos de uso.</p>
<p>La documentación para administradores o soporte técnico, a veces llamada manual de operaciones, contiene toda la información sobre el sistema terminado que no hace al uso por un usuario final. Es necesario que tenga una descripción de los errores posibles del sistema, así como los procedimientos de recuperación. Como esto no es algo estático, pues la aparición de nuevos errores, problemas de compatibilidad y demás nunca se puede descartar, en general el manual de operaciones es un documento que va engrosándose con el tiempo.</p>
<h3>Las Pruebas en el Desarrollo de Software</h3>
<p><strong>Calidad, errores y pruebas</strong></p>
<p>La calidad no es algo que se pueda agregar al software después de desarrollado si no se hizo todo el desarrollo con la cantidad en mente. Muchas veces parece que el software de calidad es aquel que brinda lo que se necesita con adecuada velocidad de procesamiento. En realidad, es mucho más que eso. Tiene que ver con la corrección, pero también con usabilidad, costo, consistencia, confiabilidad, compatibilidad, utilidad, eficiencia y apego a los estándares.</p>
<p>Todos estos aspectos de la calidad pueden ser objeto de tests o pruebas que determinen el grado de calidad. Incluso la documentación para el usuario debe ser probada.</p>
<p>Como en todo proyecto de cualquier índole,siempre se debe tratar que las fallas sean mínimas y poco costosas, durante todo el desarrollo. Y además, es sabido que cuanto más tarde se encuentra una falla, más caro resulta eliminarla. Es claro que si un error es descubierto en la mitad del desarrollo de un sistema, el costo de su corrección será mucho menor al que se debería enfrentar en caso de descubrirlo con el sistema instalado y en funcionamiento.</p>
<p>Desde el punto de vista de la programación,nos interesa la ausencia de errores (corrección), la confiabilidad y la eficiencia. Dejando de lado las dos últimas, nos concentraremos en este capítulo en las pruebas que determinan que un programa está libre de errores.</p>
<p>Un <strong>error</strong> es un comportamiento distinto del que espera un usuario razonable. Puede haber errores aunque se hayan seguido todos los pasos indicados en el análisis y en el diseño, y hasta en los requisitos aprobados por el usuario. Por lo tanto,no necesariamente un apego a los requisitos y un perfecto seguimiento de las etapas nos lleva a un producto sin errores, porque aún en la mente de un usuario pudo haber estado mal concebida la idea desde el comienzo. De allí la importancia del desarrollo incremental, que permite ir viendo versiones incompletas del sistema.</p>
<p>Por lo tanto, una primera fuente de errores ocurre antes de los requerimientos o en el propio proceso de análisis. Pero también hay errores que se introducen durante el proceso de desarrollo posterior. Así, puede haber errores de diseño y errores de implementación. Finalmente, puede haber incluso errores en la propia etapa de pruebas y depuración.</p>
<p><strong>Categorías de pruebas</strong></p>
<p>Según la naturaleza de lo que se esté controlando, las pruebas se pueden dividir en dos categorías:</p>
<ul><li>Pruebas centradas en la verificación.</li>
<li>Pruebas centradas en la validación.</li>
</ul><p>Las primeras sirven para determinar la consistencia entre los requerimientos y el programa terminado. Soporta metodologías formales de testeo, de mucho componente matemático. De todas maneras, hay que ser cuidadoso, porque no suele ser fácil encontrar qué es lo que hay que demostrar. La verificación consisten en determinar si estamos construyendo el sistema correctamente, a partir de los requisitos.</p>
<p>En general a los informáticos no les gustan las pruebas formales, en parte porque no las entienden y en parte porque requieren un proceso matemático relativamente complejo.</p>
<p>La validación consiste en saber si estamos construyendo el sistema correcto. Las tareas de validación son más informales. Las pruebas suelen mostrar la presencia de errores, pero nunca demuestran su ausencia.</p>
<p><strong>Las pruebas y el desarrollo de software</strong></p>
<p>La etapa de pruebas es una de las fases del ciclo de vida de los proyectos. Se la podría ubicar después del análisis, el diseño y la programación, pero dependiendo del proyecto en cuestión y del modelo de proceso elegido, su realización podría ser en forma paralela a las fases citadas o inclusive repertirse varias veces durante la duración del proyecto.</p>
<p>La importancia de esta fase será mayor o menor según las características del sistema desarrollado, llegando a ser vital en sistemas de tiempo real u otros en los que los errores sean irrecuperables.</p>
<p>Las pruebas no tienen el objeto de prevenir errores sino de detectarlos. Se efectúan sobre el trabajo realizado y se deben encarar con la intención de descubrir la mayor cantidad de errores posible.</p>
<p>Para realizar las pruebas se requiere gente que disfrute encontrando errores, por eso no es bueno que sea el mismo equipo de desarrollo el que lleve a cabo este trabajo. Además, es un principio fundamental de las auditorías. Por otro lado, es bastante común que a quien le guste programar no le guste probar y viceversa.</p>
<p>A veces se dan por terminadas las pruebas antes de tiempo. En las pruebas de caja blanca no es mala idea probar un 85% de las ramas y dar por terminado luego de esto. Otra posibilidad es la siembra de errores y seguir las pruebas hasta que se encuentren un 85% de los errores sembrados, lo que presumiblemente implica que se encontró un 86% de los no sembrados. Otros métodos se basan en la estadística y las comparaciones, ya sea por similitud con otro sistema en cantidad de errores o por el tiempo de prueba usado en otro sistema.</p>
<p>En un proyecto ideal, podríamos generar casos de prueba para cubrir todas las posibles entradas y todas las posibles situaciones por las que podría atravesar el sistema. Examinaríamos así exhaustivamente el sistema para asegurar que su comportamiento sea perfecto. Pero hay un problema con esto: el número de casos de prueba para un sistema complejo es tan grande que no alcanzaría una vida para terminar con las pruebas. Como consecuencia, nadie realiza una prueba exhaustiva de nada salvo en sistemas triviales.</p>
<p>En un sistema real, los casos de prueba se deben hacer sobre las partes del sistema en los cuales una buena prueba brinde un mayor retorno de la inversión o en las cuales un error represente un riesgo mayor.</p>
<p>Las pruebas cuestan mucho dinero. Pero para ello existe una máxima: “pague por la prueba ahora o pague el doble por el mantenimiento después”.</p>
<p>Todo esto lleva a que se deban planificar bien las pruebas, con suficiente anticipación, y determinar desde el comienzo los resultados que se deben obtener.</p>
<p>La idea de <em>extreme programming</em> es más radical: propone primero escribir los programas de prueba y después la aplicación, obligando a correr las pruebas siempre antes de una integración. Se basa en la idea bastante acertada de que los programas de prueba son la mejor descripción de los requerimientos.</p>
<p>Las pruebas son prácticas a realizar en diversos momentos de la vida del sistema de información para verificar:</p>
<ul><li>El correcto funcionamiento de los componentes del sistema.</li>
<li>El correcto ensamblaje entre los distintos componentes.</li>
<li>El funcionamiento correcto de las interfaces entre los distintos subsistemas que lo componen y con el resto de sistemas de información con los que se comunica.</li>
<li>El funcionamiento correcto del sistema integrado de hardware y software en el entorno de operación.</li>
<li>Que el sistema cumple con el funcionamiento esperado y permite al usuario de dicho sistema que determine su aceptación, desde el punto de vista de su funcionalidad y rendimiento.</li>
<li>Que los cambios sobre un componente de un sistema de información, no introducen un comportamiento no deseado o errores adicionales en otros componentes no modificados.</li>
</ul><p>Las diversas pruebas a que debe ser sometido un sistema deben ser realizadas tanto por el equipo de desarrolladores, como por los usuarios, equipos de operación y mantenimiento en la implantación, aceptación y mantenimiento del sistema de información.</p>
<p><strong>Tipos de pruebas</strong></p>
<p>Analizaremos 7 tipos de pruebas:</p>
<ul><li>Revisiones de código.</li>
<li>Pruebas unitarias.</li>
<li>Pruebas de integración.</li>
<li>Pruebas de sistema.</li>
<li>Pruebas de implantación.</li>
<li>Pruebas de aceptación.</li>
<li>Pruebas de regresión.</li>
</ul><p>No son tipos de pruebas intercambiables, ya que testean cosas distintas.</p>
<p>Otra posible clasificación de las pruebas es:</p>
<ul><li>De caja blanca o de código</li>
<li>De caja negra o de especificación</li>
</ul><p>En las primeras se evalúa el contenido de los módulos, mientras en las segundas se trata al módulo como una caja cerrada y se lo prueba con valores de entrada, evaluando los valores de salida. Vistas de este modo, las pruebas de caja negra sirven para verificar especificaciones.</p>
<p>Las pruebas unitarias suelen ser de caja blanca o de caja negra, mientras que las de integración, sistema y aceptación son de caja negra. Las tareas de depuración luego de encontrar errores son más bien técnicas de caja blanca, así como las revisiones de código. En todos los casos, uno de los mayores desafíos es encontrar los datos de prueba: hay que encontrar un subconjunto de todas las entradas que tengan alta probabilidad de detectar el mayor número de errores.</p>
<p><strong>Revisiones de código</strong></p>
<p>Las revisiones de código son las únicas que se podrían omitir de todos los tipos de pruebas, pero tal vez sea buen idea por lo menos hacer alguna de ellas:</p>
<ul><li>Pruebas de escritorio.</li>
<li>Recorridos de código.</li>
<li>Inspecciones de código.</li>
</ul><p>La <em>prueba de escritorio</em> rinde muy poco, tal vez menos de lo que cuesta, pero es una costumbre difícil de desterrar. Es bueno centrarse en buscar anomalías típicas, como variables u objetos no inicializados o que no se usan, ciclos infinitos y demás.</p>
<p>Los <em>recorridos</em> rinden mucho más. Son exposiciones del código escrito frente a pares. El programador, exponiendo su código, encuentra muchos errores. Además da ideas avanzadas a programadores nuevos que se lleva a recorrer.</p>
<p>Las llamadas <em>inspecciones de código</em> consisten en reuniones en conjunto entre los responsables de la programación y los responsables de la revisión.Tienen como objetivo revisar el código escrito por los programadores para chequear que cumpla con las normas que se hayan fijado y para verificar la eficiencia del mismo. Se realizan siguiendo el código de un pequeño porcentaje de módulos seleccionados al azar o según su grado de complejidad. Las inspecciones se pueden usar en sistemas grandes, pero con cuidado para no dar idea de estar evaluando al programador. Suelen servir porque los revisores están más acostumbrados a ver determinados tipos de errores comunes a todos los programadores. Además, después de una inspección a un programador, de la que surge un tipo de error, pueden volver a inspeccionar a otro para ver si no cayó en el mismo error.</p>
<p>El concepto de <em>extreme programming</em> propone programar de a dos, de modo que uno escribe y el otro observa el trabajo. Si el que está programando no puede avanzar en algún momento, sigue el que miraba. Y si ambos se traban pueden pedir ayuda a otro par. Esta no sólo es una forma más social de programación, sino que aprovecha las mismas ventajas de los recorridos e inspecciones de código, y puede prescindir de ellos.</p>
<p><strong>Pruebas unitarias</strong></p>
<p>Las pruebas unitarias se realizan para controlar el funcionamiento de pequeñas porciones de código como ser subprogramas (en la programación estructurada) o métodos (en POO). Generalmente son realizadas por los mismos programadores puesto que al conocer con mayor detalle el código, se les simplifica la tarea de elaborar conjuntos de datos de prueba para testearlo.</p>
<p>Si bien una prueba exhaustiva sería impensada teniendo en cuenta recursos, plazos, etc, es posible y necesario elegir cuidadosamente los casos de prueba para recorrer tantos caminos lógicos como sea posible. Inclusive procediendo de esta manera, deberemos estar preparados para manejar un gran volumen de datos de prueba.</p>
<p>Los métodos de cobertura de caja blanca tratan de recorrer todos los caminos posibles por lo menos una vez, lo que no garantiza que no haya errores pero pretende encontrar la mayor parte.</p>
<p>El tipo de prueba a la cual se someterá a cada uno de los módulos dependerá de su complejidad. Recordemos que nuestro objetivo aquí es encontrar la mayor cantidad de errores posible. Si se pretende realizar una prueba estructurada, se puede confeccionar un grafo de flujo con la lógica del código a probar. De esta manera se podrán determinar todos los caminos por los que el hilo de ejecución pueda llegar a pasar, y por consecuente elaborar los juegos de valores de pruebas para aplicar al módulo, con mayor facilidad y seguridad.</p>
<p>Un grafo de flujo se compone de:</p>
<ul><li>Nodos (círculos), que representan una o más acciones del módulo.</li>
<li>Aristas (flechas), que representan el flujo de control entre los distintos nodos.</li>
</ul><p>Los nodos predicados son aquellos que contienen una condición, por lo que de ellos emergen dos o más aristas.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/05/nodos_predicados.png?w=825"/></p>
<p>El paso de un diseño detallado o un pseudocódigo que representa una porción de programa a un grafo de flujo, requiere de las siguientes etapas:</p>
<ul><li>Señalar cada condición, tanto en sentencias <em>if</em> y <em>case</em> como en bucles <em>while</em> y <em>repeat</em>.</li>
<li>Agrupar todas las secuencias siguiendo los esquemas de representación de construcciones.</li>
<li>Numerar cada uno de los nodos resultantes de manera que consten de un identificador único. Las ramas de cada bifurcación pueden identificarse por el mismo número seguido de distintas letras.</li>
<li>Dibujar en forma ordenada los nodos y sus aristas.</li>
</ul><p>En el siguiente ejemplo, se muestra la manera de traducir un pequeño tramo de programa escrito en pseudocódigo a forma de grafo de flujo:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/05/pseudocodigo_grafo.png?w=825"/></p>
<p>Las pruebas unitarias tienen como objetivo verificar la funcionalidad y estructura de cada componente individualmente una vez que ha sido codificado.</p>
<p>Las pruebas unitarias constituyen la prueba inicial de un sistema y las demás pruebas deben apoyarse sobre ellas.</p>
<p>Existen dos enfoques principales para el diseño de casos de prueba:</p>
<ul><li><strong>Enfoque estructural</strong> o de <strong>caja blanca</strong>. Se verifica la estructura interna del componente con independencia de la funcionalidad establecida para el mismo. Por tanto, no se comprueba la corrección de los resultados si éstos se producen. Ejemplos de este tipo de pruebas pueden ser ejecutar todas las instrucciones del programa, localizar código no usado, comprobar los caminos lógicos del programa, etc.</li>
<li><strong>Enfoque funcional</strong> o de <strong>caja negra</strong>. Se comprueba el correcto funcionamiento de los componentes del sistema de información, analizando las entradas y salidas y verificando que el resultado es el esperado. Se consideran exclusivamente las entradas y salidas del sistema sin preocuparse por la estructura interna del mismo.</li>
</ul><p>El enfoque que suele adoptarse para una prueba unitaria está claramente orientado al diseño de casos de caja blanca, aunque se complemente con caja negra. El hecho de incorporar casos de caja blanca se debe, por una parte, a que el tamaño del componente es apropiado para poder examinar toda la lógica y por otra, a que el tipo de defectos que se busca, coincide con los propios de la lógica detallada en los componentes.</p>
<p>Los pasos necesarios para llevar a cabo las pruebas unitarias son los siguientes:</p>
<ul><li>Ejecutar todos los casos de prueba asociados a cada verificación establecida en el plan de pruebas, registrando su resultado. Los casos de prueba deben contemplar tanto las condiciones válidas y esperadas como las inválidas e inesperadas.</li>
<li>Corregir los errores o defectos encontrados y repetir las pruebas que lo detectaron. Si se considera necesario, debido a su implicación o importancia, se repetirán otros casos de prueba ya realizados con anterioridad.</li>
</ul><p>La prueba unitaria se da por finalizada cuando se hayan realizado todas las verificaciones establecidas y no se encuentre ningún defecto, o bien se determine su suspensión.</p>
<p><strong>Pruebas de integración</strong></p>
<p>En el caso de las pruebas de integración y de sistema,dado que ya se han realizado las pruebas unitarias, se tomará a cada uno de los módulos unitarios como una caja negra.</p>
<p>Las pruebas de integración tienen como base las pruebas unitarias y consisten en una progresión ordenada de testeos para los cuales los distintos módulos van siendo ensamblados y probados hasta haber integrado el sistema completo. Si bien se realizan sobre módulos ya probados en forma individual, no es necesario que se terminen todas las pruebas unitarias para comenzar con las de integración. Dependiendo de la forma en que se organicen, se pueden realizar en paralelo a las unitarias.</p>
<p>El orden de integración de los módulos influye en:</p>
<ul><li>La forma de preparar los casos de prueba.</li>
<li>Las herramientas a utilizar (módulos ficticios, muñones, impulsores o “stubs”).</li>
<li>El orden para codificar y probar los módulos.</li>
<li>El costo de preparar los casos.</li>
<li>El costo de la depuración.</li>
</ul><p>Tanto es así que se le debe prestar especial atención al proceso de elección del orden de integración que se emplee.</p>
<p>Existen principalmente dos tipos de integración:</p>
<ul><li>La<em> integración incremental</em></li>
<li>La integración&nbsp;<em>no incremental</em>.</li>
</ul><p>La <strong>integración incremental</strong> consiste en combinar el conjunto de módulos ya probados (al principio será un conjunto vacío) con los siguientes módulos a probar. Luego se va incrementando progresivamente el número de módulos unidos hasta que se forma el sistema completo.</p>
<p>En la <strong>integración no incremental</strong> o <strong>Big Bang</strong> se combinan todos los módulos de una vez.</p>
<p>Para ambos tipos de integración se deberán preparar los datos de prueba junto con los resultados esperados. Esta tarea debe ser realizada por personas ajenas a la programación de los módulos. No es necesario que la lleven a cabo una vez codificados los módulos puesto que basta con conocer qué módulos compondrán el sistema y cuál será la interfaz entre ellos.</p>
<p>Si en algún momento de la prueba se detectara uno o más errores, se dejará constancia del hecho y se reenviarán los módulos afectados al responsable de la programación para que identifique la causa del problema y lo solucione. Luego se volverán a efectuar las pruebas programadas y así sucesivamente hasta que el sistema entero esté integrado y sin errores.</p>
<p>Por el hecho de poder ser llevada a cabo por distintos caminos, la integración incremental brinda una mayor flexibilidad en el uso de recursos. Se puede integrar la estructura de módulos desde un extremo a otro y continuar hacia el extremo opuesto según distintas prioridades. La forma de llevar a cabo esta tarea dependerá de la naturaleza del sistema en cuestión, pero sea cual fuere el camino elegido, será de suma importancia una correcta planificación.</p>
<p>En la <strong>integración incremental ascendente (De abajo arriba – bottom-up)</strong> se comienza integrando primero los módulos de más bajo nivel. El proceso deberá seguir los siguientes pasos:</p>
<ul><li>Elegir los módulos de bajo nivel que se van a probar.</li>
<li>Escribir un módulo impulsor para la entrada de datos de prueba a los módulos y para la visualización de los resultados.</li>
<li>Probar la integración de los módulos.</li>
<li>Eliminar los módulos impulsores y juntar los módulos ya probados con los módulos de niveles superiores, para continuar con las pruebas.</li>
</ul><p>Estas tareas se pueden realizar en paralelo si es que se dispone de tres equipos de trabajo, o en serie de lo contrario. Para la prueba de cada uno de los módulos mencionados, es necesaria la preparación de un módulo impulsor. El objeto de los módulos impulsores es transmitir o impulsar los casos de prueba a los módulos testeados y recibir los resultados que estos produzcan en los casos en que sea necesario. Es decir, que deben simular las operaciones de llamada de los módulos jerárquicos superiores correspondientes. Estos módulos tienen que estar bien diseñados, para que no arrojen ni más ni menos errores que los que realmente pueden producirse. Al fin y al cabo, deben simular todas las situaciones que se van a producir en el sistema real.</p>
<p>La <strong>integración incremental descendente (De arriba abajo – top-down)</strong>&nbsp;parte del módulo de control principal (de mayor nivel) para luego ir incorporando los módulos subordinados progresivamente. No hay un procedimiento considerado óptimo para seleccionar el siguiente módulo a incorporar. La única regla es que el módulo incorporado tenga todos los módulos que lo invocan previamente probados.</p>
<p>En general no hay una secuencia óptima de integración. Debe estudiarse el problema concreto y de acuerdo a este, buscar el orden de integración más adecuado para la organización de las pruebas. No obstante, pueden considerarse las siguientes pautas:</p>
<ul><li>Si hay secciones críticas como ser un módulo complicado, se debe proyectar la secuencia de integración para incorporarlas lo antes posible.</li>
<li>El orden de integración debe incorporar cuanto antes los módulos de entrada y salida.</li>
</ul><p>Existen principalmente dos métodos para la incorporación de módulos:</p>
<ul><li>Primero en profundidad: primero se mueve verticalmente en la estructura de módulos.</li>
<li>Primero en anchura: Primero se mueve horizontalmente en la estructura de módulos.</li>
</ul><p>Etapas de la integración descendente:</p>
<ul><li>El módulo de mayor nivel hace de impulsor y se escriben módulos ficticios simulando a los subordinados, que serán llamados por el módulo de control superior.</li>
<li>Probar cada vez que se incorpora un&nbsp; módulo nuevo al conjunto ya engarzado.</li>
<li>Al terminar cada prueba, sustituir un módulo ficticio subordinado por el real que reemplazaba, según el orden elegido.</li>
<li>Escribir los módulos ficticios subordinados que se necesiten para la prueba del nuevo módulo incorporado.</li>
</ul><p>Los módulos ficticios subordinados se crean para permitir la prueba de los demás módulos. Pueden llevar a cabo una variedad de funciones, como por ejemplo:</p>
<ul><li>Mostrar un mensaje que demuestre que ese módulo fue alcanzado (“Módulo XX alcanzado”).</li>
<li>Establecer una conversación con una terminal. De esta forma se puede permitir que la misma persona que realiza la prueba actúe de módulo subordinado.</li>
<li>Devolver un valor constante, tabulado o elegido al azar.</li>
<li>Ser una versión simplificada del módulo representado.</li>
<li>Mostrar los datos recibidos.</li>
<li>Ser un loop sin nada que hacer más que dejar pasar el tiempo.</li>
</ul><p>Ventajas de la integración descendente:</p>
<ul><li>Las fallas que pudieran existir en los módulos superiores se detectan en una etapa temprana.</li>
<li>Permite ver la estructura del sistema desde un principio, facilitando la elaboración de demostraciones de su funcionamiento.</li>
<li>Concuerda con la necesidad de definir primero las interfaces de los distintos subsistemas para después seguir con las funciones específicas de cada uno por separado.</li>
</ul><p>Desventajas de la integración descendente:</p>
<ul><li>Requiere mucho trabajo de desarrollo adicional ya que se deben escribir un gran número de módulos ficticios subordinados que no siempre son fáciles de realizar. Suelen ser más complicados de lo que aparentan.</li>
<li>Antes de incorporar los módulos de entrada y salida resulta difícil introducir los casos de prueba y obtener los resultados.</li>
<li>Los juegos&nbsp; de datos de prueba pueden resulta difíciles o imposibles de generar puesto que generalmente son los módulos de nivel inferior los que proporcionan los detalles.</li>
<li>Induce a diferir la terminación de la prueba de ciertos módulos.</li>
</ul><p>Ventajas de la integración incremental ascendente:</p>
<ul><li>Las entradas para las pruebas son más fáciles de crear ya que los módulos inferiores suelen tener funciones más específicas.</li>
<li>Es más fácil la observación de los resultados de las pruebas puesto que es en los módulos inferiores donde se elaboran.</li>
<li>Resuelve primero los errores de los módulos inferiores que son los que acostumbran tener el procesamiento más complejo, para luego nutrir de datos al resto del sistema.</li>
</ul><p>Desventajas de la integración incremental ascendente:</p>
<ul><li>Se requieren módulos impulsores, que deben escribirse especialmente y que no son necesariamente sencillos de codificar.</li>
<li>El sistema como entidad no existe hasta que se agrega el último módulo.</li>
</ul><p>El método de<strong> integración incremental sándwich (estrategia combinada)</strong> combina facetas de los métodos ascendente y descendente. Consiste en integrar una parte del sistema en forma ascendente y la restante en forma descendente, provocando la unión de ambas partes en algún punto intermedio. La principal ventaja es que nos da mayor libertad para elegir el orden de integración de los módulos según las características específicas del sistema en cuestión. De esta manera, podremos incluir y probar antes los módulos que consideremos críticos:</p>
<ul><li>Módulos dirigidos a múltiples propósitos.</li>
<li>Módulos con mayor control (en general, los módulos de mayor nivel controlan a muchos otros módulos).</li>
<li>Módulos con alto grado de complejidad.</li>
<li>Módulos con requisitos de rendimiento muy definidos.</li>
</ul><p>La <strong>integración no incremental</strong> puede ser beneficiosa par la prueba de sistema de pequeñísima envergadura cuya cantidad de módulos sea muy limitada y la interfaz entre los mismos clara y sencilla. Consiste en integrar todos los módulos del sistema a la vez e ingresar los valores de prueba para testear todas las interfaces.</p>
<p>La única ventaja es que no se necesita ningún tipo de trabajo adicional: ni planificar el orden de integración, ni crear módulos impulsores, ni crear módulos ficticios subordinados. Por otro lado, la lista de desventajas incluye:</p>
<ul><li>No se tiene noción de la comunicación de los módulos hasta el final.</li>
<li>En ningún momento se dispone de un producto -siquiera parcial- para mostrar o presentar.</li>
<li>El hecho de realizar todas las pruebas de una vez hace que las sesiones de prueba sean largas y tediosas.</li>
<li>La cantidad de errores que arroje puede ser atemorizante.</li>
<li>La tarea de encontrar la causa de los errores resulta mucho más compleja que con los métodos incrementales.</li>
<li>Se corre el riesgo de que a poco tiempo de que se cumpla el plazo de entrega, haya que volver sobre el diseño y la codificación del sistema.</li>
</ul><p><strong>Pruebas de sistema</strong></p>
<p>Son pruebas de integración del sistema de información completo, y permiten probar el sistema en su conjunto y con otros sistemas con los que se relaciona para verificar que las especificaciones funcionales y técnicas se cumplen. Dan una visión muy similar a su comportamiento en el entorno de producción.</p>
<p>Las pruebas de sistema se realizan una vez integrados todos los componentes. Su objetivo es ver la respuesta del sistema en su conjunto, frente a distintas situaciones. Se simulan varias alternativas que podrían darse con el sistema implantado y en base a ellas se prueba la eficacia y eficiencia de la respuesta que se obtiene.</p>
<p>Se pueden distinguir varios tipos de pruebas distintos, por ejemplo:</p>
<ul><li><strong>Pruebas negativas</strong>: se trata de que el sistema falle para ver sus debilidades.</li>
<li><strong>Pruebas funcionales</strong>: dirigidas a asegurar que el sistema de información realiza correctamente todas las funciones que se han detallado en las especificaciones dadas por el usuario del sistema.</li>
<li><strong>Pruebas de comunicaciones</strong>: determinan que las interfaces entre los componentes del sistema funcionan adecuadamente, tanto a través de dispositivos remotos, como locales. Asimismo, se han de probar las interfaces hombre/máquina.</li>
<li><strong>Pruebas de volumen</strong>: consisten en examinar el funcionamiento del sistema cuando está trabajando con grandes volúmenes de datos, simulando las cargas de trabajo esperadas.</li>
<li><strong>Pruebas de sobrecarga</strong>: consisten en comprobar el funcionamiento del sistema en el umbral límite de los recursos, sometiéndole a cargas masivas. El objetivo es establecer los puntos extremos en los cuales el sistema empieza a operar por debajo de los requisitos establecidos.</li>
<li><strong>Pruebas de disponibilidad de datos</strong>: consisten en demostrar que el sistema puede recuperarse ante fallos, tanto de equipo físico como lógico, sin comprometer la integridad de los datos.</li>
<li><strong>Pruebas de facilidad de uso</strong>: consisten en comprobar la adaptabilidad del sistema a las necesidades de los usuarios, tanto para asegurar que se acomoda a su modo habitual de trabajo, como para determinar las facilidades que aporta al introducir datos en el sistema y obtener los resultados.</li>
<li><strong>Pruebas de operación</strong>: consisten en comprobar la correcta implementación de los procedimientos de operación, incluyendo la planificación y control de trabajos, arranque y rearranque del sistema, etc.</li>
<li><strong>Pruebas de entorno</strong>: consisten en verificar las interacciones del sistema con otros sistemas dentro del mismo entorno.</li>
<li><strong>Pruebas de recuperación</strong>: se simulan fallas de software y/o hardware para verificar la eficacia del proceso de recuperación.</li>
<li><strong>Pruebas de rendimiento</strong>: tiene como objeto evaluar el rendimiento del sistema integrado en condiciones de uso habitual. Consisten en determinar que los tiempos de respuesta están dentro de los intervalos establecidos en las especificaciones del sistema.</li>
<li><strong>Pruebas de resistencia o de estrés</strong>: comprueban el comportamiento del sistema ante situaciones donde se demanden cantidades extremas de recursos (número de transacciones simultáneas anormal, excesivo uso de las memorias, etc).</li>
<li><strong>Pruebas de seguridad</strong>: se utilizan para testear el esquema de seguridad intentando vulnerar los métodos utilizados para el control de accesos no autorizados al sistema. Consisten en verificar los mecanismos de control de acceso al sistema para evitar alteraciones indebidas en los datos.</li>
<li><strong>Pruebas de instalación</strong>: verifican que el sistema puede ser instalado satisfactoriamente en el equipo del cliente, incluyendo todas las plataformas y configuraciones de hardware necesarias.</li>
<li><strong>Pruebas de compatibilidad</strong>: se prueba al sistema en las diferentes configuraciones de hardware o de red y de plataformas de software que debe soportar.</li>
</ul><p><strong>Pruebas de implantación</strong></p>
<p>El objetivo de las pruebas de implantación es comprobar el funcionamiento correcto del sistema integrado de hardware y software en el entorno de operación, y permitir al usuario que, desde el punto de vista de operación, realice la aceptación del sistema una vez instalado en su entorno real y en base al cumplimiento de los requisitos no funcionales especificados.</p>
<p>Una vez que hayan sido realizadas las pruebas del sistema en el entorno de desarrollo, se llevan a cabo las verificaciones necesarias para asegurar que el sistema funcionará correctamente en el entorno de operación. Debe comprobarse que responde satisfactoriamente a los requisitos de rendimiento, seguridad, operación y coexistencia con el resto de los sistemas de la instalación para conseguir la aceptación del usuario de operación.</p>
<p>Las pruebas de <strong>seguridad</strong> van dirigidas a verificar que los mecanismos de protección incorporados al sistema cumplen su objetivo; las de <strong>rendimiento</strong> a asegurar que el sistema responde satisfactoriamente en los márgenes establecidos en cuanto a tiempos de respuesta, de ejecución y de utilización de recursos, así como los volúmenes de espacio en disco y capacidad; por último con las pruebas de <strong>operación</strong> se comprueba que la planificación y control de trabajos del sistema se realiza de acuerdo a los procedimientos establecidos, considerando la gestión y control de las comunicaciones y asegurando la disponibilidad de los distintos recursos.</p>
<p>Asimismo, también son llevadas a cabo las pruebas de <strong>gestión de copias de seguridad</strong> y recuperación, con el objetivo de verificar que el sistema no ve comprometido su funcionamiento al existir un control y seguimiento de los procedimientos de salvaguarda y de recuperación de la información, en caso de caídas en los servicios o en algunos de sus componentes. Para comprobar estos últimos, se provoca el fallo del sistema, verificando si la recuperación se lleva a cabo de forma apropiada. En el caso de realizarse de forma automática, se evalúa la inicialización, los mecanismos de recuperación del estado del sistema, los datos y todos aquellos recursos que se vean implicados.</p>
<p>Las verificaciones de las pruebas de implantación y las pruebas del sistema tienen muchos puntos en común al compartir algunas de las fuentes para su diseño como pueden ser los casos para probar el rendimiento (pruebas de sobrecarga o <em>stress</em>).</p>
<p>El responsable de implantación junto al equipo de desarrollo determina las verificaciones necesarias para realizar las pruebas así como los criterios de aceptación del sistema. Estas pruebas las realiza el equipo de operación, integrado por los técnicos de sistemas y de operación que han recibido previamente la formación necesaria para llevarlas a cabo.</p>
<p><strong>Pruebas de aceptación</strong></p>
<p>El objetivo de las pruebas de aceptación es validar que un sistema cumple con el funcionamiento esperado y permitir al usuario de dicho sistema que determine su aceptación, desde el punto de vista de su funcionalidad y rendimiento.</p>
<p>Las pruebas de aceptación, al igual que las de sistema, se realizan sobre el producto terminado e integrado; pero a diferencia de aquellas, están concebidas para que sea un usuario final quien detecte los posibles errores.</p>
<p>Se clasifican en dos tipos:</p>
<ul><li>Pruebas Alfa.</li>
<li>Pruebas Beta.</li>
</ul><p>Las <strong>pruebas Alfa</strong> se realizan por un cliente en un entorno controlado por el equipo de desarrollo. Para que tengan validez, se debe primero crear un ambiente con las mismas condiciones que se encontrarán en las instalaciones del cliente. Una vez logrado esto, se procede a realizar las pruebas y a documentar los resultados.</p>
<p>Cuando el software sea la adaptación de una versión previa, deberán probarse también los procesos de transformación de datos y actualización de archivos de todo tipo.</p>
<p>Las <strong>pruebas Beta</strong> se realizan en las instalaciones propias de los clientes. Para que tengan lugar, en primer término se deben distribuir copias del sistema para que cada cliente lo instale en sus oficinas, dependencias y/o sucursales, según sea el caso. Si se tratase de un número reducido de clientes el tema de la distribución de las copias no representa grandes dificultades, pero en el caso de productos de venta masiva, la elección de los <em>beta testers</em> debe realizarse con sumo cuidado. En el caso de las pruebas Beta ,cada usuario realizará sus propias pruebas y documentará los errores que encuentre, así como las sugerencias que crea conveniente realizar, para que el equipo de desarrollo tenga en cuenta al momento de analizar las posibles modificaciones.</p>
<p>Cuando el sistema tenga un cliente individual, las pruebas de aceptación se hacen de común acuerdo con éste, y los usuarios se determinan en forma programada, así como también se definen los aspectos a probar y la forma de informar resultados. Cuando, en cambio, se está desarrollando un producto masivo, los usuarios para pruebas de determinan de formas menos estrictas, y hay que ser muy cuidado en la evaluación del <em>feedback</em> que proveen. Por lo tanto, en este segundo caso hay que dedicar un esfuerzo considerable a la planificación de las pruebas de aceptación.</p>
<p><strong>Pruebas de regresión</strong></p>
<p>El objetivo de las pruebas de regresión es eliminar el efecto onda, es decir, comprobar que los cambios sobre un componente de un sistema de información, no introducen un comportamiento no deseado o errores adicionales en otros componentes no modificados.</p>
<p>Las pruebas de regresión se deben llevar a cabo cada vez que se hace un cambio en el sistema, tanto para corregir un error como para realizar una mejora. No es suficiente probar sólo los componentes modificados o añadidos, o las funciones que en ellos se realizan, sino que también es necesario controlar que las modificaciones no produzcan efectos negativos sobre el mismo u otros componentes.</p>
<p>Normalmente, este tipo de pruebas implica la repetición de las pruebas que ya se han realizado previamente, con el fin de asegurar que no se introducen errores que puedan comprometer el funcionamiento de otros componentes que no han sido modificados y confirmar que el sistema funciona correctamente una vez realizados los cambios.</p>
<p>Las pruebas de regresión pueden incluir:</p>
<ul><li>La repetición de los casos de pruebas que se han realizado anteriormente y están directamente relacionados con la parte del sistema modificada.</li>
<li>La revisión de los procedimientos manuales preparados antes del cambio, para asegurar que permanecen correctamente.</li>
<li>La obtención impresa del diccionario de datos de forma que se comprueba que los elementos de datos que han sufrido algún cambio son correctos.</li>
</ul><p>El responsable de realizar las pruebas de regresión será el equipo de desarrollo junto al técnico de mantenimiento, quien a su vez, será responsable de especificar el plan de pruebas de regresión y de evaluar los resultados de dichas pruebas.</p>
<h3>Relación ante los resultados de las pruebas</h3>
<p>Las pruebas nos llevan a descubrir errores, que en la mayoría de los casos son de tipo funcional, es decir, del tipo: “el sistema debería hacer tal cosa y hace tal otra”.</p>
<p>En este apartado analizaremos nada más que los pasos a seguir cuando el error sólo es atribuible a la codificación.</p>
<p><strong>Depuración</strong></p>
<p>La depuración es la corrección de errores que sólo afectan a la programación, porque no provienen de errores previos en el análisis o en el diseño. A veces la depuración se hace luego de la entrega del sistema al cliente y es parte del mantenimiento.</p>
<p>En realidad, en las revisiones de código y las pruebas unitarias, encontrar un error es considerablemente más sencillo, ya que se hace con el código a mano. Aun cuando se hubiera optado por una prueba unitaria de caja negra,es sencillo recorrer el módulo que revela un comportamiento erróneo por dentro para determinar el lugar exacto del error. Existen incluso herramientas de depuración (<em>debugging</em>) de los propios ambientes de desarrollo que facilitan esta tarea, que incluso proveen recorrido paso a paso y examen de valores de datos. Y el lenguaje C traía una macro <em>assert</em> portable, que sencillamente abortaba un programa si una condición no se cumplía.</p>
<p>De todas maneras, es importante analizar correctamente si el error está donde parece estar o proviene de una falla oculta más atrás en el código. Para encontrar estos casos más complejos son útiles las herramientas de recorrida hacia atrás, que permiten partir del lugar donde se genera el error y recorrer paso a paso el programa en sentido inverso.</p>
<p>Las pruebas de integración, de sistema y de aceptación también pueden llevar a que sea necesaria una depuración, aunque aquí es más difícil encontrar el lugar exacto del error. Por eso a menudo se utilizan <em>bitácoras</em> (<em>logs</em>), que nos permiten evaluar las condiciones que se fueron dando antes de un error mediante el análisis de un historial de uso del sistema que queda registrado en medios de almacenamiento permanente.</p>
<p>La depuración se hace en cuatro pasos:</p>
<ul><li>Reproducir el error.</li>
<li>Diagnosticar la causa.</li>
<li>Corregirla.</li>
<li>Verificar la corrección.</li>
</ul><p>Si el error no se repite al intentar reproducirlo es muy difícil hacer el diagnóstico. Como en casi todas las ciencias, se buscan causas y efectos, condiciones necesarias y suficientes para que se produzca el error. Luego hay que buscar el sector del código donde se produce el error, lo que nos lleva a las consideraciones hechas recientemente. La corrección del error entraña mucho riesgo, porque a menudo se introducen nuevos errores (hay quienes hablan de tasas de 0,2 a 0,5 nuevos errores por corrección). Y nunca hay que olvidarse de realizar una nueva verificación después de la corrección.</p>
<p><strong>Reacción ante los errores en las pruebas de sistema y de aceptación</strong></p>
<p>Hemos dicho ya que los errores que aparezcan en estos tipos de prueba van a llevar a la larga a una depuración, en la medida en que sean errores de codificación.</p>
<p>Para llegar a ello, no obstante, se requiere determinar el módulo donde se produjo el error. Esta tarea, en apariencia dificultosa, puede facilitarse considerablemente si trabajamos con un entorno de desarrollo que nos permita recorrer el código en modo de depuración sin necesidad de entrar en todos los módulos.</p>
<h2>Revisión Formal</h2>
<p>El objetivo de la revisión formal es detectar y registrar los defectos de un producto intermedio verificando que satisface sus especificaciones y que se ajusta a los estándares establecidos, señalando las posibles desviaciones.</p>
<p>Es un proceso de revisión riguroso en el que hay poca flexibilidad a la hora de llevarlo a cabo debido a que su objetivo es llegar a detectar lo antes posible, los posibles defectos o desviaciones en los productos que se van generando a lo largo del desarrollo. Esta característica fuerza a que se adopte esta práctica únicamente para productos que son de especial importancia, porque de otro modo podría frenar la marcha del proyecto.</p>
<p>En este proceso intervienen varias personas del grupo de aseguramiento de calidad, el equipo de desarrollo y según el tipo de revisión formal puede participar también el usuario.</p>
<p>El responsable del grupo de aseguramiento de calidad una vez que conoce los productos que se van a revisar formalmente, establece los grupos funcionales que van a llevar a cabo las revisiones, convocando a los participantes por adelantado, e informando del objetivo de la revisión, la agenda y las responsabilidades que tendrán asignadas en la revisión.</p>
<p>Es importante que en el transcurso de la revisión se sigan las directrices que estableció el responsable del grupo de aseguramiento de calidad, con el fin de que sea productiva y no se pierda tiempo en discusiones o ataques al responsable del producto.</p>
<p>Se concluye determinando las áreas de problemas y elaborando un informe de revisión formal y una lista de acciones correctivas que posee un carácter formal y vinculante.</p>
<h2>Revisión Técnica</h2>
<p>El objetivo de la revisión técnica es evaluar un producto intermedio del desarrollo para comprobar que se ajusta a sus especificaciones y que se está elaborando de acuerdo a las normas, estándares y guías aplicables al proyecto.</p>
<p>Con el fin de asegurar la calidad en el producto final del desarrollo, se deben llevar a cabo revisiones semiformales sobre los productos intermedios durante todo el ciclo de vida del software. Para ello, se fijan los objetivos de la revisión, la agenda que se podrá ir ajustando a lo largo del proyecto y el tipo de informe que se elaborará después de las revisiones.</p>
<p>Los participantes en una revisión técnica son el jefe de proyecto y el responsable del grupo de aseguramiento de calidad que, de forma conjunta, revisarán el producto que corresponda en cada momento.</p>
<p>Una vez fijado sobre qué productos intermedios se llevarán a cabo las revisiones, el responsable de aseguramiento de calidad recoge la información necesaria de cada producto para poder establecer los criterios de revisión y más adelante, evaluar si el producto cumple las especificaciones, es decir, si se ha elaborado de acuerdo a unas características concretas como pueden ser la aplicación de una técnica específica, la inclusión de algún tipo de información, etc. Además, se debe contar con la normativa y estándares aplicables al proyecto de forma que, no sólo se asegure que el producto cumpla sus especificaciones, sino también del modo adecuado.</p>
<p>Si se detecta alguna desviación en cuanto a sus especificaciones o a los estándares aplicados, y se considera que es necesario realizar alguna modificación, el responsable del grupo de aseguramiento de calidad elabora un informe con el que el jefe de proyecto tomará las medidas que estime convenientes. Con dichos informes de calidad, el jefe de proyecto irá confeccionando el dossier de aseguramiento de calidad, que formará parte de la documentación del proyecto al finalizar el desarrollo.</p>
<h2 class="bio">Bibliografía</h2>
<ul class="bio"><li><a href="http://materias.fi.uba.ar/7507/content/20101/lecturas/documentacion_pruebas.pdf" rel="noopener" target="_blank">UBA (Universidad de Buenos Aires)</a></li>
<li><a href="https://administracionelectronica.gob.es/pae_Home/pae_Documentacion/pae_Metodolog/pae_Metrica_v3.html" rel="noopener" target="_blank">PAe (Métrica 3)</a></li>
</ul> </article>

# La calidad del software y su medida. Modelos, métricas,normas y estándares.

<article><h2>Introducción a la Calidad del Software</h2>
<h3>Introducción</h3>
<p>La <strong>Calidad del Software</strong> es “<em>la concordancia con los requerimientos funcionales y de rendimiento explícitamente establecidos con los estándares de desarrollo documentados y con las características implícitas que se esperan de todo software desarrollado profesionalmente</em>“. La Calidad del Software (CS) es una disciplina más dentro de la Ingeniería del Software. El principal instrumento para garantizar la calidad de las aplicaciones sigue siendo el Plan de Calidad, el cual se basa en normas o estándares genéricos y en procedimientos particulares. Los procedimientos pueden variar en cada organización, pero lo importante es que estén escritos, personalizados, adaptados a los procesos de la organización y que sean cumplidos.</p>
<p>Se puede decir que los requisitos del software son la base de las medidas de calidad y que la falta de concordancia con los requisitos es una falta de calidad. Los estándares o metodologías definen un conjunto de criterios de desarrollo que guían la forma en que se aplica la Ingeniería del Software. Si no se sigue ninguna metodología siempre habrá falta de calidad. Todas las metodologías y herramientas tienen un único fin, producir software de alta calidad.</p>
<p>A la hora de definir la calidad del software se debe diferenciar entre la calidad del Producto de software y la calidad del Proceso de desarrollo. No obstante, las metas que se establezcan para la calidad del producto van a determinar las metas a establecer para la calidad del proceso de desarrollo, ya que la calidad del producto va a estar en función de la calidad del proceso de desarrollo. Sin un buen proceso de desarrollo es casi imposible obtener un buen producto.</p>
<p>La calidad el producto de software se diferencia de la calidad de otros productos de fabricación industrial, ya que el software tiene ciertas características especiales:</p>
<ol><li>El software es un producto mental, no restringido por las leyes de la Física o por los límites de los procesos de fabricación.</li>
<li>Se desarrolla, no se fabrica. El coste está fundamentalmente en el proceso de diseño, no en la producción. Y los errores se introducen también en el diseño, no en la producción.</li>
<li>El software no se deteriora con el tiempo. No es susceptible a los efectos del entorno, y su curva de fallos es muy diferente a la del hardware. Todos los problemas que surjan durante el mantenimiento estaban desde el principio, y afectan a todas las copias del mismo; no se generan nuevos errores.</li>
<li>Es artesanal en gran medida. El software, en su mayoría, se construye a medida, en vez de ser construido ensamblando componentes existentes y ya probados, lo que dificulta aún más el control de su calidad.</li>
<li>El mantenimiento del software es mucho más complejo que el mantenimiento del hardware. Cuando un componente de hardware se deteriora se sustituye por una pieza de repuesto, pero cada fallo en el software implica un error en el diseño o en el proceso mediante el cual se tradujo el diseño en código de máquina ejecutable.</li>
<li>Es engañosamente fácil realizar cambios sobre un software, pero los efectos de estos cambios se pueden&nbsp; propagar de forma explosiva e incontrolada.</li>
<li>El software con errores no se rechaza. Se asume que es inevitable que el software presente errores.</li>
</ol><p>Es importante destacar que la calidad del software debe ser considerada en todos sus estados de evolución (especificaciones, diseño, código, etc). No basta con tener en cuenta la calidad del producto una vez finalizado, cuando los problemas de mala calidad ya no tienen solución o la solución es muy costosa.</p>
<p>La problemática general a la que se enfrenta el software es:</p>
<ol><li>Aumento constante del tamaño y complejidad de los programas.</li>
<li>Carácter dinámico e iterativo a lo largo de su ciclo de vida, es decir que los programas de software a lo largo de su vida cambian o evolucionan de una versión a otra para mejorar las prestaciones con respecto a las anteriores.</li>
<li>Dificultad de conseguir productos totalmente depurados, ya que en ningún caso un programa será perfecto.</li>
<li>Se dedican elevados recursos monetarios a su mantenimiento, debido a la dificultad que los proyectos de software entrañan y a la no normalización a la hora de realizar los proyectos.</li>
<li>No suelen estar terminados en los plazos previstos, ni con los costes estipulados, ni cumpliendo los niveles deseables de los requisitos especificados por el usuario.</li>
<li>Incrementos constantes de los costes de desarrollo debido entre otros, a los bajos niveles de productividad.</li>
<li>Los clientes tienen una alta dependencia de sus proveedores por ser en muchos casos aplicaciones a “medida”.</li>
<li>Procesos artesanales de producción con escasez de herramientas.</li>
<li>Insuficientes procedimientos normalizados para estipular y evaluar la calidad, costes y productividad.</li>
</ol><p>Uno de los principales problemas a los que nos enfrentamos a la hora de hablar de la calidad del software es el siguiente: ¿Es realmente posible encontrar un conjunto de propiedades en un software que nos den una indicación de su calidad? Para dar respuesta a esta pregunta aparecen los <strong>Modelos de Calidad</strong>. En los Modelos de Calidad, la calidad se define de forma jerárquica y tienen como objetivo resolver la complejidad mediante la descomposición.</p>
<p>La Calidad del Software debe implementarse en todo el ciclo de vida del mismo. Las distintas actividades para la implantación del control de calidad en el desarrollo de software son:</p>
<ol><li>Aplicación y metodología y técnicas de desarrollo.</li>
<li>Reutilización de procesos de revisión formales.</li>
<li>Prueba del software.</li>
<li>Ajustes a los estándares de desarrollo.</li>
<li>Control de cambios, mediciones y recopilación de información.</li>
<li>Gestión de informes sobre el control de calidad.</li>
</ol><p>La Calidad del Software es el conjunto de cualidades que lo caracterizan y que determinan su utilidad y existencia, la cual plantea un adecuado balanceo de eficiencia, confiabilidad, facilidad de mantenimiento, portabilidad, facilidad de uso, seguridad e integridad.</p>
<p>La implantación de un Modelo o Estándar requiere de una Gestión de la Calidad del Software. La Calidad se logra a través de la <strong>Gestión de la Calidad</strong>, la cual, según ISO 9000:2000, consiste en la realización de actividades coordinadas que permiten dirigir y controlar una organización en lo relativo a la calidad.</p>
<h3>Gestión de la Calidad del Software</h3>
<p>La Gestión de la Calidad del Software es una actividad esencial en cualquier empresa de software para asegurar la calidad de sus productos, y la competitividad frente a la oferta del mercado. Es un conjunto de actividades de la función general de la Dirección que determina la calidad, los objetivos y las responsabilidades. Se basa en la determinación y aplicación de las políticas de calidad de la empresa (objetivos y directrices generales). La Gestión o Administración de la Calidad se aplica normalmente a nivel empresa. También puede haber una gestión de la calidad dentro de la gestión de cada proyecto.</p>
<p>El propósito de la Administración de la Calidad del Software es, en primer lugar, entender las expectativas del cliente en términos de calidad y poner en práctica un plan proactivo para satisfacer esas expectativas. Dado que la calidad está definida por el cliente, podría parecer que es completamente subjetiva. De cualquier forma, hay muchas cosas acerca de la calidad que pueden hacerse objetivamente. Esto requiere examinar cada una de las características individuales del software y determinar una o más métricas que pueden recolectarse para reflejar dichas características. Por ejemplo, una característica de calidad puede ser que la solución tenga la menor cantidad de errores. Esta característica puede medirse contando los errores y defectos de la solución.</p>
<p>La Administración de la Calidad no es un evento, es un proceso y una forma de pensamiento. Un producto de software consistente, de alta calidad no puede producirse a partir de un proceso malo. Existe la necesidad de un ciclo constante de medir la calidad, actualizar el proceso, medir otra vez, actualizar, etc. Para hacer que la administración de calidad del software funcione, es vital recolectar métricas. Si no se capturan métricas será difícil mejorar los procesos a partir de una iniciativa de administración de calidad. Uno de los propósitos de la administración de la calidad del software es encontrar errores y defectos en el proyecto tan pronto como sea posible. Entonces, un buen proceso de administración de calidad tomará más esfuerzo y costo. De cualquier manera, habrá una gran recompensa al tiempo que el proyecto avanza.</p>
<p>Por ejemplo, es mucho más fácil arreglar un problema con los requerimientos de negocio durante la fase de análisis que tener que arreglar problemas durante las pruebas. En otras palabras, el equipo de proyecto debe intentar mantener una alta calidad durante el proceso de desarrollo de los productos de software, en vez de esperar arreglar problemas durante las pruebas cercanas al final del proyecto (o en el peor de los casos, cuando el cliente encuentra el problema después que el proyecto se completó).</p>
<p>Desde el punto de vista de la calidad, la Gestión de la Calidad del Software está formada por 4 partes, las cuales son:</p>
<ol><li><strong>Planificación</strong> de la Calidad del Software.</li>
<li><strong>Control</strong> de la Calidad del Software.</li>
<li><strong>Aseguramiento</strong> de la Calidad del Software.</li>
<li><strong>Mejora</strong> de la Calidad del Software.</li>
</ol><h4>Planificación de la Calidad del Software</h4>
<p>Según la Norma ISO 9000:2000, la planificación de la calidad es la parte de la gestión de la calidad enfocada al establecimiento de los objetivos de la calidad y a la especificación de los procesos operativos necesarios y de los recursos relacionados para cumplir los objetivos de calidad.</p>
<p>La Planificación de la Calidad del Software es la parte de la Gestión de la Calidad encargada de realizar el proceso administrativo de desarrollar y mantener una relación entre los objetivos y recursos de la organización; y las oportunidades cambiantes del mercado. El objetivo es modelar y remodelar los negocios y productos de la empresa, de manera que se combinen para producir un desarrollo y utilidades satisfactorias.</p>
<p>Los aspectos a considerar en la Planificación de la Calidad del Software son:</p>
<ul><li>Modelos/Estándar de Calidad del Software a utilizar.</li>
<li>Costos de la Calidad del Software.</li>
<li>Recursos humanos y materiales necesarios.</li>
</ul><p>Los factores que determinan el Modelo o Estándar de Calidad de Software a elegir son:</p>
<ol><li>La complejidad del proceso de diseño.</li>
<li>La madurez del diseño.</li>
<li>La complejidad del proceso de producción.</li>
<li>Las características del producto o servicio.</li>
<li>La seguridad del producto o servicio.</li>
<li>Económico.</li>
</ol><p>Según la Norma ISO/IEC 90003:2004 se puede decir que:&nbsp;“La planificación de la calidad facilita el modo de adaptar la planificación del sistema de gestión de la calidad a un proyecto especifico, producto o contrato. La planificación de la calidad puede incluir referencias genéricas y/o <em>proyecto/producto/contrato</em> específico de procedimientos, como apropiados. La planificación de la calidad debería ser revisada de nuevo junto con el progreso del diseño y desarrollo, y los elementos, en cada fase, deberían ser completamente definidos al comienzo de dicha fase.”.</p>
<p>La planificación de la calidad del software a nivel de proyectos debería considerar lo siguiente:</p>
<ol><li>Inclusión de los planes de desarrollo.</li>
<li>Los requisitos de calidad relacionados con los productos y/o procesos.</li>
<li>Los sistemas de gestión de la calidad adaptando y/o identificando los procesos e instrucciones específicos, apropiados para el ámbito del manual de calidad y algunas exclusiones expuestas.</li>
<li>Los procesos de proyectos-específicos e instrucciones, tales como, especificación de pruebas del software detallando los planes, diseños, casos de pruebas y procesos para la unidad, integración, sistemas y pruebas de aceptación.</li>
<li>Los métodos, modelos, herramientas, convenios de lenguajes de programación, bibliotecas,&nbsp; marcos de trabajo y otros componentes reutilizables para ser usados en los proyectos.</li>
<li>Los criterios para el comienzo y el final de cada fase o etapa del proyecto.</li>
<li>Los tipos de análisis y otras verificaciones y actividades de validación para ser llevadas a cabo.</li>
<li>Los procesos de gestión de la configuración para ser llevados a cabo.</li>
<li>Las actividades de seguimiento y las medidas para ser llevadas a cabo.</li>
<li>Las personas responsables de aprobar de procesos de salida para su uso posterior.</li>
<li>La formación necesaria para el uso de herramientas y técnicas, y la organización de la formación previa a la habilidad necesaria.</li>
<li>Los registros para ser mantenidos.</li>
<li>La gestión de cambios, como por ejemplo, para recursos, escalas de tiempo y cambios de contrato.</li>
</ol><p>La planificación de la calidad, sin embargo, abreviada es particularmente útil para limitar los objetivos de calidad para los software siendo designados para un propósito limitado.</p>
<p>Según Humphrey (1989) un plan de calidad puede tener la siguiente estructura:</p>
<ol><li>Introducción al Producto: una descripción del producto, su objetivo en el mercado y expectativas de calidad del producto.</li>
<li>Planes del producto: Fechas críticas respecto de la liberación del producto y responsabilidades del producto respecto de su distribución y servicio.</li>
<li>Descripción del proceso: Procesos de desarrollo y servicios que serían usados en el desarrollo y en la administración.</li>
<li>Objetivos de Calidad: Objetivos y planes de calidad del producto, los cuales incluyen la identificación de los atributos de calidad del producto.</li>
<li>Manejo del riesgo: principales riesgos que pueden afectar la calidad del producto.</li>
</ol><p>Esta información puede ser presentada en diferentes documentos.</p>
<p>El plan de calidad define los atributos de calidad más importantes del producto a ser desarrollado y define el proceso de evaluación de la calidad.</p>
<p>En la Planificación de la Calidad del Software se debe determinar:</p>
<ol><li>Rol de la Planificación.</li>
<li>Requerimientos de la Calidad del Software.</li>
<li>Preparación de un Plan de Calidad del Software.</li>
<li>Implementación de un Plan de Calidad del Software.</li>
<li>Preparar un Manual de Calidad.</li>
</ol><h4>Control de la Calidad del Software</h4>
<p>Según la Norma ISO 9000:2000, el control de la calidad es la parte de la gestión de la calidad orientada al cumplimiento de los requisitos de la calidad.</p>
<p>El Control de la Calidad del Software son las técnicas y actividades de carácter operativo, utilizadas para satisfacer los requisitos relativos a la calidad, centradas en 2 objetivos fundamentales:</p>
<ol><li>Mantener bajo control un proceso.</li>
<li>Eliminar las causas de los defectos en las diferentes fases del ciclo de vida.</li>
</ol><p>Está formado por actividades que permiten evaluar la calidad de los productos de software desarrollados. El aspecto a considerar en el Control de la Calidad del Software es la “Prueba del Software”.</p>
<p>Las <strong>Pruebas de Software</strong> presentan una interesante anomalía para el Ingeniero del Software. Durante las fases anteriores de definición y de desarrollo, el Ingeniero intenta construir el software partiendo de un concepto abstracto y llegando a una implementación tangible. Luego, llegan las pruebas. El Ingeniero crea una serie de casos de prueba que intentar “demoler” el software construido. De hecho, las pruebas son uno de los pasos de la Ingeniería del Software que se puede ver como destructivo en lugar de constructivo.</p>
<p>Las Etapas del Desarrollo de Software son:</p>
<ul><li>Análisis</li>
<li>Diseño</li>
<li>Implementación</li>
<li>Pruebas</li>
<li>Mantenimiento</li>
</ul><p>La prueba es el proceso de ejecutar un programa con intención de encontrar defectos. Es un proceso destructivo que determina el diseño de los casos de prueba y la asignación de responsabilidades.</p>
<p>La prueba exitosa es aquella que descubre defectos. El “caso de prueba bueno” es aquel que tiene alta probabilidad de detectar un defecto aún no descubierto. El “caso de prueba exitoso” es aquel que detecta un defecto aún no descubierto.</p>
<p>La prueba no es:</p>
<ol><li>Demostración que no hay errores.</li>
<li>Demostración que el software desempeña correctamente sus funciones.</li>
<li>Establecimiento de confianza que un programa hace lo que debe hacer.</li>
</ol><p>La prueba demuestra hasta qué punto las funciones del software parecen funcionar de acuerdo con las especificaciones y parecen alcanzarse los requisitos de rendimiento. Además, los datos que se van recogiendo a medida que se lleva a cabo la prueba proporcionan una buena indicación de la confiabilidad del software e indican la calidad del software como un todo. Pero, la prueba no puede asegurar la ausencia de defectos; sólo puede demostrar que existen defectos en el software.</p>
<p>La prueba del software es un concepto más amplio que, a menudo, es conocido como verificación y validación (V&amp;V):</p>
<ul><li>La <strong>verificación</strong> se refiere al conjunto de actividades que aseguran que el software implementa correctamente una función específica. Su pregunta asociada es:&nbsp; ¿estamos construyendo el producto correctamente?</li>
<li>La <strong>validación</strong> se refiere a un conjunto diferente de actividades que aseguran que el software construido se ajusta a los requisitos del cliente. Su pregunta asociada es: ¿estamos construyendo el producto correcto?. La validación del software se consigue mediante una serie de pruebas de caja negra que demuestran la conformidad respecto de los requisitos del cliente. Un plan de prueba traza las clases de pruebas que se han de llevar a cabo, y un procedimiento de prueba define los casos de prueba específicos en un intento por descubrir errores de acuerdo con los requisitos.</li>
</ul><p>Los principios básicos de la pruebas de software son:</p>
<ol><li>A todas las pruebas se les debería poder hacer un seguimiento hasta los requisitos del cliente.</li>
<li>Las pruebas deberían planificarse mucho antes que empiecen.</li>
<li>Las pruebas deberían empezar por “lo pequeño” y progresar hacia “lo grande”.</li>
<li>Para ser más eficaces, las pruebas deberían ser realizadas por un equipo independiente.</li>
</ol><p>Una estrategia de prueba de software integra las técnicas de diseño de casos de prueba en una serie de pasos bien planificados que dan como resultado una correcta construcción del software. La estrategia proporciona un mapa que describe los pasos que hay que llevar a cabo como parte de la prueba, cuándo se deben planificar y realizar esos pasos, y cuánto esfuerzo, tiempo y recursos se van a requerir. Cualquier estrategia de prueba debe incorporar la planificación de la prueba, el diseño de casos de prueba, la ejecución de las pruebas; y la agrupación y evaluación de los datos resultantes.</p>
<p>Las características generales de las estrategias de prueba de software son las siguientes:</p>
<ol><li>La prueba comienza en el nivel módulo y trabaja “hacia fuera”, hacia la integración de todo el sistema basado en computadora.</li>
<li>Diferentes técnicas de prueba son apropiadas en diferentes momentos.</li>
<li>La prueba la realiza el que desarrolla el software y un grupo de prueba independiente.</li>
<li>La prueba y la depuración son actividades, pero la depuración se puede incluir en cualquier estrategia de prueba.</li>
</ol><p>Para implementar con éxito una estrategia de prueba de software, se debe:</p>
<ol><li>Especificar los requisitos del producto de manera cuantificable antes que comiencen las pruebas.</li>
<li>Especificar los objetivos de prueba de manera explícita.</li>
<li>Desarrollar un plan de prueba de haga hincapié en la prueba de ciclo rápido.</li>
<li>Construir un software robusto diseñado para probarse a sí mismo.</li>
<li>Usar revisiones de técnicas formales efectivas como filtro antes de la prueba.</li>
<li>Realizar revisiones técnicas formales para evaluar la estructura de la prueba y los propios casos de prueba.</li>
<li>Desarrollar un enfoque de mejora continua al proceso de prueba.</li>
</ol><p>Existen 2 enfoques de estrategia de prueba de software: uno tradicional y otro relacionado al ambiente Cliente/Servidor.</p>
<ul><li><strong>Estrategia Tradicional</strong></li>
</ul><p>Una estrategia Tradicional de prueba del software debe incluir pruebas de bajo nivel que verifiquen que todos los pequeños segmentos de código fuente se han implementado correctamente, así como pruebas de alto nivel que validen las principales funciones del sistema frente a los requisitos del cliente. Una estrategia proporciona un conjunto de hitos. Debido a que los pasos de la estrategia de prueba se dan cuando aumenta la presión de los plazos fijados, se debe poder medir el progreso y los problemas deben aparecer lo antes posible.</p>
<p>Inicialmente, la prueba se centra en cada módulo individualmente, asegurando que funciona adecuadamente como una unidad. La <strong>prueba de unidad</strong> hace un uso intensivo de las técnicas de prueba de caja blanca, ejercitando caminos específicos de la estructura de control del módulo para asegurar un alcance completo y una detección máxima de errores. La prueba de unidad centra el proceso de verificación en la menor unidad del diseño del software: el componente de software o módulo. Se prueba la interfaz del módulo para asegurar que la información fluye de forma adecuada hacia y desde la unidad de programa que está siendo probada. Se examinan las estructuras de datos locales para asegurar que los datos que se mantienen temporalmente conservan su integridad durante todos los pasos de ejecución del algoritmo. Se prueban las condiciones límite para asegurar que el módulo funciona correctamente en los límites establecidos. Se ejercitan todos los caminos independientes de la estructura de control con el el fin de asegurar que todas las sentencias del módulo se ejecutan por lo menos una vez. Y, finalmente, se prueban todos los caminos de manejo de errores. Antes de iniciar cualquier otra prueba es preciso probar el flujo de datos de la interfaz del módulo. Si los datos no entran correctamente, todas las demás pruebas no tienen sentido. Además de las estructuras de datos locales, durante la prueba de unidad se debe comprobar el impacto de los datos globales sobre el módulo.</p>
<p>A continuación, se deben ensamblar o integrar los módulos para formar el paquete de software completo. La <strong>prueba de integración</strong> es una técnica sistemática que permite construir la estructura del programa mientras que, al mismo tiempo, se llevan a cabo pruebas para detectar errores asociados con la interacción. El objetivo es juntar los módulos probados mediante la prueba de unidad y construir una estructura de programa que esté de acuerdo con lo que dicta el diseño. Se combinan todos las módulo por anticipado. Se prueba todo el programa en conjunto. Se encuentra un gran conjunto de errores. La corrección se hace difícil, ya que es complicado aislar las causas al tener el programa entero en toda su extensión. Una vez que se corrigen esos errores aparecen otros nuevos y el proceso continúa en lo que parece ser un ciclo sin fin.</p>
<p>Después que el software se ha integrado, se dirigen un conjunto de pruebas de alto nivel. Se deben comprobar los criterios de validación establecidos durante el análisis de requisitos. La <strong>prueba de validación</strong> proporciona una seguridad final que el software satisface todos los requisitos funcionales, de comportamiento y de rendimiento. Durante la validación se usan exclusivamente técnicas de prueba de caja negra.</p>
<p>El software, una vez validado, se debe combinar con otros elementos del sistema. La <strong>prueba del sistema</strong> verifica que cada elemento se ajusta de forma adecuada y que se alcanza la funcionalidad y el rendimiento del sistema total. La prueba del sistema está constituida por una serie de pruebas diferentes cuyo propósito primordial es ejercitar profundamente el sistema basado en computadora. Aunque cada prueba tiene un propósito diferente, todas trabajan para verificar que se ha integrado adecuadamente todos los elementos del sistema y que realizan las funciones apropiadas.</p>
<p>La <strong>prueba de regresión</strong> es volver a ejecutar un subconjunto de pruebas que se han llevado a cabo anteriormente para asegurarse que los cambios no han propagado efectos colaterales no deseados. Este tipo de prueba es la actividad que ayuda a asegurar que los cambios no introduzcan un comportamiento no deseado o errores adicionales. A medida que progresa la prueba de regresión, el número de pruebas de regresión puede crecer demasiado. Por lo tanto, el conjunto de pruebas de regresión debería diseñarse para incluir sólo aquellas pruebas que traten una o más clases de errores en cada una de las funciones principales del programa. No es práctico ni eficiente volver a ejecutar cada prueba de cada función del problema después de un cambio.</p>
<p>Cuando se construye un software a medida para un cliente, se llevan a cabo una serie de pruebas de aceptación para permitir que el cliente valide todos los requisitos. Estas pruebas las realiza el usuario final en lugar del responsable del desarrollo de sistema. Una prueba de aceptación puede ir desde un informal paso de prueba hasta la ejecución sistemática de una serie de pruebas bien planificadas.</p>
<p>La <strong>prueba alfa</strong> la realiza el cliente en el lugar del área de desarrollo. Se usa el software de forma natural con el desarrollador como observador del usuario y registrando los errores y los problemas de uso. Las pruebas alfa se realizan en un entorno controlado.</p>
<p>La <strong>prueba beta</strong> la realiza el usuario final del software en los lugares de trabajo de los clientes. La prueba beta es una aplicación en vivo del software en su entorno que no puede ser controlado por el desarrollador. El cliente registra todos los problemas que encuentra durante la prueba beta e informa a intervalos regulares al desarrollador. Como resultado de los problemas informados durante la prueba beta, el desarrollador del software realiza modificaciones y prepara una versión del producto de software para toda clase de clientes.</p>
<ul><li><strong>Estrategia Cliente/Servidor</strong></li>
</ul><p>La naturaleza distribuida de los sistemas Cliente/Servidor (C/S) plantea un conjunto de problemas específicos en la prueba del software, entre los cuales se pueden mencionar:</p>
<ol><li>Consideraciones del GUI de cliente.</li>
<li>Consideraciones del entorno destino y de la diversidad de plataformas.</li>
<li>Consideraciones de bases de datos distribuidas.</li>
<li>Consideraciones de procesamiento distribuido.</li>
<li>Entornos destino que no son robustos.</li>
<li>Relaciones de rendimiento no lineales.</li>
</ol><p>En general, las pruebas de software C/S se producen en 3 niveles:</p>
<ol><li>Aplicaciones de cliente individuales: se prueban de modo desconectado (no se consideran el funcionamiento del servidor y de la red subyacente).</li>
<li>Aplicaciones de software de cliente y del servidor asociado: se prueban, pero no se ejercitan específicamente las operaciones de red.</li>
<li>Se prueba la arquitectura completa de C/S, incluyendo el rendimiento y funcionamiento de la red.</li>
</ol><p>Los enfoques de pruebas para aplicaciones C/S son:</p>
<ol><li>Pruebas de función de aplicación: Se prueba la funcionalidad de las aplicaciones cliente utilizando métodos. La aplicación se prueba en solitario en un intento de descubrir errores en su funcionamiento.</li>
<li>Pruebas de servidor: Se prueban la coordinación y las funciones de gestión de datos del servidor. Se considera el rendimiento del servidor (tiempo de respuesta y traspaso de datos en general).</li>
<li>Pruebas de bases de datos: Se prueba la precisión e integridad de los datos almacenados en el servidor. Se examinan las transacciones enviadas por las aplicaciones cliente para asegurar que los datos se almacenen, actualicen y recuperen adecuadamente. También se prueba el archivo de datos.</li>
<li>Pruebas de transacciones: Se crea una serie de pruebas adecuadas para comprobar que todas las clases de transacciones se procesen de acuerdo con los requisitos. Las transacciones hacen hincapié en la corrección de procesamiento y en los temas de rendimiento (tiempo de procesamiento de transacciones y comprobación de volúmenes de transacciones).</li>
<li>Pruebas de comunicaciones a través de la red: Estas prueban verifican que la comunicación entre los nodos de la red se produzca correctamente, y que el paso de mensajes, las transacciones y el tráfico de red tengan lugar sin errores. También se pueden efectuar pruebas de seguridad de red como parte de esta actividad de prueba.</li>
</ol><p>Para llevar a cabo estos enfoques de prueba, se recomienda el desarrollo de perfiles operativos derivados de escenarios C/S. Un perfil operativo indica la forma en que los distintos tipos de usuarios interactúan con el sistema C/S. Esto proporciona un patrón de uso que se puede aplicar cuando se diseñan y ejecutan las pruebas.</p>
<p>La estrategia para probar una arquitectura C/S comienza por comprobar una única aplicación de cliente. La integración de los clientes, del servidor y de la red se irá probando progresivamente. Finalmente, se prueba todo el sistema como entidad operativa. La integración de módulos en el desarrollo C/S puede tener algunos aspectos ascendentes o descendentes, pero la integración en proyectos C/S tiene más hacia el desarrollo paralelo y hacia la integración de módulos en todos los niveles de diseño.</p>
<p>La naturaleza multiplataforma en red de los sistemas C/S requiere que se preste más atención a la prueba de configuraciones y a la prueba de compatibilidades. La doctrina de prueba de configuraciones impone la prueba del sistema en todos los entornos conocidos de hardware y software en los cuales vaya a funcionar. La prueba de compatibilidad asegura una interfaz funcionalmente consistente entre plataformas de software y hardware.</p>
<p>Respecto de la organización de las pruebas del software, se puede decir que en cualquier proyecto de software existe un conflicto de intereses inherente que aparece cuando comienza la prueba. Se pide a la gente que ha construido el software que lo pruebe. Esto parece totalmente inofensivo; después de todo, ¿quién podría conocer mejor un programa que los que lo han desarrollado? El que desarrolla el software siempre es responsable de probar los módulos del programa, asegurándose que cada uno lleva a cabo la función para la que fue diseñada. En muchos casos se encargará de la prueba de integración, el paso de las pruebas que lleva a la construcción (y prueba) de la estructura total del sistema.</p>
<p>Las consideraciones para generar un plan de pruebas son:</p>
<ol><li>Métodos de prueba.</li>
<li>Infraestructura (para desarrollo de software de prueba y ejecución de las pruebas).</li>
<li>Automatización de las pruebas.</li>
<li>Software de apoyo.</li>
<li>Administración de la configuración.</li>
<li>Riesgos.</li>
</ol><p>Se requiere un plan global y uno detallado para cada actividad de prueba (pruebas unitarias, de integración, de facilidad de uso, funcionales, de sistema y de aceptación).</p>
<p>El formato del plan de pruebas es:</p>
<ol><li>Propósito: Prescribir el ámbito, enfoque, recursos y plazos de las actividades de prueba.</li>
<li>Esquema: Identificador, Introducción, Items de prueba, Características a ser probadas, Características a no ser probadas, Enfoque, Criterios de aprobación por Item, Criterios de suspensión y requerimientos de continuación, Entrega de la prueba, Tareas de la prueba, Necesidades ambientales, Necesidades de personal y entrenamiento, Calendario, Riesgos y Contingencias, Aprobaciones.</li>
<li>Especificación de Prueba (complemento): Especificación de arquitectura de prueba, Implementación de las pruebas, Especificación de diseño de pruebas, Especificación de caso de prueba, Especificación de procedimiento de prueba, Ejecución de las pruebas, Evaluación de las pruebas.</li>
</ol><p>El <strong>diseño de casos de prueba</strong> para el software o para otros productos de ingeniería puede requerir tanto esfuerzo como el propio diseño inicial del producto. Sin embargo, los Ingenieros de Software tratan las pruebas como algo sin importancia, desarrollando casos de prueba que “parezcan adecuados”, pero que tienen poca garantía de ser completos. Se deben diseñar pruebas que tengan la mayor probabilidad de encontrar el mayor número de errores con la mínima cantidad de esfuerzo y tiempo posible. Cualquier producto de ingeniería puede probarse de una de estas 2 formas:</p>
<ul><li><strong>Prueba de caja negra</strong>:<br/>
Cuando se considera el software de computadora, la prueba de caja negra se refiere a las pruebas que se llevan a cabo sobre la interfaz del software. Los casos de prueba pretenden demostrar que las funciones del software son operativas, que la entrada se acepta de forma adecuada y que se produce un resultado correcto, así como que la integridad de la información externa se mantiene. Este tipo de prueba examina algunos aspectos del modelo fundamental del sistema sin tener mucho encuentra la estructura lógica interna del software. Los métodos de prueba de la caja negra se centran en los requisitos funcionales de software. La prueba de la caja negra permite al Ingeniero del Software obtener conjuntos de condicionales de entrada que ejerciten completamente todos los requisitos funcionales de un programa. La prueba de la caja negra no es una alternativa a las técnicas de prueba de la caja blanca. La prueba de la caja negra intenta encontrar errores de las siguientes categorías:<br/>
1) Funciones incorrectas o ausentes.<br/>
2) Errores de interfaz.<br/>
3) Errores en estructuras de datos o en acceso a bases de datos externas.<br/>
4) Errores de rendimiento.<br/>
5) Errores de inicialización y terminación.</li>
</ul><ul><li><strong>Prueba de caja blanca</strong><br/>
La prueba de caja blanca del software se basa en el minucioso examen de los detalles procedimentales. Se comprueban los caminos lógicos del software proponiendo casos de prueba que ejerciten conjuntos específicos de condiciones y/o bucles. Se puede examinar el estado del programa en varios puntos para determinar si el estado real coincide con el esperado o mencionado. Para este tipo de prueba, se deben definir todos los caminos lógicos y desarrollar casos de prueba que ejerciten la lógica del programa. La prueba de caja blanca no se debe desechar como impracticable. Se pueden elegir y ejercitar una serie de caminos lógicos importantes. Se pueden comprobar las estructuras de datos para verificar su validez. Se pueden combinar los atributos de la prueba de caja blanca y de caja negra, para llegar a un método que valide la interfaz del software y asegure el correcto funcionamiento interno del software. La prueba de caja blanca, denominada prueba de caja de cristal, es un método de diseño de casos de prueba que usa la estructura de control del diseño procedimental para obtener los casos de prueba.</li>
</ul><p>Una “buena prueba” tiene los siguientes atributos:</p>
<ol><li>Una alta probabilidad de encontrar un error – Para alcanzar este objetivo, el responsable de la prueba debe entender el software e intentar desarrollar una imagen mental de cómo podría fallar el software.</li>
<li>No debe ser redundante – El tiempo y los recursos para las pruebas son limitados. No hay motivo para realizar una prueba que tiene el mismo propósito que otra. Todas las pruebas deberían tener un propósito diferente.</li>
<li>Debería ser la mejor de la cosecha – En un grupo de pruebas que tienen un propósito similar, las limitaciones de tiempo y recursos pueden abogar por la ejecución de sólo un subconjunto de estas pruebas. En tales casos, se debería emplear la prueba que tenga la más alta probabilidad de descubrir una clase entera de errores.</li>
<li>No debería ser ni demasiado sencilla ni demasiado compleja – Es posible combinar una serie de pruebas en un caso de prueba, los posibles efectos secundarios de este enfoque puede enmascarar errores. En general, cada prueba debería realizarse separadamente.</li>
</ol><p>El uso de herramientas de prueba puede hacer la prueba más fácil, efectiva y productiva.</p>
<p>Existen distintos tipos de herramientas por actividad:</p>
<ol><li>Para revisiones e inspecciones: Análisis de complejidad, comprensión de código, análisis sintáctico y semántico.</li>
<li>Para planificación de pruebas: Modelos (templates) para documentación de planes de prueba, estimación de esfuerzo y calendarización de pruebas, analizador de complejidad.</li>
<li>Para diseño y desarrollo de pruebas: Generador de casos de prueba, diseño de prueba basado en requerimientos, captura y análisis de cobertura.</li>
<li>Para ejecución de pruebas: Captura, análisis de cobertura, pruebas de memoria, administración de los casos de prueba, simuladores y rendimiento.</li>
<li>Para soporte: Administración de problemas, administración de la configuración.</li>
</ol><h4>Aseguramiento de la Calidad del Software</h4>
<p>Según la Norma ISO 9000:2000, el aseguramiento de la calidad es la parte de la gestión de la calidad orientada a proporcionar confianza en que se cumplirán los requisitos de calidad.</p>
<p>El Aseguramiento de Calidad del Software es el conjunto de actividades planificadas y sistemáticas necesarias para aportar la confianza que el software satisfará los requisitos dados de calidad. Este aseguramiento se diseña para cada aplicación antes de comenzar a desarrollarla y no después. El aseguramiento de la calidad del software engloba:</p>
<ol><li>Un enfoque de gestión de calidad.</li>
<li>Métodos y herramientas de Ingeniería del Software.</li>
<li>Revisiones técnicas formales aplicables en el proceso de software.</li>
<li>Una estrategia de prueba multiescala.</li>
<li>Procedimientos para ajustarse a los estándares de desarrollo del software.</li>
<li>Mecanismos de medición y de generación de informes.</li>
</ol><p>Las revisiones del software son un “filtro” para el proceso de Ingeniería del Software. Esto es, las revisiones se aplican a varios momentos del desarrollo del software y sirven para detectar errores y defectos que pueden ser eliminados. Las revisiones del software sirven para “purificar” las actividades de la Ingeniería del Software que suceden como resultado del análisis, diseño y codificación.</p>
<p>La revisión técnica formal (RTF), a veces llamada inspección, es el filtro más efectivo desde el punto de vista del aseguramiento de la calidad y es un medio efectivo para mejorar la calidad del software.</p>
<p>El defecto se define como una anomalía del producto. Dentro del contexto del proceso del software, los términos defecto y fallo son sinónimos. Ambos implican un problema de calidad que es descubierto después de entregar el software a los usuarios finales.</p>
<p>El objetivo principal delas RTF es encontrar errores durante el proceso, de forma que se conviertan en defectos después de la entrega del software. El beneficio de estas RTF es el descubrimiento de errores al principio para que no se propaguen al paso siguiente del proceso de software.</p>
<p>Los objetivos de la RTF son:</p>
<ol><li>Descubrir errores en la función, la lógica o la implementación de cualquier representación del software.</li>
<li>Verificar que el software bajo revisión alcanza sus requisitos.</li>
<li>Garantizar que el software ha sido representado de acuerdo con ciertos estándares predefinidos.</li>
<li>Conseguir un software desarrollado en forma uniforme.</li>
<li>Hacer que los proyectos sean más manejables.</li>
</ol><p>El aseguramiento de calidad se refiere a validar los procesos usados para crear los productos. Es una herramienta especialmente útil para administradores y patrocinadores, ya que permite discutir los procesos usados para crear los productos para determinar si son razonables. Este aseguramiento tiene asociado 2 constitutivos diferentes: los Ingenieros de Software que realizan el trabajo técnico y un grupo de SQA (Software Quality Assurance) que tiene la responsabilidad de la planificación de aseguramiento de la calidad, supervisión, mantenimiento de registros, análisis e informes.</p>
<p>Las Actividades del SQA son:</p>
<ol><li>Establecimiento de un plan de SQA para un proyecto.</li>
<li>Participación en el desarrollo de la descripción del proceso de software del proyecto.</li>
<li>Revisión de las actividades de Ingeniería del Software para verificar su ajuste al proceso de software definido.</li>
<li>Auditoría de los productos de software designados para verificar el ajuste con los definidos como parte del proceso del software.</li>
<li>Asegurar que las desviaciones del trabajo y los productos del software se documentan y se manejan de acuerdo con un procedimiento establecido.</li>
<li>Registrar lo que no se ajuste a los requisitos e informar a sus superiores.</li>
</ol><p>Además de estas actividades, el grupo de SQA coordina el control y la gestión de cambios y; ayuda a recopilar y analizar las <strong>métricas del software</strong>.</p>
<p>Las métricas son escalas de unidades sobre las cuales puede medirse un atributo cuantificable. Cuando se habla de software nos referimos a la disciplina de recopilar y analizar datos basándonos en mediciones reales de software, así como a las escalas de medición. Los atributos son características observables del producto o del proceso de software, que proporciona alguna información útil sobre el estado del producto o sobre el progreso del proyecto. El término producto se utiliza para referirse a las especificaciones, a los diseños y a los listados del código. Los valores de las métricas no se obtienen sólo por mediciones. Algunos valores de métricas se derivan de los requisitos del cliente o de los usuarios y, por lo tanto, actúan como restricciones dentro del proyecto.</p>
<p>Los principios básicos de la medición son:</p>
<ol><li>Los objetivos de la medición deberían establecerse antes de empezar la recopilación de datos.</li>
<li>Todas las técnicas sobre métricas deberían definirse sin ambigüedades.</li>
<li>Las métricas deberían obtenerse basándose en una teoría válida para el dominio de aplicación.</li>
<li>Hay que hacer las métricas a medida para acomodar mejor los productos y procesos específicos.</li>
<li>Siempre que sea posible, la recopilación de datos y el análisis debería automatizarse.</li>
<li>Se deberían aplicar técnicas estadísticas válidas para establecer las relaciones entre los atributos internos del producto y las características externas de la calidad.</li>
</ol><p>Las Razones que justifican la Medición del Software son:</p>
<ol><li>Para indicar la calidad del producto.</li>
<li>Para evaluar la productividad de la gente que desarrolla el producto.</li>
<li>Para evaluar los beneficios (en términos de productividad y calidad) derivados del uso de nuevos métodos y herramientas de Ingeniería de Software.</li>
<li>Para establecer una línea base de estimación.</li>
<li>Para ayudar a justificar el uso de nuevas herramientas o formación adicional.</li>
</ol><p>Las actividades del proceso de medición son:</p>
<ol><li>Formulación: Obtención de medidas y métricas apropiadas para la representación del software.</li>
<li>Colección: Mecanismo empleado para acumular datos necesarios para obtener las métricas formuladas.</li>
<li>Análisis: Cálculo de las métricas y aplicación de herramientas matemáticas.</li>
<li>Interpretación: La evaluación de los resultados de las métricas en un esfuerzo por conseguir una visión interna de la calidad de la presentación.</li>
<li>Retroalimentación: Recomendaciones obtenidas de la interpretación de métricas y técnicas transmitidas al equipo de desarrollo de software.</li>
</ol><p>Los sistemas métricos necesitan tres tipos de valores:</p>
<ol><li>Objetivos: Se basan habitualmente en consideraciones comerciales.</li>
<li>Predicciones: Indican la viabilidad de los objetivos. Se basan en las características del producto con el que tratamos.</li>
<li>Valores Reales: Pueden ser comparados con los objetivos para supervisar la progresión del proyecto. Son mediciones discretas de los atributos del software. Es preferible utilizar mediciones objetivas basadas en reglas. Algunas mediciones se basan en estimaciones donde un valor más que medirse se evalúa.</li>
</ol><p>Las medidas de Calidad del Software deben comenzar desde la especificación y terminar con la implementación, implantación y mantenimiento o post-implantación. Debe aplicarse a lo largo de todo el proceso de Ingeniería de Software. Básicamente, la medición es una fase normal de cualquier actividad industrial. Sin mediciones es imposible perseguir objetivos comerciales normales de una manera racional.</p>
<p>Existen métricas a nivel Proyecto, Proceso y Producto respectivamente.</p>
<p><strong>Métricas de Proyecto</strong></p>
<p>Las métricas de Proyecto se consolidan para crear métricas de proceso que sean públicas para toda la organización del software. El uso de métricas para el Proyecto tiene 2 aspectos fundamentales:</p>
<ol><li>Minimizar la planificación del desarrollo haciendo los ajustes necesarios que eviten retrasos y reducir problemas/riesgos potenciales.</li>
<li>Evaluar la calidad de los productos en el momento actual y cuando sea necesario, modificando el enfoque técnico que mejore la calidad.</li>
</ol><p>Los indicadores de proyecto permiten al gestor de proyectos de software:</p>
<ol><li>Evaluar el estado del proyecto.</li>
<li>Seguir la pista de los riesgos potenciales.</li>
<li>Detectar las&nbsp; áreas de problemas antes de que se conviertan en “críticas”.</li>
<li>Ajustar el flujo y las tareas del trabajo.</li>
<li>Evaluar la habilidad del equipo del proyecto en controlar la calidad de los productos de trabajo del software.</li>
</ol><p><strong>Métricas de Proceso</strong></p>
<p>Las métricas del Proceso se recopilan de todos los proyectos y durante un largo período de tiempo. Su intento es proporcionar indicadores que lleven a mejorar los procesos de software a largo plazo. Se tendrán métricas asociadas a cada proceso del software (p.e. métricas de implementación). Estos indicadores de proceso permiten que una organización de Ingeniería de Software pueda tener una visión más profunda de la eficacia de un proceso ya existente y permiten que los gestores evalúen lo que funciona y lo que no.</p>
<p>En realidad, las medidas que recopila un equipo de proyecto y las convierte en métricas para utilizarse durante un proyecto, también pueden trasmitirse a los que tienen la responsabilidad de mejorar el proceso de software. Por esta razón, se utilizan muchas de las mismas métricas tanto en el dominio del proceso como en el del proyecto.</p>
<p>La única forma racional de mejorar cualquier proceso es medir atributos del proceso, desarrollar un juego de métricas significativas según estos atributos y utilizar las métricas para proporcionar indicadores que conducirán a una estrategia de mejora.</p>
<p>Las métricas del proceso se caracterizan por:</p>
<ol><li>El control y ejecución del proyecto.</li>
<li>Medición de tiempos del análisis, diseño, implementación, implantación y post-implantación.</li>
<li>Medición de las pruebas (errores, cubrimiento, resultado en número de defectos y número de éxito).</li>
<li>Medición de la transformación o evolución del producto.</li>
</ol><p><strong>Métricas de Producto</strong></p>
<p>Las métricas de Producto son privadas para un individuo y a menudo se combinan para desarrollar métricas del proyecto que sean públicas para un equipo de software. Están enfocadas a predecir y controlar:</p>
<ol><li>El tamaño (líneas de código, bytes de código, operadores y operandos).</li>
<li>La estructura (control de flujo, relación entre componentes, cohesión y acoplamiento).</li>
<li>La complejidad (combinación de tamaño y estructura).</li>
<li>Los índices para controlar la documentación.</li>
<li>La calidad (independencia, completo, entendible, aumentado).</li>
<li>La estabilidad (los cambios aumentan el número de fallas, los cambios se pueden dar por definición de requerimientos o por cambios del entorno).</li>
</ol><p>Las métricas del software deberían tener las siguientes características:</p>
<ol><li>Simple y fácil de calcular.</li>
<li>Empírica e intuitivamente persuasiva: Debe satisfacer las nociones intuitivas del desarrollador sobre el atributo del producto en evaluación.</li>
<li>Consistente y objetiva: Presentar resultados sin ambigüedad.</li>
<li>Consistente en el empleo de unidades y tamaños: Deben emplearse medidas que no conduzcan a extrañas combinaciones de unidades.</li>
<li>Independiente del lenguaje de programación.</li>
<li>Mecanismo para retroalimentación de calidad: Debe proporcionar información para obtener un producto final de mayor calidad.</li>
</ol><p>Las métricas a recabar dependen de los objetivos del negocio en particular. Los desarrolladores tienen a la vez objetivos comunes como, respetar el presupuesto y respetar los plazos, minimizar las tasas de defectos antes y después de la entrega del producto e intentar mejorar la calidad y la productividad. Las métricas deben ayudar a la evaluación de las representaciones del modelo lógico y físico, deben tener la capacidad de intuir sobre la complejidad del diseño y construcción; y deben ayudar en el diseño de casos de prueba.</p>
<h4>Mejora en la Calidad del Software</h4>
<p>Según la Norma ISO 9000:2000, la mejora de la calidad es la parte de la gestión de la calidad orientada a aumentar la capacidad de cumplir con los requisitos de la calidad. Los requisitos pueden estar relacionados con cualquier aspecto tal como la eficacia, la eficiencia o la trazabilidad.</p>
<p>La Mejora de la Calidad del Software es la parte de la Gestión de la Calidad que contribuye, por medio de las mediciones, a los análisis de los datos y auditorias, a efectuar mejoras en la calidad del software.</p>
<p>Una Auditoria de Calidad tiene como objetivo mostrar la situación real para aportar confianza y destacar las áreas que pueden afectar adversamente esa confianza. Otro objetivo consiste en suministrar una evaluación objetiva de los productos y procesos para corroborar la conformidad con los estándares, las guías, las especificaciones y los procedimientos.</p>
<p>Las razones para realizar una auditoria son:</p>
<ol><li>Establecer el estado del proyecto.</li>
<li>Verificar la capacidad de realizar o continuar un trabajo específico.</li>
<li>Verificar qué elementos aplicables del programa o Plan de Aseguramiento de la Calidad han sido desarrollados y documentados.</li>
<li>Verificar la adherencia de esos elementos con el programa o Plan de Aseguramiento de la Calidad.</li>
</ol><p>El propósito y la actividad de la auditoria es recoger, examinar y analizar la información necesaria para tomar las decisiones de aprobación. La auditoria es realizada de acuerdo con los planes y procedimientos documentados. El plan de auditoria establece un procedimiento para dirigir la auditoria y para las acciones de seguimiento sobre las recomendaciones de la auditoria. Al realizar la auditoria, el personal de la misma evalúa los elementos del software y los procesos para contrastarlos con los objetivos y criterios de las auditorias, tales como contratos, requerimientos, planes, especificaciones o procedimientos, guías y estándares.</p>
<p>Los resultados de la auditoria son documentados y remitidos al director de la organización auditada, a la entidad auditora, y cualquier organización externa identificada en el plan de auditoria. El informe incluye la lista de elementos no conformes u otros aspectos para las posteriores revisiones y acciones. Cuando se realiza el plan de auditoria, las recomendaciones son informadas e incluidas en los resultados de la auditoria.</p>
<p>La auditoria puede traer como consecuencia la Certificación. Dicho Proceso de Certificación comienza con la emisión de una Solicitud de Certificación y culmina con la Concesión del Certificado. Un sistema de certificación de calidad permite una valoración independiente que debe demostrar que la organización es capaz de desarrollar productos y servicios de calidad.</p>
<p>En un software se tienen las siguientes visiones de la calidad:</p>
<ol><li>Necesaria o Requerida: La que quiere el cliente.</li>
<li>Programada o Especificada: La que se ha especificado explícitamente y se intenta conseguir.</li>
<li>Realizada: La que se ha conseguido.</li>
</ol><p>El objetivo es conseguir que las tres visiones coincidan. A la intersección entre la calidad Requerida y la calidad Realizada se le llama Calidad Percibida, y es la única que el cliente valora. Toda aquella calidad que se realiza pero no se necesita es un gasto inútil de tiempo y dinero.</p>
<p>La calidad, como sistema de gestión de una organización, necesita definir estos procesos y medirlos, para poder gestionarlos, es decir, para tener la capacidad de proponer mejoras y reconocerlas.</p>
<p>Para implementar un programa de mejoras es necesario definir procesos, decidir qué se quiere mejorar, definir qué medidas serán necesarias recoger, cómo y dónde tomarlas, gestionarlas mediante herramientas, utilizarlas para la toma de decisiones y reconocer las mejoras. Cuando el proceso a mejorar es el de desarrollo del software, es importante definir qué objetivos se quieren alcanzar, para reducir el número de medidas y, en consecuencia, el coste de recopilarlas y el impacto sobre la actividad de producción de software.</p>
<p>La calidad ha dejado de ser un tópico y es necesario que forme parte de los productos o servicios que comercializamos para nuestros clientes. El cliente es el mejor auditor de la calidad, él exige el nivel que está dispuesto a pagar por ella, pero no más. Por tanto, debemos de cuantificar cuál es el nivel de calidad que nos exige para poder planificar la calidad de los productos que se generen a lo largo de la producción del producto o servicio final. Al analizar las necesidades de nuestros clientes, deberemos tener en cuenta la previsible evolución de sus necesidades y tendencias en cuanto a características. Deberemos tener en cuenta la evolución tecnológica del entorno del producción de nuestros productos para suministrarlos con el nivel tecnológico adecuado. No debemos olvidar el nivel de calidad de nuestros competidores, debiendo elaborar productos cuyas características y funcionalidades sean competitivas con las de nuestros competidores.</p>
<p>La Calidad del Software es resultado del movimiento global dentro del proceso de mejoramiento continuo de los modelos y/o estándares de producción en todos los sectores industriales, en particular, cuando éste se concentra en la producción de sistemas de información y software especializado.</p>
<h4>Calidad de los Datos</h4>
<p>Dado que la calidad tiene componentes objetivos y subjetivos es necesario catalogar los requisitos de calidad de datos de los usuarios según unas determinadas dimensiones de calidad. Se intenta definir el concepto de calidad de datos y catalogar las dimensiones de calidad en función de unos determinados criterios, como pueden ser el ciclo de vida de los datos o los tipos de investigación realizadas o simplemente la forma en la que se usan los datos. Pero todos están de acuerdo en que la calidad de datos es un concepto multidimensional que comprende distintos aspectos según las necesidades de los consumidores de datos o de los diseñadores de sistemas, y que se justifica por el hecho de la concepción de calidad que aporta ISO.</p>
<p>Algunas de las dimensiones de calidad de datos más importantes son:</p>
<p><img src="https://gsitic.files.wordpress.com/2019/05/dimensionescalidad1.png?w=825"/><img src="https://gsitic.files.wordpress.com/2019/05/dimensionescalidad2.png?w=825"/></p>
<p>Metodología para la Medición de la Calidad de los Datos</p>
<p>Existe una metodología para la medición de la calidad de los datos guardados en un almacén de datos. Se parte de la idea de almacenar información referente a la calidad de los datos en el mismo almacén de datos, dicha metodología propone una serie de pasos bien estructurados y definidos que, partiendo de los requisitos de calidad de datos de los usuarios, trata de identificar las dimensiones de calidad de datos de los usuarios, trata de identificar las dimensiones de calidad que mejor describen esos requisitos, para después obtener métricas a partir de ese conjunto de dimensiones; después se realiza el proceso de medición propiamente dicho, que consiste en generar un valor numérico como resultado de un juicio de un determinado valor del dato con respecto a la dimensión elegida; posteriormente los resultados se guardan en el mismo almacén de datos, para después analizar los resultados. La forma de guardar los datos depende fuertemente del modelo de datos elegido para el almacén de datos.</p>
</article>

# Minería de datos. Aplicación a la resolución de problemas de gestión. Tecnología y algoritmos. Procesamiento analítico en línea (OLAP). Big data. Bases de datos NoSQL.

<article><h2>La minería de datos: Data Mining</h2>
<p>El término minería o recopilación de datos (data mining) hace referencia al proceso de análisis semiautomático de BD de gran tamaño para hallar estructuras útiles. Al igual que la búsqueda de conocimiento en la inteligencia artificial o el análisis estadístico, la minería de datos intenta descubrir reglas y estructuras a partir de los datos. Es decir, la minería de datos trata de la búsqueda del conocimiento en las BD.</p>
<p>Los almacenes de datos guardan todos los datos relevantes para una organización, estando estructurados para que se pueda extraer información a partir de dichos datos. En este tema vamos a ver como la minería de datos permite sacar el máximo provecho del almacén de datos, ofreciendo una serie de técnicas y herramientas que automatizan (o semiautomatizan) el proceso de extracción de información y significado a partir de los datos que éste contiene.</p>
<p>El nombre de minería de datos (data mining) deriva de las similitudes entre buscar valiosa información de negocios en grandes BD y minar una montaña para encontrar una veta de metales preciosos. Ambos procesos requieren examinar una inmensa cantidad de material, o investigar inteligentemente hasta encontrar exactamente dónde residen los valores.</p>
<h3>El proceso de descubrimiento de conocimiento en Bases de Datos</h3>
<p>El descubrimiento de conocimiento en las BD es el proceso no trivial de identificación de patrones válidos, potencialmente útiles y comprensibles en los datos. El objetivo es la extracción de conocimiento de los datos, en el contexto de las BD de gran tamaño.</p>
<p>El proceso es iterativo, consta de unos pasos básicos e involucra decisiones por parte del usuario, siendo interactivo. Esto quiere decir que el proceso requiere el entendimiento del dominio de la aplicación por parte del usuario. Se han identificado los siguientes pasos como componentes del proceso:</p>
<ul><li>Selección de un conjunto de datos objetivo.</li>
<li>Preprocesamiento y limpieza de los datos.</li>
<li>Transformación y reducción en la dimensión de los datos.</li>
<li>Selección del método de minería de datos y de la técnica (algoritmo) de minería de datos e implementación de la técnica para realizar la extracción de patrones.</li>
<li>Interpretación o evaluación de los patrones extraídos.</li>
<li>Consolidación del conocimiento descubierto.</li>
</ul><p>Por otro lado, el consorcio Cross-Industry Standard Process for Data Mining propuso un modelo estándar y de acceso público del proceso. El modelo es jerárquico y consta de cuatro niveles de abstracción:</p>
<ul><li>El primer nivel está constituido por una serie de fases las cuales se dividen en tareas generales.</li>
<li>El segundo nivel se conoce como genérico, ya que, trata de cubrir todas las posibles situaciones de minería de datos.</li>
<li>El tercer nivel es más especializado, describiendo particularmente qué acciones deben llevarse a cabo dependiendo de situaciones específicas.</li>
<li>El cuarto nivel es la instanciación del proceso, como un registro de acciones, decisiones y resultados del proceso completo de minería de datos.</li>
</ul><h3>Definiciones de Minería de Datos</h3>
<p>Veamos ahora una serie de definiciones de minería de datos, que ayudan a entender mejor en qué consiste:</p>
<ul><li>La minería de datos pretende obtener visiones en profundidad de los datos corporativos que no son fácilmente detectables. De hecho, más que analizar los resultados de la actividad, permite modelizarla construyendo patrones o categorías que la identifiquen, respondiendo a las necesidades de información del tipo ¿qué hay en los datos de interés?, o ¿qué podría ocurrir en un futuro?, en base al descubrimiento de tendencias o agrupaciones interesantes de datos. De hecho, las herramientas enmarcadas bajo la denominación de Minería de Datos (MD), permiten no sólo el análisis de información que tradicionalmente ha venido siendo realizado por los Sistemas de Soporte a la Decisión (DSS), sino, y esto es lo realmente importante y diferencial, el planteamiento y descubrimiento automáticos de hechos e hipótesis, ya sean patrones, reglas, grupos, funciones, modelos, secuencias, relaciones, correlaciones, etc. Una cualidad que resalta es la posibilidad de anticiparse a las variaciones del entorno, lo que facilitará darles una mejor y más rápida respuesta.</li>
<li>La extracción de información oculta y predecible de grandes BD, es una nueva y poderosa tecnología con gran potencial para ayudar a las compañías a concentrarse en la información más importante de sus Bases de Información (Data Warehouse). Las herramientas de Data Mining predicen futuras tendencias y comportamientos, permitiendo en los negocios tomar decisiones proactivas y conducidas por un conocimiento acabado de la información. Los análisis prospectivos automatizados ofrecidos por un producto así van más allá de los eventos pasados provistos por herramientas retrospectivas típicas de sistemas de soporte de decisión. Las herramientas Data Mining pueden responder a preguntas de negocios que tradicionalmente consumen demasiado tiempo para poder ser resueltas y a los cuales los usuarios de esta información casi no están dispuestos a aceptar. Estas herramientas exploran las BD en busca de patrones ocultos, encontrando información predecible que un experto no puede llegar a encontrar porque se encuentra fuera de sus expectativas.</li>
<li>La minería de datos consiste en la búsqueda de relaciones y patrones globales que se hallan presentes en las grandes BD pero que están “ocultos” entre el gran volumen de datos existente. Estas relaciones representan un conocimiento útil sobre los objetos de la BD y la realidad que representan.</li>
</ul><p>Los puntos en común que observamos en las definiciones anteriores son:</p>
<ul><li>Es necesario disponer de unas BD o, mejor aún, de un almacén de datos, sobre los cuales realizar el proceso de minería.</li>
<li>El proceso de minería debe ser automático en la mayor medida posible, debido a los grandes volúmenes de datos que se analizan.</li>
<li>Los resultados obtenidos deben representar conocimiento útil y no evidente a primera vista.</li>
</ul><p>Después de estudiar el concepto y definiciones de la minería de datos, terminamos este punto poniendo de manifiesto que las aplicaciones de MD extraen conocimiento escondido, patrones de comportamiento no explícitos, relaciones ocultas o información predictiva del almacén, sin necesidad de preguntas o peticiones específicas sino utilizando distintas técnicas, tales como algoritmos matemáticos, métodos estadísticos, modelos lógicos borrosos, algoritmos genéticos, inducciones de reglas, sistemas expertos y sistemas basados en el conocimiento y redes neuronales.</p>
<h3>Fundamentos de la Minería de Datos</h3>
<p>Las técnicas de Minería de Datos son el resultado de un largo proceso de investigación y desarrollo de productos. Esta evolución comenzó cuando los datos de negocios fueron almacenados por primera vez en computadoras, y continuó con mejoras en el acceso a los datos, y más recientemente con tecnologías generadas para permitir a los usuarios navegar a través de los datos en tiempo real.</p>
<p>La Minería de Datos está lista para su aplicación en la comunidad de negocios porque está soportada por tres tecnologías que ya están suficientemente maduras:</p>
<ul><li>Recolección masiva de datos.</li>
<li>Potentes computadoras con multiprocesadores.</li>
<li>Algoritmos de Data Mining.</li>
</ul><p>Los componentes esenciales de la tecnología de Data Mining han estado bajo desarrollo durante décadas, en áreas de investigación como la estadística, la inteligencia artificial y el aprendizaje de máquinas. Hoy, la madurez de estas técnicas, junto con los motores de BD relacionales de alto rendimiento, han hecho que estas tecnologías sean prácticas para los entorno de data warehouse actuales.</p>
<h3>Fases del proceso de Minería de Datos</h3>
<p>Para alcanzar buenos resultados es necesario comprender que la minería de datos no se basa en una metodología estándar y genérica que resuelve todo tipo de problemas, sino que consiste en una metodología dinámica e iterativa que va a depender del problema planteado, de la disponibilidad de la fuente de datos, del conocimiento de las herramientas necesarias, de la metodología desarrollada, y de los requerimientos y recursos de la empresa.</p>
<p>El procedimiento para resolver un problema a través de la minería de datos se divide en dos grandes etapas: la preparación de los datos y la minería de datos propiamente dicha.</p>
<p><strong>Pasos en la fase de preparación de los datos</strong></p>
<ul><li><em>Planteamiento del problema</em>: Definir de manera objetiva cuál es el problema a resolver, determinar con qué recursos humanos y tecnológicos se cuenta, cuáles son las fuentes de información y cuál es la disponibilidad de la información.</li>
<li><em>Selección de los datos</em>: De todas las fuentes de información disponibles se debe establecer cuáles son las que se van a considerar. Es decir, se decide sobre qué datos se va a trabajar, tanto desde el punto de vista físico, como desde el punto de vista lógico. Se debe realizar un tratamiento y estructuración de la información con el objetivo de presentarla de la mejor manera posible para posteriores análisis.</li>
<li><em>Limpieza y preprocesamiento de los datos</em>: En esta fase se analizan los datos con la finalidad de reorganizar la información eliminando aquella que es poco útil o completando la que nos falta. Se eliminan los datos irrelevantes, se unifican los criterios de representación que pueden no ser los mismos en todas las fuentes de datos y se eliminan redundancias y duplicados.</li>
<li><em>Reducción y proyección de datos</em>: Consiste en encontrar las características útiles que representan las dependencias de los datos en el objetivo del proceso.</li>
</ul><p><strong>Pasos en la Minería de Datos</strong></p>
<ul><li><em>Selección de técnicas de minería de datos</em>.</li>
<li><em>Selección de los algoritmos de minería de datos</em>. En él son seleccionados los métodos para que sean usados en la búsqueda de patrones de los datos. Esto incluye decidir qué modelos y parámetros son más apropiados para la adquisición del tipo de conocimiento deseado. A través de la entrega de los datos para los algoritmos de minería de datos seleccionados se llega al conocimiento.</li>
<li><em>Extracción del conocimiento. Búsqueda de patrones</em>: Es esta fase donde se escogen y se aplican las técnicas de minería de datos para la determinación de patrones de interés en los datos. Para ello se interpretan los resultados obtenidos a lo largo del proceso para la construcción de modelos o se buscan estructuras subyacentes dentro de la información. Las herramientas de minería de datos, analizan los datos ya preparados para extraer significado e información.</li>
<li><em>Construcción del modelo. Interpretación y evaluación</em>: Con los resultados obtenidos en la fase anterior se lleva a cabo el análisis, interpretación y evaluación para la determinación de un modelo eficiente que sea útil en la toma de decisiones.</li>
<li><em>Validación del modelo</em>: Implementar el modelo desarrollado en el proceso real y determinar su efectividad en diferentes casos de aplicación. Si las pruebas arrojan resultados satisfactorios, el modelo queda comprobado y garantizado para su uso regular. Sin embargo, si los resultados son poco satisfactorios, se debería regresar a las fases anteriores y fortalecer el análisis para mejorar el modelo final.</li>
</ul><h3>Elementos o Técnicas de la Minería de Datos</h3>
<p>La aplicación ideal de la MD se llevaría a cabo sobre las BD corporativas, que como ya hemos comentado pueden ser un Almacén de Datos, o sobre otras específicas de propósito departamental (o Data Marts), contemplando elementos o técnicas como los siguientes:</p>
<ul><li><em>Agentes inteligentes</em>: Se encargan de analizar la información para detectar patrones y relaciones, ya sea de forma automática, o bien interactuando con el analista. Las técnicas que utilizan les permiten identificar grupos, comportamientos y reglas cuyo descubrimiento habría supuesto un enorme esfuerzo de trabajo metódico. Son tomados del campo de la inteligencia artificial y entre ellos destacan los sistemas expertos, el aprendizaje automático, la visión por ordenador o la teoría de juegos. Utilizan estructuras de datos y algoritmos basados en árboles de decisión, redes neuronales, técnicas de agrupamiento y lógica difusa. Estas técnicas son especialmente adecuadas para herramientas de minería que utilizan los modelos predictivo y de descubrimiento, ya que son muy buenas en la detección de patrones.</li>
<li><em>Detección de alarmas</em>: Consiste en la ejecución periódica o permanente de ciertos agentes para detectar acciones o situaciones susceptibles de desencadenar una acción extraordinaria o fuera del ciclo ordinario, pudiéndose activar en tiempo real, o detectarse y almacenarse para su posterior análisis y tratamiento.</li>
<li><em>Análisis multidimensional</em>: Se basa en la estructuración y presentación de la información bajo aquellas perspectivas, ejes o dimensiones de interés. Las técnicas multidimensionales son muy buenas para cruzar los datos de múltiples formas y con distintos niveles de agregación. Se basan en la utilización de BD multidimensionales. Los estudiaremos con detalle en el apartado dedicado a OLAP.</li>
<li><em>Consultas e informes</em>: Ésta es la forma tradicional de obtener información a partir de BD. Las plataformas suelen incorporar herramientas de consulta (lenguaje SQL) con interfaces gráficas muy avanzados, intuitivos y fáciles de usar, cierto grado de análisis multidimensional y agentes inteligentes. Adicionalmente pueden utilizar técnicas matemáticas y estadísticas para analizar los datos obtenidos. Estas técnicas son muy apropiadas si se va a utilizar el modelo de Verificación. Su principal ventaja es que son de eficiencia probada, trabajan sobre las BD relacionales ya existentes y además es muy sencillo encontrar herramientas amigables al usuario que las soporten.</li>
<li><em>Tratamiento de datos</em>: Los datos suelen estar almacenados en los formatos más adecuados para su gestión por parte de los sistemas existentes, pero pueden no ser los más adecuados para su procesamiento por parte de la MD, de ahí que muchos desarrollos de MD incorporen módulos de tratamiento de datos con el objeto de simplificar al máximo las interfaces de datos e información.</li>
</ul><h2>Aplicación a la Resolución de Problemas de Gestión</h2>
<h3>Planteamiento Inicial del Problema</h3>
<p>El desarrollo tecnológico ha aumentado considerablemente la mejora de los sistemas de almacenamiento de datos de las empresas. El problema es que, a medida que aumenta nuestra capacidad para almacenar y acceder a la información, más problemas tenemos para tratarla. Un ejemplo claro lo podemos ver en la “revolución” que ha supuesto internet y en cómo la información que se genera dentro de cualquier campo de nuestro interés aumenta considerablemente cada año, mientras que a su vez, cada vez nos vemos más incapaces de asimilarla.</p>
<p>En la industria, igualmente, la preocupación de las empresas por producir “mejor y más barato”, la búsqueda constante de reducir “incertidumbre” en el proceso de fabricación y el aumento creciente de la información que se tiene que los procesos productivos, hace que crezca, cada vez más, la necesidad por analizarla. Bien es cierto, que esta necesidad solo aparece cuando la empresa tiene un volumen de históricos del proceso realmente importante.</p>
<h3>El Análisis de la Información</h3>
<p>También la evolución de la tecnología ha facilitado y automatizado en gran medida las tareas de análisis de información. Cada paso en esta evolución se apoya en los anteriores, y cada uno de ellos ha supuesto un avance significativo para el usuario, que ha visto como cada progreso le abría nuevas posibilidades de análisis y aumentaba el nivel de abstracción de las consultas.</p>
<p>Para decidir cuál es la técnica más adecuada para una determinada situación, es necesario distinguir el tipo de información que se desea extraer de los datos. Según su nivel de abstracción, el conocimiento contenido en los datos puede clasificarse en distintas categorías y requerirá una técnica más o menos avanzada para su recuperación. Éstas son las tres categorías de conocimiento con las que nos podemos encontrar.</p>
<p><strong>Conocimiento Evidente</strong></p>
<p>Se trata de la información fácilmente recuperable con una simple consulta (por ejemplo con un lenguaje como el SQL). Un ejemplo de este tipo de conocimiento es una pregunta como “¿Cuáles fueron las ventas en España el pasado marzo?”.</p>
<p><strong>Conocimiento Multidimensional</strong></p>
<p>El siguiente nivel de abstracción consiste en considerar los datos con una cierta estructura. Por ejemplo, en vez de considerar cada transacción individualmente, las ventas de una compañía pueden organizarse en función del tiempo y de la zona geográfica, y analizarse con diferentes niveles de detalle (país, región, localidad, …).</p>
<p>Técnicamente, se trata de reinterpretar una tabla con n atributos independientes como un espacio n-dimensional, lo que permite detectar algunas regularidades difíciles de observar con la representación monodimensional clásica.</p>
<p>Este tipo de información es la que analizan las herramientas OLAP, que estudiaremos más adelante y que resuelven de forma automática cuestiones como “¿Cuáles fueron las ventas en España el pasado marzo? aumentando el nivel de detalle: mostrar las de Madrid”.</p>
<p><strong>Conocimiento Oculto</strong></p>
<p>Se trata de la información no evidente, desconocida a priori y potencialmente útil, que puede recuperarse mediante técnicas de minería de datos, como reconocimiento de regularidades. Esta información es de gran valor, puesto que no se conocía y se trata de un descubrimiento real de nuevo conocimiento, del que antes no se tenía constancia, y que abre una nueva visión del problema. Un ejemplo de este tipo sería “¿Qué tipos de clientes tenemos? ¿Cuál es el perfil típico de cada clase de usuario?”.</p>
<h3>La Minería de Datos resuelve el problema</h3>
<p>Como se ha visto en el punto anterior, las técnicas disponibles para extraer la información contenida en los datos son muy variadas y cada una de ellas es complementaria del resto, no excluyentes entre sí. Cada técnica resuelve problemas de determinadas características y para extraer todo el conocimiento oculto, en general será necesario utilizar una combinación de varias.</p>
<p>La mayor parte de la información de interés contenida en una BD, aproximadamente el 80% corresponde a conocimiento superficial, fácilmente recuperable mediante consultas sencillas con SQL. El 20% restante corresponde a conocimiento oculto que requiere técnicas más avanzadas de análisis para su recuperación. Estas cifras pueden dar la false impresión de que la cantidad de información recuperable mediante técnicas de minería de datos es despreciable. Sin embargo, se trata precisamente de información que puede resultar de vital importancia para la empresa y que no se puede desdeñar.</p>
<p>Básicamente, y como ya hemos comentado, la clave que diferencia la minería de datos respecto de las técnicas clásicas es que el análisis que realiza es exploratorio, no corroborativo. Se trata de descubrir conocimiento nuevo, no de confirmar o desmentir hipótesis. Con cualquiera de las otras técnicas es necesario tener una idea concreta de lo que se está buscando y, por tanto, la información que se obtiene con ellas está condicionada a la idea preconcebida con que se aborde el problema. Con la minería de datos es el sistema y no el usuario el que encuentra la hipótesis, además de comprobar su validez.</p>
<p>Por lo tanto, queda claro que el descubrimiento de esta información “oculta” es posible gracias a la minería de datos, que entre otras sofisticadas técnicas aplica la inteligencia artificial para encontrar patrones y relaciones dentro de los datos permitiendo la creación de modelos, es decir, representaciones abstractas de la realidad.</p>
<p>La obtención de un buen modelo permitirá una buena comprensión del funcionamiento de una empresa, y será una base idónea para la toma de decisiones. Es decir, dado que el objetivo último de la gestión de los datos corporativos es ofrecer información de calidad a la dirección, cuanto más eficiente sea el proceso de minería, mayor será en cantidad y en calidad la información disponible para soportar la toma de decisiones.</p>
<p>Mediante éstas herramientas y técnicas se pueden obtener patrones y estructuras de información muy valiosas para la industria que pueden ayudar, mediante el análisis de los grandes volúmenes de datos de históricos almacenados, a mejorar la calidad y reducir los costes de los procesos productivos así como comprender mejor las causas que generan fallos en los mismos.</p>
<p>Los beneficios de la utilización de las técnicas de minería de datos en diversas organizaciones son enormes, de forma que las empresas más innovadoras, las están incorporando con gran éxito de forma extensiva.</p>
<h3>Aplicaciones de la Minería de Datos</h3>
<p>La información hallada a través de las técnicas de minería de datos tiene numerosas aplicaciones en el mundo empresarial.</p>
<p>Las aplicaciones más usadas son las que necesitan algún tipo de predicción. Por ejemplo, cuando una persona solicita una tarjeta de crédito, la compañía emisora quiere predecir si la persona constituye un buen riesgo de crédito. La predicción tiene que basarse en los atributos conocidos de la persona, como edad, sus ingresos, sus deudas, etc. Las reglas para realizar la predicción se deducen de los mismos atributos de titulares de tarjetas de crédito pasados y actuales, junto con su conducta observada.</p>
<p>Otra clase de aplicaciones busca asociaciones. Por ejemplo, los libros que se suelen comprar juntos. Si un cliente compra un libro, puede que la librería en línea le sugiera otros libros asociados. Puede que otros tipos de asociación lleven al descubrimiento de relaciones causa-efecto. Por ejemplo, el descubrimiento de asociaciones inesperadas entre un medicamento recién introducido y los problemas cardíacos llevó al hallazgo de que el medicamento podía causar problemas cardíacos en algunas personas. El medicamento se retiró del mercado.</p>
<p>Las asociaciones son un ejemplo de patrones descriptivos. Las agrupaciones son otro ejemplo de este tipo de patrones.</p>
<p>Algunos ejemplos de campos de aplicación de la minería de datos en el mundo empresarial son:</p>
<ul><li>Gestión de mercados y de riesgos.</li>
<li>Diseño de estrategias competitivas.</li>
<li>Ingeniería financiera y promoción comercial.</li>
<li>Detección de fraudes.</li>
</ul><p>Al igual que en el mundo empresarial, en el medio científico es muy habitual la recolección de gran cantidad de datos, de los que resulta muy difícil extraer conocimiento. Por ello, la minería de datos se está aplicando en campos como:</p>
<ul><li>Diagnóstico médico.</li>
<li>Clasificación y estudio de señales biomédicas.</li>
<li>Detección de patrones en imágenes astronómicas.</li>
<li>Análisis de biosecuencias en biomedicina.</li>
<li>Técnicas documentales.</li>
</ul><p>Estudiamos ahora con más profundidad algunas de las aplicaciones más concretas de la minería de datos dentro de las organizaciones en campos como: marketing, predicción, reducción de riesgos, detección de fraudes y control de calidad.</p>
<p><strong>Marketing</strong></p>
<p>Éste es uno de los campos donde los éxitos de la minería de datos son más conocidos. Cuanto más precisa sea la información que tengamos sobre los clientes, mayores posibilidades tendremos de aumentar nuestros ingresos y rentabilizar al máximo nuestras acciones. El objetivo fundamental puede resumirse en determinar quién comprará qué, cuándo y dónde. Veamos tres aplicaciones concretas dentro del marketing:</p>
<ul><li>Targeting: Podemos aumentar espectacularmente el porcentaje de respuesta a una campaña de marketing si se dirige a los objetivos adecuados. La minería de datos permite detectar entre los potenciales clientes los que presentan una mayor probabilidad de responder a la campaña y dirigirla a ellos específicamente, con lo cual se consigue reducir drásticamente los costes.</li>
<li>Fidelización de clientes: Conseguir un nuevo cliente o recuperar uno perdido resulta mucho más costoso que mantener uno que ya lo es. De ahí la rentabilidad de las campañas de fidelización de clientes, que detectan aquéllos que parece más probable que se vayan a perder, permitiendo llevar a cabo iniciativas que eviten dicha pérdida.</li>
<li>La minería de datos también permite detectar nuevas oportunidades de mercado, comparando hábitos de consumo de diferentes clientes, por ejemplo, determinando la ubicación más conveniente para un determinado negocio.</li>
</ul><p><strong>Predicción</strong></p>
<p>Conocer a priori cómo evolucionará una variable en el futuro constituye una información muy valiosa y supone una indudable ventaja competitiva. Se trata de una herramienta de evidente interés tanto desde el punto de vista comercial, como en gestión o control de procesos.</p>
<p>A partir de los datos históricos almacenados y utilizando técnicas de minería de datos pueden elaborarse modelos que permitan estimar con precisión la evolución de una variable de futuro. Disponer de esta información con tiempo suficiente permite adecuar la respuesta de forma óptima. Esto puede resulta útil en los campos más diversos:</p>
<ul><li>Detección de oportunidades.</li>
<li>Prevención de problemas.</li>
<li>Gestión óptima del personal.</li>
<li>Optimización de stocks.</li>
</ul><p><strong>Reducción de Riesgos</strong></p>
<p>La minería de datos permite construir sistemas de evaluación automática de riesgos, basados en la experiencia previa. Estos sistemas resultan de gran utilidad cuando la cantidad de casos a evaluar es excesiva para su procesamiento manual. El empleo de técnicas de minería de datos ha aumentado la eficacia y fiabilidad de dichos sistemas, logrando un comportamiento más similar al de los expertos humanos.</p>
<p><strong>Detección de Fraudes</strong></p>
<p>Aplicando técnicas de minería de datos, pueden obtenerse modelos que permitan descubrir posibles fraudes, basándose en la detección de comportamientos anómalos, en comparación con los datos registrados anteriormente.</p>
<p>Podemos encontrar aplicaciones concretas en operadores de telefonía o empresas de gestión de tarjetas de crédito. Estas compañías analizan el uso que los clientes hacen de sus servicios y pueden localizar, de manera muy rápida, un uso fraudulento de los mismos.</p>
<p><strong>Control de Calidad</strong></p>
<p>Existen numerosos ejemplos en los que se han aplicado técnicas de minería de datos para desarrollar sistemas automáticos de control de calidad. Estos sistemas suponen un considerable ahorro en el proceso productivo, puesto que facilitan:</p>
<ul><li>Detección más precisa de productos defectuosos: A menudo el control de calidad se realiza de forma manual y, por tanto, depende de una evaluación subjetiva por parte del personal encargado del mismo. El principal problema de este método es que el criterio de calidad no es estable sino que depende de la persona que realiza el análisis. La minería de datos permite desarrollar sistemas automáticos de control de calidad que discriminan los productos defectuosos con un alto grado de precisión y fiabilidad, según un criterio objetivo.</li>
<li>Localización precoz de defectos: El control de calidad no sólo debe realizarse al final del proceso. Cuanto antes se detecte un fallo, menor será su impacto. A menudo no resulta fácil medir la variable que determina la calidad del producto en tiempo real o en la cadena de producción. En estos casos, es imprescindible utilizar técnicas de minería de datos para descubrir posibles relaciones que permitan detectar los fallos utilizando las variables disponibles durante el proceso.</li>
<li>Identificación de causas de fallos: La minería de datos no sólo resulta útil para discriminar los productos defectuosos. También ayuda a determinar los fallos más frecuentes así como identificar las causas de los mismos. Esto permite adoptar medidas para evitarlos en el futuro.</li>
<li>Análisis no destructivo: A menudo, para obtener la información que se necesita, hay que realizar un análisis destructivo. Un ejemplo típico es la evaluación de la resistencia de un material, medida que se establece forzándolo hasta que se rompe. Utilizando minería de datos es posible estimar con bastante exactitud el valor de este tipo de parámetros en función de otras características que sí pueden medirse sin destruir el producto. Esto permite controlar la calidad de todos los productos fabricados y no sólo de una pequeña muestra, ya que no se destruyen con el examen.</li>
</ul><h2>Tecnología y Algoritmos</h2>
<p>Antes de estudiar las técnicas y algoritmos principales, vamos a ver los modelos que a lo largo del tiempo han ido apareciendo y en los que se apoya la minería de datos.</p>
<h3>Modelos de la Minería de Datos</h3>
<p><strong>Modelo de Verificación</strong></p>
<p>Este es el modelo más parecido al proceso tradicional de extracción de información basado en lenguajes de consulta a BD (por ejemplo SQL). Su principal característica es que no extrae información nueva, sino que, basándose en los datos del almacén, verifica la validez de las afirmaciones que se le presentan.</p>
<p>El proceso comienza por el establecimiento de una hipótesis por parte del usuario. Este, a continuación, solicita a la herramienta que verifique su validez. Una vez recibida la respuesta, el usuario puede refinar o detallar la hipótesis, preparar unas preguntas más específicas y solicitar una nueva verificación. De esta manera se consigue un proceso iterativo dirigido por un operador humano.</p>
<p>La desventaja de este modelo es, que si al usuario no se le ocurre realizar una pregunta clave, o no ve una relación importante entre diferentes elementos de la BD, la herramienta por sí sola carece de iniciativa para investigar por su propia cuenta.</p>
<p><strong>Los nuevos Modelos Automáticos</strong></p>
<p>La minería de datos ha dado lugar a una paulatina sustitución del análisis de datos dirigido a la verificación, por un enfoque de análisis de datos dirigido al descubrimiento del conocimiento. La principal diferencia entre ambos se encuentra en que en el último, se descubre información sin necesidad de formular previamente una hipótesis. La aplicación automatizada de algoritmos de minería de datos permite detectar fácilmente patrones en los datos, razón por la cual esta técnica es mucho más eficiente que el análisis dirigido a la verificación cuando se intenta explorar datos procedentes de repositorios de gran tamaño y complejidad elevada. Dichas técnicas emergentes se encuentran en continua evolución como resultado de la colaboración entre campos de investigación tales como BD, reconocimiento de patrones, inteligencia artificial, sistemas expertos, estadística, visualización, recuperación de información, y computación de altas prestaciones.</p>
<p>Los algoritmos de minería de datos se clasifican en dos grandes categorías de modelos con distintas denominaciones:</p>
<ul><li>Modelos predictivos, también llamados:
<ul><li>Modelos supervisados.</li>
<li>Modelos basados en la memoria.</li>
<li>Minería de datos dirigida.</li>
</ul></li>
<li>Modelos de descubrimiento del conocimiento, también llamados:
<ul><li>Modelos no supervisados.</li>
<li>Modelos descriptivos.</li>
<li>Minería de datos no dirigida.</li>
</ul></li>
</ul><p>Por lo tanto con los nuevos modelos usamos la minería de datos para:</p>
<ul><li><em>Predecir</em>: Utilizar algunas variables o campos en un BD para predecir valores desconocidos o futuros.</li>
<li><em>Describir</em>: Encontrar patrones que describan la información (interpretables por el hombre).</li>
</ul><p><strong>Modelos Predictivos</strong></p>
<p>Los algoritmos supervisados o predictivos predicen el valor de un atributo (etiqueta), de un conjunto de datos, conocidos otros atributos (atributos descriptivos). A partir de datos cuya etiqueta se conoce, se induce una relación entre dicha etiqueta y otra serie de atributos. Esas relaciones sirven para realizar la predicción en datos cuya etiqueta es desconocida. Esta forma de trabajar se conoce como aprendizaje supervisado y se desarrolla en dos fases:</p>
<ul><li>Entrenamiento: Construcción de un modelo usando un subconjunto de datos con etiqueta conocida.</li>
<li>Prueba: Prueba del modelo sobre el resto de los datos.</li>
</ul><p>El usuario indica sobre qué variables se quiere obtener la predicción y el sistema proporciona la respuesta. Esta respuesta la puede proporcionar explicando cómo la consiguió, lo cual a su vez puede ser una información tan valiosa como la respuesta en sí misma, o sin explicarlo.</p>
<p>Cuando una aplicación no es lo suficientemente madura no tiene el potencial necesario para una solución predictiva fiable. En este caso se puede optar por diversos caminos alternativos:</p>
<ul><li>Modelo predictivo restringido: No se obtiene predicción alguna.</li>
<li>Modelo predictivo no restringido: Se obliga a la realización de una predicción de menor fiabilidad.</li>
<li>Modelos de descubrimiento del conocimiento: Que descubren patrones y tendencias en los datos actuales (no utilizan datos históricos).</li>
</ul><p>Ejemplos: ¿Cuál es el riesgo de este cliente?, ¿Se quedará el cliente?</p>
<p>Algunas técnicas asociadas a los modelos predictivos:</p>
<ul><li>Clasificación: Clasificar datos en clases predefinidas.</li>
<li>Estimación: A diferencia de la clasificación (que trata con resultados discretos), la estimación trata con valores numéricos continuos. A partir de un conjunto de valores de entrada, la estimación obtiene un valor para cierta variable continua, como puede ser una renta, la altura, etc.</li>
<li>Predicción de valores: Una predicción no es más que un tipo de clasificación o estimación.</li>
<li>Regresión: función que convierte datos en valores de una función de predicción.</li>
<li>Árboles de decisión: Son estructuras en forma de árbol que representan conjuntos de decisiones. Estas decisiones generan reglas para la clasificación de un conjunto de datos.</li>
<li>Redes neuronales artificiales: Modelos predecibles no lineales que aprenden a través del entrenamiento y semejan la estructura de una red neuronal biológica.</li>
<li>Series temporales.</li>
</ul><p><strong>Modelos de Descubrimiento del Conocimiento</strong></p>
<p>El objetivo de estos modelos es establecer algún tipo de relación entre todas las variables.</p>
<p>En estos modelos se utiliza la herramienta de minería para descubrir nueva información que no estaba anteriormente en el almacén de forma explícita. Según este modelo es la propia herramienta quien se plantea sus propias preguntas, sin necesidad de que el usuario establezca hipótesis o realice preguntas concretas, aunque, éste puede intervenir para guiar los caminos a explorar.</p>
<p>Habitualmente esta búsqueda se dirige hacia la categorización de los registros en grupos para detectar patrones aplicables o extraer relaciones implícitas en los datos. También es común la búsqueda de elementos extraños o fuera de lo normal.</p>
<p>Ejemplo: Un cliente que compra productos dietéticos es tres veces más probable que compre caramelos.</p>
<p>Algunas técnicas asociadas a los modelos de descubrimiento del conocimiento:</p>
<ul><li>Asociación: Permite establecer las posibles relaciones entre acciones o sucesos aparentemente independientes.</li>
<li>Reconocimiento de patrones: Permite la asociación de una señal o información de entrada con aquella o aquellas con las que guarda mayor similitud, y que ya están catalogadas en el sistema.</li>
<li>Segmentación o agrupamiento: Esta herramienta posibilita la identificación de tipologías o grupos en los cuales los elementos guardan similitud entre sí y se diferencian de los de otros grupos.</li>
<li>Clustering: Es la tarea de segmentar un grupo diverso en un número de subgrupos más similar (denominados clusters). Lo que distingue el clustering de la clasificación es que éste no requiere un conjunto predefinido de clases.</li>
<li>Reglas de asociación: Se trata del agrupamiento por afinidad que tiene como objetivo determinar qué cosas van juntas.</li>
<li>Detección de desviaciones.</li>
</ul><h3>Clasificación</h3>
<p>Dentro de los modelos de predicción, una de las técnicas más importantes es la clasificación. En este apartado vamos a describir qué es la clasificación, a estudiar técnicas para la creación de un tipo de clasificadores, denominados clasificadores de árboles de decisión y se analizarán otras técnicas de predicción.</p>
<p>De manera abstracta, el problema de la clasificación es el siguiente: dado que los elementos pertenecen a una de las clases y dados los casos pasados de los elementos junto con las clases a las que pertenecen, el problema es predecir la clase a la que pertenece un elemento nuevo.</p>
<p>La clasificación se puede llevar a cabo hallando reglas que dividan los datos dados en grupos disjuntos. Continuando con el ejemplo de un banco tiene que decidir si debe conceder una tarjeta de crédito a un solicitante. El banco tiene diversa información sobre esa persona, la cual puede utilizar para adoptar una decisión. Para adoptar la decisión el banco asigna un nivel de valor de crédito de: excelente, bueno, mediano o malo a cada integrante de un conjunto de muestras de clientes actuales según su historial de pagos. Luego, el banco intenta hallar reglas que clasifiquen a sus clientes como excelentes, buenos, medianos o malos.</p>
<p>El proceso de creación de clasificadores comienza con un muestra de los datos, denominada <em>conjunto de formación</em>. Para cada tupla del conjunto de formación ya se conoce la clase a la que pertenece. Existen diversas maneras de crear clasificadores. Una de las técnicas más utilizadas para este fin son los clasificadores de árboles de decisión.</p>
<p><strong>Clasificadores de árboles de decisión</strong></p>
<p>Los clasificadores de árboles de decisión son una técnica muy utilizada para la clasificación. Como sugiere su nombre estos clasificadores utilizan un árbol. Cada nodo hoja tiene una clase asociada, y cada nodo interno tiene un predicado o función asociado.</p>
<p>Continuando con el ejemplo, para concretar las reglas que clasifican los clientes en excelentes, buenos, medianos o malos, vamos a considerar dos atributos: titulación e ingresos. En la siguiente figura se muestra un árbol de decisión que establece las reglas concretas de clasificación.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/arboles_decision.png?w=825"/></p>
<p>Para clasificar un nuevo caso se empieza por la raíz y se recorre el árbol hasta alcanzar una hoja. En los nodos internos se evalúa el predicado o función, para hallar a que nodo hijo hay que ir. El proceso continúa hasta llegar a un nodo hoja.</p>
<p><strong>Creación de Clasificadores de árboles de decisión</strong></p>
<p>La pregunta que se plantea es el modo de crear un clasificador de árboles de decisión, dado un conjunto de casos de formación. La manera más frecuente de hacerlos es utilizar un algoritmo <em>impaciente</em>,&nbsp; que trabaja de manera recursiva, comenzando por la raíz y construyendo el árbol hacia abajo. Inicialmente solo hay un nodo, la raíz, y todos los casos de formación están asociados con este nodo.</p>
<p>En cada nodo, si todos o casi todos los ejemplos de formación asociados con el nodo pertenecen a la misma clase, el nodo se convierte en un nodo hoja a esa clase. En caso contrario, hay que seleccionar un <em>atributo de partición</em> o <em>condiciones de partición</em> para crear nodos hijos. En el ejemplo elegido, se escoge el atributo titulación y se crean cuatro hijos, uno por cada valor de la titulación.</p>
<p>Las particiones en menor número de conjuntos son preferibles a las particiones en muchos conjuntos, ya que llevan a árboles de decisión más sencillos y significativos.</p>
<p>Hay que averiguar el modo de hallar la mejor partición para un atributo. El modo de dividir un atributo depende del tipo de atributo. Los atributos pueden tener dos tipos de valores:</p>
<ul><li><em>Valores continuos</em>: Los valores se pueden ordenar de manera significativa para la clasificación, como la edad o los ingresos.</li>
<li><em>Valores categóricos</em>: No tienen ningún orden significativo para la clasificación, como los nombres de los departamentos o de los paises.</li>
</ul><p>Generalmente los atributos que son números se tratan como valores continuos, y los atributos de cadenas de caracteres se tratan como categóricos. En el ejemplo escogido se ha tratado el atributo titulación como categórico y el atributo ingresos como valor continuo.</p>
<p>En primer lugar se considera el modo de hallar las mejores particiones para los atributos continuos. Por sencillez solo se consideran <em>particiones binarias</em> de los atributos con valores continuos, es decir, particiones que den lugar a dos hijos. En caso de las <em>particiones múltiples</em> ya es más complicado y se pueden dar con valores continuos o categóricos.</p>
<p>Para los atributos categóricos se pueden tener particiones múltiples, con un hijo para cada valor del atributo. Esto funciona muy bien para los atributos categóricos con pocos valores diferentes, como la titulación o el sexo.</p>
<p>La idea principal de construcción de árboles de decisión es la evaluación de los diferentes atributos y de las distintas condiciones de partición y la selección del atributo y de la condición de partición que generen el índice máximo de ganancia de información. El mismo procedimiento funciona de manera recursiva en cada uno de los conjuntos resultantes de la partición, lo que hace que se construya de manera recursiva el árbol de decisión.</p>
<p><strong>Otros Tipos de Clasificadores</strong></p>
<p>Hay varios tipos de clasificadores a parte de los clasificadores de árbol. Dos tipos que han resultado bastante útiles son:</p>
<ul><li><em>Clasificadores de redes neuronales</em>: Utilizan los datos de formación para adiestrar redes neuronales artificiales.</li>
<li><em>Clasificadores bayesianos</em>: Hallan la distribución de los valores de los atributos para cada clase de los datos de formación.</li>
</ul><p><strong>Regresión</strong></p>
<p>La regresión trata la predicción de valores, no de clases. Dados los valores de un conjunto de variables, X1, X2, …, Xn se desea predecir el valor de una variable Y. Por ejemplo se puede tratar el nivel educativo con un número y los ingresos con otro número, y con base a estas dos variables, querer predecir la posibilidad de impago, que podría ser un porcentaje de probabilidad de impago o el importe impagado.</p>
<h3>Asociaciones</h3>
<p>Como ya se dijo, las asociaciones permiten establecer las posibles relaciones entre acciones o sucesos aparentemente independientes. Así, se puede reconocer cómo la ocurrencia de un determinado suceso puede inducir la aparición de otro u otros. Este tipo de herramientas son particularmente útiles, por ejemplo, para comprender los hábitos de compra de los clientes y para la concepción de ofertas, de ventas cruzadas y del “merchandising”.</p>
<p>Los comercios en general suelen estar interesados en las asociaciones entre los diferentes artículos que compra la gente. Ejemplos de estas asociaciones son:</p>
<ul><li>Alguien que compra pan es bastante probable que compre también leche.</li>
<li>Una persona que compró un libro X es bastante probable que también compre el libro Y.</li>
</ul><p><strong>Reglas de Asociación</strong></p>
<p>Un ejemplo de regla de asociación es: <em>pan =&gt; leche</em>. En el contexto de las compras de alimentación, la regla dice que los clientes que compran pan también tienden a comprar leche con una probabilidad elevada.</p>
<p>Una regla de asociación debe tener una población asociada: la población consiste en un conjunto de casos. En el ejemplo de la tienda de alimentación, la población puede consistir en todas las compras en la tienda de alimentación, cada compra es un caso.</p>
<p>Las reglas tienen un soporte, así como una confianza asociados. Los dos se definen en el contexto de la población:</p>
<ul><li><em>El soporte</em>: Es una medida de la fracción de la población que satisface tanto el antecedente como el consecuente de la regla. Por ejemplo, supongamos que solo el 0,001% de todas las compras incluyen leche y clavos. El soporte de la regla <em>leche =&gt; clavos</em> es bajo. Las empresas no suelen estar interesadas en reglas que tienen un soporte bajo, ya que afectan a pocos clientes y no merece la pena prestarles atención.</li>
<li><em>La confianza</em>: Es una medida de la frecuencia con que el consecuente es cierto, cuando lo es el antecedente. Por ejemplo la regla <em>pan =&gt; leche</em> tiene una confianza del 80% si el 80% de las compras que incluyen pan incluyen también leche. Hay que tener en cuenta que la confianza de <em>pan =&gt; leche</em> puede ser muy diferente de la confianza <em>leche =&gt; pan</em>, aunque las dos tiene el mismo soporte.</li>
</ul><p><strong>Otros Tipos de Asociación</strong></p>
<p>El uso de meras reglas de asociación tiene varios inconvenientes. Uno de los principales es que muchas asociaciones no son muy interesantes, ya que pueden predecirse. Por ejemplo, si mucha gente compra cereales y mucha gente compra pan, se puede predecir que un número bastante grande de personas comprará las dos cosas, aunque no haya ninguna relación entre las dos compras. Lo que resultaría interesante es una desviación de la ocurrencia conjunta de las dos compras. O dicho en términos estadísticos, lo que se busca son <em>correlaciones</em> entre los artículos.</p>
<p>Otro tipo importante son las asociaciones de secuencias. Las series de datos temporales, como las cotizaciones bursátiles en una serie de días, constituyen un ejemplo de datos de secuencias.</p>
<h2>Bases de Datos Multidimensionales</h2>
<p>La idea básica empleada por las BD multidimensionales (BDM) es muy sencilla: en lugar de utilizar tablas bidimensionales para almacenar los datos, como se hace en una BD relacional (BDR), emplea tablas n-dimensionales (o hipercubos). Es algo parecido a utilizar una hoja de cálculo para el tratamiento de datos, solo que, se podrán utilizar más de dos dimensiones y se dispondrá de otras capacidades adicionales.</p>
<p>Una BDM está diseñada para los sistemas de soporte de decisiones en la cual los datos tienen una estructura matricial (multidimensional) para su almacenamiento. Este tipo de organización admite consultas más complejas.</p>
<h3>Análisis Multidimensional</h3>
<p>El análisis multidimensional consiste en analizar hechos económicos o, de otros tipos, desde la perspectiva de sus dimensiones, abarcando los diferentes niveles de éstas.</p>
<p>Con el análisis multidimensional se da respuesta a las consultas complicadas de los usuarios, que reflejan los diversos componentes que tienen sus organizaciones. Estos componentes puedes ser de dos tipos: cuantitativos y cualitativos.</p>
<p>A estos componentes también se les llama dimensiones, y a los valores de los componentes (o dimensiones) se les llama atributos. Además, el detalle con el que se muestran los atributos puede variar, cada dimensión se puede descomponer en diferentes niveles de detalle, y éstos dependen de las necesidades del usuario.</p>
<p>Las dimensiones definen dominios como geografía, producto, tiempo, cliente, …</p>
<p>Los miembros de una dimensión se agrupan de forma jerárquica (dimensión geográfica: ciudad, provincia, autonomía, país, …).</p>
<p><strong>El Esquema Multidimensional</strong></p>
<p>La realización del análisis multidimensional a partir de trozos de información no sería nada práctica, lo que se pretende es tener disponible toda la información formando un solo conjunto, al que llamaremos esquema multidimensional.</p>
<p>Una de las características principales del esquema multidimensional es la agregabilidad, gracias a la cual se pueden presentar los valores de una determinada dimensión según sus distintos niveles de detalle. Como es lógico para poder realizar agregación es necesario tener datos en el nivel más bajo de cada dimensión, y los niveles superiores se calcularán a partir de éstos.</p>
<p>Para un óptimo análisis este esquema se soporta en las BBDD multidimensionales, éstas almacenan los datos en estructuras llamadas hipercubos (más de tres dimensiones). En la práctica estos hipercubos no son grandes matrices, sino que son matrices más reducidas que aparecen como una sola matriz. Esto reduce el espacio de índice requerido.</p>
<p>El esquema multidimensional puede ser soportado encima de un SGBD relacional (ROLAP: OLAP sobre BD Relacionales). Para ello el esquema multidimensional deberá ser transformado para poder implementarse sobre un SGBD relacional (que solo soporta tablas planas). Una de las formas de hacer esta transformación es utilizar el “esquema en estrella”, que estudiaremos más adelante.</p>
<p><strong>Características del Análisis Multidimensional</strong></p>
<ul><li>Navegabilidad: Cuando se habla de navegar se refiere a que se puede pasar de un punto a otro del esquema multidimensional. Estos movimientos son:
<ul><li>Perforación (drill-down): Consiste en variar el nivel de detalle de los datos, desde los datos más resumidos a los más detallados. Se dice que drill-down es desagregar y Roll-up es agregar.</li>
<li>Segmentación (slice and dice): Consiste en “recortar” un subconjunto de los datos moviéndose por los distintos datos de una misma dimensión o cambiando de dimensión. Es decir, es la capacidad de ver la BD desde diferentes puntos de vistas. El corte suele hacerse a lo largo del eje del tiempo para analizar tendencias. Se dice que <em>slice</em> es proyección y que <em>dice</em> es selección.</li>
</ul></li>
<li>Visualización: La presentación de los resultados se suele hacer en forma de cuadros o tablas de dos dimensiones, con el cálculo de totales parciales y generales. Se suelen fijar un conjunto de valores de dimensiones y mostrar en la tabla de dos dimensiones los valores en función de esas dimensiones.</li>
<li>Representación gráfica: Suele ser un gráfico de dos dimensiones, donde los valores de las dimensiones fijadas aparecen como comentarios y las dimensiones variables son los ejes de coordenadas. Con este tipo de representaciones se suele perder una dimensión.</li>
<li>Representación mediante mapas: Muy utilizada para dimensiones geográficas, donde se realizan perforaciones seleccionando la zona deseada.</li>
<li>Cálculos dinámicos.</li>
</ul><h3>Modelo de Datos Multidimensional (MDM)</h3>
<p>Se define un modelo de datos multidimensional como la disciplina específica para modelizar datos que es una alternativa a la modelización E/R. Es un modelo de datos (estático y dinámico) basado en estructuras multidimensionales.</p>
<p>Un modelo multidimensional contiene la misma información que un modelo E/R pero agrupa la información en un formato simétrico cuyos objetivos serían:</p>
<ul><li>Que el usuario entienda mejor el modelo.</li>
<li>Que el rendimiento y tiempo de respuesta de las consultas sea el óptimo.</li>
<li>Que los cambios en el modelo se hagan con menos impacto y mayor facilidad.</li>
</ul><p>Veamos ahora los elementos que componen la visión estática de un modelo de datos multidimensional:</p>
<ul><li>Esquema de hecho (esquema de cubo): Es el objeto a analizar. Ejemplos: empleados, ventas, stocks, …</li>
<li>Atributos de hecho o de medida: Atributos de tipo cuantitativo cuyos valores (cantidades) se obtienen generalmente por aplicación de una función estadística que resume un conjunto de valores en un único valor. Ejemplos: nº de empleados, cantidad vendida, precio medio, …</li>
<li>Funciones resumen: Funciones de tipo estadístico que se aplican a los atributos de hecho. Ejemplos: frecuencia, suma, media, máximo, etc.</li>
<li>Dimensiones: Cada uno de los ejes en un espacio multidimensional. Ejemplos: tiempo, espacio, productos, intervalos del nº de empleados, departamentos, etc.</li>
<li>Atributos de dimensión o de clasificación: Atributos de tipo cualitativo (sus valores son modalidades) que suministran el contexto en el que se obtienen las medidas en un esquema de hecho. Ejemplos: días, semanas, ciudades, provincias, etc.</li>
<li>Jerarquías: Varios atributos de dimensión unidos mediante una relación de tipo jerárquico. Ejemplos: día -&gt; semana -&gt; mes -&gt; año.</li>
<li>Series temporales: Una de las dimensiones más habituales de cualquier BDM es el tiempo. Para guardar datos en función del tiempo, se utilizan las series temporales, que son tratadas como una dimensión más.</li>
</ul><p>Vamos a estudiar ahora con más detalle dos de los elementos fundamentales en las BDM: las dimensiones y las jerarquías. Utilizaremos para ello una serie de ejemplos que nos van a ayudar a entender mejor estos dos elementos.</p>
<h3>Dimensiones</h3>
<p><strong>Ejemplo 1</strong></p>
<p>Supongamos que queremos implementar una sencilla BD para almacenar la cantidad de dinero que se gasta en el pago de las pensiones atendiendo al tipo de pensión y a la comunidad autónoma en que se paga.</p>
<p>En el caso de que hubiera dos tipos de pensiones, se podría establecer una BDM con una estructura similar a la de una hoja de cálculo, empleando tantas filas como tipos de pensiones y tantas columnas como comunidades. El gasto correspondiente a cada comunidad y pensión se almacenaría en la celdilla correspondiente, tal como se muestra a continuación:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/bdm1.png?w=825"/></p>
<p>El equivalente relacional sería una tabla de 34 filas y 3 columnas: tipo de pensión, comunidad autónoma y gasto.</p>
<p>En este ejemplo sencillo, el espacio de almacenamiento utilizado en ambos casos es el mismo, pero, ¿qué ocurre con los tiempos de acceso a la información?</p>
<p>Si se quiere acceder al gasto en un tipo de pensión y una comunidad determinados (una sola fila), el tiempo de acceso será similar, siempre que la tabla relacional esté ordenada o tenga definido un índice por tipo de pensión y comunidad autónoma.</p>
<p>Si se quiere obtener el gasto en pensiones de tipo 1 (P1) para todas las comunidades, entonces el tiempo de respuesta de la BDM es mejor, ya que solo tiene que sumar una fila de la matriz (17 sumas). En cambio en la BDR se debe recorrer todos los registros de la tabla para localizar aquellos que cumplan la condición definida (34 registros) o crear más índices.</p>
<p><strong>Ejemplo 2</strong></p>
<p>Supongamos ahora, que también es necesario almacenar la forma de pago de las pensiones y que dicha forma de pago puede ser en efectivo, por talón o transferencia. La BDM tendría el aspecto siguiente:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/bdm2.png?w=825"/></p>
<p>En esta estructura se emplea cada una de las tres dimensiones del cubo para representar cada uno de los campos que se utilizarían en el modelo relacional. Las celdas resultantes se emplean para almacenar el gasto para cada tripleta (CA, TP, FP).</p>
<p>El equivalente relacional sería una tabla con 102 filas y 4 columnas: tipo de pensión, comunidad autónoma, forma de pago y gasto.</p>
<p>De nuevo, las consultas de agregados (totales) serían más costosas en la BDR que en la BDM.</p>
<h3>Jerarquías</h3>
<p>Otro aspecto fundamental de las BDM es la posibilidad de jerarquizar las dimensiones. Vamos a ver esto con otro ejemplo.</p>
<p><strong>Ejemplo 3</strong></p>
<p>Supongamos que, además de conocer el gasto por comunidades, se quiere saber también el gasto por localidades dentro de cada comunidad.</p>
<p>La manera inmediata de representar esto consiste en añadir una nueva dimensión para crear un hipercubo de cuatro dimensiones. Sin embargo esta solución no es eficiente, ya que para cada fila de cada localidad, solo una de las celdillas contendrá el valor. Dicha celdilla será la correspondiente a la comunidad a la que pertenece la localidad.</p>
<p>Con esta estructura se gasta mucho espacio de almacenamiento en celdillas que jamás van a contener datos, por lo tanto hay que buscar otro mecanismo que lo evite. La solución a este problema es crear una jerarquía de niveles en cada dimensión para representar los diversos grados de detalle.</p>
<p>Si se dispone de este mecanismo, la solución al caso de las localidades sería tan simple como jerarquizar la dimensión de las comunidades autónomas, estableciendo las localidades como escalón inferior en la jerarquía.</p>
<p>Para ofrecer esta alternativa el gestor debe ser capaz, de operar con las celdillas, de reconocer si el valor almacenado corresponde a una comunidad o a una localidad, de forma que al hallar totales o realizar cualquier otro tipo de operación no mezcle valores correspondientes a diferentes niveles jerárquicos.</p>
<p>Por lo tanto, una celda es una posición formada por la intersección de cada uno de los elementos de las dimensiones que forman el cubo. La celda puede contener cero, uno o varios datos (cantidades).</p>
<p>Este concepto de jerarquía es extensible a más de dos niveles, por lo que se puede afinar el grado de detalle obtenido al realizar las consultas.</p>
<h3>BD Multidimensionales vs BD Relacionales</h3>
<p>Terminamos este apartado de BDM realizando una comparación entre estas BD y las BDR que son más conocidas.</p>
<p>La utilización de BDM ofrece ventajas sobre las BDR siempre que se vaya a trabajar sobre datos agregados, totales, subtotales, etc. También son superiores a la hora de trabajar con series temporales, obtener vistas de unos datos en función de otros (vistas bidimensionales del hipercubo que forma la BDM) y manejar diversos grados de detalle. En resumen son unas BD adecuadas para el estudio de alto nivel de los datos, al ofrecer una mayor flexibilidad y rapidez de acceso para el análisis de los mismos.</p>
<p>Por otra parte, si lo que se quiere es acceder a un dato individual básico, la ventaja de las BDM desaparece a favor de las BDR. Estas son capaces de recuperar un dato individual con la misma eficiencia que las multidimensionales, suelen ser capaces de almacenar mayor cantidad de información y además, dada su utilización masiva en sistemas OLTP, están optimizadas para la inserción de registros y el control concurrente de usuarios.</p>
<p>La utilización de ambos tipos de BD no es excluyente. De hecho es frecuente utilizar una BDR para almacenar los datos de nivel más bajo de la jerarquía de una BDM, de forma que si se desea obtener un dato básico, se excava a través de la jerarquía multidimensional hasta acceder a la BDR.</p>
<h2>Procesamiento Analítico en Línea (OLAP)</h2>
<p>Dado que el volumen de datos almacenados en las BD suele ser elevado, hay que resumirlos de algún modo si se quiere obtener información que puedan utilizar los usuarios. Las herramientas OLAP soportan el análisis interactivo de la información de resumen.</p>
<h3>Definición de OLAP</h3>
<p>El acrónimo OLAP significa Procesamiento Analítico en Línea (On-Line Analytical Processing), y se utiliza para hacer referencia a sistemas y herramientas de minería de datos que usan técnicas multidimensionales para la extracción y el análisis de los datos.</p>
<p>Según E.F. Codd, que fue quién acuñó el término, OLAP es: la síntesis, el análisis y la consolidación dinámica de grandes volúmenes de datos multidimensionales.</p>
<p>Según otra definición de OLAP: se trata de un término inventado para describir una aproximación dimensional interactiva al soporte de toma de decisiones (análisis desde la perspectiva de sus componentes o dimensiones, contemplando también los distintos niveles o jerarquías que éstas poseen).</p>
<p>Siempre que se habla de tecnología OLAP el adjetivo más utilizado es “multidimensional”, ya sea para referirse a los datos, a su estructura, a la BD que se emplea o a casi cualquier otro aspecto del OLAP. Esta caracterización llega hasta el punto de identificar el OLAP y las BD multidimensionales como una misma cosa. Aunque indudablemente ambas tecnologías están relacionadas, la utilización de OLAP no implica necesariamente la utilización de BD multidimensionales.</p>
<p>La pregunta que debemos respondes es, ¿qué requiere el usuario de OLAP? La respuesta es:</p>
<ul><li>Conceptos familiares para el usuario final: Dimensiones, medidas y jerarquías.</li>
<li>Acceso inmediato a los datos.</li>
<li>Información consistente.</li>
<li>Navegación y consulta sencillas.</li>
<li>Capacidades de generación de informes.</li>
<li>Datos precalculados.</li>
<li>Soporte de grandes volúmenes de datos.</li>
<li>Flexibilidad de manejo y presentación.</li>
<li>Potentes capacidades de análisis: Agregaciones, comparaciones, ratios, correlaciones, análisis de situaciones, contraste de hipótesis, descubrimiento de patrones y tendencias, previsiones, series temporales, etc.</li>
</ul><h3>Características de los Sistemas OLAP</h3>
<p>Las características básicas de los sistemas OLAP son las siguientes:</p>
<ul><li>Ofrecen una visión multidimensional y jerarquizada de los datos.</li>
<li>Son capaces de analizar tendencias a lo largo del tiempo.</li>
<li>Pueden presentar vistas de un número reducido de dimensiones elegido por el usuario.</li>
<li>Permiten ahondar en la jerarquía de los datos para acceder a los de más bajo nivel.</li>
<li>Son interactivos y soportan múltiples usuarios concurrentes.</li>
</ul><p>Resulta ahora claro, vistas sus características, como los sistemas OLAP pueden beneficiarse de las funcionalidades de una BDM:</p>
<ul><li>La visión multidimensional y la jerarquizada van explícitas en la propia estructura de la BD. La herramienta OLAP, que posiblemente esté integrada en la BDM, solo tiene que ocuparse del manejo del cubo hiperdimensional para extraer los datos conforme a los criterios establecidos por el usuario.</li>
<li>El estudio de tendencias se puede realizar aprovechando las series temporales de la BDM o, si no se dispone de dicho tipo de datos, realizando las operaciones y conversiones necesarias para manejar el tiempo como una dimensión adicional de la BD.</li>
<li>La presentación de vistas se conoce en la jerga OLAP como “slice and dice” (cortar y trocear) y se podría traducir en algo así como segmentación. Esta característica de una herramienta OLAP consiste en la capacidad de extraer “rodajas” del hipercubo que forma la BDM. Estas rodajas se extraen dado un valor fijo para una o varias dimensiones y tomando el hipercubo resultante.</li>
<li>La capacidad de perforar en los niveles de jerarquía se realiza, de nuevo, aprovechando la propia estructura de la BDM subyacente. En el caso de que se utilice una BDR como escalón inferior de la jerarquía, la herramienta OLAP debe ocuparse de que el acceso a dicho nivel sea transparente para el usuario.</li>
<li>La interactividad y el soporte de múltiples usuarios simultáneos son capacidades que dependen en gran medida de los tiempos de respuesta del gestor de BD empleado, por lo que se puede utilizar como criterio orientativo a la hora de elegir el producto que se va a adquirir para construir el sistema.</li>
</ul><h3>Implementación de Sistemas OLAP</h3>
<p>Como ya hemos comentado, debido a su orientación hacia el manejo de los datos organizados en dimensiones, el entorno natural de trabajo de los sistemas OLAP son las bases de datos multimensionales. No obstante también pueden trabajar sobre BD Relacionales, aunque en este caso sus prestaciones se ven disminuidas. Atendiendo a este criterio, los sistemas OLAP se pueden dividir en tres tipos principales, que estudiamos a continuación.</p>
<p><strong>MOLAP (Multidimensional-OLAP)</strong></p>
<p>Los primeros sistemas OLAP utilizaban arrays de memoria multidimensionales para almacenar los cubos de datos y se denominan OLAP multidimensional (MOLAP).</p>
<p>Por lo tanto, funcionan sobre BD multidimensionales. Requieren un esfuerzo previo de modelización y construcción de la BD multidimensional y de otro continuo consistente en migrar los datos en formato relacional al nuevo formato multidimensional. A cambio ofrecen un rendimiento muy superior a la hora de realizar la extracción y el análisis de los datos, puesto que los datos a los que acceden están organizados en dimensiones y jerarquías.</p>
<p>Los datos se almacenan en un sistema de matrices (hipercubo) en donde cada eje es una dimensión.</p>
<p><strong>ROLAP (Relational-OLAP)</strong></p>
<p>Posteriormente, los servicios OLAP se integraron en los sistemas relacionales y los datos se almacenaron en las BD relacionales. Estos sistemas se denominan sistemas OLAP relacionales (ROLAP).</p>
<p>Estos sistemas permiten trabajar sobre las BD corporativas ya establecidas, ahorrando así el trabajo de crear y mantener nuevas BD multidimensionales. A cambio deben ocuparse de realizar la conversión entre la visión relacional de los datos mantenida por el SGDBR y el manejo multidimensional y jerárquico que debe ofrecer al usuario, lo cual acarrea un coste en tiempo y recursos de máquina.</p>
<p>El almacenamiento se suele realizar en un esquema en estrella (no normalizado) o copo de nieve (normalizado), que vamos a estudiar posteriormente con detalle.</p>
<p>Las tendencias actuales en estos sistemas ROLAP son:</p>
<ul><li>Desarrollo de técnicas específicas para el almacenamiento (índices join, bitmap, …) y optimización de consultas.</li>
<li>Crear servidores SQL ampliado especializados en funcionar como Almacén de Datos.</li>
</ul><p>A su vez, estas tendencias dan lugar a dos tipos de modelos ROLAP:</p>
<ul><li>SGBD especializados de SQL: Proporcionan un lenguaje de consulta avanzado y soporte para el proceso de consultas SQL sobre esquemas en estrella y copo de nieve en entornos de solo lectura.</li>
<li>Servidores ROLAP: Servidores intermedios que se sitúan entre el SGBDR y las herramientas cliente. Este middleware está especializado en el soporte de consultas OLAP multidimensionales que se optimizan para servidores relacionales específicos.</li>
</ul><p>Respecto a la elección entre MOLAP y ROLAP, en la práctica resulta mucho más habitual encontrar sistemas de almacén de datos, junto con sus correspondientes herramientas OLAP y de minería de datos, implementadas mediante BD relacionales. Esto es debido a la mayor experiencia de que se dispone para trabajar sobre BD Relacionales, a la gran cantidad de productos ya disponibles en el mercado y a la confianza que las organizaciones tienen en este tipo de BD.</p>
<p><strong>HOLAP (Hybrid-OLAP)</strong></p>
<p>Además de los dos sistemas descritos, aparecen los sistemas híbridos, que almacenan algunos resúmenes en la memoria y los datos básicos y otros resúmenes en las BD Relacionales, se denominan sistemas OLAP híbridos (HOLAP).</p>
<p>Dicho de otra forma, los sistemas HOLAP proporcionan análisis multidimensional accediendo indistintamente a BD Multidimensionales o Relacionales.</p>
<p>Muchos sistemas OLAP se implementan como sistemas cliente-servidor. El servidor contiene la BD Relacional y los cubos de datos MOLAP. Los sistemas clientes obtienen vistas de los datos comunicándose con el servidor.</p>
<h3>ROLAP: Tipos de Diseño</h3>
<p>Nos detenemos ahora en los sistemas ROLAP, que a pesar de no ser los que mejor se adaptan a una herramienta OLAP, si son muy utilizados. Veamos los diferentes tipos de diseño que se deben realizar para que estos sistemas puedan dar una respuesta eficiente.</p>
<p><strong>Esquema en Estrella</strong></p>
<p>Esquema relacional adaptado a la representación de datos multidimensionales. Se basa en una serie de tablas que representan dimensiones unidas mediante claves ajenas, a una principal que actúa como nexo llamada tabla de hechos y que almacena datos agregados y precalculados (tablas no normalizadas).</p>
<p><strong>Tabla de Hechos</strong></p>
<p>El contenido de una tabla de hechos está formado por:</p>
<ul><li>Clave principal: Concatenación de las claves de todas las tablas de dimensión asociadas a la tabla de hechos.</li>
<li>Claves ajenas: Que referencian a las claves de las correspondientes dimensiones.</li>
<li>Atributos de Hecho: atributos de tipo cuantitativo cuyos valores (cantidades) se obtienen generalmente por aplicación de una función estadística que resume un conjunto de valores en un único valor. Ejemplos: nº de empleados, cantidad vendida, precio medio, et.</li>
</ul><p>Por otro lado, las características principales de una tabla de hechos son:</p>
<ul><li>Filas con pocas columnas (pocos atributos).</li>
<li>Nº de filas: Desde millones a más de miles de millones (tantas como celdas tenga el cubo).</li>
<li>Acceso, en general, vía dimensiones.</li>
</ul><p><strong>Tablas de Dimensión</strong></p>
<p>Las características de las tablas de dimensión son:</p>
<ul><li>Definen las dimensiones de negocio en términos familiares para los usuarios.</li>
<li>Filas con numerosas columnas de texto, altamente descriptivas.</li>
<li>Normalmente menos de un millón de filas.</li>
<li>Combinadas con las tablas de hecho mediante claves ajenas.</li>
<li>Altamente indexadas.</li>
<li>No están relacionadas entre sí.</li>
<li>Se utilizan como puntos de acceso a los datos detallados de la tabla de hechos.</li>
<li>A veces se tienen que desnormalizar.</li>
</ul><p><strong>Figura de Tabla de Hechos con Tabla de Dimensiones</strong></p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/tabla_dimension_hechos.png?w=825"/></p>
<p>Al igual que sucede al manejar un hipercubo multidimensional, las consultas típicas en un esquema en estrella consisten en fijar un valor o rango de ellos para las dimensiones y, a continuación, obtener la información solicitada. La respuesta se encuentra realizando operaciones de unión natural (join) entre tablas de dimensiones y la tabla de hechos. Para optimizar las consultas, el gestor de BD debe ser capaz de reconocer que está trabajando con un esquema en estrella y hacer en primer lugar los join entre las tablas de dimensiones y, con el resultado, hacer un único join con la tabla de hechos, minimizando el número de accesos físicos.</p>
<p><strong>Esquema en Copo de Nieve</strong></p>
<p>El esquema en copo de nieve es una variante del esquema en estrella que presenta las tablas de dimensión estructuradas a más de un nivel (tablas normalizadas). Se utiliza cuando hay jerarquías en las dimensiones, lo que supone más claves ajenas. Ejemplo:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/copo_nieve.png?w=825"/></p>
<p><strong>Constelación de Estrellas</strong></p>
<p>La constelación de estrellas la forman varios esquemas en estrella y/o en copo de nieve que comparten dimensiones. Ejemplo:</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/constelacion_estrellas.png?w=825"/></p>
<p><strong>Índices Bitmap</strong></p>
<p>Para poder conseguir una cierta eficiencia en los accesos, hay que considerar una serie de aspectos en el diseño físico, tales como:</p>
<ul><li>Estructuras de índices (mapas de bits, índices de combinación, índices textuales).</li>
<li>Vistas materializadas:
<ul><li>Identificación de las vistas a materializar.</li>
<li>Explotación de la vista materializada durante la consulta.</li>
<li>Actualización de las vistas materializadas durante la carga y refresco.</li>
</ul></li>
</ul><p>En este apartado vamos a estudiar cómo es la estructura de los índices bitmap.</p>
<p>Los índices bitmap son un tipo especial de índice que almacena la información en bits en vez de múltiplos de bit (byte, doble byte) y que sirve para acelerar el acceso a filas con atributos de baja cardinalidad.</p>
<p>Se dice que un atributo es de baja cardinalidad si su dominio está formado por pocos elementos. Ejemplo: el atributo sexo (H o M).</p>
<p>Se trata de guardar un mapa de bits para cada posible valor del atributo, por lo que, como se dijo anteriormente, no es eficiente usar estos índices para valorares de alta cardinalidad. Ejemplo: el índice para sexo tendrá dos bitmaps.</p>
<p>Para responder a consultas que se realicen sobre esquemas relacionales con índices bitmap, basta con hacer las operaciones lógicas apropiadas (AND, OR, NOT) sobre los bits de cada índice implicado en la consulta, lo cual es una operación muy rápida, mucho más que la comparación de cadenas o números que implica la utilización de índices de otro tipo.</p>
<p>Este tipo de índices son útiles para indexar las tablas de dimensiones en esquemas en estrella o en copo de nieve, ya que muchas de estas dimensiones suelen tener su clave principal formada por un atributo de baja cardinalidad. Ejemplo: código de provincia, sexo, estado civil, etc.</p>
<h3>Elección de una Herramienta OLAP</h3>
<p>A la hora de elegir una herramienta OLAP hay que tener en cuenta, entre otros, los puntos siguientes:</p>
<ul><li>Si obliga a trabajar con una BD multidimensional (MOLAP), relacional (ROLAP) o si soporta ambas.</li>
<li>En el caso de herramientas MOLAP es conveniente estudiar las capacidades de la BDM subyacente. Además hay que fijarse en su capacidad de aceptar accesos concurrentes y la carga de usuarios que admite, ya que el objetivo del OLAP es permitir el análisis interactivo.</li>
<li>En el caso de herramientas ROLAP, la penalización en que se incurre al no utilizar BD multidimensional, y las facilidades que ofrece la herramienta para ofrecer una vista multidimensional de los datos (optimización de accesos a esquemas en estrella, en copo de nieve e índices bitmap).</li>
<li>El límite en cuanto al número de dimensiones y de celdillas que puede manejar, sea o no multidimensional la BD subyacente. También la profundidad de los niveles de jerarquías y el manejo de series temporales.</li>
<li>La capacidad de cálculo y la facilidad para especificar qué métodos y operaciones hay que aplicar a los datos. También debe disponer de herramientas y presentación de informes.</li>
<li>El mantenimiento de las dimensiones y las jerarquías mediante herramientas automatizadas. Facilidad a la hora de modificar cualquiera de ambos elementos.</li>
</ul><h3>Comparativa de OLAP y Otros Sistemas</h3>
<p>Terminamos el estudio de los sistemas OLAP haciendo una comparativa de los mismos frente a otros. Por un lado sistemas muy relacionados, como son los Sistemas de Soporte a las Decisiones y la propia Minería de Datos, y por otros, sistemas antagónicos como los sistemas OLTP.</p>
<p><strong>Minería de Datos frente a OLAP y DSS</strong></p>
<p>Los sistemas de ayuda a la decisión (DSS) son herramientas sobre las que se apoyan los responsables de una empresa, directivos y gestores, en la toma de decisiones. Para ello, utilizan:</p>
<ul><li>Un Data Warehouse, en el que se almacena la información de interés para la empresa.</li>
<li>Herramientas de análisis multidimensional (OLAP).</li>
</ul><p>Los DSS permiten al responsable de la toma de decisiones consultar y utilizar de manera rápida y económica las enormes cantidades de datos operacionales y de mercado que se generan en una empresa. Gracias al análisis OLAP, pueden verificarse hipótesis y resolverse consultas complejas. Además, en el curso del análisis, la interpretación de los datos puede dar lugar a nuevas ideas y enfoques del problema, sugiriendo nuevas posibilidades de análisis.</p>
<p>Sin embargo, el análisis OLAP depende de un usuario que plantee una consulta o hipótesis. Es el usuario el que lo dirige y, por tanto, el análisis queda limitado por las ideas preconcebidas que aquél pueda tener.</p>
<p>La minería de datos constituye un paso más en el análisis de los datos de la empresa para apoyar la toma de decisiones. No se trata de un técnica que sustituya los DSS ni el análisis OLAP, sino que los complementa, permitiendo realizar un análisis más avanzado de los datos y extraer más información de ellos.</p>
<p>Como ya se ha comentado anteriormente, utilizando minería de datos es el propio sistema el que descubre nuevas hipótesis y relaciones. De este modo, el conocimiento obtenido con estas técnicas no queda limitado por la visión que el usuario tiene del problema.</p>
<p>Las diferencias entre minería de datos y OLAP radican esencialmente en que el enfoque desde el que se aborda el análisis con cada una de ellas es completamente distinto. Fundamentalmente:</p>
<ul><li>El análisis que realizan las herramientas OLAP es dirigido por el usuario, deductivo, parte de una hipótesis o de una pregunta del usuario y se analizan los datos para resolver esa consulta concreta. Por el contrario, la minería de datos permite razonar de forma inductiva a partir de los datos para llegar a una hipótesis general.</li>
<li>Además, las aplicaciones OLAP trabajan generalmente con datos agregados, para obtener una visión global del negocio. Por el contrario, la minería de datos trabaja con datos individuales, concretos, descubriendo las regularidades y patrones que presentan entre sí y generalizando a partir de ellos.</li>
</ul><p>Un ejemplo clarificará la diferencia entre ambas técnicas es el siguiente:</p>
<p>Una pregunta típica de un sistema OLAP/DSS sería: “El año pasado, ¿se compraron más furgonetas en Cataluña o en Madrid?”. La respuesta de sistema sería del tipo “En Cataluña se compraron 12.000 furgonetas, mientras que, durante el mismo intervalo, en Madrid se compraron 10.000”. Obviamente es una información interesante y útil, pero restringida por la hipótesis realizada a priori.</p>
<p>En cambio, un problema típico para resolver utilizando minería de datos sería, por ejemplo: “Hallar un modelo que determine las características más relevantes de las personas que compran furgonetas”. A partir de los datos del pasado, el sistema de minería de datos proporcionaría una respuesta del tipo: “Depende de la época del año y la situación geográfica. En invierno, los habitantes de Madrid que pertenecen a un cierto grupo de edad y nivel de ingresos probablemente comprarán más furgonetas que gente de las mismas características en Cataluña”.</p>
<p>Como puede verse, se trata de problemas distintos, de modo que según los objetivos perseguidos deberá utilizarse una técnica u otra. Además, puesto que sus conclusiones son complementarias, en general será conveniente combinar ambas para obtener los mejores resultados.</p>
<p><strong>Sistemas OLTP vs Sistemas OLAP</strong></p>
<p>Como ya sabemos OLAP (On-Line Analytical Processing) se define como análisis rápido de información multidimensional compartida. El término OLAP aparece en contraposición al concepto tradicional OLTP (On-Line Transactional Processing), de designa el procesamiento operacional de los datos, orientado a conseguir la máxima eficacia y rapidez en las transacciones (actualizaciones) individuales de los datos, y no su análisis de forma agregada.</p>
<p>Existen, por lo tanto, dos grupos de aplicaciones que se realizan en una empresa:</p>
<ul><li>Aplicaciones que ejecutan operaciones del día a día (compra, inventario, nóminas, …). Son los Sistemas de Procesamiento de transacciones en línea (OLTP).</li>
<li>Aplicaciones que se encargan de analizar el negocio, interpretar lo que ha ocurrido y tomar decisiones (para mejorar los servicios al cliente, incrementar ventas,…). Son los Sistemas de Procesamiento analítico en línea (OLAP).</li>
</ul><p>Los dos son sistemas de procesamiento muy diferentes. Veamos las diferencias principales entre los dos sistemas:</p>
<ul><li>OLAP permite que una compañía decida qué debe hacer y OLTP ayuda a llevar a cabo la decisión.</li>
<li>OLTP representa una “imagen” de los asuntos de la organización que se actualiza constantemente (con cada operación realizada). Los sistemas OLAP son estáticos, refrescándose periódicamente (cada semana, cada mes, …) a partir de las fuentes OLTP.</li>
<li>El diseño de los sistemas OLTP elimina redundancias, y se piensa más en la eficiencia (transacciones rápidas) que en el usuario (dificultad para navegar). Los sistemas OLAP almacenan datos redundantes para conseguir un acceso sencillo al usuario y buenos tiempos de respuesta.</li>
<li>OLTP proporciona capacidades muy limitadas para la toma de decisiones (los usuarios examinan la BD registro a registro). OLAP trabaja con un resumen de miles de registros “condensados” en una respuesta.</li>
<li>Los sistemas transaccionales (u operacionales) automatizan el día a día del negocio, buscando la eficiencia. Los sistemas analíticos se centran en la estrategia a largo plazo y están dirigidos por el negocio.</li>
<li>En cuanto a la implementación de OLTP y OLAP:
<ul><li>Surgen los sistemas EIS y DSS (basados en OLAP) para soportar la toma de decisiones. Presentan problemas para recuperar datos de la BD Operacionales.</li>
<li>No se puede implementar OLTP y OLAP en una sola BD. Actuando el SGBD como interfaz entre datos y usuarios.</li>
<li>Se necesita una arquitectura dual de BD.</li>
</ul></li>
</ul><p>En el siguiente cuadro, se observa de forma resumida, las características de los sistemas OLTP y OLAP, quedando así más claras sus diferencias.</p>
<p><img src="https://gsitic.files.wordpress.com/2018/01/oltp_vs_olap.png?w=825"/></p>
<h2>Big Data</h2>
<p>Con la irrupción de internet, llegaron nuevos conceptos que con el tiempo se han vuelto de uso cotidiano y que nos acompañan en nuestro día a día. Han repercutido para bien en nuestras vidas y casi no podemos entender las nuevas tecnologías sin estas geniales ideas. Uno de estos conceptos que han resonado mucho últimamente es <strong>Big Data</strong>; aunque como ya ha pasado en anteriores ocasiones, el halo de escepticismo y desconfianza ha planeado en torno a todo lo que lo rodea. Hay muchas dudas (fundadas) en cuanto a su concepto, uso y alcance; de esta manera se crea un ambiente de recelo aparejado a algo que parece intangible, incontrolable y sobre todo, que puede atentar nuestra privacidad.</p>
<h3>Qué significa Big Data</h3>
<p><strong>Big Data</strong> (<em>datos masivos</em> en español, aunque apenas se utiliza la traducción) es el proceso de recolección de grades cantidades de datos y su inmediato análisis para encontrar información oculta, patrones recurrentes, nuevas correlaciones, etc; el conjunto de datos es tan grande y complejo que los medios tradicionales de procesamiento son ineficaces. Y es que estamos hablando de desafíos como analizar, capturar, recolectar, buscar, compartir, almacenar, transferir, visualizar, etc, ingentes cantidades de información, obtener conocimiento en tiempo real y poner todos los sentidos en la protección de datos personales. El tamaño para albergar todo el proceso ha ido aumentando constantemente para poder recopilar e integrar toda la información.</p>
<p>La recolección de datos ha existido casi desde siempre, cuando en el amanecer el hombre hacía muescas en piedras o huesos para hacer seguimiento de las actividades cotidianas o de los suministros esenciales para subsistir. La invención de ábaco supuso un determinante empuje al cálculo y análisis que tanto necesitábamos cuando los dedos y la memoria no eran suficientes, y las primeras bibliotecas representaron además un primer intento de almacenar datos. En la época actual, todo lo que hacemos está continuamente dejando un rastro digital que se puede utilizar y analizar; los avances en tecnología, junto a la expansión de Internet y el almacenamiento en la nube, han provocado que crezca la cantidad de datos que podemos almacenar.</p>
<p>Para resumir, se puede utilizar<strong> 5 V’s</strong> como definición de <strong>Big Data</strong> (empezaron siendo 3), que es lo que caracteriza al sistema y al mismo tiempo explica sus ventajas:</p>
<ol><li><strong>Volumen</strong>. La más evidente y la que hace honor al nombre; captar y organizar absolutamente toda la información que nos llega es esencial para tener registros completos e insesgados, y que las conclusiones que obtengamos sirvan eficientemente a la hora de la toma de decisiones. Es el Business Intelligence que todos conocemos, pero a lo grande; aunque la diferencia con la clásica inteligencia de negocio viene marcada por el resto de V’s.</li>
<li><strong>Velocidad</strong>. Siempre es importante el tiempo si afrontamos tanto la necesidad de generar información (y recordemos que estamos hablando de muchos datos) como de analizarla, pero lo es más si necesitamos reaccionar inmediatamente; todo el proceso pide agilidad para extraer valor de negocio a la información que se estudia y que no se pierda la oportunidad.</li>
<li><strong>Variedad</strong>. Hay que dar uniformidad a toda la información, que tendrá su origen en datos de lo más heterogéneos, tal como veremos en el siguiente apartado. Una de las fortalezas del <strong>Big Data</strong> reside en poder conjugar y combinar cada tipo de información y su tratamiento específico para alcanzar un todo homogéneo.</li>
<li><strong>Veracidad</strong>. Se refiere a la calidad del dato y su disponibilidad; en un entorno descrito por la anterior <em>V, Variedad</em>, hay que encontrar herramientas para comprobar la información recibida; las tecnologías creadas al servicio del <strong>Big Data</strong> se muestran imprescindibles y eficientes para afrontar los retos.</li>
<li><strong>Valor</strong>. Trabajar con <strong>Big Data</strong> tiene que servier para aportar valor a la sociedad, las empresas, los gobiernos, en definitiva, a las personas; todo el proceso tiene que ayudar a impulsar el desarrollo, la innovación y la competitividad, pero también mejorar la calidad de vida de las personas.</li>
</ol><h3>Tipos de datos en Big Data</h3>
<p>Para aclarar qué es lo que se recoge para el análisis, podemos dividirlos en dos grandes categorías:</p>
<ul><li><strong>Datos estructurados</strong>. Aquellos que tienen longitud y formato (por ejemplo fechas) y que pueden ser almacenados en tablas (como las BDR). En esta categoría entran los que se compilan en los censos de población, los diferentes tipos de encuestas, los datos de transacciones bancarias, las compras en tiendas online, etc.</li>
<li><strong>Datos no estructurados</strong>. Son los que carecen de un formato determinado y no pueden ser almacenados en una tabla. Pueden ser de <em>tipo texto</em> (los que generan los usuarios de los foros, redes sociales, documentos de Word), y los de <em>tipo no-texto</em> (cualquier fichero de imagen, audio, vídeo). Dentro de esta categoría, podemos añadir los <strong>Datos semiestructurados</strong>, que son los que no pertenecen a BDR ya que no se limitan a campos determinados, aunque poseen organización interna o marcadores que facilita el tratamiento de sus elementos; estaríamos hablando de documentos XML, HTML o los datos almacenados en BD NoSQL.</li>
</ul><h3>El uso del análisis de datos</h3>
<p>Para poder analizar todo esto, se precisa de técnicas potentes y avanzada; las clásicas medias o varianzas no son por sí solas suficientes para extraer toda esa cantidad de información, ni para entender los diferentes tipos de datos que hemos descrito.</p>
<p>Antes de la irrupción <strong>Big Data</strong>, ya existían algoritmos matemáticos que nos facilitaban descubrir información oculta en los datos, como todos los que engloban el <strong>Data Mining</strong> (minería de datos): k-medias, árboles de decisión, redes neuronales, etc, que con la llegada de la potencia de cálculo de los ordenadores permitieron acortar el tiempo que se tardaba en obtener resultados. Aunque no se pensó para ser en tiempo real si no a posteriori, permite analizar datos para encontrar correlaciones entre ellos y de este modo desarrollar por ejemplo una estrategia de marketing adaptada a las conclusiones.</p>
<p>Por eso el análisis de datos siempre ha tenido un gran peso en el marketing, un mejor conocimiento del consumidor y sus necesidades propicia saber cómo aumentar las ventas; el análisis de datos nos permite establecer relaciones entre variables, predecir comportamientos, realizar agrupaciones (clustering) de grupos homogéneos, e incluso analizar textos para extraer información. Ahora con <strong>Big Data</strong>, todo esto se consigue en tiempo real y con cada nueva actualización de nuestro repositorio de datos es posible ver los cambios en las estadísticas inmediatamente.</p>
<h3>Qué utilidad puede tener</h3>
<p>Como todas las cosas en esta vida, puede tener un buen uso o usarse para propósitos “malvados”. Lo primero que llama la atención es el tema de la privacidad, ya que cada vez más detalles de nuestras vidas son almacenados y analizados por empresas y gobiernos; por supuesto, no es algo que nos debamos tomar a la ligera, pero a medida que siga avanzando la tecnología, habrá que ir adaptando las leyes y regulaciones para proteger a las personas. Por ahora, no hay más rastro de nosotros que los que ya estamos dejando día a día, y que ya están siendo analizados por terceros; a partir de este momento, todos esos registros se unen para formar un todo. Sí, podemos hablar de una representación de nosotros, pero no deja de ser un número entre millones de números, sin cara ni alma. Lo único que va a contar para estudiar es el comportamiento de grupos homogéneos tratados como tendencias en un segundo, para que al siguiente empiece de nuevo el proceso.</p>
<p>En cambio los beneficios son muchos, y muy importantes. Veamos ejemplos.</p>
<ul><li>Una eCommerce puede optimizar el stock de sus almacenes a través de la información extraída de lo que busca la gente en su web o analizando las tendencias en redes sociales y foros; también fijar precios dinámicos en sus productos extrayendo datos de múltiples fuentes (las acciones de los clientes, preferencias de los proveedores o recopilación de precios de la competencia).</li>
<li>El sector de las telecomunicaciones es una industria privilegiada, gracias a sus redes y a la proliferación de dispositivos móviles; la oportunidad más evidente es extraer información de la experiencia del usuario gracias al tráfico de voz y datos, y así poder ofrecer altas en contratos personalizados, ampliar la batalla por la competencia e incluso crear nuevas fuentes de ingresos.</li>
<li>La banca tiene ante si un reto, y una oportunidad, de poner medios para luchar contra el fraude, los delitos financieros y las brechas de seguridad, mediante <strong>Big Data</strong>. Las entidades financieras están invirtiendo enormes cantidades de dinero en perfeccionar algoritmos y la tecnología de análisis para minimizar riesgos y fortalecer su imagen de cara al cliente.</li>
<li>La Federación Alemana de Fútbol empezó a usar el análisis de grandes volúmenes de datos para mejorar el rendimiento de sus jugadores, y con los deberes bien hechos se presentaron en el Mundial de Brasil 2014.</li>
<li>Si piensas que todo lo que puede dar de sí <strong>Big Data</strong> es sólo aprovechable por grandes corporaciones, vas mal encaminado; por ejemplo, las fuerzas de seguridad utilizan estas herramientas para perseguir criminales y luchar contra el terrorismo de cualquier tipo. En materia de sanidad, el cruce de información de historiales clínicos, antecedentes familiares, clima y entorno, junto a los hábitos de consumo, permitirá un modelo predictivo personal para cada paciente, y de esta manera ayudar en la detención precoz de enfermedades y estrategias más efectivas para combatirlas. En muchas ciudades, ya se usa el análisis de datos para transformarse en más modernas e inteligentes: transportes públicos interconectados para minimizar los tiempos de espera, o semáforos que ante la previsión de un aumento del tráfico e regulan para minimizar los atascos.</li>
<li>Y por supuesto, las pymes también pueden subirse al carro del <strong>Big Data</strong>, ya que no es necesaria una gran inversión. Es suficiente con tener un CRM y a un analista de datos para extraer conclusiones de la información que utiliza una pyme, aunque siempre cabe la posibilidad de externalizarlo.</li>
</ul><h3>Big Data, modelando el futuro</h3>
<p>Todo el mundo habla cada día más, es una tendencia en aumento y ha llegado para quedarse. A medida que las herramientas se hagan más accesibles, se integrará poco a poco en nuestras vidas y pasará de ser algo desconocido o temido, a una forma más de comprender el comportamiento humano y nuestra relación con el entorno.</p>
<p>Es como el Social Media, al principio las empresas lo veía como algo ajeno a ellas, que no debían destinar recursos porque creían que no reportaría ningún beneficio; ahora, lo más normal es hacer <em>Social Marketing</em> y elaborar informes exhaustivos con las estadísticas derivadas de su presencia online. Pues ahora es el momento de cruzar esos datos con el resto de aspectos de la organización, como ventas, tráfico web, interacción con distribuidores, etc, para encontrar nuevas vías de negocio y crear nuevas estrategias.</p>
<p>Y por supuesto, para analizar toda esta información, es necesario contar con profesionales que tengan parte analista y parte creativa; estos “<em>científicos de datos</em>” serán muy demandados por las empresas y organizaciones, por lo que se abre un interesantísimo campo laboral para los amantes de los números.</p>
<h2 class="bio">Bibliografía</h2>
<ul class="bio"><li><a href="https://es.scribd.com/document/78295368/TICB1-Mineria-de-Datos" rel="noopener" target="_blank">Scribd (Roger Fabian Molina)</a></li>
<li><a href="https://mibloguel.com/big-data-significado-y-su-utilidad-en-la-sociedad/" rel="noopener" target="_blank">MiBloguel</a></li>
</ul> </article>