print('OPERAÇÕES')

print('Digite uma das operações desejadas:')
print('1 - Soma de dois números.')
print('2 - Diferença entre 2 números (maior pelo menor).')
print('3 - Produto de 2 números.')
print('4 - Divisão entre 2 números (o denominador não pode ser zero).')
print('Por favor, digite uma das opções: ')

opcao = int(input())

if opcao == 1:
    x = float(input('Digite o primeiro número: '))
    y = float(input('Digite o segundo número: '))
    print(f'{x} + {y} = {x+y}\nFim de programa!')
elif opcao == 2:
    x = float(input('Digite o primeiro número: '))
    y = float(input('Digite o segundo número: '))
    if x > y:
        print(f'{x} - {y} é: {x - y}\nFim de programa!')
    else:
        print(f'{y} - {x} é: {y - x}\nFim de programa!')
elif opcao == 3:
    x = float(input('Digite o primeiro número: '))
    y = float(input('Digite o segundo número: '))
    print(f'{x} x {y} = {x * y}\nFim de programa!')
elif opcao == 4:
    x = float(input('Digite o primeiro número: '))
    y = float(input('Digite o segundo número: '))
    if y != 0:
        print(f'{x} % {y} é: {x / y}\nFim de programa!')
    else:
        print('Denominador inválido!')
else:
    print('Opção incorreta!')