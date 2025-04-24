import csv
import json
PATH_ARBOLES = "arbolado-en-espacios-verdes.csv"

def flora_parques(nombre_archivo):
    dicParques = {}
    with open(nombre_archivo, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for fila in reader:
            if fila['espacio_ve'] not in dicParques:
                dicParques[fila['espacio_ve']]={}
            dicParques[fila['espacio_ve']][fila['id_arbol']]=fila.copy()

    return dicParques


def arboles_parque(nombre_archivo, nombre_parque):
    dicArboles ={}
    with open(nombre_archivo, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for fila in reader:
            if fila['espacio_ve']==nombre_parque:
               dicArboles[fila['id_arbol']] = fila.copy()
    print(dicArboles)
    return dicArboles

def arbol_mas_popular(nombre_parque):
    dicContadores={}
    dicArboles =arboles_parque(PATH_ARBOLES, nombre_parque)
    for arbol in dicArboles.values():
        especie = arbol['id_especie']
        if especie in dicContadores:
            dicContadores[especie] =  dicContadores[especie] + 1
        else:
           dicContadores[especie] = 1

    ordenado = dict(sorted(dicContadores.items(), key=lambda x: x[1], reverse=True))
    return list(ordenado)[:1]


def n_mas_altos(nombre_parque, n):
    dicArboles =arboles_parque(PATH_ARBOLES, nombre_parque)
    ordenado = dict(sorted(dicArboles.items(), key=lambda item: item[1]['altura_tot']))
    return(list(ordenado)[:2])

def altura_promedio(nombre_parque, especie):
    dicArboles =arboles_parque(PATH_ARBOLES, nombre_parque)
    solo_especie = {key: value for key, value in dicArboles.items() if value['id_especie'] == especie}
    altura_promedio = sum(float(value['altura_tot']) for key,value in solo_especie.items()) / len(solo_especie)
    return altura_promedio


dicResult = altura_promedio("AVELLANEDA, NICOLÁS, Pres.", '11')

'''
El/los parques con más cantidad de árboles.
El/los parques con los árboles más altos en promedio.
El/los parques con más variedad de especies.
La especie que más ejemplares tiene en la ciudad.
La razón entre especies exóticas y autóctonas.
'''


def parque_mas_poblado(archivo_parques):
    dicParques = flora_parques(archivo_parques)
    dicParques = {k: v for k, v in dicParques.items() if k and k != 'S/D'}
    parque_mayor = max(dicParques, key=lambda p: len(dicParques[p]))
    return parque_mayor

def parque_mas_alto(archivo_parques):
    dicParques = flora_parques(archivo_parques)
    dicAlturas = {}
    dicParques = {k: v for k, v in dicParques.items() if k and k != 'S/D'}

    for nombre_parque, arboles in dicParques.items():
        alturas = sum(float(arbol['altura_tot']) for arbol in arboles.values() if arbol['altura_tot'])
        promedio = alturas / len(arboles)
        dicAlturas[nombre_parque] = promedio

    dicAlturas_ordenado = dict(sorted(dicAlturas.items(), key=lambda item: item[1], reverse=True))

    return list(dicAlturas_ordenado.items())[:1]  # [(parque, promedio)]

def parque_mas_variado(archivo_parques):
    dicParques = flora_parques(archivo_parques)
    dicVariedad = {}
    dicParques = {k: v for k, v in dicParques.items() if k and k != 'S/D'}

    for nombre_parque, arboles in dicParques.items():
        especies =  set(arbol['id_especie'] for _, arbol in arboles.items())
        dicVariedad[nombre_parque] = len(especies)
    dicVariedades_ordeano = dict(sorted(dicVariedad.items() , key=lambda item: item[1], reverse=True))
    return list(dicVariedades_ordeano.items())[:1]  # [(parque, promedio)]

def arbol_mas_popular_ciudad(archivo_parques):
    dicParques = flora_parques(archivo_parques)
    dicContadorEspecies = {}
    for nombre_parque, arboles in dicParques.items():
        for _, arbol in arboles.items():
            currentArbol = arbol['nombre_cie']
            if currentArbol not in dicContadorEspecies:
                dicContadorEspecies[currentArbol] = 1
            else:
                dicContadorEspecies[currentArbol]+=1
    dicOrdenado = dict(sorted(dicContadorEspecies.items() , key=lambda item: item[1], reverse=True))
    return list(dicOrdenado.items())[:1]  # [(parque, promedio)]

def especies_autoctonas(archivo_parques):
    dicParques = flora_parques(archivo_parques)
    dicOrigen = {}
    for nombre_parque, arboles in dicParques.items():
        for _, arbol in arboles.items():
            currentOrigen = arbol['origen']
            if currentOrigen not in dicOrigen:
                dicOrigen[currentOrigen] = 1
            else:
                dicOrigen[currentOrigen]+=1
    return round(dicOrigen['Nativo/Autóctono']/  sum(v for k,v in dicOrigen.items()),2)
 # [(parque, promedio)]

