"""
Dado como datos el radio y la altura de un cilindro, calcule e 
imprima el área y su volumen
"""
import math # Importar la librería math para usar pi y funciones matemáticas

#Usamos un try-except para validar la entrada del usuario
try:
    # Definición de variables de tipo flotante 
    radio = float(input("Introduce el radio del cilindro: "))
    altura = float(input("Introduce la altura del cilindro: "))
    # Validar que el radio y la altura sean positivos
    if radio <= 0 or altura <= 0:
        print("Error: El radio y la altura deben ser números positivos")
        exit() #Terminamos el programa si no se cumple la condición
except ValueError: # Captura el error si no se puede convertir a float 
    print("Error: Debe ingresar un número válido.")
    exit()

# Definición de funciones para que nos retorne el área y volumen del cilindro
def area_cilindro(radio, altura): #resive como paramentros el radio y la altura
    return 2 * math.pi * radio * altura

def volumen_cilindro(radio, altura):
    return math.pi * radio**2 * altura #la elevacion al cuadrado se hace con **2

# Cálculo del área y volumen
area = area_cilindro(radio, altura) #llama a la función area_cilindro y le pasa los parámetros radio y altura
volumen = volumen_cilindro(radio, altura)
# Salida de resultados
print(f"El área del cilindro es: {area:.2f}") #regrese 2 decimales después del punto
print(f"El volumen del cilindro es: {volumen:.2f}")