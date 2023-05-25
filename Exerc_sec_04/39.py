from decimal import Decimal
import locale

# As funções acima foram chamadas para conseguir imprimir o valor em forma monetária

locale.setlocale(locale.LC_ALL, 'pt_BR')
print('Os ganhadores receberão a quantia total de R$ 780.000,00!')

x = 780000.00
x = Decimal(x)
print(locale.currency(x, grouping=True))


print(f'O primeiro ganhador receberá 46% do total, correspondendo a {locale.currency(((x * 46) / 100), grouping=True)}\n')

print(f'O segundo ganhador receberá 32% do total, correspondendo a {locale.currency(((x * 32) / 100), grouping=True)}\n')

print(f'O terceiro ganhador receberá o restante do prêmio, ou seja 22% do total, correspondendo a\n {locale.currency(((x * 22) / 100), grouping=True)}')