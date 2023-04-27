galera = list()
dado = list()
totmai=totmen=0
for c in range (0,3):
    dado.append(str(input("nome :")))
    dado.append(int(input("idade :")))
    galera.append(dado[:])
    dado.clear()
for pes in galera:
    if pes[1]>=21:
        print ("{} é maior de idade".format(pes[0]))
        totmai+=1
    else:
        print ("{} é menor de idade".format(pes[0]))
        totmen+=1
print("Temos {} menores de idade e {} maiores de idade".format(totmen,totmai))
