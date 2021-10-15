---
title: Modelo OSI y TCP/IP
replace:
  "Segmento<br/>": '<a class="abbr wikipedia" href="https://es.wikipedia.org/wiki/Segmentaci%C3%B3n_de_paquetes">Segmento</a><br/>'
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
| 7 | Aplicación   | FTP, DNS, DHCP, HTTP(s), POP3, SNMP, SMTP, SSH, Telnet, TFTP, LDAP, XMPP |
| 6 | Presentación | ASCII, XML, AFP, TLS, ICA, LPP, NCP, NDR, Tox, XDR, X.25 PAD |
| 5 | Sesión       | ADSP, ASP, H.245, iSNS, L2F, L2TP, NetBIOS, PAP, PPTP, ONC/RPC, RTCP, SMPP, SCP, SOCKS, ZIP, SDP |
| 4 | Transporte   | **TCP**, **UDP**, ATP, CUDP, DCCP, FCP, IL-Protocol, MPTCP, NORM, RDP, RUDP, SCTP, SPX, SST, µTP |
| 3 | Red          | **IP** (IPsec, IPv4, IPv6), OSPF, IS-IS, ICMP, IGMP, CLNS, DDP, EGP, EIGRP, IPX, PIM, RIP |
| 2 | Enlace       | ARCnet, ARP, ATM, CDP, CAN, Econet, Ethernet, EAPS, FDDI, Frame Relay, HDLC, IEEE 802.2, IEEE 802.11 wireless LAN, I²C, LattisNet, LLDP, LocalTalk, MIL-STD-1553, MPLS, NDP, PPP, Profibus, SpaceWire, SMLT, IEEE 802.1aq, Spanning Tree Protocol, StarLan, Token Ring, UDLD, UNI/O, 1-Wire, USB, PCI Express |
| 1 | Física       | V.92, xDSL, IrDA, Firewire, EIA RS-232, EIA-422, EIA-423, RS-449, RS-485, DSL, ISDN, SONET/SDH, GSM |

Tabla 2: Protocolos según capa

## TCP

**TCP** es usado por aplicaciones como HTTP(s), POP3, SMTP, FTP, FTPES, SFTP, SSH etc.
Sus características son:

* garantiza que los datos serán entregados en su destino sin errores y en el mismo
orden en que se transmitieron (reordena los paquetes antes pasar los datos a la capa de aplicación)
* proporciona acuse de recibo (**ACK**)
* los dos puntos anteriores posibilitan que los routers (capa de red) solo tienen
que enviar los datos en forma de segmentos, sin preocuparse del monitoreo de datos
* permite el monitoreo del flujo de los datos y así evita la saturación de la red
* permite que los datos se formen en segmentos de longitud variada para *entregarlos* al protocolo IP
* permite multiplexar los datos, es decir, que la información que viene de diferentes fuentes (ej: aplicaciones) en la misma línea pueda circular simultáneamente
* la unidad de datos es el segmento TCP, el cual tiene una sobrecarga mínima de 20 bytes
* es un protocolo orientado a la conexión ya que:
    * el cliente y el servidor deben anunciarse y aceptar la conexión antes de comenzar a transmitir los datos
    * permite comenzar y finalizar la comunicación amablemente
    * se compone de las siguientes etapas:
        1. Establecimiento de conexión (3-way handshake)
        2. Transferencia de datos
        3. Fin de la conexión.

