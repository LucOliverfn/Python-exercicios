sexo = str(input("Digite o seu sexo (M/F) :")).upper()
while sexo not in "MF":
    sexo = str(input("Dados invalidos. Por favor, informe seu sexo novamente: ")).upper()
print("Sexo {} registrado com sucesso".format(sexo))
