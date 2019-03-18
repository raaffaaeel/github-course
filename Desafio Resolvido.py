Desafio resolvido.

# TASK 1: Tratamentos iniciais

Passos do desafio:

ATENÇÃO: CADA ID REPRESENTA UM USUÁRIO!

# TASK 1: Tratamentos iniciais
1. Carregar o CSV com os dados dos usuarios (OK)

2. Preencher as linhas nulas na coluna saldo por 0

3. Separar dois dataframes:
    1. Contendo somente os usuários que não são vip
    
    2. Contendo somente os usuários que são vip

# TASK 2 (Precisa do resultado da task 1): Balance mais recente
4. Para cada usuário vip, calcular o seu saldo mais recente e gravar em uma nova coluna "RecentBalance".
    Salvar em um arquivo no formato csv com:
        somente os usuários com o saldo mais recente maior que 90.0
        sem duplicidades
        em um unico arquivo
        ordenado pelo RecentBalance de maneira decrescente
        com separador '|'
        com header no arquivo

# TASK 3 (Precisa do resultado da task 1): Filtros nos usuários vips + AvgBalance
Para os usuários vips
5. Filtrar somente homens
6. Agrupar por "id" (usuários) e tirar a média de saldo em uma nova coluna "AvgBalance"


# TASK 4 (Precisa do resultado da task 1): Filtos nos usuários não vips + AvgBalance
Para os usuários não vips
7. Filtrar somente mulheres com data de acesso entre 2019-01-19 e 2019-01-24.
8. Agrupar por "id" (usuários) e calcular a média de saldo em uma nova coluna "AvgBalance"

# TASK 5 (Precisa do resultado das tasks 3 e 4) Union dos dois Dataframes + resultado final
9. Realizar um union entre os dois dataframes resultantes das tasks 3 e 4, ordernar por AvgBalance de maneira crescente e gravar em um arquivo csv com header e separador ",".

# TASK FINAL: Criar um script.py, e submeter o codigo utilizando spark-submit

1. Carregar o CSV com os dados dos usuarios (OK)

from pyspark.sql.session import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("Users").getOrCreate()
sc = spark.sparkContext
sc.setLogLevel("ERROR")

#path = "FileStore/tables/users.csv"
dfUsers = spark.table("users_csv")

# TASK 1

# Preencher as linhas nulas na coluna saldo por 0

dfUsers2 = dfUsers.withColumn("balance", when(col("balance").isNull(), lit(0)).otherwise(col("balance")))

#Separar dois dataframes:
   # 1. Contendo somente os usuários que não são vip
    
   # 2. Contendo somente os usuários que são vip

usersVip = dfUsers2.filter(col("vip") == "true")
usersNotVip = dfUsers2.filter(col("vip") == "false")# != true 'diferente'
display(usersVip)

# TASK 2
# Para cada usuário vip, calcular o seu saldo mais recente e gravar em uma nova coluna "RecentBalance".
# Salvar em um arquivo no formato csv com:
# somente os usuários com o saldo mais recente maior que 90.0
# sem duplicidades
# em um unico arquivo
# ordenado pelo RecentBalance de maneira decrescente
# com separador '|'
# com header no arquivo

from pyspark.sql.functions import to_timestamp
from pyspark.sql.types import DateType

dfChangeType = usersVip.withColumn('date_access', from_unixtime(unix_timestamp('date_access', 'dd/MM/yyyy')).alias('date').cast(DateType()))

window = Window.partitionBy("id").orderBy(desc("date_access"))

RecentBalanceUsersVipTemp = dfChangeType.withColumn("RankBalance", row_number().over(window)).where(col("RankBalance") == 1).select(col("Balance").alias("RecentBalance"), "date_access", "id")
display(RecentBalanceUsersVipTemp)

display(RecentBalanceUsersVipTemp)

# somente os usuários com o saldo mais recente maior que 90.0
RecentBalanceUsersVip = usersVip.join(RecentBalanceUsersVipTemp, "id")
RecentBalanceUsersVip = RecentBalanceUsersVip.select("id", "RecentBalance", "gender", "balance", "vip" ).where(col("RecentBalance")>90.0).distinct().orderBy(desc("RecentBalance"))

outputPathCsv = "/FileStore/tables/resultado.csv"

# Salvar em um arquivo no formato csv com:
RecentBalanceUsersVip.repartition(1).write.csv(outputPathCsv, mode="overwrite", header=True, sep='|')

# TASK 3
usersVipFinal = usersVip.filter(col("gender") == "Male").groupBy("id").agg(avg(col("Balance")).alias("AvgBalance"))

display(usersVipFinal)


# TASK 4
usersNotVipFinal = usersNotVip.where(col("gender") == "Female").where(col("date_access").between('08/01/2019', '08/12/2019')).groupBy("id").agg(avg(col("Balance")).alias("AvgBalance"))

display(usersNotVipFinal)

# TASK 5
UsersFinal = usersVipFinal.union(usersNotVipFinal).orderBy(asc("AvgBalance"))

outputPathCsv = "/FileStore/tables/ResultCsv.csv"

UsersFinal.repartition(1).write.csv(outputPathCsv, header=True, mode="overwrite", sep=",")