![](https://upload.wikimedia.org/wikipedia/commons/9/98/Tcp-handshake.svg)

Figura: 3-way handshake

### Cabecera Segmento TCP

| Octeto | Bit    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |
|-------:|-------:|---|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|  **0** |  **0** | Puerto origen                         |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<| Puerto destino                                  |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
|  **4** | **32** | Número de secuencia                                                                   |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
|  **8** | **64** | Nª de acuse de recibo (si ACK esta marcado)                                           |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
| **12** | **96** | Longitud de Cabecera |<|<|<| Resevado |<|<| <span class="vertical">NS</span> | <span class="vertical">CWR</span> | <span class="vertical">ECE</span> | <span class="vertical">URG</span> | <span class="vertical">ACK</span> | <span class="vertical">PSH</span> | <span class="vertical">RST</span> | <span class="vertical">SYN</span> | <span class="vertical">FIN</span> | Tamaño de ventana |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
| **16** |**128** | Checksum                              |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<| Puntero urgente (si URG esta marcado)           |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
| **20** |**160** | Opciones (si *Longitud de Cabecera* > 5, relleno con 0 al final si es necesario)      |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
|**...** |**...** | ^                                                                                     |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
| **60** |**480** | *esto ya no es cabecera, aquí - como tarde - ya empezarían los datos*                 |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|

Tabla 3: Cabecera de Segmento TCP <span class="cabecera_segmento"></span>

* **Número de secuencia**: dentifica el primer byte del campo de datos que enviá
el segmento, al primero se le llama ISN (Initial Sequence Number) y lo elige el servidor
* **Número ACK**: indica el próximo numero de secuencia que se esta dispuesto a recibir,
por lo tanto significa que el `número ACK - 1` es el número de secuencia del último
segmento recibido
* **Longitud de Cabecera**: necesario ya que el tamaño puede variar de
20 a 60 bytes en función de cuanta información se añada en el campo opciones.
El valor viene en *número de palabras de 32-bit*, es decir, 5 equivale a 160 bit o 20 bytes.
* **Resevado**: viene a `000` y se guarda para usos futuros
* **Campos de control**: son cada uno de 1 bit y se consideran marcados cuando están a `1`:
    * URG: hay datos urgentes y el campo urgent pointer indica la cantidad de datos urgentes que se encuentran en el segmento
    * ACK: solo viene a 0 en el primer mensaje para indicar que el campo ACK ha de ser ignorado
    * PSH: invoca la función push en el protocolo, la cual consiste en entregar a la aplicación todos los datos que están en la memoria intermedia de recepción sin esperar a completarla con datos adicionales
    * RST: hace un reset de la conexión (usado cuando hay algún problema, ej: paquetes perdidos)
    * SYN: resincroniza los números de secuencia
    * FIN: el transmisor ha acabado la conexión
* **Tamaño de ventana**: informa sobre cuantos bytes se esta dispuesto a recibir en
el paquete de respuesta
* **Puntero urgente**: indica (si URG=1) que los datos comprendidos desde el
primer byte hasta el indicado por este campo son urgentes y debería procesarse
lo antes posible
* **Opciones**: permite añadir campos a la cabecera para:
    * marcar con un timestamp el momento de la transmisión para monitorar los retrasos que experimentan los segmentos desde el origen hasta el destino
    * aumentar el tamaño de la ventana
    * indicar el MSS que el origen está preparado para recibir (se especifica durante el establecimiento de la conexión)

Nota: Que el número de secuencia *identifique el primer byte del campo de datos*
significa que si por ejemplo el número de secuencia de un paquete es el 12 y
contiene 3 bytes de datos, ese 12 identifica el 1º byte del los 3 y por lo tanto
el 2º byte sería el 13, el 3º byte el 14, y si todo va bien el paquete sería
respondido con otro paquete donde el ACK sería 15 ya que el último número de
secuencia del último byte recibido ha sido el 14.

## UDP

**UDP** es usado por aplicaciones como DHCP, BOOTP, DNS, NFS, RCP y de transmisión de audio
y vídeo en tiempo real. Sus caracteristicas son:

* no emplea ninguna sincronización entre el origen y el destino (no es *fiable*):
    * permite el envío de datagramas sin que se haya establecido previamente una conexión
    * no tiene confirmación ni control de flujo, por lo que los paquetes pueden adelantarse unos a otros
    * no hay confirmación de llegada, por lo tanto no se sabe si se han perdido datagramas
* trabaja con paquetes o datagramas enteros (no con bytes individuales como TCP) a los cuales solo se les añade una sobrecarga de 8 bytes
* solo añade multiplexado de aplicación y suma de verificación de la cabecera y la carga útil

Ya que tanto TCP como UDP circulan por la misma red, puede ocurrir que el aumento
del tráfico UDP dañe el correcto funcionamiento de las aplicaciones TCP.
Por defecto, TCP pasa a un segundo lugar para dejar a los datos en tiempo real
usar la mayor parte del ancho de banda. El problema es que ambos son importantes
para la mayor parte de las aplicaciones, por lo que encontrar el equilibrio entre
ambos es crucial.

### Cabecera Datagrama UDP

| Octeto | Bit    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |
|-------:|-------:|---|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|  **0** |  **0** | Puerto origen                         |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<| Puerto destino                                  |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
|  **4** | **32** | Longitud del Mensaje                  |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<| Checksum                                        |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
|  **8** | **64** | *esto ya no es cabecera, aquí ya empezarían los datos*                                |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|

Tabla 4: Datagrama UDP <span class="cabecera_segmento"></span>

* **Puerto origen**: es opcional siendo 0 el valor nulo
* **Checksum**:
    * es opcional en IPv4 y obligatorio en IPv6
    * se calcula con el datagrama completo más una pseudo-cabecera IP (IP origen y destino, protocolo y longitud del paquete UDP) rellenando con ceros hasta llegar a un multiplico de 16
* **Longitud del Mensaje**: longitud en bytes del datagrama UDP, incluyendo la cabecera UDP

## Puertos de red

Tanto TCP como UDP usan el concepto de número de **puerto** para identificar a las
aplicaciones emisoras y receptoras.

Hay 65536 puertos (16 bits) divididos en tres tipos de puertos:

1. `____0 - _1023` **bien conocidos**: asignados por la IANA y usados por el sistema o por procesos con privilegios.
Las aplicaciones que usan este tipo de puertos son ejecutadas como servidores y se quedan a la escucha de conexiones.
Ej: FTP (21), SSH (22), Telnet (23), SMTP (25) y HTTP (80)
2. `_1024 - 49151` **registrados**: para aplicaciones de usuario de forma temporal cuando conectan con los servidores, pero también pueden representar servicios que hayan sido registrados por un tercero
3. `49152 - 65535` **dinámicos/privados**: utilizados como puertos temporales, sobre todo por los clientes al comunicarse con los servidores.

Nota: una aplicación puede estar usando simultáneamente el mismo puerto para TCP y UDP
ya que técnicamente son dos puertos separados aunque tengan el mismo numero.

| UDP   | TCP   | Nombre | Descriptción |
|------:|------:|--------|--------------|
|       |     1 | tcpmux | Multiplexor TCP |
|       |     7 | echo   | Responde con eco a llamadas remotas  |
|       |    11 | systat | Servicio del sistema para listar los puertos conectados |
|       |    13 | daytime | Envía la fecha y hora actuales |
|       |    17 | qotd | Envía la cita del día |
|       |    10 | ftpS-data | FTPS  |
|       |    21 | ftp-data | FTP |
|       |    22 | ssh | SSH, scp, SFTP |
|       |    23 | telnet | Manejo remoto de equipo, inseguro |
|       |    25 | smtp | Protocolo Simple de Transferencia de Correo |
|       |    37 | time | Sincroniza hora y fecha |
|       |    42 | nameserver | Servicio de nombres de Internet |
|       |    43 | nickname | Servicio de directorio WHOIS |
|    53 |    53 | domain | Sistema de Nombres de Dominio, por ejemplo BIND |
|       |    63 | whois++ | Servicios extendidos de WHOIS |
|    67 |       | bootps | BOOTP servidor, también usado por DHCP |
|    68 |       | bootpc | BOOTP cliente, también usado por DHCP |
|    69 |       | tftp | TFTP |
|       |    70 | gopher | Gopher |
|       |    80 | http | HTTP |
|       |    88 | kerberos | Kerberos Agente de autenticación |
|       |   101 | hostname | Servicios de nombres de host en máquinas SRI-NIC |
|       |   107 | rtelnet | Telnet remoto |
|       |   109 | pop2 | POP2 |
|       |   110 | pop3 | POP3 |
|       |   115 | sftp | [SFTP (Simple FTP)](https://en.wikipedia.org/wiki/File_Transfer_Protocol#Simple_File_Transfer_Protocol), con confundir con SFTP (SSH File Transfer Protocol) |
|       |   119 | nntp | NNTP usado en los grupos de noticias de usenet  |
|   123 |       | ntp | NTP Protocolo de sincronización de tiempo |
|   137 |       | netbios-ns | NetBIOS Servicio de nombres |
|   138 |       | netbios-dgm | NetBIOS Servicio de envío de datagramas |
|       |   139 | netbios-ssn | NetBIOS Servicio de sesiones |
|       |   143 | imap| IMAP4 Internet Message Access Protocol |
|   161 |       | snmp | SNMP Simple Network Management Protocol |
|   162 |       | snmptrap | SNMP-trap |
|       |   177 | xdmcp | XDMCP Protocolo de gestión de displays en X11 |
|       |   194 | irc | Internet Relay Chat  |
|       |   199 | smux | SNMP UNIX Multiplexer |
|       |   209 | qmtp | Protocolo de transferencia rápida de correo (QMTP) |
|       |   220 | imap3 | INAP3 |
|       |   389 | ldap | LDAP Protocolo de acceso ligero a Directorios  |
|       |   443 | https | HTTPS/SSL |
|       |   445 | microsoft-ds | Microsoft-DS (Active Directory) |
|       |   465 | smtps | SMTP Sobre SSL |
|   500 |       |  | IPSec ISAKMP, Autoridad de Seguridad Local  |
|   514 |       |  | syslog usado para logs del sistema |
|   520 |       | rip | RIP Protocolo de Información de Enrutamiento |
|   521 |       | ripng | RIP para IPv6 |
|       |   587 | smtp | SMTP sobre TLS |
|       |   631 |  | CUPS sistema de impresión de Unix |
|       |   993 | imaps | IMAP4 sobre SSL |
|       |   995 |  | POP3 sobre SSL |
|       |  1080 |  | SOCKS Proxy |
|  1194 |       |  | OpenVPN Puerto por defecto en NAS Synology y QNAP |
|       |  1352 |  | IBM Lotus Notes/Domino RCP |
|       |  1433 |  | Microsoft-SQL-Server |
|       |  1434 |  | Microsoft-SQL-Monitor |
|       |  1494 |  | Citrix MetaFrame Cliente ICA |
|       |  1521 |  | Oracle puerto de escucha por defecto |
|  1701 |   |  | Enrutamiento y Acceso Remoto para VPN con L2TP |
|  1720 |   |  | H.323 |
|       |  1723 |  | Enrutamiento y Acceso Remoto para VPN con PPTP.  |
|       |  1761 |  | Novell Zenworks Remote Control utility  |
|       |  1883 |  | MQTT protocol |
|       |  2049 |  | NFS Archivos del sistema de red |
|       |  2082 |  | cPanel puerto por defecto  |
|       |  2083 |  | cPanel puerto por defecto sobre SSL  |
|  2427 |   |  | Cisco MGCP  |
|       |  3128 |  | HTTP usado por web caches y por defecto en Squid cache  |
|       |  3306 |  | MySQL sistema de gestión de bases de datos  |
|       |  3389 |  | RDP (Remote Desktop Protocol) Terminal Server  |
|       |  3396 |  | Novell agente de impresión NDPS  |
|       |  3690 |  | Subversion  |
|       |  4200 |  | Angular, puerto por defecto  |
|       |  5000 |  | Universal plug-and-play |
|  5060 |   |  | Session Initiation Protocol (SIP) |
|       |  5222 |  | Jabber/XMPP conexión de cliente |
|       |  5223 |  | Jabber/XMPP puerto por defecto para conexiones de cliente SSL |
|       |  5269 |  | Jabber/XMPP conexión de servidor |
|       |  5432 |  | PostgreSQL sistema de gestión de bases de datos  |
|       |  5400 |  | VNC protocolo de escritorio remoto (usado sobre HTTP)  |
|       |  5500 |  | ^ |
|       |  5600 |  | ^ |
|       |  5700 |  | ^ |
|       |  5800 |  | ^ |
|       |  5900 |  | VNC protocolo de escritorio remoto (conexión normal)  |
|       |  6000 |  | X11 usado para X-windows  |
|       |  6667 |  | IRC |
|       |  6881 |  | BitTorrent puerto por defecto  |
|       |  6969 |  | BitTorrent puerto de tracker  |
|  7100 |  7100 |  | Servidor de Fuentes X11  |
|       |  8080 |  | HTTP HTTP-ALT, Tomcat lo usa como puerto por defecto.  |
|       |  8118 |  | privoxy  |
|       | 10000 |  | Webmin |

Tabla 5: Algunos puertos de red

## IP

IP es un protocolo de uso bidireccional y no orientado a conexión que transfiere
paquetes conmutados.

IP no puede garantizar la entrega de los paquetes pero siempre intentará usar
la mejor ruta conocida para el envió (best-effort delivery).

### Cabecera Datagrama IPv4

| Octeto | Bit    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |
|-------:|-------:|---|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|  **0** |  **0** | Versión|<|<|<|Longitud de Cabecera|<|<|<|Tipo de Servicio|<|<|<|<|<|<|<| Longitud Total                               |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
|  **4** | **32** | Identificador                         |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<| Flags    |<|<| Posición del Fragmento                 |<|<|<|<|<|<|<|<|<|<|<|<|
|  **8** | **64** | Tiempo de vida    |<|<|<|<|<|<| Protocolo           |<|<|<|<|<|<|<|<| Checksum                                        |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
| **12** | **96** | Dirección IP de Origen                                                                |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
| **16** |**128** | Dirección IP de Destino                                                               |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
| **20** |**160** | Opciones (si *Longitud de Cabecera* > 5, relleno con 0 al final si es necesario)      |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
|**...** |**...** | ^                                                                                     |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
| **60** |**480** | *esto ya no es cabecera, aquí - como tarde - ya empezarían los datos*                 |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|

Tabla 6: [Datagrama IPv4](https://es.wikipedia.org/wiki/Cabecera_IP) <span class="cabecera_segmento"></span>

* **Versión**: indica si es IPv4 (0100) o IPv6 (0110)
* **Longitud de Cabecera**: necesario ya que el tamaño puede variar de
20 a 60 bytes en función de cuanta información se añada en el campo opciones.
El valor viene en *número de palabras de 32-bit*, es decir, 5 equivale a 160 bit o 20 bytes.
* **Tipo de Servicio** (ToS o DSCP): indica una serie de parámetros sobre la calidad de servicio deseada
    * Existe la posibilidad de que los últimos dos bits sean ocupados por el campo opcional
    [ECN](https://en.wikipedia.org/wiki/Explicit_Congestion_Notification "Explicit Congestion Notification"){.abbr}
    (ver [IPv4 Header](https://en.wikipedia.org/wiki/IPv4#Header))
* **Longitud Total** (Total Length): longitud en bytes del datagrama IP, incluyendo la cabecera IP.
El tamaño mínimo normalmente es de 576 octetos (64 de cabeceras y 512 de datos)
* **Identificador** (Identification): único por `datagrama-origen-destino-tipo_de_protocolo` y se
utiliza para en caso de fragmentación poder distinguir los fragmentos de un datagrama de otro
* **Flags**: usados para especificar valores relativos a la fragmentación de paquetes:
    * bit 0 = 0 (reservado)
    * bit 1 (<abbr class="abbr" title="Don't Fragment">DF</abbr>): 0 = divisible, 1 = no divisible
    * bit 2 (<abbr class="abbr" title="More Fragments">MF</abbr>): 0 = último fragmento, 1 = fragmento intermedio
* **Posición del Fragmento** (Fragment Offset): marca la posición dentro del datagrama original, empezando por 0
* **Tiempo de vida**: (TTL) indica el número máximo de enrutadores que el paquete puede atravesar
* **Protocolo** (Protocol): un [número que indica el protocolo de la capa superior](https://es.wikipedia.org/wiki/Anexo:N%C3%BAmeros_de_protocolo_IP)
* **Relleno**: se usa para garantizar que el tamaño de la cabecera es múltiplo de 32

### Cabecera Datagrama IPv6

| Octeto | Bit    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |
|-------:|-------:|---|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|  **0** |  **0** | Versión |<|<|<| Clase de tráfico       |<|<|<|<|<|<|<| Etiqueta de flujo                                      |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
|  **4** | **32** | Longitud del campo de datos           |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<| Cabecera siguiente      |<|<|<|<|<|<|<| Límite de saltos        |<|<|<|<|<|<|<|
|  **8** | **64** | Dirección IP de Origen                                                                |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
| **12** | **96** | ^                                                                                     |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
| **16** |**128** | ^                                                                                     |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
| **20** |**160** | ^                                                                                     |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
| **24** |**192** | Dirección IP de Destino                                                               |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
| **28** |**224** | ^                                                                                     |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
| **32** |**256** | ^                                                                                     |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
| **36** |**288** | ^                                                                                     |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|
| **40** |**320** | *esto ya no es cabecera, aquí ya empezarían los datos*                                |<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|<|

Tabla 7: [Datagrama IPv6](https://es.wikipedia.org/wiki/IPv6#Cabecera_fija) <span class="cabecera_segmento"></span>

* **Versión**: indica si es IPv4 (0100) o IPv6 (0110)
* **Clase de Tráfico** (Traffic Class): también denominado Prioridad o simplemente Clase,
indica una serie de parámetros sobre la calidad de servicio deseada (equivalente a ToS en IPv4)
* **Etiqueta de Flujo** (Flow Label): para permitir tráficos con requisitos de tiempo real
* **Longitud total de carga útil** (Payload Length): es la longitud de los propios datos (incluyendo cabeceras de extensión), y puede ser de hasta 65.536 bytes.
* **Siguiente cabecera** (Next Header): ya no se usan cabeceras de longitud variable, si no que se encadenan sucesivas cabeceras
    * por ello desaparece el campo opciones
    * en muchos casos no es procesado por los encaminadores, sino tan sólo extremo a extremo
* **Límite de saltos** (Hop Limit): indica el número máximo de enrutadores que el paquete puede atravesar (equivalente a TTL en IPv4)
* Campos de IPv4 que ya no son necesarios:
    * *Fragment Offset* y *Identification* desaparecen porque ya que la fragmentación (si es necesaria)
    solo se hace de extremo a extremo y no por encaminadores intermedios
    * *Options* desaparece porque *Next Header* permite añadir encadenar
    [cabeceras de extensión](https://es.wikipedia.org/wiki/IPv6#Cabeceras_de_extensi%C3%B3n)

## Direcciones IPv4

Son direcciones de 32 bits (2³² direcciones posibles) organizadas en cinco clases
(A, B, C, D y E).

| Clase | Bits<br/>Iniciales | Intervalo       | Mascara de red   | CIDR  | broadcast       |
|------:|:-------------------|----------------:|-----------------:|------:|----------------:|
|     A |                `0` |   `0-127.*.*.*` |      `255.0.0.0` |  `/8` | `*.255.255.255` |
|     B |               `10` | `128-191.*.*.*` |    `255.255.0.0` | `/16` |   `*.*.255.255` |
|     C |              `110` | `192-223.*.*.*` |  `255.255.255.0` | `/24` |     `*.*.*.255` |
|     D |             `1110` | `224-239.*.*.*` | *direcciones para multicast* | < | < |
|     E |             `1111` | `240-255.*.*.*` | *direcciones para uso experimental* | < | < |

Tabla 8: [Clases IPv4](https://en.wikipedia.org/wiki/Classful_network#Classful_addressing_definition)

1. la dirección con los bit de host a 0 identifica la red
2. la dirección con los bit de host a 1 es la dirección broadcast y sirve para
enviar paquetes a todas los hots de esa red
3. de la clase A hay que descartar:
    * la dirección `0.0.0.0` que esta reservada por la IANA para identificación local
    * las direcciones `127.*.*.*` porque se usan para loopback
4. por lo tanto en cada clase hay `2^n` redes (siendo `n` el número de bits dedicados
a la red que no están fijos) y `(2^h)-2` host (siendo `h` el número de bits dedicados al host):
    * A: 128 redes (2⁽⁸⁻¹⁾) y 16.777.214 hosts (2²⁴-2) (a los que hay que descartar las IPs `0.0.0.0` y `127.*.*.*`)
    * B: 16.384 redes (2⁽¹⁶⁻²⁾) y 65.534 hosts (2¹⁶-2)
    * C: 2.097.152 redes (2⁽²⁴⁻³⁾) y 254 hosts (2⁸-2)

| CIDR           | Descripción |
|---------------:|-------------|
|    10.0.0.0/8  | Utilizado para las comunicaciones locales dentro de una red privada |
|  172.16.0.0/12 | ^ |
| 192.168.0.0/16 | ^ |
|     0.0.0.0/8  | Red actual​ (solo válido como dirección de origen) |
|   127.0.0.0/8  | Direcciones de loopback |
| 169.254.0.0/16 | Direcciones de enlace local cuando no se puede conseguir una IP de otra manera (por ej con DHCP) |

Table 9: Algunas [direcciones IPv4 especiales](https://es.wikipedia.org/wiki/IPv4#Direcciones_de_uso_especial)

## [Direcciones IPv6](https://es.wikipedia.org/wiki/Direcci%C3%B3n_IPv6)

Son direcciones de 128 bits (2¹²⁸ direcciones posibles) que se representan en ocho
bloques de 16 bits en números hexadecimales separados por el caracter `:`.

Para abreviar se pueden eliminar los ceros a la izquierda, o incluso comprimir
todos los conjuntos de ceros consecutivos con `::`, de manera que las siguientes
IPs son la misma:

* `2a01:0048:0000:0000:0000:0000:0000:0000`
* `2a01:48:0:0:0:0:0:0`
* `2a01:48::`

Hay tres tipos de IPs según su direccionamiento y encaminamiento:

* **unicast**: identifica un único interfaz de red
* **anycast**: identifica un grupo de interfaces (normalmente de nodos diferentes):
    * Los paquetes enviados a una dirección anycast solo llega a uno de los miembros
    (típicamente el más cercano)
    * las direcciones anycast tienen el mismo formato que las unicast, simplemente
    son direcciones que están en varios puntos de la red
* **multicast**: identifica un grupo de interfaces (normalmente de nodos diferentes):
    * un paquete enviado a una dirección multicast es entregado a todos los miembros

| 48b o más       | 16b o menos | 64b                  |
|:---------------:|:-----------:|:--------------------:|
| routing prefix  | subnet id   | interface identifier |

Tabla: IPv6 unicast/anycast (network prefix = routing prefix + subnet id) <span class="tb_ipv6 ipv6_unicast"></span>

| 10b    | 54b          | 64b                  |
|:------:|:------------:|:--------------------:|
| prefix | ceros        | interface identifier |

Tabla: IPv6 enlace-local (fe80::/10, prefix = 1111111010) <span class="tb_ipv6 ipv6_enlace_local"></span>

| 8b     | 4b             | 4b             | 112b     |
|:------:|:--------------:|:--------------:|:--------:|
| prefix | flags<br/>0RPT | scope<br/>XXXX | group ID |

Tabla: IPv6 unicast (ff00::/8, prefix = 11111111) <span class="tb_ipv6 ipv6_multicast"></span>

Nótese que el tipo broadcast no existe. Se puede conseguir el mismo
efecto enviando un paquete al dirección multicast del grupo all-nodes del enlace-local
ff02::1. Sin embargo no se recomienda usar el grupo all-nodes.

También se pude usar una notación equivalente a la CIDR en IPv4 para denotar
grupos de IPs, de manera que `2a01:48::/32` son todas las IPs entre
`2a01:0048:0000:0000:0000:0000:0000:0000` y `2a01:0048:ffff:ffff:ffff:ffff:ffff:ffff`.

| IP o Prefijo      | Descripción |
|------------------:|-------------|
|            ::/128 | Dirección con todo ceros se utiliza para indicar la ausencia de dirección, y no se asigna ningún nodo |
|           ::1/128 | dirección de loopback, equivalente a 127.0.0.1 de IPv4 |
|      ::X.X.X.X/96 | Dirección IPv4 compatible (DEPRECADO) |
| ::ffff:X.X.X.X/96 | Dirección IPv4 mapeada. Permite que las aplicaciones de IPv6 se comuniquen directamente con las aplicaciones de IPv4 |
|         fe80::/10 | Prefijo de enlace local, específica que la dirección solamente es válida en el enlace físico local |
|          fc00::/7 | Prefijo de [dirección local única](https://es.wikipedia.org/wiki/Unique_Local_Address) (dirección privada). Se divide en fc00::/8 (aún sin uso) y fd00::/8 |
|          ff00::/8 | Prefijo de multicast |

Tabla 10: [Tipos de direcciones IPv6](https://es.wikipedia.org/wiki/IPv6#Identificaci%C3%B3n_de_los_tipos_de_direcciones)

# Bibliografía

* PreparaTic27 - Pack1/110
* PreparaTic27 - Pack1/114
* [redeszone.net - ¿Qué protocolo es mejor?: TCP vs UDP, descubre cuándo utilizar cada uno](https://www.redeszone.net/tutoriales/internet/tcp-udp-caracteristicas-uso-diferencias/)
* [youtube.com - Curso de Redes. 10.7. Protocolo TCP: números de secuencia](https://www.youtube.com/watch?v=drBwqN038vM)
* [cv.uoc.edu - Protocolos del nivel de transporte ](http://cv.uoc.edu/UOC/a/moduls/90/90_329/web/main/m2/v4_0.html)
* [cv.uoc.edu - El protocolo UDP](http://cv.uoc.edu/UOC/a/moduls/90/90_329/web/main/m2/v4_1.html)
* [cv.uoc.edu - Formato del segmento TCP](http://cv.uoc.edu/UOC/a/moduls/90/90_329/web/main/m2/v4_2_2.html)
* [ipv6go.net - Cabecera IPv6](http://www.ipv6go.net/cabecera_ipv6.php)
* [ramonmillan.com - El protocolo IPv6 (II)](https://www.ramonmillan.com/tutoriales/ipv6_parte2.php)
* [docs.oracle.com - Descripción general de las direcciones IPv6](https://docs.oracle.com/cd/E19957-01/820-2981/ipv6-overview-10/index.html)
* [ipv6.mx - Fundamentos de IPv6](http://www.ipv6.mx/index.php/informacion/fundamentos/ipv6)
* [docs.oracle.com - Using IPv4-Compatible Address Formats](https://docs.oracle.com/cd/E19683-01/816-5250/transition-4/index.html)
