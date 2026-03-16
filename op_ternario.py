# forma compacta de una condicion if-else, también conocida como operador ternario
# sintaxis: resultado = valor_si_verdadero if condicion else valor_si_falso 
# Se recomienda usar el operador ternario para condiciones simples y claras, evitando su uso en casos complejos para mantener la legibilidad del código.

print("Uso del Operador Ternario\n")
edad = int(input("¿Cuál es tu edad? "))
es_adulto = "si" if edad >= 18 else "no"
print(f"¿Eres adulto? {es_adulto}")