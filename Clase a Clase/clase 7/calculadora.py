#------------suma------------
def sumar(x,y) : 
    suma= x+y 
    return suma 
 

#-----------resta------------
def restar(x,y) : 
    resta= x-y
    return resta 
 

#-----------muliplicacion---------
def multiplicar(x,y) : 
    multiplicacion= x*y
    return multiplicacion


#-----------division--------------
def dividir(x,y) : 
    division = 0
    if y == 0 : 
        division = "operacion no valida" 
    else :
        division = x/y
    return division
