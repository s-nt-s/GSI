---
title: Microservicios
status: draft
---

# Conceptos básicos


# Microservicios

La arquitectura de microservicios consiste en construir una aplicación como un
conjunto de pequeños servicios, los cuales se ejecutan en su propio
proceso y se comunican con mecanismos ligeros (normalmente una API de recursos HTTP).

Cada servicio se encarga de implementar una funcionalidad completa del negocio,
es desplegado de forma independiente y puede estar programado en distintos
lenguajes y usar diferentes tecnologías de almacenamiento de datos.

Esta recomendado para casos en los que:

* hay muchos tipos de clientes distintos (web, movil, etc) porque estos tendrán
distintas interfaces y ciclos de desarrollo pero se apoyaran en los mismos microservicios
* hay una gran variedad de tipos de almacenamiento, así cada microservicios puede
usar el tipo de almacenamiento que mejor le viene
* la carga de trabajo es muy variable en el tiempo, de esta manera se pueden añadir
un mayor número de instancias del microservicio que necesitemos

# Bibliografía

* PreparaTic27 - Pack3/02
* PreparaTic27 - Pack3/03
