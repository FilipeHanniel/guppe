print('--- VERIFICAÇÃO DE DATA ---')

data = input('Digite a data desejada no formato (DD/MM/AAAA): ')
data = data.split('/')
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])

if (mes > 0) and (mes < 13) and (ano > 0) and (ano < 9999):
    if (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
        if (dia > 0) and (dia < 32):
            print('Data válida')
        else:
            print('Data Inválida! Esse mês possui 31 dias!')
    elif (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
        if (dia > 0) and (dia < 31):
            print('Data válida')
        else:
            print('Data Inválida! Esse mês possui 30 dias!')
    else:
        if ((ano % 400) == 0) or (((ano % 4) == 0) and ((ano % 100) != 0)):
            if (dia > 0) and (dia < 30):
                print('Data válida')
            else:
                print('Data inválida! Fevereiro possui apenas 29 dias pois o ano é bissexto!')
        else:
            if (dia > 0) and (dia < 29):
                print('Data válida')
            else:
                print('Data inválida! Fevereiro possui apenas 28 dias pois o ano não é bissexto!')
else:
    print('Data inválida!!!')
