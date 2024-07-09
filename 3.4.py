print ("Hola, este es un programa que verifica si el primer número es mayor que 5 y el segundo número es menor que 10 o el tercer número es igual a 20")
nombre=input("Por favor ingrese su nombre ")
num1=int(input(f"{nombre} Ingrese el primer numero "))
num2=int(input(f"{nombre} Ingrese el segundo numero "))
num3=int(input(f"{nombre} Ingrese el tercer numero "))
mayorque= num1>5 
menorque= num2<10
igualque= num3==20
print(f"{nombre}, el {num1} es mayor que 5 {mayorque} y el {num2} es menor que 10 {menorque} o el tercer numero es igual a 20 {igualque}")
