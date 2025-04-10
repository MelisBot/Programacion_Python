"""
Ejercicio 2.6: Dado un número entero A, determine si es par, impar o nulo.
"""
def determinar_paridad(A):
    #usamos la condicional if elif else
    if A == 0:
        return "nulo"
    elif A % 2 == 0:
        return "par"
    else:
        return "impar"
print("Ejemplo de uso:")
print("Número 0: " +determinar_paridad(0))  # imprime: nulo
print("Número 4: " +determinar_paridad(4))  # imprime: par
print("Número 246: " +determinar_paridad(246))  # imprime: impar
print("Número -3: " + determinar_paridad(-3))  # imprime: impar
print("Número 827379: " +determinar_paridad(827379)) # imprime: impar

#En caso que pidamos valores en terminal
try:
    A = int(input("Ingrese un número entero: "))
    resultado = determinar_paridad(A) # Llama a la función para determinar la paridad
    print(f"El número {A} es {resultado}")
except ValueError:  # Captura el error si no se puede convertir a int
    print("Error: Debe ingresar un número entero válido.")
except Exception as e: # Captura cualquier otro error inesperado
    print(f"Error inesperado: {e}") # Captura cualquier otro error inesperado