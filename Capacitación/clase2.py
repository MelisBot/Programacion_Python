#Con el tipo de aperura y cerradura podemos saber que tipo de dato
#Las listas permiten cualquier tipo de dato y almacenar multiples elementos
mi_lista: list=[]
#Para acceder a los datos es mediante indices iniciando desde 0
print(mi_lista[0])

#Las tuplas son inmutables no se pueden modificar
mi_tupla: tuple=()
#Para acceder a los datos es mediante indices iniciando desde 0
print(mi_tupla[0])

#Colecciones de elementos unicos, no podemos tener elementos duplicados
mi_conjunto: set={1,2,3,4,5}
#Para acceder a los datos es mediante indices iniciando desde 0
print(mi_conjunto[0])

#Patecidos a los JSON ya que usa clave y valor
#Las claves deben ser unicas y los valores pueden ser cualquier tipo de dato
#Para acceder a los datos es mediante claves
mi_diccionario: dict={
    "nombre": "Juan",
}
#Para acceder a los datos es mediante claves
print(mi_diccionario["nombre"])

#Los más utilizados son las listas y los diccionarios.
#En DJango se utiliza mucho las tuplas
