"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICOS e também de poder colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens, se você criar um array do tipo int e com tamanho 5, este array será
    SEMPRE do tipo inteiro e poderá ter SEMPRE, no máximo 5 valores.

Já em Python:

- Dinâmico: Não possui tamanho fixo; Ou seja, podemos criar a lista e simplismente ir adicionando elementos;
- Qualquer tipo de dado: As listas não possuem tipo de dado fixo; ou seja, podemos colocar qualquer tipo de dado.

As listas em Python são representadas por colchetes: []


type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek Univ')



# Podemos facilmente checar se determinado valor está contido na lista

num = 18
if num in lista4:
    print(f"Encontrei o número {num}")
else:
    print(f"Não encontrei o número {num}")

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista

print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas


Para adicionar elementos em listas, utilizamos a função append

OBS: Com append, nós só conseguimos adicionar um elemento por vez


print(lista1)
lista1.append(42)
print(lista1)

lista1.append([8, 3, 1]) # Insere a lista como elemento único
print(lista1)

lista1.append('a')
print(lista1)

if [8,3,1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67]) # Insere cada elemento da lista como valor adicional
print(lista1)

# Podemos inserir um novo elemento na lista, informando a posição do índice
# OBS: Isso não substitui o valor inicial; o mesmo será deslocado para a "direita" da lista

lista1.insert(2, 'Novo Valor')
print(lista1)

# Podemos facilmente juntar duas listas

# lista6 = lista1 + lista2
# lista1 = lista1 + lista2
lista1.extend(lista2)
print(lista1)
__
# Podemos facilmente inverter uma lista utilizando o reverse()
# lista1.reverse()
# lista2.reverse()

print(lista1[::-1]) # O slice faz o mesmo processo do reverse
print(lista2)
__
# Copiar uma lista

lista6 = lista2.copy()
print(lista6)
__
# Contar quantidade de elementos de uma lista

print(len(lista5))
__
# Podemos remover facilmente o último elemento de uma lista
# O "pop" não somente remove o último elemento mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice.
# OBS: Os elementos à direita deste índice são deslocados para a esquerda.
# OBS: Se não tiver o elemento no índice informado, teremos um erro IndexError
lista5.pop(2)
print(lista5)
__
# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

__
# Podemos repetir elementos em uma lista
nova = [1,2,3]
nova = nova * 3
print(nova)
__
# Podemos converter uma string para uma lista

# Exemplo 01
curso = 'Programação em Python essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão o split() separa os elementos da lista pelo espaço entre elas.

# Exemplo 02
curso = 'Programação,em,Python,essencial'
print(curso)
curso = curso.split(',')
print(curso)

__
# Convertendo uma lista em uma string

lista6 = ['Programação', 'em', 'Python']
print(lista6)
# Abaixo estamos dizendo: pegue a lista6, coloque espaço entre cada elemento e transforme em uma string
curso = ' '.join(lista6)   # Poderia ter sido usado apenas a variável 'lista6' sem problemas.
print(curso)
# Abaixo estamos dizendo: pegue o underline e coloque entre cada elemento transformando em uma string
curso = '_'.join(lista6)
print(curso)

__
lista6 = [1, 2.34, True, 'Geek', 'd', [1,2,3], 938320921]

print(lista6)
print(type(lista6))

__
# Iterando sobre uma lista

# Exemplo 01 -  Utilizando for

soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 02 -  Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print('Adicione um produto na lista ou digite "sair" para sair.')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

__
# Utilizando variáveis em listas

numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

__
# Fazemos acesso aos elementos de forma indexada;
# Para entender melhor o índice negativo, pensa na lista como um círculo;

#            0        1         2         3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[2])
print(cores[-1]) #branco
print(cores[-2]) #azul
# print(cores[-5]) #ERRO, pois não existe o índice '-5'

__
for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice =  indice + 1

__
# Gerar índice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

__
# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)

print(lista)

__
# Métodos não tão importantes mas também úteis

# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

print(numeros.index(6)) # Em qual índice está o valor '6'
print(numeros.index(9)) # Em qual indice está o valor '9'

# OBS: Caso não tenha este elemento na lista, será apresentado erro
# print(numeros.index(19))

print(numeros.index(5)) # Retorna o índice do primeiro elemento encontrado, ainda que haja mais de um elemento na lista

# Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar;
print(numeros.index(5, 1)) # buscando a partir do indice 1
print(numeros.index(5, 2)) # buscando a partir do indice 2
print(numeros.index(5, 3)) # buscando a partir do indice 3

# ERRO print(numeros.index(5, 4)) # buscando a partir do indice 4 #ERRO!!!
# Se não for encontrado retornará VALUE ERROR.

# Podemos fazer busca dentro de um range, inicio/fim;
# print(numeros.index(8, 6, 8)) # buscar o indice do valor 8 entre os indices 6 e 8 - ERROR - Não existe
print(numeros.index(8, 3, 6))

__
# Revisão do slicing

# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# Trabalhando com slicing de listas com o parâmetro 'inicio'

lista = [1, 2, 3, 4]
print(lista[1:]) #iniciando no indice 1 e indo até o final

# Trabalhando com slice de lista com o parâmetro 'fim'
print(lista[:2]) #Começa em zero e vai até o indice 2, excluindo-se o indice 2 (vai até o 1)

print(lista[:4]) #Começa em zero e vai até o indice 2, excluindo-se o indice 4 ( vai até o 3)

print(lista[1:3]) #começa no indice 1 e vai até o 3, excluindo-se o 3 (vai até o 2)

# Trabalhando com slice de lista com o parâmetro 'passo':

print(lista[1::2]) # começa em 1 e vai até o final de 2 em 2

print(lista[::2]) # começa em zero e vai ate o fim de 2 em 2

print(lista[::-1])

__
# Invertendo valores em uma lista

nomes = ['Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)
nomes.reverse()
print(nomes)

__
# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho*
# * Se os valores forem todos inteiros ou reais.

lista = list(range(6))

print(lista)
print(sum(lista)) #soma
print(max(lista))
print(min(lista))
print(len(lista))

__
# Transformar uma lista em TUPLA

lista = list(range(6))
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

__
# Desempacotamento de listas

lista = [1, 2, 3]

num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)

# Se tivermos mais elementos para desempacotar do que variáveis para receber os valores, teremos Value Error;
# O mesmo ococrre se tivermos mais variáveis do que elementos na lista;

__
# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma1 (DEEP COPY)

lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas ficaram totalmente
#independentes, ou seja, modificando uma lista não afeta a outra, isto em Python é chamado de DEEP COPY, ou Cópia
#profunda.

# Forma2 (SHALLOW COPY)

lista = [1, 2, 3]
print(lista)

nova = lista # também é uma cópia

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a copia via atribuição e copiamos os dados da lista para a nova lista, mas
#após realizar a modificação em uma das listas, essa modificação se refletiu em ambas as listas.
# Isso em Python é chamado de SHALLOW COPY.
"""


