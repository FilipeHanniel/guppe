"""
Tipo Float

Tipo real, decimal

São separados por ponto e não por vírgula
"""

# Errado do ponto de vista do float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))

# Certo
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1.44, 2.33
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Conversão de float em inteiro
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
valor3 = 5j
print(valor3)
print(type(valor3))
