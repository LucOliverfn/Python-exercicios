n1 = float (input("Qual o valor da primeira nota? :"))
n2 = float (input("Qual o valor da segunda nota ? :"))
m = (n1+n2)/2
print ("sua nota é igual a {:.1f}".format(m))
if m>=6:
    print ("Você esta na media, parabens")
else:
    print ("Você esta fora da media, ficara de recuperação")