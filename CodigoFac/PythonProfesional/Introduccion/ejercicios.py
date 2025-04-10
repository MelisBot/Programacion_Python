"""
Define las variables first_name & last_name e imprime dichos valores en consola. 
Las variables debe de ser de tipo String.
"""
first_name = "Código"
last_name = "Facilito"
print(first_name) #imprime <class 'str'>, indica que first_name es d
print(f"El nombre es: {first_name}") #imprime El nombre es: Código

"Formato de forma tipada"
first_name: str = "Código"
last_name: str = "Facilito"
print(first_name) #imprime <class 'str'>, indica que first_name es de tipo str

""""
Con las variables anteriores (first_name y last_name) genera una tercera variable llamada full_name, que no será más que la suma de first_name y last_name. De esta forma imprime el nombre completo en consola.
Nota: Se debe añadir un espacio para diferenciar el nombre del apellido.
"""
full_name = first_name + " " + last_name
print(full_name) #imprime Código Facilito

""""
Usando la variable full_name, imprime en consola True o False el nombre completo es igual ‘Codigo Facilito’
"""
first_name = "Uriel"
last_name = "Hernández"
full_name = first_name + " " + last_name
print(full_name == 'Codigo Facilito') #imprime True



