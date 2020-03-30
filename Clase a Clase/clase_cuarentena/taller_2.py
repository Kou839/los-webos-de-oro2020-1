listaDoctores = ["diego", "dayana", "oscar", "diana", "rigu"]
size_list_doctores = len (listaDoctores)

listaEnfermeros = ["lou", "franchesco", "valeria", "katherin", "mencho"] 
size_list_enfermeros = len (listaEnfermeros)

listaPacientes = ["kou", "scarlet", "tyty", "roulet",]
size_list_pacientes = len (listaPacientes) 

listaEstado = ["estable", "UCI", "grave", "en observacion",]
size_list_Estado = len (listaEstado) 

def mostrar_lista(listaPacientes):
    for i in range(size_list_pacientes):
        print(i)
        print(listaPacientes[i])

decision = int(input("""
    ingrese:
    1- para ver la lista de doctores y enfermer@s
    2- para agregar personas a una lista
    3- para ver a los pacientes y su estado
    4- para finalizar 
"""))

while(decision != 4):
    if (decision == 1):
        def mostrar_dos_listas(listaDoctores, listaEnfermeros): 
            if ( size_list_doctores == size_list_enfermeros):
                print (listaDoctores, listaEnfermeros)
            contador =1  
            for i in range (size_list_doctores):
                print (i)
                print(contador ,"-",listaDoctores[i], listaEnfermeros[i])
                contador += 1
        mostrar_dos_listas (listaDoctores, listaEnfermeros)        
    
    elif(decision == 2):
        def llenarLista(): 
            lista=[]
            decision= input ("""
                ingrese:
                a- para agregar personas
                n- para no agregar a nadie mas
            """)
            while(decision == "s"):
                lista.append(input("ingrese un usuario: "))
                decision= input ("""
                ingrese:
                a- para agregar personas
                n- para no agregar a nadie mas
            """)
            return lista
        print ("ingrese a los doctores: ")
        listaDoctores = llenarLista()
        print ("ingrese a l@s enfermer@s: ")
        listaEnfermeros = llenarLista()
        print ("ingrese a los pacientes: ")
        listaPacientes = llenarLista() 

        mostrar_dos_listas (listaDoctores, listaEnfermeros)
        mostrar_lista (listaPacientes)

    elif(decision == 3):
        def mostrar_dos_listas (listaPacientes, listaEstado):
            if (size_list_pacientes == size_list_Estado):
                print("pacientes", "-", "estado")
                for i in range(size_list_pacientes): 
                    print(listaPacientes[i], listaEstado[i])
        mostrar_dos_listas(listaPacientes, listaEstado)

    else: 
        print ("ingrese un valor deltro de las opciones expuestas anteriormente ")

    decision = int(input("""
    ingrese:
    1- para ver la lista de doctores y enfermer@s
    2- para agregar personas a una lista
    3- para ver a los pacientes y su estado
    4- para finalizar 
"""))

print("#"* 40) 

print ("gracias por utilizar este programa")
    

    

