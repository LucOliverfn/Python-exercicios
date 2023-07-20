lista =[]
cont = 0
while cont <3:
    num = int(input('digite um numero para ser adicionado na lista:'))
    lista.append(num)
    cont +=1
for c,v in enumerate(lista):
    print('Na posição {} encontreei o valor {}'.format(c,v))
print(lista)
