pessoas = []
dados = []
while True:
    nome = str(input("Digite o nome a ser cadastrado :"))
    idade = int(input("Digite a idade de {} :".format(nome)))
    dados.append(nome)
    dados.append(idade)
    pessoas.append(dados[:])
    escolha = str(input("Gostaria de cadastrar masi alguma pessoa?: (S/N) :"))
    if escolha in 'Nn':
        break
print(pessoas)