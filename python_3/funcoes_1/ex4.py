def contador (*num):
    for valor in num:
        print ("{} ".format(valor), end="")
    print ("Fim")

contador(2,4,6)
contador(1,5,8,)
contador(1)
contador(4,7,8,2,4,5,)