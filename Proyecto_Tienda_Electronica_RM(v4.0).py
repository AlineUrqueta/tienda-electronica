# ==========================================
# Proyecto: Tienda Electrónica RM
# Asignatura: Introducción a la Programación
# Grupo 4
# Tercera Entrega
# ==========================================

# ==========================================
# LISTAS PARA ALMACENAR LOS REGISTROS
# ==========================================

clientes = []
productos = []
proveedores = []
empleados = []
ventas = []
ordenesCompra = []


opcion = ""

while opcion != "9":

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

    while True:
      try:
        opcion = input("Seleccione una opción: ")

        if int(opcion) >= 1 and int(opcion) <= 9:
            break
        else:
            print("Error: Debe ingresar un número entre 1 y 9.")

      except:
        print("Error: Debe ingresar un número entre 1 y 9.")

    print()

    if opcion == "1":

        print("========================================")
        print("      REGISTRO DE CLIENTES")
        print("========================================")
        print()

        rut = input("Ingrese RUT del cliente: ")
        while rut.strip() == "":
            print("Error: El RUT no puede quedar vacío.")
            rut = input("Ingrese RUT del cliente: ")

        # --- Validación: evitar RUT duplicado ---
        existeRut = False
        for cliente in clientes:
            if cliente[0] == rut:
                existeRut = True

        while existeRut:
            print("Error: Ese RUT ya está registrado.")
            rut = input("Ingrese RUT del cliente: ")
            existeRut = False
            for cliente in clientes:
                if cliente[0] == rut:
                    existeRut = True

        nombre = input("Ingrese nombre del cliente: ")
        while nombre.strip() == "" or not nombre.replace(" ", "").isalpha():
            if nombre.strip() == "":
                print("Error: El nombre no puede quedar vacío.")
            else:
                print("Error: El nombre solo debe contener letras.")
            nombre = input("Ingrese nombre del cliente: ")

        telefono = input("Ingrese teléfono: ")
        while telefono.strip() == "" or not telefono.isdigit():
            if telefono.strip() == "":
                print("Error: El teléfono no puede quedar vacío.")
            else:
                print("Error: El teléfono solo debe contener números.")
            telefono = input("Ingrese teléfono: ")

        correo = input("Ingrese correo electrónico: ")

        while correo.strip() == "" or "@" not in correo:
            if correo.strip() == "":
                print("Error: El correo electrónico no puede quedar vacío.")
            else:
                print("Error: El correo debe contener el símbolo @.")
            correo = input("Ingrese correo electrónico: ")

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

    elif opcion == "2":

        print("========================================")
        print("      REGISTRO DE PRODUCTOS")
        print("========================================")
        print()

        codigoProducto = input("Ingrese código del producto: ")
        while codigoProducto.strip() == "":
            print("Error: El código del producto no puede quedar vacío.")
            codigoProducto = input("Ingrese código del producto: ")

        # --- Validación: evitar código de producto duplicado ---
        existeCodigo = False
        for producto in productos:
            if producto[0] == codigoProducto:
                existeCodigo = True

        while existeCodigo:
            print("Error: Ese código de producto ya existe.")
            codigoProducto = input("Ingrese código del producto: ")
            existeCodigo = False
            for producto in productos:
                if producto[0] == codigoProducto:
                    existeCodigo = True

        nombreProducto = input("Ingrese nombre del producto: ")
        while nombreProducto.strip() == "":
            print("Error: El nombre del producto no puede quedar vacío.")
            nombreProducto = input("Ingrese nombre del producto: ")

        marca = input("Ingrese marca del producto: ")
        while marca.strip() == "":
            print("Error: La marca del producto no puede quedar vacía.")
            marca = input("Ingrese marca del producto: ")   

        while True:
         try:
            precio = float(input("Ingrese precio del producto: "))

            if precio <= 0:
                print("Error: El precio debe ser mayor que cero.")
            else:
              break

         except:
           print("Error: Debe ingresar un número válido, no se permiten letras.")

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

    elif opcion == "3":

        print("========================================")
        print("     REGISTRO DE PROVEEDORES")
        print("========================================")
        print()

        rutProveedor = input("Ingrese RUT del proveedor: ")
        while rutProveedor.strip() == "":
            print("Error: El RUT del proveedor no puede quedar vacío.")
            rutProveedor = input("Ingrese RUT del proveedor: ")

        # --- Validación: evitar RUT de proveedor duplicado ---
        existeRutProveedor = False
        for proveedor in proveedores:
            if proveedor[0] == rutProveedor:
                existeRutProveedor = True

        while existeRutProveedor:
            print("Error: Ese RUT ya está registrado.")
            rutProveedor = input("Ingrese RUT del proveedor: ")
            existeRutProveedor = False
            for proveedor in proveedores:
                if proveedor[0] == rutProveedor:
                    existeRutProveedor = True

        nombreProveedor = input("Ingrese nombre del proveedor: ")
        while nombreProveedor.strip() == "" or not nombreProveedor.replace(" ", "").isalpha():
            if nombreProveedor.strip() == "":
                print("Error: El nombre del proveedor no puede quedar vacío.")
            else:
                print("Error: El nombre del proveedor solo debe contener letras.")
            nombreProveedor = input("Ingrese nombre del proveedor: ")

        telefonoProveedor = input("Ingrese teléfono del proveedor: ")
        while telefonoProveedor.strip() == "" or not telefonoProveedor.isdigit():
            if telefonoProveedor.strip() == "":
                print("Error: El teléfono del proveedor no puede quedar vacío.")
            else:
                print("Error: El teléfono del proveedor solo debe contener números.")
            telefonoProveedor = input("Ingrese teléfono del proveedor: ")


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

    elif opcion == "4":

        print("========================================")
        print("      REGISTRO DE EMPLEADOS")
        print("========================================")
        print()

        rutEmpleado = input("Ingrese RUT del empleado: ")
        while rutEmpleado.strip() == "":
            print("Error: El RUT del empleado no puede quedar vacío.")
            rutEmpleado = input("Ingrese RUT del empleado: ")

        # --- Validación: evitar RUT de empleado duplicado ---
        existeRutEmpleado = False
        for empleado in empleados:
            if empleado[0] == rutEmpleado:
                existeRutEmpleado = True

        while existeRutEmpleado:
            print("Error: Ese RUT ya está registrado.")
            rutEmpleado = input("Ingrese RUT del empleado: ")
            existeRutEmpleado = False
            for empleado in empleados:
                if empleado[0] == rutEmpleado:
                    existeRutEmpleado = True

        nombreEmpleado = input("Ingrese nombre del empleado: ")
        while nombreEmpleado.strip() == "" or not nombreEmpleado.replace(" ", "").isalpha():
            if nombreEmpleado.strip() == "":
                print("Error: El nombre del empleado no puede quedar vacío.")
            else:
                print("Error: El nombre del empleado solo debe contener letras.")
            nombreEmpleado = input("Ingrese nombre del empleado: ")
            
        cargo = input("Ingrese cargo del empleado: ")
        while cargo.strip() == "":
            print("Error: El cargo del empleado no puede quedar vacío.")
            cargo = input("Ingrese cargo del empleado: ")

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

    elif opcion == "5":

        print("========================================")
        print("       REGISTRO DE VENTAS")
        print("========================================")
        print()

        folio = input("Ingrese número de boleta o factura: ")
        while folio.strip() == "":
            print("Error: El número de boleta o factura no puede quedar vacío.")
            folio = input("Ingrese número de boleta o factura: ")

        # --- Validación: evitar folio duplicado ---
        existeFolio = False
        for venta in ventas:
            if venta[0] == folio:
                existeFolio = True

        while existeFolio:
            print("Error: Ese número de boleta o factura ya fue utilizado.")
            folio = input("Ingrese número de boleta o factura: ")
            existeFolio = False
            for venta in ventas:
                if venta[0] == folio:
                    existeFolio = True

        rutCliente = input("Ingrese RUT del cliente: ")
        while rutCliente.strip() == "":
            print("Error: El RUT del cliente no puede quedar vacío.")
            rutCliente = input("Ingrese RUT del cliente: ") 

        # --- Validación: el cliente debe existir ---
        clienteExiste = False
        for cliente in clientes:
            if cliente[0] == rutCliente:
                clienteExiste = True

        while not clienteExiste:
            print("Error: El cliente no está registrado.")
            rutCliente = input("Ingrese RUT del cliente: ")
            clienteExiste = False
            for cliente in clientes:
                if cliente[0] == rutCliente:
                    clienteExiste = True

        codigoProducto = input("Ingrese código del producto: ")
        while codigoProducto.strip() == "":
            print("Error: El código del producto no puede quedar vacío.")
            codigoProducto = input("Ingrese código del producto: ")

        # --- Validación: el producto debe existir ---
        productoExiste = False
        for producto in productos:
            if producto[0] == codigoProducto:
                productoExiste = True

        while not productoExiste:
            print("Error: El producto no está registrado.")
            codigoProducto = input("Ingrese código del producto: ")
            productoExiste = False
            for producto in productos:
                if producto[0] == codigoProducto:
                    productoExiste = True

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

    elif opcion == "6":

        print("========================================")
        print("   REGISTRO DE ORDEN DE COMPRA")
        print("========================================")
        print()

        numeroOrden = input("Ingrese número de orden: ")
        while numeroOrden.strip() == "":
            print("Error: El número de orden no puede quedar vacío.")
            numeroOrden = input("Ingrese número de orden: ")

        # --- Validación: evitar número de orden duplicado ---
        existeOrden = False
        for orden in ordenesCompra:
            if orden[0] == numeroOrden:
                existeOrden = True

        while existeOrden:
            print("Error: Ese número de orden ya fue utilizado.")
            numeroOrden = input("Ingrese número de orden: ")
            existeOrden = False
            for orden in ordenesCompra:
                if orden[0] == numeroOrden:
                    existeOrden = True

        codigoProducto = input("Ingrese código del producto: ")
        while codigoProducto.strip() == "":
            print("Error: El código del producto no puede quedar vacío.")
            codigoProducto = input("Ingrese código del producto: ")

        rutProveedor = input("Ingrese RUT del proveedor: ")
        while rutProveedor.strip() == "":
            print("Error: El RUT del proveedor no puede quedar vacío.")
            rutProveedor = input("Ingrese RUT del proveedor: ")

        # --- Validación: el proveedor debe existir ---
        proveedorExiste = False
        for proveedor in proveedores:
            if proveedor[0] == rutProveedor:
                proveedorExiste = True

        while not proveedorExiste:
            print("Error: El proveedor no está registrado.")
            rutProveedor = input("Ingrese RUT del proveedor: ")
            proveedorExiste = False
            for proveedor in proveedores:
                if proveedor[0] == rutProveedor:
                    proveedorExiste = True


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

    elif opcion == "7":

         print("========================================")
         print("      CONSULTA DE CLIENTES")
         print("========================================")

         if len(clientes) == 0:
             print("No existen clientes registrados.")

         else:
           
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

    elif opcion == "8":

         print("========================================")
         print("      CONSULTA DE PRODUCTOS")
         print("========================================")

         if len(productos) == 0:
             print("No existen productos registrados.")
             print()
             print("----------------------------------------")
             input("Presione ENTER para volver al menú...")

         else:
           
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

    elif opcion == "9":

        print("========================================")
        print(" Gracias por utilizar el sistema")
        print("   Tienda Electrónica RM")
        print("========================================")
        print()

    else:
     print("Error: Debe ingresar un número entre 1 y 9.")