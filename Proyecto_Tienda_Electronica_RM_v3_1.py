# ==========================================
# Proyecto: Tienda Electrónica RM
# Asignatura: Introducción a la Programación
# Grupo 4
# Cuarta Entrega - Programación Modular (Funciones)
# ==========================================


# ==========================================
# FUNCIONES DE VALIDACIÓN DE ENTRADA
# Reutilizables por los distintos registros, para evitar repetir la misma lógica
# ==========================================

# Pide un texto por teclado y no deja continuar hasta que no quede vacío
def pedir_texto_no_vacio(mensaje, mensaje_error):
    texto = input(mensaje)
    while texto.strip() == "":
        print(mensaje_error)
        texto = input(mensaje)
    return texto


# Pide un correo electrónico y valida que no esté vacío y que contenga el símbolo @
def pedir_correo(mensaje):
    correo = input(mensaje)
    while correo.strip() == "" or "@" not in correo:
        if correo.strip() == "":
            print("Error: El correo electrónico no puede quedar vacío.")
        else:
            print("Error: El correo debe contener el símbolo @.")
        correo = input(mensaje)
    return correo


# Pide el precio de un producto y valida que sea un número mayor que cero
def pedir_precio(mensaje):
    while True:
        try:
            precio = float(input(mensaje))

            if precio <= 0:
                print("Error: El precio debe ser mayor que cero.")
            else:
                return precio

        except ValueError:
            print("Error: Debe ingresar un número válido, no se permiten letras.")


# ==========================================
# FUNCIONES DEL MENÚ PRINCIPAL
# ==========================================

# Muestra las opciones del menú principal
def mostrar_menu():
    print()
    print("========================================")
    print("       TIENDA ELECTRÓNICA RM")
    print("========================================")
    print("1. Registrar Cliente")
    print("2. Registrar Producto")
    print("3. Registrar Proveedor")
    print("4. Registrar Empleado")
    print("5. Registrar Venta")
    print("6. Registrar Orden de Compra")
    print("7. Consultar Clientes")
    print("8. Consultar Productos")
    print("9. Salir")
    print("========================================")
    print()


# Pide la opción del menú y valida que sea un número entre 1 y 9
def pedir_opcion():
    while True:
        try:
            opcion = input("Seleccione una opción: ")

            if int(opcion) >= 1 and int(opcion) <= 9:
                return opcion
            else:
                print("Error: Debe ingresar un número entre 1 y 9.")

        except ValueError:
            print("Error: Debe ingresar un número entre 1 y 9.")


# ==========================================
# FUNCIONES DE REGISTRO
# Cada una pide los datos de un módulo, los muestra y los agrega a su lista
# ==========================================

# Pide los datos de un cliente y lo agrega a la lista de clientes
def registrar_cliente(clientes):
    print("========================================")
    print("      REGISTRO DE CLIENTES")
    print("========================================")
    print()

    rut = pedir_texto_no_vacio("Ingrese RUT del cliente: ", "Error: El RUT no puede quedar vacío.")
    nombre = pedir_texto_no_vacio("Ingrese nombre del cliente: ", "Error: El nombre no puede quedar vacío.")
    telefono = pedir_texto_no_vacio("Ingrese teléfono: ", "Error: El teléfono no puede quedar vacío.")
    correo = pedir_correo("Ingrese correo electrónico: ")

    print("========================================")
    print("      CLIENTE REGISTRADO")
    print("========================================")
    print("RUT:", rut)
    print("Nombre:", nombre)
    print("Teléfono:", telefono)
    print("Correo:", correo)
    print("========================================")

    clientes.append([rut, nombre, telefono, correo])

    input("Presione ENTER para volver al menú...")
    print()


