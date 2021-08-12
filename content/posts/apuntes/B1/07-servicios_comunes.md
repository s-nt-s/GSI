---
title: Servicios comunes
replace:
  "☑": '<abbr class="nou comun" title="Servicio declarado como compartido">☑</abbr>'
  "☐": '<abbr class="nou nocom" title="Servicio NO declarado como compartido">☐</abbr>'
---

# Conceptos básicos

**Catálogo de servicios de Administración digital**: [Catálogo]({filename}../../otros/catalogo.md)
de la SGAD que difunde los servicios comunes, infraestructuras y otras soluciones
puestas a disposición de las AAPP. (ej: Cl@ve, Carpeta ciudadana)

**Declaración de servicios compartidos**: Declaración de la CETIC por la que
se definen cuales son servicios compartidos con carácter obligatorio, cuyo uso
(salvo excepciones) es obligatorio y sustitutivo respecto a los medios y servicios
particulares de las distintas unidades.
Actualmente son 14 y no todos están en producción aún.
(ej: Nube SARA, correo electrónico unificado)

Un servicio o medio pasa de simplemente común (que esta disponible para usar
si no quieres desarrollar tu propia solución) a ser declarado de uso compartido
(que es obligatorio usarlo en vez de desarrollar tu propia solución) cuando
respondan a necesidades transversales de un número significativo de unidades
administrativas.

# Principales servicios comunes

Todos son prestados por la SGAD, salvo SOROLLA2 que es prestado por la IGAE.

## Infraestructuras

### ☐ Red SARA

Conjunto de infraestructuras de comunicaciones y servicios básicos (DNS, NAT, NTP)
que permite transferencias seguras entre las AAPP.
Interconecta entre sí los distintos niveles de la Administración (estatal,
autonómica, local) y tiene enlace con la red europea, sTESTA.

Desde el Centro de Servicios Comunes de la Red SARA se ofrecen los servicios
comunes y compartidos cuyo mantenimiento es competencia de la actual SGAD.

A partir de 2017 se abre la puerta a que entidades privadas que den servicios de
administración electrónica en la nube a AAPP ubicada en al menos dos CCAA puedan
establecer un PdP en la Red SARA.

### ☑ Servicio Unificado de Telecomunicaciones

Red corporativa única, común y que dé servicio a todo el Sector Público Administrativo Estatal. El servicio
se diseñó en torno a cuatro áreas que constituyeron los cuatro lotes de su licitación:

* **Red corporativa multiservicio y servicio de telefonía fija**: incluye, entre otros, servicios de voz,
centralitas, transmisión de datos entre sedes y transmisión de datos basados en líneas especiales.
* **Comunicaciones móviles**: servicios móviles de voz y datos, mensajería masiva, mensajería móvil
corporativa y el sistema de gestión de la movilidad corporativa.
* **Internet**: conexión desde y hacia Internet de forma segura, con dos puntos de agregación y servicio de
detección, prevención y mitigación de ataques de denegación de servicio (DDoS), así como servicio de
nombres de dominio (DNS).
* **Red internacional**: red de interconexión con las sedes del extranjero. Transporte de voz y datos,
telefonía IP, cifrado de comunicaciones entre determinadas sedes, comunicaciones satelitales de
emergencia de voz y datos.

### ☑ Servicio de seguridad gestionada

Incluye equipamiento necesario, su configuración, puesta en marcha, mantenimiento
y gestión.

El SOC de la AGE proporciona, entre otros, los servicios de seguridad perimetral,
navegación segura, correo seguro, acceso remoto y auditorías de vulnerabilidades.
El proyecto está aún en fase de implementación.

### ☑ Servicio de Alojamiento de Infraestructuras TIC

Porporciona espacio físico acondicionado para albergar las infraestructuras TIC,
con una disponibiliad y nivel de servicio elevados, en un escenario de coste eficiente.

Este espacio se encuentra en **CPDs de referencia** gestionados por la SGAD
que soportan crecimientos modulares en espacio y potencia, tiene como nivel
aceptable el Tier III, pero esta preparado para una eventual evolución a Tier IV
si se requiere, además el nivel de PUE objetivo esta entre 1,4 y 1,6.
Estos CPDs de referencia proporcionan los siguientes servicios:

