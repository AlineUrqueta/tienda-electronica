# ==========================================
# Proyecto: Tienda Electrónica RM
# Asignatura: Introducción a la Programación
# Grupo 4 - Cuarta Entrega
# ==========================================


# ==========================================
# FUNCIONES DE VALIDACIÓN DE ENTRADA
# Reutilizables por los distintos registros, para evitar repetir la misma lógica
# ==========================================

# Función reutilizable para solicitar un texto y validar que no esté vacío.
# Utiliza strip() para eliminar espacios al inicio y al final antes de comprobar.
# El ciclo while repite el ingreso mientras el texto esté vacío.
def pedir_texto_no_vacio(mensaje, mensaje_error):
    texto = input(mensaje)
    while texto.strip() == "":
        print(mensaje_error)
        texto = input(mensaje)
    return texto

# Función reutilizable para validar el ingreso de un correo electrónico.
# strip() permite comprobar que el campo no contenga solamente espacios.
# El operador "not in" verifica que el correo contenga el carácter @.
def pedir_correo(mensaje):
    correo = input(mensaje)
    while correo.strip() == "" or "@" not in correo:
        if correo.strip() == "":
            print("Error: El correo electrónico no puede quedar vacío.")
        else:
            print("Error: El correo debe contener el símbolo @.")
        correo = input(mensaje)
    return correo

# Función reutilizable para solicitar y validar el precio de un producto.
# float() convierte el dato ingresado a un número decimal.
# try-except ValueError evita que el programa se detenga si se ingresa
# un valor que no puede convertirse a número.
# El ciclo while permite repetir el ingreso hasta obtener un precio válido.
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

# Función que muestra en pantalla las opciones disponibles del menú principal.
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

# Función que solicita la opción del menú y valida que corresponda a un número entero entre 1 y 9.
# int() convierte la entrada de texto a entero y ValueError controla
# el ingreso de datos que no pueden convertirse a número.
def pedir_opcion():
    while True:
        try:
            opcion = input("Seleccione una opción: ")
            numero = int(opcion)
            if numero >= 1 and numero <= 9:
                return opcion
            
            else:
                print("Error: Debe ingresar un número entre 1 y 9.")

        except ValueError:
            print("Error: Debe ingresar un número entre 1 y 9.")


# ==========================================
# FUNCIONES DE REGISTRO
# Cada una pide los datos de un módulo, los muestra y los agrega a su lista
# ==========================================

# Registra un nuevo cliente utilizando las funciones de validación.
# Los datos validados se almacenan como una lista dentro de la lista clientes.
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

    # append() agrega una lista con los datos del cliente a la lista clientes.
    clientes.append([rut, nombre, telefono, correo])

    input("Presione ENTER para volver al menú...")
    print()


# Solicita y valida los datos del producto mediante funciones auxiliares.
# Luego almacena el registro como una lista dentro de la lista productos.
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

    # append() agrega una lista con los datos del producto a la lista productos.
    productos.append([codigoProducto, nombreProducto, marca, precio])

    print()


# Solicita y valida los datos del proveedor mediante una función auxiliar.
# Luego almacena el registro como una lista dentro de la lista proveedores.
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
    
    # append() agrega una lista con los datos del proveedor a la lista proveedores.
    proveedores.append([rutProveedor, nombreProveedor, telefonoProveedor])

    input("Presione ENTER para volver al menú...")
    print()


# Solicita y valida los datos del empleado mediante una función auxiliar.
# Luego almacena el registro como una lista dentro de la lista empleados.
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

    # append() agrega una lista con los datos del empleado a la lista empleados.
    empleados.append([rutEmpleado, nombreEmpleado, cargo])

    input("Presione ENTER para volver al menú...")
    print()


# Solicita y valida los datos de la venta mediante una función auxiliar.
# Luego almacena el registro como una lista dentro de la lista ventas.
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
    
    # append() agrega una lista con los datos de la venta a la lista ventas.
    ventas.append([folio, rutCliente, codigoProducto])

    input("Presione ENTER para volver al menú...")
    print()


# Solicita y valida los datos de la orden de compra mediante una función auxiliar.
# Luego almacena el registro como una lista dentro de la lista ordenesCompra.
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

    # append() agrega una lista con los datos de la orden de compra a la lista ordenesCompra.
    ordenesCompra.append([numeroOrden, codigoProducto, rutProveedor])

    input("Presione ENTER para volver al menú...")
    print()


# ==========================================
# FUNCIONES DE CONSULTA
# Recorren la lista con un ciclo for, usando contador (y acumulador cuando corresponde)
# ==========================================

# Recorre la lista de clientes con for, muestra los datos almacenados
# mediante índices y utiliza un contador para determinar la cantidad de registros.
def consultar_clientes(clientes):
    print("========================================")
    print("      CONSULTA DE CLIENTES")
    print("========================================")

    if len(clientes) == 0:
        print("No existen clientes registrados.")
        print()
        print("----------------------------------------")
        input("Presione ENTER para volver al menú...")
        return
        
    # El contador comienza en 0 y aumentará por cada cliente recorrido.
    contador = 0

    # for recorre cada elemento de la lista clientes.
    for cliente in clientes:
        print("----------------------------------------")
        print("RUT      :", cliente[0])
        print("Nombre   :", cliente[1])
        print("Teléfono :", cliente[2])
        print("Correo   :", cliente[3])

        # Aumenta el contador en 1 cada vez que se encuentra un cliente.
        contador = contador + 1

    print("----------------------------------------")
    print("Total de clientes registrados:", contador)

    print("----------------------------------------")
    input("Presione ENTER para volver al menú...")


# Recorre la lista de productos con for, muestra sus datos mediante índices,
# utiliza un contador y acumula los precios de los productos registrados.
def consultar_productos(productos):
    print("========================================")
    print("      CONSULTA DE PRODUCTOS")
    print("========================================")

    # len() permite verificar si existen elementos almacenados en la lista.
    if len(productos) == 0:
        print("No existen productos registrados.")
        print()
        print("----------------------------------------")
        input("Presione ENTER para volver al menú...")
        return

    # contador permite contar los productos recorridos.
    # totalPrecios comienza en 0 y acumula el precio de cada producto.
    contador = 0
    totalPrecios = 0

    # for recorre cada producto almacenado en la lista productos.
    for producto in productos:
        print("----------------------------------------")
        # Los índices permiten acceder a los datos almacenados en cada producto.
        print("Código :", producto[0])
        print("Nombre :", producto[1])
        print("Marca  :", producto[2])
        print("Precio : $", producto[3])

        # Incrementa el contador por cada producto recorrido.
        contador = contador + 1
        
        # Acumula el precio del producto para obtener el valor total.
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

# Función principal que crea las listas del sistema y controla el menú.
# Desde aquí se llaman las funciones correspondientes a cada opción seleccionada.
def main():
   
    # Se crean listas para almacenar los registros de cada módulo del sistema.
    clientes = []
    productos = []
    proveedores = []
    empleados = []
    ventas = []
    ordenesCompra = []

    # Variable utilizada para almacenar la opción seleccionada en el menú.
    opcion = ""

    # El ciclo mantiene el menú activo hasta que el usuario seleccione la opción 9.
    while opcion != "9":

        # Llama a la función que muestra las opciones disponibles del menú.
        mostrar_menu()
        
        # Llama a la función que solicita y valida la opción ingresada.
        opcion = pedir_opcion()
        print()


        # Según la opción seleccionada, se llama a la función correspondiente.
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

# Llama a la función principal para iniciar la ejecución del sistema.
main()
