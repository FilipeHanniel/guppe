print('Soma sobre fatoriais')

n = int(input('Digite um valor inteiro e positivo: \n'))
s = 2
fat = 1

if n > 0:
    for i in range(2, n + 1):
        while i > 1:
            fat = i * fat
            i = i - 1

    s = s + 1/fat
else:
    print('valor inválido')

print(s)
