tup = ("Zero",  "um" ,"dois", "tres" ,"quatro" ,"cinco", "seis" ,"sete" ,"oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze" ,"dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
escolha = int(input("Digite um numero entre 0 e 20 :"))
while True:
    escolha = int(input("NUMERO NÂO DISPONIVEL. Digite um numero entre 0 e 20 :"))
    if 0<= escolha >=20:
        break
    print("Tente novamente. ", end="")
print ("voce digitou o numero {}".format(escolha[tup]))
        