* Alojamiento granular, en unidades de rack, con opciones de jaula o sala privada
* Servicio de comunicaciones común para cada CPD
* Refrigeración redundante y escalable
* Alimentación eléctrica garantizada
* Seguridad física garantizada 24x7
* Control de presencia y monitorización
* Operación y soporte 24x7
* Espacios adicionales para almacenamiento de equipos, cintotecas, etc
* Tercer CPD en caso necesario

### ☑ Servicio de nube híbrida (nubeSARA)

Provisión de IaaS y PaaS tanto sobre los CPDs de referencia de la Administración
(nube privada) como de proveedores externos (nube pública).
Está en fase de implementación.

## Identidad y firma electrónica

### ☐ Cl@ve

Plataforma común para la identificación, autenticación y firma electrónica mediante
el uso de claves concertadas (ej: usuario y contraseña) y de certificados
electrónicos centralizados (ej: DNI-e).

Permite que las aplicaciones puedan definir el nivel de aseguramiento de
autenticación que desean y que el ciudadano usuario escoja entre los métodos
disponibles.

Cl@ve admite dos posibilidades de claves concertadas:

* Cl@ve ocasional (Cl@ve PIN): sistema de clave de un solo uso recibida por SMS.
* Cl@ve permanente: acceso mediante usuario y contraseña, reforzado con claves
de un solo uso por SMS. Este sistema permite acceso a la firma en la nube.

### ☐ Cl@ve Firma

Plataforma común para la firma criptográfica utilizando certificados
centralizados.

### ☑ @firma

Plataforma de validación y firma electrónica multi-PKI. Permite la validación de
certificados y firmas electrónicas, desacoplado de las aplicaciones.

Sirve para comprobar que el certificado utilizado por el ciudadano es un certificado
válido y que no ha sido revocado y que por tanto sigue teniendo plena validez para
identificar a su propietario.

Funciona con todos los certificados electrónicos cualificados (incluido el DNI-e).

Para facilitar la integración con el servicio se proporcionan la librería Integr@,
que también permiten firma en servidor.

Además de ofrecerse como servicio, está disponible como software para instalar por las
administraciones públicas (modelo federado), con utilidades como la generación y
validación de firmas electrónicas en múltiples formatos.

### ☐ FIRe

Simplifica el uso y realización de firmas electrónicas de usuario al concentrar
en un solo componente todos los requisitos de creación de firmas basadas
tanto en certificados locales como en certificados en la nube.

### ☐ TS@

Autoridad de Sellado de Tiempo que ofrece servicios de sellado, validación y
resellado de sellos de tiempo.

### ☐ VALIDE

Servicio online de validación de certificados, y verificación y generación de firmas
electrónicas.

### ☐ Cliente @firma

Herramienta de Firma Electrónica en entornos de usuario, se ejecuta en cliente,
para evitar que la clave privada asociada a un certificado tenga que salir del
contenedor del usuario (tarjeta, usbtoken o navegador) ubicado en su PC.

### ☐ Autentica

Ofrece servicios de autenticación, autorización y Single Sign On, de empleados
públicos en el acceso a aplicaciones internas de las AAPP.

### ☐ eIDAS

Proyecto europeo para el reconocimiento paneuropeo de las identidades electrónicas.
De este modo, los servicios de administración electrónica españoles pueden aceptar
identidades provinientes de otros EEMM y a su vez los servicios de otros países
puedan reconocer el DNI electrónico.

## Registro o representación del ciudadano ante las AAPP

### ☑ GEISER

Solución integral de registro para cualquier organismo público, prestada
en modo nube y que proporciona los servicios de Registro Electrónico, Registro Presencial,
Intercambio de Registros Internos y Externos (a través de SIR).
Cumple con la certificación SICRES3.

El servicio GEISER es de uso obligatorio para toda la AGE y sus OOPP, salvo
excepciones. En todos los casos, sin excepción, será obligatoria la integración
con el SIR. Para solicitar el servicio GEISER es necesario firmar un Convenio.

