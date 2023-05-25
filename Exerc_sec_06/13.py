print('NUMEROS INTEIRO POSITIVOS PARES')

n = int(input('Digite um valor inteiro e positivo: '))

if n > 0:
    for i in range(0, n + 1, 2):
        print(i)
else:
    print('VALOR INVÁLIDO!')