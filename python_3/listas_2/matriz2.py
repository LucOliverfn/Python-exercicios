lista = []
for i in range (0,3):
    inicio = (i*3)+1
    temino = (inicio+3)
    prov = []
    for j in range (inicio,temino):
        prov.append(j)
    lista.append(prov)
print (lista, end="")