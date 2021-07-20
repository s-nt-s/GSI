﻿---
title: contenido (contenidoDocumentoEni)
summary: "Fuente: [administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/contenido/contenidoDocumentoEni.xsd](http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/contenido/contenidoDocumentoEni.xsd)"
---

<div class="widthscroll" id="contenido">
<pre><code><a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r contenido -e 2 -o <a href="contenidoDocumentoEni/contenido.csv">contenido.csv</a> http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/contenido/contenidoDocumentoEni.xsd
<a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r contenido -e 2 -o <a href="contenidoDocumentoEni/contenido.txt">contenido.txt</a> http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/contenido/contenidoDocumentoEni.xsd
<a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r contenido -e 2 -o <a href="contenidoDocumentoEni/contenido.png">contenido.png</a> http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/contenido/contenidoDocumentoEni.xsd
<a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r contenido -e 2 -o <a href="contenidoDocumentoEni/contenido.svg">contenido.svg</a> http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/contenido/contenidoDocumentoEni.xsd</code></pre>
</div>

![Diagrama de contenido (contenidoDocumentoEni.xsd)](contenidoDocumentoEni/contenido.png)


```console
curl -L http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/contenido/contenidoDocumentoEni.xsd
```
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