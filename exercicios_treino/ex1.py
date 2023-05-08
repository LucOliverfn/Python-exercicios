lista=[34, 67, 12, 9, 52, 13, 126, 42, 1, -128, -54, 87]
soma=0
prod =0
grup1=[]
gurp2=[]
grup3=[]
grup4 =[]
for c in range (0,len(lista)):
    if c<=2:
        grup1.append(lista[c])
    elif c<=5:
        gurp2.append(lista[c])
    elif c<=8:
        grup3.append(lista[c])
    else:
        grup4.append(lista[c])
    soma+=lista[c]
    prod-=lista[c]

print (grup1)   
print(soma)
print(prod)
