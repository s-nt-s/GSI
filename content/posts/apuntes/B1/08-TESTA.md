---
title: Red SARA y red TESTA
---

# Conceptos básicos

**SARA**: Conjunto de infraestructuras de comunicaciones y servicios básicos que
conecta todas las redes de las AAPP y las instituciones Europeas.

**TESTA**: proporciona una red de backbone europea para el intercambio de datos entre
administraciones públicas.

**ISA²**: ampliación del programa europeo ISA para fomentar la interoperabilidad
a escala internacional y nacional.

**Contexto normativo**:

* Ley 40/2015, artículo 155.3
* Real Decreto 4/2010, artículo 13 y 14
* BOE-A-2011-13173, NTI requisitos de conexión a la red de comunicaciones de las AP
* Real Decreto 806/2014, artículo 10

# Red SARA

Ver [ENI - NTI Requisitos de conexión a la Red de comunicaciones de las Administraciones Públicas españolas]({filename}04-ENI.md#requisitos-de-conexion-a-la-red-de-comunicaciones-de-las-administraciones-publicas-espanolas).

# Red TESTA

La Red TESTA usa rangos de direcciones IP asignados por RIPE (`62.62.0.0`),
no encaminables por Internet, y administrados por el operador de TESTA en nombre
de la Comisión Europea.

La red TESA usa la red troncal EuroDomain a la que se accede desde una EuroGates.

Para la red TESTA, la red SARA es la *National Network* de España, con un punto
único de acceso al EuroDomain.

Esta red ha tenido varias generaciones:

* TESTA (1996–2000)
    * FR -Hub/Spokes
    * Sectoral apps
* TESTA-II (2000–2006)
    * IP VPN – Any2Any
    * National Networks
* sTESTA (2006–2013)
    * Security EU Restricted
    * Dedicated Support
    * Central Services
* TESTA-NG (2013-...)
    * Multiple Cloud
    * Secure internet
    * Additional services
    * PKI, Video bridge, time stamping

La red **sTESTA** surge para (además de servir para las aplicaciones de IDABC) añadir
las siguientes funcionalidades:

* Intercambio de documentación oficial clasificada
* Transportar información militar altamente clasificada
* Cumpliendo unos parámetros de nivel de servicio muy elevados, converger con:
    * diversas redes privadas existentes sobre el mismo espacio geográfico
    * la extranet del Consejo de la UE, gracias a la participación conjunta de la
    Comisión Europea y de la Secretaría General del Consejo de la UE en la
    contratación y gestión de sTESTA
* Servir de base para el SIS

Para el transporte de información clasificada, esta puede estar previamente
encriptada o usar los mecanismos de encriptación hardware que ofrece el EuroGate.

La red sTESTA es usada por:

* EEMM y AAPP: Los ciudadanos y las empresas están fuera del alcance aunque
se benefician indirectamente debido a la protección de los datos personales en
la red
* Aplicaciones sectoriales, ej: OLAF, Eurostat, DG ENV, DG TRADE
* Instituciones europeas y las agencias europeas, ej: Europol, DG HOME (para
para la implementación de las redes SIS II y VIS II)
* La Secretaría General del Consejo para implementar la red FADO, la extranet del
Consejo y las redes de cortesía
* en proyectos no comunitarios por los EEMM y organizaciones en el contexto
del tratado de Prüm y FIU.NET (blanqueo de dinero)

La evolución a **TESTA-NG** viene motivada para:

* Facilitar la cooperación entre las administraciones públicas
* Crear interoperabilidad a nivel de la UE a través de una solución genérica
* Consolidar las redes paralelas existentes a través de una estructura flexible y confiable
* Provisión de un catálogo genérico de servicios extendido (herramientas de colaboración, PKI,
correo seguro, etc)

El enfoque de sTESTA y TESTA-NG es colaborativo. Se construye sobre las redes
administraciones nacionales, regionales o locales a través de una red transeuropea.
Cada dominio interconectado debe cumplir requisitos de seguridad, rendimiento y
organizativos para acceder a la red sTESTA.

La infraestructura está gestionada por SOC y los servicios genéricos se proporcionan
a través de un dominio altamente securizado.

Tanto sTESTA como TESTA-NG están basadas en una infraestructura resiliente
MPLS encriptada mediante IPsec.

La resiliencia se consigue con backups de manera que se pueda garantizar la continuidad
en caso de desastre. Durante una migración se crea un bridge resiliente entre
los dos entornos para que la migración tenga lugar de manera gradual.

# Bibliografía

* PreparaTic27 - Pack1/119
