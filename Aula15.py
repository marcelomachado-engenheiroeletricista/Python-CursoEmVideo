n = s = 0
while True:
    n = int(input('N1: '))
    if n == 999:
        break
    s += n
#print('Soma: {}'.format(s))
print(f'A soma é {s}')