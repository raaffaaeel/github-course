 # DSA - CURSO EM PYTHON 3 #

  3 modos de executar PYTHON 

 #MODO SHELL
 #MODO SCRIPT (arquivos com extenção.py)
 #MODO INTERATIVO (Jupyter Notebook)

 # identação é importante (1 tab ou 4 spaces) Indentação faz parte da sintaxe em Python #
 
 serie sirie com vale

  DICAS
Clareza é importante. Mantenha seu código limpo e organizado.
Código esparso é melhor que código denso.
Sempre documente seu código.
Siga os padrões não para criar complexidade, mas para manter a regra.
Erros nunca serão silenciosos, a menos que propositalmente.
Simples é melhor que complexo e complexo é melhor que complicado.
Não se sinta obrigado a criar classes sem uma boa razão

# Python possui 2 tipos de números principais:
 
INT --> números inteiros, positivos ou negativos. Ex:-7 e 7
FLOT --> números fracionário, positivo ou negativos. Ex: 7.1 e 7.1

Podemos usar a função type(), para saber qual é o tipo de número usado.

 Funções Built-in 
#  https://docs.python.org/3/library/index.html #

Operador 	Significado	Exemplo
SINAL DE +	SOMA	    2 + 2 = 4
SINAL DE -	SUBTRAÇÃO	3 - 2 = 1
SINAL *	    MULTIPLIC	2 * 3 = 6
SINAL /	    DIVISÃO	    10 / 2 = 5 
SINAL % 	MÓDULO	    5 % 2 = 1
SINAL **	POTÊNCIA 	4 ** 2 = 16
INT()	CONVERTE PARA INTEIRO	INT(3.2) = 3
FLOT()	CONVERTE PARA FLOAT	FLOAT(2) =2.0

== IGUALDADE / EQUILÊNCIA
!= DESIGUALDADE / INEQUIVALÊNCIA
>  MAIOR QUE
<  MENOR QUE
>= MAIOR QUE OU IGUAL A
<= MENOR QUE OU IGUAL A

 lINK PARA ACESSAR GITHUB 
# https://github.com/dsacademybr #

 PARA ACESSAR GITHUB DA DSA 

> NO PROMPT DIGITE <

C:\Users\BlueShift>cd ..

C:\Users>cd ..

C:\> cd\Users\BlueShift\Desktop\DSA\PythonFundamentos-master

C:\Users\BlueShift\Desktop\DSA\PythonFundamentos-master>cd Cap02

C:\Users\BlueShift\Desktop\DSA\PythonFundamentos-master\Cap02>jupyter notebook

 VARIAVEIS E OPERADORES 

""
EXISTEM ALGUMAS REGRAS QUE DEVEM SER SEGUIDAS AO DEFINIR NOMES DE VARIÁVEIS

1 - OS NOMES DAS VARIÁVEIS NÃO PODEM COMEÇAR COM UM NÚMERO.
2 - NÃO PODE HAVER ESPAÇOS NO NOME; UTILE_EM VEZ DISSO.
3 - NÃO É POSSIVEL USAR QUALQUER UM DESSES SÍMBOLOS:"',<>/|\()@#$%^&*~-+!

O ITEM 3 É CONSIDERADO UMA BOA PRATICA DE PROGRAMAÇÃO (pep8)

VISITE O SITE: 

https://www.python.org/dev
https://docs.python.org/devguide

#

and > SE AMBOS OPERADORES FOREM TRUE, RETORNA TRUE > EX(x and y)é True
or  > SE UM DOS OPERADORES FOR TRUE, RETORNA TRUE > EX (x OR y) é True
Not > Usado para reverter o estado da lógica EX > NOT (x and y) é False

#

 AULA STRINGS #

STINGS são usadas e, Python para gravar informações em formato de texto, como nomes por exemplo. Strings em Python são na verdade uma sequência de caracteres o que significa, basicamente, Python mantém o controle de cada elemento da sequência.

PYTHON entende a string "Olá" como sendo uma sequência de letras em uma ordem específica. Isso significa que vc será capaz de usar a indexação para obter um caracter específico ( como a primeira letra ou a última letra).

INDEXANDO STRINGS.
Em Python, usamos colchetes [] para representar o indice de um objeto
--> Em Python, a indexação começa por 0.

EXEMPLO: (Indexando Strings)

texto="Python e Análise de Dados"

texto[0]=P
texto[1]=Y
texto[2]=t

Obs: Uma vez criado uma string não pode ser alterado ou modificado.

# FUNÇÕES BUILT-IN DE STRINGS # 

