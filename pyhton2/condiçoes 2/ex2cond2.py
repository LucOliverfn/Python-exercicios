numero = int(input("DIgite um numero inteiro :"))
print ("1 = converter para Binario")
print ("2 = converter para Octal")
print ("3 = converter para Hexagonal")
escolha = int (input ("Digite o numero correspondente a sua escolha? : "))
if escolha==1:
    print("{} convertido para binario é {}".format(numero, bin(numero)))
elif escolha==2:
    print("{} convertido para binario é {}".format(numero, oct(numero)))
elif escolha==3:
    print("{} convertido para binario é {}".format(numero, hex(numero)))
else:
    print("NUMERO INCORRETO")