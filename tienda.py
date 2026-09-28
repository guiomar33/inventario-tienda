class inventariotienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.listproductos = []

    def agregar_producto(self, nombre, precio, cantidad):
        producto = {
            "nombre" : nombre,
            "precio" : precio,
            "cantidad" : cantidad
        }
        self.listproductos.append(producto)

    def vender_producto(self, nombre, cantidad):
        encontrado = False
        for producto in self.listproductos:
            if producto ["nombre"] == nombre:
                encontrado = True
                if producto ["cantidad"] >= cantidad:
                    producto ["cantidad"] -= cantidad
                    print("producto vendido")
                else:
                    print("no hay suficiente producto")
        if not encontrado:
            print("producto no existente")
            

    def mostrar_inventario(self):
        for producto in self.listproductos:
            print(producto ["nombre"], producto["precio"], producto["cantidad"])

    def producto_mas_caro(self):
        mas_caro = None
        for producto in self.listproductos:
            if mas_caro is None or producto["precio"] > mas_caro["precio"]:
                mas_caro = producto
        if mas_caro is None:
            print("no hay productos en el inventario")
            return None
        return mas_caro["nombre"], mas_caro["precio"]

tienda = inventariotienda("my tienda")
while True:
    print("1. agregar productos")
    print("2. vender producto")
    print("3. mostrar inventario")
    print("4. mostrar producto mas caro")
    print("5. salir")
    opcion = input("elige una opcion: ")

    if opcion == "1":
        nombre = input("nombre del producto ")
        precio = float(input("precio del producto "))
        while precio <= 0:
            precio = float(input("el precio debe de ser positivo "))
        cantidad = int(input("cantidad del producto "))
        while cantidad <= 0:
            cantidad = int(input("la cantidad debe de ser positiva"))
        tienda.agregar_producto(nombre, precio, cantidad)
    elif opcion == "2":
        nombre = input("nombre del producto ")
        cantidad = int(input("cantidad a vender "))
        while cantidad <=0:
            cantidad =int(input("la cantidad debe de ser positiva "))
        tienda.vender_producto(nombre, cantidad)
    elif opcion == "3":
        tienda.mostrar_inventario()
    elif opcion == "4":
        resultado = tienda.producto_mas_caro()
        if resultado is not None:
            nombre, precio = resultado
            print("producto mas caro", nombre, "precio", precio)
    elif opcion == "5":
        print("saliendo")
        break


