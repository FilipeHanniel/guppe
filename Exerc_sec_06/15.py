print('NUMEROS INTEIRO POSITIVOS IMPARES - CRESCENTE')

n = int(input('Digite um valor inteiro e positivo ímpar: '))

if n > 0 and (n % 2 == 1):
    for i in range(1, n + 1, 2):
        print(i)
else:
    print('VALOR INVÁLIDO!')