
#-------------Mensajes---------------#
PREGUNTA_NOMBRE= "ingrese su nombre : "
MENSAJE_EDAD= "ingrese su edad" 
MENSAJE_ESTATURA= "ingrese su estartura"
MENSAJE_BIENVENIDO= "Bienvenido"
MENSAJE_DESPEDIDA=  "¡Adios!"
#-------------------------------------

_nombrePersona = input(PREGUNTA_NOMBRE) 
print (MENSAJE_BIENVENIDO,_nombrePersona, "a este programa")
_edadPersona =int (input(MENSAJE_EDAD)) 
print ("tu edad es",_edadPersona,)
print (type(_edadPersona))
_estauraPersona =float (input(MENSAJE_ESTATURA)) 
print ("tu estatura es",_estauraPersona,)
print (type(_estauraPersona)) 
print (MENSAJE_DESPEDIDA) 

