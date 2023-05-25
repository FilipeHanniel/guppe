print('Digite as notas N1 e N2 do aluno:')

n1 = float(input())
n2 = float(input())

if n1 >= 0 and n1 <= 10 and n2 >=0 and n2 <= 10:
    print(f'A média do aluno é: ', (n1 + n2) / 2)
else:
    print('Uma ou ambas as notas são inválidas!')
