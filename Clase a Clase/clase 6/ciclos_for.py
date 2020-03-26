# _cantidadsaltos = int (input("ingrese la cantidad de saltos : ")) 
# for i in range (4):
#     print(i) 

# for i in range (_cantidadsaltos): 
#     print ("el canguro da su salto numero", i+1) 

# #elementos 
# DIAS = ["lunes", "martes", "miercoles", "jueves", "viernes" ]
# for dia in DIAS: 
#    print (dia)

#---------------posicion +18------------------ 
NOMBRES = ["ARLEY", "CHAVO", "KOU", "LUCAS", "TOBEY", "LAILA"]
EDADES = [12, 21, 16, 17, 28, 16]
print (len(NOMBRES), len(EDADES))
for i in range (len(NOMBRES)):
    if EDADES[i] >= 18 : 
     print (i, "LA PERSONA", NOMBRES[i], "ES MAYOR")

#---------------suma_edades-------------------
sumaEdades = 0 
for edad in EDADES : 
     sumaEdades += edad 
print (sumaEdades)
