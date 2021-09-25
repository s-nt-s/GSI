---
title: Modelo OSI y TCP/IP
status: draft
replace:
  "Segmento": '<a class="abbr wikipedia" href="https://es.wikipedia.org/wiki/Segmentaci%C3%B3n_de_paquetes">Segmento</a>'
  "Trama": '<a class="abbr wikipedia" href="https://es.wikipedia.org/wiki/Trama_de_red">Trama</a>'
---

# Conceptos básicos

**Modelo OSI** modelo de referencia para protocolos de red.
No es la definición de una topología ni un modelo de red en sí mismo.
Tampoco especifica ni define los protocolos que se utilizan en la comunicación,
ya que estos se implementa de forma independiente a este modelo.
El modelo OSI simplemente define la funcionalidad esperada para conseguir un estándar.

**Modelo TCP/IP**: conjunto de protocolos de red (pila de protocolos TCP/IP)
que se ha convertido en un estándar de facto aunque no coincide exactamente con el modelo OSI.

**Capas**: la base de estos modelos es su división en diferentes capas o niveles
de abstracción. Cada uno de estas capas concentra funciones específicas en cada
nivel de operación, lo que hace posible la intercomunicación de protocolos
distintos.

# Equivalencia modelo OSI - modelo TCP/IP

| # | Capas TCP/IP    | # | Capas OSI<br/>(FERTSPA) | PDU             | Función |
|--:|-----------------|--:|-------------------------|-----------------|---------|
| 4 | Aplicación      | 7 | Aplicación              | Datos           | APIs de alto nivel<br/>(ej: compartir recursos, acceso remoto a archivos) |
| ^ | ^               | 6 | Presentación            | ^               | Traducción de datos entre un servicio de red y una aplicación<br/>(ej: codificación de caracteres, compresión de datos, cifrado y descifrado) |
| ^ | ^               | 5 | Sesión                  | ^               | Manejo de sesiones de comunicación<br/>(ej: intercambio de información en forma de múltiples transmisiones hacia ambos lados entre dos nodos) |
| 3 | Transporte      | 4 | Transporte              | Segmento<br/>Datagrama | Transporte confiable y control del flujo a través de la red<br/>(ej: segmentación, ACK, multiplexación) |
| 2 | Internet        | 3 | Red                     | Paquete         | Estructura y manejo de una red multinodo<br/>(ej: direccionamiento, ruteo, control de tráfico) |
| 1 | Acceso al medio | 2 | Enlace de datos         | Trama           | Direccionamiento físico y procedimientos de acceso a medios  |
| ^ | ^               | 1 | Física                  | Bit<br/>Baudios | Especificaciones eléctricas y físicas de los dispositivo |

Tabla 1: Capas del modelo OSI y modelo TCP/IP

