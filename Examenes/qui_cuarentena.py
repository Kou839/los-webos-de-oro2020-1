#--------------Mensajes----------- 
MENSAJE_BIENVENIDO= "bienvenido al programa" 


#--------------Codigo-------------

print (MENSAJE_BIENVENIDO) 

pesosPacientesIniciales = [32,64,74,85,98,115,122,127,137,148]  



def mostrar_lista (pesosPacientesIniciales):
    if (len(pesosPacientesIniciales)):
        for i in range(len(pesosPacientesIniciales)): 
            print (pesosPacientesIniciales[i])



mostrar_lista(pesosPacientesIniciales)

presiones= []
for peso in pesosPacientesIniciales: 
    presiones.append(peso*6)

def llenarLista (): 
    pesoPaciente = []
    decision = int(input(""" Ingrese: 
          1 - para añadir peso del paciente
          2 - finalizar
          """))
    while(decision != "2"):
        if (decision == "1"):
          pesoPaciente.append (input("ingrese el peso nuevo: "))
        else: 
            print ("ingrese un valor valido")
        
        decision = int(input("""
        Ingrese: 
          1 - para añadir peso
          2 - finalizar
          """))
    return pesoPaciente
llenarLista() 

print ("la presion más alta en la lista {} es {}"
.format (pesosPacientesIniciales, max(pesosPacientesIniciales))) 

print ("la presion más baja en la lista {} es {}" 
.format (pesosPacientesIniciales, min(pesosPacientesIniciales)))

pesosPacientesIniciales.sort(reverse=True)
print ("lista ordenada de forma decreciente {}".format(pesosPacientesIniciales)) 

print ("gracias por usar este prgrama")






