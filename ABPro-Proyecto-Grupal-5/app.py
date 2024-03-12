import random, time

# Lista para guardar usuarios
clientes = []

# Lista para guardar productos
productos = []

# Entrada de datos
def validate_input(prompt, validator, error_message):
    while True:
        user_input = input(prompt).strip()  # Elimina espacios en blanco al principio y al final
        if user_input and validator(user_input):
            return user_input
        else:
            print(error_message)

# Nombre de usuario
def validate_username(username):
    return len(username) > 0 and not any(char.isdigit() for char in username)

# Edad de usuario
def validate_age(age_str):
    try:
        age = int(age_str)
        return age >= 0
    except ValueError:
        return False

# Agregar Cliente
def agregar_cliente():
    print("Ingresa la información del cliente a continuación:")
    username = validate_input("Ingresa un nombre de usuario: ", validate_username, "Nombre de usuario inválido. El nombre de usuario no puede estar vacío o contener números. Ingresa un nombre de usuario válido")
    age = validate_input("Ingresa la edad: ", validate_age, "Edad inválida. Por favor ingresa una edad válida.")
    # Agregar características
    cliente_data = {
        'nombre_usuario': username,
        'edad': int(age),
        'identificador_unico': len(clientes) + 1,  # ID único
    }
    clientes.append(cliente_data)

# Agregar Producto
def agregar_producto():
    print("Ingresa la información del producto a continuación:")
    nombre = input("Ingresa el nombre del producto: ")
    precio = input("Ingresa el precio del producto: ")
    color = input("Ingresa el color del producto: ")
    # Agregar características
    producto_data = {
        'nombre': nombre,
        'precio': precio,
        'identificador_unico': len(productos) + 1,  # ID único
        'color': color
    }
    productos.append(producto_data)

# Mostrar Clientes
def mostrar_clientes():
    print("\nInformación de clientes:")
    for cliente in clientes:
        print(f"Nombre de usuario: {cliente['nombre_usuario']}, Edad: {cliente['edad']}, ID: {cliente['identificador_unico']}")
        time.sleep(0.1)

# Mostrar Producto
def mostrar_productos():
    print("\nInformación de productos:")
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, ID: {producto['identificador_unico']}, Color: {producto['color']}")
        time.sleep(0.1)

# Eliminar cliente
def eliminar_cliente():
    if not clientes:
        print("No hay clientes para eliminar. Haz tu búsqueda nuevamente.")
        return

    print("\nClientes disponibles:")
    for cliente in clientes:
        print(f"ID: {cliente['identificador_unico']}, Nombre: {cliente['nombre_usuario']}")
        time.sleep(0.1)

    id_cliente = input("Ingresa el ID del cliente a eliminar: ")
    for cliente in clientes:
        if str(cliente['identificador_unico']) == id_cliente:
            clientes.remove(cliente)
            print("Cliente eliminado exitosamente.")
            return
    print("No se encontró ningún cliente con el ID indicdo.")

# Eliminar producto
def eliminar_producto():
    if not productos:
        print("No hay productos para eliminar.")
        return

    print("\nProductos disponibles:")
    for producto in productos:
        print(f"ID: {producto['identificador_unico']}, Nombre: {producto['nombre']}")
        time.sleep(0.1)

    id_producto = input("Ingresa el ID del producto a eliminar: ")
    for producto in productos:
        if str(producto['identificador_unico']) == id_producto:
            productos.remove(producto)
            print("Producto eliminado exitosamente.")
            return
    print("No se encontró ningún producto con el ID indicado.")

# Agregar 10 clientes
for i in range(1, 11):
    cliente_data = {
        'nombre_usuario': f"Cliente {i}",
        'edad': random.randint(18, 60),
        'identificador_unico': i
    }
    clientes.append(cliente_data)

# Agregar 5 productos
for i in range(1, 6):
    producto_data = {
        'nombre': f"Producto {i}",
        'precio': round(random.uniform(10, 100), 2),
        'identificador_unico': i,
        'color': f"Color {i}"
    }
    productos.append(producto_data)

# Menú
def menu():
    while True:
        print("\nMenú:")
        print("1. Agregar Cliente")
        print("2. Mostrar Clientes")
        print("3. Eliminar Cliente")
        print("4. Agregar Producto")
        print("5. Mostrar Productos")
        print("6. Eliminar Producto")
        print("7. Salir")

        choice = input("Selecciona una opción: ")
        if choice == '1':
            agregar_cliente()
        elif choice == '2':
            mostrar_clientes()
        elif choice == '3':
            eliminar_cliente()
        elif choice == '4':
            agregar_producto()
        elif choice == '5':
            mostrar_productos()
        elif choice == '6':
            eliminar_producto()
        elif choice == '7':
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

# Función del programa
def main():
    menu()

if __name__ == "__main__":
    main()
