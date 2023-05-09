matriz=[[0,0,0],[0,0,0],[0,0,0]]

# FOR PARA INCLUIR OS NUMEROS DENTRO DAS CASA
for linha in range (0,3):
    for coluna in range (0,3):
         matriz[linha][coluna] = int(input("digite o numero para a posição {}.{} :".format(linha,coluna)))

#FOR PARA PARA PRINTAR NA TELA 
for s in range (0,3):
    for m in range (0,3):
        print (f'[{matriz[s][m]}]', end="")
    print()