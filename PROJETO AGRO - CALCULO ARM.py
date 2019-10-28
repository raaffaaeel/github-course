PROJETO AGRO - CALCULO ARM

from pyspark.sql import udf
from pyspark.sql.functions import monotonically_increasing_id
import math

def calcula_arm_2(PETP, ARM_ANTERIOR, CAD):
  if PETP >= 0:
    return ARM_ANTERIOR+PETP
  else:
    return ARM_ANTERIOR*math.exp(PETP/CAD)


def calcula_arm_1(PETP, ARM_ANTERIOR, CAD):
  if calcula_arm_2(PETP, ARM_ANTERIOR, CAD)>CAD:
    return CAD
  else:
    return calcula_arm_2(PETP, ARM_ANTERIOR, CAD)


def generate_arm(df):
    rows = df.select('DC', 'P-ETP', 'CAD', 'row_id').collect()
    ARM_ANT = None
    ARM_LIST = []
    
    for row in rows:
        if row['DC'] == 1:
            ARM_ANT = row['CAD']
        
        ARM = calcula_arm_1(row['P-ETP'], ARM_ANT, row['CAD'])
        ARM_LIST.append((float(ARM), row['row_id']))
        ARM_ANT = ARM
    
    return ARM_LIST


df_ETPKc_PETP_with_id = df_ETPKc_PETP \
    .orderBy('RefT', col('Datas').asc(), 'DC') \
    .withColumn('row_id', monotonically_increasing_id())
arm_list = generate_arm(df_ETPKc_PETP_with_id)
df_ARM_ONLY = spark.createDataFrame(
    data=arm_list, schema=['ARM', 'row_id'])
df_ARM = df_ETPKc_PETP_with_id.join(df_ARM_ONLY, 'row_id').drop('row_id')

