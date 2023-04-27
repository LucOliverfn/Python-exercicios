while True:
    n = int (input("Digite qual numero voce deseja saber a tabuada :"))
    if n<=0:
            break
    for c in range (0,11):
        multi = n * c
        print (f"{n} X {c} = {multi}")
        print ("=====================")
print ("Fim DO prograaamaaa")