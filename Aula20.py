def lin():
    print('-'*30)


def título(txt):
    print('-'*30)
    print(txt)
    print('-'*30)


def soma(a, b):
    s = a + b
    print(s)


def contador(* núm):
    print(núm)
    for valor in núm:
        print(valor, end=' ')
        print('FIM')


def dobra(lst):
    pos = 0
    while pos <len(lst):
        lst[pos] *= 2
        pos += 1


def som(* valor):
    e = 0
    for n in valor:
        e += n
    print(f'Somando os valores {valor} temos {e}')


lin()
título('Marcelo')
soma(4, 5)
soma(b=7, a=8)
contador(2, 1, 7)
contador(4, 7, 8, 9, 7)

valores = [6, 3, 4]
dobra(valores)
print(valores)

som(5, 8)