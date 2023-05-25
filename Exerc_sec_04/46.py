print('Digite um número com 3 dígitos:')

x = input()
i = x[::-1]


if len(x) == 3:
    print(i)
else:
    print('O número digitado não possui 3 dígitos, tente novamente.')