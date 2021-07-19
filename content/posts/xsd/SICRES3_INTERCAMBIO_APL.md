﻿---
title: Fichero_Intercambio_SICRES_3 (SICRES3_INTERCAMBIO_APL)
summary: "Fuente: [administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/SICRES3_INTERCAMBIO_APL.xsd](http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/SICRES3_INTERCAMBIO_APL.xsd)"
---

<div class="widthscroll" id="Fichero_Intercambio_SICRES_3">
<pre><code><a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r Fichero_Intercambio_SICRES_3 -e 2 -o <a href="SICRES3_INTERCAMBIO_APL/Fichero_Intercambio_SICRES_3.csv">Fichero_Intercambio_SICRES_3.csv</a> http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/SICRES3_INTERCAMBIO_APL.xsd
<a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r Fichero_Intercambio_SICRES_3 -e 2 -o <a href="SICRES3_INTERCAMBIO_APL/Fichero_Intercambio_SICRES_3.txt">Fichero_Intercambio_SICRES_3.txt</a> http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/SICRES3_INTERCAMBIO_APL.xsd
<a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r Fichero_Intercambio_SICRES_3 -e 2 -o <a href="SICRES3_INTERCAMBIO_APL/Fichero_Intercambio_SICRES_3.png">Fichero_Intercambio_SICRES_3.png</a> http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/SICRES3_INTERCAMBIO_APL.xsd
<a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a> -no-gui -y -r Fichero_Intercambio_SICRES_3 -e 2 -o <a href="SICRES3_INTERCAMBIO_APL/Fichero_Intercambio_SICRES_3.svg">Fichero_Intercambio_SICRES_3.svg</a> http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/SICRES3_INTERCAMBIO_APL.xsd</code></pre>
</div>

![Diagrama de Fichero_Intercambio_SICRES_3 (SICRES3_INTERCAMBIO_APL.xsd)](SICRES3_INTERCAMBIO_APL/Fichero_Intercambio_SICRES_3.png)


