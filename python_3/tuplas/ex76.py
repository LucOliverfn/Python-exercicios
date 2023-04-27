lista = ("Lapis", 1.75, "borracha", 2.00, "caderno",15.60, "estojo",25.00, "transferidor",4.20, "compasso",9.99, "mochila",120.32, "caneta",22.33, "livro", 34.90)
print ("--"*20)
print ("            Listagem de preços")
print ("--"*20)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print('f{lista[pos]:.<30}')
    

