def cicloIntento(mensaje, impErr):

    while True:

        try:

            valor = int(input(mensaje))
            return valor
        
        except ValueError:

            print(impErr)


def imp(mensaje):

    print(mensaje)


def lea(mensaje):

    mens = input(mensaje)
    return mens


def cicloIntentoFloat(mensaje, impErr):

    while True:

        try:

            valor = float(input(mensaje))
            return valor
        
        except ValueError:

            print(impErr)
    



