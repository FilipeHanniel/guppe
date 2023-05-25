print('MAIOR E MENOR')

maior = 0
menor = 0
valorzero = 0
for i in range(10):
    x = float(input('Digite um valor: '))
    if i == 0:
        valorzero = x
    if i == 2:
        if valorzero < x:
            maior = x
            menor = valorzero
    else:
        if x > maior:
            maior = x
        elif x < menor:
            menor = x

print(f'O maior valor é: {maior}')
print(f'O menor valor é {menor}')



