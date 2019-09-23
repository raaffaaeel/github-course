LER CSV VIA PYTHON 

## Eu estou com uma dificuldade no delimitador das células do arquivo CSV, quando mando o comando de salvar o 
## arquivo editado em CSV escritor.writerow([linhas]) o delimitador por padrão é a ,, mais eu preciso alterar para ; 
## pois quando eu abro o arquivo no Excel, ele não reconhece a quebra das células com ,, então fica 
## tudo em uma coluna só. Meu codigo esta assim:

import csv

coluna_Heading = 0
coluna_Number = 1

with open("testeIfHeading00.csv", "r") as arquivo_lido, open("saida.csv", "w", newline= "") as arquivo_criado:

    #def o leitor CSV do arquivo
    leitor = csv.reader(arquivo_lido, delimiter=';')

    #def o escritor CSV do arquivo
    escritor = csv.writer(arquivo_criado, delimiter=';')

    #percorre as linhas do arquivo a ser lido
    separatec = " "
    for linhas in leitor:
        if (len(linhas[coluna_Number]) == 1) or len(linhas[coluna_Number]) <= 2:
            separatec = linhas[coluna_Heading]
        linhas.append(separatec)

        print(linhas)


