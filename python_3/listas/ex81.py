escolha ="N"
lista=[]
while escolha.upper()=="N":
    lista.append(int(input("digite um valor :")))
    escolha = str(input("Deseja continuar? S/N :"))
    if escolha.upper() == "S":
        break
print ("Você digitou {} elementos".format(len(lista)))
lista.sort(reverse=True)
print ("Os valores em ordem decrescente são {}".format(lista))
if 5 in lista:
    print("O valor 5 esta presente na lista")
else:
    print("O lavor 5 não foi encontrado na lista")