DESAFIOS CURSO EM VIDEO PYTHON.

(DESAFIO 5)
# faça um programa que leia um número inteiro e mostre
# na tela o seu  sucessor e seu antecessor.


n1 = int(input('Digite um valor: '))
a = n1-1
b = n1+1
# Abaixo 2 tipos de print para mostrar os resultados.. #
print(f'O número inteiro é {n1} o antecessor é {a} e o sucessor é {b}!!! ')
print(f'O número inteiro é >> {n1} seu antecessor é >> {n1-1} o seu sucessor é >> {n1+1}!!! ')


(DESAFIO 6)
# Crie um algoritmo que leia um numero e mostre,
# o seu dobro, triplo e raiz quadrada.

n1 = int(input('Informe um número pequeno gafanhoto '))
x = n1 * 2
y = n1 * 3
z = n1 ** (1/2)
print(f'O número escolhido, pequeno gafanhoto é {n1} o seu dobro é {x} o seu triplo é {y} e sua raiz quadrada é {z}!!! ')
print(f'O número escolhido, pequeno gafanhoto foi: {n1}, seu dobro é: {n1*2}, o triplo é: {n1*3}, e sua raiz quadrada é: {n1 ** (1/2)}!')



(DESAFIO 7)
# Desenvolva um programa que leia as duas notas de um.
# aluno, calcule e mostre a sua média.

nota1 = float(input('Informe sua primeira nota pequeno gafanhoto? '  ))
nota2 = float(input('Informe sua segunda nota pequeno gafanhoto? '   ))
valor_media = int(nota1 + nota2) / 2
print('A média do aluno é {}' .format(valor_media))
print(f' A primeira nota do aluno {nota1} a segunda nota do aluno {nota2}, sua média com base nas 2 provas é {valor_media}!!! ')


(DESAFIO 8)
# escreva um programa que leia um valor em metros e o
# exiba convertido em centimentros e milimetros.

m = int(input('Metragem: '))
c = int(m*100)
ml = int(m*1000)
print('Dentro dessa metragem existem {} centímetros e {} milímetros' .format(c, ml))



(DESAFIO 9)
# Faça um programa que leia um número inteiro qualquer,
# e mostre na tela a sua tabuada.

n1 = int(input('Digite um número? '))
print(f'O numero digitado = {n1}\nSegue abaixo sua tabuada \n'
      f'{n1} x 1 = {n1 * 1} \n{n1} x 2 = {n1 * 2} \n{n1} x 3 = {n1 * 3} \n'
      f'{n1} x 4 = {n1 * 4} \n{n1} x 5 = {n1 * 5} \n{n1} x 6 = {n1 * 6} \n'
      f'{n1} x 7 = {n1 * 7} \n{n1} x 8 = {n1 * 8} \n{n1} x 9 = {n1 * 9} \n'
      f'{n1} x 10 = {n1 * 10}')



(DESAFIO 10)
# Crie um programa que leia quanto dinheiro uma pessoa
# tem na carteira e mostre quantos dólares ela pode comprar.
# Considera US$ 1,00 = R$3,27

real = float(input('Informe quanto você tem em real? '))
dolar = 3.27
conversao = real / dolar
print(f'Valor possuído em R$ = { real } e em US$ = {conversao :.2f}')



(DESAFIO 11)
# Faça um programa que leia a largura e a altura de uma
# parede em metros, calcule a sua área e a quantidade de
# tinta necessária para pintá-la sabendo que cada litro
# de tinta, pinta uma área de 2 metros quadrados.

largura = float(input('Qual a lagura da parede? '))
altura = float(input('Qual é altura da parede?  '))
area = largura * altura
litroDeTinta = 2
qtdDeLitros = area / litroDeTinta
print(f'A parede tem {area} m², a quantidade de tinta para essa parede é = {qtdDeLitros}' )


(DESAFIO 12)
# Faça um algoritmo que leia o preço de um produto e mostre
# seu novo preço, com 5% de descontos.

