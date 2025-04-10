"""
Genera un diccionario con las siguientes llaves: name, age, course.
Imprime el diccionario en consola. El nombre del diccionario debe ser my_dictionary.
"""
my_dictionary = {
    "name": "Juan",
    "age": 25,
    "course": "Python"
}
print(my_dictionary)

"""
Utilizando el diccionario del paso anterior (my_dictionary): Genera un nuevo string con las llaves del diccionario.
Las llaves debe encontrarse separadas por un guión (-). Imprime dicho string en consola.
"""
my_dictionary = {'name':  'Cody', 'age': 12, 'course': 'python'}
keys = "-".join(my_dictionary.keys())
print(keys)

""""
Utilizando el diccionario del paso anterior (my_dictionary): Reemplaza el valor de course por una lista que contenga,
por lo menos, 3 cursos. Imprime el diccionario en consola.
"""
my_dictionary = {'name':  'Cody', 'age': 12, 'course': 'python'}
my_dictionary["course"] = ["Python", "Java", "JavaScript"]
print(my_dictionary)

""""
Utilizando el diccionario del paso anterior (my_dictionary):
 Reemplaza el valor de edad por 20 y añade una nueva llave llamada: ‘active’ que almacenara un valor bool (True o False). 
 Reemplaza la llave course por courses(Plural) Imprime el diccionario en consola.
Nota: Estos pasos debe hacerse utilizando los métodos del objeto diccionario.
"""
my_dictionary = {'name':  'Cody', 'age': 12, 'course': 'python'}
my_dictionary.update({"age": 20})
my_dictionary["active"] = True
my_dictionary["courses"] = my_dictionary.pop("course")
print(my_dictionary)

""""
"""