import math

print(f'Digite um número real: ')

x = float(input())

if x >= 0:
    print(f'A raíz quadrada de {x} é:   ', math.sqrt(x))
else:
    print(f'O número {x} elevado ao quadrado é:  ', x * x)
