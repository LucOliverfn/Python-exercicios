n1 = int (input("Digite o numero iniciador que deseja saber a tabuada:"))
inicio = 1
for cont in range (1,11):
    multi = n1*inicio
    print("-="*20)
    print("{} + {} = {}".format(n1,inicio,multi))
    inicio = inicio +1
print ("print fim da tabuada")
