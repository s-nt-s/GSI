---
title: Esquema Nacional de Seguridad (ENS)
status: draft
---

# Conceptos básicos

**ENS**: establece la política de seguridad en la utilización de medios
electrónicos y está constituido por principios básicos y requisitos mínimos
que permitan una protección adecuada de la información. Fue aprobado en
el Real Decreto 3/2010, de 8 de enero.

**ACID-T**: Dimensiones de seguridad contempladas por el ENS; Autenticidad,
Confidencialidad, Integridad, Disponibilidad y Trazabilidad.

**Política de seguridad**: Todos los órganos superiores de las AAPP
deben tener una que siga los principios básicos y requisitos mínimos
del ENS

**[Guías 800 de seguridad CCN-STIC](https://www.ccn-cert.cni.es/guias/guias-series-ccn-stic/800-guia-esquema-nacional-de-seguridad.html)**:
normas, instrucciones, guías y recomendaciones para aplicar el ENS.

## [Principios básicos](https://www.boe.es/buscar/act.php?id=BOE-A-2010-1330#a4)

* Seguridad integral
* Gestión de riesgos
* Prevención, reacción y recuperación
* Líneas de defensa: estrategia de protección constituida por varias capas
(constituidas por medidas de naturaleza organizativa, física y lógica) para:
    * ganar tiempo para racionar a los incidentes que no han podido evitarse
    * reducir la probabilidad de que el sistema sea comprometido en su conjunto
    * minimizar el impacto final sobre el mismo
* Reevaluación periódica
* Función diferenciada: En los sistemas de información se diferenciará el
responsable de la información, el responsable del servicio y el responsable de
la seguridad de manera que:
    * el responsable de la información determina los requisitos de la información tratada
    * el responsable del servicio determina los requisitos de los servicios prestados
    * el responsable de seguridad determina las decisiones para satisfacer los
    requisitos de seguridad de la información y de los servicios

Este último punto implica que la responsabilidad de la seguridad de los sistemas
de información estará diferenciada de la responsabilidad sobre la prestación
de los servicios, y que la política de seguridad debe detallar las atribuciones
de cada responsable y los mecanismos de coordinación y resolución de conflictos.

## [Requisitos mínimos](https://www.boe.es/buscar/act.php?id=BOE-A-2010-1330#a11)

* Organización e implantación del proceso de seguridad: la política de seguridad
debe ser conocida por todos e identificar a sus responsables
* Análisis y gestión de los riesgos: se han de usar metodologías reconocidas
internacionalmente
* Gestión de personal:
    * formación del personal relacionado con la información
    * para corregir o exigir responsabilidades, se identifica de forma única
    quien recibe derechos de acceso, de que tipo y quien ha realizado determinada acción
* Profesionalidad: contar con personal cualificado
* Autorización y control de los accesos
* Protección de las instalaciones: mínimo salas cerradas y control de llaves
* Adquisición de productos
* Seguridad por defecto:
    * los sistemas deben solo ofrecer la funcionalidad mínima necesaria
    * una utilización insegura debe requerir de un acto consciente por parte del usuario
* Integridad y actualización del sistema: toda actualización requiere una autorización
formal
* Protección de la información almacenada y en tránsito:
    * se considera como entornos inseguros los equipos portátiles, PDAs,
    dispositivos periféricos y redes abiertas o con cifrado débil
    * la información en soporte no electrónico derivada de información electrónica
    también debe ser objeto de seguridad
* Prevención ante otros sistemas de información interconectados: el sistema ha
  de proteger el perímetro, en particular, si se conecta a redes públicas
* Registro de actividad: registro de la actividad de los usuarios (respetando el RGPD)
para monitorizar, analizar, investigar y documentar actividades indebidas o no autorizadas,
permitiendo identificar en cada momento a la persona que actúa
* Incidentes de seguridad: detección, reacción y registro de incidentes
* Continuidad de la actividad: copias de seguridad y alta disponibilidad
* Mejora continua del proceso de seguridad

Las medidas a tomar para cumplir los requisitos básicos dependen de la
categoría del sistema y las dimensiones de seguridad (ACID-T).

## Ámbito del ENS

La Guía CCN-STIC-830 desarrolla el ámbito de aplicación del ENS.

1. Ámbito objetivo o material: hardware, software, soporte de información,
comunicaciones, instalaciones, personal y servicios de terceros,
que formen parte de sistemas que gestionen las competencias de entidades públicas
y/o contribuyan a desarrollar el procedimiento administrativo.
2. Ámbito subjetivo: el *sector público* como se detalla en la
[Ley 40/2015](https://www.boe.es/buscar/act.php?id=BOE-A-2015-10566#a2) y
la [Ley 39/2015](https://www.boe.es/buscar/act.php?id=BOE-A-2015-10565#a2):
    * AGE
    * CCAA
    * EELL
    * Sector público institucional:
        * organismos públicos y entidades de derecho público vinculados o dependientes de las AAPP
        * entidades de derecho privado vinculadas o dependientes de las AAPP
        * universidades públicas
    * corporaciones de Derecho Público
3. pudiendo quedar excluidos los sistemas que determinen las AAPP si estos
no esta relacionados con:
    * el ejercicio de derechos ni cumplimiento de
    deberes por medios electrónicos
    * el acceso por medios electrónicos de los
    ciudadanos a la información y al procedimiento administrativo

![Ambito subjetivo del ENS](img/ambito3940.png)

Figura 1: Ámbito de aplicación subjetivo del ENS

La adecuación de los sistemas al ENS se detalla en CCN-STIC-806.

## [Categoría de un sistema](https://www.boe.es/buscar/act.php?id=BOE-A-2010-1330#ani)

La categoría de un sistema se basa en cuan grave sería un incidente que afectara
a la seguridad de los activos en alguna dimensión ACID-T. Se busca determinar
el equilibrio entre la importancia del activo y el esfuerzo de seguridad requerido
(proporcionalidad entre los riesgos y las medidas de seguridad).

La operativa para designar la categoría es la siguiente:

1. Asignar un nivel (bajo, medio o algo) a cada dimensión de seguridad:
    * el responsable de la información valora el nivel de los activos de información
    * el responsable del servicio valora el nivel de los activos de servicio
2. El responsable de sistema asigna la categoría en función del máximo nivel alcanzado:
    * nivel alto -> categoría alta
    * nivel medio -> categoría media
    * nivel básico -> categoría básica

|                            | BAJO            | MEDIO             | ALTO          |
|:---------------------------|:----------------|:------------------|:--------------|
| **Tipo de perjuicio**      | **LIMITADO**    | **GRAVE**         | **MUY GRAVE** |
| **<abbr title="Reducción de forma apreciable de la capacidad de la organización para atender eficazmente con sus obligaciones corrientes">Red. capacidad</abbr>** | apreciable pero sin interrupción |  significativa pero sin interrupción | anulación de la capacidad |
| **Daño en activos**        | menor           | significativo     | muy grave o irreparable |
| **Incumplimiento de<br/>ley o regulación**   | formal subsanable | material o formal no subsanable | grave |
| **Prejuicio al individuo** | menor reparable | significativo de difícil reparación | grabe de difícil o imposible reparación |

Tabla 1: Asignación de niveles en función del tipo de perjuicio

### Guiá CCN-STIC-803: Valoración de sistemas

En la guiá CCN-STIC-803 dan indicaciones de como valorar el nivel de seguridad
de cada dimensión. Para ello propone:

1. Comenzar con la valoración de los activos de tipo **información**
2. Valorarlos en este **orden**: confidencialidad, integridad, trazabilidad, autenticidad
y, si fuera relevante,  disponibilidad (no suele serlo en el tipo *información*)
3. Continuar con los activos de tipos **servicio**, concretamente la dimensión
*disponibilidad* ya que las otras suelen venir impuestos por lo establecido en el
punto anterior para el tipo *información*
4. Asignar a cada dimensión el valor máximo de los activos que comprenda
5. La categoría del sistema corresponderá al nivel máximo de todas las dimensiones

#### Criterios comunes para todas las dimensiones

1. Disposición legal: que exista una disposición legal o administrativa que
condicione el nivel de la dimensión
2. Valorar los criterios de la [Tabla 2](#tb2) haciéndose pregunta
*¿Qué consecuencias tendría...*
por cada dimensión (la respuesta será una de las celdas de la tabla):
    * Confidencialidad: ...la revelación de información a personas no autorizadas?
    * Integridad: ...la modificación de información por alguien no autorizado?
    * Trazabilidad: ...no poder comprobar a posteriori quien ha accedido o modificado cierta información?
    * Autenticidad: ...que la información no fuera auténtica?
    * Disponibilidad: ...que una personas o sistema autorizado no pudiera usar
    el servicio?

| Criterio           | < | BAJO | MEDIO | ALTO |
|:-|:-|:-|:-|:-|
| **Perjuicio directo al ciudadano** | < | alguno | importante pero subsanable | grave de difícil o imposible reparación |
| **Incumplimiento<br/>de una norma** | **legal/administrativa** | leve subsanable | material o formal no subsanable | material y formal grave |
| ^ | **regulatoria** | incumplimiento | sanción significativa | sanción grave y/o perdida de licencia para operar |
| ^ | **contractual** | formal leve | material o formal | material o formal grave |
| ^ | **interna** | ^ | ^ | ^ |
| **Pérdidas económicas** | < | < 4% presupuesto anual | del 4% al 10% | > 10% |
| **Reputación (daño)** | < | moderado | significativo | grave |
| **Protestas** | < | individuales | públicas | masivas |
| **Delitos** | < | favorecería el delitos | favorecería significativamente o<br/>dificultaría su investigación| incitaría al delito o>es un delito en si o<br/>dificultaría enormemente su investigación |

Tabla 2: Criterios comunes a información y servicios en todas las dimensiones

Para todos los casos, a parte de las contestaciones de esta tabla, puede darse
el caso de <abbr title="no aplicable">N/A</abbr>, por ejemplo, si la revelación
de información no implica perdidas económicas ese criterio quedará marcado con
<abbr title="no aplicable">N/A</abbr>.

Adicionalmente para la dimensión *disponibilidad* se toma en como criterio el RTO:

* Si RTO > 5 días: N/A
* Si RTO <= 5 días: BAJO
* Si RTO <= 1 día: MEDIO
* Si RTO <= 4 horas: ALTO

## [Medidas de seguridad](https://www.boe.es/buscar/act.php?id=BOE-A-2010-1330#anii)

Las medidas de seguridad se dividen en tres grupos:

1. Marco organizativo [org]: medidas relacionadas con la organización global de la seguridad
2. Marco operacional [op]: medidas para proteger la operación del sistema como conjunto integral de componentes para un fin
3. Medidas de protección [mp]: medidas centradas en proteger activos concretos

Las **medidas que se aplican siempre** son:

* Marco organizativo (todas):
    * Política de seguridad
    * Normativa de seguridad
    * Procedimientos de seguridad
    * Proceso de autorización
* Marco operacional:
    * Planificación:
        * Adquisición de nuevos componentes
    * Control de acceso:
        * Identificación
        * Requisitos de acceso
        * Proceso de gestión de derechos de acceso
    * Explotación:
        * Inventario de activos
        * Configuración de seguridad
        * Mantenimiento
        * Protección frente a código dañino
* Medidas de protección:
    * Protección de las instalaciones e infraestructuras:
        * Áreas separadas y con control de acceso
        * Identificación de las personas
        * Acondicionamiento de los locales
        * Protección frente a incendios
        * Registro de entrada y salida de equipamiento
    * Gestión del personal:
        * Deberes y obligaciones
        * Concienciación
        * Formación
    * Protección de los soportes de información:
        * Etiquetado
        * Custodia
        * Transporte
    * Protección de la información:
        * Datos de carácter personal
        * Limpieza de documentos
        * Copias de seguridad (backup)
    * Protección de los servicios:
        * Protección del correo electrónico


# Bibliografía

* PreparaTic27 - Pack1/048
