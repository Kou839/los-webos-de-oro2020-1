def marco ():
    print ("#"*30) 
def saludar (nombre) : 
    print("bienvenido", nombre, "a este codigo") 

#------------suma------------
def sumar(x,y) : 
    suma= x+y 
    return suma 
print (sumar (2,4)) 

#-----------resta------------
def restar(x,y) : 
    resta= x-y
    return resta 
print (restar (3,7)) 

#-----------muliplicacion---------
def multipicar(x,y) : 
    multiplicacion= x*y
    return multiplicacion
print (multipicar (9,3))

#-----------division--------------
def dividir(x,y) : 
    division = 0
    if y == 0 : 
        division = "operacion no valida" 
    else :
        division = x/y
    return division
print (dividir (40,2))

marco() 
saludar ("Juanes")
saludar (input("ingrese su nombre :")) 
resultado = sumar (2,4) 
resultado_1 = restar (3,7) 
resultado_2 = multipicar (9,3)
resultado_3 = dividir (40,2)
print (resultado)