"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:
entrada -> processamento -> saída

se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída.

___

# Refatorando uma função

def quadrado_de_7():
    return 7 * 7

print(quadrado_de_7())
print(quadrado_de_7())
print(quadrado_de_7())

def quadrado(numero): # Essa função recebe um parâmetro
    # return numero * numero
    return numero ** 2

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)

print(ret)

print(quadrado()) #TypeError

___

# Refatorando a função

def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva ao aniversariante!!!')

def cantar_parabens(aniversariante):
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o/a {aniversariante}!!!')

cantar_parabens('Marcos')

___

# OBS: Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada
# função quantos parâmetros forem necessários. Eles são separados por vírgula.

# Exemplo

def soma(a,b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return(num1 * b) * msg

print(soma(2, 5))
print(soma(10,20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Geek '))
print(outra(5, 4, 'Python '))

# OBS: Se a gente informar um número errado de parâmetro ou argumentos, teremos TypeError

# print(soma(2, 3, 5)) # TypeError - Passando argumentos a mais
# print(soma(4)) # TypeError - Passando arguemntos a menos

___
# Nomeando parâmetros

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Angelina', 'Jolie'))

# A diferença entre Parâmetros e Argumentos

# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função.

# A ordem dos parâmetros importa!

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(nome, sobrenome))

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos
# utilizar qualquer ordem.

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Maques', nome='Marcia'))

___

"""

# Erro comum na utilização do return
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total # Lembrando que o return finaliza a função!

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))