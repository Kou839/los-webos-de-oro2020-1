listaNombres = ["santigo",
                "juanes", 
                "marco", 
                "elena", 
                "mch betancur", 
                "mch mesa", 
                "leslly", 
                "ysabella", 
                "santiago el humlde",
                "daniel", 
                "david",
                "mafer",
                "susi",
                "daniel h"]
listaNombres [4] = "Maria Camila Betancur"
listaNombres [5] = "Maria Camila Mesa" 
print (listaNombres )
listaNombres.pop (-1) 
print (listaNombres)  
listaNombres.append ("Daniel Herrera") 
print (listaNombres) 

listaEdades= [20,
              17,
              19,
              20,
              19, 
              19, 
              18, 
              20, 
              21, 
              22, 
              26, 
              21, 
              23, 
              30 ]

_desision = int (input ("""
        ingrese :
        1- para ver lista de Nombres
        2- para ver edades
        3- para ver notas
        4-salir
""")) 
while (_desision != 4) :
    if (_desision == 1) : 
        print (listaNombres)
    elif (_desision == 2) : 
        print ("aquí van las edades")
    elif (_desision  == 3) : 
        print ("aquí van las notas")
    else : 
        print("ingrese un valor valido")

    _desision = int (input ("""
        ingrese :
        1- para ver lista de Nombres
        2- para ver edades
        3- para ver notas
        4-salir
"""))  
print ("hracias por usar esste programa")
 


# tupla "no se puede editar":
#  tupla =()




#Tarea= hacer la lista de nombres



# Lista_mercado = (huevos, leche, pan, carne) 
# print (Lista_mercado (0))
# Lista_mercado (0) = "salchichas" 