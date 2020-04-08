DESAFIOS CURSO EM VIDEO PYTHON.

(DESAFIO 5))
# Faça um programa que leia um número inteiro e mostre
# na tela o seu  sucessor e seu antecessor.

#Modelo 1
n1 = int(input('Digite um valor pequeno gafanhoto: '))
a = n1 - 1
b = n1 + 1
print('Analisando o valor {}, seu antecessor é {} e seu sucessor {}' .format(n1, a, b))

#Modelo 2
n = int(input('Digite o valor: '))
print('Analisando o valor {}, seu antecessor é {}, e seu sucessor {}' .format(n, (n-1), (n+1)))



(DESAFIO 6)
# Crie um algoritmo que leia um numero e mostre,
# o seu dobro, triplo e raiz quadrada.

n1 = int(input('Informe um número pequeno gafanhoto '))
x = n1 * 2
y = n1 * 3
z = n1 ** (1/2)
print('O número escolhido, pequeno gafanhoto é {n1} o seu dobro é {x} o seu triplo é {y} e sua raiz quadrada é {z}!!! ')
print(f'O número escolhido, pequeno gafanhoto foi: {n1}, seu dobro é: {n1*2}, o triplo é: {n1*3}, e sua raiz quadrada é: {n1 ** (1/2)}!')

print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}. \n A raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))

# Modelo 2
n = int(input('Informe um número pequeno gafanhoto '))
print('O dobro de {} vale {}.'.format(n, (n * 2)))
print('O triplo de {} vale {}. \n A raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, (n**(1/2))))



(DESAFIO 7)
# Desenvolva um programa que leia as duas notas de um.
# aluno, calcule e mostre a sua média.
# MODELO 1
nota1 = float(input('Informe sua primeira nota pequeno gafanhoto? '  ))
nota2 = float(input('Informe sua segunda nota pequeno gafanhoto? '   ))
valor_media = (nota1 + nota2) / 2
print(' A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(nota1, nota2, valor_media))

# MODELO 2
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

# MODELO 1
valor = int(input('Choose a number: '))
lista2 = [1,2,3,4,5,6,7,8,9,10]
for i in lista2:
    total = valor * i
    print("{} x {} = {}".format(str(valor), str(i), str(total) ))

    valor = int(input('Choose a number: '))
    lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in lista2:
          total = valor * i
          print("{} x {} = {}".format(str(valor).rjust(2, "0"), str(i).rjust(2, "0"), str(total).rjust(2, "0")))


# MODELO 2
n1 = int(input('Digite um número? '))
print(f'O numero digitado = {n1}\nSegue abaixo sua tabuada \n'
      f'{n1} x 1 = {n1 * 1} \n{n1} x 2 = {n1 * 2} \n{n1} x 3 = {n1 * 3} \n'
      f'{n1} x 4 = {n1 * 4} \n{n1} x 5 = {n1 * 5} \n{n1} x 6 = {n1 * 6} \n'
      f'{n1} x 7 = {n1 * 7} \n{n1} x 8 = {n1 * 8} \n{n1} x 9 = {n1 * 9} \n'
      f'{n1} x 10 = {n1 * 10}')

# MODELO 3
num = int(input('Digite um numero para ver sua tabuada de mutiplicar: '))
print('-' * 12)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('{} x {:2} = {}' .format(num, 11, num*11))
print('-' * 12)

# MODELO 4
num = int(input('Digite um numero para ver sua tabuada de menos: '))
print('{} - {:2} = {}'.format(num, 1, num-1))
print('{} - {:2} = {}'.format(num, 2, num-2))
print('{} - {:2} = {}'.format(num, 3, num-3))
print('{} - {:2} = {}'.format(num, 4, num-4))
print('{} - {:2} = {}'.format(num, 5, num-5))
print('{} - {:2} = {}'.format(num, 6, num-6))
print('{} - {:2} = {}'.format(num, 7, num-7))
print('{} - {:2} = {}'.format(num, 8, num-8))
print('{} - {:2} = {}'.format(num, 9, num-9))
print('{} - {:2} = {}'.format(num, 10, num-10))
print('{} - {:2} = {}' .format(num, 11, num-11))



(DESAFIO 10)
# Crie um programa que leia quanto dinheiro uma pessoa
# tem na carteira e mostre quantos dólares ela pode comprar.
# Considera US$ 1,00 = R$3,27

real = float(input('Informe quanto você tem em real? '))
dolar = 3.27
conversao = real / dolar
print(f'Valor possuído em R$ = {real :.2f} e em US$ = {conversao :.2f}')

real = float(input('Informe quanto você tem em real? '))
dolar = real / 4.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))



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


www.ifd.uci.edu/~gohike/pythonlibs/#pygame

(DESAFIO 20)
# O mesmo professor do desafio anterior quer sortear a ordem de
# apresentação de trabalhos dos alunos
# Faça um programa que leia o nome dos quatro alunos e
# mostre a ordem sorteada.

