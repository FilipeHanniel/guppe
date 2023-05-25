import math

print('Digite um número real positivo')

x = float(input())

if x >= 0:
    print(f'O número {x} ao quadrado é: ', x * x,f'\nA raíz quadrada de {x} é', math.sqrt(x))
else:
    print(f'O número digitado é negativo!!!')
