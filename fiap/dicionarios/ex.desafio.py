lista = []
while True:
    print("Nome\tTelefone\tEmail")
    for c in lista:
        print(c["nome"], c["numero"], c["email"])
    print("\n\n\n")
   
    n = (input("Digite o seu nome :"))
    email = (input("Digite seu email :"))
    numero = (input("Digite o seu telefone:"))
    d = {"nome":n, "email":email, "telefone":numero}
    lista.append(d)
    escolha =(input("Gostaria de adicionar mais uma pessoa ao cadastro? S/N :")).upper
    if escolha=="N":
        break
print ("Fim do programa")