CURSO EM PYTHON GUANABARA -

nome = 'Guanabara'
idade = 25
peso = 75.8
print (nome, idade, peso)

# Como perguntar cada 
nome = input('Qual seu nome? ')
idade = input('Quantos anos você tem? ')
peso = input('Qual  é seu peso? ')
print (nome, idade, peso)


# Programa #

# Como perguntar cada 
nome = input('Qual seu nome? ' )
print("Seja muito benvindo", nome)

idade = input('Quantos anos você tem?   ')
print("Nossa sua idade mostra que tem bastante experiencia na área !  ", nome, )

peso = input('Qual seu peso?  ')
print("Leve para ser rápido né!", nome)

profissão = input('Qual sua profissão?   ')
print("Excelente profissão de!  ", profissão, ",", nome)

print (nome,    idade,    peso,     profissão)

-------------------------------------------------

>>> AULA 6 > TIPOS PRIMITIVOS E SAÍDAS DE DADOS

# EXERCICIO AULA 4


n1 = int(input('Digite um número:'))
n2 = int(input('Digite mais um número:'))
s = n1 + n2
print('A soma vale', s)

int > Numero inteiro com qualquer valor EX. 7 _4 0 9875
float > Ponto flutuante tudo que tiver ponto - EX. 4.5  0.076  -15.223
bool > Boleano representa dois valores EX. True ou False.
str > Todas as palvras entre '' EX. 'Olá' '7.5' ''

** Potência
// Divisão Inteira
% Resto da Divisão



Forma de usar print

print('A soma vale',s)
print('A soma vale()'.format(s))  # sintaxe nova python 3

n = input('Digite um valor')
print(n.isalnum())

# is Metodos de tipos



>>> Curso Python #07 - Operadores Aritméticos + - * / ** // %

n1 = int(input('Digite um número:'))
n2 = int(input('Digite mais um número:'))
s = n1 + n2

print('A soma vale{}'.format(s))
print('A soma entre {} e {} vale {}'.format(n1, n2, s))


5 + 2 ==
5 - 2 ==
5 * 2 ==
5 / 2 ==
5 ** 2 ==
5 //2 ==
5 % 2 ==

Ordem de Precedência

1 >   ()
2 >   **
3 >   * / // %
4 >   + -



nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))


>>>> Curso Python 08 - Utilizando Módulos  <<<<


import bebidas # importa toda a biblioteca #

from doce import pudim  # importar apenas 1 funcionalidade #

import math # importa toda a biblioteca

from math import sqrt # importa apenas 1 item da biblioteca.

ceil # aredonda para cima.
floor # aredonda pra baixo.
trnc # vai eliminar da virgula pra frente
pow # semelhante aos dois **
sqrt # calcular raiz quadrada
factorial # 


>>>>> Curso Python #08 - Utilizando Módulos <<<<

# Calcule Raiz quadrada #
# ceil arredonda para cima
# floor arredonda para baixo

# Este modelo traz o pacote inteiro #
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

# Este modelo traz direto para pasta.
from math import sqrt, floor
num = int(input("Digite um número: '))
raiz = sqrt(num)
print('Araiz de {} é igual a {:.2f}'.format(num, floor(raiz)))


# Foi importado biblioteca em python.org
import emoji
print(emoji.emojize(" To sabendo em ::smirk:", use_aliases=True))
print(emoji.emojize(" To sabendo em ::heart_eyes:", use_aliases=True))


>>>>>>>>>> Curso Python #09 - Manipulando Texto <<<<< 


lista = 'Curso em Video python'
print(lista[0:14])
print(lista[15:21])

# Quando ser necessário inserir texto grande usar print(""" texto""")#
print("""O mesmo professor do desafio anterior quer sortear a ordem de
apresentação de trabalhos dos alunos
Faça um programa que leia o nome dos quatro alunos e
mostre a ordem sorteada.""")

# TRANSFORMAR AS LETRAS EM MAIUSCULOS #
lista = 'Curso em Video python'
print(lista.upper().count('o'))

# TRANSFORMAR AS LETRAS EM MAIUSCULOS E CONTAR 'O' 
lista = 'Curso em Video python'
print(lista.upper().count('O'))

# CONTAR OS CARACTER DE LISTA
lista = 'Curso em Video python'
print(len(lista.strip()))

# Trocar uma palavra da frase ou nome de coluna #
lista = 'Curso em Video Python'
print(lista.replace('Android','python'))


# Trocar uma palavra da frase ou nome de coluna #
lista = 'Curso em Video Python'
lista = lista.replace('Python','Android')
print(lista)

# TRANSFORMAR FRASE EM MINUSCULO #
lista = 'Curso em Video Python'
PRINT(lista.lower().find('video'))


lista = 'Curso em Video Python'
print(lista.split())




>>>>>>>>>> Curso Python #10 - Condições (Parte 1) <<<<<

# Condição

tempo = int(input('Quantos anos tem seu carro?  '))
if tempo <=3:
    print('Carro novo')
else:
    print('carro velho')
    print('--FIM--')


tempo = int(input('Quantos anos tem seu carro?  '))
print('Carro novo' if tempo <=3 else'carro velho')
print('--FIM--')

----------------------------------------------------

nome = str(input('Qual é o seu nome? '))
if nome == 'Arthur':
    print('Que nome lindo você tem!!! ')
print('Bom dia, {}!!'.format(nome))

# CONDIÇÃO SIMPLIFICADA #
n1 = float(input('Digite nota 1 '))
n2 = float(input('digite nota 2 '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
#print('PARABENS' if m >=6 else 'ESTUDE MAIS')
if m>=6.0:
    print('Sua média foi boa!! PARABÉNS!! ')
else:
    print('Sua média foi ruim!!! ESTUDE MAIS!!!')




 >>>>>>>>>>  Curso Python #11 - Cores no Terminal <<<<<

nome = 'Rafael'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[3m',
         'retoebranco':'\33[7:30'}
print('Olá!! Muito prazer em te onhecer, {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa'])))

11 > VIDEOS 
35 > EXERCICIOS

>>>>> FINALIZADO PRIMEIRO MUNDO PYTHON 3 <<<<<

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


>>>>>> INICIO MUNDO 2 PYTHON 3 <<<<<<

( MUNDO 2 >> AULA 12 >> Condições Aninhadas )

# estrutura condicional aninhada.
nome = str(input('Qual seu nome? '))
if nome =='Arthur':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é em popular no Brasil. ')
elif nome in 'Evelyn Lucia Claudia Lina':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom, {}!!'.format(nome))


---------------------------------------------------------------

( MUNDO 2 >> AULA 13 >>  )

