from decimal import Decimal
import locale
# As funções acima foram chamadas para conseguir imprimir o valor em forma monetária
locale.setlocale(locale.LC_ALL, 'pt_BR') # relativo ao valor em moeda decimal

print('Olá vendedor, digite o total vendido:')

total = input()
total = Decimal(total)

print(f'O total a ser pago com desconto de 10% é: R$ {locale.currency(((total * 90)/100), grouping=True)}\n')

print(f'Para o parcelamento em 3x sem juros no valor total teremos o valor de cada parcela de R$ {locale.currency((total / 3), grouping=True)}\n')

print(f'Para compra à vista temos o desconto de 5%. Valor com desconto R$ {locale.currency(((total * 95) / 100),)}')