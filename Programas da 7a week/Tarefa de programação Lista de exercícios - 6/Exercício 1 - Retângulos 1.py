larg = int(input("Digite o número da largura do retângulo: "))
alt = int(input("Digite o número da altura do retângulo: "))

x=larg
y=alt

while y > 0:
    while x > 0:
        print ("#", end="")
        x = x - 1
    print ()
    y = y - 1
    x = larg

