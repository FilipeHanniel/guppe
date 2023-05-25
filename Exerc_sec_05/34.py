print('--- CONCEITO DO ALUNO ---\n\n')

nota = float(input('Digite a nota do aluno: '))
falta = int(input('Digite a quantidade de faltas do aluno: '))

if (nota >= 0) and (nota <= 10):
    if (nota >= 9) and (nota <= 10):
        if falta <= 20:
            print('CONCEITO "A"')
        else:
            print('CONCEITO "B"')
    elif (nota >= 7.5) and (nota < 9):
        if falta <= 20:
            print('CONCEITO "B"')
        else:
            print('CONCEITO "C"')
    elif (nota >= 5) and (nota < 7.5):
        if falta <= 20:
            print('CONCEITO "C"')
        else:
            print('CONCEITO "D"')
    elif (nota >= 4) and (nota < 5):
        if falta <= 20:
            print('CONCEITO "D"')
        else:
            print('CONCEITO "E"')
    elif (nota >= 0) and (nota < 4):
        if falta <= 20:
            print('CONCEITO "E"')
        else:
            print('CONCEITO "F"')
else:
    print('Nota inválida!')
