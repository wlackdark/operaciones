
print ("Hola, este es un programa que verifica si no es cierto que ambos números son mayores que 10.")
nombre=input("Por favor ingrese su nombre ")
num1=int(input(f"{nombre} Ingrese el primer numero "))
num2=int(input(f"{nombre} Ingrese el segundo numero "))
mayorque= not num1>10 and num2>10
print(f"{nombre}, el {num1} y el {num2} no son mayores que 10 {mayorque}")
