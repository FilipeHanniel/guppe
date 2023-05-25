print('MÉDIA PONDERADA.\nA nota deverá estar entre 0 e 10')

n1 = float(input('Digite a nota N1: '))
n2 = float(input('Digite a nota N2: '))
n3 = float(input('Digite a nota N3: '))

print('As notas N1 e N2 possuem peso "1".')
print('A nota N3 possui peso "2".')

m = (n1 + n2 + (2*n3))/4

if m >= 6:
    print(f'A média do aluno é: {m}\nAluno aprovado!\nPARABÉNS!!!')
else:
    print(f'A média do aluno é {m}\nAluno reprovado!')
