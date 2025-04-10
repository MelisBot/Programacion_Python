#Imprimir un mensaje hola mundo
print("Hola Mundo, desde un script de Python.")

"""
Para hacer comentarios largos se utiliza triple comilla doble.
Este es un comentario largo.
"""
"""
Variables en Python
Las variables son contenedores de datos.
<Variable> = <Valor>
En Python, las variables no necesitan ser declaradas con ningún tipo en particular y pueden incluso
cambiar de tipo después de haber sido seteadas.
"""
name = "CódigoFacilito" #Variable de tipo string (str)
print(name) #imprime CódigoFacilito
print(type(name)) #imprime el tipo de dato de la variable name

#Ejemplo con variable de tipo entero (int)
age = 20
print(age) #imprime 20
print(type(age)) #imprime el tipo de dato de la variable age

""""
Se recomienda usas <snake_case> para nombrar variables
Esto significa que las variables deben ser escritas en minúsculas y separadas por guiones bajos.
Ejemplo: variable_nombre
"""
first_name = "Código"
last_name = "Facilito"
print("Ejemplo usando <snake_case>: "+first_name + " " + last_name) #imprime Código Facilito