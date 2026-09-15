import utilidades

class Producto():

    def __init__(self, nombre_producto, precio_base, stock):

        self.nombre_producto = nombre_producto
        self.precio_base = precio_base
        self._stock = stock

    def aplicar_descuento(self):

        return self.precio_base



    def reducir_stock(self, cantidad):

        if cantidad <= self._stock:

            self._stock -= cantidad
            utilidades.imp(f"Venta valida, quedan {self._stock} unidades de {self.nombre_producto} en la bodega")
            exito = True   

        else:

            utilidades.imp(f"Solo hay {self._stock} unidades de {self.nombre_producto} en bodega,por lo que no se pueden vender {cantidad} unidades")
            exito = False
            
        return exito


    
class Produc_ropa(Producto):

    def __init__(self, nombre_producto, precio_base, stock, talla):

        super().__init__(nombre_producto, precio_base, stock)
        self.talla = talla


    def aplicar_descuento(self):

        if self._stock > 50:

            descuento = 1 - 0.2
            precio = self.precio_base * descuento

        else:

            precio = self.precio_base

        return precio

    

class Produc_electronico(Producto):

    def __init__(self, nombre_producto, precio_base, stock, meses_garantia):

        super().__init__(nombre_producto, precio_base, stock)
        self.meses_garantia = meses_garantia


    def aplicar_descuento(self):

        descuento = 1- 0.1
        return self.precio_base * descuento