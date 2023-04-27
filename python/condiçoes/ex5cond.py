numero = int(input("Qual onumero que deseja saber se é par ou impar? :"))
valor = numero%2
if valor==1:
    print ("O numero {} é impar".format(numero))
else:
    print ("O numero {} é par".format(numero))