# Pide los datos de un producto y lo agrega a la lista de productos
def registrar_producto(productos):
    print("========================================")
    print("      REGISTRO DE PRODUCTOS")
    print("========================================")
    print()

    codigoProducto = pedir_texto_no_vacio("Ingrese código del producto: ", "Error: El código del producto no puede quedar vacío.")
    nombreProducto = pedir_texto_no_vacio("Ingrese nombre del producto: ", "Error: El nombre del producto no puede quedar vacío.")
    marca = pedir_texto_no_vacio("Ingrese marca del producto: ", "Error: La marca del producto no puede quedar vacía.")
    precio = pedir_precio("Ingrese precio del producto: ")

    print()
    print("========================================")
    print("      PRODUCTO REGISTRADO")
    print("========================================")
    print("Código :", codigoProducto)
    print("Nombre :", nombreProducto)
    print("Marca  :", marca)
    print("Precio : $", precio)
    print("========================================")
    input("Presione ENTER para volver al menú...")

    productos.append([codigoProducto, nombreProducto, marca, precio])

    print()


# Pide los datos de un proveedor y lo agrega a la lista de proveedores
def registrar_proveedor(proveedores):
    print("========================================")
    print("     REGISTRO DE PROVEEDORES")
    print("========================================")
    print()

    rutProveedor = pedir_texto_no_vacio("Ingrese RUT del proveedor: ", "Error: El RUT del proveedor no puede quedar vacío.")
    nombreProveedor = pedir_texto_no_vacio("Ingrese nombre del proveedor: ", "Error: El nombre del proveedor no puede quedar vacío.")
    telefonoProveedor = pedir_texto_no_vacio("Ingrese teléfono del proveedor: ", "Error: El teléfono del proveedor no puede quedar vacío.")

    print()
    print("========================================")
    print("    PROVEEDOR REGISTRADO")
    print("========================================")
    print("RUT      :", rutProveedor)
    print("Nombre   :", nombreProveedor)
    print("Teléfono :", telefonoProveedor)
    print("========================================")

    proveedores.append([rutProveedor, nombreProveedor, telefonoProveedor])

    input("Presione ENTER para volver al menú...")
    print()


# Pide los datos de un empleado y lo agrega a la lista de empleados
def registrar_empleado(empleados):
    print("========================================")
    print("      REGISTRO DE EMPLEADOS")
    print("========================================")
    print()

    rutEmpleado = pedir_texto_no_vacio("Ingrese RUT del empleado: ", "Error: El RUT del empleado no puede quedar vacío.")
    nombreEmpleado = pedir_texto_no_vacio("Ingrese nombre del empleado: ", "Error: El nombre del empleado no puede quedar vacío.")
    cargo = pedir_texto_no_vacio("Ingrese cargo del empleado: ", "Error: El cargo del empleado no puede quedar vacío.")

    print()
    print("========================================")
    print("     EMPLEADO REGISTRADO")
    print("========================================")
    print("RUT    :", rutEmpleado)
    print("Nombre :", nombreEmpleado)
    print("Cargo  :", cargo)
    print("========================================")

    empleados.append([rutEmpleado, nombreEmpleado, cargo])

    input("Presione ENTER para volver al menú...")
    print()


# Pide los datos de una venta y la agrega a la lista de ventas
def registrar_venta(ventas):
    print("========================================")
    print("       REGISTRO DE VENTAS")
    print("========================================")
    print()

    folio = pedir_texto_no_vacio("Ingrese número de boleta o factura: ", "Error: El número de boleta o factura no puede quedar vacío.")
    rutCliente = pedir_texto_no_vacio("Ingrese RUT del cliente: ", "Error: El RUT del cliente no puede quedar vacío.")
    codigoProducto = pedir_texto_no_vacio("Ingrese código del producto: ", "Error: El código del producto no puede quedar vacío.")

    print()
    print("========================================")
    print("       VENTA REGISTRADA")
    print("========================================")
    print("Boleta/Factura :", folio)
    print("RUT Cliente    :", rutCliente)
    print("Producto       :", codigoProducto)
    print("========================================")

    ventas.append([folio, rutCliente, codigoProducto])

    input("Presione ENTER para volver al menú...")
    print()


