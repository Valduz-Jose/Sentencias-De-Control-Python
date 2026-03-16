# Reserva Hotel
# pedir nombre,dias de estadia,cuarto con vista al mar?

CUARTO_SIN_VISTA_MAR = 150.50
CUARTO_CON_VISTA_MAR = 190.50

print("Bienvenido al sistema de reserva de hotel")

nombre = input("¿Cuál es tu nombre? ")

dias_estadia = int(input("¿Cuántos días de estadía deseas? "))

cuarto_vista_mar_txt = input("¿Deseas un cuarto con vista al mar? (s/n): ").strip().lower() == "si"

cuarto_vista_mar = "SI" if cuarto_vista_mar_txt else "NO"

if cuarto_vista_mar:
  costo_total = dias_estadia * CUARTO_CON_VISTA_MAR
else:
  costo_total = dias_estadia * CUARTO_SIN_VISTA_MAR
print(f"Hola {nombre}, has reservado un cuarto con vista al mar: {cuarto_vista_mar} por {dias_estadia} días son {costo_total} dolares.")