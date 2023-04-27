inicio = int (input("Digite o numero iniciador da contagem:"))
fim = int(input("Digite o numero que a contagem ira acabar:"))
salto = int(input("Digite qual sera o salto da contagem: "))
for c in range(inicio,fim+1,salto):
    print (c)
