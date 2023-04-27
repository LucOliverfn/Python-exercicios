inicio = int (input("Digite o numero iniciador da contagem:"))
razao = int(input("Digite qual sera a razao da contagem: "))
fim = inicio +(10-1) * razao
for cont in range (inicio,fim + razao,razao):
    print (cont, end=" --> ")
print ("fim")