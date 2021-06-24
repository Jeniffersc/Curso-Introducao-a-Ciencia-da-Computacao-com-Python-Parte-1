num_int = int(input("Digite um número inteiro: "))

unidade = num_int % 10
num_int = (num_int - unidade)/10
dezena = num_int % 10

print("O dígito das dezenas é", dezena)
