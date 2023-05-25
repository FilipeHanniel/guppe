"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais;
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreender todo o programa.

2 - Variáveis locais;
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas.

Para declarar variáveis em Python fazemos:

nome_da_variável = valor_da_variável

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nós
não colocamos o tip de dado dela. Este tipo é inferido ao atribuírmos o valor a mesma.

Exmeplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;
"""

# Exemplo
numero = 42
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

nao_existo = 0j
print(nao_existo)
print(type(nao_existo))

numero = 3

if numero > 10:
    novo = numero + 10 # A variável 'novo' está declarada localmente dentro do bloco do 'if' portanto é local
    print(novo)

print(novo)
