print('SOMA DOS N PRIMEIROS NUMEROS NATURAIS')

n = int(input('Digite um valor inteiro positivo para "N": '))
soma = 0

if n > 0 and (n % 2 == 0):
    for i in range(n + 1):
        soma = i + soma
    print(soma)
else:
    print('VALOR INVÁLIDO!')

