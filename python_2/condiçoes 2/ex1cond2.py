valor = float(input("Qual o valor da casa que voce deseja comprar? :"))
sal = float(input("Qual o seu salario? :"))
anos = float(input("Em quantos anos voce deseja pagar o emprestimo? :"))
prestacao = valor/(anos*12)
print("Para pagar uma casa no valor de {:.2f} em {} anos, a prestação é de {}".format(valor,anos,prestacao) )
if prestacao>=(sal*30)/100:
    print ("Desculpe, mas voce não poderá financiar essa casa por exeder o valor necessario")
    print(" EMPRESTIMO NEGADO")
else:
    print ("EMPRESTIMO AUTORIZADO")