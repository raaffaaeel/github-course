APACHE SPARK - AULA RAFAEL ERLANCHER


DIA 1: SPARK CORE, ARQUITETURA, RDD, SPARK UI, YARN.

DIA 2: DATAFRAME API, HANDS ON, DESAFIO.

DIA 3: DATABRICKS.

DIA 4: SPARK ML, STRUCTURED, SPARK STREAMING. KAFTA.

DIA 5: SCALA, PARÂMETROS, CONFIGURAÇÕES, PERFOMANCE IN SPARK, TROUBLESHOOTING.


sc  - Sc para abrir SPARK CONTEXT


from pyspark.sql.functions import *
from pyspark.sql.types import * 

#comandos para ler o arquivo contar as linhas  #
path = "C:/AULA SPARK/rddExample.csv"

# comando para trazer arquivo em texto #
rdd1 = sc.textFile(path)

# comando´para contar as linhas do texto
rdd1.count()  

rdd1.toDebugString()

rdd1.take(2)  - traz duas linhas do arquivo.

rdd1Total = sc.wholeTextFiles(path) - ler todo arquivo.

rdd1 = sc.textFile(path) - ?

def soma1(x):  - # Essa função é para verdadeiro e falso
    return x + 1

soma1(4)


 #Essa função mais a informação abaixo mostra se verdadeiro e falso.
def filtro_header(x):  
        return x != "id|first_name|last_name|email|gender|ip_address"

rdd2 = rdd1.filter(filtro_header)

#"1|2|3".split("|") - Separar 

rdd3 = rdd2.map(lambda x: x.split("|"))  #função anonima 

#Metodo 1 para separa homen e mulher#
rdd4 = rdd3.keyBy(lambda x: x[4])
rdd4.countByKey().items()

# Metodo 2 para separa homen e mulher#
rdd4 = rdd3.keyBy(lambda x: x[4])
rdd5 = rdd4.groupByKey()
rdd5.map(lambda x: (x[0], len(x[1]))).collect()

# Criar Tabela do arquivo #
schema = ["id int", "first_name string", "last_name string", "email string", "gender string", "ip_address string"]

dfExample = spark.createDataFrame(rdd3, schema)

dfExample.show()

df = spark.read.csv(path, header=True, sep="|")

# Traz a tabela toda em coluna, inserir a quantidade que precisa trazer a coluna #
df.show()

# Traz os nomes das colunas #
df.printschema()




