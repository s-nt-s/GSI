---
title: Identidad y firma electrónica. Reglamento eIDAS. DNI electrónico
Status: draft
---

# Identidad y firma electrónica

**Firma electrónica** (concepto jurídico): Conjunto de datos en forma electrónica,
consignados junto a otros o asociados con ellos,
que pueden ser utilizados como medio de identificación del firmante.

**Firma digital** (concepto tecnológico): Valor o conjunto de caracteres,
calculado criptográficamente a partir de unos datos,
que permiten verificar la integridad, autenticidad y no repudio de dichos datos,
denominados como *mensaje*.

Pasos para realizar una firma y verificarla en el receptor:

1. Se calcula el hash del mensaje
2. Se encripta el hash del mensaje con la clave privada del emisor (esta es la firma)
3. Se envían al receptor el documento junto con la firma
4. En el receptor, se calcula de nuevo el hash del mensaje original
5. Se utiliza la clave pública del emisor para desencriptar la firma
6. Se compara el hash calculado con el desencriptado,
si coinciden se ha mantenido la integridad y se garantiza el no repudio

## Clave pública/privada, tercero de confianza y clave concertada

* **Clave privada**: Parte que se utiliza para firmar y no se debe compartir
* **Clave pública**: Parte que se comparte para que el receptor pueda desencriptar
y verificar que el emisor posee la clave privada.
* **Tercero de confianza**: Actor externo que acredita que la clave realmente
es de quien dice ser.

Adicionalmente, los sistemas de **clave concertada** se aceptan como sistema de
identificación en el Art. 9 de la Ley 39/2015 y se basan en el registro previo del usuario,
durante el cual se acuerda una clave a usar con el proveedor y que garantiza la
identidad del usuario, sin ser necesario un certificado electrónico.  
Un ejemplo sería Cl@ve Permanente o cualquier otro sistema de usuario-contraseña

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

## Sello de tiempo

En sello de tiempo vincula unos datos a un instante concreto, aportando la prueba
de que estos datos existían en ese instante.

Esto soluciona el problema de dar un falso negativo al validar unos datos
que fueron firmados con un certificado que era valido cuando se uso pero que
ahora (cuando se esta validadando) se encuentra revocado.

Una firma que incluye un sello de tiempo con el resultado de la validación del
certificado es una **firma longeva**, siendo esta longevidad determinada
por el sellado y por lo tanto requerirá resellado antes de que caduque
el certificado que se usó para el sello de tiempo.

## Formatos de firma (hash y cifrado asimétrico)

* PKCS#7 / CMS: Permite diferentes tipos de objetos (data, signed-data, enveloped-data, signed-and-enveloped- data, digested-data y encrypted-data)
* CAdES: Permite tanto attached signature, como detached signature. Define diferentes perfiles para firma electrónica avanzada:
    * CAdES-BES (Basic Electronic Signature): firma con un formato básico, incluyendo los atributos necesarios para la firma electrónica
    * CAdES-EPES (Explicit Policy Electronic Signature): firma el documento incorporando el identificador de la política de firma a aplicar (por ejemplo: política de firma de la AGE v1.9 urn:oid:2.16.724.1.3.1.1.2.1.9)
    * CAdES-T (Timestamped): añade un sello de tiempo sobre cualquiera de las anteriores.
    * CAdES-C (Complete): añade referencias a datos de verificación (certificados y listas de revocación).
    * CAdES-X (Extended): añade un sello de tiempo a CAdES-C para proteger contra el posible compromiso de validez en el futuro. Sello de tiempo a la validación.
    * CAdES-XL (eXtended Long-term): añade certificados y evidencias de revocación (ej. CRL o respuestas OCSP), para permitir la verificación en el futuro, incluso si su fuente original no estuviera disponible.
    Los PSCs eliminan los certificados de las CRLs una vez que el certificado ha caducado. Esto supone que en formatos de firma no-longeva no resulta posible validar la firma si el certificado ha caducado en el periodo transcurrido entre la firma y su validación. Para evitar este problema, los formatos de firma longeva incorporan el resultado de la validación en el momento de la propia firma.
    * CAdES-A (Archival): añade sellos de tiempo posteriores periódicamente (re-sellado) para prevenir el compromiso causado por la debilidad de los algoritmos de firma con el tiempo.
* XMLDsig:
    * Define una sintaxis XML para soporte a la firma digital.
    * Permite firmar cualquier tipo de recurso, no solo XML.
    * Existen varios modos: detached signature, enveloped signature y enveloping signature.
* XAdES (XML Advanced Electronic Signature): Define varios perfiles de uso de XMLDsig para firma electrónica avanzada: XAdES-BES, XAdES-EPES, XAdES-T, XAdES-C, XAdES-X, XAdES-XL, XAdES-A
* PAdES (PDF Advanced Electronic Signature)
* S/MIME (Secure / Multipurpose Internet Mail Extensions)
* ASiC (Associated Signature Container)
    * Define una estructura de contenedor para englobar: archivo, firma y sello de tiempo
    * El contenedor está basado en zip



---

Bibliografía:

* PreparaTic27 - Pack1/080
* [www.uv.es - Introducción a los certificados digitales](https://www.uv.es/sto/articulos/BEI-2003-11/certificados_digitales.html)
* [mozilla.org - OCSP Stapling in Firefox](https://blog.mozilla.org/security/2013/07/29/ocsp-stapling-in-firefox/)
* [wikipedia.org - OCSP stapling](https://en.wikipedia.org/wiki/OCSP_stapling)
