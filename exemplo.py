def subtracao(a, b):
    c = a - b
    return c

x = int(input("Digite um número: "))
y = int(input("Digite um número: "))
if subtracao(x, y) < 0:
    print("Resposta Negativa!!!")
else:
    print("Resposta Positiva!!!")