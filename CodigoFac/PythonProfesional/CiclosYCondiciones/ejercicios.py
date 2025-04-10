"""
Crea una lista de longitud 10. Utilizando un ciclo for-each
imprime en consola todos los números pares mayores a 5. 
La lista debe tener por nombre my_list.
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in my_list:
    if number > 5 and number % 2 == 0:
        print(number) 

"""
Define una variable de tipo string llamada sentence. Utilizando un ciclo while, imprime la cantidad de caracteres que posee la variable hasta encontrar un punto (.).
E.g

sentence = "Hola mundo. Curso de Python."
>>> 10
"""
sentence = "Hola mundo. Curso de Python."
counter = 0
while sentence[counter] != ".":
    counter += 1
print(counter)

"""
Crea una lista de longitud 5 que contengan tuplas de 2 elementos de números enteros. (e.g (10, 20) ) . Utilizando un ciclo for-each, imprime en consola las tuplas. Cada impresión en consola (Una por cada elemento) debe seguir el siguiente formato: ‘{first_element} - {second_element}’. La lista debe tener por nombre: my_list
E.g

my_list = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

>>> 1 - 2
>>> 3 - 4
>>> 5 - 6
>>> 7 - 8
>>> 9 - 10
"""
my_list = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
for first_element, second_element in my_list:
    print(f"{first_element} - {second_element}")

    
