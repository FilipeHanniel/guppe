print('--- AUMENTO ---\n\n')

valor = float(input('Digite o preço do produto para a correção do valor: '))

if (valor >= 0) and (valor <= 50):
    valor = valor + valor * 5/100
    if valor <= 80:
        print(f'O novo valor do produto é de R$ {valor} reais!\nBARATO!!!')
    elif (valor > 80) and (valor <= 120):
        print(f'O novo valor do produto é de R$ {valor} reais!\nNORMAL.')
    elif (valor > 120) and (valor <= 200):
        print(f'O novo valor do produto é de R$ {valor} reais!\nCARO!!.')
    elif valor > 200:
        print(f'O novo valor do produto é de R$ {valor} reais!\nMUITO CARO!!!.')
elif (valor > 50) and (valor <= 100):
    valor = valor + valor * 10 / 100
    if valor <= 80:
        print(f'O novo valor do produto é de R$ {valor} reais!\nBARATO!!!')
    elif (valor > 80) and (valor <= 120):
        print(f'O novo valor do produto é de R$ {valor} reais!\nNORMAL.')
    elif (valor > 120) and (valor <= 200):
        print(f'O novo valor do produto é de R$ {valor} reais!\nCARO!!.')
    elif valor > 200:
        print(f'O novo valor do produto é de R$ {valor} reais!\nMUITO CARO!!!.')
elif valor > 100:
    valor = valor + valor * 15 / 100
    if valor <= 80:
        print(f'O novo valor do produto é de R$ {valor} reais!\nBARATO!!!')
    elif (valor > 80) and (valor <= 120):
        print(f'O novo valor do produto é de R$ {valor} reais!\nNORMAL.')
    elif (valor > 120) and (valor <= 200):
        print(f'O novo valor do produto é de R$ {valor} reais!\nCARO!!.')
    elif valor > 200:
        print(f'O novo valor do produto é de R$ {valor} reais!\nMUITO CARO!!!.')
else:
    print('Valor inválido!')
