import math

print(f'Digite um numero real:')

x = float(input())

if x >= 0:
    print(f'A raíz quadrada de {x} é: ', math.sqrt(x))
else:
    print(f'O número fornecido é inválido!')

# Outra forma de calcular seria usando a estrutura de repetição, mas como não é o propósito da seção fiz com IF