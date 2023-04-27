print("-="*20)
print("ANALISADOR DE TRIANGULOS")
print("-="*20)
r1= float(input ("Digite o primeiro numero :"))
r2= float(input ("Digite o segundo numero :"))
r3= float(input ("Digite o terceiro numero :"))
if r1<r2+r3 and r2 <r1+r3 and r3<r1+r2:
    print("Os seguimentos acima podem formar triangulo")
else:
    print ("Os seguimnetos acima não podem formar triangulo")