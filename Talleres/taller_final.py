import sys
import matplotlib.pyplot as plt 
import pandas as p 
#------------PUNTO_1-------------------
def validador_archivo (file):
    assert(file) 
    return False
validador= True

while (validador):
    file= input('ingrese nombre del archivo: ')
    try:
        validador= open(file)
        validador= False
    except FileNotFoundError: 
        print("el nombre del archivo que ingresaste no existe") 


ecg = p.read_csv(file,encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(ecg["muestra"].values())
y = list(ecg["valor"].values())
plt.title(input("ingrese el titulo de la grafica : "))
plt.xlabel(input("¿que nombre desea ingresar en el eje x? : "))
plt.ylabel(input("¿que nombre desea ingresar en el eje y? : "))
plt.plot(x,y)
plt.savefig(input("ingrese el nombre de como desea guardar la grafica : "))
plt.show()

#----------------Punto_2----------------------
nombre = "No has ingresado tu nombre"
try:
    nombre = (input('Ingrese su nombre : '))
except ValueError:
    print ("estas ingresando mal el nombre, usa los caracteres adecudos")
print ("Hola", nombre)

edad = "No ingresaste edad"
try:
    edad = int (input('Ingrese su edad : '))
except ValueError:
    print ("ingresaste mal la edad, use solo numeros en este apartado")
print ("Su edad es", edad)

estatura = "No has ingresado tu estatura"
try:
    estatura = float (input('Ingrese su estatura : '))
except ValueError:
    print ("no usaste los caracteres adecuatos")
print ("Tu estatura es", estatura)

peso = "No ingresaste tu peso"
try:
    peso = float (input('Ingrese su peso : '))
except ValueError:
    print ("ingresaste mal el peso")
print ("Tu peso es", peso)

IMC = ((peso/estatura**2))
print ("Tu IMC es de  : ",IMC) 

#-----------------Punto_3-------------
kilogramos_de_arroz= "ingresaste incorrectamente los kilogramos de arroz"
try:
    kilogramos_de_arroz = float (input('Ingrese los kilogramos de arroz : '))
except ValueError:
    print ("ingresaste incorrectamente los kilogramos de arroz")
print ("los kilogramos de arroz que tienes son: ", kilogramos_de_arroz)

kilogramos_de_lentejas = "ingresaste incorrectamente los kilogramos  de lentejas"
try:
    kilogramos_de_lentejas = float (input('Ingrese los kilogramos de lentejas : '))
except ValueError:
    print ("ingresaste incorrectamente los kilogramos  de lentejas")
print ("los kilogramos de lentejas que tienes son: ", kilogramos_de_lentejas)

kilogramos_de_frijoles = "ingresaste incorrectamente los kilogramos de frijoles"
try:
    kilogramos_frijoles = float (input('Ingrese los kilogramos de frijoles : '))
except ValueError:
    print ("ingresaste incorrectamente los kilogramos de frijoles")
print ("lod kilogramos de frijoles que tienes son: ", kilogramos_de_frijoles)

kilos_de_papa = "ingresaste incorrectamente los kilogramos de papa"
try:
    kilogramos_de_papa = float (input('Ingrese los kilogramos de papa : '))
except ValueError:
    print ("ingresaste incorrectamente los kilogramos de papa")
print ("los kilogramos de papa que tienes son: ", kilogramos_de_papa)

mercado = {
    "articulos" : ["Arroz", "Lentejas", "Frijoles", "Papa"]
}
kilogramos = (kilogramos_de_arroz, kilogramos_de_lentejas, kilogramos_de_frijoles, kilogramos_de_papa)


print (mercado["articulos"])
print (kilogramos)

plt.bar (mercado["articulos"], kilogramos)
plt.title("articulos vs Kilogramos", fontsize=25)
plt.xlabel("(articultos)")
plt.ylabel("(kilogramos)")
plt.savefig("articulososVskilogramos.png")
plt.show ()

#-------------------Punto_4-----------------------
def validador_opinion (opinion):
    assert(opinion.endswith("."))
    return False
validador = True

while (validador):
    opinion =  input('Cual es su opinión frente a esta cuarentena: ')
    try:
        validador = validador_opinion (opinion)
    except AssertionError:
        print("La entrada no es válida")

#-------------------Punto_5--------------------
labels = 'Leche', 'Huevos', 'Vino','Arroz','Queso','Salchichas'
sizes = [12, 8, 4, 26, 30, 20]
explode = (0, 0, 0, 0, 0.2, 0)
plt.pie(sizes, explode=explode, labels=labels, shadow=True, startangle=0)
plt.title("% DE COMPRAS")
plt.savefig("Grafica_de_compras.png")
plt.show()