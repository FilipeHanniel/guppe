print('QUAL É O MAIOR?')

n = int(input('Digite a quantidade de números que será digitada: '))
print('\n')

valor = 0
valorinicial = 0
maior = 0
somamaior = 0

if n > 0:
    for i in range(n):
        valor = float(input(f'Digite o valor {i+1} de {n}: '))
        if i == 0:
            valorinicial = valor
            somamaior = somamaior + 1
        elif i == 1:
            if valor >= valorinicial:
                maior = valor
                somamaior = somamaior + 1
            else:
                maior = valorinicial
                somamaior = somamaior + 1
        else:
            if valor > maior:
                maior = valor
                somamaior = somamaior + 1

print(f'O valor maior é {maior}')
print(f'Esse valor ocorreu {somamaior} vezes')
