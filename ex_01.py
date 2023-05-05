def exibir(x, y):
    while (x == y) or (x < y):
        print(x)
        x += 1
n = int(input("Digite o número do começo:"))
m = int(input("Digite o número do fim:"))
exibir(n, m)