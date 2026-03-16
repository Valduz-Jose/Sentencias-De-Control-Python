# identificar la estacion del a*o segun el mes ingresado por el usuario

print("Identificar la estación del año")
mes = int(input("Ingrese el mes en numero (1-12): "))
estacion = None
if mes ==1 or mes == 2 or mes == 12:
    estacion = "Invierno"
elif mes == 3 or mes == 4 or mes == 5:
    estacion = "Primavera"
elif mes == 6 or mes == 7 or mes == 8:
    estacion = "Verano"
elif mes == 9 or mes == 10 or mes == 11:
    estacion = "Otoño"
else:
    print("Mes no valido, por favor ingrese un numero entre 1 y 12")
    
print(f"El mes {mes} corresponde a la estación: {estacion}")
