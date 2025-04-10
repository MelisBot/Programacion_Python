#Info para clase Marte 11 de Marzo de 2025
"""Tipo de datos dinamicos en Python

Python es un lenguaje de programación de tipado dinámico, lo que significa que no es necesario declarar el tipo de dato
de una variable al crearla, el tipo de dato se asigna automáticamente al valor que se le asigna a la variable.

Los tipos de datos dinamicos en Python son:
- Enteros: Números sin decimales
- Flotantes: Números con decimales
- Booleanos: Verdadero o Falso
- Strings: Secuencia de caracteres
- Listas: Colección de elementos mutables
- Tuplas: Colección de elementos inmutables
- Conjuntos: Colección de elementos únicos
- Diccionarios: Colección de elementos que se almacenan en pares clave-valor

"""

"""List"""
# Las listas son un tipo de dato que permite almacenar múltiples elementos en una sola variable 
# Ejemplo:
fruits = ["apple", "banana", "cherry"]
print(fruits) #imprime ['apple', 'banana', 'cherry']
print(type(fruits)) #imprime el tipo de dato de la variable fruits
# Las listas pueden contener elementos de diferentes tipos de datos como enteros, flotantes, booleanos, strings, listas, tuplas, conjuntos y diccionarios.

#Métodos de las listas
#append(): Agrega un elemento a la lista
#remove(): Elimina un elemento de la lista
#pop(): Elimina el último elemento de la lista
#clear(): Elimina todos los elementos de la lista
#copy(): Devuelve una copia de la lista
#index(): Devuelve el índice de un elemento en la lista
#insert(): Inserta un elemento en una posición específica de la lista
#count(): Cuenta el número de veces que un elemento aparece en la lista
#sort(): Ordena los elementos de la lista
#reverse(): Invierte el orden de los elementos de la lista
#extend(): Agrega los elementos de una lista a otra lista
#copy(): Devuelve una copia de la lista
#len(): Devuelve la longitud de la lista
#max(): Devuelve el elemento más grande de la lista
#min(): Devuelve el elemento más pequeño de la lista
#sum(): Devuelve la suma de los elementos de la lista

# Se puede acceder a los elementos de una lista usando su índice
# Ejemplo:
print(fruits[0]) #imprime apple
print(fruits[1]) #imprime banana
print(fruits[2]) #imprime cherry
# Se puede agregar un elemento a una lista usando el método append()
# Ejemplo:
fruits.append("orange")
print(fruits) #imprime ['apple', 'banana', 'cherry', 'orange']
# Se puede eliminar un elemento de una lista usando el método remove()
# Ejemplo:
fruits.remove("banana")
print(fruits) #imprime ['apple', 'cherry', 'orange']

"""Tuples"""
# Las tuplas un tipo de dato que permite almacenar múltiples elementos en una sola variable
# Las tuplas son inmutables, es decir, no se pueden modificar después de su creación
# Ejemplo:
colors = ("red", "green", "blue")
print(colors) #imprime ('red', 'green', 'blue')
print(type(colors)) #imprime el tipo de dato de la variable colors

#Métodos de las tuplas
#count(): Cuenta el número de veces que un elemento aparece en la tupla
#index(): Devuelve el índice de un elemento en la tupla
#len(): Devuelve la longitud de la tupla
#max(): Devuelve el elemento más grande de la tupla
#min(): Devuelve el elemento más pequeño de la tupla
#sum(): Devuelve la suma de los elementos de la tupla
# Las tuplas son inmutables, es decir, no se pueden modificar después de su creación.

"""Sets"""
# Los conjuntos son un tipo de dato que permite almacenar elementos únicos
# Ejemplo:
fruits_set = {"apple", "banana", "cherry"}
print(fruits_set) #imprime {'apple', 'banana', 'cherry'}

#Métodos de los conjuntos
#add(): Agrega un elemento al conjunto
#remove(): Elimina un elemento del conjunto
#clear(): Elimina todos los elementos del conjunto
#copy(): Devuelve una copia del conjunto
#difference(): Devuelve la diferencia entre dos conjuntos
#intersection(): Devuelve la intersección entre dos conjuntos
#union(): Devuelve la unión entre dos conjuntos
# Se puede acceder a los elementos de un conjunto usando un bucle for o el método for loop
# Ejemplo:
for fruit in fruits_set:
    print(fruit)
    # Se puede agregar un elemento a un conjunto usando el método add()
    # Ejemplo:
    fruits_set.add("orange")
    print(fruits_set) #imprime {'apple', 'banana', 'cherry', 'orange'}
# Los conjuntos no tienen un orden definido, por lo que no se puede acceder a los elementos de un conjunto mediante su índice.
# Los conjuntos no pueden contener elementos duplicados.
# Los conjuntos no pueden ser vacíos.