Python é uma linguagem orientada a objeto, sendo assim as estruturas de dados possuem atributos (propriedades) e métodos (rotina associadas às propriedades). Tanto os atributos quanto os métodos são acessados usando ponto(.).

OS MÉTODOS ESTÃO SOB A FORMA;

objeto.atributo
objeto.método()
objeto.método(parâmetros)

# Para fazer uma quebra de linha em PYTHON 3 utilizar \n no incio da palavra ou texto #


Função para colocar o texto em Maiusculo --> s.upper()

Função para colocar o texto em minusculo -->  s.lower()


Quando se tem uma lista e precisamos fazer o Backup desta lista utilizamos --> 

Ex:
old_list = [1,2,5,10]

Nem List []

for item in old_list:
    new_list.append(item)


Fim 

Como inserir endereço das redes sociais.
 Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>  #





--> Lista são criadas com COUCHETES []

--> Diciónarios criamos com CHAVES {}

--> Tuplas são criadas com PARENTESES ()


Diciónarios - MAPEAMENTO DE CHAVES E VALORES

{chave1: valor1, chave2: valor2}


# Isso é uma lista
estudantes_lst = [ "Rafael", 37, "Arthur", 8, "Evelyn", 36, "Lina", 64, "Ademar", 70]

#Resposta do estudantes_dict#
estudantes_lst = 
['Rafael', 37, 'Arthur', 8, 'Evelyn', 36, 'Lina', 64, 'Ademar', 70]


# Isso é um dicionário
estudantes_dict = {"Juninho":24, "Fernanda":22, "Tamires":26, "Cristiano":25}

#Resposta do estudantes_dict#
estudantes_dict =
{'Juninho': 24, 'Fernanda': 22, 'Tamires': 26, 'Cristiano': 25}


#Inserir um novo nome na tabela lista #
estudantes_dict["Pedro"] = 23

# Limpar a tabela #
estudantes_dict.clear()

# Deletar a tabela #
del estudantes_dict



#Craiando novo Dicionario.

estudantes = {"Mateus":24, "Fernanda":22, "Tamires":26, "Cristiano":25}


# CONTA QUANTAS INFORMAÇÕES TEM NA DICIONARIO #
len(estudantes)

# CONTA QUANTAS CHAVES TEM #
estudantes.keys()

# CONTA QUANTOS VALORES EXIXTE #
estudantes.values()

# CONTA QUANTOS ITEMS NA TABELA #
estudantes.items()


# Unir os 2 dicionarios em uma só #
estudantes.update(estudantes2)

estudantes
{'Mateus': 24,
 'Fernanda': 22,
 'Tamires': 26,
 'Cristiano': 25,
 'Maria': 27,
 'Erika': 28,
 'Milton': 26}

dic1 = {}

dic1
{}

dic1["key_one"] = 2

print(dic1)
{'key_one': 2}

dic1[10] = 5

dic1
{'key_one': 2, 10: 5}

dic1[8.2] = "Python"

dic1
{'key_one': 2, 10: 5, 8.2: 'Python'}

dic1["teste"] = 5
dic1
{'key_one': 2, 10: 5, 8.2: 'Python', 'teste': 5}

dict1 = {}
dict1
{}

dict1["teste"] = 10
dict1["key"] = "teste"

# Atenção, pois chave e valor podem ser iguais, mas representam coisas diferentes.
dict1
{'teste': 10, 'key': 'teste'}

dict2 = {}

dict2["key1"] = "Big Data"
dict2["key2"] = 10
dict2["key3"] = 5.6
dict2
{'key1': 'Big Data', 'key2': 10, 'key3': 5.6}

a = dict2["key1"]
b = dict2["key2"]
c = dict2["key3"]
a, b, c
('Big Data', 10, 5.6)

# Dicionário de listas
dict3 = {'key1':1230,'key2':[22,453,73.4],'key3':['leite','maça','batata']}

dict3
{'key1': 1230, 'key2': [22, 453, 73.4], 'key3': ['leite', 'maça', 'batata']}

dict3['key2']
[22, 453, 73.4]
# Acessando um item da lista, dentro do dicionário
dict3['key3'][0].upper()
'LEITE'
# Operações com itens da lista, dentro do dicionário
var1 = dict3['key2'][0] - 2
var1
20
# Duas operações no mesmo comando, para atualizar um item dentro da lista
dict3['key2'][0] -= 2

dict3
{'key1': 1230, 'key2': [20, 453, 73.4], 'key3': ['leite', 'maça', 'batata']}


Criando dicionários aninhados
# Criando dicionários aninhados
dict_aninhado = {'key1':{'key2_aninhada':{'key3_aninhada':'Dict aninhado em Python'}}}

