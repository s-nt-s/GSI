---
title: Bases de datos relacionales
status: draft
replace:
  "DBA": '<abbr title="Administrador de la base de datos" class="abbr">abbr</a>'
---
# Conceptos básicos

* **DDL**: creación, manipulación o borrado de tablas y de todo lo relacionado con ellas como
los atributos, índices o reglas de integridad (ej: CREATE, DROP, ALTER)

* **DML**: consultas, inserciones, modificaciones o borrados de los datos
(ej: SELECT, INSERT, UPDATE, DELETE)

* **DCL**: controla el acceso a los datos (ej: GRANT, REVOKE)

Propiedades **ACID**:

* **A**tomicidad: la transacción tiene efecto o no en su totalidad, nunca parcialmente
* **C**onsistencia: se debe preservar la integridad y consistencia de la BD
* A**i**slamiento: los cambios no son visibles hasta ejecutar el *commit*
* **D**uradero: los cambios se hacen persistente una vez ejecutado el *commit*

# SGDB

## Arquitectura ANSI/X3/SPARC

1. **Nivel físico** o interno: describe cómo los datos se almacenan en la base
de datos y en el hardware del equipo
2. **Nivel conceptual**: describe los datos que se almacenan dentro de la BD y
cómo los datos están relacionados entre sí (el DBA trabaja en este nivel)
3. **Nivel lógico** o externo: formado por las *vistas de usuario*, que excluye datos
irrelevantes y datos que el usuario no está autorizado a acceder (el usuario trabaja en este nivel)

ANSI establece 3 familias de modelos de datos:

