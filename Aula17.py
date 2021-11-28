'''num = [2, 5, 7, 7]
num[2] = 8
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(3)
if 7 in num:
    num.remove(7)
else:
    print('Não achei o 7')
print(num)
print(f'A lista tem {len(num)} elementos.')'''

'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)'''

'''for v in valores:
    print(f'{v}...', end='')

for c, v in enumerate(valores):
    print(f'\nNa posição {c} encontrei {v}', end='')
print('\nFim da lista')
a = [2, 3, 7]
b = a # ligação, não cópia
#b = a[:] # cópia 
b[2] = 9
print(f'Lista a: {a}')
print(f'Lista b: {b}')'''

teste = list()
teste.append('Marcelo')
teste.append(26)
galera = list()
galera.append(teste[:])
teste[0] = 'GOTOSA'
teste[1] = 26
galera.append(teste)
print(teste)

pessoal = [['Marcelo', 26], ['GOTOSA', 26], ['Wippel', 26], ['Gabi', 17]]
print(pessoal[0][0])
for p in pessoal:
    print(f'{p[0]} tem {p[1]} anos de idade')

pessoas = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoas.append(dado[:])  #[:] para criar copia
    dado.clear()
print(pessoas)
