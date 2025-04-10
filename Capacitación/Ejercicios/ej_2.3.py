""" 
Ejercicio 2.3: Calcular las raices reales de la expresion cuadratica ax^2 + bx + c = 0
a,b, c donde a != 0 
x1 variable de tipo real y almacenar el resultado de la primera raiz real de la ecuacion cuadratica
x2 variable de tipo real y almacenar el resultado de la segunda raiz real de la ecuacion cuadratica
Se ocupa estructura selectiva simpre si entonces
"""
import math  

# Definición de la función para calcular las raíces
def calcular_raices(a, b, c):
    # Calcula el discriminante
    dis = b**2 - 4*a*c
    # Calcula las raíces reales
    if dis >= 0:
        x1 = (-b + math.sqrt(dis)) / (2 * a) # Calcula la primera raíz
        x2 = (-b - math.sqrt(dis)) / (2 * a) # Calcula la segunda raíz
        # Verifica si las raíces son iguales
        if x1 == x2:
            print("Las raíces son iguales.")
        else:
            print("Las raíces son diferentes.")
        return x1, x2
    else:
        return None, None # Si el discriminante es negativo, no hay raíces reales
    
# Definición de la función principal    
def main():
    # Usamos un try-except para validar la entrada del usuario
    try:
        a = float(input("Introduce el valor de a: "))  # ingresa el valor de a
        if a == 0:
            raise ValueError("El valor de 'a' no puede ser cero.")  
        b = float(input("Introduce el valor de b: "))  
        c = float(input("Introduce el valor de c: "))  
        
    except ValueError:
        print(f"Error : Debe ingresar un número válido.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except TypeError:
        print("Error: Debe ingresar un número válido.")
    except Exception as ex:
        print(f"Error, excepcion no reconocida: {ex}")
        return  # salir del programa si hay un erro
    
    # Llama a la función para calcular las raíces
    x1, x2 = calcular_raices(a, b, c)

    # Imprime los resultados
    if x1 is not None and x2 is not None:
        print(f"Las raíces reales de la ecuación cuadrática son: {x1:.2f} y {x2:.2f}")
    else:
        print("La ecuación cuadrática no tiene raíces reales.")

if __name__ == "__main__":  # Si se ejecuta el archivo directamente
    main()  # Llama a la función principal