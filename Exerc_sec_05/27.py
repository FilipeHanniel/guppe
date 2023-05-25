print('CLASSIFICAÇÃO DE NADADORES.')

idade = int(input('Digite a idade do nadador: '))

if idade < 5:
    print('Nadador não possui idade suficiente para competir!')
elif idade >= 5 and idade <=7:
    print('Categoria INFANTIL A')
elif idade >= 8 and idade <= 10:
    print('Categoria INFANTIL B')
elif idade >= 11 and idade <= 13:
    print('Categoria JUVENIL A')
elif idade >= 14 and idade <= 17:
    print('Categoria JUVENIL B')
elif idade >= 18:
    print('Categoria SÊNIOR!')
else:
    print('idade incompatível!')