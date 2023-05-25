print('SEQUÊNCIAS')

n = int(input('Digite o valor de "N" para calcular as sequências: '))

s1 = 0
s2 = 0
s3 = 0

for i in range(1, n + 1):
    s1 = s1 + i

for i in range(1, n + 1):
    s2 = (((2 * i) - 1) - (i ** 2)) + s2

for i in range(1, n + 1):
    s3 = s3 + ((2 * i) - 1)

print(s1, s2, s3)
