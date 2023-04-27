n1 = float(input("Digite a primeira nota :"))
n2 = float(input("Diite a segunda nota :"))
media = (n1+n2)/2
if media<5.0:
    print ("Sua media foi de {}, voce esta REPROVADO".format(media))
elif media>=5.0 and media<=6.9:
    print ("Sua media foi de {}, voce esta de RECUPERAÇÃO".format(media))
else:
    print ("Sua media foi de {}, voce esta APROVADO".format(media))