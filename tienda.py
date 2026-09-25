print("================================")
print("       TIENDA DE FELIPE")
print("================================")

nombre = input("Ingrese su nombre: ")
producto = input("Ingrese el nombre del producto: ")
precio = int(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad: "))

total = precio * cantidad

print("\n--- RESUMEN DE COMPRA ---")
print("Cliente: ", nombre)
print("Producto: ", producto)
print("Precio: ", precio)
print("Cantidad: ", cantidad)
print("Total: ", total)

descuento = (total * 10 / 100) if total > 100 else 0

print("Descuento: ", descuento)

total_final = total - descuento

print("Total a pagar: ", total_final)

print("\nGracias por su compra, ", nombre, "!")