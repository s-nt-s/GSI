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

## [Categoría de un sistema](https://www.boe.es/buscar/act.php?id=BOE-A-2010-1330##ani)

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

En la guiá CCN-STIC-803 se dan indicaciones más detalladas de como valorar.

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
