n = int(input("Digite um número para ser decomposto: "))

fator = 2
multiplicidade = 0
     
while n>1:
    while n % fator == 0:
        n = n / fator
        multiplicidade = multiplicidade + 1        
    if multiplicidade > 0:
        print("fator", fator, "multiplicidade", multiplicidade)
    multiplicidade = 0
    fator = fator + 1
