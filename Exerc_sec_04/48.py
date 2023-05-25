print('Digite o tempo em segundos:')

tempo = int(input())

if tempo <= 60:
    print(f'Temos {tempo} segundos')
elif (tempo > 60) and (tempo < 3600):
    print(f'Temos {int(tempo / 60)} minuto e {tempo % 60} segundos')
else:
    print(f'Temos {int(tempo / 3600)} horas, {tempo % 3600} minutos e {(tempo % 3600) - 60} segundos')
    # corrigir pequeno defeito nos segundos
