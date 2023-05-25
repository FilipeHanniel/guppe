import math
print('EQUAÇÃO DO 2º GRAU')

print('ax² + bx + c = 0')

a = float(input('Digite o valor de "a": '))
b = float(input('Digite o valor de "b": '))
c = float(input('Digite o valor de "c": '))

delta = b*b - (4*a*c)
x1 = (-b + math.sqrt(delta))/2 * a
x2 = (-b - math.sqrt(delta))/2 * a

if a != 0 and delta > 0:
    print(f'As raízes da equação {a}x² + {b}x + {c} = 0 são:\nX1 = {x1}\nX2 = {x2}\nFim do programa!')
elif a != 0 and delta < 0:
    print('NÃO EXISTE RAIZ!\nFim do programa!')
elif a != 0 and delta == 0:
    print(f'Existe apenas uma raíz real para a equação {a}x² + {b}x + {c} = 0\n X = {x1}')
else:
    print('Não é equação do segundo grau! "a" deve ser diferente de zero!!!\nFim do programa!')