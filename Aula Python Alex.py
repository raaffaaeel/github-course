AULA PYTHON ALEX





linguagem Função

>>> def soma(x, y, z):
...     total = x + y + z
...     return total
...
>>> print(soma(500, 500, 2000))
3000


>>> def funcao(x, v):
...     return (x + v)
...
>>> a = funcao("rafael ", "macedo")
>>> a
'rafael macedo'


FUNÇÃO input
>>> nome = input("digite seu nome:\n")
digite seu nome:
Rafael macedo
>>> print(nome)
Rafael macedo
>>> print(f"\n\n\n {nome}")



 Rafael macedo
>>>

linguagem calcula:

def calcula(a, b):
...     return(int(a) ** int(b))
...
>>> k = input("digite um numero: ")
digite um numero:  10
>>> j = input("digite um numero: ")
digite um numero: 3
>>>
>>> calcula(k, j)
1000


CONTROLE DE FLUXO IF

>>> def verifica(x):
...     if x < 100:
...             print("X é menor que 100")
...     elif x > 100:
...             print("X é menor que 100")
...     else:
...             print("X é menor que 100")
...
>>> verifica(10)
X é menor que 100
>>>

>>> x=101
>>>
>>> verifica(x)
X é menor que 100


COMANDO LOOP WHILE

>>> x=0
>>> while x <=10:
...     print(x)
...     x=x+1
...
0
1
2
3
4
5
6
7
8
9
10
>>>

TESTE
>>> a = 10
>>> b = 50
>>> while a <= b:
...     print(b-a)
...     a += 1
...
40
39
38
37
36
35
34
33
32
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
>>>

COMANDO LISTA

>>> lista = ["Fiat", "Ford", "Hyundai"]
>>> lista
['Fiat', 'Ford', 'Hyundai']
>>> for c in lista:
...     print(c)
...
Fiat
Ford
Hyundai
>>> for a in range(10):
...     print(a)
...
0
1
2
3
4
5
6
7
8
9
>>>



