# Exploración de árboles urbanos en parques

Este análisis busca responder preguntas clave sobre la flora de los parques porteños, utilizando un dataset provisto por el GCBA. Las funciones analizan un archivo con información de árboles y agrupan los datos por parque.


## Preguntas exploradas

1. ¿Cuál es el parque con más árboles?
2. ¿Cuál es el parque con los árboles más altos en promedio?
3. ¿Cuál es el parque con mayor variedad de especies?
4. ¿Cuál es la especie más común en toda la ciudad?
5. ¿Cuál es la proporción entre especies exóticas y autóctonas?

## Soluciones usadas

Se generaron distintos scripts con el fin de obtener más detalles sobre la flora de GCBA.

### `def parque_mas_poblado(archivo_parques)`
* Recibe como parámetro el path del archivo local de los árboles de la ciudad y retorna el nombre del parque con **mayor cantidad de árboles registrados**.  
* La función construye un diccionario agrupando por nombre de parque y cuenta la cantidad de árboles por cada uno.

---

### `def parque_mas_alto(archivo_parques)`
* Recibe como parámetro el archivo de datos y retorna el nombre del parque con **mayor altura promedio** de sus árboles.  
* Para cada parque, calcula el promedio de la columna `altura_tot` y luego selecciona el de mayor valor.

---

### `def parque_mas_variado(archivo_parques)`
* Retorna el nombre del parque con **mayor variedad de especies de árboles**.  
* Agrupa los árboles por parque y dentro de cada uno calcula cuántas especies distintas (`id_especie`) existen.  
* Luego ordena por cantidad y devuelve el de mayor diversidad.

---

### `def arbol_mas_popular_ciudad(archivo_parques)`
* Identifica la **especie con mayor cantidad de ejemplares en toda la ciudad**, sin importar el parque.  
* Agrupa por `nombre_cie` (nombre científico de la especie) y devuelve la que más se repite.

---

### `def especies_autoctonas(archivo_parques)`
* Calcula la **proporción de árboles autóctonos** con respecto al total de árboles registrados.  
* Se usa la columna `origen`, y se cuenta cuántos son `Nativo/Autóctono` en relación al total.  
* El resultado es un valor entre 0 y 1 que representa el porcentaje de especies autóctonas en la ciudad.

---

> Nota: Todas las funciones hacen uso del archivo `arbolado-en-espacios-verdes.csv` provisto por el GCBA, el cual contiene datos detallados por árbol, incluyendo especie, altura, origen y ubicación.
