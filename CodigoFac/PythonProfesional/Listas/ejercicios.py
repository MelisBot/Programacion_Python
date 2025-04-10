"""
Define una lista de N números enteros. Imprime en consola la suma del primer y último elemento de la lista. 
La lista dee tener por nombre numbers.

Reto: Intenta resolver el reto usando menos de 3 líneas de código.
"""
numbers = [1, 2, 3, 4, 5]
print(numbers[0] + numbers[-1]) #imprime 6

""""
Define una lista de N números enteros e imprime en consola la suma de todos los elementos.
La lista debe tener por nombre numbers.
"""
numbers = [1, 2, 3, 4, 5]
print(sum(numbers)) #imprime 15

"""
Define una lista de longitud 10 de Strings. La lista debe tener por nombre strings_list 
Genera una sub lista con los 3 primeros y últimos elementos. Imprime en consola la nueva sub lista.
"""
strings_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(strings_list[:3] + strings_list[-3:]) #imprime ['a', 'b', 'c', 'h', 'i', 'j']


""""
Define una lista de 10 Strings. Imprime en consola True o False si ‘CodigoFacilito’
Se encuentra como elemento de la lista. La lista debe tener por nombre strings_list.
"""
strings_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print('CodigoFacilito' in strings_list) #imprime False

"""
Crea una matriz de 3x3 e imprime en consola True si: 
El primer elemento de cada fila es un número par. 
El nombre de la matriz debe ser matrix.
"""
matrix = [
    [2, 3, 4],
    [6, 7, 8],
    [10, 11, 12]
]
print(all([i[0] % 2 == 0 for i in matrix])) #imprime True


