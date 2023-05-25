import math

print('LOGARÍTIMO')

x = int(input('Digite um número inteiro e maior que zero:\n'))

if x > 0:
    print(f'O logarítimo de {x} é {math.log(x)}')
else:
    print('Número inválido!')
