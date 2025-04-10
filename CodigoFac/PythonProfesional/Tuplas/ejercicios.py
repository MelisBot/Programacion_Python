"""
Define una tupla de Longitud 3 (Cualquier tipo de dato) e imprime en consola el último elemento.
El nombre de la tupla debe ser my_tuple.
"""
my_tuple = (1, "a", True)
print(my_tuple[-1]) #imprime True

"""
Define una tupla de longitud 5 (Cualquier tipo de dato) y usando tuple unpacking genera 3 nuevas
variables para, el primer, penúltimo y el último elemento. Imprime dichas variables en consola.
La tupla debe tener por nombre my_tuple.
"""
my_tuple = (1, "b", 3.14, False, "z")
first, *_, penultimate, last = my_tuple
print(first)       # imprime 1
print(penultimate) # imprime False
print(last)        # imprime "z"

""""
Usando la siguiente lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
genera una tupla llamada pares. Imprime dicha tupla en consola.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = tuple([i for i in numbers if i % 2 == 0])
print(pares) #imprime (2, 4, 6, 8, 10)


