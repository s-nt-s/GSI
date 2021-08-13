---
title: Reutilización de la información del Sector Público (RISP)
---

# Conceptos básicos

Con la **RISP** se busca potenciar la **economía de los datos**.

La **[NTI reutilización de recursos de información]({filename}04-ENI.md#reutilizacion-de-recursos-de-informacion)**
determinar las pautas básicas para la reutilización de documentos y recursos de
información elaborados o custodiados por el sector público.

La directiva (UE) 2019/1024 define los siguientes conceptos:

* **Formato abierto**: formato de archivo independiente de plataformas y puesto
a disposición del público sin restricciones que impidan la reutilización
* **Formato legible por máquina**: formato de archivo estructurado que permite
a las aplicaciones informáticas identificar, reconocer y extraer con facilidad
datos específicos, incluidas las declaraciones fácticas y su estructura interna
* **Datos dinámicos**: documentos en formato digital, sujetos a actualizaciones
frecuentes o en tiempo real, debido a su volatilidad o rápida obsolescencia
(ej: datos de sensores)

e identifica como datos de alto valor los:

* geoespaciales
* de medio ambiente
* meteorológicos
* estadísticos
* de sociedades mercantiles
* de movilidad y transporte

y por lo tanto han de ofrecerse gratuitamente, legibles por máquina y a través
de API. Si es posible, además deben estar disponibles para descarga masiva.

# Ley 37/2007

## Ámbito

**Ambito subjetivo**:

* AGE + CCAA + EELL
* Sector público institucional
* Universidades de manera supletoria

**Ambito objetivo**: documentos en poder de las AAPP y sus organismos
que no constituyan una actividad administrativa pública.

El intercambio de documentos entre AAPP no se considera RISP.

Quedan excluidos los documentos:

* con prohibiciones o limitaciones de acceso por la ley 19/2013.
* que afecten a la defensa nacional, seguridad del estado o protección
de la seguridad pública
* obtenidos por la Agencia Tributaria y la Seguridad Social
* con derechos de propiedad intelectual o industrial por parte de terceros
* producidos por instituciones educativas y de investigación
* de radiodifusión sonora o televisiva
* limitados por la protección de datos, a no ser que haya disociación
* realizados como colaboración público-privada mediante convenios

## Puesta a disposición

Tres modalidades de puesta a disposición de datos:

1. sin sujeción a condiciones
2. sujeta a condiciones establecidas en una licencia-tipo
3. acuerdos exclusivos

Las licencias-tipo han de ser las menos restrictivas posibles y preferiblemente
que dispongan de formato digital (ej: Creative Common).

Los datos deben estar en un formato procesable por máquinas y sus metadatos
cumplir el ENI (ver [NTI reutilización de recursos de información]({filename}04-ENI.md#reutilizacion-de-recursos-de-informacion)).

Para clasificar la calidad del formato de los datos se puede usar la
[escala de madurez de datos abiertos o modelo de las cinco estrellas de Tim Berners-Lee](https://datos.gob.es/es/noticia/cual-es-el-nivel-de-madurez-de-los-datos-abiertos-en-espana):

1. datos en cualquier formato (PDF, imágenes, etc) y con licencia abierta
2. datos estructurados (ej: tablas excel)
3. datos estructurados no propietarios (ej: CSV, XML, JSON, etc)
4. datos estructurados identificados por URIs (RDF)
5. datos enlazados: conjuntos de datos enlazados a otros conjuntos para proveer contexto

La ley prohíbe otorgar derechos exclusivos salvo que sean necesarios para proporcionar
un servicio público (revisable cada 3 años) o se trate de digitalización de recursos culturales
(10 años prorrogables cada 7).

## Tarifas

Las tarifas están limitadas a los costes marginales derivados de la producción,
puesta a disposición o difusión. Dichas tarifas deben ser públicas y transparentes,
y la formula de su calculo justificada.

Aún así se debe optar por la gratuidad por defecto.

Lo anterior no aplica en:

* organismos a los que se les exija generar ingresos para cubrir una parte
sustancial de presupuesto o de los costes de recogida, producción o difusión
* bibliotecas, universidades, museos y archivos

## Condiciones

Las condiciones básicas para la reutilización son:

* no desnaturalizar la información ni modificarla (incluídos los metadatos)
* citar la fuente de los datos y la fecha de última actualización
* en caso de datos de carácter personal:
    * indicar la finalidad de reutilización
    * prohibición de revertir la disociación (si la hay)

Las multas por incumplimiento son:

* infracciones **leves**: multa de 1.000 a 10.000 €:
    * no mencionar la fuente o última fecha de actualización
    * alteración leve de la información
    * incumplimiento leve de las condiciones de la licencia
* infracciones **graves**: multa de 10.001 a 50.000 €:
    * reutilizar la información para otro cometido al concedido o sin haber obtenido la licencia necesaria
    * alteración grave del contenido
    * incumplimiento grave de condiciones de la licencia
* infracciones **muy graves**: multa de 50.001 a 100.000 €:
    * desnaturalizar la información
    * alteración muy grave de su contenido

## Solicitudes de reutilización

Las solicitudes se dirigen al órgano en posesión de la información, identificando
los documentos que se solicita y los fines de la reutilización.

El órgano competente tiene 20 días para resolver la solicitud prorrogables a otros
20 en caso de dificultades (silencio administrativo = denegada).

## Protección de datos

La publicación de documentos que contienen datos personales debe:

* contar con el consentimiento de las personas afectadas
* anominizar o seudonimizar los datos personales
* disociar los datos personales (es decir, eliminarlos)

# Bibliografía

* PreparaTic27 - Pack1/031
