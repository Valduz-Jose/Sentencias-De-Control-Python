# Tienda en linea que calcula descuentos segun si es miembro y el monto de la compra

print("*****Bienvenido a la tienda en linea****")

MONTO_COMPRA_DESC = 1000
monto_compra = float(input("Ingrese el monto de su compra: "))
es_miembro = input("¿Es usted miembro? (si/no): ").lower()

descuento = 0

if monto_compra >= MONTO_COMPRA_DESC and es_miembro.strip() == "si":
  descuento = 0.1
elif es_miembro.strip() == "si":
  descuento = 0.05
elif monto_compra >= MONTO_COMPRA_DESC:
  descuento = 0.03
else:
  descuento = 0
  
if descuento !=0:
  monto_descuento = monto_compra * descuento
  monto_final = monto_compra - monto_descuento
  print(f"Usted tiene un descuento del {descuento*100}%, el monto a pagar es: {monto_final}")
else:
  print(f"No tiene descuento, el monto a pagar es: {monto_compra} lo invitamos a hacerse miembro de la tienda")