print('PAR OU ÍMPAR')

total = 0
par = 0
valor = float(input('Digite um valor: '))

while valor != 1000:
    if (valor % 2) == 0:
        print('Esse número é par!\nDigite "1000" para encerrar!')
        par = par + 1
        total = total + 1
    else:
        print('Esse número é ímpar!\nDigite "1000" para encerrar!')
        total = total + 1
    valor = float(input('Digite um valor: '))

print(f'O total de números digitados foi {total}\nO total de números pares digitados foi {par}')
print('PROGRAMA ENCERRADO!')