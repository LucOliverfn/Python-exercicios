from random import randint
escolha = randint(0,10)
tentativas = 0
print("OLÁ vamos brincar de acertar o numero que eu estou pensando")
print("Será que vc consegue acertar?")
numero = int(input("de 0 a 10, qual o numero que eu escolhi :"))
#acertou = "False"
#while not acertou:
while escolha != numero:
    tentativas+=1
    if numero>escolha:
        print("Menos, Tente novamemte")
        numero = int(input("Qual numero que eu escolhi ??? :"))
    if numero<escolha:
        print("Mais, Tente novamente")
        numero = int(input("Qual numero que eu escolhi ??? :"))
tentativas = tentativas +1
print("Parabens, o numero que eu pensei foi {}, voce precisou de {} tentativas para acertar.".format(escolha, tentativas))

