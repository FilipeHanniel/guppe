"""
Modulo Collections - Default Dict

https://docs.python.org/3/library/collections.html#defaultdict-objects

Recaptulação Dicionários
dicionario = {'curso': 'Programação em Python: Essencial'}

print(dicionario)

print(dicionario['curso'])

print(dicionario['outro']) # Gera um KeyError

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Esse valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será criada
e o valor default será atribuído.

OBS: Lambdas são funões sem nome que podem ou não receber parâmetros de entrada e retornar
valores.
__



"""

# Fazendo o import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)

dicionario['curso'] = 'Programação em Python: Essencial.'

print(dicionario)

print(dicionario['outro'])    # KeyError no dicionario comum, mas aqui não.

print(dicionario)
