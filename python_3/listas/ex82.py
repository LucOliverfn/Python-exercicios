escolha ="N"
lista = []
lista_par=[]
lista_impar=[]
while escolha.upper()=="N":
    num = int(input("digite um numero qualquer :"))
    lista.append(num)
    if num%2==0:
        lista_par.append(num)
    else:
        lista_impar.append(num)   
    escolha = str(input("Deseja continuar? S/N :"))
    if escolha.upper() == "S":
        break
print ("A lista completa é {}".format(lista))
print ("A lista de pares é {}".format(lista_par))
print ("A lista de impares é {}".format(lista_impar))