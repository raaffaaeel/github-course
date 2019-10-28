PYTHON USP

# colocqndo 2 variaveis #
peso = 78
altura = 1.83

print (peso)
print (altura)

# buscando o indice de massa corporal, peso / altura elevado ao quadrado #
IMC = peso / (altura ** 2)
IMC

IMCinteiro = int(IMC)
IMCinteiro

# escrevendo variavel e contando caracter #
texto = "Bom dia, tudo bem"
len(texto)
17

# alterando uma variavel para string #
temp = str(texto)
'Bom dia, tudo bem'

# alterando uma variavel para string #
temp = str(IMC)
temp
'23.291229956104985'


len(temp)
18

------------------------

temperaturaFahrenheit = 98 

temperaturaCelsius = (float(temperaturaFahrenheit) - 32) * 5 / 9

print ("A temperatura em celsius é", temperaturaCelsius)

A temperatura em celsius é >25.555555555555557<

------------------------

temperaturaFahrenheit = input("Digite uma temperatura em Fahrenheit:  ")

temp = float(temperaturaFahrenheit)

temperaturaCelsius = (temperaturaFahrenheit - 32) * 5 / 9

-----------------------

nomeDamae = input("Qual o nome da sua mãe? ")
nomeDoPai = input("Qual o nome do seu Pai? ")

print("Bom dia Sra.", nomeDamae, "!!! E Bom dia Sr." nomeDoPai, ",")


>>>>>>>>>>>>> Tarefa de programação: Lista de exercícios - 1 <<<<<<<<<<<<<<<<<<<<

"""Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, calcule e imprima (saída de dados) seu perímetro e sua área.

Observação: a saída deve estar no formato: "perímetro: x - área: y"

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

Entrada de Dados:
Digite o valor correspondente ao lado de um quadrado: 3

Saída de Dados:
perímetro: 12 - área: 9

Dica: lembre-se que um quadrado tem quatro lados iguais, logo só é necessário pedir o lado uma vez """

Resposta > ok
lado = a = int(input("Digite o lado do quadrado: ? "))
perimetro  = lado *4
area = lado * lado
print("perimetro:", perimetro, "-", "area:", area)

Resposta2:
lado=int(input("Digite o lado do quadrado:"))
         
perimetro  = lado *4
area = lado * lado

print(" area:", area,)
print("perimetro:", perimetro )

>>>>>>>>>>>> Tarefa de programação: Lista de exercícios 2 <<<<<<<<<<<<<<<<<<<

"""Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética. Observe o exemplo abaixo:

Exemplo:

Entrada de Dados:
Digite a primeira nota: 4

Digite a segunda nota: 5

Digite a terceira nota: 6

Digite a quarta nota: 7

Saída de Dados:
A média aritmética é 5.5"""

Resposta > ok
p1 = float(input("Digite a primeira nota:"))
p2 = float(input("Digite a segunda nota:"))
p3 = float(input("Digite a terceira nota:"))
p4 = float(input("Digite a quarta nota:"))
media = (p1 + p2 + p3 + p4) / 4
print("Média aritmética: ",media)

........................................................

#CALCULAR TEMPO #
segundos_str = input("Por favor, entre com número de segundos que deseja converter: ")
total_segs = int(segundos_str)

dias = total_segs // 86400
horas = total_segs // 3600
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(dias, "dias", horas, "horas ", minutos, "minutos e", segs_restantes_final, "segundos.")


>>>>>>>>>>>> Tarefa de programação: Lista de exercícios 3 <<<<<<<<<<<<<<<<<<<

#Uma empresa de cartão de crédito envia suas faturas por email com a seguinte mensagem:
#Escreva um programa que receba (entrada de dados através do teclado) o nome do cliente, o dia de vencimento, o mês de vencimento e o valor da 
#fatura e imprima (saída de dados) a mensagem com os dados recebidos, no mesmo formato da mensagem acima. Note que o programa imprime a saída em 
#duas linhas diferentes. Note também que, como não é preciso realizar cálculos, o valor não precisa ser convertido para número, pode ser tratado como texto.


