---
title: Esquema Nacional de Interoperabilidad (ENI)
status: draft
---

# Conceptos básicos

**ENI**: establece los principios y directrices de interoperabilidad en el
intercambio y conservación de la información electrónica por parte de
las AAPP (Real Decreto 4/2010, de 8 de enero).

**NTI**: concretan detalles para facilitar los aspectos más prácticos y
operativos de la interoperabilidad entre las AAPP y con el ciudadano.

**EIF**: Marco Europeo de Interoperabilidad, cuyas recomendaciones sobre
interoperabilidad fueron tenidas en cuenta para la elaboración del ENI y sus NTI.

**Modelo de datos**: conjunto de definiciones (nivel conceptual),
interrelaciones (nivel lógico), y reglas y convenciones (nivel físico)
que permiten describir los datos para su intercambio.

# Ojetivos

* Establecer los **criterios y recomendaciones** que deben seguir las AAPP
para garantizar la interoperabilidad y la no discriminación de los ciudadanos
por razón de su elección tecnológica.
* Proporcionar los **elementos comunes** para facilitar la interacción de las AAPP,
y comunicar los requisitos de interoperabilidad a la industria.
* Facilitar la **implantación de políticas de seguridad**, contribuyendo a una
favoreciendo racionalidad técnica y economía de escala.

La interoperabilidad se concibe, al igual que la seguridad, desde una perspectiva integral.

# Elementos

* **Principios básicos de interoperabilidad**: La interoperabilidad:
    * como cualidad integral presente desde la concepción y
    a lo largo de todo el ciclo de vida.
    * con carácter multidimensional (organizativo, semántico y técnico)
    * con enfoque de soluciones multilaterales para obtener las ventajas derivadas
    del escalado, de las arquitecturas modulares y multiplataforma y de compartir,
    reutilizar y colaborar
* **Interoperabilidad organizativa**:
    * establecer y publicar las condiciones para el consumo de servicios puestos
    a disposición del resto de entidades
    * ofrecer servicios a través de la **Red SARA**
    * mantener inventario de procedimientos y servicios
    * mantener relación actualizada de los órganos administrativos,
    oficinas de registro y atención al ciudadanos, y las relaciones entre ellos
* **Interoperabilidad semántica**: Identificar, inventariar y publicar
**modelos de datos** con carácter común (CISE)
* **Interoperabilidad técnica**: Uso de **estándares abiertos** y, de forma
complementaría, estándares de uso generalizado con respecto a:
    * documentos y expedientes electrónicos puestos a disposición o requeridos del ciudadano
    * aplicaciones y servicios en su relación con el ciudadano y otras entidades (ej: sede electrónica)
* **Infraestructuras y servicios comunes**:
    * enlazar infraestructuras y servicios de las AAPP con las infraestructuras
    y servicios comunes de la AGE
    * intercambio de asientos registrales a través de **ORVE** y **SIR**
* **Utilización, preferentemente, de la Red SARA**:
    * conectar la red de la entidad a la Red SARA
    * aplicar el Plan de Direccionamiento de la Administración
    * sincronizar las aplicaciones y servicios con la hora oficial a través
    del Real Instituto y Observatorio de la Armada o los servicios de la Red SARA
* **Reutilización** y transferencia de tecnología:
    * licenciar como **EUPL** (o equivalente) las aplicaciones susceptibles de ser reutilizadas
    * inventariar en el **CTT** las aplicaciones para su libre reutilización
    * reutilizar las soluciones ya disponibles en el CTT
    * publicar el código fuente con licencias de libre reutilización
* **Interoperabilidad de la firma electrónica y de los certificados**:
adopción de la política de firma electrónica y de certificados de la AGE
o uso de esta como referencia para elaborar la propia. Rige aspectos relativos a:
    * validación de certificados y firmas electrónicas
    * listas de confianza
    * aplicaciones usuarias
    * prestadores de servicios de certificación (TSL)
    * plataformas de validación de certificados y firma electrónica (ej @firma)
* **Recuperación y conservación del documento electrónico**:
    * definir y publicar la **PGDE**
    * definir los calendarios de conservación de los documentos y expedientes
    * definir normativa interna en cuanto a la generación de copias autenticas
    * definir el esquema institucional de metadatos
    * cumplir el ENS, el RGPD y el LOPD-GDD
    * utilizar preferentemente firmas longevas
    * digitalizar los documentos en soporte papel

