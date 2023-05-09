print("=-"*20)
print ("      JOGA NA MEGA SENA     ")
print("=-"*20)
from random import randint
cont = 0
lista =[]
jogos=[]
total=0
vezes = int (input("Quantos numeros voce quer que ue sorteie? :"))
print ("---------- Sorteando----------")
while total<=vezes:
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >=6:
            break
        lista.sort()
        jogos.append(lista[:])
        lista.clear
print("os numeros sorteados foram {}".format(jogos))

