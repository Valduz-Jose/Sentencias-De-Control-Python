# Solicitar al usuario si desea continuar en el sistema bancario 
print("Bienvenido al sistema bancario")

salir_sistema_txt = input("¿Desea salir del sistema bancario? (s/n): ")

salir_sistema = salir_sistema_txt.strip().lower() == "si"
if not salir_sistema:
  print("Continuamos en el sistema bancario!")
else:
  print("¡Gracias por usar el sistema bancario! ¡Hasta luego!")