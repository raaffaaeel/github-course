## ESTE SCRIPT TEM FINALIDADE DE LER O ARQUIVO E TRANSFORMAR EM JSON ##

#!/usr/bin/python

import sys

#print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))

path = sys.argv[1]
filename = sys.argv[2]


data = ""
with open(path + filename) as file:
   data = file.read()

listaColunas = str(data).split(',')
print(listaColunas)

modeloColunaMapeada = ''',{ 
  "source": { 
    "type": "typeSource",
    "ordinal": ordinalSource
  },
  "sink": {
    "name": "nameSink",
    "type": "typeSink"
  }
}'''

stringColunasMapeadasFinal = ""
ordinal = 1
for i in listaColunas:
    stringColunasMapeadasFinal += modeloColunaMapeada\
        .replace('typeSource', 'String')\
        .replace('ordinalSource', str(ordinal))\
        .replace('nameSink', str(i))\
        .replace('typeSink', 'String')

    ordinal += 1


resultFinal = '''
"columnmapping": {
    "type": "TabularTranslator",
    "mappings": [
''' + stringColunasMapeadasFinal[1:] + '''
]
}
'''


with open(path + 'mapping_' + filename, 'w') as file:
    file.write(resultFinal)


