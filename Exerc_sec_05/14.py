print('MÉDIA DO ALUNO\nDigite a nota do aluno entre 0 e 10 para cada trabalho\n')

n1 = float(input('Nota do TRABALHO DE LABORATÓRIO: '))
n2 = float(input('Nota da AVALIAÇÃO SEMESTRAL: '))
n3 = float(input('Nota do EXAME FINAL: '))

m = ((n1*2) + (n2*3) + (n3*5)) / 10

if m >= 0 and m <= 2.9:
    print(f'A média do aluno é {m}\nAluno REPROVADO! ')
elif m > 2.9 and m <= 4.9:
    print(f'A média do aluno é {m}\nAluno em RECUPERAÇÃO!')
else:
    print(f'A média do aluno é {m}\nAluno APROVADO!!!')





