---
title: Identidad y firma electrónica. Reglamento eIDAS. DNI electrónico
Status: draft
---

# Conceptos básicos

**Firma electrónica** (concepto jurídico): Conjunto de datos en forma electrónica,
consignados junto a otros o asociados con ellos,
que pueden ser utilizados como medio de identificación del firmante.

**Firma digital** (concepto tecnológico): Valor o conjunto de caracteres,
calculado criptográficamente a partir de unos datos,
que permiten verificar la integridad, autenticidad y no repudio de dichos datos,
denominados como *mensaje*.

**Certificado de firma electrónica**: declaración electrónica que vincula
los datos de validación de una firma con una persona física y confirma,
al menos, el nombre o seudónimo de esa persona

**Sello de electrónico**: Datos en formato electrónico anejos a otros datos,
o asociados de manera lógica con ellos, para garantizar el origen y
la integridad de estos últimos.

**Sello de tiempo electrónico**: Sello electrónico que vincula unos datos a un
instante concreto, aportando la prueba de que estos datos existían en ese instante.
Una firma que incluye un sello de tiempo con el resultado de la validación del
certificado es una **firma longeva**, siendo esta longevidad determinada
por el sellado y por lo tanto requerirá resellado antes de que caduque
el certificado que se usó para el sello de tiempo.

**Certificado de autenticación de sitio web**: declaración que autentica
un sitio web y lo vincula a la persona física o jurídica a quien se
ha expedido el certificado

# Conceptos eIDAS

Del cumplimiento del **eIDAS** (reglamento UE 910/2014) se derivan las siguientes
definiciones:

**Firma avanzada**: firma electrónica que cumple los requisitos:

* estar vinculada al firmante de manera única
* permitir la identificación del firmante
* haber sido creada utilizando datos de creación de la firma electrónica que el firmante puede utilizar,
con un alto nivel de confianza, bajo su control exclusivo
* estar vinculada con los datos firmados por la misma de modo tal que cualquier modificación ulterior
de los mismos sea detectable

**Firma electrónica cualificada**: firma electrónica avanzada que se crea
mediante un dispositivo cualificado de creación de firmas electrónicas
y que se basa en un certificado cualificado de firma electrónica.
A efectos jurídicos este tipo de firma:

* tendrá un efecto equivalente al de una firma manuscrita
* y si además esta basada en un certificado cualificado emitido en un estado
miembro será reconocida como una firma electrónica cualificada
en todos los demás Estados miembros.

**Dispositivo cualificado de creación de firma electrónica**:
dispositivo de creación de firmas electrónicas que cumple los requisitos:

* estar garantizada razonablemente la confidencialidad de los datos de creación
de firma electrónica utilizados para la creación de firmas electrónicas
* los datos de creación de firma electrónica utilizados para la creación de
firma electrónica solo puedan aparecer una vez en la práctica
* existe la seguridad razonable de que los datos de creación de firma electrónica utilizados para la
creación de firma electrónica no pueden ser hallados por deducción y de que la firma está protegida
con seguridad contra la falsificación mediante la tecnología disponible en el momento
* los datos de creación de la firma electrónica utilizados para la creación de firma electrónica puedan
ser protegidos por el firmante legítimo de forma fiable frente a su utilización por otros

**Certificado cualificado de firma electrónica**: certificado de firma electrónica
que ha sido expedido por un prestador cualificado de servicios de confianza
y que cumple, entre otros, los requisitos siguientes:

* Indicar si ha sido expedido como certificado cualificado
* Indicar si los datos de validación se encuentran en un dispositivo cualificado
de firma.
* Contener el nombre del firmante o, en su caso, un seudónimo claramente establecido como tal

**Sello cualificado de tiempo electrónico**:
Sello electrónico avanzado que cumple con los siguientes requisitos:

* Vincular la fecha y hora con los datos de forma que se elimine
la posibilidad de modificar los datos sin que se detecte.
* Basarse en una fuente de información temporal vinculada al Tiempo Universal Coordinado.
* Haber sido firmada mediante el uso de firma electrónica avanzada o sellada
con un sello electrónico avanzado del prestador cualificado de servicios de
confianza o por cualquier método equivalente.

