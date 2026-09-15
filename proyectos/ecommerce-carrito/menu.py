import utilidades
import opcionesMenu

while True:

    utilidades.imp("1. Registrar productos")
    utilidades.imp("2. Ver catalogo")
    utilidades.imp("3. Registrar clientes")
    utilidades.imp("4. Agregar producto al carrito de un cliente")
    utilidades.imp("5. Valor total carrito de un cliente")
    utilidades.imp("0. Salir")

    op = utilidades.cicloIntento("\nIngrese una opción\n", "Dato invalido, por favor intente nuevamente")

    match op:

        case 1:

            opcionesMenu.op1()

        case 2:

            opcionesMenu.op2()

        case 3:

            opcionesMenu.op3()

        case 4:

            opcionesMenu.op4()

        case 5:

            opcionesMenu.op5()

        case 0:

            utilidades.imp("Cerrando....\n")
            utilidades.imp("Cerrado.")
            break

        case _:
            
            utilidades.imp("Por favor ingrese una opción que este en el menú.\n")