sair = "N"
n1 = int(input("Digite o primerio numero por favor :"))
n2 = int (input("Digite o segundo numero por favor :"))
while sair == "N":
    print ("[1] somar")
    print ("[2] multiplicar")
    print ("[3] maior")
    print ("[4] novos numeros")
    print ("[5] sair ")
    escolha = int(input ("Digite uma opção :"))
    if escolha==1:
        soma = n1 +n2
        print ("A soma de {} e {} é de {}".format(n1,n2,soma))
    if escolha==2:
        multi = n1*n2
        print ("A multiplicação de {} e {} é de {}".format(n1,n2,multi))
    if escolha==3:
        if n1>n2:
            print ("Entre {} e {} o maior valor é {}".format(n1,n2,n1))
        if n1<n2:
            print ("Entre {} e {} o maior valor é {}".format(n1,n2,n2))
        else:
            print("{} e {} são iguais".format(n1,n2))
    if escolha==4:
        n1 = int(input("Digite o primerio numero por favor :"))
        n2 = int (input("Digite o segundo numero por favor :"))
    if escolha==5:
        print ("SAINDO DO SISTEMA") 
        sair=="S"
        exit()
