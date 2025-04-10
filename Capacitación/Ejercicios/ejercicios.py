"""
Ejercicio 1.5: Dado como datos el radio y la altura de un cilindro, calcule e 
imprima el área y su volumen
"""
from math import pi

def area_cilindro(radio: float, altura: float) -> float:
    """
    Función enfocada en obtener el área de un cilindro en base al radio y altura
    :param radio: Radio del cilindro en formato float
    :param altura: Altura del ciclindro en formato float
    :return Float area del cilindro
    """
    return 2 * pi * radio * altura

def volumen_cilindro(radio: float, altura: float) -> float:
    """
    Función enfocada en obtener el volumen de un cilindro en base al radio y altura
    :param radio: Radio del cilindro en formato float
    :param altura: Altura del ciclindro en formato float
    :return Float volumen del cilindro
    """
    return pi * radio**2 * altura

def ejercicio_1():
    try:
        radio = float(input("Introduce el radio del cilindro: "))
        altura = float(input("Introduce la altura del cilindro: "))

        if radio <= 0 or altura <= 0:
            print("Error: El radio y la altura deben ser números positivos")
            raise ValueError

        area = area_cilindro(altura=altura, radio=radio)
        volumen = volumen_cilindro(radio=radio, altura=altura)
        print(f"El área del cilindro es: {area:.2f}")
        print(f"El volumen del cilindro es: {volumen:.2f}")
    except ValueError:
        print("Error: Debe ingresar un número válido.")
    except Exception as ex:
        print(f"Error, excepcion no reconocida: {ex}")


"""
Ejercicio 1.7: Dado los tres lados de un triángulo pueda determinar su área.
"""
def area(lado1: float, lado2:float, lado3:float) -> float:
    """
    función enfocada en obtener el área de un triángulo en base a sus lados
    :param lado1: Lado 1 del triángulo en formato float
    :param lado2: Lado 2 del triángulo en formato float
    :param lado3: Lado 3 del triángulo en formato float
    :return: Float área del triángulo
    """
    s = (lado1 + lado2 + lado3) / 2
    return (s*(s-lado1)*(s-lado2)*(s-lado3))**0.5

def ejercicio_2():
    try:
        lado1 = float(input("Ingrese el primer lado del triángulo: "))
        lado2 = float(input("Ingrese el segundo lado del triángulo: "))
        lado3 = float(input("Ingrese el tercer lado del triángulo: "))

        if lado1 <= 0 or lado2 <= 0 or lado3 <=0:
            print("Error: Los lados deben ser números positivos")
            raise ValueError
        
        if lado1 +lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
            print("Error: Los lados no forman un triángulo.")
            raise ValueError
        
        area_triangulo = area(lado1, lado2, lado3)
        print(f"El área del triángulo es: {area_triangulo:.4f}")

    except ValueError:
        print("Error: Debe ingresar un número válido.")
        return
    except Exception as ex:
        print(f"Error, excepcion no reconocida: {ex}")


""" 
Ejercicio 2.3: Calcular las raices reales de la expresion cuadratica ax^2 + bx + c = 0
a,b, c donde a != 0 
x1 variable de tipo real y almacenar el resultado de la primera raiz real de la ecuacion cuadratica
x2 variable de tipo real y almacenar el resultado de la segunda raiz real de la ecuacion cuadratica
Se ocupa estructura selectiva simpre si entonces
"""
def calcular_raices(a : float, b : float, c : float ) -> tuple:
    """
    Función enfocada en obtener las raíces de una ecuación cuadrática
    :param a: Coeficiente a de la ecuación cuadrática
    :param b: Coeficiente b de la ecuación cuadrática
    :param c: Coeficiente c de la ecuación cuadrática
    :return: Tuple con las raíces reales de la ecuación cuadrática
    """
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        x1 = (-b + discriminante**0.5) / (2*a)
        x2 = (-b - discriminante**0.5) / (2*a)
        print("Las raíces son diferentes.")
        return x1, x2  
     
    elif discriminante == 0:
        x1 = -b / (2*a)
        x2 = x1
        print("Las raíces son iguales.")
        return x1, x2
    else:
        print("La ecuación cuadrática no tiene raíces reales.")
        return None, None
    
def ejercicio_3():
    try:
        a = float(input("Ingrese el coeficiente a: "))
        b = float(input("Ingrese el coeficiente b: "))
        c = float(input("Ingrese el coeficiente c: "))

        if a and b and c == 0:
            raise ValueError("El coeficiente 'a' no puede ser cero.")
        
        x1, x2 = calcular_raices(a, b, c)
        
        if x1 and x2:  # Verificación simplificada
            print(f"La primera raíz X1 es: {x1:.4f}")
            print(f"La segunda raíz X2 es: {x2:.4f}")
            print(f"Las raíces reales de la ecuación cuadrática son: {x1:.2f} y {x2:.2f}")
        else:
            print("La ecuación cuadrática no tiene raíces reales.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as ex:
        print(f"Error, excepción no reconocida: {ex}")


"""
Ejercicio 2.6: Dado un número entero A, determine si es par, impar o nulo.
"""
def determinar_paridad(a: int) -> str:
    if a == 0:
        print("El número es nulo")
    elif a % 2 == 0:
        print("El número es par") 
    else:
        return"El número es impar"

def ejercicio_4():
    try:
        a = int(input("Ingrese un número entero: "))
        print(f"El número ingresado es: {a}")
        determinar_paridad(a)
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
    except Exception as ex:
        print(f"Error, excepcion no reconocida: {ex}") 


"""
Ejercicio 2.7: Dado como datos de entrada tres números enterros
A,B y C determine si los mismos estan en orden creciente.
"""
def orden_creciente(a : int, b: int, c: int) -> str:
    
    if a < b < c:
        print ("Los números están en orden creciente")
    elif a > b > c:
        print ("Los números están en orden decreciente")
    elif a == b == c:
        print ("Los números son iguales")
    else:
        return ("Los números son iguales o decrecientes")
    
def ejercicio_5():   
    try :
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        c = int(input("Ingrese el tercer número: "))

        print(f"Los números son: {a}, {b}, {c}")
        orden_creciente(a, b, c)
        
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
    except Exception as ex:
        print(f"Error, excepcion no reconocida: {ex}")

if __name__ == '__main__':
    ejercicio_1()
    ejercicio_2()
    ejercicio_3()
    ejercicio_4()
    ejercicio_5()

