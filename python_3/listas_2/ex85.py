lista=[[],[]]
valor =0
for h in range(0,7):
    n = int(input("Digite o {}° numero :".format(h+1)))
    if n%2==0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print ("-="*20)
print("TODOS OS VAORES :{}".format(lista))
lista[0].sort()
lista[1].sort()
print ("Os numeros pares são {}".format(lista[0]))
print ("Os numeros impares são {}".format(lista[1]))
