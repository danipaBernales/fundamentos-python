# Stock inicial del producto
stock_inicial = int(input("Ingresa el stock del producto: "))
print(f"Se registraron {stock_inicial} unidades del producto")

# Cantidad de productos seleccionados
productos_seleccionados = int(input("Ingresa la cantidad de productos seleccionados: "))

# Disponibilidad de stock
if productos_seleccionados > stock_inicial:
    print("No hay suficiente stock disponible.")
    exit()
elif productos_seleccionados > 20:
    print("No se pueden solicitar más de 20 unidades en un mismo pedido.")
    exit()

# Entrega unidad extra compra mayorista
if productos_seleccionados > 12 and stock_inicial >= (productos_seleccionados + 1):
    productos_seleccionados += 1
    print("Se entregó una unidad extra del producto por compra mayorista.")

# Actualiza stock
stock_actualizado = stock_inicial - productos_seleccionados

# Cantidad de productos entregados y el stock actualizado
print(f"Se entregaron {productos_seleccionados} unidades del producto.")
print(f"El stock disponible ahora es de {stock_actualizado} unidades.")

