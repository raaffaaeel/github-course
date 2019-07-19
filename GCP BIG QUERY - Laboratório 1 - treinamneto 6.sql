GCP BIG QUERY - Laboratório 1 - treinamneto 6 #

#Primeira consulta
Crie uma consulta que produza o tempo médio de viagem para viagens com origem no aeroporto de Frankfurt, na 
Alemanha (FRA) e destinado ao aeroporto em Kuala Lumpur, na Malásia (KUL), e agrupe os resultados por companhia aérea. 
Os tempos médios resultantes devem ser semelhantes.

  SELECT
  airline,
  AVG(minutes) AS media
FROM
 `qwiklabs-gcp-d52b35a1b75ae15c.JasmineJasper.triplog`
 WHERE
 origin='FRA' and destination='KUL'
 GROUP BY airline;
-----------------------------------------------------------------------
#Segunda consulta
Crie uma consulta que produza o tempo médio de viagem para viagens com origem no Aeroporto de Londres Heathrow, 
Reino Unido (LHR) e destinado ao aeroporto em Kuala Lumpur, Malásia (KUL), e agrupe os resultados por companhia 
aérea e encomende do menor para o maior . Os tempos médios resultantes devem revelar se a companhia aérea, a PlanePeople Air, 
manteve sua promessa de usar aviões mais rápidos do aeroporto de Heathrow.

SELECT
  airline,
  AVG(minutes) AS media
FROM
 `qwiklabs-gcp-d52b35a1b75ae15c.JasmineJasper.triplog`
 WHERE
 origin='LHR' and destination='KUL'
 GROUP BY airline
 ORDER BY media;

 -----------------------------------------------------------------------


 # LABORATÓRIO 2 -  TREINAMENTO 6 

 gsutil cp gs://cloud-training/preppde/benchmark.py gs://qwiklabs-gcp-93ac4096d3394702

 gsutil cp gs://cloud-training/preppde/ gs://qwiklabs-gcp-93ac4096d3394702/benchmark.py

 gsutil cp gs://cloud-training/preppde/benchmark.py gs://qwiklabs-gcp-93ac4096d3394702/benchmark.py


 -----------------------------------------------------------------------

 QWIKLABS TREINAMENTO 6

 Laboratório 1 > Criando um pipeline de transformação de dados com o Cloud Dataprep.

Você pode listar o nome da conta ativa com este comando:

> gcloud auth list <

Saída:

Credentialed accounts:
 - <myaccount>@<mydomain>.com (active)
Exemplo de saída:


Credentialed accounts:
 - google1623327_student@qwiklabs.net
Você pode listar o ID do projeto com este comando:

> gcloud config list project <

Saída:

[core]
project = <project_ID>
Exemplo de saída:

[core]
project = qwiklabs-gcp-44776a13dea667a6

 #standardSQL
 CREATE OR REPLACE TABLE ecommerce.all_sessions_raw_dataprep
 OPTIONS(
   description="Raw data from analyst team to ingest into Cloud Dataprep"
 ) AS
 SELECT * FROM `next-marketing-analytics.ecommerce.all_sessions_raw`
 WHERE date = '20170801'; # limiting to one day of data 56k rows for this lab

 name=CPSSinkConnector
connector.class=com.google.pubsub.kafka.sink.CloudPubSubSinkConnector
tasks.max=10
topics=to-pubsub
cps.topic=from-kafka
cps.project=qwiklabs-gcp-gcpd-4d3211b78b35


--------------------------------------------------------------------

* LABORATÓRIO 6 

> Prever tarifa de táxi com um modelo de previsão do BigQuery ML <


Explorar dados de táxi de táxi em Nova York
Pergunta: Quantas viagens os táxis amarelos receberam por mês em 2015?

Copie e cole o seguinte código SQL no Editor de Consultas:

#standardSQL
SELECT
  TIMESTAMP_TRUNC(pickup_datetime,
    MONTH) month,
  COUNT(*) trips
