print('MULTIPLOS DE 3 OU 4\n')

soma = 0

for i in range(1001):
    if (i % 3 == 0) or (i % 5 == 0):
        soma = soma + i

print(soma)