import locale

locale.setlocale(locale.LC_ALL, 'pt_BR') # relativo ao valor em moeda decimal ({locale.currency("variável", grouping=True)})
print('=== COMISSÃO ===')

venda = float(input('Digite o valor da venda: R$ '))

if (venda > 0) and (venda < 20000):
    print(f'\n\nCOMISSÃO DO VENDEDOR -> R${locale.currency((400 + venda * 14/100), grouping=True)}')
elif (venda >= 20000) and (venda < 40000):
    print(f'\n\nCOMISSÃO DO VENDEDOR -> R${locale.currency((500 + venda * 14 / 100), grouping=True)}')
elif (venda >= 40000) and (venda < 60000):
    print(f'\n\nCOMISSÃO DO VENDEDOR -> {locale.currency((550 + venda * 14 / 100), grouping=True)}')
elif (venda >= 60000) and (venda < 80000):
    print(f'\n\nCOMISSÃO DO VENDEDOR -> {locale.currency((600 + venda * 14 / 100), grouping=True)}')
elif (venda >= 80000) and (venda < 100000):
    print(f'\n\nCOMISSÃO DO VENDEDOR -> {locale.currency((650 + venda * 14 / 100), grouping=True)}')
elif venda > 100000:
    print(f'\n\nCOMISSÃO DO VENDEDOR -> {locale.currency((700 + venda * 16 / 100), grouping=True)}')
