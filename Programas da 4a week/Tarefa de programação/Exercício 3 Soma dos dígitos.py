n = input("Digite um número inteiro: ")

print(sum(int(i) for i in n))

#A função nativa sum calcula a soma dos itens de um objeto iterável. Por padrão, a função input retorna uma string, que é iterável no Python. Como queremos a soma algébrica dos dígitos, basta converter cada um para o tipo inteiro.