nome = input("Digite o nome do cliente")
dia = input("Digite o dia de vencimento")
mes = input("Digite o mês de vencimento")
valor = input("Digite o valor da fatura")

print("Olá,", nome)
print("A sua fatura com vencimento em", dia, "de", mes, "no valor de r$", valor,"esta fechada.")


"""
Reescreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja, faça um programa em Python que, dada a quantidade de segundos, "quebre" esse valor em dias, horas, minutos e segundos. A saída deve estar no formato: a dias, b horas, c minutos e d segundos. Seja cuidadoso com o formato! Espaços a mais, vírgulas faltando ou outras diferenças são considerados erro

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

Entrada de Dados:
Por favor, entre com o número de segundos que deseja converter: 178615

Saída de Dados:
2 dias, 1 horas, 36 minutos e 55 segundos. """

segundos_str = input("Por favor, entre com número de segundos que deseja converter: ")
total_segs = int(segundos_str)

dias = total_segs // 86400
horas = total_segs // 3600
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(dias, "dias", horas, "horas ", minutos, "minutos e", segs_restantes_final, "segundos.")



"""
Exercício 3
Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas. Observe o exemplo abaixo:

Exemplo 1:

Entrada de Dados:
Digite um número inteiro: 78615

Saída de Dados:
O dígito das dezenas é 1

Exemplo 2:

Entrada de Dados:
Digite um número inteiro: 2

Saída de Dados:
O dígito das dezenas é 0

Dica: O operador "//" faz uma divisão inteira jogando fora o resto, ou seja, aquilo que é menor que o divisor. O operador "%" devolve apenas o resto da divisão inteira jogando fora o resultado, ou seja, tudo que é maior ou igual ao divisor.

How to submit
When you're ready to submit, you can upload files for each part of the assignment on the "My submission" tab."""

n = int (input("Digite um número inteiro: ")) 
d = (n // 10) % 10 
print()
print("O dígito das dezenas é", d)

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


> execução condicional <

tenperatura = 102
if temperatura > 100:
	aguaferve = True
	evaporacao = "muito rápido"


aguaferve

evaporacao

---------------

tempodejogo = int(input("Quando tempo temos já jpgando? "))

if tempodejogo <= 90:
	print("Ainda tem jogo pela frente")
	print("Que bom, eu adoro futebol")
else:
	print("Putz, tá acabando o jogo")
	print("Apita logo, juiz!!!!")


>>>>>>>>>>>>>>>  DESAFIO IF e ELSE <<<<<<<<<<<<<<<


import math
 
a = float(input("Digite um valor para a: "))
b = float(input("Digite um valor para b: "))
c = float(input("Digite um valor para c: "))
 
delta = b ** 2 - 4 * a * c

if delta == 0:
	raiz1 = (-b + math.sqtr(delta)) / (2 * a)
	print("A única raiz é: ", raiz1)
else:
	if delta < 0:
		print("Esta equação não possui raizes reais")
	else:	
		raiz1 = (-b + math.sqtr(delta)) / (2 * a)
		raiz2 = (-b - math.sqtr(delta)) / (2 * a)
		print("A primeira raiz é : ", raiz1)
		print("A segunda raiz é :", raiz2)

Versão 2

import math

def delta(a, b, c):
		return b ** 2 - 4 * a * c

def main():
		a = float(input("Digite um valor para a: "))
        b = float(input("Digite um valor para b: "))
        c = float(input("Digite um valor para c: ")) 
        imprime_raizes(a, b, c)

def imprime_raizes(a, b, c):
		if delta(a, b, c) == 0:
				raiz1 = (-b + math.sqtr(delta(a, b, c))) / (2 * a)
				print("A única raiz é: ", raiz1)
		else:
				if delta(a, b, c) < 0:
						print("Esta equação nãp possui raizes reais")
				else: 
						raiz1 = (-b + math.sqtr(delta(a, b, c))) / (2 * a)
						raiz2 = (-b + math.sqtr(delta(a, b, c))) / (2 * a)
						print("A primeira raiz é : ", raiz1)
						print("A segunda raiz é : ", raiz2)						        




>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


Exercício 1 - Par ou ímpar?
Receba um número inteiro na entrada e imprima

par

quando o número for par ou

ímpar

quando o número for ímpar.

R:
#sabendo se o numero e par ou impar.

numero = float(input('Digite um número para saber se é par ou impar:'))
resto = numero % 2

if resto == 0:
    print('Número é par')
else:
    print('Número é impar')



Exercícios 2 - FizzBuzz parcial, parte 1
Receba um número inteiro na entrada e imprima

Fizz

se o número for divisível por 3. Caso contrário, imprima o mesmo número que foi dado na entrada.

R:
# Exercícios 2 - FizzBuzz parcial, parte 1

n = int (input ("fizz"))
if (n % 3 == 0):
	print ("fizz")
else:
	print ("",n)



Exercícios 3 - FizzBuzz parcial, parte 2
Receba um número inteiro na entrada e imprima

Buzz

se o número for divisível por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

R:

m = int (input ("Buzz"))
if (m % 5 == 0):
	print ("Buzz")
else:
	print ("",m)


Exercícios 4 - FizzBuzz parcial, parte 3
Receba um número inteiro na entrada e imprima

FizzBuzz

na saída se o número for divisível por 3 e por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

R: 

def fizz_buzz(n):
    for num in range(n):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)