```console
curl -L http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e/SICRES3_INTERCAMBIO_APL.xsd
```
```xml
<xs:schema elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="Fichero_Intercambio_SICRES_3">
    <xs:complexType>
      <xs:sequence>
        <xs:element minOccurs="1" maxOccurs="1" name="De_Origen_o_Remitente">
          <xs:complexType>
            <xs:sequence>
              <xs:element minOccurs="1" maxOccurs="1" name="Codigo_Entidad_Registral_Origen">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="21"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Decodificacion_Entidad_Registral_Origen">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="80"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="1" maxOccurs="1" name="Numero_Registro_Entrada">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="20"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="1" maxOccurs="1" name="Fecha_Hora_Entrada">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="14"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Timestamp_Entrada" type="xs:base64Binary"/>
              <xs:element minOccurs="0" maxOccurs="1" name="Codigo_Unidad_Tramitacion_Origen">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="21"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Decodificacion_Unidad_Tramitacion_Origen">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="80"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element minOccurs="1" maxOccurs="1" name="De_Destino">
          <xs:complexType>
            <xs:sequence>
              <xs:element minOccurs="1" maxOccurs="1" name="Codigo_Entidad_Registral_Destino">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="21"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Decodificacion_Entidad_Registral_Destino">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="80"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Codigo_Unidad_Tramitacion_Destino">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="21"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Decodificacion_Unidad_Tramitacion_Destino">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="80"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element minOccurs="1" maxOccurs="unbounded" name="De_Interesado">
          <xs:complexType>
            <xs:sequence>
              <xs:element minOccurs="0" maxOccurs="1" name="Tipo_Documento_Identificacion_Interesado">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="1"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Documento_Identificacion_Interesado">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="17"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Razon_Social_Interesado">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="80"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Nombre_Interesado">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="30"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Primer_Apellido_Interesado">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="30"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Segundo_Apellido_Interesado">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="30"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Tipo_Documento_Identificacion_Representante">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="1"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Documento_Identificacion_Representante">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="17"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Razon_Social_Representante">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="80"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Nombre_Representante">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="30"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Primer_Apellido_Representante">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="30"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Segundo_Apellido_Representante">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="30"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Pais_Interesado">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="4"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Provincia_Interesado">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="2"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Municipio_Interesado">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="5"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Direccion_Interesado">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="160"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Codigo_Postal_Interesado">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="5"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Correo_Electronico_Interesado">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="160"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Telefono_Contacto_Interesado">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="20"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Direccion_Electronica_Habilitada_Interesado">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="160"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Canal_Preferente_Comunicacion_Interesado">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="2"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Pais_Representante">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="4"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Provincia_Representante">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="2"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Municipio_Representante">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="5"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Direccion_Representante">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="160"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Codigo_Postal_Representante">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="5"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Correo_Electronico_Representante">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="160"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Telefono_Contacto_Representante">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="20"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Direccion_Electronica_Habilitada_Representante">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="160"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Canal_Preferente_Comunicacion_Representante">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="2"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Observaciones">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="160"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element minOccurs="1" maxOccurs="1" name="De_Asunto">
          <xs:complexType>
            <xs:sequence>
              <xs:element minOccurs="1" maxOccurs="1" name="Resumen">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="240"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Codigo_Asunto_Segun_Destino">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="16"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Referencia_Externa">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="16"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Numero_Expediente">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="80"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element minOccurs="0" maxOccurs="unbounded" name="De_Anexo">
          <xs:complexType>
            <xs:sequence>
              <xs:element minOccurs="1" maxOccurs="1" name="Nombre_Fichero_Anexado">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="80"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="1" maxOccurs="1" name="Identificador_Fichero">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="50"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Validez_Documento">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="2"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="1" maxOccurs="1" name="Tipo_Documento">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="2"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Certificado" type="xs:base64Binary"/>
              <xs:element minOccurs="0" maxOccurs="1" name="Firma_Documento" type="xs:base64Binary"/>
              <xs:element minOccurs="0" maxOccurs="1" name="TimeStamp" type="xs:base64Binary"/>
              <xs:element minOccurs="0" maxOccurs="1" name="Validacion_OCSP_Certificado" type="xs:base64Binary"/>
              <xs:element minOccurs="1" maxOccurs="1" name="Hash" type="xs:base64Binary"/>
              <xs:element minOccurs="0" maxOccurs="1" name="Tipo_MIME">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="20"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Anexo" type="xs:base64Binary"/>
              <xs:element minOccurs="0" maxOccurs="1" name="Identificador_Documento_Firmado">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="50"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Observaciones">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="50"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element minOccurs="1" maxOccurs="1" name="De_Internos_Control">
          <xs:complexType>
            <xs:sequence>
              <xs:element minOccurs="0" maxOccurs="1" name="Tipo_Transporte_Entrada">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="2"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Numero_Transporte_Entrada">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="20"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Nombre_Usuario">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="80"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Contacto_Usuario">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="160"/>
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
              <xs:element minOccurs="0" maxOccurs="1" name="Aplicacion_Version_Emisora">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="4"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="1" maxOccurs="1" name="Tipo_Anotacion">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="2"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Descripcion_Tipo_Anotacion">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="80"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="1" maxOccurs="1" name="Tipo_Registro">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="1"/>
                    <xs:enumeration value="0"/>
                    <xs:enumeration value="1"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="1" maxOccurs="1" name="Documentacion_Fisica">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="1"/>
                    <xs:enumeration value="1"/>
                    <xs:enumeration value="2"/>
                    <xs:enumeration value="3"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Observaciones_Apunte">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="50"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="1" maxOccurs="1" name="Indicador_Prueba">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="1"/>
                    <xs:enumeration value="0"/>
                    <xs:enumeration value="1"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="1" maxOccurs="1" name="Codigo_Entidad_Registral_Inicio">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="21"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" name="Decodificacion_Entidad_Registral_Inicio">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="80"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element minOccurs="1" maxOccurs="1" name="De_Formulario_Generico">
          <xs:complexType>
            <xs:sequence>
              <xs:element minOccurs="1" maxOccurs="1" name="Expone">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="4000"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element minOccurs="1" maxOccurs="1" name="Solicita">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:maxLength value="4000"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```