#-----------LIBRERIAS-------------
import sys 
import matplotlib.pyplot as plt 
import pandas as p 

#-----------MENSAJE---------------
MENSAJE_PUNTO_5= """
    Es mucha, y se ve reflejada en las distintas inquietudes que se 
    dan a lo largo de los videos de la clase. si, se puede retrasar el video unos minutos, 
    pero realmente no es lo mismo si le puedo preuntar al profesor directamente en una
    clase supervisada(presencial).
    Ese sería el unico problema y principal diferencia con el no supervisado. 
    """

#-----------PUNTO1----------------
def validador_archivo (file):
    assert(file)
    return False
validador= True

while (validador): 
    file= input('Ingrese el nombre del archivo: ')
    try:
        validador= open(file)
        validador= False
    except FileNotFoundError: 
        print("El nombre del archivo que ingresaste no existe")

ppg= p.read_csv(file, encoding='UTF-8', header=0, delimiter=";").to_dict()
x= list(ppg["muestra"].values())
y= list(ppg["valor"].values())
plt.title(input("Ingrese el titulo de la gráfica: "))
plt.xlabel(input("¿que nombre desea ingresar en el eje x?: "))
plt.ylabel(input("¿que nombre desea ingresar en el eje y?: "))
plt.plot(x,y)
plt.savefig(input("Ingrese el nombre de como desea guardar la gráfica: "))
plt.show()

#--------------PUNTO2-------------------
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

#----------------PUNTO3---------------
ppg= p.read_csv(file, encoding='UTF-8', header=0, delimiter=";").to_dict()
x= list(ppg["muestra"].values())
y = list(ppg["valor"].values())
plt.title("PPG-uV")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("mi_ppg.png")
plt.close()

ecg= p.read_csv(file, encoding='UTF-8', header=0, delimiter=";").to_dict()
x= list(ecg["muestra"].values())
y = list(ecg["valor"].values())
plt.title("ECG-uV")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("mi_ecg.png")
plt.close()

eeg= p.read_csv(file, encoding='UTF-8', header=0, delimiter=";").to_dict()
x= list(eeg["muestra"].values())
y = list(eeg["valor"].values())
plt.title("EEG-uV")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("mi_eeg.png")
plt.close()

#----------------PUNTO4---------------
labels = 'sala', 'habitación', 'baño','cocina'
sizes = [30, 60, 5, 10]
explode = (0, 0,1, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, shadow=True, startangle=0)
plt.title("% DE SITIOS")
plt.savefig("Grafica_de_sitios.png")
plt.show()

#--------------PUNTO5----------
_enmisPalabras= input(MENSAJE_PUNTO_5)
print(_enmisPalabras)