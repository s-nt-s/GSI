---
title: metadatosExp (MetadatosExpedienteEni)
summary: "Fuente: [administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e/metadatos/MetadatosExpedienteEni.xsd](http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e/metadatos/MetadatosExpedienteEni.xsd)"
---

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema 
xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
xmlns:eniexpmeta="http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e/metadatos" 
targetNamespace="http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e/metadatos" 
elementFormDefault="qualified" attributeFormDefault="unqualified">
	<xsd:annotation>
		<xsd:documentation xml:lang="es">XSD METADATOS EXPEDIENTE ELECTRONICO ENI (v1.0)</xsd:documentation>
	</xsd:annotation>
	<xsd:element name="metadatosExp" type="eniexpmeta:TipoMetadatos"/>
	<xsd:complexType name="TipoMetadatos">
		<xsd:sequence>
			<xsd:element name="VersionNTI" type="xsd:anyURI"/>
			<xsd:element name="Identificador" type="xsd:string"/>
			<xsd:element name="Organo" type="xsd:string" minOccurs="1" maxOccurs="unbounded"/>
			<xsd:element name="FechaAperturaExpediente" type="xsd:dateTime"/>
			<xsd:element name="Clasificacion" type="xsd:string"/>
			<xsd:element name="Estado">
				<xsd:annotation>
					<xsd:documentation xml:lang="es">	- E01 - Abierto.
	- E02 - Cerrado.
	- E03 - Índice para remisión cerrado. </xsd:documentation>
				</xsd:annotation>
				<xsd:complexType>
					<xsd:simpleContent>
						<xsd:extension base="eniexpmeta:enumeracionEstados"/>
					</xsd:simpleContent>
				</xsd:complexType>
			</xsd:element>
			<xsd:element name="Interesado" type="xsd:string" minOccurs="0" maxOccurs="unbounded">
				<xsd:annotation>
					<xsd:documentation xml:lang="es">Obligatorio cumplimentar si existe un interesado.</xsd:documentation>
				</xsd:annotation>
			</xsd:element>
		</xsd:sequence>
		<xsd:attribute name="Id" type="xsd:ID" use="optional"/>
	</xsd:complexType>
<xsd:simpleType name="enumeracionEstados">
		<xsd:restriction base="xsd:string">
			<xsd:enumeration value="E01"/>
			<xsd:enumeration value="E02"/>
			<xsd:enumeration value="E03"/>
		</xsd:restriction>
	</xsd:simpleType>
</xsd:schema>
```

![MetadatosExpedienteEni](MetadatosExpedienteEni/metadatosExp.png){#metadatosExp}
