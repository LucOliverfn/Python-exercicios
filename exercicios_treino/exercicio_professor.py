lista= []
while True:
    print (" (C) Cadastrar \n (L) Listar \n (P) Procurar \n (S) Sair")
    escolha = str(input("Qual a opção que o senhor(a) dejesa :")).upper()
    if escolha=="C":
        print ("-="*20)
        placa = str(input("informe a placa do veiculo :"))
        modelo = str(input("informe o modelo do veiculo :"))
        marca = str(input("informe a marca do veiculo :"))
        ano = str(input("informe o ano de fabrição do veiculo :"))
    if escolha=="L":
        print()
    if escolha=="S":
        break
print("fim do programa")