# Las NTI

El ENI establece la serie de NTI que son de obligado cumplimiento por las AAPP
que desarrollan aspectos concretos de la interoperabilidad entre las AAPP
y con los ciudadanos.

## Catálogo de estándares

## Documento electrónico

Esta NTI recoge los requisitos mínimos sobre la estructura y formato de los
documentos para su intercambio y por tanto para la interoperabilidad.

**Objetivo**: describir los componentes del documento electrónico, contenido,
en su caso, firma electrónica y metadatos, así como la estructura y formato
para su intercambio.

**Ámbito**: documentos administrativos electrónicos y documentos susceptibles
de formar parte de un eExpediente. Ej:

* Documentos de decisión: resoluciones, acuerdos, contratos, convenios y declaraciones
* Documentos de transmisión: comunicaciones, notificaciones, publicaciones y acuses de recibo
* Documentos de constancia: actas, certificados y diligencias
* Documentos de juicio: informes
* Documentos de ciudadano: solicitudes, denuncias, alegaciones, recursos,
comunicaciones, facturas y otros incautados
* Otros: documentos de organizaciones / ciudadanos objeto de intercambio

Un eDoc puede estar formado por varios ficheros (ej: fichero de texto + fichero
de imagen), varias firmas asociadas y varios conjuntos de metadatos vinculados a
cada fichero individual, pero a efectos de tratamiento, gestión y conservación
constituye un único objeto electrónico.

El eDoc debe tener sentido completo y ser susceptible de identificación
y tratamiento diferenciado, y constituya evidencia de acciones.

**Componentes** del eDoc:

* Contenido: conjunto de datos del documento.
* Firma electrónica: permite detectar cambios posteriores a la firma y esta
vinculada de forma única al firmante y a los datos. todos los documentos
susceptibles de estar en un eExpediente deben tener al menos una firma, cuyo
tipo puede ser un CSV o una firma basada en certificados (base64).
* Metadatos: proporciona contexto (propiedades relativas a la gestión/conservación
de los documentos) y da caracter probatorio del eDoc en el tiempo.
El NTI no especifica la implementación pero si sus condiciones de intercambio y
reproducción.

**Metadato de gestión** de documentos: Información estructurada o semiestructurada
que hace posible la creación, gestión y uso de documentos a lo largo del tiempo.
Sirven para identificar, autenticar y contextualizar documentos, y a las personas,
los procesos y los sistemas que los crean, gestionan, mantienen y utilizan.

**Metadatos mínimos obligatorios**:

* Versión NTI: http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e
* Identificador: ES_ORGNAO_AAAA_IDespecífico (ej: ES_E00010207_2010_MPR000000000000000000000010207)
* Fecha de captura: YYYY-MM-DDTHH:MM:SS (ISO 8601)
* Origen: 0 = Ciudadano, 1 = Administración
* Estado de elaboración:
    * Original (Ley 11/2007 Art. 30)
    * Copia electrónica auténtica con cambio de formato (Ley 11/2007 Art. 30.1)
    * Copia electrónica auténtica de documento papel (Ley 11/2007 Art. 30.2 y 30.3)
    * Copia electrónica parcial auténtica
    * Otros
* Nombre de formato: Formato lógico del fichero de contenido del documento electrónico
(ha de ser uno de los listados en la NTI de Catálogo de estándares)
* Tipo documental:
    * Documentos de decisión:
        * Resolución
        * Acuerdo
        * Contrato
        * Convenio
        * Declaración
    * Documentos de transmisión:
        * Comunicación
        * Notificación
        * Publicación
        * Acuse de recibo
    * Documentos de constancia:
        * Acta
        * Certificado
        * Diligencia
    * Documentos de juicio:
        * Informe
    * Documentos de ciudadano:
        * Solicitud
        * Denuncia
        * Alegación
        * Recursos
        * Comunicación ciudadano
        * Factura
        * Otros incautados
    * Otros
* Tipo de firma: CSV o alguno de los formatos de firma electrónica listados en
la NTI de Política de firma y certificados de la Administración:
* Si *Tipo firma* = CSV:
    * Valor CSV
    * Definición generación CSV: Referencia a la Orden, Resolución o documento
    que define la creación del CSV correspondiente (ej: BOE-A-YYY-XXXXX)
* Si *Estado de elaboración* = *Copia electrónica auténtica con cambio de formato (Ley 11/2007 Art.30.1)*
o *Copia electrónica parcial auténtica*:
    * Identificador de documento de origen: ES_ORGNAO_AAAA_IDespecífico

