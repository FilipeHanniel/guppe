print('Digite dois números inteiros!')

x = int(input())
y = int(input())

if x > y and x != y:
    print(f'O maior deles {x}!\nA diferença entre {x} e {y} é: ', x - y)
elif x < y:
    print(f'O maior deles é {y}!\nA diferença entre {y} e {x} é:', y - x)
else:
    print(f'Os números {x} e {y} são iguais!!!')