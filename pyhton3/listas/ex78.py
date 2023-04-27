lista =[]
for c in range (0,5):
    lista.append(int(input("Digite o {}° numero da lista: ".format(c+1))))
    #num = int(input("Digite o {}° numero da lista: ".format(c+1)))
    #lista.append(num)
print ("Voce digitou a seguinte lista {}".format(lista))
print ("O maior numero da lista foi o {} encontrado nas posiçoes ".format(max(lista)),end="")
for i,v in enumerate(lista):
    if v == max(lista):
        print ("{}......".format(i), end="")
print()
print ("O menor numero da lista foi o {}, encontrado nas posições ".format(min(lista)), end="")
for o,x in enumerate(lista):
    if x == min(lista):
        print ("{}......".format(o), end="")