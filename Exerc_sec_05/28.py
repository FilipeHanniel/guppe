print('PROGRAMA MÉDIAS\n\n')

opcao = input(f'Digite uma das opções desejadas:\n(a) MÉDIA GEOMÉTRICA: {chr(8731)}X*Y*Z\n(b) '
      f'MÉDIA PONDERADA: (X+2 * Y+3 * Z) / 6\n(c) MÉDIA HARMÔNICA: 1 / (1/X) + (1/Y) + (1/Z)\n(d)'
      f' MÉDIA ARITIMÉTICA: (X + Y + Z) / 3\n')

x = float(input('Digite o valor para X: '))
y = float(input('Digite o valor para Y: '))
z = float(input('Digite o valor para Z: '))

if opcao == 'a':
    print(f'{chr(8731)}{x} x {y} x {z}  = {(x*y*z) ** (1/3)}')
elif opcao == 'b':
    print(f'({x} + 2 x {y} + 3 x {z}) / 6 = {((x+2) * (y+3) * z) / 6}')
elif opcao == 'c':
    print(f'1/(1/{x} + 1/{y} + 1/{z}) = {1 / ((1/x) + (1/y) + (1/z))}')
elif opcao == 'd':
    print(f'({x} + {y} + {z}) / 3 = {(x + y + z) / 3}')
else:
    print('Opção inválida!\nFIM DE PROGRAMA!')