print(fizz_buzz())


Exercício 5 - Verificando ordenação
Receba 3 números inteiros na entrada e imprima

crescente

se eles forem dados em ordem crescente. Caso contrário, imprima

não está em ordem crescente

R:

num1 = int(input("Digite o primeiro número"))
num2 = int(input("Digite o segundo número"))
num3 = int(input("Digite o terceiro número"))
if num1 < num2 and num2 < num3:
	print("Crescente")

else:
	print("Não está na ordem crescente")




>>>>>>>>>>>>>>>>>>>>>>>> SEMANA 4 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


WHILE

i = 0

while i <= 10:
	print(2 ** i)
	i = i + 1


print("Digite uma sequência de valores terminados por zero.")
soma = 0

valor = 13
while valor != 0:
	valor = int(input("Digite um valor a ser somado: "))
	soma = soma + valor

print("A soma dos valores digitados é: ", soma)


--------------------------------------------------------


tamanho = int(input("Digite o tamanho da sequência de números: "))

produto = 1
i = 0

while i < tamanho:
	valor = int(input("Digite um valor a ser mutiplicado: "))
	produto = produto * valor
	i = i + 1

print("A produto dos valores digitados é: ", produto)


-------------------------------------------------------

Exemplo como pegar ultimo numero e os 3 primeiro

x = 6532

x % 10

x // 10
-------------------------------------------------------


>>>>>  Ordem decrecente  <<<<<<

decrescente = True
anterior = int(input("Digite o primeiro número da sequência: "))

valor = 1

while valor != 0 and decrescente:
	valor = int(input("Digite um número da sequência: "))
	if valor > anterior: 
		decrescente = False
	anterior = valor 	

if decrescente:
	print("A sequência está em ordem decrescente! :-) ")
else:	
	print("A sequência não está em ordem decrescente! :-( ")

-------------------------------------------------------

Exemplo de indicador de passagem.

meuCartão = int(input("Digite o número do seu cartão de crédito"))

cartãoLido = 1
encontreimeuCartãoNaLista = False

while cartãoLido != 0 and not encontreimeuCartãoNaLista:
	cartãoLido= int(input("Digite o número do proximo cartão de crédito: "))
	if cartãoLido == meuCartão:
		encontreimeuCartãoNaLista = True

if encontreimeuCartãoNaLista:
	print("EBA!!! Meu cartão está lá")
else:
	print("XII!!! Meu cartão não está lá")


-------------------------------------------------------

# CONSTA AS QUANTIDADES DE IMPARES E PARES DIGITADOS E FINALIZA APOS DIGITAR 0.


terminou = False
p = i = 0
while (not terminou):
    n = int(input("Digite um número, ou zero para terminar: "))
    if n == 0:
        terminou = True
    else:
        if n % 2 == 0:
            p = p + 1
        else:
            i = i + 1

