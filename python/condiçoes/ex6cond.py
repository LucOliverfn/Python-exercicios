viagem = float(input("Qual a distancia que voce ira percorrer na viagem? :"))
if viagem>=200:
    custo= viagem*0.45
    print ("A taxa da viagem vai ficar em torno de 0.45. O custo da sua viagem vai ficar em torno de {:.2f}".format(custo))
else:
    custo= viagem*0.50
    print ("A taxa da viagem vai ficar em torno de 0.50. O custo da sua viagem vai ficar em torno de {:.2f} Reais".format(custo))