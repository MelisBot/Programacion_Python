#En python las constantes no existen, pero se pueden simular con variables en mayúsculas
"""
Constantes en Python
Es recomendable usar la version snake_case para nombrar constantes en Python 
(todas las letras en mayúsculas y separadas por guiones bajos).
debemos hacer las variables como MAYÚSCULAS para indicar que son constantes.
"""
#Ejemplo:
PI = 3.1416
print(PI) #imprime 3.1416
#Se recomienda usar mayúsculas para nombrar constantes en Python
 
""""
Operadores relacionales en python
Los operadores relacionales son utilizados para comparar dos valores.
Los operadores relacionales son:
== Igual a
!= Diferente
> Mayor que
< Menor que
>= Mayor o igual que
<= Menor o igual que
(Bool(True/False))
"""
number_one = 10
number_two = 5
result = number_one == number_two
print(result) #imprime False
print(type(result)) #imprime <class 'bool'>
#Ejemplo:
num1 = 10
num2 = 5
print(num1 == num2) #imprime False
print(num1 != num2) #imprime True
print(num1 > num2) #imprime True
print(num1 < num2) #imprime False   
print(num1 >= num2) #imprime True
print(num1 <= num2) #imprime False
