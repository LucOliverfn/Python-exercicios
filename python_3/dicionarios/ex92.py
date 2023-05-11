dicionario = {}
dicionario['nome'] = str(input("NOME = "))
ano = int(input("Ano de Nascimento:"))
dicionario['idade'] = 2023-ano
dicionario['CTPS'] = int(input("Carteira de Trabalho (0 não tem): "))
if dicionario['CTPS'] >0:
    dicionario['contrato'] = int(input("Contratação: "))
    dicionario['salario'] = float(input("Salario :"))
    dicionario['aposentadoria'] = (dicionario['contrato']-ano)+35
print(dicionario)
for k,v in dicionario.items():
    print(f'{k} tem o valor de {v}')