"""Diccionarios"""
# Los diccionarios son un tipo de dato que permite almacenar elementos que se almacenan en pares clave-valor
# Ejemplo:
person = {"name": "John", "age": 30, "is_active": True}
print(person) #imprime {'name': 'John', 'age': 30, 'is
#Métodos de los diccionarios
#clear(): Elimina todos los elementos del diccionario
#copy(): Devuelve una copia del diccionario
#get(): Devuelve el valor asociado a una clave
#items(): Devuelve una lista de pares clave-valor del diccionario
#keys(): Devuelve una lista de las claves del diccionario
#pop(): Elimina un elemento del diccionario
#popitem(): Elimina el último elemento del diccionario
#update(): Actualiza el diccionario con los elementos de otro diccionario
#values(): Devuelve una lista de los valores del diccionario
# Se puede acceder a los elementos de un diccionario usando su clave
# Ejemplo:
print(person["name"]) #imprime John
print(person["age"]) #imprime 30
print(person["is_active"]) #imprime True
# Se puede agregar un elemento a un diccionario usando el método update()
# Ejemplo:
person.update({"city": "New York"})
print(person) #imprime {'name': 'John', 'age': 30, 'is_active': True, 'city': 'New York'}
# Los diccionarios pueden contener elementos duplicados.
# Los diccionarios pueden ser vacíos.
# Ejemplo de uso de un diccionario para almacenar información de un usuario
user = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "is_active": True
}
print(user["first_name"] + " " + user["last_name"]) #imprime John Doe
# Se puede acceder a los elementos de un diccionario usando un bucle for
# Ejemplo:
for key, value in user.items():
    print(key + ": " + str(value))

"""Strings"""
# Las cadenas de texto son un tipo de dato que permite almacenar secuencias de caracteres
# Ejemplo:
name = "John"
print(name) #imprime John
print(type(name)) #imprime el tipo de dato de la variable name

#Métodos de las cadenas de texto
#capitalize(): Convierte el primer carácter de la cadena en mayúsculas
#casefold(): Convierte la cadena a minúsculas
#center(): Centra la cadena en un ancho especificado
#count(): Cuenta el número de veces que aparece una subcadena en la cadena
#encode(): Codifica la cadena en un formato específico
#endswith(): Devuelve True si la cadena termina con una subcadena específica
#expandtabs(): Expande los tabuladores en la cadena
#find(): Devuelve la posición de la primera aparición de una subcadena en la cadena
#format(): Formatea la cadena con los argumentos especificados
#format_map(): Formatea la cadena con un diccionario
#index(): Devuelve la posición de la primera aparición de una subcadena en la cadena    
#isalnum(): Devuelve True si todos los caracteres de la cadena son alfanuméricos
#isalpha(): Devuelve True si todos los caracteres de la cadena son alfabéticos
#isascii(): Devuelve True si todos los caracteres de la cadena son ASCII
#isdecimal(): Devuelve True si todos los caracteres de la cadena son decimales
#isdigit(): Devuelve True si todos los caracteres de la cadena son dígitos
#isidentifier(): Devuelve True si la cadena es un identificador válido
#islower(): Devuelve True si todos los caracteres de la cadena están en minúsculas
#isnumeric(): Devuelve True si todos los caracteres de la cadena son numéricos
#isprintable(): Devuelve True si todos los caracteres de la cadena son imprimibles
#isspace(): Devuelve True si todos los caracteres de la cadena son espacios en blanco
#istitle(): Devuelve True si la cadena es un título
#isupper(): Devuelve True si todos los caracteres de la cadena están en mayúsculas
#join(): Une los elementos de una lista con la cadena
#ljust(): Justifica la cadena a la izquierda en un ancho especificado
#lower(): Convierte la cadena a minúsculas
#lstrip(): Elimina los espacios en blanco a la izquierda de la cadena
#partition(): Divide la cadena en tres partes
#replace(): Reemplaza una subcadena en la cadena
#rfind(): Devuelve la posición de la última aparición de una subcadena en la cadena
#rindex(): Devuelve la posición de la última aparición de una subcadena en la cadena
#rjust(): Justifica la cadena a la derecha en un ancho especificado
#rpartition(): Divide la cadena en tres partes
#rsplit(): Divide la cadena en una lista
#rstrip(): Elimina los espacios en blanco a la derecha de la cadena
#split(): Divide la cadena en una lista
#splitlines(): Divide la cadena en una lista en las líneas
#startswith(): Devuelve True si la cadena comienza con una subcadena específica
#strip(): Elimina los espacios en blanco de la cadena
#swapcase(): Convierte mayúsculas en minúsculas y viceversa
#title(): Convierte la primera letra de cada palabra en mayúsculas
#upper(): Convierte la cadena a mayúsculas
#zfill(): Rellena la cadena con ceros a la izquierda

# Se pueden concatenar cadenas de texto usando el operador + o el método join() de la cadena vacía "" 
# Ejemplo:
name = "John"
age = 30
print(name + " tiene " + str(age) + " años") #imprime "John tiene 30 años"
# Otra forma de concatenar cadenas de texto es usando el método join() de la cadena
# vacía "" y una lista de cadenas de texto
# Ejemplo:
name = "John"
age = 30
print(" ".join([name, "tiene", str(age), "años"])) #imprime "John tiene 30 años"
