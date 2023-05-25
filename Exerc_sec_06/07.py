print('MEDIA DE POSITIVOS')

soma = 0
neg = 0 #Esse contador receberá o número de vezes que um número não positivo foi adicionado
for i in range(10):
    num = int(input('Digite um número inteiro: '))
    if num >= 0:
        soma = num + soma
        neg = neg + 1

print(f'A média dos valores é: {soma / (10 - neg)}')