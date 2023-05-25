print('SOMA DOS DIVISORES')

n = int(input('Digite um número inteiro positivo: '))
soma = 0

if n > 0:
    for i in range(1, n):
        if n % i == 0:
            soma = soma + i
else:
    print('valor inválido!')

print(soma)
