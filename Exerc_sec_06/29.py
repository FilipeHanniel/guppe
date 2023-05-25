print('SÉRIE DE 5 TERMOS')

s = 0
f = 1

for i in range(2, 6):
    while i > 1:
        f = i * f
        i = i - 1
    s = (1 / f) + s

print(s)