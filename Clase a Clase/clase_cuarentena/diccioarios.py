#En los diccionarios podemos hacer uso del sistema llave valor
#Esto indica que al igual queden en un diccionaria toda palabra tiene
#su significado. Por ejemplo hagamos un diccionario de medios de transporte:
#un diccionario vacio se inicia de la siguiente forma: 
diccionario={}
#incluyendo su contenido
medios_transporte = {
    "carros":
    [
        "BMW",
        "AUDI",
        "CHEVROLET",
        "MAZDA"
    ],
    "motos" : ["AKT","HARLEY","AUTECO"]    
}
#en el caso de este diccionario podemos ver que se cuenta con
#las llaves carros y motos, cuando se solicita la llave carro se
# devuelve los carros asociados a este llave. igualmente para el caso
print ("los elementos que componen la llave carros son : {}".
format(medios_transporte["carros"]))
#de motos
print ("los elementos que componen la llave motos son : {}".
format(medios_transporte["motos"]))

print("#"*60)
estudiantes_programacion= {
    "Nombres" : ["Yuuto", "Lalo", "Usagi"],
    "Edad" : [19,21,20]
    
}

print("#"*60)
print(estudiantes_programacion["Nombres"])
print(estudiantes_programacion["Edad"])
print("#"*60) 

#si queremos obtener todas las llaves du un diccionario, lo podemos hacer así 
print(medios_transporte.keys())
print(estudiantes_programacion.keys())
#para poderlas literar las transformamos en lista
print (list (medios_transporte.keys()))
llaves= list (medios_transporte.keys())

#para obtener las llaves
print (medios_transporte.values())
#para poderlas literar las transformamos en lista
print (list (medios_transporte.values())) 
valores= list (medios_transporte.values())
print(valores[0]) 

diccionario={} 
diccionario['Estudiantes']= ['Meli','Vale','cathe']
diccionario['Profesores']= ['Braiam','Diego',] 
diccionario['Aulas']= ['A202','A206',] 
print (diccionario)
print(list(diccionario.keys()))
print(list(diccionario.values()))
print(diccionario['profesores'])
print(diccionario)

#los diccionarioos nos permiten tener de unna forma más organizada la información
#en ocaciones podemos ver diccionarios de diccionarios 
materiales={}
materiales['oro']= ['18k','16k']
materiales['marcadores']= ['pelikan','paper maker']
print(type(materiales))
diccionario['Elementos']=materiales 
print(diccionario['Elementos'] ['marcadores']) 

notas = {}
notas["QUIZ1"]= [4,5,4,5,4,5,4,5,4,5,4,5]
notas["QUIZ2"]= [4,5,4,5,4,5,4,5,4,5,4,5]
notas["PARCIAL"]= [4,5,4,5,4,5,4,5,4,5,4,5]
notas["TALLERES"]= [4,5,4,5,4,5,4,5,4,5,4,5]
estudiantes_programacion["notas"]=notas

print (estudiantes_programacion["notas"]["QUIZ1"])
#operaciones con diccionarios

#generar una copia sin afectar al original 
diccionario_copia=diccionario.copy()
print(diccionario_copia)

#limpiar el contenido de un diccionario
diccionario_copia.clear()
print (diccionario_copia)

#crear un diccionario con las llaves el valor inicial será el mismopara todos 
keys = ["idiomas","carreras"]
values = "soy un valor genérico"
created_dic = dict.fromkeys(keys,values)
print (created_dic)

#sin valor inicial
created_dic = dict.fromkeys (keys)
print (created_dic)

#obtener la definición de otra manera directamente de una lista
print (diccionario.get("profesores"))

#eliminar un componente del diccionario 
diccionario_copy = diccionario.copy()

#se ingresa el valor específico valor de la llave a eliminar
diccionario_copy.pop("profesors") 
print(diccionario_copy)

#elimina la útima llave agregada
diccionario_copy.popitem()
print(diccionario_copy)

#Agregar una llave o si exise sobrescribe su valor
diccionario_copy.setdefault("computadoras",["Apple","Dell","Lenovo"])
print(diccionario_copy)
diccionario_copy.setdefault("computadoras",["Apple","Dell","Lenovo","IBM"]) 
print(diccionario_copy)