Sus principales características son:

* Uso en modo servicio (en la nube)
* Sólo requiere conexión a internet desde la Red SARA, certificado digital y escáner
* Posee su propio libro de registro por lo cual sirve tanto para el registro de los propios asientos
como los que están destinados hacia otras Administraciones (a través de la plataforma SIR)
* Dispone de servicios web que permiten utilizar la información de GEISER por otros sistemas o
aplicaciones
* Permite la distribución de los asientos registrales a las unidades de tramitación

### ☐ ORVE

Solución de registro completa que proporciona un servicio en la nube para
gestionar las Oficinas de Registro de entrada/salida de una Administración,
proporcionando su propio libro de registro.

Adicionalmente posibilita el intercambio de registros en formato electrónico
con otros organismos conectados a la plataforma SIR (cumple SICRES3).

Para solicitar el servicio ORVE es necesario firmar un Acuerdo de Adhesión.

### ☐ SIR

Infraestructura básica que permite el intercambio de asientos electrónicos de registro entre
las AAPP, independientemente de la aplicación de registro utilizada,
siempre que tenga certificación SICRES3.

### ☐ REC

Proporciona una vía de tramitación para todas aquellas solicitudes,
escritos y comunicaciones realizadas por el ciudadano o por empresas, y dirigidas hacia las
AAPP, que no se ajusten a procedimientos administrativos ya contemplados
en las Sedes electrónicas de las distintas Administraciones.

### ☐ APODERA

Permite la inscripción de poderes apud-acta otorgados presencial o telemáticamente, para hacer
constar y gestionar las representaciones que los interesados otorguen a un representante, con
el fin de que pueda actuar en su nombre ante la AAPP.

### ☐ Habilit@

Permite recoger a los funcionarios que se habiliten por parte de la Administración para actuar en
nombre de los ciudadanos que deseen actuar en procedimientos electrónicos de la AGE y que no
dispongan de firma electrónica.

### ☐ [Representa](https://administracionelectronica.gob.es/ctt/representa){.abbr}

Sirve de punto único para la validación de la habilitación de los profesionales
asociados a colectivos de representación de personas físicas o jurídicas.
Dicha representación y habilitación permite la tramitación de un procedimiento
administrativo en nombre del ciudadano.

## Atención al ciudadano

### ☐ [Punto de Acceso General](http://administracion.gob.es/){.abbr}

Facilita la relación de los ciudadanos con las AAPP al ser la puerta de entrada
vía internet a los servicios públicos.

### ☑ Red 060

Servicio Multicanal de Atención al Ciudadano que proporciona:

* una infraestructura de Red Inteligente capaz de absorber y atender consultas telefónicas de ciudadanos
* un conjunto de agentes que dan respuesta a las consultas que requieran un mayor grado de personalización

Las unidades adheridas pueden prestar el servicio de atención a los ciudadanos a través del
número único 060 o mantener un número de acceso directo durante un período de tiempo
delimitado en los casos que así se acuerde por las características del servicio.
La adscripción se realizará mediante Convenio/Acuerdo de Colaboración.

### ☐ Carpeta Ciudadana

Punto de Acceso General que permite a un ciudadano, sin necesidad de registrarte,
conocer sus expedientes que se tienen abiertos en los distintos organismos, sus asientos
registrales entre administraciones o sus datos en poder de la administración.

### ☐ FACE

Permite recibir en un solo punto todas las facturas electrónicas de la AGE,
distribuirlas a las plataformas de facturación, o gestionarlas para aquellos
Órganos Gestores que no dispongan de dichas aplicaciones, e informará a los
proveedores del estado de tramitación de dichas facturas.

Esto simplifica a los proveedores el envío de facturas, al centralizar en un
único punto todos los organismos y al unificar el formato de factura electrónica.

## Intercambio de información entre AAPP

### ☐ Plataforma de Intermediación de Datos (PID)

Aplicación horizontal que permite a una AP cedente poner datos a disposición de
otra AP cesionaria para su consulta.

