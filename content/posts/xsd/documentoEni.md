---
title: documento (documentoEni)
summary: "Fuente: [administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/documentoEni.xsd](http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/documentoEni.xsd)"
---

<div class="widthscroll" id="documento">
<pre><code><a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r documento -e 5 -o <a href="documentoEni/documento.csv">documento.csv</a> http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/documentoEni.xsd
<a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r documento -e 5 -o <a href="documentoEni/documento.txt">documento.txt</a> http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/documentoEni.xsd
<a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r documento -e 5 -o <a href="documentoEni/documento.png">documento.png</a> http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/documentoEni.xsd
<a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r documento -e 5 -o <a href="documentoEni/documento.svg">documento.svg</a> http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/documentoEni.xsd
</code></pre>
</div>

![Diagrama de documento (documentoEni.xsd)](documentoEni/documento.png)

| PATH | NAME | TYPE | NAMESPACE | COMMENT |
|:----|:----|:----|:----|:----|
| /documento | documento | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e | El elemento "documento" podrá aparecer como elemento raíz de un documento XML objeto de intercambio o como elemento no raíz (elemento hijo). |
| /documento/contenido | contenido | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e |  |
| /documento/contenido/DatosXML | DatosXML | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e | Contenido en formato XML. En caso de datos XML cuya codificación difiera de la de esta estructura raíz se incluirá una cláusula CDATA. |
| /documento/contenido/ValorBinario | ValorBinario | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e | Contenido en base64. |
| /documento/contenido/referenciaFichero | referenciaFichero | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e | Referencia interna al fichero de contenido. |
| /documento/contenido/NombreFormato | NombreFormato | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e | El formato del fichero de contenido del documento electrónico atenderá a lo establecido en la NTI de Catálogo de estándares. |
| /documento/metadatos | metadatos | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e |  |
| /documento/metadatos/VersionNTI | VersionNTI | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e |  |
| /documento/metadatos/Identificador | Identificador | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e |  |
| /documento/metadatos/Organo | Organo | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e |  |
| /documento/metadatos/FechaCaptura | FechaCaptura | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e |  |
| /documento/metadatos/OrigenCiudadanoAdministracion | OrigenCiudadanoAdministracion | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e |  |
| /documento/metadatos/EstadoElaboracion | EstadoElaboracion | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e | - EE01 - Original. - EE02 - Copia electrónica auténtica con cambio de formato. - EE03 - Copia electrónica auténtica de documento papel. - EE04 - Copia electrónica parcial auténtica. - EE99 - Otros. |
| /documento/metadatos/EstadoElaboracion/ValorEstadoElaboracion | ValorEstadoElaboracion | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e |  |
| /documento/metadatos/EstadoElaboracion/IdentificadorDocumentoOrigen | IdentificadorDocumentoOrigen | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e |  |
| /documento/metadatos/TipoDocumental | TipoDocumental | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e | /*Documentos de decisión*/ - TD01 - Resolución. - TD02 - Acuerdo. - TD03 - Contrato. - TD04 - Convenio. - TD05 - Declaración. /*Documentos de transmisión*/ - TD06 - Comunicación. - TD07 - Notificación. - TD08 - Publicación. - TD09 - Acuse de recibo. /*Documentos de constancia*/ - TD10 - Acta. - TD11 - Certificado. - TD12 - Diligencia. /*Documentos de juicio*/ - TD13 - Informe. /*Documentos de ciudadano*/ - TD14 - Solicitud. - TD15 - Denuncia. - TD16 - Alegación. - TD17 - Recursos. - TD18 - Comunicación ciudadano. - TD19 - Factura. - TD20 - Otros incautados. /*Otros*/ - TD99 - Otros. |
| /documento/firmas | firmas | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e |  |
| /documento/firmas/firma | firma | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e |  |
| /documento/firmas/firma/TipoFirma | TipoFirma | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e | - TF01 - CSV. - TF02 - XAdES internally detached signature. - TF03 - XAdES enveloped signature. - TF04 - CAdES detached/explicit signature. - TF05 - CAdES attached/implicit signature. - TF06 - PAdES. |
| /documento/firmas/firma/ContenidoFirma | ContenidoFirma | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e |  |
| /documento/firmas/firma/ContenidoFirma/CSV | CSV | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e |  |
| /documento/firmas/firma/ContenidoFirma/CSV/ValorCSV | ValorCSV | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e |  |
| /documento/firmas/firma/ContenidoFirma/CSV/RegulacionGeneracionCSV | RegulacionGeneracionCSV | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e |  |
| /documento/firmas/firma/ContenidoFirma/FirmaConCertificado | FirmaConCertificado | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e |  |
| /documento/firmas/firma/ContenidoFirma/FirmaConCertificado/FirmaBase64 | FirmaBase64 | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e |  |
| /documento/firmas/firma/ContenidoFirma/FirmaConCertificado/Signature | Signature | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e |  |
| /documento/firmas/firma/ContenidoFirma/FirmaConCertificado/ReferenciaFirma | ReferenciaFirma | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e | Referencia interna al fichero que incluye la firma. |

```console
curl -L http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/documentoEni.xsd
```
```xml
﻿<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema 
xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
xmlns:enids="http://administracionelectronica.gob.es/ENI/XSD/v1.0/firma" 
xmlns:enidocmeta="http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/metadatos" 
xmlns:enifile="http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/contenido" 
xmlns:enidoc="http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e" 
targetNamespace="http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e" 
elementFormDefault="qualified" attributeFormDefault="unqualified">
	<xsd:annotation>
		<xsd:documentation xml:lang="es">XSD DOCUMENTO ENI (v1.0)</xsd:documentation>
	</xsd:annotation>
	<xsd:import namespace="http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/metadatos" schemaLocation="http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/metadatos/metadatosDocumentoEni.xsd"/>
	<xsd:import namespace="http://administracionelectronica.gob.es/ENI/XSD/v1.0/firma" schemaLocation="http://administracionelectronica.gob.es/ENI/XSD/v1.0/firma/firmasEni.xsd"/>
	<xsd:import namespace="http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/contenido" schemaLocation="http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/contenido/contenidoDocumentoEni.xsd"/>
	<xsd:element name="documento" type="enidoc:TipoDocumento">
		<xsd:annotation>
			<xsd:documentation xml:lang="es">El elemento "documento" podrá aparecer como elemento raíz de un documento XML objeto de intercambio o como elemento no raíz (elemento hijo).</xsd:documentation>
		</xsd:annotation>
	</xsd:element>
	<xsd:complexType name="TipoDocumento">
		<xsd:sequence>
			<xsd:element ref="enifile:contenido"/>
			<xsd:element ref="enidocmeta:metadatos"/>
			<xsd:element ref="enids:firmas" minOccurs="0" maxOccurs="1">
				<xsd:annotation>
					<xsd:documentation xml:lang="es">La firma es obligatoria para el documento administrativo electrónico y para todo aquel documento electrónico susceptible de ser incorporado en un expediente electrónico.</xsd:documentation>
				</xsd:annotation>
			</xsd:element>
		</xsd:sequence>
		<xsd:attribute name="Id" type="xsd:ID" use="optional"/>
	</xsd:complexType>
</xsd:schema>
```