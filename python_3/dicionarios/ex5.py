estado = {}
brasil = []
for cont in range (0,3):
    estado['uf'] = str(input('unidade ferderativa (uf) :'))
    estado['sigla'] = str(input('Sigla do estado :'))
    brasil.append(estado.copy())
print(brasil)
for z in brasil:
    for k, v in z.items():
        print(f'{k}:{v}')
        print()
