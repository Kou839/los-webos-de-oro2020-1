import pandas as pd 
#primera entrada nombre de archivo
#segunda entrada Enconding 
#tercera entrada el header
#delimitador es el caracter especial que separa mis datos
#.to_dict transforma mis datos en un diccionario

diccionario=pd.read_csv("estudiantes.cvs", enconding='UTF-8', header= 0,delimiter';').to_dict()

