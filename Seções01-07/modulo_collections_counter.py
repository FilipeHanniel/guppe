"""
Módulo Collections - Counter (contador)

Collections -> High-performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um
dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de ocorrências
desse elemento.


___
# Realizando o import

# Utilizando o Counter

from collections import Counter

# Exemplo 01

# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 45, 45, 66, 66, 43, 34, 1254, 1024]

# Utilizando o Counter
res = Counter(lista)
print(res)
print(type(res))

# Counter({1: 5, 2: 4, 3: 4, 4: 3, 5: 2, 45: 2, 66: 2, 43: 1, 34: 1, 1254: 1, 1024: 1})
# Veja que para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências.
__
# Exemplo 2

print(Counter('Geek University'))

# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

__

"""
from collections import Counter

# Exemplo 3

texto = """Uma ressalva inicial. As desigualdades e os mecanismos de exploração dos recursos dos países mais pobres não 
chegaram ao fim desde que Rodney se tornou uma espécie de mártir da negritude de esquerda. Mas as mudanças que deram 
uma cara nova às relações internacionais não foram aquelas que o militante guianês esperava."""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as cinco palavras com mais ocorrência no texto
print(res.most_common(10))
