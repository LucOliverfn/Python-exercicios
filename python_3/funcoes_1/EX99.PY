from time import sleep
def maior(*num):
    mai = 0
    print("-="*30)
    print ("Analisando os valores passados...")
    
    for i in num:
        print ("{} ".format(i),end="")
        sleep(0.5)
        if i>mai:
            mai = i
    print(f'foram informados {len(num)} ao todo')
    print(f'O maior valor informado foi o {mai}')
maior(2,3,4,5,6,7)
maior (4,7,0)
maior (1,2)
maior (6)
maior()