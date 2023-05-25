import random

print('PROVA DE MATEMÁTICA - SOMA\n\n')
pergunta1 = 0
pergunta2 = 0
pergunta3 = 0
pergunta4 = 0
pergunta5 = 0
xperg1 = 0
xperg2 = 0
xperg3 = 0
xperg4 = 0
xperg5 = 0
yperg1 = 0
yperg2 = 0
yperg3 = 0
yperg4 = 0
yperg5 = 0
total = int(0)
x = random.randint(1, 101)
y = random.randint(1, 101)
soma = (x + y)
res = int(input(f'Qual o resultado da soma {x} + {y} = '))
if res == soma:
    total = total + 1
    pergunta1 = x + y
    xperg1 = x
    yperg1 = y

x = random.randint(1, 101)
y = random.randint(1, 101)
res = int(input(f'Qual o resultado da soma {x} + {y} = '))
if res == (x + y):
    total = total + 1
    pergunta2 = x + y
    xperg2 = x
    yperg2 = y

x = random.randint(1, 101)
y = random.randint(1, 101)
res = int(input(f'Qual o resultado da soma {x} + {y} = '))
if res == (x + y):
    total = total + 1
    pergunta3 = x + y
    xperg3 = x
    yperg3 = y

x = random.randint(1, 101)
y = random.randint(1, 101)
res = int(input(f'Qual o resultado da soma {x} + {y} = '))
if res == (x + y):
    total = total + 1
    pergunta4 = x + y
    xperg4 = x
    yperg4 = y

x = random.randint(1, 101)
y = random.randint(1, 101)
res = int(input(f'Qual o resultado da soma {x} + {y} = '))
if res == (x + y):
    total = total + 1
    pergunta5 = x + y
    xperg5 = x
    yperg5 = y

print(f'\n\nO número de acertos foi {total} de 5 questões!')

print('Essas questões estão corretas! Parabéns!!!')
if pergunta1 != 0:
    print(f'{xperg1} + {yperg1} = {pergunta1}')
if pergunta2 != 0:
    print(f'{xperg2} + {yperg2} = {pergunta2}')
if pergunta3 != 0:
    print(f'{xperg3} + {yperg3} = {pergunta3}')
if pergunta4 != 0:
    print(f'{xperg4} + {yperg4} = {pergunta4}')
if pergunta5 != 0:
    print(f'{xperg5} + {yperg5} = {pergunta5}')