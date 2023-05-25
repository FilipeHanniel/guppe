"""
Modulo Collections: Ordered Dict

https://docs.python.org/3/library/collections.html#collections.OrderedDict 

# Em um dicionario, a ordem de inserção dos elemsntos não é garantida.
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }

for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')


___
OrderedDict -> É um dicionário que nos garante a ordem de inserção dos elemsntos.

# Fazendo o Import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 })

for chave, valor in dicionario.items():
    print(f'chava={chave}: valor={valor}')

__

"""

# Entendendo a diferença entre Dict e Ordered Dict

# Dicionários comuns:

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)

# Ordered Dict:

from collections import OrderedDict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)    # False, já que a ordem dos elementos importam para o OrderecDict

