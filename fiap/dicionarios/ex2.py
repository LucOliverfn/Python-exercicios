alunos = [{"nome":"murilo", 
        "idade":19, 
        "email":"Murillo@fiap.com.br", 
        "nota":7.0},
        {"nome":"maria rita", 
        "idade":32, 
        "email":"maria@fiap.com.br", 
        "nota":4.4},

         {"nome":"murilo", 
        "idade":19, 
        "email":"Murillo@fiap.com.br", 
        "nota":10}
]

# soma = alunos[0]["nota"] + alunos[0]["nota"] + alunos[0]["nota"]
# media = soma/3.0
# print ("Soma :{}".format(soma))
# print ("Media :{}".format(soma))

soma = 0
for aluno in alunos:
    soma = soma + aluno["nota"]


print("Soma: ", soma )