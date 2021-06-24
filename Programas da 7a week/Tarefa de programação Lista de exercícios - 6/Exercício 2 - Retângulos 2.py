larg = int(input("Digite o número da largura do retângulo: "))
alt = int(input("Digite o número da altura do retângulo: "))

x=larg
y=alt
cont=larg

while y > 0:
    while x > 0 and x <= larg:
        if y==1 or y==alt:
            print ("#", end="")
        else:
            if x==1 or x==cont:
                print ("#", end="")
            else:
                print(" ", end="")
        x = x - 1       
    print ()
    y = y - 1
    x = larg
