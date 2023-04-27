lista =[]
escolha = "S"
while escolha =="S":
    num = int(input ("Digite um numero :"))
    lista.append(num)
    if num not in lista:
        lista.append(num)
    escolha = str(input("Deseja continuar ? S/N :")).upper
print (lista.sort())