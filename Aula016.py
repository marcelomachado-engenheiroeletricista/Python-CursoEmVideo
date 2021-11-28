lanche = ('Bumger', 'Suco', 'Pizza', 'Pudim')   #variavel composta "Tupla" imutaveis
print(lanche[1])
for comida in lanche:
    print(comida)
for cont in range(0, len(lanche)):
    print(lanche[cont], cont)

print(sorted(lanche))

a = (2, 5, 6)
b = (5, 8, 4)
c = a + b
d = b + a
print(c)
print(d)
print(c.count(5))
print(c.index(8))
del(d)
r = ('Marcelo', 26, 'M')