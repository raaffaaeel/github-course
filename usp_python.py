print('Eu serei expert em python')

10
type(10)
<class 'int'>

type("tudo bem")
<class 'str'>

5 / 2
<2.5>

type(5 / 2)
<float>

10 // 3
<3>

10 % 3
<1>

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

