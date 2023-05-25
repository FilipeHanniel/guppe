print('APOSENTADORIA')

idade = int(input('Digite a idade: '))
tempo = int(input('Digite o tempo de serviço em anos: '))

if (idade >= 65 and tempo >= 30) or (idade >= 60 and tempo >= 25):
    print('Essa pessoa pode se aposentar!')
else:
    print('Essa pessoa não pode se aposentar!')

