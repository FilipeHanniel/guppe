print('NUMEROS NATURAIS - ORDEM DESCRESCENTE')

n = int(input('Digite um valor positivo para "N": '))

for i in range(n, -1, -1): # Aqui na função 'range' delimitamos start em n, stop em -1(para em 0) e step = -1(regressivo)
    print(i)
