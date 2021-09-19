---
title: Big Data
---

# Conceptos básicos

**Data lake**: repositorio de datos al natural (sin modificaciones)
de todo tipo (estructurados, semi-estructurados, no estructurados, binarios, etc).

**Data Warehouse** (DW): base de datos corporativa caracterizada por la
integración y depuración de información procedente de múltiples fuentes de datos
tanto internas como externas a la organización.
Su fin es el de procesar la información para poder analizarla.

**Data Mart**: almacenes de datos especializados por áreas o temas.

**Big data**: conjuntos de datos tan grandes y complejos que precisan de aplicaciones
informáticas no tradicionales de procesamiento de datos para tratarlos adecuadamente.

**Minería de datos**: extracción de patrones o de información implícita u oculta
contenida en los datos.

# Data Warehouse

Un DW se caracteriza por ser **OVNI**:

* estar **O**rientado a temas
* son **V**arriantes en el tiempo: toda información tiene una referencia temporal
* son **N**o volátiles, pues la información solo es de consulta, ni se puede borrar
ni modificar.
* son una solución **I**ntegral, pues la información procedente de diversas fuentes.

## Aprovisionamiento del DW

Para poblar de datos un DW desde distintas fuentes se hace uso de herramientas ETL:
(ej: Pentaho Data Integration, Scriptella, Ab Initio o AWS Glue).

Hay dos enfoques posibles:

* Bottom Up: Se aprovisionan almacenes temáticos (Data Mart) y del conjunto de ellos se crea
el DW.
* Top Down: Se aprovisiona el DW y, si se requiere especialización temática, se aprovisionan a
partir del DW los Data Marts.

## Explotación del DW

Los DW, a diferencia de los sistemas transaccionales (OLTP), se basan en
el uso de estructuras multidimensionales que permiten la manipulación y
visualización de los datos de manera más eficiente (OLAP).
Son una variante de los modelos relacionales tradicionales y se componen de:

* Tablas de **hechos**: donde se almacena la información propiamente dicha (ej: Ventas)
* Tablas de **dimensiones**: perspectivas de alto nivel acerca de los datos
(ej: Marcas, Productos, Clientes y Tiempo).

![](img/dw.png)

Figura 1: Tablas de hechos y dimensiones

Este modelo permite representar la información mediante Cubos OLAP (o dimensionales)
donde cada eje representa las dimensiones requeridas para las búsquedas.

Las operaciones  habituales de este modelo son:

* **Slice-and-dice**: permite obtener los datos seleccionando un valor fijo de una dimensión
* **Drill-down**: permite ver datos de nivel inferior (aumenta nivel de detalle)
* **Roll-up**: permite ver datos con mayor nivel de agregación (disminuye nivel de detalle)
* **Pivot**: permite cambiar los ejes
* **Drill-across**: similar a drill-down, con la diferencia de que su forma de ir de lo general a lo
específico es agregar un atributo a la consulta como nuevo criterio de análisis
* **Drill-through**: permite visualizar los datos relacionados al valor de un Indicador en su máximo
nivel de detalle

![](img/rollup-drilldown.png)

Figura 2: Operaciones OLAP Roll Up, Drill Down, Slice and Dice

# Arquitectura OLAP

Su objetivo es agilizar la consulta de grandes cantidades de datos, por lo que es
lo más rápido para ejecutar sentencias SQL de tipo SELECT.

Se usa en:

* Data Warehouse
* Sistemas de soporte a decisiones (DSS)
* Sistemas de información ejecutiva (EIS)
* Inteligencia de negocios (o Business Intelligence)

Tipos de sistemas OLAP:

* **ROLAP**: a nivel físico la información se almacena de forma relacional,
pero para su explotación se construyen cubos dinámicamente.
* **MOLAP**: la información se almacena directamente de forma multidimensional (cubos).
* **HOLAP**: mezcla de los dos anteriores.

Algunos ejemplos de BBDD que permiten almacenar cubos MOLAP/HOLAP son:
Hbase, Oracle OLAP o SQL Server Analysis Services.

# Minería de datos

El concepto minería de datos abarca:

* la etapa de análisis en bruto
* aspectos de gestión de datos y de bases de datos
* el procesamiento de los datos, del modelo y de las consideraciones de inferencia
* la generación de métricas de intereses
* el post-procesamiento de las estructuras descubiertas, su visualización y la actualización en línea

Para definir modelos relacionados con los análisis predictivos y la minería de
datos que puedan ser intercambiados por distintas aplicaciones se usa
el lenguaje de marcado **PMML** creado por el Data Mining Group.

