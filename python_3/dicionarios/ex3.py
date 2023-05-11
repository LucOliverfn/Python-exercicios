filme ={'nome':'Star Wars', 'ano':1997, 'diretor':'George Lucas'}
filme2 ={'nome':'matrix', 'ano':1988, 'diretor':'brothers wachawski'}
print(filme.values())
print(filme.keys())
print(filme.items())
locadora=[]
locadora.append(filme)
locadora.append(filme2)

for k,v in filme.items():
    print(f'o {k} é {v}')
print (locadora[1]['nome'])
print (locadora[0])