from random import randint

lista = []
prov = []
iguais = []
for cont in range(0,100):
    lista.append (randint(1,100))
consulta = int(input("Qual numero voce deseja consultar? :"))
for c in range(0,len(lista)):
    print (lista[c],end=",")
    if consulta == lista[c]:
        prov.append (lista[c])

if consulta in lista:
    print()
    print ("O numero {} está na lista e ele ocorre {} vezes na lista".format(consulta,len(prov)))
else:
    print()
    print("O numero {} não está na lista".format(consulta))


