from decimal import Decimal
import locale
# As funções acima foram chamadas para conseguir imprimir o valor em forma monetária
locale.setlocale(locale.LC_ALL, 'pt_BR') # relativo ao valor em moeda decimal

print('Bem vindo trabalhador\nPor gentileza, digite o número de dias trabalhados:')

x = input() # nº de dias trabalhados

x = float(x)

bruto = 30 * x

total = bruto - ((bruto * 8) / 100)

# total = Decimal(total)

print(f'O valor total a receber será de {locale.currency(total, grouping=True)}')