print ("P = ", p)
print ("I = ", i)


-------------------------------------------------------


SEMANA 4  - Tarefa de programação: Lista de exercícios - 3

Exercício 1
Escreva um programa que receba um número natural nn na 
entrada e imprima n! (fatorial) na saída.

Exemplo:

Dica: lembre-se que o fatorial de 0 vale 1!

Digite o valor de n: 5
120

n = int(input("Digite o valor de n: "))
 
fatorial = 1
 
while (n > 0):
    fatorial = fatorial * n
    n -= 1
 
print(fatorial)

---------------------------------------------------------

Exercício 2
Receba um número inteiro positivo na entrada e imprima os nn primeiros números ímpares naturais. 
Para a saída, siga o formato do exemplo abaixo.

Exemplo:
Resposta

n = int(input("Digite o valor de n: "))

i = 0
ímpar = 1

while i < n: 
  print(ímpar)
  i = i + 1
  ímpar = ímpar + 2


------------------------------------------------------


Exercício 3
Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

Exemplo:

Dica: Para separar os dígitos, lembre-se: o operador "//" faz uma divisão inteira jogando fora o resto, ou seja, 
aquilo que é menor que o divisor; O operador "%" devolve apenas o resto da divisão inteira jogando fora o resultado, 
ou seja, tudo que é maior ou igual ao divisor.
	
x = int(input("Numero: "))

soma = 0

while (x != 0):
    resto = x % 10
    x = (x - resto)//10
    soma = soma + resto
print(soma)


------------------------------------------------------	


>>>> Funções <<<<


def >>> Difinindo uma nova função <<<<

def soma ( x, y, z):
	return x + y + z

def multiplica (x, y, z):
	return x * y * z

def nome_do_seu_time ():  # ESSA FUNÇÃO SÓ RETORNA NOME DO SPC
	return "SPFC"

def quieta():
	x =	10 + 20
	print("O valor calculado é ", x)	


print (soma(10, 20, 30))
print (soma(-20, 100, 200))	

