import utilidades
import producto
import cliente

list_productos = []
list_clientes = []

def op1():

   global list_productos
   utilidades.imp("\tREGISTRAR PRODUCTOS\n")
   op = utilidades.cicloIntento("¿Cuantos productos desea registrar?\n", "Dato invalido, por favor intente nuevamente")
   numero = 0
   for i in range(op):
        
        numero = i + 1
        utilidades.imp(f"¿Cual es el tipo del producto Nro.{numero} que desea registrar?")
        utilidades.imp("1. Electronico")
        utilidades.imp("2. Ropa")    
        utilidades.imp("3. Otro") 

        op = utilidades.cicloIntento("Ingrese una opción\n", "Dato invalido, por favor intente nuevamente")

        match op:

            case 1:

                utilidades.imp("\tPRODUCTO TIPO ELECTRONICO\n")
                nombre_prod = utilidades.lea("Ingrese el nombre del producto\n")
                precio_prod = utilidades.cicloIntentoFloat("Ingrese el precio del producto\n",
                                                           "Dato invalido, por favor digite el precio en datos numericos")
                
                unidades_prod = utilidades.cicloIntento("¿Cuantas unidades del producto desea registrar?\n",
                                                        "Las unidades se mide en numeros enteros(1,2,3,...), por favor intente nuevamente")
                
                garantia_prod = utilidades.cicloIntento("¿Cuantos meses de garantia poseera el producto?\n",
                                                        "Error, dato invalido, por favor digite la cantidad de meses de garantia del producto")
                
                list_productos.append(producto.Produc_electronico(nombre_prod, precio_prod, unidades_prod, garantia_prod))
                utilidades.imp("\nProducto registrado exitosamente.\n")

            case 2:

                utilidades.imp("\tPRODUCTO TIPO ROPA\n")
                nombre_prod = utilidades.lea("Ingrese el nombre del producto\n")
                precio_prod = utilidades.cicloIntentoFloat("Ingrese el precio del producto\n",
                                                           "Dato invalido, por favor digite el precio en datos numericos")
                
                unidades_prod = utilidades.cicloIntento("¿Cuantas unidades del producto desea registrar?\n",
                                                        "Las unidades se mide en numeros enteros(1,2,3,...), por favor intente nuevamente")
                
                talla_prod = utilidades.lea("Ingrese la talla\n")
                list_productos.append(producto.Produc_ropa(nombre_prod, precio_prod, unidades_prod, talla_prod))
                utilidades.imp("\nProducto registrado exitosamente.\n")

            case 3:

                utilidades.imp("\tPRODUCTO TIPO OTRO\n")
                nombre_prod = utilidades.lea("Ingrese el nombre del producto\n")
                precio_prod = utilidades.cicloIntentoFloat("Ingrese el precio del producto\n",
                                                           "Dato invalido, por favor digite el precio en datos numericos")
                
                unidades_prod = utilidades.cicloIntento("¿Cuantas unidades del producto desea registrar?\n",
                                                        "Las unidades se mide en numeros enteros(1,2,3,...), por favor intente nuevamente")
                
                list_productos.append(producto.Producto(nombre_prod, precio_prod, unidades_prod))
                utilidades.imp("\nProducto registrado exitosamente.\n")

            case _:

                utilidades.imp("Por favor ingrese una opción que este en el menú.")
                




def op2():

    global list_productos
    utilidades.imp("\tCATALOGO DE PRODUCTOS\n")
    if len(list_productos) != 0:

        numero = 0
        for items_prod in list_productos:

            numero += 1
            utilidades.imp(f"Producto Nro{numero}.\nNombre: {items_prod.nombre_producto}\nPrecio base: {items_prod.precio_base}")
            if isinstance(items_prod, producto.Produc_ropa):
                utilidades.imp(f"Descuento: {items_prod.aplicar_descuento()}, solo aplica al comprar más de 50 unidades\nTalla: {items_prod.talla}\n")

            elif isinstance(items_prod, producto.Produc_electronico):
                utilidades.imp(f"Descuento: {items_prod.aplicar_descuento()}\n")

            else:
                utilidades.imp("Descuento: N/A\n")

    else:
        utilidades.imp("Aún NO hay productos registrados.")
        while True:

            op = utilidades.cicloIntento("¿Desea ir a registrar productos?\n1. SI\n2.NO\n\nDigite una opción\n",
                                "Dato invalido, por favor digite el precio en datos numericos")

            match op:

                case 1:

                    op1()
                    break

                case 2:

                    utilidades.imp("Saliendo...\n")
                    break

                case _:

                    utilidades.imp("opción invalida, por favor digite 1 ó 2")                    

        
    

