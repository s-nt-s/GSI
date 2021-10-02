---
title: Tipos y algoritmos
status: draft
---

# Conceptos básicos

**TAD**:
conjunto de valores y de operaciones definidos
mediante una especificación independiente de cualquier representación.

**Algoritmo**: conjunto de pasos o instrucciones que se deben seguir para realizar
una determinada tarea.

# [Cota superior asintótica](https://es.wikipedia.org/wiki/Cota_superior_asint%C3%B3tica)

Concepto matemático usado para estimar el **tiempo o coste de ejecución** de un algoritmo
(también puede aplicar a las operaciones de la implementación de TAD) en función
del tamaño del dato de entrada.

Por ejemplo, el *ordenamiento por inserción* crece cuadráticamente a medida que
aumenta el tamaño de entrada, por lo tanto este algoritmo es de tipo `O(n²)`
(orden de n cuadrado).

| Notación      | Nombre |
|---------------|--------|
| O(1)          | Orden constante |
| O(log log n)  | Orden sublogarítmico |
| O(log n)      | Orden logarítmico |
| O(√n)         | Orden sublineal |
| O(n)          | Orden lineal o de primer orden |
| O(n log n)    | Orden lineal logarítmica |
| O(n²)         | Orden cuadrática o de segundo orden |
| O(n³), ...    | Orden cúbica o de tercer orden, ... |
| O(c^n), n > 1 | Orden exponencial |
| O(n!)         | Orden factorial |

Tabla: Ordenes de complejidad de menor a mayor <span class="complejidad_nombre"></span>

