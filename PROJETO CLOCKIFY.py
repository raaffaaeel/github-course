PROJETO CLOCKIFY

# Importar o arquivo .csv ou excel

# Inserir este arquivo no Blob

# Usar Databricks para ler o arquivo no Blob e separar as informações.

#1#
from pyspark.sql.types import *
from pyspark.sql.functions import *
import pandas as pd

#2#
dbutils.fs.unmount("/mnt/clockify")

#3#
AccountName = "alphateam"
fullname = "fs.azure.account.key." +AccountName+ ".blob.core.windows.net"
AccountKey = "LcTgpCIfUlo9KvTLjjoYCdHZXM0+bDteYJ+3Kdef13mUOm72tWrVR307TH6rY7RkjY2ZWyGBZv4BhrrApDh4pQ=="
Container = "clockify"
accountsource = "wasbs://"+Container+"@" +AccountName+ ".blob.core.windows.net/"
pathToMount = 'clockify'

dbutils.fs.mount(source = accountsource,
mount_point = "/mnt/"+str(pathToMount),
extra_configs = {fullname : AccountKey})


#4#
%fs

ls /mnt/clockify/2019


#5# Ler Excel 
dfclockify = pd.read_excel('/dbfs/mnt/clockify/2019/clockify_report_04-01-2019_to_04-30-2019.xlsx', 'Clockify report', index_col=None)


#6# Transforma dataframe em .csv
dfclockify.to_csv('/dbfs/mnt/clockify/2019/clockify_report_04-01-2019_to_04-30-2019.csv', encoding='utf-8')

#7# Rodar Schema
schemaclockify = StructType([
	StructField("Project", StringType(), True),
	StructField("Client", StringType(), True),
	StructField("Time", StringType(), True),
	StructField("Task", StringType(), True),
	StructField("User", StringType(), True),
	StructField("Email", StringType(), True),
	StructField("Tags", StringType(), True),
	StructField("Billable", StringType(), True),
	StructField("Start Date", DateType(), True),
	StructField("Start Time", DateType(), True),
    StructField("End Date", DateType(), True),
    StructField("End Time", DateType(), True),
	StructField("Duration (h)", DateType(), True),
	StructField("Duration (decimal)", DecimalType(), True),
	StructField("Hourly Rate (USD)", DecimalType(), True),
	StructField("Amount (USD)", DecimalType(), True)	
	])


#8# Ler o arquivo CSV após conversão
dfcsvclockify = spark.read.csv("dbfs:/mnt/clockify/2019/clockify_report_04-01-2019_to_04-30-2019.csv", header=True, sep=',', encoding='UTF-8', inferSchema='true')

#9# Mostrar tabela.
display(dfcsvclockify)

#10# Fazer o select das colunas necessarias.

dfclockify = pd.read_excel('/dbfs/mnt/clockify/2019/clockify_report_04-01-2019_to_04-30-2019.xlsx', 'Clockify report', index_col=None)