# IMPORTAR O MODULO INTEIRO #
import random
n1 = str(input('Primeiro aluno: ' ))
n2 = str(input('Segundo nome: ' ))
n3 = str(input('Terceiro nome: ' ))
n4 = str(input('Quarto aluno: ' ))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A Ordem da Apresentação será  ')
print(lista)

# IMPORTANDO APENAS O METEDOS, shuffle #
from random import shuffle
n1 = str(input('Primeiro aluno: ' ))
n2 = str(input('Segundo nome: ' ))
n3 = str(input('Terceiro nome: ' ))
n4 = str(input('Quarto aluno: ' ))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A Ordem da Apresentação será  ')
print(lista)


(DESAFIO 21)
# Faça um programa em python que abra e reproduza
# o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('djpuffy.mp3')
pygame.mixer.music.play()
pygame.event.wait()


(DESAFIO 22)
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com tvodas minúsculas
#Quantas letras ao todo sem considerar espaços
# Quantas letras tem o primeiro nome.


nome = input('digite seu nome e sobrenome: ')
print(f'nome com todas as letras maiuscula: {nome.upper()}')
print(f'nome com todoas a letras minuscula: {nome.lower()}')
d = nome.split()
print(f'esse nome tem {len("".join(d))} letras')
print(f'o primeiro nome tem {len(d[0])}')


(DESAFIO 23)
# Faça um programa que leia um número de 0 a 9999  e mostre na tela cada um
# dos digitos separados
# EX Digite um numero: 1834
#unidade: 4
#dezena: 3
#centgena: 8
#milhar 1

#Exemplo 1:

import math
num = int(input('Digite um número de 0 a 9999: '))
u = num % 10
d = math.floor((num % 100)/10)
c = math.floor((num % 1000)/100)
m = math.floor(num/1000)
print('unidade:{}\ndezena:{}\ncentena:{}\nmilhar:{}'.format(u, d, c, m))

#Exemplo 2:

num = '000' + str(input('Digite um número de 0 a 9999: '))
u = num[-1]
d = num[-2]
c = num[-3]
m = num[-4]
print('unidade:{}\ndezena:{}\ncentena:{}\nmilhar:{}'.format(u, d, c, m))



(DESAFIO 24)
# Crie um programa que leia o nome de uma cidade  e diga se ela
# começa ou não com o nome "SANTO"

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() =='SANTO')



(DESAFIO 25)
# Crie um programa que leia o nome de uma pessoa e diga se ela tem
# "SILVA" no nome.

nome = str(input('Digite seu nome completo:  ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))


(DESAFIO 26)
 Faça um programa qie leia uma frase pelo teclado e mostre.
# Faça um programa que leia uma frase pelo teclado e mostre.
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a ultima vez.

frase = str(input('Digite uma frase')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))



(DESAFIO 27)
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o último nome separadamente.
# EX. Ana Maria de Souza
# EX. Ana
# EX. Souza

nome = str(input('Digite um nome completo de uma pessoa: '))
nome = nome.strip()
nomes = nome.split()
qtdNomes = len(nomes)
print('Primeiro nome: {}'.format(nomes[0]))
print('Último nome: {}'.format(nomes[qtdNomes - 1]))


(DESAFIO 28)
# ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR PENSAR EM UM NÚMERO INTEIRO
# ENTRE 0 E 5  E PEÇA PARA O USUARIO TENTAR DESCOBRIR QUAL FOI O NUMERO
# ESCOLHIDO PELO COMPUTADOR. O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU
# OU PERDEU.

from random import randint # este metodo faz 
from time import sleep     # este metodo faz apos a pergunta mostrar print('PROCESSANDO...')
computador = randint(0, 5) # Faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um numero 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei?  ')) # jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABENS! Você conseguiu vencer')
else:
    print('GANHEI!! Eu pensei no número {} e não no {}!'.format(computador, jogador))


(DESAFIO 29)
# ESCREVE UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO
# SE ELE ULTRAPASSAR 80 KM MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO
# A MULTA VAI CUSTAR R$ 7.00 POR CADA KM ACIMA DO LIMITE.

velocidade = float(input('Qual a velocidade do carro?  '))
if velocidade > 80:
    print('MULTADO!!! Você excedeu o limite permitido da via que é de 80km/h ')
    valor_da_multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(valor_da_multa))
print('Tenha um bom dia! Dirija com Segurança!!!')



(DESAFIO 30)
# CRIE UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E MOSTRE NA TELA SE ELA É PAR OU IMPAR

num = int(input('Digite um numero:  '))
resultado = num % 2
if resultado == 0:
    print('O numero {} é PAR'.format(num))
else:
    print('O numero {} é ÍMPAR'.format(num))


(DESAFIO 31)
# DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTANCIA DE UMA VIAGEM EM KM
# CALCULE O PREÇO DA PASSAGEM, COBRANDO R$ 0.50 POR KM PARA VIAGENS ATÉ 200KM
# E 0,45 PARA VIAGENS MAIS LONGAS.

