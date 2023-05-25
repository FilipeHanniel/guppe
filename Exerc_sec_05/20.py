print('TRIÂNGULO')

a = float(input('Digite o valor do lado A: '))
b = float(input('Digite o valor do lado B: '))
c = float(input('Digite o valor do lado C: '))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b and a == c:
        print('Triângulo EQUILÁTERO')
    elif a == b or a == c or b == c:
        print('Triângulo ISÓCELES')
    else:
        print('Triângulo ESCALENO')
else:
    print('VALORES INVÁLIDOS!\nA soma de dois lados deve ser sempre maior que o outro lado!')