![](https://upload.wikimedia.org/wikipedia/commons/f/fc/PDUs.PNG)

Figura 1: Viaje de los datos a través del modelo OSI

# Protocolos

| # | Capa         | Protocolos |
|--:|--------------|------------|
| 7 | Aplicación   | FTP, DNS, DHCP, HTTP(s), POP3, SMTP, SSH, Telnet, TFTP, LDAP, XMPP |
| 6 | Presentación | ASCII, XML, AFP, TLS, ICA, LPP, NCP, NDR, Tox, XDR, X.25 PAD |
| 5 | Sesión       | ADSP, ASP, H.245, iSNS, L2F, L2TP, NetBIOS, PAP, PPTP, ONC/RPC, RTCP, SMPP, SCP, SOCKS, ZIP, SDP |
| 4 | Transporte   | **TCP**, **UDP**, ATP, CUDP, DCCP, FCP, IL-Protocol, MPTCP, NORM, RDP, RUDP, SCTP, SPX, SST, µTP |
| 3 | Red          | **IP** (IPsec, IPv4, IPv6), OSPF, IS-IS, ICMP, IGMP, CLNS, DDP, EGP, EIGRP, IPX, PIM, RIP |
| 2 | Enlace       | ARCnet, ATM, CDP, CAN, Econet, Ethernet, EAPS, FDDI, Frame Relay, HDLC, IEEE 802.2, IEEE 802.11 wireless LAN, I²C, LattisNet, LLDP, LocalTalk, MIL-STD-1553, MPLS, NDP, PPP, Profibus, SpaceWire, SMLT, IEEE 802.1aq, Spanning Tree Protocol, StarLan, Token Ring, UDLD, UNI/O, 1-Wire, USB, PCI Express |
| 1 | Fisica       | V.92, xDSL, IrDA, Firewire, EIA RS-232, EIA-422, EIA-423, RS-449, RS-485, DSL, ISDN, SONET/SDH, GSM |

Tabla 2: Protocolos según capa

## TCP y UDP

TCP y UPD son los principales protocolos de transporte de la pila de protocolos TCP/IP.

**TCP** es usado por aplicaciones como HTTP(s), POP3, SMTP, FTP, FTPES, SFTP, SSH etc.
Sus características son:

* garantiza que los datos serán entregados en su destino sin errores y en el mismo
orden en que se transmitieron (reordena los paquetes antes pasar los datos a la capa de aplicación)
* proporciona acuse de recibo (**ACK**)
* los dos puntos anteriores posibilitan que los routers (capa de red) solo tienen
que enviar los datos en forma de segmentos, sin preocuparse del monitoreo de datos
* usa el concepto de número de **puerto** para identificar a las aplicaciones emisoras y receptoras. Hay 65536 puertos (16 bits) divididos en tres tipos de puertos:
    1. `____0 - _1023` **bien conocidos**: asignados por la IANA y usados por el sistema o por procesos con privilegios.
    Las aplicaciones que usan este tipo de puertos son ejecutadas como servidores y se quedan a la escucha de conexiones.
    Ej: FTP (21), SSH (22), Telnet (23), SMTP (25) y HTTP (80)
    2. `_1024 - 49151` **registrados**: para aplicaciones de usuario de forma temporal cuando conectan con los servidores, pero también pueden representar servicios que hayan sido registrados por un tercero
    3. `49152 - 65535` **dinámicos/privados**: utilizados como puertos temporales, sobre todo por los clientes al comunicarse con los servidores.
* permite el monitoreo del flujo de los datos y así evita la saturación de la red
* permite que los datos se formen en segmentos de longitud variada para *entregarlos* al protocolo IP
* permite multiplexar los datos, es decir, que la información que viene de diferentes fuentes (ej: aplicaciones) en la misma línea pueda circular simultáneamente
* la unidad de datos es el segmento TCP, el cual tiene una sobrecarga de 20 bytes
* es un protocolo orientad a la conexión ya que:
    * el cliente y el servidor deben anunciarse y aceptar la conexión antes de comenzar a transmitir los datos
    * permite comenzar y finalizar la comunicación amablemente
    * se compone de las siguientes etapas:
        1. Establecimiento de conexión (3-way handshake)
        2. Transferencia de datos
        3. Fin de la conexión.

**UDP** es usado por aplicaciones como DHCP, BOOTP, DNS, NFS, RCP y de transmisión de audio
y vídeo en tiempo real. Sus caracteristicas son:

* no emplea ninguna sincronización entre el origen y el destino (no es *fiable*):
    * permite el envío de datagramas sin que se haya establecido previamente una conexión
    * no tiene confirmación ni control de flujo, por lo que los paquetes pueden adelantarse unos a otros
    * no hay confirmación de llegada, por lo tanto no se sabe si se han perdido datagramas
* trabaja con paquetes o datagramas enteros (no con bytes individuales como TCP) a los cuales solo se les añade una sobrecarga de 8 bytes
* usa el mismo sistema de puertos que TCP

Ya que tanto TCP como UDP circulan por la misma red, puede ocurrir que el aumento
del tráfico UDP dañe el correcto funcionamiento de las aplicaciones TCP.
Por defecto, TCP pasa a un segundo lugar para dejar a los datos en tiempo real
usar la mayor parte del ancho de banda. El problema es que ambos son importantes
para la mayor parte de las aplicaciones, por lo que encontrar el equilibrio entre
ambos es crucial. 

# Bibliografía

* PreparaTic27 - Pack1/110
* [redeszone.net - ¿Qué protocolo es mejor?: TCP vs UDP, descubre cuándo utilizar cada uno](https://www.redeszone.net/tutoriales/internet/tcp-udp-caracteristicas-uso-diferencias/)
