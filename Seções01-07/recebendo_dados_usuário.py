"""
Recebendo dados do usuário

input() => Todo dado recebido via input é do tipo String

Em Pyton, string é tudo que estiver entre:
-aspas simples;
-aspas duplas;
-aspas simples triplas;
-aspas duplas triplas.



"""
# Entrada de Dados
# print("Qual o seu nome?")
# nome = input()

nome = input("Qual o seu nome?")



# Processamento

# Saída de Dados (Exemplo "antigo" do Python 2.x)
# print("Seja bem vindo(a) %s" % nome )

# Exemplo de print mais recente:
# print("Seja bem vindo(a) {0}".format(nome))

# Exemplo de print mais atual ainda (3.7 em diante):
print(f"Seja bem vindo(a) {nome} ")

#print("Qual a sua idade?")
idade = int(input("Qual sua idade?"))

# Saída
# print("O %s tem %s" % (nome, idade) )

print(f" A {nome} tem {idade} anos")

"""
int(idade) => cast

Cast é a conversão de um tipo de dado para outro
"""

print(f"A {nome} nasceu em {2022 - idade}")

