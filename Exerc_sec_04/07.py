print('Digite a temperatura em Graus Fahrenheit:')

temper = input()

temper = float(temper)

cel = (5 * (temper - 32)) / 9

print(f'A temperatura de {temper}º graus  Fahrenheit equivale a {cel}º graus Celsius')