La AP cesionaria podrá validar o consultar los datos necesarios en la tramitación de un
procedimiento, evitando al ciudadano aportar documentos que hayan sido generados
por cualquier Administración.

La plataforma de Intermediación ofrece servicios web de verificación y consulta
de datos bajo el protocolo SCSPv3.

## Sistemas de información trasversales

### ☐ SIA

Inventario actualizado de forma corresponsable por todos los Organismos participantes,
que contiene la relación de procedimientos y servicios de la AGE y las diferentes
AAPP participantes.

### ☐ DIR3

Inventario unificado y común a toda la Administración de las unidades orgánicas,
organismos públicos, sus oficinas asociadas y unidades de gestión económica-presupuestaria,
facilitando el mantenimiento distribuido y corresponsable de la información.

## Comunicación y notificaciones al ciudadanos

### ☑ NOTIFIC@

Plataforma para gestionar automáticamente todas las notificaciones y comunicaciones
que se generan en los organismos emisores.

La entrega se puede realizar por varias vías en función de las condiciones
establecidas por el destinatario:

* comparecencia electrónica en la Carpeta Ciudadana
* comparecencia en la Dirección Electrónica Habilitada (DEH) y/o en la sede electrónica del organismo emisor
* en soporte papel

### ☐ [Plataforma de Mensajería](https://administracionelectronica.gob.es/ctt/sim){.abbr} (SIM)

Sistema integral que permite a las aplicaciones incluir gestión de mensajes
en diferentes canales, correos electrónicos, sms, sin necesidad de tener en
cuenta las particularidades de cada canal o el proveedor que se utiliza.

## Expediente, documento y archivo electrónico

### ☑ InSiDe

Sistema para la gestión de documentos y expedientes electrónicos que cumple los
requisitos del ENI. Supone la gestión íntegramente electrónica de los documentos
del expediente, como paso previo al archivado definitivo de la documentación
en un formato interoperable y duradero.

InSiDe se presta en dos modos distintos, para su uso por parte de cualquier administración:

**InSide**: Permite almacenar o modificar documentos, expedientes electrónicos y sus metadatos
obligatorios asociados en cualquier gestor documental compatible con el estándar CMIS. También
es posible la asociación de documentos a expedientes, la gestión del índice, la validación y
visualización de los documentos y expedientes para su uso en papel, y la gestión de las firmas.

**G-Inside**: Servicios web en la nube SARA para validar y generar documentos y
expedientes en base al ENI, generación de documentos PDF de visualización del
documento y expediente electrónicos. G-Inside no almacena nada.

**Suite CSV**: Complemento a Inside que añade funcionalidades relacionadas con
la gestión de documentos electrónicos con CSV, como la generación, consulta o el
almacenamiento de documentos.

### ☑ ARCHIVE

Aplicación web de archivo definitivo que dispone de operaciones para trabajar con
expedientes y documentos electrónicos. Las operaciones principales son:

* Administración de un Archivo
* Gestión de Centros de Archivo
* Gestión de los Metadatos de las Normas Técnicas
* Gestión de Expedientes
* Transferencia de expedientes entre Archivos
* Generación de actas de cambio de custodia

## Apoyo a la tramitación administrativa

### ☐ PAGOS

Plataforma que facilita la implantación del pago telemático en las aplicaciones
que gestionan trámites que conlleven el pago de tasas, en los Organismos de la AGE.

## Utilidades para portales y servicios públicos

### ☐ PLATA

Plataforma de traducción de textos/documentos/htmls. Basada en motores de traducción
opensource (Moses, Apertium), permite la traducción automática de portales web a los idiomas
cooficiales y a inglés, francés o portugués a partir de textos en castellano.

### ☐ EGEO

Permite la creación de mapas interactivos para su presentación en portales web, cuadros de
mando y otras aplicaciones sin necesidad de conocimientos de georreferenciación ni desarrollos
adicionales. Dispone de un entorno para la gestión de dichos mapas basado en
parametrización y plantillas de datos con estructura simple (Excel, CSV o XML).

