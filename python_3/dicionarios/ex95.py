dicionario = {}
galera = []
while True:
    dicionario.clear
    dicionario['nome'] =  str(input("Nome  :"))
    while True:
        dicionario['sexo'] = str(input("SEXO  [M/F] :")).upper()[0]
        if dicionario["sexo"] in 'MF':
            break
        print("ERRO! Por Favor, Digite apenas M ou F.")
    dicionario['idade'] = int (input('Idade: '))
    galera.append(dicionario[:])
    while True:
        escolha = str(input("Quer continuar [S/N]:")).upper()[0]
        if escolha in 'SN':
            break
        ("ERRO! Por Favor, Digite apenas S ou N.")
    if escolha =='N':
        break
print (galera)

