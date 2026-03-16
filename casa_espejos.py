print("Bienvenido a la casa de los espejos")

edad = int(input("¿Cuál es tu edad? "))
tiene_miedo_oscuridad = input("¿Tienes miedo a la oscuridad? (s/n): ").strip().lower() == "si"

if not tiene_miedo_oscuridad and edad >= 10:
    print("Puedes entrar a la casa de los espejos.")
else:
    print("Lo siento, no puedes entrar a la casa de los espejos.")