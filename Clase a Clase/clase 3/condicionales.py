#-------------Mensajes---------------#
PREGUNTA_NOMBRE= "ingrese su nombre : "
PREGUNTA_EDAD = "ingresa por tu madre tu edad : "
MENSAJE_BIENVENIDO= "Bienvenido"
MENSAJE_DESPEDIDA=  "¡Adios!" 
MENSAJE_TOCAYO = "OE hermano somos tocayos"
MENSAJE_JOVEN = "Eres Joven"
MENSAJE_ADULTO = "Eres Adulto" 
MENSAJE_ADULTO_MAYOR = "se esta poniendo viejo, cuentese las arrugas y no se haga el pendejo"
#---------------VARIABLES--------------
NOMBRE_PERSONAL = "Juan"
#---------------ENTRADAS---------------
_nombreUsuario = "" 
_edadUsuario = 0
#---------------CODIGO---------------
print (MENSAJE_BIENVENIDO)
_nombreUsuario = input (PREGUNTA_NOMBRE)
if (NOMBRE_PERSONAL == _nombreUsuario) :
    print (MENSAJE_TOCAYO)
 
_edadUsuario = int(input(PREGUNTA_EDAD))

if ((_edadUsuario >= 0) and (_edadUsuario <= 25)) : 
    print (MENSAJE_JOVEN)
elif ((_edadUsuario >= 26) and (_edadUsuario  <= 65)) :
    print (MENSAJE_ADULTO)
else : 
    print (MENSAJE_ADULTO_MAYOR) 
print (MENSAJE_DESPEDIDA)

