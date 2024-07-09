#Realice un programa que consecutivamente pida ingresar dos valores para realizar operaciones matemáticas y muestre el resultado en consola.
print ("Hola, este es un programa que calcula operaciones básicas matematicas y muestra el resultado")
nombre=input("Por favor ingrese su nombre ")
num1=int(input(f"{nombre} Ingrese el primer numero "))
num2=int(input(f"{nombre} Ingrese el segundo numero "))
#suma
suma=num1+num2
print(f"{nombre} La suma de {num1} + {num2} es: {suma}")
#resta
resta=num1-num2
print(f"{nombre} La resta de {num1} - {num2} es: {resta}")
#multiplicacion
multiplicacion=num1*num2
print(f"{nombre} La multiplicacion de {num1} * {num2} es: {multiplicacion}")
#division
division=num1/num2
print(f"{nombre} La division de {num1} / {num2} es: {division}")
#division_entera
division_entera=num1//num2
print(f"{nombre} La division entera de {num1} // {num2} es: {division_entera}")
#modulo
modulo=num1%num2
print(f"{nombre} El modulo de {num1} / {num2} es: {modulo}")
#potencia
potencia=num1**num2
print(f"{nombre} La potencia de {num1} ^ {num2} es: {potencia}")