Un **certificado cualificado de sello electrónico** debe contener al menos,
el nombre del creador y, cuando proceda, su número de registro oficial.

**Certificado cualificado de autenticación de sitio web**: Certificado de
autenticación de sitio web que cumple con los siguientes requisitos:

* se expide a una persona física o jurídica, identificada en el propio certificado
* deberá aparecer al menos su ciudad y estado
* contiene el/los nombre/s de dominio explotados por la persona física o
jurídica a la que se expida el certificado

**Lista de servicios de confianza TSL**: Lista de prestadores de
servicios de certificación que expiden certificados cualificados.
Cada EEMM de la UE debe publicar y mantener su lista de Confianza de sus PSC
supervisados y acreditados.

Los tipos de firma exigidos por el sector público son, de menor a mayor
nivel de garantía:

1. firma electrónica avanzada
2. firma electrónica avanzada basada en un certificado cualificada de firma electrónica
3. firma electrónica cualificada

Siendo normalmente exigido el nivel 1 o 2, y siempre aceptándose cualquier
certificado de nivel superior al exigido pero nunca exigiendo una firma
superior a la cualificada.

En la decisión de ejecución UE 910/2014 se establece que los formatos de firmas
electrónicas avanzadas y sellos avanzados que deben reconocer el sector público
son XAdES, CAdES o PAdES en niveles de conformidad B, T o LT (XL), y los
contenedores ASiC.

Adicionalmente, los sistemas de **clave concertada** se aceptan como sistema de
identificación en el Art. 9 de la Ley 39/2015 y se basan en el registro previo del usuario,
durante el cual se acuerda una clave a usar con el proveedor y que garantiza la
identidad del usuario, sin ser necesario un certificado electrónico.  
Un ejemplo sería Cl@ve Permanente o cualquier otro sistema de usuario-contraseña.

En la resolución de 14 de julio de 2017 de la SGAD se establece que el uso de
firma electrónica no criptográfica ha de garantizar igualmente la autenticidad,
integridad y no repudio cumpliendo lo siguiente:

* Utilizar un sello electrónico cualificado del organismo que incluya un sello
de tiempo
* Garantizar la autenticidad del firmante vía Cl@ve
* Recoger evidencias para la verificación de identidad. Dichas evidencias también
han de sellarse
* Devolver un justificante CSV verificable en sede
* Incluir un campo check para que el interesado exprese consentimiento y voluntad
de firma

# Ampliación de conceptos tecnológicos

## Clave pública/privada y tercero de confianza

* **Clave privada**: Parte que se utiliza para firmar y no se debe compartir
* **Clave pública**: Parte que se comparte para que el receptor pueda desencriptar
y verificar que el emisor posee la clave privada.
* **Tercero de confianza**: Actor externo que acredita que la clave realmente
es de quien dice ser.

Pasos para realizar una firma y verificarla en el receptor:

1. Se calcula el hash del mensaje
2. Se encripta el hash del mensaje con la clave privada del emisor (esta es la firma)
3. Se envían al receptor el documento junto con la firma
4. En el receptor, se calcula de nuevo el hash del mensaje original
5. Se utiliza la clave pública del emisor para desencriptar la firma
6. Se compara el hash calculado con el desencriptado,
si coinciden se ha mantenido la integridad y se garantiza el no repudio

## Certificado digital

El certificado digital es un documento electrónico, expedido y firmado
por una tercera parte de confianza (AC), que vincula una clave pública
con la identidad del propietario de la clave privada complementaria.

**X.509 v3** (o PKIX) es el estándar de la ITU-T (adoptado por la IETF, RFC5280)
para infraestructuras de clave pública.
Especifica la estructura y formato de los certificados digitales de clave pública,
de las listas de revocación de certificados (CRL) y de los certificados de atributos.

Su sintaxis se define en lenguaje ASN.1 y tiene la siguiente estructura:

* Version
* Serial number: identificador del certificado, único para cada CA.
* Signature algorithm: algoritmo empleado por la CA para firmar el certificado
* Issuer: nombre de la tercera parte de confianza (CA) que lo expide
* Validity period: periodo de validez de las claves (desde - hasta)
* Subject: sujeto titular vinculado a la clave pública (en notación DN)
* Subject Public Key Information: clave pública y algoritmo usado para
crearla (lo que la ley incluye en los "datos de verificación de firma")
* Campos opcionales:
    * Issuer unique identifier: Permite reutilizar nombres de emisor
    * Subject unique identifier: Permite reutilizar nombres de sujeto
