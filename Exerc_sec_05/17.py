print('ÁREA DO TRAPÉZIO.')

b1 = float(input('Digite o valor da base maior: '))
b2 = float(input('Digite o valor da base menor: '))
h = float(input('Digite o valor da altura: '))

if b1 > 0 and b2 > 0:
    m = ((b1+b2) * h) / 2
    print(f'A área do Trapézio é: {m}')
else:
    print('Um ou mais valores estão incorretos!\nAs bases devem ser maior que zero!')
