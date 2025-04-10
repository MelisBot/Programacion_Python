# Estrcutura de control IF, ELSE, ELIF, operador ternario

"""La estructura de control IF"""
#La estructura de control IF se utiliza para tomar decisiones en un programa.
#Si la condición es verdadera, se ejecuta el bloque de código correspondiente. 
#Sintaxis:
# if condición:
#     bloque de código
# Ejemplo:
if 5 > 3:
    print("5 es mayor que 3")

"""La estructura de control ELSE"""
#La estructura de control ELSE se utiliza para ejecutar un bloque de código si la condición es falsa.
#Sintaxis:
# if condición:
#     bloque de código
# else:
#     bloque de código

#Ejemplo:
if 5 < 3:
    print("5 es menor que 3")
else:
    print("5 es mayor o igual que 3")

"""La estructura de control ELIF"""
#La estructura de control ELIF se utiliza para ejecutar un bloque de código si la condición es verdadera.
#Sintaxis:
# if condición:
#     bloque de código
# elif condición:
#     bloque de código
# else:
#     bloque de código
# Ejemplo:
if 5 > 3:
    print("5 es mayor que 3")
elif 5 < 3:
    print("5 es menor que 3")
else:
    print("5 es igual que 3")

"""Operador ternario"""
#El operador ternario se utiliza para tomar decisiones de manera más concisa.
#Sintaxis:
# variable = valor1 if condición else valor2
# Ejemplo:

x = 5
y = 3
mayor = x if x > y else y 
print(mayor)  # Salida: 5
