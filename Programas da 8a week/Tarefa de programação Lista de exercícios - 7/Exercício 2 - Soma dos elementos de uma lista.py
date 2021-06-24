

def soma_elementos (lista):
    cont = len(lista)
    i = 0
    soma = 0
    while i < cont:
        lista_cop = lista [:]
        soma = soma + lista_cop[i]
        i = i + 1
    return (soma)

lista = [1, 2, 5, 100]

lista = soma_elementos (lista)
print (lista)