Las características principales de la minería de datos son:

* Trabaja con la información oculta
* Suelen ser soluciones con una arquitectura cliente-servidor
* Poseen gran variedad de herramientas para la extracción de la información
* Es habitual hacer uso de un procesamiento paralelo que acelere el proceso
* Produce cinco tipos de información:
    * Asociaciones
    * Secuencias
    * Clasificaciones
    * Agrupamientos
    * Pronósticos

Algunas de las técnicas de aprendizaje automático usadas son:

* Redes neuronales
* Árboles de decisión
* Algoritmos genéticos
* Clustering o agrupamiento

Dichas técnicas se clasifican en:

* De **verificación**: verifica la validez de la información que se le presenta
* **Supervisados**: cuentan con una fase de entrenamiento para construir el modelo,
es decir, predicen un dato desconocido a priori a patir de otros conocidos
( regresión, árboles de decisión, redes neuronales, estadísticos, etc)
* **No supervisados**: no cuentan con esa fase de entrenamiento, es decir,
se descubren patrones y tendencias en los datos (clustering, redes de asociación, etc)

# Big Data

Se caracteriza por las siguientes **V**s (principalmente las 3 primeras):

* **Volumen**: se trabaja con gran cantidad de datos
* **Velocidad**: los datos están en movimiento como consecuencia de la creación de datos en tiempo real
* **Variedad**: diferentes tipos de fuentes y de datos
* **Veracidad de los datos**: en referencia a la incertidumbre de los datos, es decir, al grado de
fiabilidad de la información
* **Viabilidad**: capacidad de una organización para utilizar de forma eficaz el gran volumen de datos
que maneja
* **Visualización de los datos**: la forma en que los datos son presentados una vez que se procesan
* **Valor de los datos**: se refiere al valor que se puede obtener de ellos cuando se transforman en
información

Los datos puedes ser:

* estructurados: bases de datos
* semi-estructurados: XML, JSON, etc
* no estructurados: texto random, contenido multimedia, etc

y pueden ser procesados mediante:

* **batch** o lotes: procesamiento de forma espaciada en el tiempo (ej: cada 15 minutos)
* **stream** o tiempo (semi-)real: procesamiento de los datos (casi) en el momento
en que estos se producen (ej: cada segundo)

## Fases y procesos de Big Data

1. **ETL**
2. **Análisis de los datos**. Algunos tipos:
    * Análisis **descriptivo**: explica la situación de lo qué ha pasado
    * Análisis **diagnóstico**: explica la situación del por qué ha pasado
    * Análisis **predictivo**: anticipa lo qué pasará
    * Análisis **prescriptivo**: recomienda qué podemos hacer para que pase
3. Visualización de datos. Ejemplo de herramientas a tal propósito:
    * Tableau
    * IBM Watson Analytics
    * MS Power BI
    * Qilk
    * Microstrategy

# Apache Hadoop

Hadoop es un entorno de trabajo para programar aplicaciones distribuidas que manejen
grandes volúmenes de datos. Su objetivo es acercar el procesamiento al lugar en
donde se encuentran almacenados para reducir el tráfico de red y el tiempo invertido
en él.

Para ello hace uso de tres servicios:

* Almacenamiento fiable de datos utilizando HDFS
* Procesamiento de datos en paralelo para sistemas de alto rendimiento mediante MapReduce
* Hadoop Common: Conjunto de utilidades para la integración de subproyectos de Hadoop.
Proporciona acceso a los sistemas de archivos soportados por Hadoop.

Un clúster típico Hadoop incluye unodo maestro y múltiples nodos esclavo.

* El nodo maestro consiste en jobtracker (rastreador de trabajo), tasktracker (rastreador de tareas), namenode (nodo de nombres), y datanode (nodo de datos).
* Un esclavo o compute node (nodo de cómputo) consisten en un nodo de datos
(datanode) y un rastreador de tareas.

Hadoop requiere JRE 1.6 o superior, y los scripts de arranque y apagado
requiere tener habilitado SSH entre los nodos del cluster.

