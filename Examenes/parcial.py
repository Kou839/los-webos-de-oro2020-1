############Mensaje############
mensaje_menu = """
    1- mostrar los atributos de los estudiantes
    2- mostrar los atributos de los profesores
    3- mostrar los atributos del director
    4- salir
"""

#estudiantes:
#           atributos: nombre, edad, genero, colegio
#           funcion: asistir(clases_asistidad)


class Estudiante(): 
    def __init__(self,nombre_ingresado,edad_ingresada,genero_ingresado,colegio_graduado):
        self.humano= "estudiante"
        self.nombre= nombre_ingresado
        self.edad= edad_ingresada
        self.genero= genero_ingresado
        self.colegio= colegio_graduado 
    def asistir(self,clases_asistidas):
        for i in range (clases_asistidas):
            print("""
            hola soy un estudiante, mi nombre es {} tengo una edad de {} soy {} y me gradue del colegio {} y asisti a la clase numero {}"""
            .format(self.nombre,self.edad,self.genero,self.colegio,i+1)) 

#profesor: 
#         atributos: nombre, edad, nivel educativo
#         funcion: dictarClase(clases_dictadas)
#         --> entradas: clases_dictadas= cantidad de clases dictadas
#         --> salidas: none

class Profesor():
    def __init__(self,nombre_ingresado,edad_ingresada,nivel_educativo_ingresado): 
        self.humano = "profesor"
        self.nombre = nombre_ingresado
        self.edad = edad_ingresada
        self.nivelEducativo = nivel_educativo_ingresado
    def dictarClase(self,clases_dictadas):
        for i in range(clases_dictadas):
            print("""
            hola, soy un profesor. mi nombre es {} tengo {} mi nivel educativo  es {}. he dictado {} clases y estoy cansado
            """.format(self.nombre,self.edad,self.nivelEducativo, i+1)) 

#director: 
#         atributos: nombre, edad, nivel educativo
#         funcion: contratar(profesores_contratadps)
#         --> entradas: profesores_contratados= cantidad de profesores contratados
#         --> salidas: none 

class Director(Profesor):
    def contratar (self,nombre,edad_ingresada,nivel_educativo): 
        profesorContratado= Profesor(nombre,edad_ingresada,nivel_educativo)
        return(profesorContratado) 


estudiante1 = Estudiante("Yui", 17, "femenino", "IEALP")
estudiante1.asistir(4)

estudiante2 = Estudiante("Marco", 20, "masculino", "colegio x")
estudiante2.asistir(3)

estudiante3 = Estudiante("santiago", 21, "masculino", "colegio y")
estudiante3.asistir(4)

estudiante4 = Estudiante("Covid", 19, "RNA", "wuhan school")
estudiante4.asistir(2)

estudiante5 = Estudiante("lina", 17, "femenino", "licedo")
estudiante5.asistir(4)

profesor1 = Profesor("Ernesto", 37, "doctorado")
profesor1.dictarClase(7)


profesor2 = Profesor("Yuko", 36, "doctorado")
profesor2.dictarClase(6)

director= Director("Diego", 38, "doctorado")
director.contratar("Diana", 31, "posgrado")
director.contratar("Yeison", 25, "prerado")






def main():
    _eleccion_usuario =0
    while (_eleccion_usuario !=4):
        _eleccion_usuario = int(input(mensaje_menu))
        if (_eleccion_usuario==1):
            print(estudiante1.nombre, estudiante1.edad, estudiante1.genero, estudiante1.colegio)
        elif (_eleccion_usuario==2): 
            print(profesor1.nombre,profesor1.edad,profesor1.nivelEducativo)
        elif (_eleccion_usuario==3): 
            print(director.nombre, director.edad, director.nivelEducativo)
        elif (_eleccion_usuario==4):
            print("gracis por usar este menu")
        else:
            print("ingrese solo los valores mostrados") 

############Entrada al codigo############ 
main()