Pero la complejidad no solo depende del tamaño del dato de entrada, si no
de que dato en concreto es, por lo tanto [tenemos 3 casos](https://es.wikipedia.org/wiki/Casos_peor,_mejor_y_promedio)
(ej: buscar secuencialmente un elemento en una lista):

* el **caso mejor**: `Ω(1)` = el elemento buscado es el primero
* el **caso peor**: `Θ(n)` = el elemento buscado es el último
* el **caso esperado o promedio**: `O(n/2)` = puesto que todas la posiciones son equiprobables

Por lo general, se considera el caso promedio.

También se puede medir la **[complejidad espacial](https://en.wikipedia.org/wiki/Space_complexity)**,
que es la cantidad de memoria requerida para ejecutar el algoritmo.

| Algoritmo      | Caso  | <        | <    | Observaciones |
|----------------|-------|----------|------|---------------|
| ^              | mejor | promedio | peor | ^             |
| Quicksort      | Ω(n log n) | Θ(n log n) | O(n²) | |
| Mergesort      | Ω(n log n) | Θ(n log n) | O(n log n) | |
| Timsort        | Ω(n) | Θ(n log n) | O(n log n) | |
| Heapsort       | Ω(n log n) | Θ(n log n) | O(n log n) | |
| Bubble Sort    | Ω(n) | Θ(n²) | O(n²) | |
| Insertion Sort | Ω(n) | Θ(n²) | O(n²) | |
| Selection Sort | Ω(n²) | Θ(n²) | O(n²) | |
| Tree Sort      | Ω(n log n) | Θ(n log n) | O(n²) | |
| Shell Sort     | Ω(n log n) | Θ(n log²n) | O(n log²n) | |
| Bucket Sort    | Ω(n+k) | Θ(n+k) | O(n²) | k = nº de buckets |
| Radix Sort     | Ω(nk) | Θ(nk) | O(nk) | k = nº de digitos |
| Counting Sort  | Ω(n+k) | Θ(n+k) | O(n+k) | k = max - min |
| Cubesort       | Ω(n) | Θ(n log n) | O(n log n) | |

Tabla: Complejidad de algoritmos de ordenación <span class="complejidad_ordenacion"></span>

| TAD | Acceso | Búsqueda | Inserción | Borrado |
|-----|--------|----------|-----------|---------|
| [Array](https://es.wikipedia.org/wiki/Vector_(inform%C3%A1tica)) | Θ(1) | Θ(n) | Θ(n) | Θ(n) |
| [Pila](https://es.wikipedia.org/wiki/Pila_(inform%C3%A1tica)) | Θ(n) | Θ(n) | Θ(1) | Θ(1) |
| [Cola](https://es.wikipedia.org/wiki/Cola_(inform%C3%A1tica)) | Θ(n) | Θ(n) | Θ(1) | Θ(1) |
| [Lista enlazada<br/>simple circular](https://es.wikipedia.org/wiki/Lista_enlazada#Listas_enlazadas_simples_circulares) | Θ(n) | Θ(n) | Θ(1) | Θ(1) |
| [Lista enlazda<br/>doblemente circular](https://es.wikipedia.org/wiki/Lista_enlazada#Listas_enlazadas_doblemente_circulares) | Θ(n) | Θ(n) | Θ(1) | Θ(1) |
| [Skip List](https://es.wikipedia.org/wiki/Skip_list) | Θ(log n) | Θ(log n) | Θ(log n) | Θ(log n) |
| └─ *caso peor*                                     | O(n)      | O(n)      | O(n)      | O(n) |
| [Tabla Hash](https://es.wikipedia.org/wiki/Tabla_hash) | | Θ(1) | Θ(1) | Θ(1) |
| └─ *caso peor*                                       | | O(n) | O(n) | O(n) |
| [Árbol binario de busqueda](https://es.wikipedia.org/wiki/%C3%81rbol_binario_de_b%C3%BAsqueda) | Θ(log n) | Θ(log n) | Θ(log n) | Θ(log n) |
| └─ *caso peor*                                                       | O(n)      | O(n)      | O(n)      | O(n) |
| [Árbol cartesiano](https://es.wikipedia.org/wiki/%C3%81rbol_cartesiano) | | Θ(log n) | Θ(log n) | Θ(log n) |
| └─ *caso peor*                                                | | O(n)      | O(n)      | O(n) |
| [B-Tree](https://es.wikipedia.org/wiki/%C3%81rbol-B) | Θ(log n) | Θ(log n) | Θ(log n) | Θ(log n) |
| [Árbol rojo-negro](https://es.wikipedia.org/wiki/%C3%81rbol_rojo-negro) | Θ(log n) | Θ(log n) | Θ(log n) | Θ(log n) |
| [Árbol biselado](https://es.wikipedia.org/wiki/%C3%81rbol_biselado) | | Θ(log n) | Θ(log n) | Θ(log n) |
| [Árbol AVL](https://es.wikipedia.org/wiki/%C3%81rbol_AVL) | Θ(log n) | Θ(log n) | Θ(log n) | Θ(log n) |
| [Árbol KD](https://es.wikipedia.org/wiki/%C3%81rbol_kd) | Θ(log n) | Θ(log n) | Θ(log n) | Θ(log n) |
| └─ *caso peor*                                  | O(n)      | O(n)      | O(n)      | O(n) |

Tabla: Complejidad de operaciones sobre TAD (*caso peor* omitido cuando coincide con el *caso promedio*)  <span class="complejidad_tad"></span>

# TAD

Tienen tres tipos de operaciones:

* Creación
* Transformación: asignación de valores, permutas, etc
* Análisis: consultar valor, búsquedas, recorridos, etc

# Bibliografía

* [gsitic.wordpress.com - B3]({filename}/posts/gsitic.wordpress.com/bloque_3.md#tablas,-listas-y-arboles)
* [webdiis.unizar.es - Los Tipos Abstractos de Datos](http://webdiis.unizar.es/~elvira/eda/material0304/TADespec/TAD.pdf)
* [cs.us.es - Análisis de la complejidad de los algoritmos](https://www.cs.us.es/~jalonso/cursos/i1m-19/temas/tema-28.html)
* [infor.uva.es - Complejidad algorítmica](https://www2.infor.uva.es/~jvalvarez/docencia/tema5.pdf)
* [bigocheatsheet.com](https://www.bigocheatsheet.com/)
