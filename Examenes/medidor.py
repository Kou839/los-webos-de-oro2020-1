#----------MENSAJES----------
MENSAJE_BIENVENIDO = "bienvenido a este programa" 
MENSAJE_OBSERVACIÓN = "estado en observación" 
MENSAJE_SALUDABLE = "estado saludable"
MENSAJE_HIPOTERMIA = "estado hipotermia" 
MENSAJE_ALERTA = "estado alerta"
MENSAJE_PELIGRO = "¡estado peligro!"
PREGUNTA_NOMBRE = "ingrese su nombre para continuar:"
PREGUNTA_NACIONLIDAD = "ingrese su pais de procedeniencia:"
PREGUNTA_TEMPERATURA = "ingrese su temperatura:"
#----------VARIABLES----------
temperatura = 0.0
#----------ENTRADAS-----------
_nombrePaciente = ""
_nacionalidadPaciente = ""
_temperaturaPaciente = 0.0
#----------CODIGOS---------- 
print (MENSAJE_BIENVENIDO) 
_nombrePaciente = input (PREGUNTA_NOMBRE)
_nacionalidadPaciente = input (PREGUNTA_NACIONLIDAD) 
_temperaturaPaciente = float (input (PREGUNTA_TEMPERATURA)) 
if (_nacionalidadPaciente == "china" or "iran" or "italia") :
    print (MENSAJE_OBSERVACIÓN)

elif (_temperaturaPaciente >= 36.00) and (_temperaturaPaciente <=38.40) :
    print (MENSAJE_SALUDABLE)
elif (_temperaturaPaciente < 36.00) : 
    print (MENSAJE_HIPOTERMIA)
elif (_temperaturaPaciente == 38.50) and (_temperaturaPaciente <= 40) : 
    print (MENSAJE_ALERTA) 
else : 
    print (MENSAJE_PELIGRO)