FROM
  `bigquery-public-data.new_york.tlc_yellow_trips_2015`
GROUP BY
  1
ORDER BY
  1



 > Pergunta: Qual foi a velocidade média das viagens de táxi amarelo em 2015? <

Substitua a consulta anterior pelo seguinte e clique em Executar :

#standardSQL
SELECT
  EXTRACT(HOUR
  FROM
    pickup_datetime) hour,
  ROUND(AVG(trip_distance / TIMESTAMP_DIFF(dropoff_datetime,
        pickup_datetime,
        SECOND))*3600, 1) speed
FROM
  `bigquery-public-data.new_york.tlc_yellow_trips_2015`
WHERE
  trip_distance > 0
  AND fare_amount/trip_distance BETWEEN 2
  AND 10
  AND dropoff_datetime > pickup_datetime
GROUP BY
  1
ORDER BY
  1

------------------------------------------------------------------------

> Sua equipe decide testar se esses campos abaixo são boas entradas para seu modelo de previsão de tarifas <

Quantidade de pedágios
Valor da Tarifa
Hora do dia
Endereço de levantamento
Deixar o endereço
Número de passageiros
Substitua a consulta pelo seguinte:

#standardSQL
WITH params AS (
    SELECT
    1 AS TRAIN,
    2 AS EVAL
    ),

  daynames AS
    (SELECT ['Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat'] AS daysofweek),

  taxitrips AS (
  SELECT
    (tolls_amount + fare_amount) AS total_fare,
    daysofweek[ORDINAL(EXTRACT(DAYOFWEEK FROM pickup_datetime))] AS dayofweek,
    EXTRACT(HOUR FROM pickup_datetime) AS hourofday,
    pickup_longitude AS pickuplon,
    pickup_latitude AS pickuplat,
    dropoff_longitude AS dropofflon,
    dropoff_latitude AS dropofflat,
    passenger_count AS passengers
  FROM
    `nyc-tlc.yellow.trips`, daynames, params
  WHERE
    trip_distance > 0 AND fare_amount > 0
    AND MOD(ABS(FARM_FINGERPRINT(CAST(pickup_datetime AS STRING))),1000) = params.TRAIN
  )

  SELECT *
  FROM taxitrips


# OBS:

Observe algumas coisas sobre a consulta:

A parte principal da consulta está na parte inferior ( SELECT * from taxitrips).
taxitripsfaz a maior parte da extração para o conjunto de dados de NYC, SELECTcontendo os recursos de treinamento e o rótulo.
Os WHEREdados remove que você não quer treinar por diante.
O WHEREtambém inclui uma cláusula de amostragem para coletar apenas 1/1000 dos dados.
Defina uma variável chamada TRAINpara que você possa criar rapidamente um EVALconjunto independente .
Agora que você entendeu melhor a finalidade dessa consulta, clique em Executar .
  _________________________________________________________________________________



> Digite a seguinte consulta para criar um modelo e especificar opções de modelo <

CREATE or REPLACE MODEL taxi.taxifare_model
OPTIONS
  (model_type='linear_reg', labels=['total_fare']) AS

WITH params AS (
    SELECT
    1 AS TRAIN,
    2 AS EVAL
    ),

  daynames AS
    (SELECT ['Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat'] AS daysofweek),

  taxitrips AS (
  SELECT
    (tolls_amount + fare_amount) AS total_fare,
    daysofweek[ORDINAL(EXTRACT(DAYOFWEEK FROM pickup_datetime))] AS dayofweek,
    EXTRACT(HOUR FROM pickup_datetime) AS hourofday,
    pickup_longitude AS pickuplon,
    pickup_latitude AS pickuplat,
    dropoff_longitude AS dropofflon,
    dropoff_latitude AS dropofflat,
    passenger_count AS passengers
  FROM
    `nyc-tlc.yellow.trips`, daynames, params
  WHERE
    trip_distance > 0 AND fare_amount > 0
    AND MOD(ABS(FARM_FINGERPRINT(CAST(pickup_datetime AS STRING))),1000) = params.TRAIN
  )

  SELECT *
  FROM taxitrips


  ___________________________________________________________________________________


 > Avaliar o desempenho do modelo de classificação <