## Comunicación y mensajería

### ☑ Correo Electrónico Multidominio

Punto centralizado que da servicio de correo electrónico y agenda electrónica sin necesidad de
tener instalaciones in situ o contrataciones externas.

Incluye correo electrónico sobre clientes pesados (Outlook, Thunderbird, etc...),
correo web, correo sobre dispositivos móviles, sincronización de agendas,
listas de distribución, etc.

Al mismo tiempo permite la gestión descentralizada de los buzones de cada dominio
por parte de los Organismos adheridos.

### ☐ REÚNETE

Servicio de videoconferencia para todas las Administraciones Públicas.

### ☐ ALMACÉN

Aplicación web que permite enviar documentos de gran tamaño a uno o varios usuarios.

## Gestión de RRHH

### ☑ NEDAES

Permite realizar la gestión completa de nómina, incluyendo la elaboración
de toda la información de las fases de cálculo, contabilidad y pago según la
normativa en materia de retribuciones de los empleados públicos al servicio de la AGE.

### ☑ SIGP

Ofrece a los responsables y gestores de RRHH una herramienta que unifica
procedimientos y permite una gestión electrónica integrada de los expedientes.

Ofrece a los empleados públicos un punto de acceso único, para la generación, firma y entrega
de solicitudes y otras comunicaciones dirigidas a/o recibidas de los gestores de RRHH que las
tramitan.

A los jefes de unidad o personas designadas les ofrece la posibilidad de comunicación
con RRHH y con sus colaboradores.

El acceso a SIGP se lleva a cabo a través de FUNCIONA.

### ☐ FUNCIONA

