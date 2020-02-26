#--------------Mensajes--------------
MENSAJE_BIENVENIDO = "Bienvenido"
MENSAJE_DESPEDIDA =  "Muchas gracias, adios"
MENSAJE_BAJO_PESO = "estas por debajo de lo normal"
MENSAJE_PESO_NORMAL = "su estado es estable"
MENSAJE_SOBREPERO = "tienes sobrepeso"
MENSAJE_OBESIDAD_GRADO_III = "¡masa cirtica!"
MENSAJE_TOCAYO = "hey, tenemos el mismo nombre" 
PREGUNTA_NOMBRE = "ingrese nu nombre:"
PREGUNTA_ESTAURA =  "ingrese su estatura:"
PREGUNTA_PESO = "ingrese su peso:"
PREGUNTA_EDAD = "ingrese su edad:"
#--------------Variables--------------
NOMBRE_PERSONAL = "Juanes"
IMC = 0.0
#--------------Entradas--------------
_nombreUsuario = ""
_edadUsuario = 0
_pesoUsuario = 0.0
_estaturaUsuario = 0.0
#--------------Codigos--------------
print (MENSAJE_BIENVENIDO)
_nombreUsuario = input (PREGUNTA_NOMBRE)
_edadUsuario = int (input (PREGUNTA_EDAD))
_pesoUsuario = float (input (PREGUNTA_PESO))
_estaturaUsuario = float (input (PREGUNTA_ESTAURA))
IMC = (_pesoUsuario / _estaturaUsuario ** 2)
print (IMC)

if (IMC >= 12) and (IMC <= 18) :
    print (MENSAJE_BAJO_PESO) 

if (NOMBRE_PERSONAL == _nombreUsuario) :
    print (MENSAJE_TOCAYO)

elif (IMC >= 19) and (IMC <= 24) : 
    print (MENSAJE_PESO_NORMAL)

elif (IMC >= 25) and (IMC <= 39) : 
    print (MENSAJE_SOBREPERO)

else : 
    print (MENSAJE_OBESIDAD_GRADO_III) 
print (MENSAJE_DESPEDIDA)
