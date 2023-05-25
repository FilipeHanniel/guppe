print('INTERVALO DE PARES')

x = int(input('Digite dois números: \n'))
y = int(input())
soma = 0
mult = 1

for i in range(x, y + 1):
    if i % 2 == 0:
        soma = soma + x

for i in range(x, y + 1):
    if i % 2 != 0:
        mult = mult * i

print(f'A soma dos números pares no intervalo de {x} até {y} é: \n{soma}.\nA multiplicação dos ímpares é: \n{mult}')