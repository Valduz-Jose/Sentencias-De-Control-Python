# Sistema de Envios
# pedir peso y destino (nacional o internacional)
NACIONAL = 10
INTERNACIONAL = 20

print("Sistema de Envios\n")
peso = float(input("Ingrese el peso del paquete en kg: "))
destino = input("Ingrese el destino (nacional/internacional): ").strip().lower()
costo_envio = None

if destino == "nacional":
    costo_envio = peso * NACIONAL
elif destino == "internacional":
    costo_envio = peso * INTERNACIONAL
else:
    print("Destino no valido")
   
if costo_envio != None:
  print(f"El costo de envío para un paquete de {peso} kg con destino {destino} es: ${costo_envio:.2f}")