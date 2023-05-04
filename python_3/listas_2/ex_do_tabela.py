lista = []
prov = []
soma=0
media = 0
for cont in range (0,7):
    lista.append(int(input("Digite o {}° numero:".format(cont+1)))) 
    soma+=lista[cont]
    media= soma/len(lista)
print ("Numero   Soma   Media")
for c in range (7,0,-1):    
    print("{}       {}        {}".format(lista[-1],soma,media))
    soma -=lista[-1]
    del lista[-1]
    if len(lista)!=0:
        media= soma/len(lista)
    else:
          media= soma/1
    
     
    
#    lista.pop(c)
#    print(lista)
