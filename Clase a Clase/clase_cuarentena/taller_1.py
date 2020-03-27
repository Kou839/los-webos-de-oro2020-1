#--------MENSAJES------
MENSAJE_BIENVENIDO = "hola , Bienvenido"
PREGUNTA_EDAD = "ingrese su edad: "
PREGUNTA_LISTA_DE_COMPRAS = "deseas adquirir articulos ? s ->si n ->no "
#--------CODIGO--------
listaCompras = "esta será tu lista de compras producto a producto"

eliminarProducto = "do u like to delete  un producto de la lista ? cual ? s ->si n->no"

PREGUNTA_NUMERO = "ingresa el number de products que quieras eliminar"
#---------------------------------
print(MENSAJE_BIENVENIDO)

_desicion = int (input("""
    ingrese :
    1-edad
    2-lista de productos de compra
    3-lista de compras producto a producto
    4-eliminar un producto de la lista de compras
    5-salir
"""))

while (_desicion != 5):
    if(_desicion ==1):
        _edadUsuario = int(input(PREGUNTA_EDAD))
        if  ((_edadUsuario >= 0) and (_edadUsuario <= 17)) :
            print("acceso denegado")
        elif((_edadUsuario >= 18) and (_edadUsuario <= 29)):
             print("acceso permitido")
        elif (_edadUsuario >=30) and (_edadUsuario <=59):
            print("¡felicidades1, obtienes un descuento del 30%")
        else:
            print("obtienes un descuento acorde a tu edad")
    elif (_desicion ==2) :
        productos = []
        _listaCompras = input(PREGUNTA_LISTA_DE_COMPRAS)
        while (_listaCompras =="s") :
            productos.append (input("ingrese: "))
            _listaCompras = input (PREGUNTA_LISTA_DE_COMPRAS)
        print (productos)


    else:
        print("ingrese un valor que sea valido")
    _desicion = int (input("""
      ingrese :
      1-edad
      2-lista de productos to buy
      3-lista de compras producto a producto
      4-eliminar un producto de la lista de compras
      5-salir
"""))
print("gracias por usar este programa, feliz día.")