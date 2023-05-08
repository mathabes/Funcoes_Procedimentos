def primo(x: int) -> None:
    div = 0
    for cont in range(1, x):
        if x % cont == 0:
            div += 1
    if x != 1 and div < 2:
        print("true")
    else:
        print("false")
        
        
n = int(input("Digite um número: "))
primo(n)
