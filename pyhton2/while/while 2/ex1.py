s=0
n=0
tot = 0
while True:
    n = int(input("Digite um numero :"))
    s += n
    tot+= 1
    if n ==999:
        break
print (f"Você digitou {tot} numeros e a soma dos numeros digitados foi de {s}")
