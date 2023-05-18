
def voto(a):
    idade = 2023 - a
    if idade >=18 and idade<=64:
        return f'com {idade} anos : Voto Obrigatorio'
    elif idade<18 and idade>=16:
        return f'com {idade} anos : Voto Opcional'
    elif idade<18:
        return f'com {idade} anos : Voto Negado'
    elif idade>=65:
        return f'com {idade} anos : Voto Opcional'
ano = int (input("Em qual ano voce nasceu :"))
print(voto(ano))
