vel =int(input("Qual a velocidade do carro? :"))
if vel>80:
    print ("Você foi multado ")
    multa = (vel-80)*7
    print ("sua multa foi de {}".format(multa))
else:
    print("FIM DO PROGRAMA")