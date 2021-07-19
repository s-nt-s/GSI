---
title: IndiceContenido (IndiceContenidoExpedienteEni)
---

Esquema `IndiceContenido` - [administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e/indice-e/contenido/IndiceContenidoExpedienteEni.xsd](http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e/indice-e/contenido/IndiceContenidoExpedienteEni.xsd)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema 
xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
xmlns:eniconexpind="http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e/indice-e/contenido" 
targetNamespace="http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e/indice-e/contenido" 
elementFormDefault="qualified" attributeFormDefault="unqualified">
	<xsd:annotation>
		<xsd:documentation xml:lang="es">XSD CONTENIDO INDICE EXPEDIENTE ELECTRONICO ENI (v1.0)</xsd:documentation>
	</xsd:annotation>
	<xsd:element name="IndiceContenido" type="eniconexpind:TipoIndiceContenido"/>
	<xsd:complexType name="TipoIndiceContenido">
		<xsd:sequence>
			<xsd:element name="FechaIndiceElectronico" type="xsd:dateTime"/>
			<xsd:choice maxOccurs="unbounded">
				<xsd:element name="DocumentoIndizado" type="eniconexpind:TipoDocumentoIndizado"/>
				<xsd:element name="ExpedienteIndizado" type="eniconexpind:TipoIndiceContenido"/>
				<xsd:element name="CarpetaIndizada" type="eniconexpind:TipoCarpetaIndizada"/>
			</xsd:choice>
		</xsd:sequence>
		<xsd:attribute name="Id" type="xsd:ID" use="optional"/>
	</xsd:complexType>
	<xsd:complexType name="TipoDocumentoIndizado">
		<xsd:sequence>
			<xsd:element name="IdentificadorDocumento" type="xsd:string"/>
			<xsd:element name="ValorHuella" type="xsd:string"/>
			<xsd:element name="FuncionResumen" type="xsd:string"/>
			<xsd:element name="FechaIncorporacionExpediente" type="xsd:dateTime" minOccurs="0"/>
			<xsd:element name="OrdenDocumentoExpediente" type="xsd:string" minOccurs="0"/>
		</xsd:sequence>
		<xsd:attribute name="Id" type="xsd:ID" use="optional"/>
	</xsd:complexType>
	<xsd:complexType name="TipoCarpetaIndizada">
		<xsd:sequence>
			<xsd:element name="IdentificadorCarpeta" type="xsd:string"/>
			<xsd:choice maxOccurs="unbounded">
				<xsd:element name="DocumentoIndizado" type="eniconexpind:TipoDocumentoIndizado"/>
				<xsd:element name="ExpedienteIndizado" type="eniconexpind:TipoIndiceContenido"/>
				<xsd:element name="CarpetaIndizada" type="eniconexpind:TipoCarpetaIndizada"/>
			</xsd:choice>
		</xsd:sequence>
		<xsd:attribute name="Id" type="xsd:ID" use="optional"/>
	</xsd:complexType>
</xsd:schema>
```

![IndiceContenidoExpedienteEni](IndiceContenidoExpedienteEni/IndiceContenido.png){#IndiceContenido}