print (soma(12345, 4321)
print (soma(20*32, soma(3, 4))
print (soma(10, 30, 100)

multiplica(soma(20, 40, 7), soma(65, 3, 2), multiplica(2, 3, 4))
-------------------------------------------------------

Teste fatorial

def fatorial(n):
	fat = 1 
	while (n > 1):
		fat = fat * n
		n = n - 1


def testa_fatorial():
	if fatorial(1) == 1:
		print("Funciona para 1")
	else:
		print("Não funciona para 1")	
	if fatorial(2) == 2:
		print("Funciona para 2")
	else:
		print("Não funciona para 2")
	if fatorial(0) == 1:
		print("Funciona para 0")
	else:
		print("Não funciona para 0")
	if fatorial(5) == 120:
		print("Funciona para 5")
	else:
		print("Não funciona para 5")


testa_fatorial()



>>>> Calcular binomial <<<<

def numero_binominal(n, k):
	return fatorial(n) / (fatorial(k) * fatorial(n-k))



>>>> Testes automatizados <<<<
	

def fatorial (n):
	if n < 0:
		return 0
	i = fat = 1
	while i <= n:
		fat = fat * i
		i = i + 1
	return fat
	

def test_fatorial0():
	assert fatorial(0) == 1

def test_fatorial1():
	assert fatorial(1) == 1	 

def test_fatorial_negativo():
	assert fatorial(-10) == 0

def test_fatorial4():
	assert fatorial(4) == 24

def test_fatorial5():
	assert fatorial(5) == 120	


----------------------------------------------


>>>>>>>>>>>>>>>  Tarefa de programação: Lista de exercícios - 4  <<<<<<<<<<<<<<<<<<<

Exercício 1 - Máximo
Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.

Exemplos de execução no shell do Python:

def maximo(x, y):
    if x > y :
        return x
    else :
        return y


maximo(3,4)        

maximo(0, -1)


--------------------------------------------------------------------------------------------

Exercício 2 - Primos
Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior 
número primo menor ou igual ao número passado à função

Exemplos de execução no shell do Python:

def ehPrimo(k):
    divisores = 0
    for divisor in range(1, k):
        if k % divisor == 0:
            divisores = divisores + 1
        if divisores > 1:
          break
    if divisores > 1:
        return False
    else:
        return True

def maior_primo(x):
    primo = x
    i = 0
    while i <= x:
        if ehPrimo(i):
            primo = i
        i = i + 1
    return primo


maior_primo(100)

maior_primo(7)


Dica: escreva uma função éPrimo(k) e faça um laço percorrendo os números até o número dado checando se o número é primo
ou não; se for, guarde numa variável. Ao fim do laço, o valor armazenado na variável é o maior primo encontrado.



--------------------------------------------------------------------------------------------

Exercício 3 - Vogais
Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.

Exemplos de execução no shell de Python


def vogal(x):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if x in vogais:
        return True
    elif x.isalpha():
        return False
    else:
        return False


vogal("a")
vogal("b")
vogal("E")



Os valores True e False devolvidos devem ser do tipo bool (booleanos), e não strings

Dica: Lembre-se que para passar uma vogal como parâmetro ela precisa ser um texto, ou seja, precisa estar entre aspas.

-------------------------------------------------------------------------------------------


>>>>>>>>>>>  Tarefa de programação: Programa completo - Jogo do NIM <<<<<<<<<<<<<<<<<<<<


 Jogo do NIM

 Você conhece o jogo do NIM? Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro. Dois jogadores jogam alternadamente, retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.

Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente.

Objetivo
Você deverá escrever um programa na linguagem Python, versão 3, que permita a uma "vítima" jogar o NIM contra o computador. O computador, é claro, deverá seguir a estratégia vencedora descrita acima.

Sejam n o número de peças inicial e m o número máximo de peças que é possível retirar em uma rodada. Para garantir que o computador ganhe sempre, é preciso considerar os dois cenários possíveis para o início do jogo:

Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida com a frase "Você começa"
Caso contrário, o computador toma a inciativa de começar o jogo.
Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador. Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.

Seu trabalho, então, será implementar o Jogo e fazer com que o computador se utilize da estratégia vencedora.

Seu Programa
Com o objetivo do EP já definido, uma dúvida que deve surgir nesse momento é como modelar o jogo de forma que possa ser implementado em Python 3 correspondendo rigorosamente às especificações descritas até agora.

Para facilitar seu trabalho e permitir a correção automática do exercício, apresentamos a seguir um modelo, isto é, uma descrição em linhas gerais de um conjunto de funções que resolve o problema proposto neste EP. 
Embora sejam possíveis outras abordagens, é preciso atender exatamente o que está definido abaixo para que a correção automática do trabalho funcione corretamente.

O programa deve implementar:

Uma função computador_escolhe_jogada que recebe, como parâmetros, os números n e m descritos acima e devolve um inteiro correspondente à próxima jogada do computador de acordo com a estratégia vencedora.
Uma função usuario_escolhe_jogada que recebe os mesmos parâmetros, solicita que o jogador informe sua jogada e verifica se o valor informado é válido. Se o valor informado for válido, a função deve devolvê-lo;
caso contrário, deve solicitar novamente ao usuário que informe uma jogada válida.
Uma função partida que não recebe nenhum parâmetro, solicita ao usuário que informe os valores de n e m e inicia o jogo, alternando entre jogadas do computador e do usuário (ou seja, chamadas às duas funções anteriores). 
A escolha da jogada inicial deve ser feita em função da estratégia vencedora, como dito anteriormente. A cada jogada, deve ser impresso na tela o estado atual do jogo, ou seja, quantas peças foram removidas na última jogada e quantas restam na mesa. 
Quando a última peça é removida, essa função imprime na tela a mensagem "O computador ganhou!" ou "Você ganhou!" conforme o caso.
Observe que, para isso funcionar, seu programa deve sempre "lembrar" qual é o número de peças atualmente no tabuleiro e qual é o máximo de peças a retirar em cada jogada.

Cuidado: o corretor automático não funciona bem se você tiver alguma chamada a input() antes da definição de todas as funções do jogo (a menos que essa chamada esteja dentro de uma função). Se seu programa usar input() 
sem que ele esteja dentro de alguma função, coloque-o no final do programa.

Campeonatos
Como todos sabemos, uma única rodada de um jogo não é suficiente para definir quem é o melhor jogador. Assim, uma vez que a função partida esteja funcionando, você deverá criar uma outra função chamada campeonato. 
Essa nova função deve realizar três partidas seguidas do jogo e, ao final, mostrar o placar dessas três partidas e indicar o vencedor do campeonato. O placar deve ser impresso na forma

Placar: Você ??? X ??? Computador

Execução
Dado que é possível jogar partidas individuais ou campeonatos, seu programa deve começar solicitando ao usuário que escolha se prefere jogar apenas uma partida (opção 1) ou um campeonato (opção 2).

Veja um exemplo de como deve funcionar o jogo:


 def usuario_escolhe_jogada(n, m):
    print()
    while True:
        num = int(input("Quantas peças você vai tirar? "))
        if num > m or (n - num) < 0:
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()
        else:
            if num < 2:
                print("Você tirou uma peça.")
            else:
                print("Voce tirou", num, "peças.")
            return num

def multiplo(n, m):
    achou = False
    if(n % (m+1)) == 0:
        achou = True
    return achou

def computador_escolhe_jogada(n, m):
    print()
    qtd = 0
    if n <= m:
        qtd =  n
    else:
        if multiplo(n, m):
            qtd = m
        else:
            pc = 0
            while pc % (m + 1) != n % (m + 1):
                pc = pc + 1
                if pc % (m + 1) == n % (m + 1):
                    qtd = pc
                    break
    if qtd < 2:
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou",qtd,"peças.")
    return qtd

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if multiplo(n, m):
        print()
        print("Voce começa!")
        jogador = 1
    else:
        print()
        print("Computador começa!")
        jogador = 0

    while n > 0:

        if jogador == 0:
            n = n - computador_escolhe_jogada(n, m)
            jogador = 1
        else:
            n = n - usuario_escolhe_jogada(n, m)
            jogador = 0
        if n == 0 and jogador == 0:
            print("Fim do jogo! Você ganhou!")
            break
        elif n == 0 and jogador == 1:
            print("Fim do jogo! O computador ganhou!")
            break

        if n < 2:
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            print("Agora restam",n,"peças no tabuleiro.")

def campeonato():
    print("\nVoce escolheu um campeonato!\n")
    rodada = 1
    while rodada <= 3:
        print("**** Rodada",rodada,"****")
        print()
        partida()
        print()
        rodada = rodada + 1
    print("**** Final do campeonato! ****\n")
    print("Placar: Você 0 X",(rodada-1),"Computador")

print("Bem-vindo ao jogo do NIM! Escolha:\n")
op = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
if op == 1:
    print("\nVoce escolheu uma partida isolada\n")
    partida()
elif op == 2:
    campeonato()


>>>>>>>>>>>>> Tarefa de programação: Lista de exercícios - 5  <<<<<<<<<<<<<

Exercício 1


Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes 
à largura e à altura de um retângulo, respectivamente. O programa deve imprimir uma cadeia de caracteres que represente o 
retângulo informado com caracteres '#' na saída.

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
while altura > 0:
    x = 0
    while x < largura:
        print("#" , end = '') 
        x+=1
    altura = altura - 1
    print()

----------------------------------------------------------------------------

Exercício 2

# -*- coding: utf-8 -*-
largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
ALT = altura
LARG = largura
while altura > 0:
    x = 0
    while x < largura:
        if altura == (ALT) or x == (LARG - 1) or altura == 1 or x == 0:
            print("#" , end = '')
        else: 
            print(" " , end = '')
        x+=1
    altura = altura - 1
    print()


--------------------------------------------------------------------------

>>>>>>>>>>>>> Tarefa de programação: Lista de exercícios - 6  <<<<<<<<<<<<<

Tarefa de programação: Lista de exercícios - 6
Atividade não enviada. Você deve obter 16/20 pontos para passar.
Prazo	
Seja aprovado nessa tarefa até 24 de Nov de 22:59 PST
InstruçõesMeus enviosDiscussões


Exercício 1 - Removendo elementos repetidos
Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista 
possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.

Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?


def remove_repetidos(lista):
    nova_lista = []
    for i in lista :
        if i not in nova_lista :
            nova_lista.append(i)
    return sorted(nova_lista)


-----------------------------------------------------------------------



Exercício 2 - Soma dos elementos de uma lista
Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente à soma dos elementos da lista recebida.

def soma_elementos(lista):
    soma = 0
    for i in lista :
      soma = soma + i
    return soma


-----------------------------------------------------------------------


>>>>>>>>>>>>> Tarefa de programação: Lista de exercícios - 7  <<<<<<<<<<<<<


Tarefa de programação: Programa completo - Similaridades entre textos - Caso COH-PIAH

Introdução
John é monitor na matéria de Introdução à Produção Textual I na Penn State University (PSU). Durante esse período, John descobriu que uma epidemia de COH-PIAH estava se espalhando pela PSU. Essa doença rara e altamente contagiosa faz com que as pessoas contaminadas produzam textos extremamente semelhantes de forma involuntária. Após a entrega da primeira redação, John desconfiou que alguns alunos estavam sofrendo de COH-PIAH. John, se preocupando com a saúde da turma, resolveu buscar um método para identificar os casos de COH-PIAH. Para isso, ele necessita da sua ajuda para desenvolver um programa que o auxilie a identificar os alunos contaminados.

Detecção de autoria
Utilizando diferentes estatísticas do texto, é possível identificar aspectos que funcionam como uma “assinatura” do autor. Diferentes pessoas possuem diferentes estilos de escrita, algumas preferindo sentenças mais curtas, outras preferindo sentenças mais longas.

Essas “assinatura” pode ser utilizada para detecção de plágio, evidência forense, ou nesse caso, para detectar a grave doença COH-PIAH.

Traços linguísticos
Nesse exercício utilizaremos as seguintes estatísticas para detectar a doença:

Tamanho médio de palavra: Média simples do número de caracteres por palavra.
Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
Razão Hapax Legomana: Número de palavras utilizadas uma vez dividido pelo número total de palavras.
Tamanho médio de sentença: Média simples do número de caracteres por sentença.
Complexidade de sentença: Média simples do número de frases por sentença.
Tamanho médio de frase: Média simples do número de caracteres por frase.
Funcionamento do programa
Diversos estudos foram compilados e hoje se conhece precisamente a assinatura de um portador de COH-PIAH. Seu programa deverá receber diversos textos e calcular os valores dos diferentes traços linguísticos da seguinte forma:

Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 4 diferentes (o, gato, caçava, rato). Nessa frase, a relação Type-Token vale \frac{4}{5} = 0.8 
5
4
​	 =0.8
Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 3 que aparecem só uma vez (gato, caçava, rato). Nessa frase, a relação Hapax Legomana vale \frac{3}{5} = 0.6 
5
3
​	 =0.6
Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença).
Complexidade de sentença é o número total de frases divido pelo número de sentenças.
Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).
Após calcular esses valores para cada texto, você deve comparar com a assinatura fornecida para os infectados por COH-PIAH. O grau de similaridade entre dois textos, aa e bb, é dado pela fórmula:

S_{ab} = \frac{\sum_{i=1}^6 || f_{i,a} - f_{i,b} ||}{6}S 
ab
​	 = 
6
∑ 
i=1
6
​	 ∣∣f 
i,a
​	 −f 
i,b
​	 ∣∣
​	 

Onde:

S_{ab}S 
ab
​	  é o grau de similaridade entre os textos aa e bb;
f_{i,a}f 
i,a
​	  é o valor de cada traço linguístico ii no texto aa; e
f_{i,b}f 
i,b
​	  é o valor de cada traço linguístico ii no texto bb.
Perceba que quanto mais similares aa e bb forem, menor S_{ab}S 
ab
​	  será. Para cada texto, você deve calcular o grau de similaridade com a assinatura do portador de COH-PIAH e no final exibir qual o texto que mais provavelmente foi escrito por algum aluno infectado.


import re

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):\n")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):\n")

    return textos

