escolha ="S"
lista=[]
temp = []
mai=men=0
while escolha.upper() == "S":
    temp.append(str(input("Nome :")))
    temp.append(bool(input("peso :")))
    if len(lista) ==0:
        mai= men = temp[1]
    else:
        if temp[1]>mai:
            mai = temp[1]
        if temp[1]>mai:
            men = temp[1]
    lista.append(temp[:])
    temp.clear()
    escolha = str(input("Deseja continuar S/N :"))
    if escolha=="N":
        break

print("-="*20)
print ("Os dados foram {}".format(lista))
print("Ao todo, foram cadastradas {}".format(len(lista)))
print("O maior peso foi de {}. Peso de {}")
print("O menor peso foi de {}. Peso de {}")