dict_aninhado
{'key1': {'key2_aninhada': {'key3_aninhada': 'Dict aninhado em Python'}}}

dict_aninhado['key1']['key2_aninhada']['key3_aninhada']
'Dict aninhado em Python'

Fim

--------------------------------------------------------------

# EM PYTHON TUPLAS SÃO IMUTÁVEIS #

As Tuplas são construídas com o uso de parênteses () e virgula separando cada elemento da tupla.

tupla=(item1, item2,..., itemz)


# Criando uma tupla
tupla1 = ("Geografia", 23, "Elefantes")

# Imprimindo a tupla
tupla1
('Geografia', 23, 'Elefantes')


# Tuplas não suportam append()
tupla1.append("Chocolate")   
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-3-cb90e5e5a1a0> in <module>
      1 # Tuplas não suportam append()
----> 2 tupla1.append("Chocolate")

AttributeError: 'tuple' object has no attribute 'append'

# Tuplas não suportam delete de um item específico
del tupla1["Gatos"]  
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-24facd06bb21> in <module>
      1 # Tuplas não suportam delete de um item específico
----> 2 del tupla1["Gatos"]

TypeError: 'tuple' object does not support item deletion

# Tuplas podem ter um único item
tupla1 = ("Chocolate")
tupla1
'Chocolate'

tupla1 = ("Geografia", 23, "Elefantes")
tupla1[0]
'Geografia'

# Verificando o comprimento da tupla
len(tupla1)
3

# Slicing, da mesma forma que se faz com listas
tupla1[1:]
(23, 'Elefantes')

tupla1.index('Elefantes')
2

# Tuplas não suportam atribuição de item
tupla1[1] = 21
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-12-59bcc25f7f2b> in <module>
      1 # Tuplas não suportam atribuição de item
----> 2 tupla1[1] = 21

TypeError: 'tuple' object does not support item assignment

# Deletando a tupla
del tupla1
tupla1
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-14-9c021f243716> in <module>
----> 1 tupla1

NameError: name 'tupla1' is not defined

# Criando uma tupla
t2 = ('A', 'B', 'C')

t2
('A', 'B', 'C')

# Tuplas não suportam atribuição de item
t2[0] = 'D'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-17-f90994f4060e> in <module>
      1 # Tuplas não suportam atribuição de item
----> 2 t2[0] = 'D'

TypeError: 'tuple' object does not support item assignment

# Usando a função list() para converter uma tupla para lista
lista_t2 = list(t2)

lista_t2
['A', 'B', 'C']
lista_t2.append('D')

# Usando a função tuple() para converter uma lista para tupla
t2 = tuple(lista_t2)
t2
('A', 'B', 'C', 'D')

Fim

--------------------------------------------------------------------------

TIPOS DE OBJETO - CATEGORIA  - MUTÁVEL ?
                -            -
NUMEROS         - NUMÉRICO   -   NÃO
STRINGS         - SEQUÊNCIA  -   NÃO
LISTAS          - SEQUÊNCIA  -   SIM
DICIONARIO      - MAPEAMENTO -   SIM
TUPLAS          - SEQUÊNCIA  -   NÃO



Exercícios Cap02 - Soluções
# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
lista = ['chocolate', 'banana', 'abacaxi', 'uva', 'morango']
print(lista)
['chocolate', 'banana', 'abacaxi', 'uva', 'morango']

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
frase1 = 'Se beber '
frase2 = 'não dirija!'
frase_final = frase1 + frase2
print(frase_final)
Se beber não dirija!

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
tup1 = (1, 2, 2, 3, 4, 4, 4, 5)
tup1.count(4)
3

# Exercício 5 - Crie um dicionário vazio e imprima na tela
dict3 = {}
print(dict3)
{}

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dict = {'k1':'martelo', 'k2':'serrote', 'k3':'machado'}
print(dict)
{'k1': 'martelo', 'k2': 'serrote', 'k3': 'machado'}

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dict['k4'] = 'parafuso'
print(dict)
{'k1': 'martelo', 'k2': 'serrote', 'k3': 'machado', 'k4': 'parafuso'}

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.
dict2 = {'chave1':'Geografia', 'chave2':'Biologia', 'chave3':[70, 90]}
print(dict2)
{'chave1': 'Geografia', 'chave2': 'Biologia', 'chave3': [70, 90]}

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
lst = ['String1', (90, 92), {'k1':'v1', 'k2':'v2'}, 99.98]
print(lst)
['String1', (90, 92), {'k1': 'v1', 'k2': 'v2'}, 99.98]

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
frase[0:100]
'Cientista de Dados é o profissional mais sexy do século XXI'

Fim

----------------------------------------------------------------

( Trabalhando Game em Python )