def separa_palavras(frase):
    #A funcao recebe um texto e devolve uma lista das palavras dentro dele
    return frase.split()

def separa_sentencas(texto):
    #A funcao recebe um texto e devolve uma lista das sentencas dentro do texto
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas
    
def separa_frases(sentenca):
    #A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca
    return re.split(r'[,:;]+', sentenca)

def n_palavras_diferentes(lista_palavras):
    #Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def n_palavras_unicas(lista_palavras):
    #Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras(texto):
    return len(lista_palavras(texto))

def caractere_palavras(texto):
    stnc = separa_sentencas(texto)
    frs = list()
    for i in stnc:
        x = separa_frases(i)
        frs += x
    plvr = list()
    for i in frs:
        x = separa_palavras(i)
        plvr += x
        
    s = 0
    for i in plvr:
        s += len(i)
    return s

def caractere_sentencas(texto):
    stnc = separa_sentencas(texto)
    frs = 0
    for i in stnc:
        x = len(i)
        frs += x
    return frs

def caractere_frases(texto):
    stnc = separa_sentencas(texto)
    frs = list()
    for i in stnc:
        x = separa_frases(i)
        frs += x
    plvr = 0
    for i in frs:
        x = len(i)
        plvr += x
    return plvr

def conta_frases(texto):
    c = separa_sentencas(texto)
    frases = []
    for w in c:
        f = separa_frases(w)
        frases += f
    return len(frases)

