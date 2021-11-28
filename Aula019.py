pessoas = {'nome': 'Marcelo', 'sexo': 'M', 'idade': 26}
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
pessoas['nome'] = 'GOTOSA'
pessoas['peso'] = 50
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {'uf': 'Santa', 'sigla': 'SC'}
estado2 = {'uf': 'Paraná', 'sigla': 'PR'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['uf'])

estado = dict()
pais = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    pais.append(estado.copy()) #copia para dicionario
for e in pais:
    print(e)
for e in pais:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}')
for e in pais:
    for v in e.values():
        print(v, end=' ')
    print()