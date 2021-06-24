import math

def main ():
    a = int(input("Digite o número de a: "))
    b = int(input("Digite o número de b: "))
    c = int(input("Digite o número de c: "))
    imprime_raizes(a, b, c)

def delta (a, b, c):
    return b ** 2 - 4 * a * c

def imprime_raizes (a, b, c):
    d = delta (a, b, c)
    if d == 0:
        raiz = (- b + math.sqrt(b ** 2 - 4 *a * c ))/ (2 * a)
        print ("A única raíz é ", raiz)
    else:
        if d < 0:
            print ("Esta equação não possui raízes reais")
        else:
            raiz1 = (- b + math.sqrt(b ** 2 - 4 *a * c ))/ (2 * a)
            raiz2 = (- b - math.sqrt(b ** 2 - 4 *a * c ))/ (2 * a)
            print ("A primeira raíz é ", raiz1)
            print ("A segunda raíz é ", raiz2)
