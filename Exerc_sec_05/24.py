import locale

locale.setlocale(locale.LC_ALL, 'pt_BR') # relativo ao valor em moeda decimal ({locale.currency("variável", grouping=True)})

print('TRIBUTAÇÃO')

valor = float(input('Digite o valor do produto: '))

estado = input('Digite um dos estados:\n1. MG (Minas Gerais).\n2. SP (São Paulo). \n3. RJ (Rio de Janeiro). \n4. MS (Mato Grosso do Sul).\n')

if estado == '1' or estado == 'MG' or estado == 'mg':
    print(f'A alíquota para MG é de 7%.\nValor do tributo: R$ {locale.currency(((valor*7)/100), grouping=True)}')
elif estado == '2' or estado == 'SP' or estado == 'sp':
    print(f'A alíquota para SP é de 12%.\nValor do tributo: R$ {locale.currency(((valor*12)/100), grouping=True)}')
elif estado == '3' or estado == 'RJ' or estado == 'rj':
    print(f'A alíquota para RJ é de 15%.\nValor do tributo: R$ {locale.currency(((valor*15)/100), grouping=True)}')
elif estado == '4' or estado == 'MS' or estado == 'ms':
    print(f'A alíquota para MG é de 8%.\nValor do tributo: R$ {locale.currency(((valor*8)/100), grouping=True)}')
else:
    print('Digite uma opção válida!')