* Extensions: Permiten asociar información adicional a sujetos, claves públicas, etc
y se componen de tres partes:
    * Extensión ID: Identificador que proporciona la semántica y el tipo de información (texto, fecha, etc) del valor de la extensión
    * Critical: flag que indica si es seguro o no ignorar el campo de extensión si no se reconoce el tipo
    * Value: valor de la extensión
* Ejemplos de extensiones:
    * Subject Alternative Name (SAN): identidades adicionales, seudónimos
    * Authority Information Access: enlaces al servidor OCSP de la VA
    * CRL distribution points (CDP) y Freshest CRL (Delta CRL dist. point):
    enlaces a las CRL y a la Delta-CRL
    * Key Usage: Restringe el propósito de la clave pública certificada, indicando, por ejemplo,
        * digitalSignature: uso para autenticación
        * nonRepudiation / ContentCommitment: uso para firma digital
        * keyCertSign: para certificados de CA
* Issuer digital signature: firma de la tercera parte de confianza (autofirmado)

### Validación de firma con certificado

La validación de una firma con certificado conlleva a su vez
la validación del certificado, para ello hay que comprobar:

* Los limites de su uso (Key Usage)
* El periodo de validez (Validity period)
* El estado de vigencia del certificado, pues puede estar revocado o temporalmente
suspendido antes de vencer el periodo de validez

Para comprobar este último punto hay dos tecnicas diferentes:

**CLR**: Listas mantenidas por las CAs donde aparecen los número de serie
de los certificados revocados antes de expirar y la fecha de revocación.
Se acceden a ellas a través de repositorios HTTP o LDAP cuya ubicación
esta indicada en la extensión CDP del certificado.

Para mitigar el que supone el crecimiento de la CRL se emplean los delta-CRL
(extensión Freshest CRL) que solo contienen los certificados revocados desde
la publicación de la última CRL de base.

**OCSP**: Protocolo que permite consultar a una VA el estado de un certificado.
Usa mensajes codificados en ASN.1 y se envían sobre HTTP. Las respuestas pueden
ser *good*, *unknown* o *revocked* y van firmadas y con sello de tiempo.

