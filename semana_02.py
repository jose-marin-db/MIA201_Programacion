
'''Ejercicio 1'''
lista = [1, 2, 3, 4, 5]
lista_nombres = ['Bogotá', 'Rosario', 'San Fernando', 'San Miguel']

def invertirLista(l):
    i=len(l)-1
    t=[]
    while i>=0:
        t.append(l[i])
        i=i-1
    return t

def inverirListaRec(l):
    if(len(l)==1):
        return l
    else:
        return invertirLista(l[1:])+ l[0:1]

lista_invertida = inverirListaRec(lista_nombres)
print(lista_invertida)


'''
Ejercicio 2:
'''
def Collatz(n):
    if(n%2==0 and n!=0):
        n=n/2
    else:
        n=n*3+1
    if(n==1):
        return n
    else:
        return Collatz(n)+1
        

resultado = Collatz(0)
print(resultado)

'''
Ejercicio 3:
'''
diccionario = {"luno":["resto","resto2"],"dos":["resto"]}

def contar_definiciones(dic):
    dic_out ={}
    for key in dic:
        dic_out[key] = len(dic[key])
    return dic_out

t = contar_definiciones(diccionario)
print(t)

def cantidad_de_claves_letra(dic, letra):
    cont = 0
    for key in dic:
        if key[0].lower()==letra.lower():
            cont=cont+1
    return cont

c = cantidad_de_claves_letra(diccionario, "l")

print(c)


'''

#EJERCICIO 4:

0= nuevo
1= prendido
-1= quemado

'''

nuevo=0
prendido = 1
quemado = -1


def propagar(fosforos, fuego=False):
    actual= fosforos[0]
    if(len(fosforos)==1):
        if (actual== prendido or actual == quemado or (actual ==nuevo and not fuego)):
            return [actual]
        else:
            return [prendido]
    else:      
        if actual== prendido:
            return [prendido] + (propagar(fosforos[1:],True))
        elif actual == quemado:
            return [quemado] + (propagar(fosforos[1:],False))
        else:
            if actual == nuevo:
                if fuego:
                    return [prendido] + (propagar(fosforos[1:],True))
                elif len(fosforos)==1:
                    return [actual]  
                else:
                    if(fosforos[1]==prendido):
                        return [prendido] + (propagar(fosforos[1:],True))
                    else:
                        vuelta = (propagar(fosforos[1:],False))
                        if vuelta[0]==prendido:
                            return [prendido] +  vuelta
                        else:
                            return [actual] +  vuelta



    

propagado = propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
print(propagado)
propagado = propagar([ 0, 0, 0, 1, 0, 0])
print(propagado)