#----------MENSAJES---------- 
PREGUNTA_PACIENTES = "ingrese numero de pacientes:" 
PREGUNTA_PACIENTES_UCI = "ingrese numero de pacientes uci:"
PREGUNTA_NOMBRE = "ingrese su nombre para continuar:"
MENSAJE_RIESGO_BAJO = "riesgo bajo" 
MENSAJE_RIESGO_MEDIO = "riesgo medio"   
MENSAJE_RIESGO_ALTO = "riesgo alto"
MENSAJE_BIENVENIDO = "hola que tal"
#----------VARIABLES----------
NOMBRE_PERSONAL = "Juanes"
#----------ENTRDAS----------
_nombreUsuario = ""
_numeroPacientes = 0 
_uciPacientes = 0
#----------CODIGO---------- 
print (MENSAJE_BIENVENIDO) 
_nombreUsuario  = input (PREGUNTA_NOMBRE) 
_numeroPacientes = int (input (PREGUNTA_PACIENTES)) 
if (_numeroPacientes > 0) and (_numeroPacientes < 1000) : 
    print (MENSAJE_RIESGO_BAJO)
elif (_numeroPacientes <= 5000) : 
    _uciPacientes = int (input (PREGUNTA_PACIENTES_UCI)) 
    if (_uciPacientes > 1000) : 
         print (MENSAJE_RIESGO_ALTO) 
    else:
        print (MENSAJE_RIESGO_MEDIO) 
else : 
    print (MENSAJE_RIESGO_ALTO)