# RESOLVENDO TIPO 1 #
distância = float(input('Qual a distância da viagem?  '))
print('Você está preste a comçar uma viagem de {}km.'.format(distância))
preço = distância * 0.50 if distância<=200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))

# RESOLVENDO TIPO 2 #
distancia = int(input('Qual a distância da viagem?  '))
print('Você está preste a começar uma viagem de {}km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da passagem será de R${:.2f}'.format(preco))



(DESAFIO 32)
# FAÇA UM PROGRAMA QUALQUER E MOSTRE SE ELE É BISSEXTO.

ano = int(input('Que ano quer analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))


from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))



(DESAFIO 33)
# FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL O MENOR

a = int(input('Primeira valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# VERIFICANDO QUEM É MENOR #
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é maior #
maior = a
if b > a and b >c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))



(DESAFIO 34)
# ESCREVA UM PROGRAMA QUE PERGUNTE O SALARIO DE UM FUNCIONARIO E CALCULE
# O VALOR DO SEU AUMENTO.
# PARA SALÁRIO SUPERIORES A 1.250,00, CALCULE UM AUMENTO DE 10%
# PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%

salário = float(input('Qual salrio do funcionario? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora. '.format(salário, novo))




(DESAFIO 35)
# DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS E DIGA AO USUARIO
# SE ELAS PODEM OU NÃO FORMAR UM TRIÂNGULO.
# R1 # R2 # R3
print('-='*20)
print('Analizador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento '))
r2 = float(input('Segundo segmento '))
r3 = float(input('Terceiro segmento '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!!! ')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!! ')



(DESAFIO 36)  
# Alterar a cor da variavél  

nome = 'Rafael'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[3m',
         'pretoebranco':'\33[7:30'}
print('Olá!! Muito prazer em te conhecer, {}{}{}!!'.format(cores['azul'], nome, cores['limpa']))



(DESAFIO 36.a)
# de uma casa. o programa vai perguntar o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que elea não pode exceder 30%
# do saláriou então o emprestimoseá negado.

casa = float(input('Qual valor da casa? R$ '))
salário = float(input( 'Qual o valor do seu salario? '))
anos = int(input('Em quantos anos você que pagar a casa? '))
prestação = casa /(anos * 10)
minimo = salário * 30 / 100

print(' Para pagar uma casa de R%{:.2f}) em {} anos'.format(casa, anos), end='')
print('A prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo pode ser consedido!!!!')
else:
    print('Empréstimo NEGADO!!! ')



(DESAFIO 37)
# Escreva um programa que leia um número inteiro qualquer e peça para o
# usuario escolher qual será abase de convrsão:
#-1 para binário
#-2 para octal
#-3 para hexadecimal

num = int(input(' Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão: 
 [1] converter para BIANRIO
 [2] converter para OCTAL     
 [3] converter para HEXADECIMAl ''')

opção = int(input(' Sua opcão: '))
if opção == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)))
else:
    print('Opção invalida. Tente novamente  ')    


(DESAFIO 38)
# ESCREVA UM PROGRAMA QUE LEIA DOIS NUMEROS INTEIROS E COMPARE-OS
# MOSTRANDO NA TELA UMA MENSAGEM:
# O PRIMEIRO VALOR É MENOR
# O SEGUNDO VALOR É MAIOR
# NÃ0 EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS

n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite o outro numero inteiro: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O SEGUNDO valor é maior ')
else:
    print('Os dois valores são iguais ')



(DESAFIO 39)
#FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME DE ACORDO COM SUA IDADE
# SE ELE AINDA VAI SE ALISTAR O SERVIÇO MILITAR
# SE ´A HORA DE SE ALISTAR
# SE JÁ PASSOU DO TEMPO DO ALISTAMENTO
# SEU PROGRAMA TBM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU O PRAZO.

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce já deveria ter se alistado há {} anos .'.format(saldo))
    ano = atual - 18
    print ('Seu alistamento foi em {}'.format(ano))



(DESAFIO 40)
# CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MEDIA,
# MOSTRANDO UMA MENSAGEM NO FINAL DE ACORDO COM A MEDIA ATINGIDA:
## MEDIA ABAIXO DE 5.0: REPROVADO
## MEDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO
## MEDIA 7.0 OU SUPERIOR: APROVADO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Tirando  {:.1f} e {:.1f}, a média do aluno será {:.1f}'.format(n1, n2, media))
if 7 > media >= 5:
    print('O Aluno está em RECUPERAÇÃO ')
elif media < 5:
    print('O aluno está REPROVADO ')
elif media >=7:
    print('O aluno está APROVADO, parabens !!!!!')

#############################################################

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
if 7 > média >= 5:
    print('O aluno está em RECUPERACÃO. ')
elif média < 5:
    print('O aluno está REPROVADO.')
elif média >= 7:
    print('O aluno está APROVADO.')


(DESAFIO 41)    

