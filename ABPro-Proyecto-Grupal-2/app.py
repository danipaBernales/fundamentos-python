#TeLoVendo / Registro usuarios con mensaje motivador
usuarios = ["Tomas", "Daniela", "Johanna", "Alan", "Hugo", "Pepin"]

usuario_ingresado = input("Ingresa tu usuario: ")
while usuario_ingresado not in usuarios:
    usuario_ingresado = input("Error, vuelve a ingresar tu usuario: ")

print("Hola equipo! Vamos a trabajar juntos para lograr grandes cosas! " + usuario_ingresado + "!")
print("En el sistema hay " + str(len(usuarios)) + " usuarios registrados :O")

print("La lista de usuarios es:")
for usuario in usuarios:
    print("- " + usuario.upper())

posicion = usuarios.index(usuario_ingresado)
texto = "Recuerda que estás en la posición " + str(posicion) + " de la lista de usuarios :)"

print(texto)
print("El string contiene " + str(len(usuarios)) + " palabras... por ahora :S")

print("Esta es la tupla: ")
tupla = tuple(usuarios)
print(tupla)


"""

- ¿Qué es un dato booleano? ¿Qué utilidad puede tener para el desarrollo de un programa?
    Un booleano es un tipo de dato que puede ser VERDADERO o FALSO. Sirve para hacer comprobaciones.


- Investigar qué significa que python sea un lenguaje de tipado dinámico.
    Significa que no es necesario especificar un tipo de dato.


- Investigar y documentar sobre la creación de Módulos en Python.
    Los módulos son archivos que tienen definiciones y declaraciones de Python y pueden ser importados en otros programas de Python para reutilizar el código.

- Investigar y documentar sobre la creación de Paquetes en Python.
    Son las formas que existen en Python para organizar los módulos.

- Investigar e implementar el uso del archivo __init__.py
    El archivo __init__.py es un archivo que se ejecuta cuando se importa un módulo.

"""