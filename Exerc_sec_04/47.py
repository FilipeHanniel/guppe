print('Digite um número inteiro de 4 dígitos:')

x = input()
lista = list(x)

print(lista)

if len(x) == 4:
    for elemento in lista:
        print(elemento)
else:
    print('o número digitado não possui 4 digitos!')
print('Fim do programa!')