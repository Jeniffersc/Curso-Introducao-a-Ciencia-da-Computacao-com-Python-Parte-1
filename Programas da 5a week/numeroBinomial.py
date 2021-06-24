# Não é preciso solicitar os valores de n, no terminal do py usa-se o nome da função e o valor escolhido
# FATORAL(VALOR_DE_N_ESCOLHIDO)
# FATORAL(VALOR_DE_K_ESCOLHIDO)

def fatorial (x): #Fatorial de qualquer número x, por exemplo o de n e de k
    fat = 1
    while x > 0: 
        fat = fat * x
        x = x - 1
    return fat

def numero_binomial(n, k):
    return fatorial(n) // (fatorial(k) * fatorial(n-k))

#Testes automatizados 
 def testa_fatorial(x): 
    if fatorial (1) == 1:
        print ("Funciona para 1")
    else:
        print ("Não funciona para 1")
        
    if fatorialDeN (2) == 2:
        print ("Funciona para 2")
    else:
        print ("Não funciona para 2")
        
    if fatorialDeN (0) == 1:
        print ("Funciona para 0")
    else:
        print ("Não funciona para 0")
        
    if fatorialDeN (5) == 120:
        print ("Funciona para 5")
    else:
        print ("Não funciona para 5")

def testa_numero_binominal (): #Testa a função número binomial
    if numero_binomial (8, 3) == 56:
        print ("Funciona para n=8 e k=3")
    else:
        print ("Não funciona para n=8 e k=3")
