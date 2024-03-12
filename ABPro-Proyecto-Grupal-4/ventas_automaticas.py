import time, random

# Stock inicial de productos y stock máximo que pueden enviar los proveedores
stock_productos = {"Producto 1": {"stock": 120, "max_proveedor": 50},
                "Producto 2": {"stock": 150, "max_proveedor": 50}}
compras_realizadas = 0

# Compra simulada de productos
def realizar_compra():
    global compras_realizadas
    producto = random.choice(list(stock_productos.keys()))
    cantidad = random.randint(1, 10)
    compras_realizadas += 1

    if stock_productos[producto]["stock"] >= cantidad:
        stock_productos[producto]["stock"] -= cantidad
        print(f"Compra {compras_realizadas}: Se compraron {cantidad} unidades del {producto}")
    else:
        print(f"Compra {compras_realizadas}: No hay suficiente stock disponible para comprar {cantidad} unidades del {producto}")

    if stock_productos[producto]["stock"] < 100:
        enviar_proveedor(producto)

    if compras_realizadas % 10 == 0:
        imprimir_stock()

# Envío de productos por parte de un proveedor
def enviar_proveedor(producto):
    global stock_productos
    cantidad_a_enviar = min(50, 150 - stock_productos[producto]["stock"], stock_productos[producto]["max_proveedor"])
    if cantidad_a_enviar > 0:
        stock_productos[producto]["stock"] += cantidad_a_enviar
        print(f"Proveedor envió {cantidad_a_enviar} unidades del {producto}")
    else:
        print("Los stock de los proveedores están agotados y no pueden enviar más unidades.")

# Stock disponible de productos
def imprimir_stock():
    print("Stock actual:")
    for producto, data in stock_productos.items():
        print(f"{producto}: {data['stock']} unidades")
    print()

# Compras automáticas
while True:
    realizar_compra()
    time.sleep(3)
