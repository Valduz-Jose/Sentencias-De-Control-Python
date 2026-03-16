# cual es el mayor de dos numeros

print("Verificar el mayor")
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

mayor = numero1 if numero1 > numero2 else numero2

print(f"El mayor de los dos números es: {mayor}")