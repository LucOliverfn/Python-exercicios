
som=0
n = (int (input ("Digite um valor  :")), int (input ("Digite um valor  :")),int (input ("Digite um valor  :")),int (input ("Digite um valor  :")),int (input ("Digite um valor  :")))
print ("Você digitou os valores {}".format(n))
print ("O numero 9 apareceu {} vezes".format(n.count(9)))
if 3 in n:
    print ("O numero 3 foi digitado na posição numero {}".format(n.index(3)+1))
else:
    print("O numero 3  não foi digitado por você")
print ("Voce digitou {} numero pares".format(som))
for cont in n:
    if n % 2==0:
        som +=1