Portal que provee de información y servicios de interés para todo el personal de
la AGE. Actualmente consta de un [portal de intranet](http://www.funciona.es)
y una [sede electrónica](https://sede.funciona.gob.es).

### ☐ TRAMA

Permite la tramitación electrónica de solicitudes de permisos e incidencias de los empleados
públicos, estableciendo un flujo de validación y aprobación para las solicitudes. También se
integra con el sistema de control horario (presencia) del organismo, u ofrece el suyo propio en
caso de que no exista, para poner a disposición de los empleados sus datos de fichajes, permisos
e incidencias.

## Gestión económica y presupuestaría

### ☑ SOROLLA2

Servicio de gestión económica presupuestaria orientado a facilitar la gestión económico-presupuestaria
que se realiza en los centros gestores del gasto de la AGE, sus OOAA y otros Entes Públicos.

Trata de favorecer la normalización de los procedimientos de gestión presupuestaria
y de propiciar una cultura de costes.

El objetivo del sistema es facilitar la gestión administrativa y contable de las dotaciones
presupuestarias a su cargo, sirviendo de registro y archivo de las operaciones (administrativas o
contables) realizadas, siendo el punto de información de la situación de cada una de las
actuaciones de gestión y proporcionando el avance de la situación económica de los créditos.

La IGAE proporciona servicio de hospedaje a las entidades que se adhieran al sistema SOROLLA2,
efectuándose el acceso bien a través de la red SARA o a través de Internet.

# ☑ Servicios compartidos

| Servicio | Ámbito | Responsable |
|:-|:-|:-|
| S. Unificado de<br/>Telecomunicaciones        | AGE y OOPP  | SGAD (dirección técnica, gestión y coordinación) |
| nubeSARA                                      |           ^ | SGAD y órganos proveedores de este servicio |
| S. de seguridad<br/>gestionada                | AGE y OOPP¹ | SGAD (dirección técnica, gestión y coordinación)<br/>Entidades adheridas (seguridad) |
| S. de Alojamiento de<br/>Infraestructuras TIC | AGE y OOPP² | SGAD y unidades proveedoras del servicio |
| Correo electrónico<br/>unificado              | AGE y OOPP³ | SGAD, aunque se contempla que en un futuro<br/>pueda compartir la prestación del servicio<br/>con otras unidades TIC |
| Red 060  |            ^ | SGAD (dirección técnica, gestión y coordinación)<br/>SG de Transparencia y Atención al Ciudadano (MPTAP) |
| GEISER   | AGE y OOPP⁴<br/>Todos los casos deben ser<br/>interoperables con el SIR | SGAD (dirección técnica, gestión y coordinación) |
| Notific@ | AGE y OOPP⁵ | SGAD (dirección técnica y coordinación)<br/>Gestión compartida entre<br/>SGAD (Notific@, DEH y Carpeta Ciudadana)<br/>AEAT (Centro de Impresión y Ensobrado) |
| @Firma   |           ^ | SGAD (dirección técnica, gestión y coordinación)<br/>Entidades con el modelo federado,<br/>previa aprobación de la SGAD, podrían actuar como<br/>prestadoras adicionales para otros organismos |
| InSiDe   |           ^ | SGAD (dirección técnica y coordinación) |
| ARCHIVE  |           ^ | SGAD (dirección técnica y coordinación)<br/>Gestión compartida entre<br/>SGAD (punto de vista técnico)<br/>y la unidad de Gestión de Documentación del MPTFP |
| NEDAES   | AGE y OOPP⁶ | SGAD (dirección técnica, gestión y coordinación)<br/>La SG de Organización y Procedimientos es responsable<br/>de la información obtenida del RCP |
| SIGP     |           ^ | ^ |
| SOROLLA2 | AGE y OOPP con<br/>presupuesto limitativo⁷| IGAE |

Previa autorización por el CE-CETIC:

1. excluidas aquellas unidades que cumpliendo el ENS, en lo relativo al
contenido de este servicio compartido, dispongan de soluciones propias ya
operativas que proporcionen similar o superior funcionalidad que el servicio compartido,
cuando justifiquen que la estructura de costes de su solución, los costes
de migración a la solución compartida y los requerimientos específicos y de integración
con su arquitectura aconsejen el mantenimiento de la solución específica.
2. excluido el alojamiento de las infraestructuras
cuyo propósito específico sean exclusivamente la Defensa Nacional y la
Seguridad del Estado, que hayan sido contratadas en el ámbito objetivo de aplicación
de la Ley 24/2011
3. excluidas aquellas unidades que hayan realizado
una gran inversión para proporcionar el servicio con probada eficiencia
económica y tecnológica, y para las cuales la migración al servicio compartido
resulte antieconómica
4. excluidas aquellas unidades que dispongan de
soluciones de registro específicas operativas y proporcionen las funcionalidades
equivalentes o superiores a las del servicio compartido, cuando justifiquen que
la estructura de costes de su solución, los costes de migración a la solución
compartida y los requerimientos específicos y de integración con su arquitectura
aconsejan el mantenimiento de la solución específica, así como cuando se
evidencien razones de incapacidad del servicio común de implementar funcionalidades
específicas que se identifiquen como imprescindibles para la Gestión del
Organismo.
En cualquier caso deberán ser interoperables con el SIR.
5. excluidas aquellas unidades que dispongan de soluciones propias
ya operativas que proporcionen similar o superior funcionalidad que el servicio
compartido, cuando justifiquen que la estructura de costes de su solución, los
costes de migración a la solución compartida y los requerimientos específicos y de
integración con su arquitectura aconsejen el mantenimiento de la solución específica.
6. excluidos organismos atendiendo exclusivamente
a razones de incapacidad del servicio común de implementar funcionalidades
específicas que se identifiquen como imprescindibles para la gestión de la entidad
7. excluidos aquellos centros gestores y organismos
que dispongan de soluciones propias o contratadas de gestión económico-presupuestaria,
cuando justifiquen que la estructura de costes de su solución, los costes de migración
a la solución compartida y los requerimientos específicos y de integración con su
arquitectura aconsejan el mantenimiento de la solución específica, así como cuando
se evidencien razones de incapacidad del servicio común de implementar funcionalidades
específicas que se identifiquen como imprescindibles para la gestión de la entidad.
También se podrá utilizar una solución propia o contratada mientras el órgano
responsable de la provisión del servicio no pueda atender a su implantación.

# Bibliografía

* PreparaTic27 - Pack1/049
