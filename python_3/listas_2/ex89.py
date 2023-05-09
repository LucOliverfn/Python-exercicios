lista=[]
while True:
    nome=str(input("Nome :"))
    n1=float(input("nota 1 :"))
    n2=float(input("nota 2 :"))
    media = (n1+n2)/2
    escolha = str(input("Gostaria de continuar S/N :"))
    lista.append([nome,[n1,n2],media])
    if escolha.upper()=="N":
        break
print ("-="*20)
print("No.  Nome    Média")
print ("-="*20)
for i, a in enumerate(lista):
    print (f'{i}  {a[0]} {a[2]}')
    # print("{} {}   {}".format(i,lista[i][0],lista[i][2]))
while True:
    notas = int(input("gostaria de cosnultar as notas de qual aluno? (999 interrompe):"))
    if notas==999:
        print("finallizando...")
        break
    if notas <=len(lista)-1:
        print("As notas de {} são {} ".format(lista[notas][0], lista[notas][1]))
