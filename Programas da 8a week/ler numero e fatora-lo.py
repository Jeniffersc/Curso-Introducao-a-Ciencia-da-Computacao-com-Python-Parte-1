def fatorial ():
    n = 1
    fat=1
    while n>0:
        n = int(input("Digite um número inteiro positivo para ser fatoriado: "))#: 
        while n>0:
            fat = fat * n
            n = n - 1
        print (fat)
