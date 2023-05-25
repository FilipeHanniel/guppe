print('ÍNDICE DE MASSA CORPORAL\n')

sexo = input('Digite M para o sexo masculino ou \nF para o sexo feminino: ')

h = float(input('Digite a altura do paciente: '))

if sexo == 'M' or 'm':
    print(f'O Peso ideal é: {(72.7*h) -58} kg')
elif sexo == 'F' or 'f':
    print(f'O peso ideal é {(62.1*h) -44.7} kg')
else:
    print('O parâmetro indicado para o sexo está incorreto!')