import random
import random
#--------------mensajes---------------
MENSAJE_DADO = """
 ingrese la suma de 
 los dados
  :""" 
NUMERO_DESEADO = 12 
#--------------variables-------------
dado1 = random.randint (1,6)
dado2 = random.randint (1,6)
SUMA = (dado1 + dado2)
#--------------codigo--------------------
while ( SUMA != NUMERO_DESEADO ) :
  print (SUMA)
  dado1 = random.randint (1,6)
  dado2 = random.randint (1,6) 
  suma =   (dado1 + dado2)  
print (SUMA)
 
