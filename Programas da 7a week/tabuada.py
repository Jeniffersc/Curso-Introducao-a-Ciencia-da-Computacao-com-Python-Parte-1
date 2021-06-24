linha = 1
coluna = 1
while linha <= 10:
    while coluna <= 10:
        print (linha * coluna, end = "\t") #\t irá adicionar um tab entre os resultados
        coluna = coluna + 1
    linha = linha + 1
    print () #pula linha de uma tabela a outra
    coluna = 1
