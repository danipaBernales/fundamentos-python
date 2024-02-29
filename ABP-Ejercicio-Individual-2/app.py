#Sitio / Punto de venta
usuarios = ["Tomas", "Daniela", "Johanna", "Alan", "Hugo", "Pepe", "Luis"]

usuario_ingresado = input("Ingresa tu usuario:")
while usuario_ingresado not in usuarios:
    usuario_ingresado = input("Error, vuelve a ingresar tu usuario: ")

print("Bienvenide " + usuario_ingresado)
print("En el sistema hay registrados " + str(len(usuarios)) + " usuarios")

print("Lista de usuarios:")
for usuario in usuarios:
    print("- " + usuario)