precoproduto = float(input('Informe o preço do produto? '))
desconto = float(5/100) * precoproduto
novoprecoproduto = int(precoproduto - desconto)
print(f'O preço do produto antes do desconto era, R$ {precoproduto} após o desconto o novo preço é R$ {novoprecoproduto :.2f} !! Venha aproveitar pequeno gafanhoto!! ') 


(DESAFIO 13)
# Faça um algoritmo que o salário de um funcionário e mostre
# seu novo salário, com 15% de aumento.

salario = float(input('Informe o salário do funcionario: '))
aumento = 15/100 * salario
novoSalario = salario + aumento
print(f'O salário antes do aumento era de R${salario :.2f}, salário após o aumento é de R${novoSalario :.2f}')



(DESAFIO 14)
# Escreva um programa que converta uma temperatura
# digitada em C graus cecius para graus fairenet.

c = float(input('Informe a temperatura em C: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {} C corresponde a {} F!'.format(c, f))



(DESAFIO 15)
#Escreva um programa que pergunte a quantidade
# de KM percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço a pagar
# sabendo que o carro custa R$ 60,00 por dia e 0,15 por km.

dias = int(input('Informe quantos dias de aluguel?'  ))
km = float(input('Quantos km rodado?'  ))
pago = (dias * 60) + (km * 0.15)
print(' O total a pagar é de R${:.2f}'.format(pago))


(DESAFIO 16)
#Crie um programa que leia um numero real qualquer pelo
#teclado e mostre na tela a sua porção inteira.
#ex. Digite um número: 6.127 O numero 6.127 tem a parte inteira 6.

import math
num = float(input('Digite um valor: '))
print('O Valor digitado foi {} e a sua porcao inteira é {}'.format(num, math.trunc(num)))


from math import trunc
num = float(input('Digite um valor:  '))
print('O valor digitado foi {}  e a sua porção inteira é {}'.format(num, trunc(num)))


num = float(input('Digite um valor:  '))
print('O valor digitado foi {}  e a sua porção inteira é {}'.format(num, int(num)))


(DESAFIO 17)
# Faça um programa que leia o comprimento do cateto aposto e do
# cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento
# da hipotenusa.

# SEM MODULO
co = float(input('Comprimento do oposto  '))
ca = float(input('Comprimento do cateto adiacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

# IMPORTATNDO MODULO INTEIRO.
import math
co = float(input('Comprimento do oposto  '))
ca = float(input('Comprimento do cateto adiacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

# IMPORTANDO APENAS O MODULO HYPOT #
from math import hypot
co = float(input('Comprimento do oposto  '))
ca = float(input('Comprimento do cateto adiacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))


(DESAFIO 18)
# Faça um programa que leia um Ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangete desse Ângulo.

# IMPORTANDO MODULO INTEIRO #
import math
angulo = float(input('Digite um ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))

# IMPORTANDO APENAS OS METEDOS, radians, sin, cos, tan #
from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo que você deseja: '))
seno = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))



(DESAFIO 19)
# Um professor quer sortear um dos seus quatro alunos para apagar
# o quadro. Faça um programa que ajude ele lendo o nome deles
# e escrevendo o nome do escolhido.

# o metodo choice faz com que o computador escolha um item da lista #
import random
n1 = str(input('Primeiro aluno ' ))
n2 = str(input('Segundo nome ' ))
n3 = str(input('Terceiro nome ' ))
n4 = str(input('Quarto aluno ' ))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O nome do aluno escolhido foi {}'.format(escolhido))

# IMPORTANDO APENAS O METEDOS, choice #
from random import choice
n1 = str(input('Primeiro aluno ' ))
n2 = str(input('Segundo nome ' ))
n3 = str(input('Terceiro nome ' ))
n4 = str(input('Quarto aluno ' ))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O nome do aluno escolhido foi {}'.format(escolhido))