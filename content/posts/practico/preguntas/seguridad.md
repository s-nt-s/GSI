---
title: Medidas de seguridad
---

<!--

| Ley/Guía     | Título |
|--------------|----------|
| RD 3/2010    | Esquema Nacional de Seguridad |
| CCN-STIC-801 | Responsabilidades y Funciones |
| CCN-STIC-805 | Política de Seguridad de la Información |
| RD 3/2010 A1 | Categorías de los sistemas |
| CCN-STIC-803 | Valoración de Sistemas |
| RD 3/2010 A2 | Medidas de seguridad |
| CCN-STIC-804 | Guía de implantación |
| RGPD         | Reglamento (UE) 2016/679: Reglamento General de Protección de Datos |
| LOPD-GDD     | LO 3/2018: Protección de Datos Personales y garantía de los derechos digitales |

-->
# Valoración del sistema

Usar RD 3/2010 A1 y CCN-STIC-803

**1.** Valorar los criterios de la siguiente tabla haciéndose pregunta
*¿Qué consecuencias tendría...*
por cada dimensión (la respuesta será una de las celdas de la tabla o *no aplica*):

* Confidencialidad: ...la revelación de información a personas no autorizadas?
* Integridad: ...la modificación de información por alguien no autorizado?
* Trazabilidad: ...no poder comprobar a posteriori quien ha accedido o modificado cierta información?
* Autenticidad: ...que la información no fuera auténtica?
* Disponibilidad: ...que una persona o sistema autorizado no pudiera usar
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
| **Delitos** | < | favorecería el delitos | favorecería significativamente o<br/>dificultaría su investigación| incitaría al delito o es un delito en si o<br/>dificultaría enormemente su investigación |

**2.** Valorar la dimensión **disponibilidad** según RTO:

* si RTO > 5 días: N/A
* si RTO <= 5 días: BAJO
* si RTO <= 1 día: MEDIO
* si RTO <= 4 horas: ALTO

Con ello rellenamos la tabla:

| Activo | Tipo        | C | I | T | A | D |
|--------|-------------|---|---|---|---|---|
| Ej 1   | servicio    |   |   |   |   |   |
| Ej 2   | información |   |   |   |   |   |
| **Valor máximo** | < |   |   |   |   |   |

# Medidas de seguridad

Usar RD 3/2010 A2 y CCN-STIC-804 para ENS, y RGPD y LOPD-GDD protección de datos
(realizar evaluación de impacto - Art 35 RGPD - si corresponde).

## Marco organizativo

1. `[org.1]` Incluir el sistema dentro de la Política de Seguridad (CCN-STIC-805) del organismo
2. `[org.4]` Establecer un proceso formal de autorización que cubra todos los elementos del sistema

## Marco operacional

1. `[op.pl.1]` Realizar un análisis de riesgo: informal (BAJO), semiformal (MEDIO) y formal (ALTO)
2. `[op.acc.1 AT]` Definir controles de identificación que:
    * permita saber quién recibe y qué derechos de acceso recibe, y quién ha hecho algo y qué ha hecho
    * se deshabiliten las cuentas cuando el usuario cese en sus funciones o quien autorizo revoque dicha autorización
    * cumpla la siguiente correspondencia entere nivel de **autenticidad** y los nivel de seguridad:
        * autenticidad BAJO -> nivel de seguridad bajo, sustancial o alto (ej: login/password)
        * autenticidad MEDIO -> nivel de seguridad sustancial o alto (ej: login/password + OTP, certificado electrónico SW)
        * autenticidad ALTO -> nivel de seguridad alto (ej: certificado electrónico cualificado en soporte HW)
