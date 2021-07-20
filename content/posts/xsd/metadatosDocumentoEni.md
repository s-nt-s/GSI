﻿---
title: metadatos (metadatosDocumentoEni)
summary: "Fuente: [administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/metadatos/metadatosDocumentoEni.xsd](http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/metadatos/metadatosDocumentoEni.xsd)"
---

<div class="widthscroll" id="metadatos">
<pre><code><a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r metadatos -e 2 -o <a href="metadatosDocumentoEni/metadatos.csv">metadatos.csv</a> http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/metadatos/metadatosDocumentoEni.xsd
<a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r metadatos -e 2 -o <a href="metadatosDocumentoEni/metadatos.txt">metadatos.txt</a> http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/metadatos/metadatosDocumentoEni.xsd
<a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r metadatos -e 2 -o <a href="metadatosDocumentoEni/metadatos.png">metadatos.png</a> http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/metadatos/metadatosDocumentoEni.xsd
<a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r metadatos -e 2 -o <a href="metadatosDocumentoEni/metadatos.svg">metadatos.svg</a> http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/metadatos/metadatosDocumentoEni.xsd</code></pre>
</div>

![Diagrama de metadatos (metadatosDocumentoEni.xsd)](metadatosDocumentoEni/metadatos.png)


```console
curl -L http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/metadatos/metadatosDocumentoEni.xsd
```
```xml
<?xml version="1.0" encoding="utf-8"?>
<xsd:schema 
xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
xmlns:enidocmeta="http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/metadatos" 
targetNamespace="http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/metadatos" 
elementFormDefault="qualified" attributeFormDefault="unqualified">
	<xsd:annotation>
		<xsd:documentation xml:lang="es">XSD METADATOS DOCUMENTO ENI (v1.0)</xsd:documentation>
	</xsd:annotation>
	<xsd:element name="metadatos" type="enidocmeta:TipoMetadatos"/>
	<xsd:complexType name="TipoMetadatos">
		<xsd:sequence>
			<xsd:element name="VersionNTI" type="xsd:anyURI"/>
			<xsd:element name="Identificador" type="xsd:string"/>
			<xsd:element name="Organo" type="xsd:string" minOccurs="1" maxOccurs="unbounded"/>
			<xsd:element name="FechaCaptura" type="xsd:dateTime"/>
			<xsd:element name="OrigenCiudadanoAdministracion" type="xsd:boolean"/>
			<xsd:element name="EstadoElaboracion" type="enidocmeta:TipoEstadoElaboracion">
				<xsd:annotation>
					<xsd:documentation xml:lang="es">- EE01 - Original. 	
- EE02 - Copia electrónica auténtica con cambio de formato.	
- EE03 - Copia electrónica auténtica de documento papel. 	
- EE04 - Copia electrónica parcial auténtica.	
- EE99 - Otros.	</xsd:documentation>
				</xsd:annotation>
			</xsd:element>
			<xsd:element name="TipoDocumental" type="enidocmeta:tipoDocumental">
				<xsd:annotation>
					<xsd:documentation xml:lang="es">/*Documentos de decisión*/
- TD01 - Resolución.
- TD02 - Acuerdo.
- TD03 - Contrato.
- TD04 - Convenio.
- TD05 - Declaración.
/*Documentos de transmisión*/
- TD06 - Comunicación.
- TD07 - Notificación.
- TD08 - Publicación.
- TD09 - Acuse de recibo.
/*Documentos de constancia*/
- TD10 - Acta.
- TD11 - Certificado.
- TD12 - Diligencia.
/*Documentos de juicio*/
- TD13 - Informe.
/*Documentos de ciudadano*/
- TD14 - Solicitud.
- TD15 - Denuncia.
- TD16 - Alegación.
- TD17 - Recursos.
- TD18 - Comunicación ciudadano.
- TD19 - Factura.
- TD20 - Otros incautados.
/*Otros*/
- TD99 - Otros.</xsd:documentation>
				</xsd:annotation>
			</xsd:element>
		</xsd:sequence>
		<xsd:attribute name="Id" type="xsd:ID" use="optional"/>
	</xsd:complexType>
	<xsd:complexType name="TipoEstadoElaboracion">
		<xsd:sequence>
			<xsd:element name="ValorEstadoElaboracion" type="enidocmeta:enumeracionEstadoElaboracion"/>
			<xsd:element name="IdentificadorDocumentoOrigen" type="xsd:string" minOccurs="0" maxOccurs="1"/>
		</xsd:sequence>
	</xsd:complexType>
<xsd:simpleType name="enumeracionEstadoElaboracion">
		<xsd:restriction base="xsd:string">
			<xsd:enumeration value="EE01"/>
			<xsd:enumeration value="EE02"/>
			<xsd:enumeration value="EE03"/>
			<xsd:enumeration value="EE04"/>
			<xsd:enumeration value="EE99"/>
		</xsd:restriction>
	</xsd:simpleType>
<xsd:simpleType name="tipoDocumental">
		<xsd:restriction base="xsd:string">
			<xsd:enumeration value="TD01"/>
			<xsd:enumeration value="TD02"/>
			<xsd:enumeration value="TD03"/>
			<xsd:enumeration value="TD04"/>
			<xsd:enumeration value="TD05"/>
			<xsd:enumeration value="TD06"/>
			<xsd:enumeration value="TD07"/>
			<xsd:enumeration value="TD08"/>
			<xsd:enumeration value="TD09"/>
			<xsd:enumeration value="TD10"/>
			<xsd:enumeration value="TD11"/>
			<xsd:enumeration value="TD12"/>
			<xsd:enumeration value="TD13"/>
			<xsd:enumeration value="TD14"/>
			<xsd:enumeration value="TD15"/>
			<xsd:enumeration value="TD16"/>
			<xsd:enumeration value="TD17"/>
			<xsd:enumeration value="TD18"/>
			<xsd:enumeration value="TD19"/>
			<xsd:enumeration value="TD20"/>
			<xsd:enumeration value="TD99"/>
		</xsd:restriction>
	</xsd:simpleType>
</xsd:schema>
```