print('MULTIPLO DE 11, 13 ou 17')

n = int(input('Digite um número inicial para a busca do múltiplo: \n'))

while n % 11 != 0 or n % 13 != 0 or n % 17 != 0:
    n = n + 1

print(n)