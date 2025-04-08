'''
    Vamos ahora a implementar computacionalmente este modelo. Queremos definir las funciones:

    Ejercicio 1: Crear
    Implementá la función crear_album(figus_total) que devuelve un álbum (vector) vacío con figus_total espacios para pegar figuritas.

    Ejercicio 2: Incompleto
    ¿Cuál sería el comando de Python que nos dice si hay al menos un cero en el vector que representa el álbum? ¿Qué significa que haya al menos un cero en nuestro vector?

    Implementá la función album_incompleto(A) que recibe un vector y devuelve True si el álbum A no está completo y False si está completo.

    Esta función y la anterior son realmente sencillas --cada una puede escribirse en una sola línea. En otro contexto quizas podrías usar directamente esa línea y evitarte definir la función. Sin embargo, en esta etapa nos parece interesante que organices tu código definiendo estas funciones, por más que tengan solo una línea de código cada una.

    Ejercicio 3: Comprar
    Implementá una función comprar_figu(figus_total) que reciba el número total de figuritas que tiene el álbum (dado por el parámetro figus_total) y devuelva un número entero aleatorio que representa la figurita que nos tocó.

    Ejercicio 4: Cantidad de compras
    Implementá la función cuantas_figus(figus_total) que, dado el tamaño del álbum (figus_total), genere un álbum nuevo, simule su llenado y devuelva la cantidad de figuritas que se debieron comprar para completarlo.

    Ejercicio 5:
    Ejecutá n_repeticiones = 1000 veces la función anterior utilizando figus_total = 6 y guardá en una lista los resultados obtenidos en cada repetición. Con los resultados obtenidos estimá cuántas figuritas hay que comprar, en promedio, para completar el álbum de seis figuritas.

    Ayuda: la media o promedio se calcula como la suma de todos los elementos divididos la cantidad.

    Ejercicio 6:
    Escribí una función llamada experimento_figus(n_repeticiones, figus_total) que simule el llenado de n_repeticiones álbums de figus_total figuritas y devuelva el número estimado de figuritas que hay que comprar, en promedio, para completar el álbum.

    Para esto, una posibilidad es que la función experimento_figus() llame a la función cuantas_figus() tantas veces como lo indica el parámetro n_repeticiones y guarde los resultados parciales en una lista, a partir de la cual luego realice el promedio.

    ¿Cuál es el resultado para 100 repeticiones en un álbum de 860 figuritas?

    Ahora con paquetes de figuritas
    ¿Cómo impacta en lo realizado tener paquetes con figuritas en lugar de figus sueltas?
    ¿Cómo puede representarse un paquete?
    Ejercicios con paquetes
    Ejercicio 7:
    Simulá la generación de un paquete con cinco figuritas, sabiendo que el álbum es de 860. Tené en cuenta que, como en la vida real, puede haber figuritas repetidas en un paquete.

    Ejercicio 8:
    Implementá una función comprar_paquete(figus_total, figus_paquete) que, dado el tamaño del álbum (figus_total) y la cantidad de figuritas por paquete (figus_paquete), genere un paquete (lista) de figuritas al azar.

    Ejercicio 9:
    Implementá una función cuantos_paquetes(figus_total, figus_paquete) que dado el tamaño del álbum y la cantidad de figus por paquete, genere un álbum nuevo, simule su llenado y devuelva cuántos paquetes se debieron comprar para completarlo.

    Ejercicio 10:
    Calculá n_repeticiones = 100 veces la función cuantos_paquetes, utilizando figus_total = 860, figus_paquete = 5. Guarda los resultados obtenidos en una lista y calculá su promedio. Si los recursos de la computadora lo permiten, hacelo con 1000 repeticiones.

    No olvides guardar todo en un archivo figuritas.py. Tené en cuenta que el archivo que entregues debe poder ser importado para testear la función experimento_figus() sin que se ejecuten comandos no deseados.
'''

import random
'''
Ejercicio 1: Crear
    Implementá la función crear_album(figus_total) que devuelve un álbum (vector) vacío con 
    figus_total espacios para pegar figuritas.
'''

def crear_album(figus_total):
    output = []
    [output.append(0) for x in range(figus_total)]
    return output

'''    while (figus_total>0):
        figus_total=figus_total-1
        output.append(0)
'''

'''
    Ejercicio 2: Incompleto
    ¿Cuál sería el comando de Python que nos dice si hay al menos un cero en el vector 
    que representa el álbum? ¿Qué significa que haya al menos un cero en nuestro vector?
'''

