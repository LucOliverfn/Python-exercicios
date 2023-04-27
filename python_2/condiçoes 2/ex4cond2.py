from datetime import date
ano=int(input("Digite o ano em que voce nasceu :"))
atual = date.today().year
idade = atual - ano
if atual-ano<18:
    print ( "voce ainda vai se alistar ao serviço militar")
    saldo = 1
elif atual-ano==18:
    print ("é a hora de voce se alista")
else:
    at
