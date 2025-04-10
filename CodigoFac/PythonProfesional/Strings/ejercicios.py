"""
Define un string llamado name. Imprime en consola si name es, o no, un palindromo (True o False)

Reto: Intenta resolver el reto usando menos de 3 líneas de código.
"""
name = "ana"
print(name == name[::-1]) #imprime True

"""
Crea una variable de tipo string llamada name . 
Imprime en consola el valor de dicha variable con todas sus letras en minúsculas, exceptuando la primera, 
que debe encontrarse en mayúsculas. Por ejemplo:

name = 'CodigoFacilito'
>>> Codigofacilito

name = 'Python Profesional'
>>> Python profesional
"""
name = 'CodigoFacilito'
name = 'Python Profesional'
print(name.capitalize()) #imprime Python profesional

"""
Crea una variable de tipo string llamada name e imprime en consola True o False
 si el primer o último carácter son vocales.
"""
name = "codigo"
print(name[0] in "aeiou" or name[-1] in "aeiou") #imprime True

"""
Genera 3 nuevas variables: name, age, course y utilizando un f-string, imprime en consola, en el mismo orden,
 el valor de cada una de las variables. Los valores deben separarse por un guión (-). Por ejemplo

name, age, course = ‘Cody’, 12, ‘Python’
>>> Cody-12-Python
"""
name = "Cody"
age = 12
course = "Python"
print(f"{name}-{age}-{course}") #imprime Cody-12-Python

""""
Dada la siguiente lista de números enteros lista = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] genera un string con los primeros 5 elementos de la lista.
 Cada valor debe encontrarse separado por un espacio. Imprime en consola dicho string.
"""
lista = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
print(" ".join(lista[:5])) #imprime 1 2 3 4 5

