def MinMax (temperaturas):
    print("A menor temperatura do mês foi: ", mínima(temperaturas), " C.")
    print("A maior temperatura do mês foi: ", máxima(temperaturas), " C.")

def mínima (temps): #SE COLOCAR NO TERMINAL: minima([0,1,2]) O PROGRAMA IRÁ RETORNAR O MENOR NÚMERO DESSA LISTA: 0,1,2
    min = temps[0] #inicializa a variável com a primeira temperatura passada como parâmetro
    i = 1 #Incializa com 1, pois o mínimo já contem o valor da primeira temperatura
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min

def máxima (temps): #SE COLOCAR NO TERMINAL: minima([0,1,2]) O PROGRAMA IRÁ RETORNAR O MENOR NÚMERO DESSA LISTA: 0,1,2
    max = temps[0] #inicializa a variável com a primeira temperatura passada como parâmetro
    i = 1 #Incializa com 1, pois o mínimo já contem o valor da primeira temperatura
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i + 1
    return max

def teste_pontual(temp, valor_esperado):
    valor_calculado = mínima(temp)
    if valor_calculado != valor_esperado:
        print ("Valor errado para array ", temp)
        print ("O valor esperado era ", valor_esperado, ". Valor calculado foi: ", valor_calculado)    

def testa_mínima():
    print("Iniciando os testes")
    teste_pontual([0], 0)
    
    #AO INVÉS DE FAZER AS LINHAS ABAIXO, FAZ-SE AS LINHA DE CIMA E A FUNÇÃO testa_pontual()

    #temp = [0]
    #if mínima (temp) != 0:
        #print ("Valor errado para array ", temp)
    
    teste_pontual([0, 0, 0, 0, 0], 0)
    #if mínima (temp) != 0:
        #print ("Valor errado para array ", temp)
    
    teste_pontual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
    #if mínima (temp) != 0:
        #print ("Valor errado para array ", temp)
    
    teste_pontual([37, 30, 25, 26, 29, 31, 22, 100], 22)
    #if mínima (temp) != 22:
        #print ("Valor errado para array ", temp)
    
    teste_pontual([-15, -12, 0, 20, 30], -15)
    #if mínima (temp) != -15:
        #print ("Valor errado para array ", temp)
        
    print ("Finalizando os testes")

#É NECESSÁRIO IMPLEMENTAR A FUNÇÃO TESTA_MÁXIMA
    
