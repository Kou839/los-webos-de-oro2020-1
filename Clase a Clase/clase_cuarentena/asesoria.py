#estructura for

print(range(4)) 
print (list(range(4)))

print (list(range(7)))
lista = list(range(7))
print(lista)
for cosa in lista:
    print(cosa)
print("#"*40)
for posicion in range(7):
    print(posicion)

print("#"*40)
print (len(lista))
size_list = len(lista)
alimentos = ["carne", "huevo","salchicha","leche"]
precios = [5000,300,2500,5000]
size_list_alimentos= len (alimentos)
size_list_precios= len (precios)
print("#"*40)
for cosa in alimentos:
    print(cosa)
print("#"*40)
if (size_list_alimentos==size_list_precios):
    for i in range(size_list_alimentos):
        print(i)
        print(alimentos[i],precios[i])
else: print("las listas no tienen la misma cantidad de elementos") 
print("#"*40)


