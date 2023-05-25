x = int(input('Digite um número inteiro: '))

if (x % 3 == 0) and (x % 5 != 0):
    print(f'{x} é divisível por três!')
elif (x % 3 != 0) and (x % 5 == 0):
    print(f'{x} é divisível por cinco!')
elif (x % 3 == 0) and (x % 5 == 0):
    print(f'{x} é divisível por três e cinco!!!')
else:
    print(f'{x} não é divisível nem por três nem por cinco!')
