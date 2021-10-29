---
title: Catálogo de servicios comunes
summary: "Fuente: [PAe - Catálogo de servicios](https://www.administracionelectronica.gob.es/pae_Home/pae_Estrategias/Racionaliza_y_Comparte/catalogo-servicios-admon-digital.html)"
version: { "XLSX":"https://www.administracionelectronica.gob.es/pae_Home/dam/jcr:615a99ea-33ef-42e8-bdee-6b17acec6a11/Soluciones-SGAD-2018.xlsx", "PDF":"https://www.administracionelectronica.gob.es/pae_Home/dam/jcr:736d93af-5aef-457c-bad8-f5496ffa1734/Catalogo-servicios-administracion-digital-version-2018.pdf", "ODS":"https://www.administracionelectronica.gob.es/pae_Home/dam/jcr:7a978076-50de-4e2b-b8e1-742691d6f510/Soluciones-SGAD-2018.ods" }
replace:
  "☑": '<abbr class="nou comun" title="Servicio declarado como compartido">☑</abbr>'
  "☐": '<abbr class="nou nocom" title="Servicio NO declarado como compartido">☐</abbr>'
---

<script>
    function getBloque(selector) {
        var bloque = [];
        document.querySelectorAll(selector).forEach(function(e) {
            let p=e.parentNode;
            bloque.push(p);
            while (p.nextElementSibling && p.nextElementSibling.tagName=="P" && p.nextElementSibling.querySelector("abbr.nou")==null) {
                p = p.nextElementSibling;
                bloque.push(p);
            }
        });
        return bloque;
    }
    function onlyComun() {
        const hide = document.getElementById("comun").checked;
        getBloque("abbr.nocom").forEach(function(e) {
            if (hide) e.setAttribute("style", "display: none;");
            else e.removeAttribute("style");
        });
    }
</script>

<input type="checkbox" id="comun" onclick="onlyComun(this)"/> <label for="comun">Ver solo servicios declarados como compartidos</label>

# Administración digital y servicios al ciudadano

Soluciones dirigidas al impulso de la administración digital y ofrecer servicios digitales a ciudadanos

## Identidad digital o firma electrónica

