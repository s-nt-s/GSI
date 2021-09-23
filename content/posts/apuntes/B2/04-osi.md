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


# Bibliografía

* PreparaTic27 - Pack1/110
