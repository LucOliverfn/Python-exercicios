from datetime import date
atual = date.today().year
data = int(input("Em que ano voce nasceu ? :"))
idade = atual-data
if (idade<=9):
    print ("Você esta na categoria MIRIM")
elif (idade>9) and (idade<=14):
    print ("Você esta na categoria INFANTIL")
elif (idade>14) and (idade<=19):
    print ("Você esta na categoria JUNIOR")
elif (idade==20):
    print ("Você esta na categoria SENIOR")
else:
    print ("Você esta na categoria MASTER")