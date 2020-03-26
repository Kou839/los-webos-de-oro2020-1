#-------------Mensajes------------
MENSAJE_BIENVENIDO = "Bienvenido al programa" 

#------------Codigo-------------- 

print (MENSAJE_BIENVENIDO) 

listaIniciales = [1,2,4,8,16,32,64]

def mostrar_lista (listaIniciales): 
    if (len(listaIniciales)):
        for i in range(len(listaIniciales)): 
            print (listaIniciales[i])


def llenarlista (): 
    listaIngresados =[] 
    decision = input ("""
    ingrese: 
         i - para agregar edad nueva
         n - para salir
         """) 
    while(decision == "i"):
        listaIngresados.append (input("ingrese la edad del paciente: "))
        decision = input ("""
    ingrese: 
         i - para agregar edad nueva
         n - para salir 
        """)
        return listaIngresados
print ("desea ingresar la edad de los pacientes: ")

edades= llenarlista ()

mostrar_lista(edades) 



promedio = (((1+2+4+8+16+32+64)/7)) 
print ("promedio de edades: ") 
print (promedio) 

mostrar_lista(edades)

lista_iniciales = [1,2,4,8,16,32,64]
lista_adicionar = [edades]
lista_adicionar.extend (lista_iniciales)
print (lista_adicionar)

print ("el más longevo en la lista de nuevos {} es {} "
.format(edades, max (edades)))
print ("el más longevo en la lista de nuevos {} es {} "
.format(lista_iniciales, max(lista_iniciales)))

print ("el más longevo en la lista de nuevos {} es {} "
.format(edades, min (edades)))
print ("el más longevo en la lista de nuevos {} es {} "
.format(lista_iniciales, min (lista_iniciales)))

edades.sort()
print ("lista nuevos ordenada crecientemente {}".format(edades))
lista_iniciales.sort()
print ("lista iniciales ordenada crecientemente {}".format(lista_iniciales))

edades.sort(reverse= true)
print ("lista nuevos ordenada decrecientemente {}".format(edades))
lista_iniciales.sort(reverse= true)
print ("lista iniciales ordenada decrecientemente {}".format(lista_iniciales)) 

print (lista_iniciales)
lista_iniciales.insert (4, 87) 
print ("se insertó la edad 87 años en la cuarta posición")
print (lista_iniciales)

valor_eliminado= lista_iniciales.pop(6)
print(lista_iniciales, "El numero quee eliminó fue {} de la posición 6 de la lista {}"
.format(valor_eliminado)) 



