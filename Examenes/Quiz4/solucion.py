import matplotlib.pyplot as plt
import pandas as p 

inventario = p.read_csv("inventario.csv", encoding='UTF-8',header=0, delimiter=";").to_dict
print(inventario)

plt.title("Elementos vs unidades",fontsize=20)
plt.bar(inventario["Elemento"].values(),inventario["Unidades"].values(),align="center")
plt.xlabel("Elemento")
plt.ylabel("Unidades")
plt.xticks(rotation=90)
plt.savefig("Inventario.png")
plt.show() 

plt.title("Elementos vs Viejo",fontsize=20)
plt.bar(inventario["Elemento"].values(),inventario["Viejo"].values(),align="center")
plt.xlabel("Elemento")
plt.ylabel("Viejo")
plt.xticks(rotation=90)
plt.savefig("Inventario.png")
plt.show() 

plt.title("Elementos vs Nuevo",fontsize=20)
plt.bar(inventario["Elemento"].values(),inventario["Nuevo"].values(),align="center")
plt.xlabel("Elemento")
plt.ylabel("Nuevo")
plt.xticks(rotation=90)
plt.savefig("Inventario.png")
plt.show() 

