print('NUMEROS INTEIRO POSITIVOS PARES - DECRESCENTE')

n = int(input('Digite um valor inteiro e positivo par: '))

if n > 0 and (n % 2 == 0):
    for i in range(n, -1, -2):
        print(i)
else:
    print('VALOR INVÁLIDO!')