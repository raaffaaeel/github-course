Semana Python Renzo 

vscode - ok
Python - ok


if idade >= 18:
     print('Maior de Idade')
 elif idade < 14:
     print('Criança')
 else:
     print('Adolescente')if idade >= 18:
     print('Maior de Idade')
 elif idade < 14:
     print('Criança')
 else:
     print('Adolescente')



>>> print('Ola Mundo')
Ola Mundo
>>> type(')
  File "<stdin>", line 1
    type(')
          ^
SyntaxError: EOL while scanning string literal
>>> type('')
<class 'str'>
>>> rafael = 'Rafael'
>>> type(rafael)
<class 'str'>
>>> rafael
'Rafael'
>>> rafael = 'Rafael'
>>> rafael
'Rafael'
>>> rafael = "Rafael"
>>> type(rafael)
<class 'str'>
>>> rafael
'Rafael'
>>> rafael = "Rafael's"
>>> rafael
"Rafael's"


-- 3 aspas pula linha --

>>> rafael = '''Rafael
... de
... Araujo
... Macedo'''
>>> rafael
'Rafael\nde\nAraujo\nMacedo'


>>> rafael
'Rafael\nde\nAraujo\nMacedo'
>>> help(rafael.lower)
Help on built-in function lower:

lower() method of builtins.str instance
    Return a copy of the string converted to lowercase.

>>> rafael.lower()
'rafael\nde\naraujo\nmacedo'
>>> help(rafael.upper)
Help on built-in function upper:

upper() method of builtins.str instance
    Return a copy of the string converted to uppercase.

>>> rafael.upper()
'RAFAEL\nDE\nARAUJO\nMACEDO'


>>> '2987233'
'2987233'
>>> 'a'.lower()
'a'
>>> type('2987233')
<class 'str'>
>>> '2'+'2'
'22'
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>>

saber posição dops caracteres.


>>> rafael
'Rafael\nde\nAraujo\nMacedo'
>>> rafael[0]
'R'
>>> rafael[1]
'a'
>>> rafael[2]
'f'
>>> rafael[3]
'a'
>>> rafael[4]
'e'
>>> rafael[5]
'l'

pegar o tamanho.

>>> len('a')
1
>>> len('')
0
>>> rafael
'Rafael\nde\nAraujo\nMacedo'
>>> tamanho = len(rafael)
>>> tamanho
23
>>> rafael[tamanho -1]
'o'
>>> rafael[-1]
'o'


>>> numeros = list(range(10))
>>> numeros
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>>
>>> list(range(1, 10, 2))
[1, 3, 5, 7, 9]
>>>
>>> list(range(1, 10,))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>>
>>> numero[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'numero' is not defined
>>> numeros[0]
0
>>> numeros[-1]
9
>>> numeros[:5]
[0, 1, 2, 3, 4]
>>>
>>> numeros
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> numeros + [10, 11, 12]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
>>>
>>> numeros
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



tuplas

>>> tpl = (1,3,5)
>>> type(tpl)
<class 'tuple'>

>>> dir(tpl)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>>
>>> tpl = 1,3,5
>>> tpl
(1, 3, 5)
>>>
>>> tpl[0]
1
>>> tpl[0:2]
(1, 3)
>>>
>>> primiero, segundo, terceiro = tpl

>>> primiero
1
>>> segundo
3
>>> terceiro
5
>>>
>>> primeira, *demais = tpl

>>> primeira
1


>>> for letra in rafael:
...      print(rafael)    ??????



dicionario

>>> dct = {'br': 'portugues'}
>>> type(dct)
<class 'dict'>

>>> dct['br']
'portugues'
>>>
>>> dct['en'] = 'Inglês'
>>> len(dct)
2
>>> dct['en']
'Inglês'
>>>
>>> dct
{'br': 'portugues', 'en': 'Inglês'}

for qq_coisa in dct:
...      print(qq_coisa)
...
br
en
>>> for chave in dct: print(chave, dct[chave])
...
br portugues
en Inglês
>>>

>>> for chave in dct.keys(): print(chave, dct[chave], sep='->')
...
br->portugues
en->Inglês

for item in dct.items(): print(item[0], item[1])
...
br portugues
en Inglês


>>> for pais, lingua in dct.items(): print(pais, lingua)
...
br portugues
en Inglês


dct = {'rafael' : 38, 'evelyn': 37}
>>> for pais, lingua in dct.items(): print(pais, lingua)
...
rafael 38
evelyn 37
>>>
>>> def imprimir():
...     print('inicio')
...     print('Final')
...
>>> type(imprimir)
<class 'function'>
>>>
>>> imprimir()
inicio
Final


soma

>>> def soma(a, b):
...     return a + b
...
>>> soma(2, 3)
5
>>> soma(2,-3)
-1

