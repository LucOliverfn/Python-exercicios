dicionario = {}
gols = []
dicionario['nome'] = str(input("Nome do jogador :"))
partidas= int (input("Quantas partidas {} jogou :".format(dicionario['nome'])))
if partidas > 0:
    ngols = 0
    for i in range (0,partidas):
        ng =int(input('Quantos gols na partida {} :'.format(i+1)))
        ngols+=ng
        gols.append(ng)
    dicionario['gols']= gols[:]
    dicionario['total'] = ngols
    print("-="*30)
    print (dicionario)
    print("-="*30)
    for k,v in dicionario.items():
        print ("O campo {} tem o valor {}".format(k,v))
    print("-="*30)
    print ("o jogador {} jogou {} partidas".format(dicionario["nome"], partidas))
    for i in range(0,partidas):
        print("=> Na partida {}, fez {} gols".format(i+1, dicionario["gols"][i]))
    print ("Foi um total de {}".format(ngols))
    