* Modelo **relacional**: al que nos referimos cuando hablamos de SGDB sin concretar
* [Modelo **codasyl**](https://es.wikipedia.org/wiki/CODASYL): estructura en red
donde se establecen relaciones n:m
* Modelo **jerárquico**: presenta una estructura en árbol donde nodos y ramas siguen una relación
del tipo 1:n

## Concurrencia

Los problemas que pueden surgir a raíz de distintas transacciones concurrentes
(T1 y T2):

* **Lectura no repetible**: T1 lee dos veces un valor y no coincide porque entre
medias T2 lo ha cambiado
* **Lectura sucia**: T1 lee un dato modificado por T2 antes de que este haya hecho
el *commit* de manera que si T2 falla (rollback) o vuelve a modificar el dato, T1
habría leído un dato que nunca llego a ser valido
* **Lectura fantasma**: T1 hace dos veces la misma consulta y en la segunda obtiene
más datos porque entre medias T2 añadió nuevas filas

Esto esta relacionado con los niveles de aislamiento:

* **Lectura no comprometida**: Los cambios realizados por las transacciones se encuentran
disponibles inmediatamente
* **Lectura comprometida**: Los cambios solo están disponibles después del *commit*.
Precie *lecturas sucias*
* **Lectura repetible**: las filas leídas o actualizadas por una transacción quedan
bloqueadas hasta que finaliza dicha transacción. Previene la *lectura sucia* y
la *lectura no repetible*
* **Serializable**: las transacciones ejecutadas de manera simultanea producen los
mismos efectos que si se ejecutaran en serie. Previene todos los problemas

| Nivel de<br/>aislamiento | Lectura | < | < |
|-|-|-|-|
| ^            | sucia | no repetible | fantasma |
| Lectura **no**<br/>comprometida | SI | SI | SI |
| Lectura<br/>comprometida        | NO | SI | SI |
| Lectura<br/>repetible           | NO | NO | SI |
| Serializable                    | NO | NO | NO |

Tabla: Niveles de aislamiento

El mecanismo de control más usado es el [**Two-phase-locking**](https://es.wikipedia.org/wiki/Bloqueo_de_dos_fases) que garantiza la serialización de las transaciones.
Su funcionamiento consiste en que cada transacción debe emitir todas las solicitudes
de bloqueo antes de que pueda emitir cualquier solicitud de desbloqueo. Las **fases** son:

* Fase de expansión (crecimiento): la transacción emite cualquier nueva solicitud
de bloqueo que se requiera. Las solicitudes de desbloqueo no están permitidas en esta fase.
* Fase de reducción: la transacción libera bloqueos adquiridos en la fase de expansión.
Las nuevas solicitudes de bloqueo no están permitidas en esta fase.

# Modelo Entidad/Relación Extendido

Se compone de **Entidades**:

* regulares: existe por si mismas
* débiles: su existencia depende de otra entidad

![](img/entidad.png)

y **Relaciones**:

* relaciones regulares
* relaciones débiles:
    * dependencia de existencia: las ocurrencias de la entidad débil
    no pueden existir sin la ocurrencia de la entidad regular de la que dependen
    * dependencia de identificación: además de lo anterior, las ocurrencias del
    la entidad débil no se pueden identificar sólo mediante sus propios atributos,
    sino que se les tiene que añadir el identificador de la entidad regular de la
    que dependen
* relaciones exclusivas: su existencia entre dos entidades implica la no existencia
de otras relaciones

![](img/relacion_exclusividad.png)

Las **relaciones** se caracterizan por su:

* **Tipo de correspondencia**: número máximo de ocurrencias de una entidad que
pueden intervenir en una ocurrencia de la relación:
    * relaciones **1:1**: cada ocurrencia de una entidad se relaciona con una y
    solo una ocurrencia de la otra entidad
    * relaciones **1:N**: cada ocurrencia de una entidad puede estar relacionada
    con cero, una o varias ocurrencias de la otra entidad
    * relaciones **M:N**: cada ocurrencia de una entidad puede estar relacionada
    con cero, una o varias ocurrencias de la otra entidad y viceversa
* **Cardinalidad**: el número máximo y mínimo de ocurrencias de una entidad que
pueden estar interrelacionadas con una ocurrencia de otro entidad

La **cardinalidad máxima** coincide con el **tipo de correspondencia**.

![](img/relacion_correspondencia.png)

Figura: Representación de la correspondencia

![](img/relacion_cardinalidad.png)

Figura: Representación de la cardinalidad

Las extensiones del modelo E/R consisten en:

* **Generalización**: se abstrae una entidad de nivel superior a partir de
varias entidades (ej: de *profesor* y *estudiante* a *persona*)
* **Especialización**: inversa de *generalización* (ej: de *empleado* a
*secretario*, *técnico* e *ingeniero*)
* **Categorías**: subtipo que aparece como resultado de la unión de varios
tipos de entidad (ej: teniendo *persona* y *compañia* se crea subtipo
*propietario* para relacionarlo con *vehículo*)
* **Agregación**: construir un nuevo tipo de entidad como composición de otros
y sus relaciones (ej: teniendo *empresa* y *solicitante* relacionados por
*entrevista* se crea el tipo compuesta *empresa-entrevista-solicitante* para
relacionarla con *oferta*)
* **Desagregación**: inverso de la *agregación*
* **Asociación**: relacionar dos tipos de entidades que normalmente son de dominios
independientes, pero coyunturalmente se asocian

Estas extensiones dan lugar a jerarquías entre tipos y subtipos

![Jerarquías E/R](img/er_jerarquia.png)

Figura: **d** = los subtipos son disjuntos<br/>**O** = los subtipos pueden solaparse<br/>**U** = uniones por categorías.<br/>La presencia de una jerarquía total se representa con una doble línea entre el supertipo y el triángulo.

# Bibliografía

* PreparaTic27 - Pack1/063
* PreparaTic27 - Pack1/064
* PreparaTic27 - Pack1/088
* [manuel.cillero.es - Modelo Entidad/Relación Extendido](https://manuel.cillero.es/doc/metodologia/metrica-3/tecnicas/modelo-entidad-relacion-extendido/)
* [glosarioit.co - Bloqueo de dos fases](https://www.glosarioit.com/Bloqueo_de_dos_fases)
