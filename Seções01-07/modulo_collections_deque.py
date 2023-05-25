"""
Módulo Collections - Deque

https://docs.python.org/3/library/collections.html#collections.deque

Podemos dizer que o deque é uma lista de alta performance.

"""

# Importação
from collections import deque

# Criando deques

deq = deque('geek')

print(deq)
print(type(deq))

# Adicionando elementos no deque

deq.append('y')    # adiciona no final

print(deq)

deq.appendleft('k')    # adiciona no começo da lista
print(deq)

# Removendo elementos

print(deq.pop())    # remove e retorna o último elemento

print(deq)

print(deq.popleft())    # remove e retorna o primeiro elemento
print(deq)