from time import sleep
def contador(inicio,fim,salto):
    while inicio>=fim:
        print("Contagem de {} até {} com salto {}".format(inicio,fim,salto))
        while fim>inicio:
            print (inicio, end="")
            inicio-=salto
        print("FIM")
    if fim>inicio:
        print("Contagem de {} até {} com salto {}".format(fim,inicio,salto))
        while fim>inicio:
            print(fim, end="")
            fim+=salto
        print("Fim")

def divisao():
    print ("-="*30)

divisao()
contador(1,10,1)
divisao()
contador(10,1,1)
print ("Agora é a sua vez de personalizar a contagem")
inicio = int(input("inicio :"))
fim = int(input("Fim : "))
salto = int(input("Salto :"))
contador(inicio,fim,salto)


