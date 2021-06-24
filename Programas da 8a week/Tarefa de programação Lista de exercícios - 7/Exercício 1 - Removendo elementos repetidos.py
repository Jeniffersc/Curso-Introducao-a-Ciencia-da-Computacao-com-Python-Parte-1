def remove_repetidos(lista):
    lista_cop = []#Criar uma lista vazia
    for i in lista: #Para todo item na lista passada como parâmetro verifica:
        if i not in lista_cop: #Se o item não está na lista vazia, faça:
            lista_cop.append(i) #Adicione na ultima posição da lista vazia o item que não estava até em então
    lista_cop.sort() #Função sort: ORDENAÇÃO DE UMA LISTA: É comum termos uma lista toda bagunçada e querermos ordenar os elementos contidos nela. Para ordenar uma lista de valores, basta chamar o método sort da lista.
    return lista_cop #Retorna a lista com os elementos de forma unica e ordenada 

lista = [26, 4, 2001, 1, 2, 3, 3] #Definir a lista 

lista = remove_repetidos(lista) #Faz com que a lista acima seja passada como parâmetro para a função remove_repetidos
print (lista) 
    
