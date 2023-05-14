dicionario = {}

dicionario['nome'] =  str(input("Nome  :"))

while True:
    escolha = str(input("GOSTARIA DE CONTINUAR [S/N] :")).upper()
    while True:
        dicionario['sexo'] = str(input("SEXO  [M/F] :")).upper()
        if dicionario["sexo"] in 'MF':
            break
        print("ERRO! Por Favor, Digite apenas M ou F.")

    if escolha in 'SN':
        if escolha == 'N':
            break
    print("ERRO! Por Favor, Digite apenas S ou N.")
