# convertidor de notas de numeros a letras
print("Convertidor de notas de números a letras\n")
nota = float(input("Ingrese la nota numérica (0-10): "))
letra = None

if 9 <= nota <= 10:
    letra = "A"
elif 8 <= nota < 9:
    letra = "B"
elif 7 <= nota < 8:
    letra = "C"
elif 6 <= nota < 7:
    letra = "D"
elif 0 <= nota < 6:
    letra = "F"
else:
    letra = "Nota no válida"
    
print(f"La nota numérica {nota} corresponde a la letra: {letra}")