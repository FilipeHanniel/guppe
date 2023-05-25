"""
Dicionários

OBS: Em algumas linguagnes de programação os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por {} CHAVES.

print(type({}))

OBS: Sobre Dicionários
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;

__

# Criação de Dicionários

# Forma 1 (mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

print(paises['eua'])

# Forma 2 (menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

__
# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['py'])
# print(paises['ru]) - Caso tentemos fazer um acesso através de uma chave que não existe, teremos um KeyError.

# Forma 2 - Acessando via get -  Recomendado

print(paises.get('br'))
print(paises.get('ru'))  # Nesse caso, não existindo a chave o resultado será NONE, e não haverá erro no programa.

# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado KeyError

pais = paises.get('ru')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')


# Podemos definir um valor padrão para o caso de não encontrarmos o objeto ou a chave informada
pais = paises.get('br', 'Não encontrado')

print(f'Encontrei o país {pais}')

__
# Podemos verificar se determinada chave se encontra em um dicionário

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

__
# Podemos utilizar qualquer tipo de dado inclusive, lista, tupla, dicionário, como chaves de dicionários

# Tuplas são bastante interessantes em serem utilizadas com chaves de dicionários pois as mesmas são imutáveis
localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (35.7749, 122.4194): 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))

__
# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1
receita['abr'] = 350

print(receita)

# Forma 2

novo_dado = {'mai': 500}
receita.update(novo_dado)

print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 550

print(receita)

# Forma 2

receita.update({'mai': 600})

print(receita)

# Conclusão 1: A forma de adicionar novos elementos ou atualizar dados já existentes é a mesma.
# Conclusão 2: Em dicionários, NÃO podemos ter chaves repetidas.

__
# Remover dados de um dicionário
print(receita)
# Forma 1 (mais comum)
ret = receita.pop('mar')
print(ret)
print(receita)
# OBS1: Aqui precisamos sempre informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# OBS2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2

del receita['fev']
print(receita)

# del receita['fev'] - Se a chave não existir, será gerado um KeyError
# neste caso, o valor removido não é retornado

__

"""

# Imagine que você tem um comércio eletrônico onde temos um carrinho de compras na qual adicionamos produtos.
"""
Carrinho de Compras:
    Produto 1:
        -nome;
        -quantidade;
        -preço
    Produto 2:
        -nome;
        -quantidade;
        -preço


# 1 - Poderiamos utilizar uma lista para isso? Sim

carrinho = []

produto1 = ['playstation4', 1, 2300.00]
produto2 = ['God of War', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber qual é o índice de informação no produto

# 2 - Poderíamos utilizar uma tuplas para isso? Sim

produto1 = ('Playstation4', 1, 2300.00)
produto2 = ('God of War', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Teríamos que saber qual é o índice de informação no produto


# 3 - Poderíamos utilizar um DICIONARIO para isso? sim!

carrinho = []
produto1 = {'nome': 'Playstation4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God of War', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
#podemos ter a certeza sobre cada informação.

__
# Métodos de dicionários

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionário (zerar dados)

d.clear()

print(d)

__
# Copiando um dicionário para outro

#forma01

novo = d.copy()  # Deep Copy

print(novo)
print(type(novo))

novo['d'] = 4

print(d)
print(novo)

#forma02 - Shallow Copy

novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)

__

"""

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parâmetros: um iterável e um valor.
# ele vai gerar para cada valor do iterável um chave e irá atribuir a essa chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1,11), 'novo')

print(veja)

