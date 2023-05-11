pessoas = {'nome':'lucas', 'sexo': 'm', 'idade':22}
del(pessoas['sexo'])
pessoas['graduação'] = 'Estudante'
for k, v in pessoas.items():
    print(f'{k}={v}')