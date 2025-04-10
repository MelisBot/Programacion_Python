"""
Define una función que permita retornar el cubo de un número.
La función debe tener por nombre “cubo” y debe recibir como
argumento un número entero.
"""
def cubo(n):
    return n ** 3

"""
Define una función que permita conocer cuantas vocales posee un string. 
La función debe tener por nombre “vocales” y debe recibir como argumento un string.
La función debe retornar la cantidad de vocales que dicho string posee.
"""
def vocales(string):
    vocales = 0
    for i in string:
        if i in "aeiou":
            vocales += 1
    return vocales
"""
Define un función llamada “promedio” que permita calculas el promedio de una lista.
La función debe recibir como argumento una lista de números enteros y retornar el promedio de dicha lista.

"""
def promedio(lista):
    return sum(lista) / len(lista) 

"""
Define una función que permita conocer si el primer y último elemento de una lista
 son el mismo elemento. La función debe tener por nombre “iguales”. 
 La función debe recibir como argumento una lista de números enteros con longitud 
 mayor a 2. La función debe retornar verdadero o falso si el primer y último 
 elemento son el mismo número.
- Si la función recibe una lista con 2 o menos elementos retornará None.
"""
def iguales(lista):
    if len(lista) <= 2:
        return None
    return lista[0] == lista[-1]

"""
Define una función que nos permita conocer si todos los elementos de una lista 
son el mismo. La función debe tener por nombre “iguales” y debe recibir como
 argumento un listado de números enteros. La función debe retornar True o False
   si todos los elementos de la lista son el mimos.
- La función retornará None si la lista se encuentra vacía o solo posee un elemento.
"""
def iguales(lista):
    if len(lista) < 2:
        return None
    return all([i == lista[0] for i in lista])