**Intercambio de eDocs**: salvo acuerdo excepcional entre las AAPP, a estructura
consiste en un XML con los tres componentes: contenido (normalmente en base64),
metadatos y firma. Preferentemente se usar la Red Sara como medio de transmisión.
Si el eDoc forma parte de un asiento registral éste será tratado como un
documento adjunto al mensaje de datos de intercambio.

**Acceso a eDocs** en eSedes debe mostrar:

* El contenido del documento electrónico cuando éste sea representable
* La información básica de cada una de las firmas del documento
* Descripción y valor de los metadatos mínimos obligatorios

## Digitalización de documentos

**Objetivo**: establecer los requisitos a cumplir en la digitalización de
documentos no electrónicos (ej: papel) a través de medios fotoeléctricos.

**Ambito** cualquier órgano de la AP o Entidad de Derecho Público vinculada
o dependiente de aquélla sobre cualquier documento en soporte papel u otro
soporte susceptible de digitalización, independientemente de que hubiese sido
aportado por el ciudadano o generado por una organización.

Un **eDoc digitalizado esta compuesto** por:

* imagen electrónica
* metadatos mínimos obligatorios en la NTI de Documento electrónico, siendo
el metadato *Estado de elaboración* = *Copia electrónica autentica con cambio de formato*
* metadatos opcionales de la NTI de Política de gestión de eDocs (ej: resolución,
tamaño, idioma)
* si procede, firma de la imagen electrónica (eSello o CSV)

**Requisitos de la imagen electrónica**:

* Usar uno de los formatos del NTI de Catálogo de estandares (JPEG, PNG, TIFF, SVG, PDF o PDF/A)
* El nivel de **resolución** mínimo para imágenes electrónicas será de
**200 píxeles por pulgada**, tanto en blanco y negro, color o escala de grises
* La imagen será **fiel al documento** origen (respetará la geometría del original
en tamaños y proporciones y no contendrá caracteres o gráficos que no figurasen
en el original)

**Proceso de digitalización**: Conlleva las siguientes tareas:

1. Digitalización por medio fotoeléctrico
2. Si procede, optimización automática de la imagen electrónica para garantizar
su legibilidad (ej: umbralización, reorientación, eliminación de bordes negros)
3. Asignación de los metadatos
4. Si procede, firma de la imagen electrónica

Si se realiza el último paso se obtendrá un *eDoc completamente conformado*,
en caso contrarío sera un *eDoc pendiente de completar*.

En cuanto a la destrucción de originales tras la digitalización hay que cumplir
con el **Real Decreto 1164/2002**:
La eliminación de documentos sólo podrá llevarse a cabo tras una valoración
documental por parte de la Comisión Superior Calificadora de Documentos Administrativos,
que acredite que los documentos originales no poseen valor histórico o artístico,
ni utilidad para la gestión administrativa que exija su conservación.
Además, los documentos originales cuya eliminación se propone deberán carecer de
valor probatorio para los derechos y obligaciones de las personas físicas o jurídicas.

## Expediente electrónico

## Política de firma electrónica y de certificados de la Administración

## Protocolos de intermediación de datos

## Relación de modelos de datos

## Política de gestión de documentos electrónicos

## Requisitos de conexión a la Red de comunicaciones de las Administraciones Públicas españolas

## Procedimientos de copiado auténtico y conversión entre documentos electrónicos, así como desde papel u otros medios físicos a formatos electrónicos

**Objetivo**: establecer las reglas para la generación de copias electrónicas
auténticas, copias papel auténticas de documentos públicos administrativos
electrónicos y para la conversión de formato de documentos electrónicos.

## Modelo de Datos para el intercambio de asientos entre las Entidades Registrales

## Reutilización de recursos de información

## Reutilización y transferencia de tecnología

## Declaración de conformidad con el Esquema Nacional de Interoperabilidad

## URL´s de esquemas XML



---

Bibliografía:

* PreparaTic27 - Pack1/045
* PreparaTic27 - Pack1/046
* [administracionelectronica.gob.es - ENI](https://administracionelectronica.gob.es/ctt/eni)
* [administracionelectronica.gob.es - Interoperabilidad](https://administracionelectronica.gob.es/pae_Home/pae_Estrategias/pae_Interoperabilidad_Inicio.html)
