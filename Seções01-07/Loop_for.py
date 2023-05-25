"""
Estruturas de Repetição

Loop for

Loop -> Estrutura de repetição
for -> Umas dessas estruturas

C ou Java
for(int i = 0 < limitador; i++){
    //execução do loop
}

Python

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
-String
    nome = 'Geek University'
-Lista
    lista = [1, 3, 4, 5]
-Range
    numeros = range(1,10)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)    # temos que transformar em uma lista

#Exemplo de for 1 (iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (iterando sobre um range)
for numero in range(1,10):
    print(numero)

range(valor_inicial, valor_final)

OBS: O valor final não é inclusive

"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)    # temos que transformar em uma lista


"""
Enumerate:

for indice, letra in enumerate(nome):
    print(nome[indice])
    
for indice, letra in enumerate(nome):
    print(letra)
    
for _, letra in enumerate(nome):   #OBS: Quando não precisamos de um valor podemos descartá-lo utilizando um "underline" _
    print(letra)

for valor in enumerate(nome):
    print(valor)
    
for valor in enumerate(nome):
    print(valor[0])
    
((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '))
"""



"""
qtd = int(input('Quantas vezes esse loop deve rodar'))

for n in range(1, qtd):
    print(f'Imprimindo {n+1}')
    
    
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor:'))
    soma = soma + num
print(f'A soma é {soma}')   

nome = 'Geek University'
for letra in nome:
    print(letra, end='') 
"""

# Original: U+1F60D
# Modificado: U0001F60D


for x in range(3):
    for num in range (1,10):
        print('\U0001F60D' * num)

