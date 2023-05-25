print('Digite dois números reais:')

x = float(input())
y = float(input())

if x > y and x != y:
    print(f'O número {x} é maior que {y}!')
elif x == y:
    print('NÚMEROS IGUAIS!!!')
else:
    print(f'O número {y} é maior que {x}')


