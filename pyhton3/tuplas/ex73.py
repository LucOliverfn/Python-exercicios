time = ("fluminense", "Botafogo", "fortaleza", "vasco", "Palmeiras", "internacional", "bragantino", "São paulo", "flamengo", "Goias", "cruzeiro", "athletico-pr", "Corinthians", "cuiaba", "Atletico-mg", "santos", "bahia", "coritiba", "America-mg" )
print ("os 5 primeiros times do brasileirão são : {}".format(time[0:5]))
print ("os 5 ultimos times do brasileirão são : {}".format(time[14:])) #ou pode ser time[-4:]
print ("Times em ordem alfabetica {}".format(sorted(time)))
print ("O cruzeiro está na posição {}".format(time.index("cruzeiro")+1))