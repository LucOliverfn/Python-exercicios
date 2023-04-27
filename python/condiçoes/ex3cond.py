import random
lista = [0,1,2,3,4,5]
escolhido = random.choice(lista)
advinhado = int(input("qual o numero que o computaodr escolheu :"))
if escolhido==advinhado:
    print ("VOCE ACERTOU, PARABENS!!!!!! ")
else:
    print ("VOCE ERROU, O NUMERO ESCOLHIDO PELO COMPUTADOR FOI O ", escolhido)
print("FIM DO PROGRAMA")
