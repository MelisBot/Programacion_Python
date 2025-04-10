#Ejercicios usando el libro de Metodologias de la programacion
#Clase 2 - Estructuras de datos 11-03-2025
#Ejercicio 1

"""
Construya un programa en python tal que dado el costo de una articulo vendido
y la cantidad de dinero entregada por el cliente, calcule e imprima el cambio
que se debe entregar al mismo.
"""
#Costo del producto
costo = float(input("Ingrese precio del producto:"))
#Pago del cliente
pago = float(input("Ingrese pago realizado:"))

if costo < 0 or pago < 0: #si el costo o el pago son menores a 0 (negativos)
    print("El costo y el pago deben ser positivos")
elif costo == 0 or pago == 0: #si el costo o el pago son iguales a 0
    print(f"El costo del producto es {costo} y el pago es {pago} por lo tanto no hay cambio")
elif pago < costo:
    print(" El pago es insuficiente")
elif pago == costo:
    print("El pago es igual al costo del producto no hay cambio")
elif pago > costo:
    cambio = pago - costo
    print(f"Costo del producto:$ {costo}\n  Pago:$ {pago}\n  Cambio:$ {cambio}\n")
else:
    print("Error en el sistema")

#Ejercicio 2
"""
Dadas las base y la altura de un triangulo, calcule e imprima su superficie."
"""

#Base del triangulo
base = float(input("Ingresa la base del triangulo: "))
#Altura del triangulo
altura = float(input("Ingresa la altura del triangulo: "))

if base < 0 or altura < 0:
    print("La base y la altura deben ser positivas")
elif base == 0 or altura == 0:
    print("La base y la altura deben ser positivas")
else:
    superficie = (base * altura) / 2
    print(f"La superficie del triangulo con base {base} y altura {altura} es: {superficie}")   


#Ejercicio 3
nombre: str = input("Ingresa el nombre del dinosaurio: ")
peso: int = int(input("Ingresa el peso en libras: "))
longitud: float = float(input("Ingresa la longitud en pies: "))

if not nombre: #Si no se recive el nombre
    print("El nombre no puede estar vacio, ingresa un nombre ")
elif peso < 0 or longitud < 0: #si el peso o la longitud son negativos
    print("El peso y la longitud deben ser positivos")
else:
    peso = peso * 1000
    longitud = longitud * 0.3048
    print(f"El dinosaurio {nombre} pesa: {peso} kg y su largo es: {longitud:.2f} metros")
