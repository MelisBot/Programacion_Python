# nombre: str = input("Ingresa el nombre: ")
# apellido: str = input("Ingresa el apellido: ")
nombre: str = "aqsdasd"
edad: int = int(input("Ingresa tu edad: "))
sueldo: float = 5000.50
es_valido: bool = False
vacio = None
# Casting o Casteo o Conversión
# "20", "0", "-1" => 20, 0, -1 | "asdasdasd" => ???
print(type(edad))
#con el metodo dir es necesario utilizar para ver que metodos se pueden utilizar con una variable
#Casting o casteo de variables
#Convertir una variable de un tipo de dato a otro
#Ejemplo: int a float, str a int, etc.
#Para hacer un casting se utiliza el nombre del tipo de dato al que se quiere convertir la variable
#Ejemplo:
num1 = 5
num2 = float(num1)
print(num2) #imprime 5.0
#Al hacer este tipo de conbersiones se debe tener en cuenta que se puede perder información