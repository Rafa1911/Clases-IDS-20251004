clientes = [input("Dijite clientes: ")]
productos = [input("Dijite el producto: ")]
pedidos = [input("Digite el pedido: ")]

# Función para generar códigos automáticos
def generar_codigo(prefijo, numero):
    return f"{prefijo}{numero:03d}"

# Menú principal
opcion = ""

while opcion != "8":
    print("\n===== CAFETERÍA ESEN BREW =====")
    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Registrar nuevo cliente")
    print("4. Mostrar clientes")
    print("5. Registrar pedido")
    print("6. Mostrar pedidos del día")
    print("7. Mostrar categorías disponibles")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    # 1. Mostrar productos
    if opcion == "1":
        if not productos:
            print("No hay productos registrados.")
        else:
            print("\n--- PRODUCTOS ---")
            for p in productos:
                print(f"{p['codigo']} | {p['nombre']} | {p['categoria']} | ${p['precio']:.2f}")

    # 2. Agregar producto
    elif opcion == "2":
        print("\n--- AGREGAR PRODUCTO ---")
        nombre = input("Nombre del producto: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))
        codigo = generar_codigo("P", len(productos) + 1)
        productos.append({"codigo": codigo, "nombre": nombre, "categoria": categoria, "precio": precio})
        print(f"Producto agregado con código: {codigo}")

    # 3. Registrar cliente
    elif opcion == "3":
        print("\n--- REGISTRAR CLIENTE ---")
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        telefono = input("Teléfono: ")
        codigo = generar_codigo("C", len(clientes) + 1)
        clientes.append({"codigo": codigo, "nombre": nombre, "correo": correo, "telefono": telefono})
        print(f"Cliente registrado con código: {codigo}")

    # 4. Mostrar clientes
    elif opcion == "4":
        if not clientes:
            print("No hay clientes.")
        else:
            print("\n--- CLIENTES ---")
            for c in clientes:
                print(f"{c['codigo']} | {c['nombre']} | {c['correo']} | {c['telefono']}")

    # 5. Registrar pedido
    elif opcion == "5":
        print("\n--- REGISTRAR PEDIDO ---")
        cod_cliente = input("Ingrese código del cliente (ej: C001): ")

        encontrado = False
        for c in clientes:
            if c["codigo"] == cod_cliente:
                encontrado = True
                break

        if not encontrado:
            print("Cliente no encontrado.")
        else:
            print("Ingrese los códigos de productos. Escriba FIN para terminar.")
            for p in productos:
                print(f"{p['codigo']} - {p['nombre']} (${p['precio']})")

            items = []
            total = 0

            while True:
                cod_prod = input("Producto: ").upper()
                if cod_prod == "FIN":
                    break
                for p in productos:
                    if p["codigo"] == cod_prod:
                        items.append(cod_prod)
                        total += p["precio"]
                        print("Producto agregado.")
                        break
                else:
                    print("Producto no encontrado.")

            if items:
                codigo_pedido = generar_codigo("O", len(pedidos) + 1)
                pedidos.append({"codigo": codigo_pedido, "cliente": cod_cliente, "items": items, "total": total})
                print(f"Pedido registrado. Código: {codigo_pedido} | Total: ${total:.2f}")
            else:
                print("Pedido vacío. No se registró.")

    # 6. Mostrar pedidos
    elif opcion == "6":
        if not pedidos:
            print("No hay pedidos registrados.")
        else:
            print("\n--- PEDIDOS DEL DÍA ---")
            for o in pedidos:
                print(f"{o['codigo']} | Cliente: {o['cliente']} | Productos: {o['items']} | Total: ${o['total']:.2f}")

    # 7. Categorías disponibles
    elif opcion == "7":
        categorias = set([p["categoria"] for p in productos])
        print("\n--- CATEGORÍAS DISPONIBLES ---")
        for c in categorias:
            print("-", c)

    elif opcion == "8":
        print("Gracias por usar ESEN Brew ☕")
    else:
        print("Opción inválida, intente de nuevo.")
