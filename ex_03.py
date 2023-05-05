def delta(a, b, c):
    resp = b**2 - (4*a*c)
    return resp
x = int(input("Digite o valor de a: "))
y = int(input("Digite o valor de b: "))
z = int(input("Digite o valor de c: "))
print("O valor de delta é:", delta(x, y, z))