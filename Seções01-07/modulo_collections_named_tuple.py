"""
Módulo Collections - Named Tuple

https://docs.python.org/3/library/collections.html#collections.namedtuple

# Recaptulação Tupla
tupla = (1, 2, 3)
print(tupla[1])

Named Tuple -> São tuplas diferenciadas onde especificamos um nome para a mesma e também parâmetros.

"""

# Importando

from collections import namedtuple

# Precisamos definir o nome e parâmetros.

# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raça nome')

# Forma 2 - Declaração Named Tuple

cachorro =  namedtuple('cachorro', 'idade, raça, nome')

# Forma 3 -

cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])

# Usando

ray = cachorro(idade=2, raça='chow-chow', nome='ray')

print(ray)
print(type(ray))

# Acessando os dados

# forma 01

print(ray[0])    # idade
print(ray[1])    # raça

# forma 02

print(ray.idade)    #idade

print(ray.raça)     #raça


print(ray.index('chow-chow'))
print(ray.count('chow-chow'))