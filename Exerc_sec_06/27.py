print('SÉRIE HARMÔNICA\n')

n = int(input('Digite um valor inteiro e positivo: \n'))
s = 0

if n > 0:
    for i in range(1, n + 1):
        s = s + 1/i

print(s)
