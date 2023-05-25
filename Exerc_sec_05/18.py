print('CALCULADORA BÁSICA.\n')

op = input('Digite a operação desejada:\n"+" soma\n"-" subtração\n"/" divisão\n"*" multiplicação\n')

if op == '+':
    x = float(input('Digite o primeiro valor: '))
    y = float(input('Digite o segundo valor: '))
    print(f'\n{x} mais {y} é: {x + y}')
elif op == '-':
    x = float(input('Digite o primeiro valor: '))
    y = float(input('Digite o segundo valor: '))
    print(f'\n{x} menos {y} é: {x - y}')
elif op == '/':
    x = float(input('Digite o primeiro valor: '))
    y = float(input('Digite o segundo valor: '))
    if y != 0:
        print(f'\n{x} dividido por {y} é: {x / y}')
    else:
        print('Não é possível dividir por zero!')
elif op == '*':
    x = float(input('Digite o primeiro valor: '))
    y = float(input('Digite o segundo valor: '))
    print(f'\n{x} vezes {y} é: {x * y}')
else:
    print('OPERADOR INVÁLIDO!')
