---
title: De_Control (SICRES4_MENSAJE_APL)
summary: "Fuente: [administracionelectronica.gob.es/pae_Home/dam/jcr:06f79467-afcc-473a-a6cb-f2d00791ad17/2021-SICRES4_MENSAJE_APL.xsd](https://administracionelectronica.gob.es/pae_Home/dam/jcr:06f79467-afcc-473a-a6cb-f2d00791ad17/2021-SICRES4_MENSAJE_APL.xsd)"
---

<div class="widthscroll" id="De_Control">
<pre><code><a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r De_Control -e 1 -o <a href="SICRES4_MENSAJE_APL/De_Control.csv">De_Control.csv</a> https://administracionelectronica.gob.es/pae_Home/dam/jcr:06f79467-afcc-473a-a6cb-f2d00791ad17/2021-SICRES4_MENSAJE_APL.xsd
<a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r De_Control -e 1 -o <a href="SICRES4_MENSAJE_APL/De_Control.txt">De_Control.txt</a> https://administracionelectronica.gob.es/pae_Home/dam/jcr:06f79467-afcc-473a-a6cb-f2d00791ad17/2021-SICRES4_MENSAJE_APL.xsd
<a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r De_Control -e 1 -o <a href="SICRES4_MENSAJE_APL/De_Control.png">De_Control.png</a> https://administracionelectronica.gob.es/pae_Home/dam/jcr:06f79467-afcc-473a-a6cb-f2d00791ad17/2021-SICRES4_MENSAJE_APL.xsd
<a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r De_Control -e 1 -o <a href="SICRES4_MENSAJE_APL/De_Control.svg">De_Control.svg</a> https://administracionelectronica.gob.es/pae_Home/dam/jcr:06f79467-afcc-473a-a6cb-f2d00791ad17/2021-SICRES4_MENSAJE_APL.xsd</code></pre>
</div>

![Diagrama de De_Control (SICRES4_MENSAJE_APL.xsd)](SICRES4_MENSAJE_APL/De_Control.png)


```console
curl -L https://administracionelectronica.gob.es/pae_Home/dam/jcr:06f79467-afcc-473a-a6cb-f2d00791ad17/2021-SICRES4_MENSAJE_APL.xsd
```
```xml
<xs:schema elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="De_Control">
    <xs:complexType>
      <xs:sequence>
        <xs:element minOccurs="1" maxOccurs="1" name="Codigo_Entidad_Registral_Origen">
          <xs:simpleType>
            <xs:restriction base="xs:string">
              <xs:maxLength value="21"/>
            </xs:restriction>
          </xs:simpleType>
        </xs:element>
        <xs:element minOccurs="1" maxOccurs="1" name="Codigo_Entidad_Registral_Destino">
          <xs:simpleType>
            <xs:restriction base="xs:string">
              <xs:maxLength value="21"/>
            </xs:restriction>
          </xs:simpleType>
        </xs:element>
        <xs:element minOccurs="1" maxOccurs="1" name="Identificador_Intercambio">
          <xs:simpleType>
            <xs:restriction base="xs:string">
              <xs:maxLength value="33"/>
            </xs:restriction>
          </xs:simpleType>
        </xs:element>
        <xs:element minOccurs="1" maxOccurs="1" name="Tipo_Mensaje">
          <xs:simpleType>
            <xs:restriction base="xs:string">
				<xs:maxLength value="2"/>
				<xs:enumeration value="01"/>
				<xs:enumeration value="02"/>
				<xs:enumeration value="03"/>
				<xs:enumeration value="04"/>
				<xs:enumeration value="05"/>
				<xs:enumeration value="06"/>
            </xs:restriction>
          </xs:simpleType>
        </xs:element>
        <xs:element minOccurs="0" maxOccurs="1" name="Descripcion_Mensaje">
          <xs:simpleType>
            <xs:restriction base="xs:string">
              <xs:maxLength value="1024"/>
            </xs:restriction>
          </xs:simpleType>
        </xs:element>
        <xs:element minOccurs="0" maxOccurs="1" name="Numero_Registro_Entrada_Destino">
          <xs:simpleType>
            <xs:restriction base="xs:string">
              <xs:maxLength value="20"/>
            </xs:restriction>
          </xs:simpleType>
        </xs:element>
        <xs:element minOccurs="0" maxOccurs="1" name="Fecha_Hora_Entrada_Destino">
          <xs:simpleType>
            <xs:restriction base="xs:string">
              <xs:maxLength value="19"/>
            </xs:restriction>
          </xs:simpleType>
        </xs:element>
        <xs:element minOccurs="1" maxOccurs="1" name="Indicador_Prueba">
          <xs:simpleType>
            <xs:restriction base="xs:string">
              <xs:enumeration value="0"/>
              <xs:enumeration value="1"/>
            </xs:restriction>
          </xs:simpleType>
        </xs:element>
        <xs:element minOccurs="0" maxOccurs="unbounded" name="Identificador_Fichero">
          <xs:simpleType>
            <xs:restriction base="xs:string">
              <xs:maxLength value="50"/>
            </xs:restriction>
          </xs:simpleType>
        </xs:element>
        <xs:element minOccurs="0" maxOccurs="1" name="Codigo_Error">
          <xs:simpleType>
            <xs:restriction base="xs:string">
              <xs:maxLength value="4"/>
            </xs:restriction>
          </xs:simpleType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```