'''
tabela ANSI para cores
\033[style text back m
\033[o:33:44m

style
0 none
1 bold
4 underline
7 negative (inverte)

text
30 - branco
31 - vermelho
32 - verde
33 - amarelo
34 - azul
35 - magenta
36 - ciano
37 - cinza

back
40 - branco
41 - vermelho
42 - verde
43 - amarelo
44 - azul
45 - magenta
46 - ciano
47 - cinza

'''
print('\033[7;30;45mOlá, GOTOSA!\033[m')
a = 1
b = 3
print('Os valores são: \033[1;35;40m{}\033[m e \033[1;30;45m{}\033[m'.format(a, b))
g = 'GOTOSA'
print('Amo minha {}{}{} '.format("\033[1;30;45m", g, "\033[m"))