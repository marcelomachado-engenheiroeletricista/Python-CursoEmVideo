#help()
def contador(i, f, p=0):
    """"
    -> Faz uma contagem e mostra na tel.
    :param i: ínício da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    :=0: se não houver nada, fica zerado sem problema
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM')


def teste(a):
    global n #utiliza variavel global
    x = 8 #variavel local
    print(f'{n} {x}') #escopo local



def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f




n = 2
x = 1 # variavel global
teste(1)

help(contador)

r1 = soma(3, 2, 3)
r2 = soma(3, 2)
r3 = soma(3)
print(f'{r1} {r2} {r3}')

t = int(input('Digite um número: '))
print(f'O fatorial de {t} é igual a {fatorial(t)}')