3. `[op.acc.2 ICAT]` Definir requisitos de acceso que garanticen que únicamente las personas autorizadas pueden consultar información o interactuar con el sistema
4. `[op.acc.5 ICAT]` Uso de Mecanismo de autenticación adecuado al Reglamento eIDAS:
    * BAJO: un solo factor, y si este es *algo que se sabe* se aplicará reglas básicas de calidad
    * MEDIO: dos factores, y si alguno es *algo que se sabe* se establecerán exigencias rigurosas de calidad y renovación
    * ALTO: las credenciales
        * se obtienen tras un registro presencial o telemático usando certificado cualificado en dispositivo cualificado de creación de firma
        * caducan
        * para *algo que se tiene*, se requerirá el uso de elementos criptográficos HW usando algoritmos y parámetros acreditados por el CCN
5. `[op.exp.1]` Realizar Inventario de activos detallando su naturaleza e identificando a su responsable
6. `[op.exp.6]` Protección frente a código dañino:
    * Monitorizar puntos de entrada y salida
    * Uso firewalls
7.  `[op.exp.8 T]` Registro de la actividad de los usuarios que incluye *qué*, *quién*, *cuando* y
si tuvo éxito o error. Según el nivel de **trazabilidad**:
    * BAJO -> registros de actividad en los servidores
    * MEDIO -> revisión informal de los registros de actividad buscando patrones anormales
    * ALTO -> sistema automático de recolección de registros y correlación de eventos

Para categoría **MEDIA**:

1. `[op.exp.5]` Gestión de cambios para evitar modificaciones no controladas o errores
2. `[op.exp.7y9]` Realizar Gestión de incidentes y un Registro de la gestión de incidentes que:
    * incluye reporte inicial, las actuaciones de emergencia y las modificaciones del sistema derivadas del incidente
    * incluye evidencia que pueda, posteriormente, sustentar una demanda judicial, o hacer frente a ella
    * tras su análisis se revisará la determinación de los eventos auditables
3. `[op.acc.3 ICAT]` Segregar funciones y tareas (CCN-STIC-801) que garantice que se separen mediante controles lógicos suficientes las tareas incompatibles
4. `[op.mon.1]` Uso de herramientas de detección o prevención de intrusión

Para categoría **ALTA**:

1. `[op.pl.5]` Uso de Componentes certificados, sus funcionalidades y nivel de seguridad ha sido
evaluado conforme a normas europeas o internacionales reconocidas por el Esquema Nacional de Evaluación y Certificación de la Seguridad de las Tecnologías de la Información
2. `[op.ext.9 D]` Medios alternativos
3. `[op.cont.2 D]` Incluir el sistema dentro del Plan de Continuidad del Organismo
4. `[op.exp.10 T]` Protección de los registros de actividad

## Medidas de protección

1. `[mp.if.1]` Áreas separadas y con control de acceso
2. `[mp.per.3]` Concienciación del personal
3. `[mp.com.1]` Perímetro seguro con cortafuegos (en **ALTA** serán de distintos fabricantes
  en cascada y con sistemas redundantes)
4. `[mp.per.4]` Formación para evitar riesgos asociados a un mal uso del sistema a causa del desconocimiento de su funcionamiento
5. `[mp.info.1]` Cumplir el RGPD y LOPD-GDD en cuanto a los Datos de carácter personal
6. `[mp.info.9 D]` Copias de seguridad

Por categoría **MEDIA**:

1. `[mp.com.2 C]` Protección de la confidencialidad usando VPN para conexiones foráneas y usando certificados acreditados por el CCN. En el nivel **ALTO** se usará
preferentemente dispositivos HW
2. `[mp.sw.1]` Desarrollo de aplicaciones en un entorno diferente y separado de producción,
utilizando una metodología de desarrollo reconocida que tome en consideración
aspectos de seguridad, datos usados en pruebas y permita inspección de código

Para categoría **ALTA**:

1. `[mp.com.4]` Segregación de redes para tener control de entrada de usuarios y salida de información
2. `[mp.com.9 D]` Medios alternativos de comunicación para el caso que fallen los medios habituales
3. `[mp.info.3 C]` Cifrado de la información, solo estando en claro mientras se hace uso de ella
4. `[mp.info.5 T]` Sellos de tiempo que prevendrán la posibilidad del repudio posterior
