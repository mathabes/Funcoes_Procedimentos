def nota (x):
    if (x < 10) and (x > 0) or (x == 0) or (x == 10):
       return print ("true")
    else:
        return print("false")
n = int(input("Digite uma nota: "))
nota(n)
