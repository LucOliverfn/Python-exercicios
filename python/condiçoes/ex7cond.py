sal= float(input("Qual o seu salario :"))
if sal>1250:
    aumento= (sal*10)/100
    print("Seu salario vai ter um aumento de 10%, sendo ele de {:.2f} reais".format(aumento))
else:
    aumento= (sal*15)/100
    print("Seu salario vai ter um aumento de 15%, sendo ele de {:.2f} reais".format(aumento))
print ("Fim do programa")