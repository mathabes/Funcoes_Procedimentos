#ERRADO
def primo(x):
    div = 0
    for cont in range(1, x):
        if x % cont == 0:
            div += 1
        if div == 2:
            return print("true")
        else:
            return print("false")
n = int(input("Digite um número: "))
primo(n)
