print('MÉDIA DE NOTAS\n')

denominador = 0
soma = 0

while True:
    nota = int(input('Digite uma nota entre 10 e 20: \nUm valor inválido encerra o programa: \n'))
    if (nota >= 10) and (nota <= 20):
        soma = soma + nota
        denominador = denominador + 1
    else:
        break

print(f'A média do aluno é {soma/denominador}')
print('fim do programa!')