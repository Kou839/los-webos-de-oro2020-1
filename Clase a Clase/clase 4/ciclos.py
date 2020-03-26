# numero = 0
# NUMERO_DESEADO = 12
# while (numero < NUMERO_DESEADO) : 
#     numero = numero + 1
#     print (numero)
# print (numero) 
import random
PREGUNTA_NUMERO = """
 Ingrese un numero
 entero 
 entre el 1-10
 : """
MENSAJE_FALLO = "¡¡TE VAS A MORIR PEROO!!"
MENSAJE_ACIERTO = "FELICIDADES, SABES MI NUMERO FAVORITO :V"  
MENSAJE_MAYOR = "ESTAS CERCA EL NUMERO QUE INGRESÓ ES MÁS GRANDE" 
MENSAJE_MENOR = "ESTAS CERCA EL NUMERO QUE INGRESÓ ES MÁS PEQUEÑO" 

NUMERO_FAVORITO = random.randint(1,10) 
_numeroIgresado = int (input (PREGUNTA_NUMERO)) 
while (_numeroIgresado != NUMERO_FAVORITO) :
    print (MENSAJE_FALLO) 
    if (_numeroIgresado > NUMERO_FAVORITO) : print (MENSAJE_MAYOR) 
    else : print (MENSAJE_MENOR)
    _numeroIgresado = int (input (PREGUNTA_NUMERO))
print (MENSAJE_ACIERTO)


