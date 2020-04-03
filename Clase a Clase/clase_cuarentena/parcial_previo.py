class canguro():
    def __init__(self,id,peso,altura,genero):
        self.animal = "canguro"
        self.id= id
        self.peso = peso
        self.altura = altura
        self.genero = genero        
    def numeroSaltos(self,saltos):
        for i in range(saltos):
            print ("salto", i+1)



animal1 = canguro ("007",56 , 1.6, "hembra")


print("la id del canguro es: ", animal1.id)
print("el peso del canguro es: ", animal1.peso)
print("la altura del canguro es: ", animal1.altura)
print("el genero del canguro es: ", animal1.genero)
print("el numero de saltos del canguro es: ", animal1.numeroSaltos(14))




class cuidador(): 
    def __init__(self,id,nombre):
        self.id = id
        self.nombre = nombre 
    def alimentarCanguros(self, cangurosAlimentados):
        for i in range(cangurosAlimentados):
            print ("alimento", i+1 ) 

cuidador1 = cuidador("001","Royer")


print("la id del cuidador es: ", cuidador1.id) 
print("el nombre del cuidador es: ", cuidador1.nombre)
print("la cantidad de canguros alimentados es: ",cuidador1.alimentarCanguros(27))

class jefe(): 
    def __init__(self,nombre): 
        self.nombre = nombre
    def contratarCuidador(self,id,nombre):
        print("voy a contratar un cuidador")
        contratar = cuidador(id,nombre)
        return contratar 


jefe1 = jefe("Razor") 
jefe1.contratarCuidador("016", "Miya")

print("Mi nombre es", jefe1.nombre,"y hoy voy a contratar a :", jefe1.contratarCuidador("016", "Miya"), "por favor llevense bien con ella")
    

