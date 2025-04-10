"""
Ejercicio 2.7: Dado como datos de entrada tres números enterros
A,B y C determine si los mismos estan en orden creciente.
"""
#Se espera que A sea menor que B y B menor a C
#Ejemplo: 1,2,3 -> orden creciente
def orden_creciente(a, b, c):
    if a < b:
        if b < c:
            return " Los números están en orden creciente."
        else:
            return "Los números no están en orden creciente"
    else:
        return "Los números no están en orden creciente"

#Recibir valores enteros por teclado
try:
    #Entradas de números enteros
    A = int(input("Ingrese el primer número entero: "))
    B = int(input("Ingrese el segundo número entero: "))
    C = int(input("Ingrese el tercer número entero: "))
except ValueError:  # Captura el error si no se puede convertir a int 
    print("Error: Solo se permiten números enteros")  
except Exception as e: # Captura cualquier otro error inesperado 
        print(f"Error inesperado: {e}") 
else:
     #Llamada a la función con los valores de entrada
    resultado = orden_creciente(A, B, C)
    print(f"El número {A}, {B} y {C} son: {resultado}")