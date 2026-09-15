import producto
import utilidades

class Cliente():

    def __init__(self, nombre):

        self.nombre = nombre
        self.carrito = []

    def agg_carrito(self, product, cantidad):

        if isinstance(product, producto.Producto):

            if product.reducir_stock(cantidad) == True:

                producto_carrito = {
                    "producto": product,
                    "cantidad": cantidad
                }
                for item in self.carrito:

                    if item["producto"] == product:

                        item["cantidad"] += cantidad
                        return True
                    
                self.carrito.append(producto_carrito)
                exito = True
                return exito

            else:

                utilidades.imp(f"No se pudo agregar {cantidad} unidades de {product.nombre_producto} al carrito de {self.nombre}")
                exito = False
                return exito
        else:

            utilidades.imp("el producto NO es valido")
        

    def total_carrito(self):

        total = 0
        for item in self.carrito:

            total += item["producto"].aplicar_descuento() * item["cantidad"]  
             
        return total


            

        