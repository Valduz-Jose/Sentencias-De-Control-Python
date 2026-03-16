# solicitar nombre y pasos caminados
# define constantes meta pasos y calorias por paso
# calcular las calorias quemadas

print("Aplicacion de Salud y Fitnees")
META_PASOS_DIARIO = 10000
CALORIAS_POR_PASO = 0.04

nombre = input("¿Cuál es tu nombre? ")
pasos_caminados = int(input("¿Cuántos pasos has caminado hoy? "))

# verificamos si llego a la meta
meta_alcanzada = pasos_caminados >= META_PASOS_DIARIO
meta_alcanzada_str = "SI" if meta_alcanzada else "NO"
calorias_quemadas = pasos_caminados * CALORIAS_POR_PASO
print(f"Hola {nombre}, has caminado {pasos_caminados} pasos hoy.")
print(f"¿Has alcanzado tu meta diaria de {META_PASOS_DIARIO} pasos? {meta_alcanzada_str}")
print(f"Has quemado aproximadamente {calorias_quemadas:.2f} calorías")
