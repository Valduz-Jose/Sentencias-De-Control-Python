# validar usuario y password
print("Bienvenido al Sistema de Autenticacion\n")
USER = "admin"
PASSWORD= '123'

user = input("Ingrese su usuario: ")
pasword = input("Ingresa tu password:")

if user == USER and pasword == PASSWORD:
  print("¡Bienvenido al sistema!")
elif user == USER:
  print("Contraseña incorrecta")
elif pasword == PASSWORD:
  print("Usuario incorrecto")
else:
  print("Ingrese datos validos")