def op3():

    global list_clientes
    utilidades.imp("\tREGISTRAR CLIENTES\n")
    op = utilidades.cicloIntento("¿Cuantos clientes desea registrar?\n", "Dato invalido, por favor intente nuevamente")
    numero = 0
    for i in range(op):

        numero = i + 1
        nombre_client = utilidades.lea(f"{numero}.\nIngrese el nombre del cliente\n").upper()
        list_clientes.append(cliente.Cliente(nombre_client))
        if op != 1:

            utilidades.imp(f"\nCliente Nro.{numero} registrado correctamente.\n")
            
        else:

            utilidades.imp("\nCliente registrado correctamente.\n")
    

def op4():

    global list_clientes
    global list_productos
    if len(list_productos) != 0:

        while True:

            numero = 0
            encontrado = False
            utilidades.imp("\tAGREGAR PRODUCTOS A CARRITO\n")
            buscar_nombre_client = utilidades.lea("Ingrese el nombre del cliente\n").upper()
            for cliente in list_clientes:

                if buscar_nombre_client == cliente.nombre:

                    encontrado = True
                    cant = utilidades.cicloIntento(f"\n¿Cuantos productos desea añadir al carrito de {buscar_nombre_client}?\n",
                                                    "Dato invalido, por favor ingrese solo números(enteros), intente nuevamente\n")

                    op2()
                    
                    for i in range(cant):
                            
                        while True:

                            num_product = utilidades.cicloIntento("Ingrese el número del producto que desea agregar al carrito\n",
                                                                "Dato invalido, por favor ingrese solo números(enteros), intente nuevamente\n")
                            
                            numero = num_product - 1
                            if numero < len(list_productos):

                                while True:

                                    cantidad = utilidades.cicloIntento(f"Ingrese la cantidad de '{list_productos[numero].nombre_producto}' que desea agregar al carrito\n",
                                                                    "Dato invalido, por favor ingrese solo números(enteros), intente nuevamente\n")

                                    exito = cliente.agg_carrito(list_productos[numero], cantidad)
                                    if  exito == True:

                                        utilidades.imp(f"\n{list_productos[numero].nombre_producto} agregado correctamente.\n")
                                        break

                                    elif exito == False:

                                        utilidades.imp("Intente nuevamente\n")

                                    elif exito == None:

                                        break

                                break

                            else:

                                utilidades.imp(f"el numero de producto {num_product} no se encuentra en el catalogo de productos, intente nuevamente\n")

                    break
                
            if encontrado == True:

                break

            else:

                utilidades.imp(f"el cliente {buscar_nombre_client} NO se encuentra en el regitro de clientes, por favor verifique el nombre e intente neuvamente")
    else:
        utilidades.imp("Aún NO hay productos registrados.")
        while True:

            op = utilidades.cicloIntento("¿Desea ir a registrar productos?\n1. SI\n2.NO\n\nDigite una opción\n",
                                "Dato invalido, por favor digite el precio en datos numericos")

            match op:

                case 1:

                    op1()
                    break

                case 2:

                    utilidades.imp("Saliendo...\n")
                    break

                case _:

                    utilidades.imp("opción invalida, por favor digite 1 ó 2")    

                
def op5():

    global list_clientes
    utilidades.imp("\tTOTAL CARRITO CLIENTES")
    if len(list_clientes) != 0:

        while True:

            encontrado = False
            buscar_nombre_client = utilidades.lea("Ingrese el nombre del cliente\n").upper()
            for cliente in list_clientes:
            
                if buscar_nombre_client == cliente.nombre:

                    encontrado = True
                    utilidades.imp(f"Cliente: {cliente.nombre}\nValor Total Carrito: {cliente.total_carrito()}\n")

            if encontrado == True:
            
                break
            
            else:
            
                utilidades.imp(f"el cliente {buscar_nombre_client} NO se encuentra en el regitro de clientes, por favor verifique el nombre e intente neuvamente")

    else:
        utilidades.imp("Aún NO hay clientes registrados.")
        while True:

            op = utilidades.cicloIntento("¿Desea ir a registrar clientes?\n1. SI\n2.NO\n\nDigite una opción\n",
                                "Dato invalido, por favor digite el precio en datos numericos")

            match op:

                case 1:

                    op3()
                    break

                case 2:

                    utilidades.imp("Saliendo...\n")
                    break

                case _:

                    utilidades.imp("opción invalida, por favor digite 1 ó 2")   





