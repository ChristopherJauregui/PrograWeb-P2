# Función que reciba un diccionario y agregar una clave-valor, retornar el diccionario modificado (Debe agregarlo al final)
'''dicc = {'Clave1': 'Valor1', 'Clave2': 'Valor2', 'Clave3': 'Valor3'}
print(dicc)
dicc['Clave4'] = 'Valor4'
print(dicc)'''

#Función que reciba un diccionario y elimine una clave-valor, retornar el diccionario modificado
'''print(dicc)
del dicc['Clave2'] 
print(dicc)'''
#Función que reciba un diccionario y modifique el valor de una clave, retornar verdadero si pudo modificar y falso si no pudo
'''dicc = {'Clave1': 'Valor1', 'Clave2': 'Valor2', 'Clave3': 'Valor3'}
print(dicc)
print("----------------------")
def Modificar(dicc):
    clave = input("Clave a modificar: ")
    newValor = input("Nuevo valor: ")
    if clave in dicc:
        dicc[clave] = newValor
        return True
    else:
        return False

if Modificar(dicc):
    print("Se ha modificado corretamente.")
    print(dicc)
else:
    print("La clave especificada no existe en el diccionario.")'''
#Función que combine dos diccionarios, regresar el diccionario resultante
'''dicc = {'Clave1': 'Valor1', 'Clave2': 'Valor2', 'Clave3': 'Valor3'}
dicc2 = {'Clave4': 'Valor4', 'Clave5': 'Valor5', 'Clave6': 'Valor6'}

def combinar(dicc,dicc2):
    dicc3 = {**dicc,**dicc2}
    return dicc3

print(dicc)
print(dicc2)
print("----------------------")
print(combinar(dicc,dicc2))'''
#Función que agregue elementos a un conjunto, retornar verdadero si pudo agregar y falso si no pudo.
'''conj = {1, 2, 3, 4, 5}

def addElem(conjunto):
    elemento = input("Nuevo elemento: ")
    if int(elemento) not in conjunto:
        conjunto.add(int(elemento))
        return True
    else:
        return False
    
if addElem(conj):
    print("Elemento agregado con éxito.")
    print(conj)
else:
    print("El elemento ya existe en el conjunto.")'''
#Función que elimine un elemento de un conjunto, retornar verdadero si pudo eliminar y falso si no pudo
'''conj = {1, 2, 3, 4, 5}
print(conj)
def eliminar_elemento(conjunto):
    elemento = input("Elemento a eliminar: ")
    if int(elemento) in conjunto:
        conjunto.discard(int(elemento))
        return True
    else:
        return False
    
if eliminar_elemento(conj):
    print("Elemento eliminado con éxito.")
    print(conj)
else:
    print("El elemento no existe en el conjunto.")'''
#Función que combine dos conjuntos, regresar el conjunto resultante
'''conj1={1,2,3,4,5}

conj2={6,7,8,9,10}

def Combinar(c1, c2):
    conj3 = c1.union(c2)
    return conj3

print(conj1)
print(conj2)
print("----------------------")
print(Combinar(conj1,conj2))'''
#Función que regrese la diferencia de dos conjuntos
'''conj1={1,2,3,4,5}
conj2={1,3,5,7,9}

def diferencia(c1, c2):
    diferencia = c1.difference(c2)
    return diferencia

print(conj1)
print(conj2)
print("----------------------")
print(diferencia(conj1,conj2))'''
#Función que agregue un elemento a una tupla y lo guarde los cambios en una tupla nueva, regresar la nueva tupla
'''tupla = ('id', 'nombre', 'clasificacion')

def agregar_a_tupla(tupla):
    elemento = input("Ingresa el elemento a agregar: ")
    newtupla = tupla + (elemento,)
    return newtupla
print(tupla)
print("----------------------")
print(agregar_a_tupla(tupla))'''
#Función que elimine un elemento a una tupla y lo guarde los cambios en una tupla nueva, regresar la nueva tupla
'''tupla = ('id', 'nombre', 'clasificacion')

def borrar_a_tupla(tupla):
    elemento = input("Ingresa el elemento a eliminar: ")
    newtupla = tuple(e for e in tupla if e != elemento)
    return newtupla
print(tupla)
print("----------------------")
print(borrar_a_tupla(tupla))'''
#Función que concatene dos tuplas en una nueva, regresar la nueva tupla
'''tupla1 = ('id', 'nombre', 'clasificacion')
tupla2 = ('direccion', 'telefono', 'email')

def concatenar(tupla1,tupla2):
    lista1 = list(tupla1)
    lista2 = list(tupla2)
    nueva_lista = lista1 + lista2
    nvatupla = tuple(nueva_lista)
    return nvatupla

print(tupla1)
print(tupla2)
print("----------------------")
print(concatenar(tupla1, tupla2))'''
#Función que revertir el orden de una tupla y lo guarde los cambios en una tupla nueva, regresar la nueva tupla
'''tupla = ('id', 'nombre', 'idclasificacion')

def invertir(tupla):
    invtupla = tuple(reversed(tupla))
    return invtupla

print(tupla)
print("----------------------")
print(invertir(tupla))'''
#Función que recibe un diccionario y lo imprime
'''dicc = {'Clave1': 'Valor1', 'Clave2': 'Valor2', 'Clave3': 'Valor3'}

def Imprimir(dicc):
    print(dicc)

Imprimir(dicc)'''
#Función que recibe un tupla y la imprime
'''tupla = ('id', 'nombre', 'idclasificacion')

def Imprimir(tupla):
    print(tupla)

Imprimir(tupla)'''
#Función que recibe un conjunto y lo imprime
'''Conj={1,3,5,7,9}

def Imprimir(Conj):
    print(Conj)

Imprimir(Conj)'''
