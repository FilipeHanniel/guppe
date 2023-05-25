print('DIVISORES')

n = int(input('Digite um número inteiro positivo: '))

if (n > 0) and (n % 2 == 0):
    for i in range(2, n + 1):
        if n % i == 0:
            print(i)
else:
    print('valor inválido!')
