print('PRESTAÇÃO DE UM EMPRÉSTIMO')
sal = float(input('Digite o salário do trabalhador '))

prest = float(input('Digite o valor da pretação '))

if sal * (0.2) >= prest:
    print('Empréstimo Concedido!')
else:
    print('Empréstimo negado!')