Consultar directamente a las CAs, vía OCSP, conlleva problemas de rendimiento
tanto para la CA como para el cliente. Como solución a esto se usa OCSP Stapling,
una técnica por la que el propio servidor web (que esta visitando el cliente)
consulta el servido OCSP periódicamente de manera que cuando un cliente
va a hacer el [TLS/SSL handshake](https://es.wikipedia.org/wiki/Seguridad_de_la_capa_de_transporte#Handshake_TLS) con él puede adjuntar (grapa)
las respuestas del OCSP en ese mismo proceso.

## Sello de tiempo y firma longeva

El sello de tiempo soluciona el problema de dar un falso negativo al validar unos datos
que fueron firmados con un certificado que era valido cuando se uso pero que
ahora (cuando se esta validadando) se encuentra revocado.

Una **firma longeva**, al incluir el resultado de la validación del
certificado, soluciona el problema de que los PSCs eliminen los certificados
de las CRLs una vez que el certificado ha caducado, lo que impedía saber después
de su fecha de caducidad si alguna vez fueron revocados y cuando.

## Formatos de firma (hash y cifrado asimétrico)

La terminación AdES denota que es una firma electrónica avanzada.

* PKCS#7 / CMS: Permite diferentes tipos de objetos (data, signed-data, enveloped-data, signed-and-enveloped-data, digested-data y encrypted-data)
* CAdES: Permite tanto attached signature, como detached signature.
* XMLDsig:
    * Define una sintaxis XML para soporte a la firma digital.
    * Permite firmar cualquier tipo de recurso, no solo XML.
    * Existen varios modos: detached signature, enveloped signature y enveloping signature.
* PAdES (PDF Advanced Electronic Signature)
* S/MIME (Secure / Multipurpose Internet Mail Extensions)
* ASiC (Associated Signature Container)
    * Define una estructura de contenedor para englobar: archivo, firma y sello de tiempo
    * El contenedor está basado en zip

CAdES y XAdES son respectivamente versiones AdES de CMS y XMLDsig
que permiten los siguientes perfiles:

* BES (Basic Electronic Signature): firma con un formato básico, incluyendo los atributos necesarios para la firma electrónica
* EPES (Explicit Policy Electronic Signature): firma el documento incorporando el identificador de la política de firma a aplicar (por ejemplo: política de firma de la AGE v1.9 urn:oid:2.16.724.1.3.1.1.2.1.9)
* T (Timestamped): añade un sello de tiempo sobre cualquiera de las anteriores.
* C (Complete): añade referencias a datos de verificación (certificados y listas de revocación).
* X (Extended): añade un sello de tiempo a C (Complete) para proteger contra el posible compromiso de validez en el futuro.
* XL (eXtended Long-term): añade certificados y evidencias de revocación (ej. CRL o respuestas OCSP), para permitir la verificación en el futuro, incluso si su fuente original no estuviera disponible.
Esto implementa la *firma longeva*.
* A (Archival): añade sellos de tiempo posteriores periódicamente (re-sellado) para prevenir el compromiso causado por la debilidad de los algoritmos de firma con el tiempo.


<fieldset class="firma_ades">
  <legend>A</legend><div>
<fieldset>
  <legend>X-L</legend><div>
<fieldset>
  <legend>X</legend><div>
<fieldset>
  <legend>C</legend><div>
<fieldset>
  <legend>T</legend><div>
<fieldset class="firma_ades_leaf">
  <legend>BES</legend>
  <p>Signed info</p>
  <p>Signature</p>
  <p>Key info</p>
  <p>Signed properties</p>
  <p>Unsigned properties</p>
</fieldset>
  <p>Sellado de tiempo sobre la firma electrónica</p>
</div></fieldset>
  <p>Referencias a las listas de revocación y a los certificados</p>
</div></fieldset>
  <p>Sellado de tiempo sobre las referencias a los certificados y las listas de revocación</p>
</div></fieldset>
  <p>Certificados y listas de revocación</p>
</div></fieldset>
  <p>Secuencia de sellados de tiempo</p>
</div></fieldset>

# Servicios comunes para firma electrónica

**Suite @firma**, la cual se copone de:

* Plataforma @firma: permite la validación de certificados digitales mediante
llamadas a WS
* VALIDe: permite la validación manual de firmas, certificados, y visualizar y
realizar firmas
* TS@: permite realizar sellados y resellados de tiempo (firma longeva)
* Cliente @firma (Autofirma): permite la realización firmas en el cliente
* Cl@ve firma: permite la realización de firmas con certificado electrónico en la nube
* Integr@: facilita la integración con @firma y la realización de firma en
servidor (sello del organismo) para entornos Java

**FIRe**: solución que simplifica el uso y realización de
firmas electrónicas de usuario al concentrar en un solo
componente todos los requisitos de creación de firmas
basadas tanto en certificados locales como en certificados en
la nube.

![Descripción Técnica de FIRe](https://administracionelectronica.gob.es/ctt/resources/Soluciones/2331/Info%20Adicional/Imagen/Arquitectura%20FIRe.jpg)

---

Bibliografía:

* PreparaTic27 - Pack1/080
* [www.uv.es - Introducción a los certificados digitales](https://www.uv.es/sto/articulos/BEI-2003-11/certificados_digitales.html)
* [mozilla.org - OCSP Stapling in Firefox](https://blog.mozilla.org/security/2013/07/29/ocsp-stapling-in-firefox/)
* [wikipedia.org - OCSP stapling](https://en.wikipedia.org/wiki/OCSP_stapling)
* [blog.signaturit.com - Firma electrónica avanzada, simple o cualificada, ¿sabes distinguirlas?](https://blog.signaturit.com/es/firma-electronica-simple-vs-avanzada)
* [mineco.gob.es - FAQ Reglamento (UE) Nº 910/2014 y eIDAS](https://avancedigital.mineco.gob.es/es-es/Servicios/FirmaElectronica/Paginas/preguntas-frecuentes.aspx)
* [Cl@ve - definiciones](https://clave.gob.es/clave_Home/dnin/definiciones.html)
