# Bodega virtual de productos
def bodega_virtual():
    return {
        1: {"nombre": "ZAPATILLAS", "cantidad": 20},
        2: {"nombre": "POLERAS", "cantidad": 10},
        3: {"nombre": "ZAPATOS", "cantidad": 15},
        4: {"nombre": "POLERÓN", "cantidad": 3},
        5: {"nombre": "CHAQUETA", "cantidad": 5},
        6: {"nombre": "GUANTES", "cantidad": 4}
    }

# Actualizar productos en bodega
def almacenar_stock(bodega, id_producto, cantidad):
    if id_producto in bodega:
        bodega[id_producto]["cantidad"] += cantidad
    else:
        print("Producto no existe")

# Actualizar stock de un producto en bodega
def actualizar_stock(bodega, id_producto, cantidad):
    if id_producto in bodega:
        bodega[id_producto]["cantidad"] = cantidad
    else:
        print("Producto no existe")
        
# Productos y cantidades disponibles en bodega      
def unidades_disponibles(bodega):
    return {producto["nombre"]: producto["cantidad"] for producto in bodega.values()}
        
# Stock disponeble de un producto
def stock_disponible_producto(bodega, id_producto):
        if id_producto in bodega:
            return bodega[id_producto]["cantidad"]
        else: 
            return 0

# Productos y cantidades disponibles mayor a especificada a petición usuario 
def producto_unidad_usuario(bodega, cantidad):
    return [producto["nombre"] for producto in bodega.values() if producto["cantidad"] > cantidad]

# Ingresar usuarios
def ingresar_usuario(clientes):
    nombre = input("Ingresa el nombre del cliente: ")
    clientes.append(nombre)
    return len(clientes)

# Clientes registrados
def clientes_registrados(clientes):
    return len(clientes)

# Solicitud de compra
def solicitar_compra(id_cliente, id_producto, cantidad=1, bodega=None, clientes=None):
    if not bodega:
        return "Bodega no especificada"
    
    if id_producto not in bodega:
        return "Producto no existe"
    
    if id_cliente not in clientes:
        return "Usuario no registrado"
    
    stock_disponible = bodega[id_producto]["cantidad"]
    
    if stock_disponible >= cantidad:
        bodega[id_producto]["cantidad"] -= cantidad
        return "Compra aprobada y en camino"
    else:
        return "No hay suficiente stock, compra cancelada"

# Menu opciones a usuario      
def menu():
    print("1. Ver unidades totales disponibles")
    print("2. Ver unidades disponibles de un producto en particular")
    print("3. Ver productos con más de un número de unidades en stock")
    print("4. Ingresar usuario")
    print("5. Mostrar cantidad de usuarios registrados en la tienda")
    print("6. Solicitar compra")
    print("7. Salir")
    opcion = int(input("Selecciona una opción: "))
    return opcion

# Crea bodega
bodega = bodega_virtual()
# Clientes registrados
clientes = {}

# Obtener opciones del menú seleccionadas por usuario
while True:
    opcion = menu()
    
    if opcion == 1:
        print("Unidades disponibles para cada producto:", unidades_disponibles(bodega))
    elif opcion == 2:
        id_producto = input("Ingresa el ID del producto: ")
        if id_producto in bodega:
            print("Unidades disponibles:", stock_disponible_producto(bodega, id_producto))
        else:
            print("Producto no existe")
    elif opcion == 3:
        cantidad = int(input("Ingresa el número de unidades solicitadas: "))
        productos_sobre_cantidad = producto_unidad_usuario(bodega, cantidad)
        if productos_sobre_cantidad:
            print("Productos con más de", cantidad, "unidades:", productos_sobre_cantidad)
        else:
            print("No hay productos con más de", cantidad, "unidades disponibles")
    elif opcion == 4:
        nuevo_cliente_id = ingresar_usuario(clientes)
        print("Usuario registrado con ID:", nuevo_cliente_id)
    elif opcion == 5:
        print("Total usuarios registrados:", len(clientes))
    elif opcion == 6:
        id_cliente = int(input("Ingresa el ID del usuario: "))
        id_producto = input("Ingresa el ID del producto: ")
        cantidad = int(input("Ingresa la cantidad a comprar: "))
        if id_cliente in clientes:
            print(solicitar_compra(id_cliente, id_producto, cantidad, bodega))
        else:
            print("Cliente no existe")
    elif opcion == 7:
        break
    else:
        print("Opción inválida. Elige una opción disponible en el menú.")