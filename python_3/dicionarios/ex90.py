boletim = {}
boletim['nome']=str(input("Nome do auluno : "))
boletim['media']=float(input("Media de {} :".format(boletim['nome'])))
for k , v in boletim.items():
    print(f'{k} é igual a {v}')
if boletim['media'] <7.0:
    print("Situação é iguala reprovado")
else:
    print("A situação do aluno é Aprovado")