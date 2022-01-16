---
title: Evaluación de riesgos
---

El análisis de riesgos consiste en el estudio de las posibles amenazas así como los daños que estos
puedan producir en los activos de la organización.

Para la evaluación de riesgos se utilizará la metodología Magerit por ser la más extendida en la
Administración. Para facilitar su realización se utilizará la herramienta MicroPilar del CCN-CERT que
que se adaptada al ENS.

Los pasos a seguir serán:

1. determinar los activos relevantes para la organización, su interrelación
y su valor, en el sentido de qué perjuicio (coste) supondría su degradación
2. determinar a qué amenazas están expuestos los activos
3. estimar el riesgo, definido como el impacto ponderado por la tasa de ocurrencia
de la amenaza

Los activos se clasifican en:

* Esenciales:
    * servicios
    * información
* Subordinados:
    * datos que materializan la información
    * servicios auxiliares que se necesitan para poder organizar el sistema
    * aplicaciones informáticas (software) que permiten manejar los datos
    * equipos informáticos (hardware) que permiten hospedar datos, aplicaciones
    y servicios
    * soportes de información que son dispositivos de almacenamiento de datos
    * equipamiento auxiliar que complementa el material informático
    * redes de comunicaciones que permiten intercambiar datos
    * instalaciones que acogen equipos informáticos y de comunicaciones
    * personas que explota u operan todos los elementos anteriores

| Activo | Amenaza | Vulnerabilidad | Impacto | Riesgo | Dimensión |
|--------|---------|----------------|---------|--------|-----------|
| Subsistama A | Que los organismos no cumplan la obligación | Baja | Alto | Medio | D |
| ^ | Problemas de sincronización | Baja | Medio | Medio | ACID |
| ^ | Código dañino en los datos | Baja | Medio | Medio | CID |
| Subsistema B | Suplantación de identidad del usuario | Baja | Medio | Medio | ACI |
| ^ | Ataques externos | Media | Medio | Medio | D |
| ^ | Corrupción de datos | Baja | Bajo | Medio | AI |
| Información | Manipulación o perdida de datos | Media | Medio | Medio | IDT |
| ^ | Destrucción de la información | Media | Alto | Medio | D |
| Comunicaciones y Hardware |Desastres naturales | Baja | Alto | Medio | IDT |
| ^ | Caídas de las redes | Media | Bajo | Medio | D |
| ^ | Interceptación de información | Media | Medio | Bajo | C |
| Sistemas externos | Interrupción de los servicios | Media | Alto | Alto | D |
