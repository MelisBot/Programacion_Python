"""
Dado los tres lados de un triángulo pueda determinar su área.
"""
import math 
# Definición de funciones para que nos retorne el área del triángulo
def area(lado1, lado2, lado3):
    s = (lado1 + lado2 + lado3) / 2  
    return math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3))

# Definición de la función principal
def main():
    # Usamos un try-except para validar la entrada del usuario
    try:
        lado1 = float(input("Ingrese el primer lado del triángulo: "))
        lado2 = float(input("Ingrese el segundo lado del triángulo: "))
        lado3 = float(input("Ingrese el tercer lado del triángulo: "))

        # Validar que los lados sean positivos
        if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
            print("Error: Los lados deben ser números positivos.")
            return
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        return

    # Validar que los lados formen un triángulo
    if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
        print("Error: Los lados no forman un triángulo.")
        return

    # Cálculo del área
    area_triangulo = area(lado1, lado2, lado3)
    print(f"El área del triángulo es: {area_triangulo:.4f}")  # Regresa 4 decimales después del punto

if __name__ == "__main__": # Si se ejecuta el archivo directamente
    main() # Llama a la función principal