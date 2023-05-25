print('CONSUMO')

km = float(input('Digite a distância em Km: '))
l = float(input('Digite a quantidade de litros consumida: '))

consumo = km / l

if consumo < 8:
    print('VENDA O CARRO!')
elif consumo >=8 and consumo < 12:
    print('ECONÔMICO!')
elif consumo >= 12:
    print('SUPER ECONÔMICO!!!')