# Pide los datos de una orden de compra y la agrega a la lista de órdenes de compra
def registrar_orden_compra(ordenesCompra):
    print("========================================")
    print("   REGISTRO DE ORDEN DE COMPRA")
    print("========================================")
    print()

    numeroOrden = pedir_texto_no_vacio("Ingrese número de orden: ", "Error: El número de orden no puede quedar vacío.")
    codigoProducto = pedir_texto_no_vacio("Ingrese código del producto: ", "Error: El código del producto no puede quedar vacío.")
    rutProveedor = pedir_texto_no_vacio("Ingrese RUT del proveedor: ", "Error: El RUT del proveedor no puede quedar vacío.")

    print()
    print("========================================")
    print(" ORDEN DE COMPRA REGISTRADA")
    print("========================================")
    print("Orden      :", numeroOrden)
    print("Producto   :", codigoProducto)
    print("Proveedor  :", rutProveedor)
    print("========================================")

    ordenesCompra.append([numeroOrden, codigoProducto, rutProveedor])

    input("Presione ENTER para volver al menú...")
    print()


# ==========================================
# FUNCIONES DE CONSULTA
# Recorren la lista con un ciclo for, usando contador (y acumulador cuando corresponde)
# ==========================================

# Muestra todos los clientes registrados y el total de clientes
def consultar_clientes(clientes):
    print("========================================")
    print("      CONSULTA DE CLIENTES")
    print("========================================")

    if len(clientes) == 0:
        print("No existen clientes registrados.")
        return

    contador = 0

    for cliente in clientes:
        print("----------------------------------------")
        print("RUT      :", cliente[0])
        print("Nombre   :", cliente[1])
        print("Teléfono :", cliente[2])
        print("Correo   :", cliente[3])

        contador = contador + 1

    print("----------------------------------------")
    print("Total de clientes registrados:", contador)

    print("----------------------------------------")
    input("Presione ENTER para volver al menú...")


# Muestra todos los productos registrados, el total de productos y el valor total
def consultar_productos(productos):
    print("========================================")
    print("      CONSULTA DE PRODUCTOS")
    print("========================================")

    if len(productos) == 0:
        print("No existen productos registrados.")
        print()
        print("----------------------------------------")
        input("Presione ENTER para volver al menú...")
        return

    contador = 0
    totalPrecios = 0

    for producto in productos:
        print("----------------------------------------")
        print("Código :", producto[0])
        print("Nombre :", producto[1])
        print("Marca  :", producto[2])
        print("Precio : $", producto[3])

        contador = contador + 1
        totalPrecios = totalPrecios + producto[3]

    print("----------------------------------------")
    print("Total de productos registrados:", contador)
    print("Valor total de los productos: $", totalPrecios)

    print("----------------------------------------")
    input("Presione ENTER para volver al menú...")


# ==========================================
# PROGRAMA PRINCIPAL
# Contiene las listas de registros y coordina el menú, llamando a las funciones anteriores
# ==========================================

# Crea las listas de registros y controla el menú, llamando a las demás funciones
def main():
    clientes = []
    productos = []
    proveedores = []
    empleados = []
    ventas = []
    ordenesCompra = []

    opcion = ""

    while opcion != "9":

        mostrar_menu()
        opcion = pedir_opcion()
        print()

        if opcion == "1":
            registrar_cliente(clientes)

        elif opcion == "2":
            registrar_producto(productos)

        elif opcion == "3":
            registrar_proveedor(proveedores)

        elif opcion == "4":
            registrar_empleado(empleados)

        elif opcion == "5":
            registrar_venta(ventas)

        elif opcion == "6":
            registrar_orden_compra(ordenesCompra)

        elif opcion == "7":
            consultar_clientes(clientes)

        elif opcion == "8":
            consultar_productos(productos)

        elif opcion == "9":
            print("========================================")
            print(" Gracias por utilizar el sistema")
            print("   Tienda Electrónica RM")
            print("========================================")
            print()


main()
