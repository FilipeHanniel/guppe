"""
Estruturas Lógicas: and, or, not, is

Operadores unários:
    - not
Operadores binários:
    - and, or, is

Regras de funcionamento:
Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True vira False, se for False vira True
Pra o 'is', o valor é comparado com um segundo
"""

ativo = False
logado = False

if not ativo:
    print('Você precisa ativar sua conta, Por favor cheque seu e-mail')
else:
    print('Bem vindo usuário')

print(not True)

if logado is False:
    print('Você precisa ativar sua conta, Por favor cheque seu e-mail')
else:
    print('Bem vindo usuário')

if ativo:
    print('Bem vindo usuário')
else:
    print('Você precisa ativar sua conta, Por favor cheque seu e-mail')

print(ativo is True)