def conta_sentencas(texto):
    return len(separa_sentencas(texto))

def lista_palavras(texto):
    stnc = separa_sentencas(texto)
    frs = list()
    for i in stnc:
        x = separa_frases(i)
        frs += x
    plvr = list()
    for i in frs:
        x = separa_palavras(i)
        plvr += x
    return plvr

def wal(texto):
    return caractere_palavras(texto) / n_palavras(texto)

def ttr(texto):
    return n_palavras_diferentes(lista_palavras(texto)) / n_palavras(texto)

def hlr(texto):
    return n_palavras_unicas(lista_palavras(texto)) / n_palavras(texto)

def sal(texto):
    return caractere_sentencas(texto) / conta_sentencas(texto)

def sac(texto):
    return conta_frases(texto) / conta_sentencas(texto)

def pal(texto):
    return caractere_frases(texto) / conta_frases(texto)
    
def calcula_assinatura(texto):
    
    vwal = wal(texto)
    #print("Tamanho medio de palavra: ", vwal)
    vttr = ttr(texto)
    #print("Relação Type-Token: ", vttr)
    vhlr = hlr(texto)
    #print("Razão Hapax Legomana: ", vhlr)
    vsal = sal(texto)
    #print("Tamanho médio de sentença: ", vsal)
    vsac = sac(texto)
    #print("Complexidade média da sentença: ", vsac)
    vpal = pal(texto)
    #print("Tamanho medio de frase: ", vpal)
    return [vwal, vttr, vhlr, vsal, vsac, vpal]
    

def compara_assinatura(ass_cp,as_b):
    i = 0
    x = 0
    s = 0
    ca = list()
    while i<=5:
        x = ass_cp[i]-as_b[i]
        if x<0:
            ca.append(x*-1)
        else:
            ca.append(x)
        i += 1
    
    for i in ca:
        x = i
        s += x
    
    return s/6
    
    
    
    

def avalia_textos(lista_textos, ass_cp):
    ca = []
    for i in lista_textos:
        as_b = calcula_assinatura(i)
        ca.append(as_b)
    cpa = []
    for i in ca:
        x = compara_assinatura(ass_cp,i)
        cpa.append(x)
    return cpa.index(min(cpa))+1
        
        
    
        
        
    
    
ass_cp = le_assinatura()

lista_textos = le_textos()

print ('O autor do texto', avalia_textos(lista_textos, ass_cp), 'está infectado com COH-PIAH')