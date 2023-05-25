print('LEITURA DE NÚMEROS')

n = int(input('Digite um número interio entre 100 e 999: '))

if (n > 99) and (n < 1000):
    n = str(n)
    print(n[0])
    print(n[1])
    print(n[2])
else:
    print('VALOR INVÁLIDO')