def incompleto(album):
    return 0 in album



'''
    Ejercicio 3: Comprar
    Implementá una función comprar_figu(figus_total) que reciba el número total de figuritas 
    que tiene el álbum (dado por el parámetro figus_total) y devuelva un número entero aleatorio que 
    representa la figurita que nos tocó.

'''

def comprar_figu(figus_total):
    return random.randint(0,figus_total-1)

'''
Ejercicio 4: Cantidad de compras
    Implementá la función cuantas_figus(figus_total) que, dado el tamaño del álbum (figus_total), 
    genere un álbum nuevo, simule su llenado y devuelva la cantidad de figuritas que se debieron comprar para completarlo.
'''

def cuantas_figus(figus_total):
    mi_album=crear_album(figus_total)
    while incompleto(mi_album):
        figu = comprar_figu(figus_total)
        mi_album[figu] = mi_album[figu] + 1
    return sum(mi_album)



'''    Ejercicio 5:
    Ejecutá n_repeticiones = 1000 veces la función anterior utilizando figus_total = 6
     y guardá en una lista los resultados obtenidos en cada repetición. 
     Con los resultados obtenidos estimá cuántas figuritas hay que comprar, en promedio, 
     para completar el álbum de seis figuritas.
'''

def promedio_compra(n_repeticiones,figus_total):
    acumulador = 0
    i= 0
    while i<n_repeticiones:
        acumulador = acumulador + cuantas_figus(figus_total)
        i=i+1
    return acumulador/n_repeticiones

     
'''Ejercicio 6:
    Escribí una función llamada experimento_figus(n_repeticiones, figus_total)
    que simule el llenado de n_repeticiones álbums de figus_total figuritas y
    devuelva el número estimado de figuritas que hay que comprar, en promedio, para completar el álbum.
'''

def experimento_figus(n_repeticiones, figus_total):
    acumulador = 0
    i= 0
    while i<n_repeticiones:
        acumulador = acumulador + promedio_compra(n_repeticiones,figus_total)
        i=i+1
    return acumulador/n_repeticiones


'''Ejercicio 7:
    Simulá la generación de un paquete con cinco figuritas, sabiendo que el álbum es de 860. 
    Tené en cuenta que, como en la vida real, puede haber figuritas repetidas en un paquete.

'''

def sim_generar_paquete(figus_total):
    figus = []
    for i in range(5):
        figus.append(comprar_figu(figus_total))
    return figus


''' Ejercicio 8:
    Implementá una función comprar_paquete(figus_total, figus_paquete) que,
    dado el tamaño del álbum (figus_total) y la cantidad de figuritas por paquete (figus_paquete), 
    genere un paquete (lista) de figuritas al azar.
'''
def comprar_paquete(figus_total, figus_paquete):
    figus = []
    for i in range(figus_paquete):
        figus.append(comprar_figu(figus_total))
    return figus


'''Ejercicio 9:
    Implementá una función cuantos_paquetes(figus_total, figus_paquete) 
    que dado el tamaño del álbum y la cantidad de figus por paquete, 
    genere un álbum nuevo, simule su llenado y devuelva cuántos paquetes se debieron comprar para completarlo.
'''

def cuantos_paquetes(figus_total, figus_paquete) :
    mi_album=crear_album(figus_total)
    while incompleto(mi_album):
        paquete = comprar_paquete(figus_total,figus_paquete)
        for figu in paquete:
            mi_album[figu] = mi_album[figu] + 1
    return sum(mi_album)/figus_paquete



'''Ejercicio 10:
    Calculá n_repeticiones = 100 veces la función cuantos_paquetes,
    utilizando figus_total = 860, figus_paquete = 5. 
    Guarda los resultados obtenidos en una lista y calculá su promedio.
    Si los recursos de la computadora lo permiten, hacelo con 1000 repeticiones.

'''

var_n_repeticiones = 1000
var_figus_total = 860
var_figus_paquete = 5

lista_paquetes=[]

for i in range(var_n_repeticiones):
    lista_paquetes.append(cuantos_paquetes(var_figus_total,var_figus_paquete))
promedio_paquetes = sum(lista_paquetes)/var_n_repeticiones
print(promedio_paquetes)
print(f"Deberás comprar {promedio_paquetes} paquetes, equivalente a {promedio_paquetes*5} figuritas para llenar un album de {var_figus_total} figuritas.")
