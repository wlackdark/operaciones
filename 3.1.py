print ("Hola, este es un programa que verifica si dos numeros son mayores que 10")
nombre=input("Por favor ingrese su nombre ")
num1=int(input(f"{nombre} Ingrese el primer numero "))
num2=int(input(f"{nombre} Ingrese el segundo numero "))
mayores10= num1>10 and num2>10
print(f"{nombre} Los numeros {num1} y {num2} son mayores que 10 {mayores10}")
