"""
Funções com retorno


Testes
numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print {ret_pr}')


OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é None

OBS: Funções Python que retornam valores, devem retornar estes valores com a palavra reservada return

OBS: Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos passar
a execução da função para outras funções.


# Vamos "refatorar" esta função para que ela retorne um valor


def quadrado_de_7():
    return 7 * 7

# Criamos uma variável para receber o retorno da função
ret = quadrado_de_7()

print(f'Retorno de quadrado_de_7 {ret}')

print(f'Retorno mais 1: {quadrado_de_7() + 1}')

# Refatorando a primeira função

def diz_oi():
    return 'Oi!'

print(diz_oi())

OBS: Sobre a palavra reservada "return"
1 - Ela finaliza a função, ou seja, ela sai da execução da função;
# Exemplo 1

def diz_oi():
    print('EStou sendo executado antes do retorno')
    return "Oi!"
    print('Estou sendo executado após o retorno') # Essa linha nunca será executada pois o return já saiu da função

print(diz_oi())

2 - Podemos ter em uma função, diferentes "returns";
# Exemplo 2

def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;
# Exemplo 3

def outra_funcao():
    return 2, 3, 4, 5

# num1, num2, num3, num4 = outra_funcao()
# print(num1, num2, num3, num4)

print(outra_funcao())

_____
# Vamos crirar uma função para jogar a moeda (cara ou coroa)

from random import random

def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())




"""

# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação desnecessária

def eh_impar():
    numero = 61
    if numero % 2 != 0:
        return True
    # else -  Não ha necessidade nesse caso
    return False

print(eh_impar())