☐ **[CL@VE](http://administracionelectronica.gob.es/ctt/clave)**: Cl@ve es la plataforma común del Sector Público Administrativo Estatal para la identificación, autenticación y firma electrónica mediante el uso de claves concertadas. Su utilización está abierta a todas las AAPP.

Ambito: AAPP || Organismo: SGAD, AEAT, Seg-Social, Policía

☐ **[Cl@ve Firma](https://administracionelectronica.gob.es/ctt/clavefirma)**: Cl@ve Firma es la plataforma de firma electrónica basada en certificados centralizados para las AAPP.

Ambito: AAPP || Organismo: SGAD

☑ **[Plataforma @firma](http://administracionelectronica.gob.es/ctt/afirma)**: Es una plataforma de validación y firma electrónica multi-PKI, que se pone a disposición de las AAPP, proporcionando servicios para implementar la autenticación y firma electrónica avanzada de una forma rápida y efectiva.

Ambito: AAPP || Organismo: SGAD

☐ **[TS@](http://administracionelectronica.gob.es/ctt/tsa)**: Es una Autoridad de Sellado de Tiempo puesta a disposición de todas las AAPP con el objetivo de ofrecer los servicios de sellado, validación y resellado de sellos de tiempo.

Ambito: AAPP || Organismo: SGAD

☐ **[VALIDE](http://administracionelectronica.gob.es/ctt/valide)**: Servicio online que las AAPP pueden ofrecer a los ciudadanos para la validación de certificados, y verificación y generación de firmas electrónicas.

Ambito: AAPP y Ciudadanos || Organismo: SGAD

☐ **[Cliente @firma](http://administracionelectronica.gob.es/ctt/clienteafirma)**: Es una herramienta  de Firma Electrónica que puede ser facilitada al ciudadano desde cualquier servicio de administración electrónica para que el ciudadano realice las operaciones de autenticación y firma electrónica.

Ambito: AAPP || Organismo: SGAD

☐ **[e-VISOR](http://administracionelectronica.gob.es/ctt/evisor)**: Aplicación web que permite la generación de informes y justificantes de firma electrónica en formato PDF u ODF que cuando se firman con sello electrónico o se les añade un CSV se convierten en copias auténticas.

Ambito: AAPP || Organismo: SGAD

☐ **[Portafirmas electrónico](http://administracionelectonica.gob.es/ctt/portafirmas)**: El Portafirmas es una aplicación web de usuario final que permite a un usuario identificado remitir documentos a firmar a la carpeta “pendiente de firma” de otro usuario del sistema, el cual es avisado por el sistema mediante un mensaje.

Ambito: AAPP || Organismo: SGAD

☐ **[Portal de firma](http://administracionelectronica.gob.es/ctt/portalfirma)**: Sitio web que pretende acercar y hacer más accesible la firma electrónica a ciudadanos y empresas. Se estructura en torno a una serie de tutoriales sobre la operativa básica de firma y validación de firmas electrónicas y en torno a conceptos relacionados con la firma, como los certificados digitales, el proceso de firma, plataformas de validación, aspectos legales, etc.

Ambito: AAPP y Ciudadanos || Organismo: SGAD

☐ **[Política de firma y certificados AGE](http://administracionelectronica.gob.es/es/ctt/politicafirma)**: El artículo 18 del Real Decreto 4/2010 por el que se regula el ENI, establece que la política de firma electrónica y de certificados de la AGE, servirá de marco general de interoperabilidad para la autenticación y el reconocimiento mutuo de firmas electrónicas dentro de su ámbito de actuación. También establece que dicha política podrá ser utilizada como referencia por otras AAPP para definir las políticas de certificados y firmas a reconocer dentro de sus ámbitos competenciales.

Ambito: AGE || Organismo: SGAD

☐ **[Autentica](http://administracionelectronica.gob.es/ctt/autentica)**: AutenticA es un servicio de autenticación, autorización y Single Sign On de empleados públicos, altos cargos y personal relacionado, para aplicaciones internas de las AAPP Dispone de un repositorio horizontal de usuarios provenientes de fuentes primarias. AutenticA provee atributos de los usuarios, como la unidad y el puesto.

Ambito: AAPP || Organismo: SGAD

☐ **[FIRe - Solución Integral de Firma Electrónica](http://administracionelectronica.gob.es/ctt/fire)**: FIRe es una solución que simplifica el uso y realización de firmas electrónicas de usuario al concentrar en un solo componente todos los requisitos de creación de firmas basadas tanto en certificados locales como en certificados en la nube.

Ambito: AAPP || Organismo: SGAD

☐ **[eIDAS - Sistema europeo de reconocimiento de identidades electrónicas](http://administracionelectronica.gob.es/ctt/eIDAS)**: Proyecto europeo para conseguir el reconocimiento paneuropeo de las identidades electrónicas. De este modo, los servicios de administración electrónica españoles pueden aceptar identidades provinientes de otros países europeos y a su vez los servicios de otros países puedan reconocer el DNI electrónico.

Ambito: AAPP || Organismo: SGAD

## Registro o representación del ciudadano ante las AAPP

☐ **[SIR - Sistema de Interconexión de registros](http://administracionelectronica.gob.es/ctt/sir)**: El Sistema de Interconexión de Registros permite interconectar oficinas de registro presenciales  y electrónicas, basándose en la NTI de SICRES 3.0.

Ambito: AAPP || Organismo: SGAD

☐ **[REC - Registro Electrónico Común](http://administracionelectronica.gob.es/ctt/rec)**: Posibilita la presentación de solicitudes, escritos y comunicaciones dirigidas a la AGE y sus Organismos Públicos que no se ajusten a procedimientos administrativos ya contemplados en los registros electrónicos de las distintas Administraciones.

Ambito: AGE || Organismo: SGAD

☐ **[SICRES](http://administracionelectronica.gob.es/ctt/sicres)**: Normaliza y establece de forma única, global y completa, el Modelo de Datos para el intercambio de asientos entre Entidades Registrales con independencia del Sistema de Registro origen o destino, y de la tecnología de intercambio.

Ambito: AAPP || Organismo: SGAD

☑ **[Geiser - Gestión Integrada de Servicios de Registro](http://administracionelectronica.gob.es/ctt/geiser)**: GEISER es una solución integral de registro para cualquier organismo público, que cubre tanto la gestión de sus oficinas de registro de entrada/salida como la recepción y envío de registros en las unidades tramitadoras destinatarias de la documentación.
La aplicación permite la digitalización de la documentación presentada por el ciudadano en las oficinas, y al contar con certificación SICRES 3.0 posibilita el intercambio de registros en formato electrónico con otros organismos conectados a la plataforma SIR.

Ambito: AAPP || Organismo: SGAD

☐ **[ORVE - Oficina de Registro Virtual](http://administracionelectronica.gob.es/ctt/sir)**: Aplicación en la nube que permite digitalizar y firmar electrónicamente la documentación presentada en ventanilla de registro, e intercambiar asientos registrales a través del Sistema de Interconexión de Registros (SIR).
ORVE permite digitalizar el papel que presenta el ciudadano en las oficinas de registro, y enviarlo electrónicamente al destino al instante, sea cual sea su ubicación geográfica o nivel de administración competente.

Ambito: AAPP || Organismo: SGAD

☐ **[REA - Registro Electrónico de Apoderamientos](http://administracionelectronica.gob.es/ctt/rea)**: El proyecto consiste en la implementación de un registro electrónico de representación y apoderamientos, creado y regulado en el RD 1671/2009 (art. 15), para hacer constar y gestionar las representaciones que los interesados otorguen a terceros, con el fin de que éstos puedan actuar en su nombre de forma electrónica ante la AGE y/o sus organismos públicos vinculados o dependientes (Orden HAP 1637/2012).

Ambito: AGE || Organismo: SGAD

☐ **[RFH - Registro de Funcionarios Habilitados](http://administracionelectronica.gob.es/ctt/rfh)**: El Registro de funcionarios habilitados-RFH, previsto en e art 12 de la Ley 39/2015 permite hacer constar las habilitaciones de los funcionarios de la AGE y sus organismos públicos para que actúen ante la administración en nombre del ciudadano en procedimientos que requieran firma electrónica.

Ambito: AGE || Organismo: SGAD

☐ **[Representa](http://administracionelectronica.gob.es/ctt/representa)**: Representa permite disponer de un punto común para la validación de la habilitación e identidad de los profesionales asociados a colectivos de representación de personas físicas o jurídicas. Dicha representación y habilitación permite la tramitación de un procedimiento administrativo en nombre del ciudadano.

Representa proporciona la información de representación a través de un servicio web. Este servicio web recibe un NIF y opcionalmente una lista de colectivos, y devuelve información sobre los colectivos a los que pertenece.

Ambito: AAPP || Organismo: SGAD

☐ **[Notaría](http://administracionelectronica.gob.es/es/ctt/notaria)**: El Servicio de Consulta de Poderes Notariales es un servicio horizontal que se ofrece a todas las Administraciones para la consulta de subsistencia de Poderes Notariales y de Administradores.

Ambito: AAPP || Organismo: SGAD

## Información al ciudadano

☐ **[Punto de Acceso General](http://administracionelectronica.gob.es/ctt/pag)**: Facilita la intercomunicación de los ciudadanos y empresas con las AAPP (AAPP) actuando de forma centralizada como agregador de la información y servicios electrónicos relacionados con las AAPP. [administracion.gob.es](http://administracion.gob.es)

Ambito: AAPP || Organismo: SGAD

☑ **[Punto de Acceso Telefónico de los servicios de las Administraciones Públicas (060)](http://administracionelectronica.gob.es/ctt/telefono060)**: El número telefónico corto 060 es el Punto de Acceso telefónico de los ciudadanos a los servicios que proporcionan la AGE. Se proporciona un servicio con una oferta normalizada: por una parte, servicios de atención de competencia directa de la SEAP y, por otra parte, la atención y prestación de los trámites de distintos servicios de las AAPP.

Ambito: AAPP || Organismo: SGAD

☐ **[Carpeta Ciudadana](https://administracionelectronica.gob.es/ctt/ccd)**: Carpeta Ciudadana permitirá a los ciudadanos consultar el estado de sus expedientes, acceder a sus notificaciones permitiendo la notificación por comparecencia, gestionar sus apoderamientos permitiendo la revocación o renuncia, y consultar los datos intermediados a través de la plataforma de intermediación con su consentimiento.

Ambito: AGE || Organismo: SGAD

☐ **[FACE - Punto General de Entrada de Facturas AGE](http://administracionelectronica.gob.es/es/ctt/face)**: El Punto General de Entrada de Facturas Electrónicas permite recepcionar en un solo punto todas las facturas electrónicas de la AGE, distribuirlas a las plataformas de facturación, o gestionarlas para aquellos Órganos Gestores que no dispongan de dichas aplicaciones, e informará a los proveedores del estado de tramitación de dichas facturas.

Ambito: AAPP || Organismo: SGAD

☐ **[FACE2B](https://administracionelectronica.gob.es/ctt/faceb2b)**: La plataforma FACEB2B es un Registro Electrónico Único que permite la remisión de facturas del subcontratista al contratista principal y traslada dichas facturas al destinatario de las mismas según la configuración que consignen en el directorio de empresas.

Ambito: Sector privado || Organismo: SGAD

☐ **[Transparencia local](http://administracionelectronica.gob.es/ctt/transparencia)**: El servicio del Portal de la Transparencia en la Nube facilita que las Entidades Locales puedan disponer, de forma gratuita y previa adhesión, de un Portal de Transparencia propio, junto con las herramientas de gesitón y administración necesarias, así como toda la infraestructura TIC necesaria para alojarlos en las condiciones de seguridad, interoperabilidad y accesibilidad. Con ello, pueden dar cumplimiento a las obligaciones establecidas por la Ley 19/2013, de 9 de diciembre, de transparencia, acceso a la información pública y buen gobierno.

Ambito: EELL || Organismo: SGAD

## Tramitación y comunicación con ciudadanos

☐ **[Cambio de Domicilio-SCCD](http://administracionelectronica.gob.es/ctt/sccd)**: Unifica en un solo trámite, las actualizaciones que el ciudadano debe hacer para comunicar un nuevo domicilio a las organismos de todas las Administraciones.

Ambito: AAPP || Organismo: SGAD

## Impulso Administración Digital-OTROS

☐ **[Inscripción en Pruebas Selectivas](http://administracionelectronica.gob.es/ctt/ips)**: Ofrece al ciudadano la posibilidad de inscribirse en pruebas selectivas convocadas por la AGE. Por otro lado, ofrece a las AAPP la posibilidad de convocar pruebas selectivas a través de esta plataforma.

Ambito: AGE || Organismo: SGAD

☐ **[Cita Previa](http://administracionelectronica.gob.es/ctt/citaprevia)**: Permite a las oficinas de atencióna a los ciudadanos planificar horarios, calendarios, y organizar la atención a los ciudadanos de forma presencial en función del trámite. El ciudadano podrá concertar las citas presenciales para la gestión de sus trámites de una forma muy sencilla a través de internet o bien poniendose en contacto con las diferentes oficinas.

Ambito: AAPP y Ciudadanos || Organismo: SGAD

## Tramitación y comunicación con ciudadanos

☐ **[Plataforma de Intermediación de Datos](http://administracionelectronica.gob.es/ctt/svd)**: Ofrece a las diferentes AAPP la posibilidad de acceder a datos que ya se encuentran en poder de la administración y que de otro modo el ciudadano tendría que aportar al trámite con un certificado específico en papel. 
Se trata de una pieza clave para conseguir el cumplimiento del derecho reconocido a los ciudadanos en el ley 11/2007 de no tener que aportar datos que ya obren en poder de la administración.
Actualmente ofrece los servicios de verificación de datos de identidad, residencia, prestación de desempleo, títulos oficiales, TGSS, AEAT, catastro, nivel y grado de dependencia, prestaciones públicas.

Ambito: AAPP || Organismo: SGAD

☐ **[Portfolio soluciones SCSP - Sustitución de Certificados en Papel](http://administracionelectronica.gob.es/ctt/scsp)**: Sustitución de Certificados en Soporte Papel es un conjunto de especificaciones orientadas al intercambio de datos entre AAPP con el objetivo de eliminar los certificados administrativos en papel.
Las librerías SCSP facilitan la integración con sistemas compatibles con la especificación SCSP 
El Cliente ligero SCSP permite la interacción inmediata con todos los servicios ofrecidos por la plataforma de intermediación de datos.

Ambito: AAPP y Ciudadanos || Organismo: SGAD

☐ **[Plataforma electrónica de adhesiones](http://administracionelectronica.gob.es/ctt/adhesiones)**: Plataforma electrónica de Adhesiones está accesible a través de los Portales de la AGE, de las CCAA y de las EELL y puede ser utilizada por los usuarios cuyo perfil les permita, haciendo uso de su firma electrónica, actuar en representación de su Organismo y cumplimentar y firmar las condiciones concretas en las que acepta la adhesión a un convenio, acuerdo de colaboración o servicio que ofrezca la Secretaría de Estado de Función Pública a través de la Secretaría General de la Administración Digital.

Ambito: AAPP y Ciudadanos || Organismo: SGAD

☐ **[CORINTO - Correspondencia interadministrativa](http://administracionelectronica.gob.es/ctt/corinto)**: La aplicación CORINTO (Correspondencia Interadministrativa) consiste en una aplicación Web centralizada que proporciona un servicio de Correspondencia entre unidades existentes en el DIR3, que permite a las mismas el intercambio de documentación con plenas garantías registrales, gracias al Registro Electrónico Común, y de recepción y no repudio, gracias a los sistemas de firma electrónica.

Ambito: AAPP || Organismo: SGAD

☐ **[SIA - Sistema de Información Administrativa](http://administracionelectronica.gob.es/ctt/SIA)**: El Sistema de Información Administrativa, SIA, es una aplicación cuya función básica es la de actuar como repositorio de información relevante en lo concerniente a la relación entre Administración y ciudadano. Así, la misma aspira a integrar los procedimientos administrativos y servicios electrónicos existentes en el conjunto de las AAPP, si bien el foco actual está en el ámbito de la AGE. 
Da cumplimiento al Artículo 9 del RD 4/2010.

Ambito: AAPP || Organismo: SGAD

☐ **[Direntidades - Directorio de Entidades](http://administracionelectronica.gob.es/ctt/direntidades)**: DIRe permite a las entidades (personas jurídicas del ámbito privado) mantener su información básica actualizada, para que las distintas aplicaciones de la Secretaría General de Administración Digital y de otros  organismos públicos o servicios privados hagan uso de dicha información.

Ambito: Sector privado || Organismo: SGAD

☐ **[DIR3 -  Directorio Común de Unidades Orgánicas y Oficinas](http://administracionelectronica.gob.es/ctt/dir3)**: El Directorio Común se concibe como un Inventario de información sobre la estructura orgánica de la Administración Pública, y sus oficinas de atención ciudadana. Es decir, es un catálogo de las unidades orgánicas, organismos públicos, y oficinas de registro y atención al ciudadano de la Administración codificadas de forma únivoca según especificado en el Artículo 9 del RD 4/2010.

Ambito: AAPP || Organismo: SGAD

☑ **[NOTIFIC@](http://administracionelectronica.gob.es/ctt/notifica)**: Consiste en un concentrador de peticiones de emisión de comunicaciones y notificaciones en un formato común que actúa como intermediario y gestor de las peticiones.

Ambito: AAPP || Organismo: SGAD

☐ **[SNE - Notificaciones electrónicas](http://administracionelectronica.gob.es/ctt/sne)**: El servicio proporciona a cada ciudadano o empresa un buzón seguro asociado a una Dirección Electrónica Habilitada, en la cual recibirá las comunicaciones y notificaciones administrativas sustituyendo así la tradicional manera de recibir las notificaciones administrativas vía correo postal,.

Ambito: AAPP y Ciudadanos || Organismo: SGAD

☐ **[Dirección Electrónica Habilitada Única - Punto único de notificaciones para todas las Administraciones Públicas](http://administracionelectronica.gob.es/ctt/lema)**: El Punto único de notificaciones para todas las AAPP o Dirección Electrónica Habilitada única facilita el acceso a los ciudadanos a las notificaciones y comunicaciones emitidas por las AAPP en el ejercicio de su actividad.

Ambito: AAPP y Ciudadanos || Organismo: SGAD

☐ **[Plataforma de Mensajería (SIM)](http://administracionelectronica.gob.es/ctt/sim)**: La Plataforma de Mensajería integra el envío de mensajes tanto de EMAIL como de SMS en una sola herramienta.

Ambito: AGE || Organismo: SGAD

## Gestión de documento y expediente electrónico y Archivo

☑ **[InSiDe - Infraestructura y Sistemas de Documentación Electrónica](http://administracionelectronica.gob.es/ctt/inside)**: InSiDe es la abstracción de un gestor documental que cumpla con los estándares CMIS para la gestión documental de los expedientes y documentos electrónicos según lo especificado en las NTI del ENI.
- Permite almacenar documentos, firmas, metadatos, versiones de los documentos, etc. 
- Permite su consulta y gestión por medio de servicios web.

Ambito: AAPP || Organismo: SGAD

☑ **[ARCHIVE](http://administracionelectronica.gob.es/es/ctt/archive)**: Archive es una aplicación web de archivo definitivo de expedientes y documentos electrónicos, que cumple con lo dispuesto al respecto en el RD 4/2010, de 8 de enero, por el que se regula el ENI en el ámbito de la Administración electrónica.
Archive proporciona las herramientas necesarias para la creación por parte de un super-administrador de un sistema de administración y gestión de Centros de Archivo multidepartamental, así como la integración en Archive de las correspondientes aplicaciones consumidoras y la gestión de los documentos y expedientes electrónicos remitidos por las mismas.

Ambito: AAPP || Organismo: SGAD

☐ **[Especificación de documento electrónico](http://administracionelectronica.gob.es/ctt/documentoe)**: La estructura a aplicar para el intercambio de documentos electrónicos será de forma general un fichero XML que incluirá los tres componentes del documento electrónico identificados, esto es, Fichero de contenido, Bloque de metadatos y Firma/s.

Ambito: AAPP || Organismo: SGAD

☐ **[Especificación de expediente electrónico](http://administracionelectronica.gob.es/ctt/expedientee)**: La estructura a aplicar para el intercambio de expedientes electrónicos será de forma general: un fichero XML, índice firmado, metadatos mínimos obligatorios, y, opcionalmente, un elemento para incluir una visualización alternativa de la información del expediente.

Ambito: AAPP || Organismo: SGAD

☐ **[eEMGDE](http://administracionelectronica.gob.es/ctt/eEMGDE)**: Esquema de metadatos para la gestión del documento electrónico mencionado por la NTI de Política de gestión de documentos electrónicos.

Ambito: AAPP || Organismo: SGAD

## Impulso Administración Digital-OTROS

☐ **[ACCEDA - Sede y Gestión Electrónica de Procedimientos](http://administracionelectronica.gob.es/ctt/acceda)**: Acceda es una plataforma genérica que permite implementar una sede electrónica. También actua como tramitador para cubrir las necesidades básicas de la tramitación electrónica permitiendo implementar de forma rápida y sencilla, nuevos procedimientos administrativos electrónicamente, sin necesidad de un desarrollo particular para cada uno.

Ambito: AAPP || Organismo: SGAD

## Tramitación y comunicación con ciudadanos

☐ **[Pasarela de Pagos Centralizada](https://administracionelectronica.gob.es/ctt/pagos)**: Esta plataforma facilita la implantación del pago telemático en las aplicaciones que gestionan trámites que conlleven el pago de tasas, en los Organismos de la AGE.

Ambito: AGE || Organismo: SGAD

☐ **[PAE-Portal de Administración Electrónica](http://administracionelectronica.gob.es/ctt/pae)**: Portal que constituye un punto centralizado de información donde dar a conocer la situación actual de la Administración electrónica: noticias y eventos, informes, estudios y boletines, base legislativa, organización y estrategias, etc.

Ambito: AAPP y Ciudadanos || Organismo: SGAD

☐ **[OBSAE - Observatorio de Administración Electrónica](http://administracionelectronica.gob.es/PAe/OBSAE)**: El Observatorio de Administración Electrónica se dedica al análisis y difusión de la situación de la Administración Electrónica en España. Para ello, sintetiza, analiza y publica indicadores de Administración Electrónica, realiza estudios periódicos, publica boletines y notas técnicas sobre el desarrollo de la Administración Electrónica y colabora con entidades internacionales, como la CE, la OCDE y la ONU.

Ambito: AAPP y Ciudadanos || Organismo: SGAD

☐ **[DataOBSAE - Indicadores de Administración Electrónica](http://dataobsae.administracionelectronica.gob.es/)**: Cuadro de Mando sobre indicadores de Administración Electrónica en las AAPP, obtenidos a partir de datos proporcionados por los servicios horizontales de la SGAD así como de otras fuentes externas. También permite el acceso a informes de elaboración periódica.

Ambito: AAPP y Ciudadanos || Organismo: SGAD

☐ **[CTT - Centro de Transferencia de Tecnología](http://administracionelectronica.gob.es/ctt/ctt)**: Constituye el directorio general de aplicaciones para su reutilización en las AAPP especificado en la ley 11/2007 y de obligado uso en la AGE.

Ambito: AAPP || Organismo: SGAD

☐ **[CISE](http://administracionelectronica.gob.es/ctt/cise)**: Catálogo de diferentes activos semánticos para el intercambio de información que se produce entre las AAPP y entre éstas y los ciudadanos.

Ambito: AAPP || Organismo: SGAD

☐ **[Portal datos.gob.es](http://administracionelectronica.gob.es/ctt/datosgob)**: Datos.gob.es es el portal de carácter nacional que organiza y gestiona el catálogo de información pública, el punto de acceso único a los conjuntos de datos de la AGE. Asimismo, desde este portal se proporciona información general, materiales formativos y noticias de actualidad sobre la reutilización de la información del séctor público.

Ambito: AAPP || Organismo: SESIAD, SGAD

## Información al ciudadano

☐ **[PLATA](http://administracionelectronica.gob.es/ctt/plata)**: Plataforma de traducción automática.

Ambito: AAPP || Organismo: SGAD

☐ **[PTPLATA](https://administracionelectronica.gob.es/ctt/ptplata/)**: El portal de traducción automática PLATA  permite al usuario traducir textos y ficheros entre más de 360 combinaciones de idiomas. El portal utiliza la traducción del motor PLATA de la AGE y del motor de traducciónMT@EC de la Comisión Europea para ofrecer los textos traducidos al usuario. Ambos sistemas de traducción son sistemas de traducción automática sin revisión o intervención humana. La calidad de las traducciones está dentro de los umbrales de calidad  marcados para este tipo de sistemas de traducción.

Ambito: AAPP || Organismo: SGAD

☐ **[EGEO](http://administracionelectronica.gob.es/ctt/egeo)**: EGEO es un servicio común que facilita la creación de mapas interactivos para su presentación en portales web, sin necesidad de conocimientos de georreferenciación ni desarrollos adicionales. Dispone de un entorno para la gestión de dichos mapas basado en una parametrización sencilla y plantillas de datos con una estructura simple (Excel o XML).

Ambito: AAPP || Organismo: SGAD

☐ **[BUSCADORAGE](http://administracionelectronica.gob.es/ctt/buscadorage)**: El servicio de buscador permite la búsqueda de información en los portales y sedes de los Ministerios y sus organismos dependientes.

Ambito: AAPP || Organismo: SGAD

## Impulso Administración Digital-OTROS

☐ **[OAW-Servicio de diagnóstico en línea](http://administracionelectronica.gob.es/PAe/accesibilidad)**: Servicio que proporciona a cada Departamento de las AAPP la posibilidad de realizar, directamente, análisis automáticos de accesibilidad conformes al estudio del observatorio basado en la norma UNE 139803:2004 o/y en la norma UNE 139803:2012.

Ambito: AAPP || Organismo: SGAD

☐ **[FORMA](http://administracionelectronica.gob.es/ctt/forma)**: Sistema que permite generar formularios y encuestas para publicación web. Proporcionando al editor la posibilidad de crear formularios, sin necesidad de conocimientos de programación y que puedan ser autoadministrados por cada editor.

Ambito: AAPP || Organismo: SGAD

☐ **[ADISE](http://administracionelectronica.gob.es/ctt/adise)**: Sistema destinado a monitorizar la disponibilidad de los servicios electrónicos prestados por la AGE y las diferentes AAPP. Este sistema proporciona información sobre si el servicio o la página web monitorizada está accesible o no en base a múltiples parámetros.

Ambito: AAPP || Organismo: SGAD

☐ **[RUN - Reductor de URLs](http://administracionelectronica.gob.es/ctt/run)**: RUN es una solución sencilla para su uso en mensajería instantánea, redes sociales, emails, o cualquier otra comunicación que requiera una URL corta para ahorrar espacio o para tener una dirección más amigable para la difusión de un servicio o contenido. Dicha dirección tendrá la forma http://run.gob.es/xxxxx.

Ambito: AAPP || Organismo: SGAD

☐ **[Portal de acceso para Entidades Locales](http://administracionelectronica.gob.es/ctt/portaleell)**: Este portal ofrece una herramienta de gestión de identidades de los empleados públicos de las entidades locales  y un portal de autenticación único que proporciona single sign-on entre todos los servicios ofrecidos. Cualquier organismo puede solicitar la inclusión en la plataforma de nuevas aplicaciones orientadas a las EELL de modo que éstas puedan acceder desde un punto centralizado.

Ambito: AAPP || Organismo: SGAD

☐ **[Portal de acceso para Comunidades Autónomas](http://administracionelectronica.gob.es/ctt/portalccaa)**: Este portal ofrece una herramienta de gestión de identidades de los empleados públicos de las CCAA  y un portal de autenticación único que proporciona single sign-on entre todos los servicios ofrecidos. Cualquier organismo puede solicitar la inclusión en la plataforma de nuevas aplicaciones orientadas a las CCAA de modo que éstas puedan acceder desde un punto centralizado.

Ambito: AAPP || Organismo: SGAD

# Gestión Interna

Soluciones que podrían ser utilizadas para prestar los servicios generales a un organismo público desde una unidad TIC

## Comunicación y mensajería

☑ **[Correo Electrónico Multidominio](http://administracionelectronica.gob.es/ctt/correogobes)**: El correo electrónico multidominio permite, desde un punto centralizado, dar servicio de correo electrónico y agenda electrónica sin necesidad de tener instalaciones in situ o contrataciones externas. Incluye correo electrónico sobre clientes pesados (Outlook, Thunderbird, etc..), correo web, correo sobre dispositivos móviles, sincronización de agendas, listas de distribución, etc. Al mismo tiempo permite la gestión descentralizada de los buzones de cada dominio por parte de los Organismos adheridos.

Ambito: AAPP || Organismo: SGAD

☐ **[Videoconferencia Reúnete](http://administracionelectronica.gob.es/ctt/reunete)**: Servicio Común de Reuniones Virtuales de la AGE, desde el cual se ofrecen herramientas colaborativas a todas las AAPP con el fin de rentabilizar el trabajo en equipo y contribuir a disminuir el gasto en las AAPP

Ambito: AAPP || Organismo: SGAD

☐ **[Almacen](http://administracionelectronica.gob.es/ctt/almacen)**: Aplicación para el intercambio de ficheros de gran tamaño. Se puede acceder desde Funciona.

Ambito: AGE || Organismo: SGAD

## RRHH

☑ **[NEDAES - Nónima estándar](http://administracionelectronica.gob.es/ctt/nedaes)**: Realiza la gestión de nómina de los empleados públicos incluidos en el ámbito de la Ley 30/1984 sobre Medidas para la Reforma de la Función Pública, en los términos de la Ley 7/2007 de 12 abril del Estatuto Básico del Empleado Público.

Ambito: AGE || Organismo: SGAD

☑ **[SIGP - Sistema Integrado de Gestión de Personal](http://administracionelectronica.gob.es/ctt/sigp)**: Permite la gestión completamente electrónica de un amplio conjunto de procedimientos en materia de gestión de RR.HH. mediante el uso de firma electrónica en todas sus fases, incluida en la participación del empleado público; intercambia  información entre las Unidades de RR.HH implicadas de forma completamente telemática y sus datos provienen de, y  se anotan en, el  Registro Central de Personal.   Así mismo facilita la comunicación entre la unidad de RR.HH, empleados públicos  y jefes de otras unidades.

Ambito: AGE || Organismo: SGAD

☐ **[FUNCIONA – Portal del Empleado](http://www.funciona.es)**: Portal de Intranet del empleado Público: ofrece información sobre expediente personal, nómina, solicitudes de concursos, formación, ayudas de acción social, participación en concursos de traslados, directorio de personal, concursos de traslados, ofertas de puestos, etc. Permite la creación de portales de Intranet específicos de difusión abiertos o restringidos a grupos de usuarios.

Ambito: AGE || Organismo: SGAD

☐ **[SERVINOMINA](http://administracionelectronica.gob.es/ctt/servinomina)**: El Servicio de Visualización de Nóminas (Servinómina) permite la consulta de la nómina a través del Portal Funciona y la eliminación del recibo de nómina en papel. Este servicio está dirigido a aquellos organismos que realicen su nómina con NEDAES.

Ambito: AGE || Organismo: SGAD

☐ **[Portal SIRES](http://administracionelectronica.gob.es/ctt/sires)**: El portal SIRES, es un portal de transferencia segura de ficheros entre Organismos de la AGE y la División del Registro Central de Personal para el envío a, o la obtención de datos de carácter personal procedentes del RCP.

Ambito: AGE || Organismo: SGAD

☐ **[TRAMA (Gestión de vacaciones, 
permisos e incidencias)](http://administracionelectronica.gob.es/ctt/trama)**: El sistema TRAMA, permite el fichaje tanto por dispositivo de reloj como con el uso de certificado electrónico, es la solución desplegada en Servicios Centrales  y numerosas Delegaciones y Subdelegaciones de Gobierno para la gestión de trámites del personal.
Basado en software libre (JAVA y motor de tramitación jBPM),  presenta interfaces de integración  (servicios web) con BADARAL.

Ambito: AAPP || Organismo: SGAD

☐ **[Estadísticas TRAMA](http://administracionelectronica.gob.es/ctt/estadisticatrama)**: El sistema TRAMA, permite el fichaje tanto por dispositivo de reloj como con el uso de certificado electrónico, así como la gestión de trámites de personal de los empleados públicos.
Basado en software libre (JAVA y motor de tramitación jBPM),  presenta interfaces de integración con BADARAL y Autentica.

Ambito: AAPP || Organismo: SGAD

☐ **[RCP - Registro Central de Personal](http://administracionelectronica.gob.es/pae_Home/pae_Estrategias/Racionaliza_y_Comparte/soluciones_cloud/Gestion_RRHH.html)**: Sistemas de información: RCP, RCPDOC, CERTE, BADARAL, SuscripcionesRCP. Dispone de servicios web de documentos, estadopersona, datospersona, AnotaRCP, expediente personal, generación de documentos, consulta de puestos y conceptos codificados, unidades orgánicas,  certificados, y comunicación con CEPIT-MUFACE. La función del RCP es realizar la inscripción y anotación de todos los actos de relevancia de la vida administrativa de los empleados públicos de su ámbito de actividad. Para el empleado público es un modelo único de transparencia de todos los actos que afectan a su vida administrativa, dado que puede consultarlos todos, además de sus documentos registrales, a través de Funciona y de Carpeta Ciudadana. Para el gestor de RR.HH es una herramienta única en la gestión de personal porque en todo momento conoce el estado del personal bajo su ámbito competencial a través de RCP, BADARAL y la Plataforma de Intermediación de Datos (PID). Para los responsables de las políticas públicas es una importante fuente de información para el conocimiento exacto de la situación actual y previsión de la futura y para la toma de decisiones. Más de 30 Universidades Públicas españolas tienen suscrito convenio con el RCP, lo que redunda en unos elevados ahorros derivados de las economías de escalas. Integrado con Funciona, AutenticA, @firma, Portafirmas AGE, Carpeta Ciudadana, DIR3, REINA, eSIR, PID, Muface, SIGP, y otros sistemas de RRHH de la AGE. [administracionelectronica.gob.es/ctt/anota](https://administracionelectronica.gob.es/ctt/anota)

Ambito: AGE || Organismo: SGAD

☐ **[Anota RCP](http://administracionelectronica.gob.es/ctt/anota)**: Anota permite a las unidades de RRHH de la Administración del Estado y de las Universidades Públicas el envío de documentos electrónicos al Registro Central de Personal.

Ambito: AAPP || Organismo: SGAD

☐ **[CECIR - Portal CECIR](http://administracionelectronica.gob.es/pae_Home/pae_Estrategias/Racionaliza_y_Comparte/soluciones_cloud/Gestion_RRHH.html#.WKL6fRtFDcs)**: Sistemas de información: Portal CECIR, Gestión de Propuestas, Gestión de Expedientes RPT-Asistencias-Convocatorias-Autorizaciones de contratación, Convoca, Gestión de dotaciones, Simulación de Costes RPT. Servicio web de Propuestas. Espacio de trabajo electrónico para los gestores de RRHH de los Departamentos Ministeriales con competencias de presentación de expedientes de modificaciones de puestos de trabajo. Mantiene total integración con el RCP de tal modo que las modificaciones aprobadas se incorporan de forma inmediata a las relaciones de puestos del RCP. Integrado con @firma, portafirmas AGE, PAPIRO (gestión exp. Costes de Personal).

Ambito: AGE || Organismo: SGAD

## Gestión de subvenciones

☐ **[Aura](https://administracionelectronica.gob.es/ctt/aura)**: AURA permite la tramitación electrónica de las solicitudes de subvenciones por daños en infraestructuras municipales y red viaria a consecuencia de inundaciones y otros efectos de los temporales de lluvia, nieve y viento.

Ambito: AAPP || Organismo: SGAD

☐ **[Galatea](http://administracionelectronica.gob.es/ctt/galatea)**: GALATEA es un servicio común en la nube que permite a los Organismos Intermedios designados por la Autoridad competente, la gestión integral, homogénea y centralizada de los proyectos cofinanciados con los Fondos FEDER correspondientes al periodo de programación 2014-2020.

Ambito: AAPP || Organismo: SGAD

## Otros servicios de Gestión Interna

☐ **[CIRCABC](http://administracionelectronica.gob.es/ctt/circabc)**: CIRCABC es una herramienta de trabajo en grupo para intercambio de información y trabajo colaborativo entre las comunidades de usuarios, basada en tecnologías web y en software de fuentes abiertas. Permite a una comunidad dada (comité, grupo de trabajo, grupo de proyecto, etc.) geográficamente separada mantener un espacio privado en Internet donde pueden compartir información, documentos, participar en foros de discusión y funcionalidades varias.

Ambito: AAPP || Organismo: SGAD

☐ **[Intranets para organismos](http://www.funciona.es)**: Cualquier unidad puede crear su espacio o una Intranet de difusión restringida a través del portal FUNCIONA 
En la actualidad ya contiene otros portales genéricos de amplia divulgación como el espacio de imagen institucional y el de prevención de riesgos laborales, así como portales de otros organismos como la Oficina del Partícipe del Plan de Pensiones de la AGE.

Ambito: AGE || Organismo: SGAD

## Incidencias y peticiones

☐ **[Gestión de Incidencias - Pandora](http://administracionelectronica.gob.es/ctt/pandora)**: Herramienta corporativa para el alta, gestión y seguimiento de las incidencias informáticas, tanto a nivel de las diversas aplicaciones puestas a disposición de las distintas unidades, como todo aquello relacionado con equipos informáticos, software ofimático, comunicaciones de voz y datos, etc.

Ambito: AAPP || Organismo: SGAD

## Inventario y gestión de activos

☐ **[Gestión de Inventario](http://administracionelectronica.gob.es/ctt/inventarioseap)**: Inventariado de equipos en las redes en tiempo real, con información detallada de los equipos con cualquier S.O. Enlace con herramienta real de gestión de inventario, compras, garantías, mantenimiento, usuarios, desafectaciones, almacenaje.

Ambito: AAPP || Organismo: SGAD

☐ **[Gestión de Material - PeMat](http://administracionelectronica.gob.es/ctt/pemat)**: La aplicación de petición de material es un producto que pretende facilitar las peticiones de material (de escritorio, de archivo, informático, etc.) dentro de la un organismo, así como el control del uso del mismo.

Ambito: AAPP || Organismo: SGAD

## Tramitación interna

☐ **[Registro de Recursos Administrativos](http://administracionelectronica.gob.es/ctt/recursos)**: Aplicación de gestión para la unidad responsable del registro, gestión y seguimiento de los Recursos Administrativos.

Ambito: AAPP || Organismo: SGAD

# Infraestructuras

IAAS: Infraestructuras como servicio

## Telecomunicaciones

☐ **[Comunicaciones SARA](http://administracionelectronica.gob.es/ctt/redsara)**: La red SARA es un conjunto de infraestructuras tecnológicas que permiten la interconexión entre sí, de las AAPP, facilitando el intercambio de información y servicios entre ellas.

Ambito: AAPP || Organismo: SGAD

☐ **[Gateway IPv6 para organismos de la administración](http://administracionelectronica.gob.es/ctt/gatewayipv6)**: Como serivicio a las AAPP y dentro del proyecto europeo Gen6, la Red SARA ofrece a los distintos organismos la posibilidad de actuar como Gateway de sus comunicaciones IPv6 en el entorno de Internet.

Ambito: AAPP || Organismo: SGAD

☑ **[Servicio Unificado de Telecomunicaciones](http://administracionelectronica.gob.es/ctt/comunicaciones)**: Destinado a proporcionar a las entidades de la AGE y sus OOPP una comunicación de calidad entre todas sus sedes y entre todos suss empleados. Incluye:
- Red corporativa multiservicio y servicio de telefonía fija.
- Comunicaciones móviles
- Internet
- Red internacional.

Ambito: AGE || Organismo: SGAD

## Seguridad

☑ **[Servicio de seguridad gestionada](http://administracionelectronica.gob.es/ctt/ciberseguridad)**: Servicio compartido de la AGE que engloba al  conjunto de servicios de ciberseguridad necesarios para proporcionar una adecuada protección a la AGE y sus Organismos Públicos. Incluye el equipamiento necesario, así como su configuración, puesta en marcha, mantenimiento y gestión.

Ambito: AGE || Organismo: SGAD

## Consolidación  de infraestructuras

☑ **Servicio de Alojamiento de Infraestructuras TIC**: Porporciona espacio físico acondicionado para albergar las infraestructuras TIC de las diferentes unidades de la AGE y sus Organismos Públicos, con una disponibiliad y nivel de servicio elevados, en un escenario de coste eficiente.

Ambito: AGE || Organismo: SGAD

☑ **Servicio de nube híbrida (nubeSARA)**: Servicio que proporciona servicios de computación y almacenamiento en nube híbrida para la AGE y sus OOPP, mediante la configuación de nodos de consolidación tanto en CPDs de la Administración (nube privada) como de proveedores externos (nube pública).

Ambito: AGE || Organismo: SGAD

# Producción regulatoria, guías e informes relevantes

Producción regulatoria así como guías, metodologías, buenas prácticas e informes que faciliten el avance en materia de Administración Digital.

## Producción regulatoria

☐ **[Esquema Nacional de Seguridad](http://administracionelectronica.gob.es/ctt/ens)**: El ENS, regulado por el  Real Decreto 3/2010(Abre en nueva ventana) , de 8 de enero, determina la política de seguridad que se ha de aplicar en la utilización de los medios electrónicos. El ENS está constituido por los principios básicos y requisitos mínimos para una protección adecuada de la información. Será aplicado por las AAPP para asegurar el acceso, integridad, disponibilidad, autenticidad, confidencialidad, trazabilidad y conservación de los datos, informaciones y servicios utilizados en medios electrónicos que gestiones en el ejercicio de sus competencias.

Ambito: AAPP || Organismo: SGAD, CCN, colaboración de todas las AAPP

☐ **[Esquema Nacional de Interoperabilidad. Normas Técnicas de Interoperabilidad](http://administracionelectronica.gob.es/ctt/eni)**: El ENI, regulado por el Real Decreto 4/2010(Abre en nueva ventana) , de 8 de enero, establece el conjunto de criterios y recomendaciones que deberán ser tenidos en cuenta por las AAPP para la toma de decisiones tecnológicas que garanticen la interoperabilidad. Las normas técnicas de interoperabilidad previstas en su disposición adicional primera desarrollan ciertos aspectos concretos.

Ambito: AAPP || Organismo: SGAD con la colaboración de todas las AAPP

☐ **[Plan de Transformación Digital de la AGE y sus OOPP. Estrategia TIC](http://administracionelectronica.gob.es/PAe/estrategiaTIC)**: El Plan de Transformación digital de la AGE  y sus Organismos Públicos(Abre en nueva ventana) , la Estrategia TIC, constituye el marco estratégico global para avanzar en la transformación de la Administración, estableciendo sus principios rectores, los objetivos y las acciones para alcanzarlos, así como los hitos para el desarrollo gradual de la Administración Digital con un horizonte temporal hasta 2020.

Ambito: AGE || Organismo: SGAD con la colaboración de los departamentos Ministeriales

## Metodologías y guías

☐ **[Guías de aplicación de las Normas Técnicas de Interoperabilidad](http://administracionelectronica.gob.es/PAe/NTinteroperabilidad)**: Estas guías sirven de ayuda práctica a las Administraciones APP a la hora de interpretar y aplicar las Normas Técnicas de Interoperabilidad.

Ambito: AAPP || Organismo: SGAD

☐ **[Guías del Observatorio de Accesibilidad Web](http://administracionelectronica.gob.es/PAe/accesibilidad/documentacion)**: Las guías del observatorio de Accesibilidad Web pretenden ser una ayuda para la gestión y mantenimiento de la accesibilidad en los portales web de la Administración. Todas estas guías se están coordinando y preparando dentro de la iniciativa del Observatorio de Accesibilidad Web.

Ambito: AAPP || Organismo: SGAD

☐ **[MAGERIT](http://administracionelectronica.gob.es/pae_Home/pae_Documentacion/pae_Metodolog/pae_Magerit.html)**: MAGERIT es una metodología de análisis y gestión de riesgos elaborada como respuesta a la percepción de que la Administración, y, en general, toda la sociedad, dependen de forma creciente de las tecnologías de la información para el cumplimiento de su misión.

Ambito: AAPP || Organismo: SGAD

☐ **[Métrica v.3](http://administracionelectronica.gob.es/PAe/metrica3)**: Métrica es una metodología para sistematizar las actividades que dan soporte al ciclo de vida del software.

Ambito: AAPP || Organismo: SGAD

☐ **[Guía de Comunicación Digital de la AGE](http://administracionelectronica.gob.es/PAe/guia_comunicacion_digital)**: La Guía de Comunicación Digital para la AGE proporciona un marco de criterios, recomendaciones y buenas prácticas a tener en cuenta por sus Departamentos y organismos al crear, generar contenidos o evolucionar los sitios y portales web, las sedes electrónicas o los sitios relacionados con las nuevas tecnologías web2.0 (blogs, cuentas o perfiles de redes sociales a los que accede bajo los nombres oficiales de los Departamentos u organismos de la AGE).

Ambito: AGE || Organismo: SGAD

## Informes del Observatorio de la Administración Electrónica (OBSAE)

☐ **[REINA - Tecnologías de la Información y las Comunicaciones en la Administración del Estado](http://administracionelectronica.gob.es/PAe/REINA)**: El informe REINA presenta un análisis cuantitativo del sector de Tecnologías de la Información y las Comunicaciones en la Administración del Estado recogiendo los agregados económicos e indicadores más significativos del mismo, junto con las características más representativas del parque de recursos informáticos, efectuando al mismo tiempo un contraste con los relativos a otros sectores públicos y privados.

Ambito: AGE || Organismo: SGAD, con la colaboración del resto de AGE

☐ **[IRIA - Tecnologías de la Información y las Comunicaciones en las Administraciones Públicas](http://administracionelectronica.gob.es/PAe/IRIA)**: El informe IRIA presenta una visión global de la situación y uso de los Sistemas y Tecnologías de la Información y las Comunicaciones en las AAPP, recogiendo los principales agregados del sector y su evolución, resaltando sus peculiaridades y favoreciendo así la creación de un marco general de actuación que oriente las futuras decisiones de planificación y adquisición de Sistemas y Tecnologías de la Información en el ámbito administrativo.

Ambito: AAPP || Organismo: SGAD, con la colaboración de AAPP

☐ **[CAE - Administración Electrónica en CCAA](http://administracionelectronica.gob.es/PAe/CAE)**: Este informe integra anualmente la información sobre Administración Electrónica proporcionada por las Comunidades Autónomas en el ámbito de la Conferencia Sectorial de AAPP, con el objeto de 
monitorizar el avance de la Administración Autonómica hacia la Administración electrónica ymantener una radiografía permanentemente actualizada sobre el estado de las diferentes administraciones en este tema.

Ambito: CCAA || Organismo: SGAD, con la colaboración de las CCAA

☐ **[Informe de Presupuestos](https://administracionelectronica.gob.es/PAe/presupuestosTIC)**: Este informe analiza la dimensión y estructura de Gastos e Inversiones en Tecnologías de la Información y las Comunicaciones de la Administración del Estado y la Seguridad Social.

Ambito: AGE || Organismo: SGAD

☐ **[Boletín OBSAE](http://administracionelectronica.gob.es/PAe/boletinOBSAE)**: Informe trimestral con los principales indicadores de la Administración Electrónica en España.

Ambito: AGE || Organismo: SGAD

☐ **[Notas técnicas del OBSAE](http://administracionelectronica.gob.es/pae_Home/pae_OBSAE/pae_NotasTecnicas.html)**: Artículos mensuales sobre aspectos concretos del desarrollo de la Administración Electrónica.

Ambito: AGE || Organismo: SGAD
