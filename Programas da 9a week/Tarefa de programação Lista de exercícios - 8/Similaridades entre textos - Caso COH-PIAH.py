import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

#------------------------------------------------------------------------------

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    cont = 0
    for i in range (len(as_a)): 
        cont = cont + (abs(as_a[i] - as_b[i]))
    
    return cont / 6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    lista_total_palavras = separa_palavras(texto)
    n_total_palavras = len(lista_total_palavras)
    
    tam_palavras = 0
    for i in range (n_total_palavras):
        tam_palavras = tam_palavras + len(lista_total_palavras[i])
        
    tam_med_palavra = tam_palavras / n_total_palavras
    type_token = n_palavras_diferentes(texto) / n_total_palavras
    hapax_legomana = n_palavras_unicas(texto) / n_total_palavras
    n_total_sentencas = len(separa_sentencas(texto))
    n_total_frases = len(separa_frases(texto))
    tam_med_sentenca = tam_palavras / n_total_sentencas
    complex_sent = n_total_frases / n_total_sentencas    
    tam_med_frase = tam_palavras / n_total_frases  
    assinatura = [tam_med_palavra, type_token, hapax_legomana, tam_med_sentenca, complex_sent, tam_med_frase]
    
    return assinatura    
    pass

def avalia_textos(textos, ass_cp):
    #IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.
    cont = 1
    assinatura_texto = calcula_assinatura(textos[cont])
    nivel_similaridade = compara_assinatura(assinatura_texto, ass_cp)
    men_nivel = nivel_similaridade  
    texto_infectado = cont
    cont = cont + 1
    while cont <(len (textos)):
        assinatura_texto = calcula_assinatura(textos[cont])
        nivel_similaridade = compara_assinatura(assinatura_texto, ass_cp)
        if nivel_similaridade < men_nivel:
            men_nivel = nivel_similaridade 
            texto_infectado = cont             
        cont = cont + 1
                  
    print ("O autor do texto %d está infectado com COH-PIAH " % (texto_infectado))
    return texto_infectado
    pass

def main():
    assinatura_cp = le_assinatura() #lê a assinatura do aluno infectado com COH-PIAH e retorna a assinatura, que é uma lista contendo os 6 traços linguísticos
    textos_lidos = le_textos()  #lê os textos e retorna uma lista de textos que serão comparados com a assinatura do aluno infectado com COH-PIAH
    avalia_textos(textos_lidos, assinatura_cp) #todos os textos serão comparados com a assinatura do aluno infectado com COH-PIAH para ver qual é mais parecido

    xonr
