soma=0
cont=0
for c in range (1,7):
    num =int (input("digite o {} valor :".format(c)))
    if num%2==0:
        soma = soma +num
        cont += 1
print("Você dogitou {} numeros pares. A soma deles se da por {}".format(cont,soma))
    
