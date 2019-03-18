DESAFIO SPARK

Passos do desafio:

# TASK 1: Tratamentos iniciais
1. Relacionar o Json de usuários com o csv de usuários pelo campo "id"
2. Preencher as linhas nulas na coluna saldo por 0
3. Separar dois dataframes:
	1. Contendo somente os usuários que não são vip
	2. Contendo somente os usuários que são vip

# TASK 2 (Precisa do resultado da task 1): Balance mais recente
4. Para cada usuário vip, calcular o seu saldo mais recente e gravar em uma nova coluna "RecentBalance".
	Salvar em um arquivo no formato Json com:
		o nome e o sobrenome de cada usuário junto com seu saldo mais recente, porém somente os usuários com o saldo mais recente maior que 90.0
		sem duplicidades
		em um unico arquivo
		ordenado pelo RecentBalance de maneira decrescente

# TASK 3 (Precisa do resultado da task 1): Filtros nos usuários vips + AvgBalance
Para os usuários vips
5. Filtrar somente homens que tenham sobrenome que comece com a letra "d"
6. Feito o passo 5, agrupar por first_name, last_name e id e calcular a média de saldo em uma nova coluna "AvgBalance"


# TASK 4 (Precisa do resultado da task 1): Filtos nos usuários não vips + AvgBalance
Para os usuários não vips
7. Filtrar somente mulheres com data de acesso entre 2019-01-19 e 2019-01-24.
8. Feito o passo 7, agrupar por first_name, last_name e id e calcular a média de saldo uma nova coluna "AvgBalance"

# TASK 5 (Precisa do resultado das tasks 3 e 4) Union dos dois Dataframes + resultado final
Realizar um union entre os dois dataframes resultantes, ordernar por AvgBalance de maneira crescente e gravar em um arquivo csv.

# TASK FINAL: Criar um script.py, e submeter o codigo utilizando spark-submit


path = "C:/AULA SPARK DESAFIO/"


from pyspark.sql.functions import *
from pyspark.sql.types import * 

path = "C:/AULA SPARK DESAFIO/"

pathuserscsv = path + "users_info.csv"
pathusersjson = path + "users_json.json"

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("first_name", StringType(), True),
    StructField("last_name", StringType(), True),
    StructField("gender", StringType(), True),
    StructField("vip", StringType(), True),
    StructField("balance", DecimalType(20,2), True),
    ])

	dfuserscsv = spark.read.csv(pathuserscsv, schema=
		schema, header=True, sep=",")

dfusersjson = spark.read.json(pathusersjson, multiLine=True)
dfusersjson.show()

dfusersjson2 = dfusersjson.select("users.*")
dfusersjson2.show()

usersjoin = dfusersjson2.join(dfuserscsv, "id")
usersjoin.show()	

usersjoin0 = Usersjoin.fillna({'balance': 0})
usersjoin0.show()

usersNVIP = usersjoin0.where(usersjoin0.vip == "false")
usersNVIP.show()

usersVIP = usersjoin0.where(usersjoin0.vip == "true")
usersVIP.show()

	########################


#############################################

# 13.03.2019 _ Desafio #

from pyspark.sql.types import *
from pyspark.sql.functions import *

path="C:/Spark/Aulas/Dia2/"

pathUsersCSV = path + "users_info.csv"
pathUsersJson = path + "users_json.json"

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("first_name", StringType(), True),
    StructField("last_name", StringType(), True),
    StructField("gender", StringType(), True),
    StructField("vip", StringType(), True),
    StructField("balance", DecimalType(20,2), True),
    ])


dfUsersCSV = spark.read.csv(pathUsersCSV, schema=schema, header=True, sep=",")

dfUsersJson = spark.read.json(pathUsersJson, multiLine=True)
dfUsersJson2 = dfUsersJson.select("users.*")

UsersJoin = dfUsersJson2.join(dfUsersCSV, "id")

UsersJoin0 = UsersJoin.fillna({'balance': 0})

UsersNVIP = UsersJoin0.where(UsersJoin0.vip == "false")
UsersVIP = UsersJoin0.where(UsersJoin0.vip == "true")

usersjoin = dfusersjson2.join(dfuserscsv, "id")
