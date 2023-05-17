from random import randint


def sorteio(lista):
    print ('sorteando 5 valores da lista :', end="")
    for i in range (0,5):
        n = randint(1,10)
        lista.append(n)
        print (f'{n}' , end="")
def somaPar():
    soma = 0
    for i in numeros:
        if i%2 ==0:
            soma += i
    print(f'Somando os valore pares de {numeros}, temos {soma}')
numeros = []
sorteio(numeros)
somaPar(numeros)  