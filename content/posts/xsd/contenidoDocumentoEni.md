---
title: contenido (contenidoDocumentoEni)
---

Esquema `contenido` - [administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/contenido/contenidoDocumentoEni.xsd](http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/contenido/contenidoDocumentoEni.xsd)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema 
xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
xmlns:enifile="http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/contenido" 
targetNamespace="http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/contenido" 
elementFormDefault="qualified" attributeFormDefault="unqualified">
	<xsd:annotation>
		<xsd:documentation xml:lang="es">XSD CONTENIDO DOCUMENTO ENI (v1.0)</xsd:documentation>
	</xsd:annotation>
	<xsd:element name="contenido" type="enifile:TipoContenido"/>
	<xsd:complexType name="TipoContenido">
		<xsd:sequence>
			<xsd:choice>
				<xsd:element name="DatosXML" type="xsd:anyType">
					<xsd:annotation>
						<xsd:documentation xml:lang="es">Contenido en formato XML. En caso de datos XML cuya codificación difiera de la de esta estructura raíz se incluirá una cláusula CDATA.</xsd:documentation>
					</xsd:annotation>
				</xsd:element>
				<xsd:element name="ValorBinario" type="xsd:base64Binary">
					<xsd:annotation>
						<xsd:documentation xml:lang="es">Contenido en base64.</xsd:documentation>
					</xsd:annotation>
				</xsd:element>
				<xsd:element name="referenciaFichero" type="xsd:string">
					<xsd:annotation>
						<xsd:documentation xml:lang="es">Referencia interna al fichero de contenido.</xsd:documentation>
					</xsd:annotation>
				</xsd:element>
			</xsd:choice>
			<xsd:element name="NombreFormato" type="xsd:string">
				<xsd:annotation>
					<xsd:documentation xml:lang="es">El formato del fichero de contenido del documento electrónico atenderá a lo establecido en la NTI de Catálogo de estándares.</xsd:documentation>
				</xsd:annotation>
			</xsd:element>
		</xsd:sequence>
		<xsd:attribute name="Id" type="xsd:ID" use="optional"/>
	</xsd:complexType>
</xsd:schema>
```

![contenidoDocumentoEni](contenidoDocumentoEni/contenido.png){#contenido}
