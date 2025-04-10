#Strings (Cadenas de texto)
#Integers (Números enteros)
#Floats (Números con decimales)
#Booleans /(True/False) 
"MAÑANA 11 DE MARZO DE 2025"
#List  (Listas)
#Tuples (Tuplas)
#Sets (Conjuntos)
#Dictionaries (Diccionarios)

"""Strings"""
# El tipo de dato string es una secuencia de caracteres
# Se pueden definir strings usando comillas simples o dobles
# Ejemplo:
name = "CódigoFacilito"
print(name) #imprime CódigoFacilito
print(type(name)) #imprime el tipo de dato de la variable name
# Strings pueden ser concatenados usando el operador +
# Ejemplo:
first_name = "Código"
last_name = 'Facilito' #Se puede usar comillas simples o dobles
#Se recomienda usar comillas simples para strings de una sola línea y comillas dobles para strings de varias líneas
print(first_name + " " + last_name) #imprime Código Facilito

"""Integers"""
# El tipo de dato entero es un número sin decimales
# Ejemplo:
age = 25
print(age) #imprime 25
print(type(age)) #imprime el tipo de dato de la variable age
# Se pueden realizar operaciones aritméticas con números enteros como suma, resta, multiplicación y división entre otros
# Ejemplo:
num1 = 10
num2 = 5
print(num1 + num2) #imprime 15

"""Floats"""
# El tipo de dato float es un número con decimales
# Ejemplo:
price = 9.99
print(price) #imprime 9.99
print(type(price)) #imprime el tipo de dato de la variable price
# Se pueden realizar operaciones aritméticas con números flotantes como suma, resta, multiplicación y división entre otros

"""Booleans"""
# El tipo de dato booleano es un tipo de dato que puede ser verdadero o falso
# Ejemplo:
is_active = True
print(is_active) #imprime True
print(type(is_active)) #imprime el tipo de dato de la variable is_active
# Se pueden realizar operaciones lógicas con booleanos como AND, OR y NOT entre otros
# Ejemplo:
is_admin = True
is_user = True
print(is_admin and is_user) #imprime True
print(is_admin or is_user) #imprime True
print(not is_admin) #imprime False

"""List"""
# Las listas son un tipo de dato que permite almacenar múltiples elementos
# Ejemplo:
fruits = ["apple", "banana", "cherry"]
print(fruits) #imprime ['apple', 'banana', 'cherry']
print(type(fruits)) #imprime el tipo de dato de la variable fruits

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
# Las tuplas son un tipo de dato que permite almacenar múltiples elementos
# Ejemplo:
colors = ("red", "green", "blue")
print(colors) #imprime ('red', 'green', 'blue')
print(type(colors)) #imprime el tipo de dato de la variable colors