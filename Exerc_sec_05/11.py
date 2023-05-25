print('Digite um número Inteiro positivo diferente de zero:\n')

x = int(input())

if x > 0:
    x = str(x)
    lista = (list(x))
    lista = [int(val) for val in lista] # Cada elemento da lista é uma string que está sendo convertida em inteiro.
    print(lista)
    soma = sum(lista) # Essa função soma cada elemento da lista (Necessário serem números).
    print(soma)
else:
    print('Número inválido!')
