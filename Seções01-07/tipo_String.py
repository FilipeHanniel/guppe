"""
Em Python, um dado é considerado do tipo string sempre que:
- Estiver entre áspas simples -> 'uma string', '234', 'True'...
- Estiver entre áspas duplas  -> "uma string", "234", "True"...
- Estiver entre àspas simples triplas -> '''uma string''', '''234''', '''True'''

print('Geek')

nome = "Geek University"
print(nome)
print(type(nome))

nome = "Ginas's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = "Angelina \" Jolie"
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) # Transforma em uma lista de strings

nome = 'Geek University'
print(nome[0:4]) #Imprime apenas uma parte da string (Slice de Sting
print(nome[5:15])
print(nome.split()[0])
print(nome[::-1])  #Começe do primeiro elemento, vá até o último e inverta (método Pytônico)
print(nome.replace('G', 'P'))

"""
# - Estiver entre àspas duplas triplas  -> """uma string""", """234"""

nome = 'Geek University'
print(nome[0:4]) #Imprime apenas uma parte da string
print(nome[5:15])
print(nome.split()[0])
print(nome[14])
print(nome[::-1])  #Começe do primeiro elemento, vá até o último e inverta

print(nome.replace('G', 'P'))

texto = 'socorram me subino onibus em marrocos' #Palíndromo
print(texto)
print(texto[::-1])



