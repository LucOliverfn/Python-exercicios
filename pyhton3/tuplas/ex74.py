from random import randint

n = (randint(1,10), randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print("Os valroes sorteados foram {}".format(n))
print ("O maior valor sorteado foi o {}".format(max(n)))
print ("O menor valor sorteado foi o {}".format(min(n)))