Selecione seus critérios de desempenho
Para modelos de regressão linear, você deseja usar uma métrica de perda, como o Root Mean Square Error (RMSE) . Você deseja continuar treinando e melhorando o modelo até que ele tenha o menor RMSE.

Em BQML, mean_squared_erroré um campo de consulta ao avaliar seu modelo de ML treinado. Adicione um SQRT()para obter o RMSE.

Agora que o treinamento está concluído, você pode avaliar o desempenho do modelo com essa consulta ML.EVALUATE. Copie e cole o seguinte no editor de consultas e clique em Executar :

#standardSQL
SELECT
  SQRT(mean_squared_error) AS rmse
FROM
  ML.EVALUATE(MODEL taxi.taxifare_model,
  (

  WITH params AS (
    SELECT
    1 AS TRAIN,
    2 AS EVAL
    ),

  daynames AS
    (SELECT ['Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat'] AS daysofweek),

  taxitrips AS (
  SELECT
    (tolls_amount + fare_amount) AS total_fare,
    daysofweek[ORDINAL(EXTRACT(DAYOFWEEK FROM pickup_datetime))] AS dayofweek,
    EXTRACT(HOUR FROM pickup_datetime) AS hourofday,
    pickup_longitude AS pickuplon,
    pickup_latitude AS pickuplat,
    dropoff_longitude AS dropofflon,
    dropoff_latitude AS dropofflat,
    passenger_count AS passengers
  FROM
    `nyc-tlc.yellow.trips`, daynames, params
  WHERE
    trip_distance > 0 AND fare_amount > 0
    AND MOD(ABS(FARM_FINGERPRINT(CAST(pickup_datetime AS STRING))),1000) = params.EVAL
  )

  SELECT *
  FROM taxitrips

  ))
Agora você está avaliando o modelo contra um conjunto diferente de viagens de táxi com seu params.EVALfiltro.

Depois que o modelo for executado, revise os resultados do modelo (o valor do RMSE do modelo irá variar um pouco).


___________________________________________________________________________________


> Preveja o valor da tarifa de táxi
Em seguida, você escreverá uma consulta para usar seu novo modelo para fazer previsões. Copie e cole o seguinte no editor de consultas e clique em Executar :

#standardSQL
SELECT
*
FROM
  ml.PREDICT(MODEL `taxi.taxifare_model`,
   (

 WITH params AS (
    SELECT
    1 AS TRAIN,
    2 AS EVAL
    ),

  daynames AS
    (SELECT ['Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat'] AS daysofweek),

  taxitrips AS (
  SELECT
    (tolls_amount + fare_amount) AS total_fare,
    daysofweek[ORDINAL(EXTRACT(DAYOFWEEK FROM pickup_datetime))] AS dayofweek,
    EXTRACT(HOUR FROM pickup_datetime) AS hourofday,
    pickup_longitude AS pickuplon,
    pickup_latitude AS pickuplat,
    dropoff_longitude AS dropofflon,
    dropoff_latitude AS dropofflat,
    passenger_count AS passengers
  FROM
    `nyc-tlc.yellow.trips`, daynames, params
  WHERE
    trip_distance > 0 AND fare_amount > 0
    AND MOD(ABS(FARM_FINGERPRINT(CAST(pickup_datetime AS STRING))),1000) = params.EVAL
  )

  SELECT *
  FROM taxitrips

));
Agora você verá as previsões do modelo para tarifas de táxi juntamente com as tarifas reais e outros 
recursos para esses passeios. Seus resultados devem ser semelhantes aos abaixo:

___________________________________________________________________________________