![](https://upload.wikimedia.org/wikipedia/commons/2/2b/Hadoop_1.png)

Figura 3: Cluster Hadoop multinodo

## HDFS

HDFS es un sistema de archivos distribuidos en cada nodo de un clúster.
Es escalable, tolerante a fallos y permite alta concurrencia y un intenso
acceso a datos.

Esta pensado principalmente para programas batch donde los datos no son en tiempo
real. Divide archivos en bloques de tamaño fijo y los distribuye en distintos nodos
del clúster. La alta disponibilidad se consigue a través de la replicación de
archivos en el cúster.

En HDFS se distinguen dos tipos de máquinas:

* **Namenode**: Actúa como máster y almacena todos los metadatos necesarios para
construir el sistema de ficheros a partir de los datos que almacenan los
*datanodes*, es decir, almacena la estructura de directorios y de ficheros y
los metadatos necesarios para componer cada fichero a partir de sus bloques.
La localización de los bloques en el clúster la almacena en memoria RAM,
a partir de la información que le proporcionan los *datanodes* al arrancar el sistema de archivos.
* **Datanonde**: Se pueden considerar esclavos, se limitan casi prácticamente a
almacenar los bloques que componen cada fichero, así como, a proporcionarlos
al *namenode* o a los clientes que lo solicitan.

Además, el *namenode* proporciona:

* balanceo: al distribuir los bloques entre los diferentes *datanodes*
* tolerancia a fallos: detectando mediante heartbeat si un *datanode* ha caído
y en tal caso replicando sus datos a otro

## MapReduce en Hadoop

1. Fase **Map**: se ejecuta en subtareas llamadas mappers, que son los
responsables de generar pares clave-valor filtrando, agrupando, ordenando o
transformando los datos originales. Los pares de datos intermedios no se almacenan en HDFS.
2. Fase **Shuffle** (sort): paso intermedio (si es necesario) entre Map y Reduce
que ayuda a recoger los datos y ordenarlos de manera conveniente para el
procesamiento. Se busca agregar las ocurrencias repetidas en cada uno de los mappers.
3. Fase **Reduce**: gestiona la agregación de los valores producidos por todos
los mappers del sistema (o por la fase shuffle) de tipo clave-valor en función
de su clave. Cada reducer finaliza generando un fichero de salida de forma
independiente, generalmente escrito en HDFS.

![](https://aprenderbigdata.com/wp-content/uploads/MapReduce-esquema-1024x615.png)

Figura 4: MapReduce en Hadoop

### Job Tracker y Task Tracker

El motor MapReduce de Hadoop consiste en un unico *job tracker* (master) que
recibe los trabajos enviados por los clientes y múltiples *task tracker*
(slave, hay uno en cada workernode).

El *job tracker* divide un *job* en múltiples trabajos repartido entre los *task tracker*
disponibles en el clúster, intentando mantener el trabajo lo más cerca posible de los datos.
El *task tracker* a su vez, asigna cada tarea (una operación *map* o una operación *reduce*)
a uno de los *task slot* disponibles en el nodo.

Si el trabajo no puede ser almacenado en el nodo que tiene los datos, se da prioridad
a los nodos del mismo rack.

Si un trabajo no llega a tiempo o falla, es reprogramado. El *task tracker*
genera en cada nodo un proceso separado para evitar que el propio *task tracker*
falle si falla un trabajo.

El *task tracker* manda periódicamente información al *job tracker* para que este
sepa su estado.

El *job tracker* es capaz de reanudar un trabajo por donde lo dejo en caso de fallo,
a partir de la versión Hadoop 0.21.

## YARN

Hadoop YARN permite a Hadoop soportar varios motores de ejecución y proporciona
un planificador agnóstico a los trabajos que se encuentran en ejecución en el clúster.

Esta mejora es también conocida como Hadoop 2 y permite usar motores de ejecución
distintos a MapReduce.

![](https://aprenderbigdata.com/wp-content/uploads/Apache-Hadoop-1-vs-2-768x350.png)

Figura 5: Evolución de Hadoop 1 a 2

Se divide en tres componentes principales: Resource Manager, Node Manager y Application Master.

## Proyectos relacionados con Hadoop

Apache **Ambari**: herramienta basada en web para el aprovisionamiento, administración y
seguimiento de clústeres Apache Hadoop, que incluye soporte para Hadoop HDFS, Hadoop
MapReduce, Hive, HCatalog, HBase, ZooKeeper, Oozie, Pig y Sqoop.

Apache **Avro**: sistema de serialización de datos que provee estructuras de
datos, un formato de datos binario compacto y rápido, un archivo contenedor para almacenar
datos persistentes e integración con lenguajes dinámicos.

Apache **Cassandra**: base de datos distribuida de segunda generación altamente
escalable, que tiene un diseño totalmente distribuido de Dynamo y el modelo de datos basado
en ColumnFamily de Bigtable.

Apache **Flume**: se utiliza para almacenar datos (semiestructurados o no estructurados) en streaming en
HDFS. Es muy útil cuando existe múltiples servidores generando datos de forma continua.

Apache **HBase**: una base de datos escalable y distribuida que soporta el almacenamiento de datos
estructurados en tablas. Permite la realización de tablas a partir de ficheros de datos.

Apache **HCatalog**: proyecto para gestionar los metadatos de Hive con el fin de que puedan
accederse a ellos con Pig y MapReduce.

Apache **Hive**: facilita la consulta y gestión de grandes conjuntos de datos que residen en
almacenamientos distribuidos. Hive proporciona un mecanismo para la ver la estructura de los
datos utilizando un lenguaje similar a SQL llamado HiveQL.

Apache **Mahout**: software libre centrado en la implementación de algoritmos de machine
learning distribuidos.

Apache **Oozie**: gestor de flujos de trabajo que permite planificar la ejecución de jobs MapReduce
(ej: de forma programada en un momento dado, cuando lleguen nuevos datos).

Apache **Pig**: plataforma para el análisis de grandes conjuntos de datos que se
caracteriza por un lenguaje de alto nivel para la creación de los programas de análisis de datos,
junto con la infraestructura necesaria para la evaluación de estos programas.
Su estructura es susceptible de una paralelización
sustancial, lo que a su vez permite manejar grandes conjuntos de datos.

Apache **Spark**: motor de cálculo rápido y general para datos Hadoop. Proporciona
un modelo de programación sencillo y expresivo que soporta una amplia gama de aplicaciones,
incluyendo ETL, machine learning, procesamiento de flujo, y computación gráfica.

Apache **ZooKeeper**: servicio centralizado construido para mantener la información de
configuración, proporcionar sincronización distribuida y la prestación de servicios de grupo.

Apache **Parquet** y Apache **OCR**: formatos de almacenamiento de datos orientado a columnas.

# Tipos de bases de datos NoSQL

* **Clave-valor**: cada elemento se asocia con una clave única. Ej: Redis, DynamoDB, Aerospike, etc.
* **Documentales**: almacenan la información como si fueran documentos utilizando estructuras
como JSON o XML. Ej: Mongo DB, Couch DB, Raven DB, etc.
* Orientadas a **Grafos**: la información se almacena como nodos y las relaciones a través de las
aristas del grafo. Ej: Neo4j, Orient DB, Arango DB, etc.
* Orientadas a **Objetos**: la información se almacena como objetos. Ej: Versant, Object DB, etc.
* **Columnares**: estos sistemas almacenan los datos cambiando el enfoque transaccional de filas a
columnas. Ej: Cassandra, Hbase, etc.

# Bibliografía

* <strike title="Inteligencia artificial es un tema relacionado con BigData, pero en el temario no aparece explícitamente">PreparaTic27 - Pack1/070</strike>
* <strike title="Conocimiento experto es un tema relacionado con BigData, pero en el temario no aparece explícitamente">PreparaTic27 - Pack1/071</strike>
* PreparaTic27 - Pack1/075
* PreparaTic27 - Pack1/076
* PreparaTic27 - Pack3/07/23
* [blog.powerdata.es - Data Lake vs Data Warehouse. Veamos sus principales diferencias](https://blog.powerdata.es/el-valor-de-la-gestion-de-datos/data-lake-vs-data-warehouse.-veamos-sus-principales-diferencias)
* [campusbigdata.com- Data Mining vs Big Data](https://www.campusbigdata.com/big-data-blog/item/82-data-mining-vs-big-data)
* [geographica.com - Qué es Business Intelligence y cómo se relaciona con el Big Data](https://geographica.com/es/blog/business-intelligence-se-relaciona-big-data/)
* [autoritas.net - Escala de valor en la analítica de datos. By Gartner](https://www.autoritas.net/2016/05/16/escala-de-valor-en-la-analitica-de-datos-by-gartner/)
* [docplayer.net - IBM Big Data Platform](https://docplayer.net/8988314-Ibm-big-data-platform.html)
* [thuyct89.wordpress.com - Overview about Big Data course](https://thuyct89.wordpress.com/2016/08/31/overview-about-big-data-course/)
* [aprenderbigdata.com - ¿Qué es Hadoop MapReduce?](https://aprenderbigdata.com/hadoop-mapreduce/)
* [aprenderbigdata.com - Introducción a Cloudera y Componentes](https://aprenderbigdata.com/introduccion-cloudera-hadoop/)
* [hadoop.apache.org - MapReduce Tutorial](https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)
* [aprenderbigdata.com - ¿Qué es Hadoop Yarn?](https://aprenderbigdata.com/hadoop-yarn/)
* [youtube.com - 019 MapReduce Daemons JobTracker and TaskTracker Explained](https://www.youtube.com/watch?v=doRS6xUoAyY)
