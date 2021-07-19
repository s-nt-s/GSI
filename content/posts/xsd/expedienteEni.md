---
title: expediente (expedienteEni)
summary: "Fuente: [administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e/expedienteEni.xsd](http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e/expedienteEni.xsd)"
---

<div class="widthscroll" id="expediente">
<pre><code><a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r expediente -e 6 -o <a href="expedienteEni/expediente.csv">expediente.csv</a> http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e/expedienteEni.xsd
<a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r expediente -e 6 -o <a href="expedienteEni/expediente.txt">expediente.txt</a> http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e/expedienteEni.xsd
<a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r expediente -e 6 -o <a href="expedienteEni/expediente.png">expediente.png</a> http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e/expedienteEni.xsd
<a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r expediente -e 6 -o <a href="expedienteEni/expediente.svg">expediente.svg</a> http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e/expedienteEni.xsd
</code></pre>
</div>

![Diagrama de expediente (expedienteEni.xsd)](expedienteEni/expediente.png)

| PATH | NAME | TYPE | NAMESPACE | COMMENT |
|:----|:----|:----|:----|:----|
| /expediente | expediente | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice | indice | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/IndiceContenido | IndiceContenido | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/IndiceContenido/FechaIndiceElectronico | FechaIndiceElectronico | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/IndiceContenido/DocumentoIndizado | DocumentoIndizado | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/IndiceContenido/DocumentoIndizado/IdentificadorDocumento | IdentificadorDocumento | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/IndiceContenido/DocumentoIndizado/ValorHuella | ValorHuella | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/IndiceContenido/DocumentoIndizado/FuncionResumen | FuncionResumen | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/IndiceContenido/DocumentoIndizado/FechaIncorporacionExpediente | FechaIncorporacionExpediente | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/IndiceContenido/DocumentoIndizado/OrdenDocumentoExpediente | OrdenDocumentoExpediente | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/IndiceContenido/ExpedienteIndizado | ExpedienteIndizado | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/IndiceContenido/ExpedienteIndizado/FechaIndiceElectronico | FechaIndiceElectronico | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/IndiceContenido/ExpedienteIndizado/DocumentoIndizado | DocumentoIndizado | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/IndiceContenido/ExpedienteIndizado/ExpedienteIndizado | ExpedienteIndizado | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/IndiceContenido/ExpedienteIndizado/CarpetaIndizada | CarpetaIndizada | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/IndiceContenido/CarpetaIndizada | CarpetaIndizada | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/IndiceContenido/CarpetaIndizada/IdentificadorCarpeta | IdentificadorCarpeta | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/IndiceContenido/CarpetaIndizada/DocumentoIndizado | DocumentoIndizado | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/IndiceContenido/CarpetaIndizada/ExpedienteIndizado | ExpedienteIndizado | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/IndiceContenido/CarpetaIndizada/CarpetaIndizada | CarpetaIndizada | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/firmas | firmas | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/firmas/firma | firma | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/firmas/firma/TipoFirma | TipoFirma | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e | - TF01 - CSV. - TF02 - XAdES internally detached signature. - TF03 - XAdES enveloped signature. - TF04 - CAdES detached/explicit signature. - TF05 - CAdES attached/implicit signature. - TF06 - PAdES. |
| /expediente/indice/firmas/firma/ContenidoFirma | ContenidoFirma | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/firmas/firma/ContenidoFirma/CSV | CSV | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/firmas/firma/ContenidoFirma/CSV/ValorCSV | ValorCSV | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/firmas/firma/ContenidoFirma/CSV/RegulacionGeneracionCSV | RegulacionGeneracionCSV | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/firmas/firma/ContenidoFirma/FirmaConCertificado | FirmaConCertificado | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/firmas/firma/ContenidoFirma/FirmaConCertificado/FirmaBase64 | FirmaBase64 | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/firmas/firma/ContenidoFirma/FirmaConCertificado/Signature | Signature | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/indice/firmas/firma/ContenidoFirma/FirmaConCertificado/ReferenciaFirma | ReferenciaFirma | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e | Referencia interna al fichero que incluye la firma. |
| /expediente/metadatosExp | metadatosExp | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/metadatosExp/VersionNTI | VersionNTI | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/metadatosExp/Identificador | Identificador | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/metadatosExp/Organo | Organo | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/metadatosExp/FechaAperturaExpediente | FechaAperturaExpediente | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/metadatosExp/Clasificacion | Clasificacion | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |  |
| /expediente/metadatosExp/Estado | Estado | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e | - E01 - Abierto. - E02 - Cerrado. - E03 - Índice para remisión cerrado. |
| /expediente/metadatosExp/Interesado | Interesado | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e | Obligatorio cumplimentar si existe un interesado. |
| /expediente/VisualizacionIndice | VisualizacionIndice | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e | Elemento opcional que permite visualizar el contenido completo del expediente (contenido del índice). |
| /expediente/VisualizacionIndice/DatosXML | DatosXML | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e | Contenido en formato XML. En caso de datos XML cuya codificación difiera de la de esta estructura raíz se incluirá una cláusula CDATA. |
| /expediente/VisualizacionIndice/ValorBinario | ValorBinario | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e | Contenido en base64. |
| /expediente/VisualizacionIndice/referenciaFichero | referenciaFichero | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e | Referencia interna al fichero de contenido. |
| /expediente/VisualizacionIndice/NombreFormato | NombreFormato | element | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e | El formato del fichero de contenido del documento electrónico atenderá a lo establecido en la NTI de Catálogo de estándares. |

```console
curl -L http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e/expedienteEni.xsd
```
```xml
<?xml version="1.0" encoding="utf-8"?>
<xsd:schema 
xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
xmlns:eniexpind="http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e/indice-e" 
xmlns:eniexpmeta="http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e/metadatos" 
xmlns:eniexp="http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e" 
xmlns:enifile="http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/contenido" 
targetNamespace="http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e" elementFormDefault="qualified" attributeFormDefault="unqualified">
	<xsd:annotation>
		<xsd:documentation xml:lang="es">XSD EXPEDIENTE ELECTRONICO ENI (v1.0)</xsd:documentation>
	</xsd:annotation>
	<xsd:import namespace="http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e/indice-e" schemaLocation="http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e/indice-e/IndiceExpedienteEni.xsd"/>
	<xsd:import namespace="http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e/metadatos" schemaLocation="http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e/metadatos/MetadatosExpedienteEni.xsd"/>
	<xsd:import namespace="http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/contenido" schemaLocation="http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/contenido/contenidoDocumentoEni.xsd"/>
	<xsd:element name="expediente" type="eniexp:TipoExpediente"/>
	<xsd:complexType name="TipoExpediente">
		<xsd:annotation>
			<xsd:documentation>Para el intercambio de un expediente electrónico, se envía en primer lugar, el índice del expediente. Posteriormente, se enviarán los documentos que lo componen , uno a uno,  y siguiendo la distribución reflejada en el contenido del Índice.</xsd:documentation>
		</xsd:annotation>
		<xsd:sequence>
			<xsd:element ref="eniexpind:indice"/>
			<xsd:element ref="eniexpmeta:metadatosExp"/>
			<xsd:element name="VisualizacionIndice" type="enifile:TipoContenido" minOccurs="0" maxOccurs="1">
				<xsd:annotation>
					<xsd:documentation>Elemento opcional que permite visualizar el contenido completo del expediente (contenido del índice).</xsd:documentation>
				</xsd:annotation>
			</xsd:element>
		</xsd:sequence>
		<xsd:attribute name="Id" type="xsd:ID" use="optional"/>
	</xsd:complexType>
</xsd:schema>
```