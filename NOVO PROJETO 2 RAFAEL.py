NOVO PROJETO 2 - 18.03.2019

# No data Bricks foi criado notebook PROJETO 2.
#Conectando com Azure Blob com Data Bricks #
AccountName = "alphateam"
AccountKey = "IJ4ArIYPvgDe+qUMJhUGDwxYjDmFZDZMtYAznO1CHCIUlqY9cQTVcP3zgD9EYGHlvEIUcNHqKuu+GnG4PpHrEA=="
Container = "curso001"
fullname = "fs.azure.account.key." +AccountName+ ".blob.core.windows.net"
accountsource = "wasbs://"+Container+"@" +AccountName+ ".blob.core.windows.net/"
pathToMount = 'ORDERS'  

# INSERIR AS BIBLIOTECAS PARA NÃO APARECER ERRO #

from pyspark.sql.session import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window
from pyspark.sql.functions import to_timestamp
from pyspark.sql.types import DateType

# CRIAÇÃO DA PASTA rafa #
dbutils.fs.mount(source = accountsource,
  mount_point = "/mnt/rafa",
  extra_configs = {fullname : AccountKey})

# NESTE MOMENTO A FUNÇÃO ABAIXO PARA BUSCAR O LOCAL DO ARQUIVO #
%fs
ls dbfs:/mnt/rafa/ORDERS/date_load=20190316/

# CRIAÇÃO DE 3 DATA FRAME #

dfArquivo00 = spark.read.csv ("dbfs:/mnt/rafa/ORDERS/date_load=20190316/HOUR_LOAD=00/", header=True)
display(dfArquivo00)


dfArquivo01 = spark.read.csv ("dbfs:/mnt/rafa/ORDERS/date_load=20190316/HOUR_LOAD=01/", header=True)
display(dfArquivo01)

dfArquivo04 = spark.read.csv ("dbfs:/mnt/rafa/ORDERS/date_load=20190316/HOUR_LOAD=04/", header=True)
display(dfArquivo04)

#######################################

Para dimensão de produtos sugiro utilizar essas colunas do arquivo que esta no BLOB:
,freedom_order.sr_sku
,freedom_order.shippings_products_productname (essa coluna que precisa sofrer datacleansing)

########

Para fato de pedidos separei as colunas abaixo, que possuem alguma informação de preço ou quantidade. Coloquei também
 a chave do produto e a chave do pedido:
,freedom_order.sr_order (chave do pedido)
,freedom_order.sr_sku (chave do produto)
,freedom_order.shippings_products_sku
,freedom_order.shippings_products_unitprice
,freedom_order.shippings_products_unitdiscount
,freedom_order.shippings_products_quantity
,freedom_order.shippings_products_netprice

########

# PROJETO 2 #

# Criando shema e tabelas no Mysql ##

SET GLOBAL time_zone = '+8:00'; 

# PROJETO 2 #

CREATE TABLE ods1.pedidos00 (
  `freedom_order_sr_order` text DEFAULT NULL,
  `freedom_order_sr_payments` text DEFAULT NULL,
  `freedom_order_sr_shipping` text DEFAULT NULL,
  `freedom_order_sr_customer` text DEFAULT NULL,
  `freedom_order_sr_sku` text DEFAULT NULL,
  `freedom_order_catalog` text DEFAULT NULL,
  `freedom_order_storecode` text DEFAULT NULL,
  `freedom_order_saledate` text DEFAULT NULL,
  `freedom_order_saleschannel` text DEFAULT NULL,
  `freedom_order_amount` text DEFAULT NULL,
  `freedom_order_subtotal` text DEFAULT NULL,
  `freedom_order_id_code` text DEFAULT NULL,
  `freedom_order_id_origin` text DEFAULT NULL,
  `freedom_order_id_country` text DEFAULT NULL,
  `freedom_order_customer_externalcode` text DEFAULT NULL,
  `freedom_order_customer_name` text DEFAULT NULL,
  `freedom_order_customer_email` text DEFAULT NULL,
  `freedom_order_customer_cpfcnpj` text DEFAULT NULL,
  `freedom_order_customer_inscricaoestadual` text DEFAULT NULL,
  `freedom_order_customer_birthdate` text DEFAULT NULL,
  `freedom_order_customer_createdate` text DEFAULT NULL,
  `freedom_order_customer_gender` text DEFAULT NULL,
  `freedom_order_customer_persontype` text DEFAULT NULL,
  `freedom_order_customer_phonenumber` text DEFAULT NULL,
  `freedom_order_customer_phoneddd` text DEFAULT NULL,
  `freedom_order_customer_mobilenumber` text DEFAULT NULL,
  `freedom_order_customer_mobileddd` text DEFAULT NULL,
  `freedom_order_customer_score` text DEFAULT NULL,
  `freedom_order_customer_address_country` text DEFAULT NULL,
  `freedom_order_customer_address_state` text DEFAULT NULL,
  `freedom_order_customer_address_statecode` text DEFAULT NULL,
  `freedom_order_customer_address_city` text DEFAULT NULL,
  `freedom_order_customer_address_street` text DEFAULT NULL,
  `freedom_order_customer_address_number` text DEFAULT NULL,
  `freedom_order_customer_address_district` text DEFAULT NULL,
  `freedom_order_customer_address_postalcode` text DEFAULT NULL,
  `freedom_order_customer_address_referencepoint` text DEFAULT NULL,
  `freedom_order_customer_address_description` text DEFAULT NULL,
  `freedom_order_customer_address_businessaddress` text DEFAULT NULL,
  `freedom_order_payments_cardholder` text DEFAULT NULL,
  `freedom_order_payments_expirationmonth` text DEFAULT NULL,
  `freedom_order_payments_expirationyear` text DEFAULT NULL,
  `freedom_order_payments_securitycode` text DEFAULT NULL,
  `freedom_order_payments_cardbrand` text DEFAULT NULL,
  `freedom_order_payments_installmentsnumber` text DEFAULT NULL,
  `freedom_order_payments_value` text DEFAULT NULL,
  `freedom_order_payments_optin` text DEFAULT NULL,
  `freedom_order_payments_externalcode` text DEFAULT NULL,
  `freedom_order_payments_paymentdate` text DEFAULT NULL,
  `freedom_order_payments_deliveryid` text DEFAULT NULL,
  `freedom_order_payments_typepayment` text DEFAULT NULL,
  `freedom_order_shippings_deliveryid` text DEFAULT NULL,
  `freedom_order_shippings_servicedelivery` text DEFAULT NULL,
  `freedom_order_shippings_deadlineindays` text DEFAULT NULL,
  `freedom_order_shippings_expecteddeliverydate` text DEFAULT NULL,
  `freedom_order_shippings_freight` text DEFAULT NULL,
  `freedom_order_shippings_canceledpayment` text DEFAULT NULL,
  `freedom_order_shippings_status` text DEFAULT NULL,
  `freedom_order_shippings_laststatusdate` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_date` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_username` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_externalcode` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_status` text DEFAULT NULL,
  `freedom_order_shippings_address_country` text DEFAULT NULL,
  `freedom_order_shippings_address_state` text DEFAULT NULL,
  `freedom_order_shippings_address_statecode` text DEFAULT NULL,
  `freedom_order_shippings_address_city` text DEFAULT NULL,
  `freedom_order_shippings_address_street` text DEFAULT NULL,
  `freedom_order_shippings_address_number` text DEFAULT NULL,
  `freedom_order_shippings_address_district` text DEFAULT NULL,
  `freedom_order_shippings_address_postalcode` text DEFAULT NULL,
  `freedom_order_shippings_address_referencepoint` text DEFAULT NULL,
  `freedom_order_shippings_address_description` text DEFAULT NULL,
  `freedom_order_shippings_address_businessaddress` text DEFAULT NULL,
  `freedom_order_shippings_recipient_name` text DEFAULT NULL,
  `freedom_order_shippings_recipient_cpfcnpj` text DEFAULT NULL,
  `freedom_order_shippings_recipient_birthdate` text DEFAULT NULL,
  `freedom_order_shippings_recipient_gender` text DEFAULT NULL,
  `freedom_order_shippings_recipient_persontype` text DEFAULT NULL,
  `freedom_order_shippings_recipient_phonenumber` text DEFAULT NULL,
  `freedom_order_shippings_recipient_phoneddd` text DEFAULT NULL,
  `freedom_order_shippings_recipient_mobilenumber` text DEFAULT NULL,
  `freedom_order_shippings_recipient_mobileddd` text DEFAULT NULL,
  `freedom_order_shippings_products_externalcode` text DEFAULT NULL,
  `freedom_order_shippings_products_sku` text DEFAULT NULL,
  `freedom_order_shippings_products_unitprice` text DEFAULT NULL,
  `freedom_order_shippings_products_unitdiscount` text DEFAULT NULL,
  `freedom_order_shippings_products_quantity` text DEFAULT NULL,
  `freedom_order_shippings_products_productname` text DEFAULT NULL,
  `freedom_order_shippings_products_freebie` text DEFAULT NULL,
  `freedom_order_shippings_products_netprice` text DEFAULT NULL,
  `freedom_order_shippings_carrier_id` text DEFAULT NULL,
  `freedom_order_shippings_carrier_tradingname` text DEFAULT NULL,
  `freedom_order_timestamp` text DEFAULT NULL,
  `freedom_order_shippings_sellerid` text DEFAULT NULL,
  `freedom_order_shippings_agreedate` text DEFAULT NULL,
  `freedom_order_device` text DEFAULT NULL,
  `freedom_order_utm_key` text DEFAULT NULL,
  `freedom_order_utm_value` text DEFAULT NULL,
  `freedom_order_unique_id` text DEFAULT NULL,
  `freedom_order_utm_key_id` text DEFAULT NULL,
  `freedom_order_date_publish_kafka` text DEFAULT NULL,
  `freedom_order_nm_country` text DEFAULT NULL,
  `freedom_order_date_load` text DEFAULT NULL,
  `freedom_order_hour_load` text DEFAULT NULL,
  `freedom_order_minute_load` text DEFAULT NULL
) ENGINE=INNODB DEFAULT CHARSET=utf8;

select * from ods1.pedidos00;

create database stage1;
use stage1;
CREATE TABLE stage1.pedidos00cleansing (
  `freedom_order_sr_order` text DEFAULT NULL,
  `freedom_order_sr_payments` text DEFAULT NULL,
  `freedom_order_sr_shipping` text DEFAULT NULL,
  `freedom_order_sr_customer` text DEFAULT NULL,
  `freedom_order_sr_sku` text DEFAULT NULL,
  `freedom_order_catalog` text DEFAULT NULL,
  `freedom_order_storecode` text DEFAULT NULL,
  `freedom_order_saledate` text DEFAULT NULL,
  `freedom_order_saleschannel` text DEFAULT NULL,
  `freedom_order_amount` text DEFAULT NULL,
  `freedom_order_subtotal` text DEFAULT NULL,
  `freedom_order_id_code` text DEFAULT NULL,
  `freedom_order_id_origin` text DEFAULT NULL,
  `freedom_order_id_country` text DEFAULT NULL,
  `freedom_order_customer_externalcode` text DEFAULT NULL,
  `freedom_order_customer_name` text DEFAULT NULL,
  `freedom_order_customer_email` text DEFAULT NULL,
  `freedom_order_customer_cpfcnpj` text DEFAULT NULL,
  `freedom_order_customer_inscricaoestadual` text DEFAULT NULL,
  `freedom_order_customer_birthdate` text DEFAULT NULL,
  `freedom_order_customer_createdate` text DEFAULT NULL,
  `freedom_order_customer_gender` text DEFAULT NULL,
  `freedom_order_customer_persontype` text DEFAULT NULL,
  `freedom_order_customer_phonenumber` text DEFAULT NULL,
  `freedom_order_customer_phoneddd` text DEFAULT NULL,
  `freedom_order_customer_mobilenumber` text DEFAULT NULL,
  `freedom_order_customer_mobileddd` text DEFAULT NULL,
  `freedom_order_customer_score` text DEFAULT NULL,
  `freedom_order_customer_address_country` text DEFAULT NULL,
  `freedom_order_customer_address_state` text DEFAULT NULL,
  `freedom_order_customer_address_statecode` text DEFAULT NULL,
  `freedom_order_customer_address_city` text DEFAULT NULL,
  `freedom_order_customer_address_street` text DEFAULT NULL,
  `freedom_order_customer_address_number` text DEFAULT NULL,
  `freedom_order_customer_address_district` text DEFAULT NULL,
  `freedom_order_customer_address_postalcode` text DEFAULT NULL,
  `freedom_order_customer_address_referencepoint` text DEFAULT NULL,
  `freedom_order_customer_address_description` text DEFAULT NULL,
  `freedom_order_customer_address_businessaddress` text DEFAULT NULL,
  `freedom_order_payments_cardholder` text DEFAULT NULL,
  `freedom_order_payments_expirationmonth` text DEFAULT NULL,
  `freedom_order_payments_expirationyear` text DEFAULT NULL,
  `freedom_order_payments_securitycode` text DEFAULT NULL,
  `freedom_order_payments_cardbrand` text DEFAULT NULL,
  `freedom_order_payments_installmentsnumber` text DEFAULT NULL,
  `freedom_order_payments_value` text DEFAULT NULL,
  `freedom_order_payments_optin` text DEFAULT NULL,
  `freedom_order_payments_externalcode` text DEFAULT NULL,
  `freedom_order_payments_paymentdate` text DEFAULT NULL,
  `freedom_order_payments_deliveryid` text DEFAULT NULL,
  `freedom_order_payments_typepayment` text DEFAULT NULL,
  `freedom_order_shippings_deliveryid` text DEFAULT NULL,
  `freedom_order_shippings_servicedelivery` text DEFAULT NULL,
  `freedom_order_shippings_deadlineindays` text DEFAULT NULL,
  `freedom_order_shippings_expecteddeliverydate` text DEFAULT NULL,
  `freedom_order_shippings_freight` text DEFAULT NULL,
  `freedom_order_shippings_canceledpayment` text DEFAULT NULL,
  `freedom_order_shippings_status` text DEFAULT NULL,
  `freedom_order_shippings_laststatusdate` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_date` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_username` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_externalcode` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_status` text DEFAULT NULL,
  `freedom_order_shippings_address_country` text DEFAULT NULL,
  `freedom_order_shippings_address_state` text DEFAULT NULL,
  `freedom_order_shippings_address_statecode` text DEFAULT NULL,
  `freedom_order_shippings_address_city` text DEFAULT NULL,
  `freedom_order_shippings_address_street` text DEFAULT NULL,
  `freedom_order_shippings_address_number` text DEFAULT NULL,
  `freedom_order_shippings_address_district` text DEFAULT NULL,
  `freedom_order_shippings_address_postalcode` text DEFAULT NULL,
  `freedom_order_shippings_address_referencepoint` text DEFAULT NULL,
  `freedom_order_shippings_address_description` text DEFAULT NULL,
  `freedom_order_shippings_address_businessaddress` text DEFAULT NULL,
  `freedom_order_shippings_recipient_name` text DEFAULT NULL,
  `freedom_order_shippings_recipient_cpfcnpj` text DEFAULT NULL,
  `freedom_order_shippings_recipient_birthdate` text DEFAULT NULL,
  `freedom_order_shippings_recipient_gender` text DEFAULT NULL,
  `freedom_order_shippings_recipient_persontype` text DEFAULT NULL,
  `freedom_order_shippings_recipient_phonenumber` text DEFAULT NULL,
  `freedom_order_shippings_recipient_phoneddd` text DEFAULT NULL,
  `freedom_order_shippings_recipient_mobilenumber` text DEFAULT NULL,
  `freedom_order_shippings_recipient_mobileddd` text DEFAULT NULL,
  `freedom_order_shippings_products_externalcode` text DEFAULT NULL,
  `freedom_order_shippings_products_sku` text DEFAULT NULL,
  `freedom_order_shippings_products_unitprice` text DEFAULT NULL,
  `freedom_order_shippings_products_unitdiscount` text DEFAULT NULL,
  `freedom_order_shippings_products_quantity` text DEFAULT NULL,
  `freedom_order_shippings_products_productname` text DEFAULT NULL,
  `freedom_order_shippings_products_freebie` text DEFAULT NULL,
  `freedom_order_shippings_products_netprice` text DEFAULT NULL,
  `freedom_order_shippings_carrier_id` text DEFAULT NULL,
  `freedom_order_shippings_carrier_tradingname` text DEFAULT NULL,
  `freedom_order_timestamp` text DEFAULT NULL,
  `freedom_order_shippings_sellerid` text DEFAULT NULL,
  `freedom_order_shippings_agreedate` text DEFAULT NULL,
  `freedom_order_device` text DEFAULT NULL,
  `freedom_order_utm_key` text DEFAULT NULL,
  `freedom_order_utm_value` text DEFAULT NULL,
  `freedom_order_unique_id` text DEFAULT NULL,
  `freedom_order_utm_key_id` text DEFAULT NULL,
  `freedom_order_date_publish_kafka` text DEFAULT NULL,
  `freedom_order_nm_country` text DEFAULT NULL,
  `freedom_order_date_load` text DEFAULT NULL,
  `freedom_order_hour_load` text DEFAULT NULL,
  `freedom_order_minute_load` text DEFAULT NULL
) ENGINE=INNODB DEFAULT CHARSET=utf8;

select * from stage1.pedidos00cleansing;

CREATE TABLE stage1.dimensao (
  freedom_order_sr_order TEXT DEFAULT NULL,
  freedom_order_sr_payments TEXT DEFAULT NULL,
  freedom_order_sr_shipping TEXT DEFAULT NULL,
  freedom_order_sr_customer TEXT DEFAULT NULL, 
  ) ENGINE=INNODB DEFAULT CHARSET=utf8;

SET GLOBAL time_zone = '+8:00'; 
drop table ods1.pedidos01;

CREATE TABLE ods1.pedidos01 (
  `freedom_order_sr_order` text DEFAULT NULL,
  `freedom_order_sr_payments` text DEFAULT NULL,
  `freedom_order_sr_shipping` text DEFAULT NULL,
  `freedom_order_sr_customer` text DEFAULT NULL,
  `freedom_order_sr_sku` text DEFAULT NULL,
  `freedom_order_catalog` text DEFAULT NULL,
  `freedom_order_storecode` text DEFAULT NULL,
  `freedom_order_saledate` text DEFAULT NULL,
  `freedom_order_saleschannel` text DEFAULT NULL,
  `freedom_order_amount` text DEFAULT NULL,
  `freedom_order_subtotal` text DEFAULT NULL,
  `freedom_order_id_code` text DEFAULT NULL,
  `freedom_order_id_origin` text DEFAULT NULL,
  `freedom_order_id_country` text DEFAULT NULL,
  `freedom_order_customer_externalcode` text DEFAULT NULL,
  `freedom_order_customer_name` text DEFAULT NULL,
  `freedom_order_customer_email` text DEFAULT NULL,
  `freedom_order_customer_cpfcnpj` text DEFAULT NULL,
  `freedom_order_customer_inscricaoestadual` text DEFAULT NULL,
  `freedom_order_customer_birthdate` text DEFAULT NULL,
  `freedom_order_customer_createdate` text DEFAULT NULL,
  `freedom_order_customer_gender` text DEFAULT NULL,
  `freedom_order_customer_persontype` text DEFAULT NULL,
  `freedom_order_customer_phonenumber` text DEFAULT NULL,
  `freedom_order_customer_phoneddd` text DEFAULT NULL,
  `freedom_order_customer_mobilenumber` text DEFAULT NULL,
  `freedom_order_customer_mobileddd` text DEFAULT NULL,
  `freedom_order_customer_score` text DEFAULT NULL,
  `freedom_order_customer_address_country` text DEFAULT NULL,
  `freedom_order_customer_address_state` text DEFAULT NULL,
  `freedom_order_customer_address_statecode` text DEFAULT NULL,
  `freedom_order_customer_address_city` text DEFAULT NULL,
  `freedom_order_customer_address_street` text DEFAULT NULL,
  `freedom_order_customer_address_number` text DEFAULT NULL,
  `freedom_order_customer_address_district` text DEFAULT NULL,
  `freedom_order_customer_address_postalcode` text DEFAULT NULL,
  `freedom_order_customer_address_referencepoint` text DEFAULT NULL,
  `freedom_order_customer_address_description` text DEFAULT NULL,
  `freedom_order_customer_address_businessaddress` text DEFAULT NULL,
  `freedom_order_payments_cardholder` text DEFAULT NULL,
  `freedom_order_payments_expirationmonth` text DEFAULT NULL,
  `freedom_order_payments_expirationyear` text DEFAULT NULL,
  `freedom_order_payments_securitycode` text DEFAULT NULL,
  `freedom_order_payments_cardbrand` text DEFAULT NULL,
  `freedom_order_payments_installmentsnumber` text DEFAULT NULL,
  `freedom_order_payments_value` text DEFAULT NULL,
  `freedom_order_payments_optin` text DEFAULT NULL,
  `freedom_order_payments_externalcode` text DEFAULT NULL,
  `freedom_order_payments_paymentdate` text DEFAULT NULL,
  `freedom_order_payments_deliveryid` text DEFAULT NULL,
  `freedom_order_payments_typepayment` text DEFAULT NULL,
  `freedom_order_shippings_deliveryid` text DEFAULT NULL,
  `freedom_order_shippings_servicedelivery` text DEFAULT NULL,
  `freedom_order_shippings_deadlineindays` text DEFAULT NULL,
  `freedom_order_shippings_expecteddeliverydate` text DEFAULT NULL,
  `freedom_order_shippings_freight` text DEFAULT NULL,
  `freedom_order_shippings_canceledpayment` text DEFAULT NULL,
  `freedom_order_shippings_status` text DEFAULT NULL,
  `freedom_order_shippings_laststatusdate` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_date` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_username` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_externalcode` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_status` text DEFAULT NULL,
  `freedom_order_shippings_address_country` text DEFAULT NULL,
  `freedom_order_shippings_address_state` text DEFAULT NULL,
  `freedom_order_shippings_address_statecode` text DEFAULT NULL,
  `freedom_order_shippings_address_city` text DEFAULT NULL,
  `freedom_order_shippings_address_street` text DEFAULT NULL,
  `freedom_order_shippings_address_number` text DEFAULT NULL,
  `freedom_order_shippings_address_district` text DEFAULT NULL,
  `freedom_order_shippings_address_postalcode` text DEFAULT NULL,
  `freedom_order_shippings_address_referencepoint` text DEFAULT NULL,
  `freedom_order_shippings_address_description` text DEFAULT NULL,
  `freedom_order_shippings_address_businessaddress` text DEFAULT NULL,
  `freedom_order_shippings_recipient_name` text DEFAULT NULL,
  `freedom_order_shippings_recipient_cpfcnpj` text DEFAULT NULL,
  `freedom_order_shippings_recipient_birthdate` text DEFAULT NULL,
  `freedom_order_shippings_recipient_gender` text DEFAULT NULL,
  `freedom_order_shippings_recipient_persontype` text DEFAULT NULL,
  `freedom_order_shippings_recipient_phonenumber` text DEFAULT NULL,
  `freedom_order_shippings_recipient_phoneddd` text DEFAULT NULL,
  `freedom_order_shippings_recipient_mobilenumber` text DEFAULT NULL,
  `freedom_order_shippings_recipient_mobileddd` text DEFAULT NULL,
  `freedom_order_shippings_products_externalcode` text DEFAULT NULL,
  `freedom_order_shippings_products_sku` text DEFAULT NULL,
  `freedom_order_shippings_products_unitprice` text DEFAULT NULL,
  `freedom_order_shippings_products_unitdiscount` text DEFAULT NULL,
  `freedom_order_shippings_products_quantity` text DEFAULT NULL,
  `freedom_order_shippings_products_productname` text DEFAULT NULL,
  `freedom_order_shippings_products_freebie` text DEFAULT NULL,
  `freedom_order_shippings_products_netprice` text DEFAULT NULL,
  `freedom_order_shippings_carrier_id` text DEFAULT NULL,
  `freedom_order_shippings_carrier_tradingname` text DEFAULT NULL,
  `freedom_order_timestamp` text DEFAULT NULL,
  `freedom_order_shippings_sellerid` text DEFAULT NULL,
  `freedom_order_shippings_agreedate` text DEFAULT NULL,
  `freedom_order_device` text DEFAULT NULL,
  `freedom_order_utm_key` text DEFAULT NULL,
  `freedom_order_utm_value` text DEFAULT NULL,
  `freedom_order_unique_id` text DEFAULT NULL,
  `freedom_order_utm_key_id` text DEFAULT NULL,
  `freedom_order_date_publish_kafka` text DEFAULT NULL,
  `freedom_order_nm_country` text DEFAULT NULL,
  `freedom_order_date_load` text DEFAULT NULL,
  `freedom_order_hour_load` text DEFAULT NULL,
  `freedom_order_minute_load` text DEFAULT NULL
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE ods1.pedidos04 (
  `freedom_order_sr_order` text DEFAULT NULL,
  `freedom_order_sr_payments` text DEFAULT NULL,
  `freedom_order_sr_shipping` text DEFAULT NULL,
  `freedom_order_sr_customer` text DEFAULT NULL,
  `freedom_order_sr_sku` text DEFAULT NULL,
  `freedom_order_catalog` text DEFAULT NULL,
  `freedom_order_storecode` text DEFAULT NULL,
  `freedom_order_saledate` text DEFAULT NULL,
  `freedom_order_saleschannel` text DEFAULT NULL,
  `freedom_order_amount` text DEFAULT NULL,
  `freedom_order_subtotal` text DEFAULT NULL,
  `freedom_order_id_code` text DEFAULT NULL,
  `freedom_order_id_origin` text DEFAULT NULL,
  `freedom_order_id_country` text DEFAULT NULL,
  `freedom_order_customer_externalcode` text DEFAULT NULL,
  `freedom_order_customer_name` text DEFAULT NULL,
  `freedom_order_customer_email` text DEFAULT NULL,
  `freedom_order_customer_cpfcnpj` text DEFAULT NULL,
  `freedom_order_customer_inscricaoestadual` text DEFAULT NULL,
  `freedom_order_customer_birthdate` text DEFAULT NULL,
  `freedom_order_customer_createdate` text DEFAULT NULL,
  `freedom_order_customer_gender` text DEFAULT NULL,
  `freedom_order_customer_persontype` text DEFAULT NULL,
  `freedom_order_customer_phonenumber` text DEFAULT NULL,
  `freedom_order_customer_phoneddd` text DEFAULT NULL,
  `freedom_order_customer_mobilenumber` text DEFAULT NULL,
  `freedom_order_customer_mobileddd` text DEFAULT NULL,
  `freedom_order_customer_score` text DEFAULT NULL,
  `freedom_order_customer_address_country` text DEFAULT NULL,
  `freedom_order_customer_address_state` text DEFAULT NULL,
  `freedom_order_customer_address_statecode` text DEFAULT NULL,
  `freedom_order_customer_address_city` text DEFAULT NULL,
  `freedom_order_customer_address_street` text DEFAULT NULL,
  `freedom_order_customer_address_number` text DEFAULT NULL,
  `freedom_order_customer_address_district` text DEFAULT NULL,
  `freedom_order_customer_address_postalcode` text DEFAULT NULL,
  `freedom_order_customer_address_referencepoint` text DEFAULT NULL,
  `freedom_order_customer_address_description` text DEFAULT NULL,
  `freedom_order_customer_address_businessaddress` text DEFAULT NULL,
  `freedom_order_payments_cardholder` text DEFAULT NULL,
  `freedom_order_payments_expirationmonth` text DEFAULT NULL,
  `freedom_order_payments_expirationyear` text DEFAULT NULL,
  `freedom_order_payments_securitycode` text DEFAULT NULL,
  `freedom_order_payments_cardbrand` text DEFAULT NULL,
  `freedom_order_payments_installmentsnumber` text DEFAULT NULL,
  `freedom_order_payments_value` text DEFAULT NULL,
  `freedom_order_payments_optin` text DEFAULT NULL,
  `freedom_order_payments_externalcode` text DEFAULT NULL,
  `freedom_order_payments_paymentdate` text DEFAULT NULL,
  `freedom_order_payments_deliveryid` text DEFAULT NULL,
  `freedom_order_payments_typepayment` text DEFAULT NULL,
  `freedom_order_shippings_deliveryid` text DEFAULT NULL,
  `freedom_order_shippings_servicedelivery` text DEFAULT NULL,
  `freedom_order_shippings_deadlineindays` text DEFAULT NULL,
  `freedom_order_shippings_expecteddeliverydate` text DEFAULT NULL,
  `freedom_order_shippings_freight` text DEFAULT NULL,
  `freedom_order_shippings_canceledpayment` text DEFAULT NULL,
  `freedom_order_shippings_status` text DEFAULT NULL,
  `freedom_order_shippings_laststatusdate` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_date` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_username` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_externalcode` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_status` text DEFAULT NULL,
  `freedom_order_shippings_address_country` text DEFAULT NULL,
  `freedom_order_shippings_address_state` text DEFAULT NULL,
  `freedom_order_shippings_address_statecode` text DEFAULT NULL,
  `freedom_order_shippings_address_city` text DEFAULT NULL,
  `freedom_order_shippings_address_street` text DEFAULT NULL,
  `freedom_order_shippings_address_number` text DEFAULT NULL,
  `freedom_order_shippings_address_district` text DEFAULT NULL,
  `freedom_order_shippings_address_postalcode` text DEFAULT NULL,
  `freedom_order_shippings_address_referencepoint` text DEFAULT NULL,
  `freedom_order_shippings_address_description` text DEFAULT NULL,
  `freedom_order_shippings_address_businessaddress` text DEFAULT NULL,
  `freedom_order_shippings_recipient_name` text DEFAULT NULL,
  `freedom_order_shippings_recipient_cpfcnpj` text DEFAULT NULL,
  `freedom_order_shippings_recipient_birthdate` text DEFAULT NULL,
  `freedom_order_shippings_recipient_gender` text DEFAULT NULL,
  `freedom_order_shippings_recipient_persontype` text DEFAULT NULL,
  `freedom_order_shippings_recipient_phonenumber` text DEFAULT NULL,
  `freedom_order_shippings_recipient_phoneddd` text DEFAULT NULL,
  `freedom_order_shippings_recipient_mobilenumber` text DEFAULT NULL,
  `freedom_order_shippings_recipient_mobileddd` text DEFAULT NULL,
  `freedom_order_shippings_products_externalcode` text DEFAULT NULL,
  `freedom_order_shippings_products_sku` text DEFAULT NULL,
  `freedom_order_shippings_products_unitprice` text DEFAULT NULL,
  `freedom_order_shippings_products_unitdiscount` text DEFAULT NULL,
  `freedom_order_shippings_products_quantity` text DEFAULT NULL,
  `freedom_order_shippings_products_productname` text DEFAULT NULL,
  `freedom_order_shippings_products_freebie` text DEFAULT NULL,
  `freedom_order_shippings_products_netprice` text DEFAULT NULL,
  `freedom_order_shippings_carrier_id` text DEFAULT NULL,
  `freedom_order_shippings_carrier_tradingname` text DEFAULT NULL,
  `freedom_order_timestamp` text DEFAULT NULL,
  `freedom_order_shippings_sellerid` text DEFAULT NULL,
  `freedom_order_shippings_agreedate` text DEFAULT NULL,
  `freedom_order_device` text DEFAULT NULL,
  `freedom_order_utm_key` text DEFAULT NULL,
  `freedom_order_utm_value` text DEFAULT NULL,
  `freedom_order_unique_id` text DEFAULT NULL,
  `freedom_order_utm_key_id` text DEFAULT NULL,
  `freedom_order_date_publish_kafka` text DEFAULT NULL,
  `freedom_order_nm_country` text DEFAULT NULL,
  `freedom_order_date_load` text DEFAULT NULL,
  `freedom_order_hour_load` text DEFAULT NULL,
  `freedom_order_minute_load` text DEFAULT NULL
) ENGINE=INNODB DEFAULT CHARSET=utf8;

use stage1;
CREATE TABLE stage1.pedidos01cleansing (
  `freedom_order_sr_order` text DEFAULT NULL,
  `freedom_order_sr_payments` text DEFAULT NULL,
  `freedom_order_sr_shipping` text DEFAULT NULL,
  `freedom_order_sr_customer` text DEFAULT NULL,
  `freedom_order_sr_sku` text DEFAULT NULL,
  `freedom_order_catalog` text DEFAULT NULL,
  `freedom_order_storecode` text DEFAULT NULL,
  `freedom_order_saledate` text DEFAULT NULL,
  `freedom_order_saleschannel` text DEFAULT NULL,
  `freedom_order_amount` text DEFAULT NULL,
  `freedom_order_subtotal` text DEFAULT NULL,
  `freedom_order_id_code` text DEFAULT NULL,
  `freedom_order_id_origin` text DEFAULT NULL,
  `freedom_order_id_country` text DEFAULT NULL,
  `freedom_order_customer_externalcode` text DEFAULT NULL,
  `freedom_order_customer_name` text DEFAULT NULL,
  `freedom_order_customer_email` text DEFAULT NULL,
  `freedom_order_customer_cpfcnpj` text DEFAULT NULL,
  `freedom_order_customer_inscricaoestadual` text DEFAULT NULL,
  `freedom_order_customer_birthdate` text DEFAULT NULL,
  `freedom_order_customer_createdate` text DEFAULT NULL,
  `freedom_order_customer_gender` text DEFAULT NULL,
  `freedom_order_customer_persontype` text DEFAULT NULL,
  `freedom_order_customer_phonenumber` text DEFAULT NULL,
  `freedom_order_customer_phoneddd` text DEFAULT NULL,
  `freedom_order_customer_mobilenumber` text DEFAULT NULL,
  `freedom_order_customer_mobileddd` text DEFAULT NULL,
  `freedom_order_customer_score` text DEFAULT NULL,
  `freedom_order_customer_address_country` text DEFAULT NULL,
  `freedom_order_customer_address_state` text DEFAULT NULL,
  `freedom_order_customer_address_statecode` text DEFAULT NULL,
  `freedom_order_customer_address_city` text DEFAULT NULL,
  `freedom_order_customer_address_street` text DEFAULT NULL,
  `freedom_order_customer_address_number` text DEFAULT NULL,
  `freedom_order_customer_address_district` text DEFAULT NULL,
  `freedom_order_customer_address_postalcode` text DEFAULT NULL,
  `freedom_order_customer_address_referencepoint` text DEFAULT NULL,
  `freedom_order_customer_address_description` text DEFAULT NULL,
  `freedom_order_customer_address_businessaddress` text DEFAULT NULL,
  `freedom_order_payments_cardholder` text DEFAULT NULL,
  `freedom_order_payments_expirationmonth` text DEFAULT NULL,
  `freedom_order_payments_expirationyear` text DEFAULT NULL,
  `freedom_order_payments_securitycode` text DEFAULT NULL,
  `freedom_order_payments_cardbrand` text DEFAULT NULL,
  `freedom_order_payments_installmentsnumber` text DEFAULT NULL,
  `freedom_order_payments_value` text DEFAULT NULL,
  `freedom_order_payments_optin` text DEFAULT NULL,
  `freedom_order_payments_externalcode` text DEFAULT NULL,
  `freedom_order_payments_paymentdate` text DEFAULT NULL,
  `freedom_order_payments_deliveryid` text DEFAULT NULL,
  `freedom_order_payments_typepayment` text DEFAULT NULL,
  `freedom_order_shippings_deliveryid` text DEFAULT NULL,
  `freedom_order_shippings_servicedelivery` text DEFAULT NULL,
  `freedom_order_shippings_deadlineindays` text DEFAULT NULL,
  `freedom_order_shippings_expecteddeliverydate` text DEFAULT NULL,
  `freedom_order_shippings_freight` text DEFAULT NULL,
  `freedom_order_shippings_canceledpayment` text DEFAULT NULL,
  `freedom_order_shippings_status` text DEFAULT NULL,
  `freedom_order_shippings_laststatusdate` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_date` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_username` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_externalcode` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_status` text DEFAULT NULL,
  `freedom_order_shippings_address_country` text DEFAULT NULL,
  `freedom_order_shippings_address_state` text DEFAULT NULL,
  `freedom_order_shippings_address_statecode` text DEFAULT NULL,
  `freedom_order_shippings_address_city` text DEFAULT NULL,
  `freedom_order_shippings_address_street` text DEFAULT NULL,
  `freedom_order_shippings_address_number` text DEFAULT NULL,
  `freedom_order_shippings_address_district` text DEFAULT NULL,
  `freedom_order_shippings_address_postalcode` text DEFAULT NULL,
  `freedom_order_shippings_address_referencepoint` text DEFAULT NULL,
  `freedom_order_shippings_address_description` text DEFAULT NULL,
  `freedom_order_shippings_address_businessaddress` text DEFAULT NULL,
  `freedom_order_shippings_recipient_name` text DEFAULT NULL,
  `freedom_order_shippings_recipient_cpfcnpj` text DEFAULT NULL,
  `freedom_order_shippings_recipient_birthdate` text DEFAULT NULL,
  `freedom_order_shippings_recipient_gender` text DEFAULT NULL,
  `freedom_order_shippings_recipient_persontype` text DEFAULT NULL,
  `freedom_order_shippings_recipient_phonenumber` text DEFAULT NULL,
  `freedom_order_shippings_recipient_phoneddd` text DEFAULT NULL,
  `freedom_order_shippings_recipient_mobilenumber` text DEFAULT NULL,
  `freedom_order_shippings_recipient_mobileddd` text DEFAULT NULL,
  `freedom_order_shippings_products_externalcode` text DEFAULT NULL,
  `freedom_order_shippings_products_sku` text DEFAULT NULL,
  `freedom_order_shippings_products_unitprice` text DEFAULT NULL,
  `freedom_order_shippings_products_unitdiscount` text DEFAULT NULL,
  `freedom_order_shippings_products_quantity` text DEFAULT NULL,
  `freedom_order_shippings_products_productname` text DEFAULT NULL,
  `freedom_order_shippings_products_freebie` text DEFAULT NULL,
  `freedom_order_shippings_products_netprice` text DEFAULT NULL,
  `freedom_order_shippings_carrier_id` text DEFAULT NULL,
  `freedom_order_shippings_carrier_tradingname` text DEFAULT NULL,
  `freedom_order_timestamp` text DEFAULT NULL,
  `freedom_order_shippings_sellerid` text DEFAULT NULL,
  `freedom_order_shippings_agreedate` text DEFAULT NULL,
  `freedom_order_device` text DEFAULT NULL,
  `freedom_order_utm_key` text DEFAULT NULL,
  `freedom_order_utm_value` text DEFAULT NULL,
  `freedom_order_unique_id` text DEFAULT NULL,
  `freedom_order_utm_key_id` text DEFAULT NULL,
  `freedom_order_date_publish_kafka` text DEFAULT NULL,
  `freedom_order_nm_country` text DEFAULT NULL,
  `freedom_order_date_load` text DEFAULT NULL,
  `freedom_order_hour_load` text DEFAULT NULL,
  `freedom_order_minute_load` text DEFAULT NULL
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE stage1.pedidos04cleansing (
  `freedom_order_sr_order` text DEFAULT NULL,
  `freedom_order_sr_payments` text DEFAULT NULL,
  `freedom_order_sr_shipping` text DEFAULT NULL,
  `freedom_order_sr_customer` text DEFAULT NULL,
  `freedom_order_sr_sku` text DEFAULT NULL,
  `freedom_order_catalog` text DEFAULT NULL,
  `freedom_order_storecode` text DEFAULT NULL,
  `freedom_order_saledate` text DEFAULT NULL,
  `freedom_order_saleschannel` text DEFAULT NULL,
  `freedom_order_amount` text DEFAULT NULL,
  `freedom_order_subtotal` text DEFAULT NULL,
  `freedom_order_id_code` text DEFAULT NULL,
  `freedom_order_id_origin` text DEFAULT NULL,
  `freedom_order_id_country` text DEFAULT NULL,
  `freedom_order_customer_externalcode` text DEFAULT NULL,
  `freedom_order_customer_name` text DEFAULT NULL,
  `freedom_order_customer_email` text DEFAULT NULL,
  `freedom_order_customer_cpfcnpj` text DEFAULT NULL,
  `freedom_order_customer_inscricaoestadual` text DEFAULT NULL,
  `freedom_order_customer_birthdate` text DEFAULT NULL,
  `freedom_order_customer_createdate` text DEFAULT NULL,
  `freedom_order_customer_gender` text DEFAULT NULL,
  `freedom_order_customer_persontype` text DEFAULT NULL,
  `freedom_order_customer_phonenumber` text DEFAULT NULL,
  `freedom_order_customer_phoneddd` text DEFAULT NULL,
  `freedom_order_customer_mobilenumber` text DEFAULT NULL,
  `freedom_order_customer_mobileddd` text DEFAULT NULL,
  `freedom_order_customer_score` text DEFAULT NULL,
  `freedom_order_customer_address_country` text DEFAULT NULL,
  `freedom_order_customer_address_state` text DEFAULT NULL,
  `freedom_order_customer_address_statecode` text DEFAULT NULL,
  `freedom_order_customer_address_city` text DEFAULT NULL,
  `freedom_order_customer_address_street` text DEFAULT NULL,
  `freedom_order_customer_address_number` text DEFAULT NULL,
  `freedom_order_customer_address_district` text DEFAULT NULL,
  `freedom_order_customer_address_postalcode` text DEFAULT NULL,
  `freedom_order_customer_address_referencepoint` text DEFAULT NULL,
  `freedom_order_customer_address_description` text DEFAULT NULL,
  `freedom_order_customer_address_businessaddress` text DEFAULT NULL,
  `freedom_order_payments_cardholder` text DEFAULT NULL,
  `freedom_order_payments_expirationmonth` text DEFAULT NULL,
  `freedom_order_payments_expirationyear` text DEFAULT NULL,
  `freedom_order_payments_securitycode` text DEFAULT NULL,
  `freedom_order_payments_cardbrand` text DEFAULT NULL,
  `freedom_order_payments_installmentsnumber` text DEFAULT NULL,
  `freedom_order_payments_value` text DEFAULT NULL,
  `freedom_order_payments_optin` text DEFAULT NULL,
  `freedom_order_payments_externalcode` text DEFAULT NULL,
  `freedom_order_payments_paymentdate` text DEFAULT NULL,
  `freedom_order_payments_deliveryid` text DEFAULT NULL,
  `freedom_order_payments_typepayment` text DEFAULT NULL,
  `freedom_order_shippings_deliveryid` text DEFAULT NULL,
  `freedom_order_shippings_servicedelivery` text DEFAULT NULL,
  `freedom_order_shippings_deadlineindays` text DEFAULT NULL,
  `freedom_order_shippings_expecteddeliverydate` text DEFAULT NULL,
  `freedom_order_shippings_freight` text DEFAULT NULL,
  `freedom_order_shippings_canceledpayment` text DEFAULT NULL,
  `freedom_order_shippings_status` text DEFAULT NULL,
  `freedom_order_shippings_laststatusdate` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_date` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_username` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_externalcode` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_status` text DEFAULT NULL,
  `freedom_order_shippings_address_country` text DEFAULT NULL,
  `freedom_order_shippings_address_state` text DEFAULT NULL,
  `freedom_order_shippings_address_statecode` text DEFAULT NULL,
  `freedom_order_shippings_address_city` text DEFAULT NULL,
  `freedom_order_shippings_address_street` text DEFAULT NULL,
  `freedom_order_shippings_address_number` text DEFAULT NULL,
  `freedom_order_shippings_address_district` text DEFAULT NULL,
  `freedom_order_shippings_address_postalcode` text DEFAULT NULL,
  `freedom_order_shippings_address_referencepoint` text DEFAULT NULL,
  `freedom_order_shippings_address_description` text DEFAULT NULL,
  `freedom_order_shippings_address_businessaddress` text DEFAULT NULL,
  `freedom_order_shippings_recipient_name` text DEFAULT NULL,
  `freedom_order_shippings_recipient_cpfcnpj` text DEFAULT NULL,
  `freedom_order_shippings_recipient_birthdate` text DEFAULT NULL,
  `freedom_order_shippings_recipient_gender` text DEFAULT NULL,
  `freedom_order_shippings_recipient_persontype` text DEFAULT NULL,
  `freedom_order_shippings_recipient_phonenumber` text DEFAULT NULL,
  `freedom_order_shippings_recipient_phoneddd` text DEFAULT NULL,
  `freedom_order_shippings_recipient_mobilenumber` text DEFAULT NULL,
  `freedom_order_shippings_recipient_mobileddd` text DEFAULT NULL,
  `freedom_order_shippings_products_externalcode` text DEFAULT NULL,
  `freedom_order_shippings_products_sku` text DEFAULT NULL,
  `freedom_order_shippings_products_unitprice` text DEFAULT NULL,
  `freedom_order_shippings_products_unitdiscount` text DEFAULT NULL,
  `freedom_order_shippings_products_quantity` text DEFAULT NULL,
  `freedom_order_shippings_products_productname` text DEFAULT NULL,
  `freedom_order_shippings_products_freebie` text DEFAULT NULL,
  `freedom_order_shippings_products_netprice` text DEFAULT NULL,
  `freedom_order_shippings_carrier_id` text DEFAULT NULL,
  `freedom_order_shippings_carrier_tradingname` text DEFAULT NULL,
  `freedom_order_timestamp` text DEFAULT NULL,
  `freedom_order_shippings_sellerid` text DEFAULT NULL,
  `freedom_order_shippings_agreedate` text DEFAULT NULL,
  `freedom_order_device` text DEFAULT NULL,
  `freedom_order_utm_key` text DEFAULT NULL,
  `freedom_order_utm_value` text DEFAULT NULL,
  `freedom_order_unique_id` text DEFAULT NULL,
  `freedom_order_utm_key_id` text DEFAULT NULL,
  `freedom_order_date_publish_kafka` text DEFAULT NULL,
  `freedom_order_nm_country` text DEFAULT NULL,
  `freedom_order_date_load` text DEFAULT NULL,
  `freedom_order_hour_load` text DEFAULT NULL,
  `freedom_order_minute_load` text DEFAULT NULL
) ENGINE=INNODB DEFAULT CHARSET=utf8;

use stage1;
select * from stage1.pedidos00cleansing;
select * from stage1.pedidos01cleansing;
select * from stage1.pedidos04cleansing;

use ods1;
select * from ods1.pedidos00;
select * from ods1.pedidos01;
select * from ods1.pedidos04;

SET GLOBAL time_zone = '+8:00'; 

#########################################

#CONECTANTO COM TALEND NOVAMENTE FIZ A CONEXÃO PARA TRAZER OS 3 ARQUIVOS E AUTOMATIZAR O PROCESSO.
# 26.03.2019 # Projeto 2 Março 2019 #

################# Abaixo os comandos usados para criar uma unica tabela com os 3 arquivos + criação da tabela dimensão e fato ###

CREATE TABLE ods3.totalpedidos (
  `freedom_order_sr_order` text DEFAULT NULL,
  `freedom_order_sr_payments` text DEFAULT NULL,
  `freedom_order_sr_shipping` text DEFAULT NULL,
  `freedom_order_sr_customer` text DEFAULT NULL,
  `freedom_order_sr_sku` text DEFAULT NULL,
  `freedom_order_catalog` text DEFAULT NULL,
  `freedom_order_storecode` text DEFAULT NULL,
  `freedom_order_saledate` text DEFAULT NULL,
  `freedom_order_saleschannel` text DEFAULT NULL,
  `freedom_order_amount` text DEFAULT NULL,
  `freedom_order_subtotal` text DEFAULT NULL,
  `freedom_order_id_code` text DEFAULT NULL,
  `freedom_order_id_origin` text DEFAULT NULL,
  `freedom_order_id_country` text DEFAULT NULL,
  `freedom_order_customer_externalcode` text DEFAULT NULL,
  `freedom_order_customer_name` text DEFAULT NULL,
  `freedom_order_customer_email` text DEFAULT NULL,
  `freedom_order_customer_cpfcnpj` text DEFAULT NULL,
  `freedom_order_customer_inscricaoestadual` text DEFAULT NULL,
  `freedom_order_customer_birthdate` text DEFAULT NULL,
  `freedom_order_customer_createdate` text DEFAULT NULL,
  `freedom_order_customer_gender` text DEFAULT NULL,
  `freedom_order_customer_persontype` text DEFAULT NULL,
  `freedom_order_customer_phonenumber` text DEFAULT NULL,
  `freedom_order_customer_phoneddd` text DEFAULT NULL,
  `freedom_order_customer_mobilenumber` text DEFAULT NULL,
  `freedom_order_customer_mobileddd` text DEFAULT NULL,
  `freedom_order_customer_score` text DEFAULT NULL,
  `freedom_order_customer_address_country` text DEFAULT NULL,
  `freedom_order_customer_address_state` text DEFAULT NULL,
  `freedom_order_customer_address_statecode` text DEFAULT NULL,
  `freedom_order_customer_address_city` text DEFAULT NULL,
  `freedom_order_customer_address_street` text DEFAULT NULL,
  `freedom_order_customer_address_number` text DEFAULT NULL,
  `freedom_order_customer_address_district` text DEFAULT NULL,
  `freedom_order_customer_address_postalcode` text DEFAULT NULL,
  `freedom_order_customer_address_referencepoint` text DEFAULT NULL,
  `freedom_order_customer_address_description` text DEFAULT NULL,
  `freedom_order_customer_address_businessaddress` text DEFAULT NULL,
  `freedom_order_payments_cardholder` text DEFAULT NULL,
  `freedom_order_payments_expirationmonth` text DEFAULT NULL,
  `freedom_order_payments_expirationyear` text DEFAULT NULL,
  `freedom_order_payments_securitycode` text DEFAULT NULL,
  `freedom_order_payments_cardbrand` text DEFAULT NULL,
  `freedom_order_payments_installmentsnumber` text DEFAULT NULL,
  `freedom_order_payments_value` text DEFAULT NULL,
  `freedom_order_payments_optin` text DEFAULT NULL,
  `freedom_order_payments_externalcode` text DEFAULT NULL,
  `freedom_order_payments_paymentdate` text DEFAULT NULL,
  `freedom_order_payments_deliveryid` text DEFAULT NULL,
  `freedom_order_payments_typepayment` text DEFAULT NULL,
  `freedom_order_shippings_deliveryid` text DEFAULT NULL,
  `freedom_order_shippings_servicedelivery` text DEFAULT NULL,
  `freedom_order_shippings_deadlineindays` text DEFAULT NULL,
  `freedom_order_shippings_expecteddeliverydate` text DEFAULT NULL,
  `freedom_order_shippings_freight` text DEFAULT NULL,
  `freedom_order_shippings_canceledpayment` text DEFAULT NULL,
  `freedom_order_shippings_status` text DEFAULT NULL,
  `freedom_order_shippings_laststatusdate` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_date` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_username` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_externalcode` text DEFAULT NULL,
  `freedom_order_shippings_statushistory_status` text DEFAULT NULL,
  `freedom_order_shippings_address_country` text DEFAULT NULL,
  `freedom_order_shippings_address_state` text DEFAULT NULL,
  `freedom_order_shippings_address_statecode` text DEFAULT NULL,
  `freedom_order_shippings_address_city` text DEFAULT NULL,
  `freedom_order_shippings_address_street` text DEFAULT NULL,
  `freedom_order_shippings_address_number` text DEFAULT NULL,
  `freedom_order_shippings_address_district` text DEFAULT NULL,
  `freedom_order_shippings_address_postalcode` text DEFAULT NULL,
  `freedom_order_shippings_address_referencepoint` text DEFAULT NULL,
  `freedom_order_shippings_address_description` text DEFAULT NULL,
  `freedom_order_shippings_address_businessaddress` text DEFAULT NULL,
  `freedom_order_shippings_recipient_name` text DEFAULT NULL,
  `freedom_order_shippings_recipient_cpfcnpj` text DEFAULT NULL,
  `freedom_order_shippings_recipient_birthdate` text DEFAULT NULL,
  `freedom_order_shippings_recipient_gender` text DEFAULT NULL,
  `freedom_order_shippings_recipient_persontype` text DEFAULT NULL,
  `freedom_order_shippings_recipient_phonenumber` text DEFAULT NULL,
  `freedom_order_shippings_recipient_phoneddd` text DEFAULT NULL,
  `freedom_order_shippings_recipient_mobilenumber` text DEFAULT NULL,
  `freedom_order_shippings_recipient_mobileddd` text DEFAULT NULL,
  `freedom_order_shippings_products_externalcode` text DEFAULT NULL,
  `freedom_order_shippings_products_sku` text DEFAULT NULL,
  `freedom_order_shippings_products_unitprice` text DEFAULT NULL,
  `freedom_order_shippings_products_unitdiscount` text DEFAULT NULL,
  `freedom_order_shippings_products_quantity` text DEFAULT NULL,
  `freedom_order_shippings_products_productname` text DEFAULT NULL,
  `freedom_order_shippings_products_freebie` text DEFAULT NULL,
  `freedom_order_shippings_products_netprice` text DEFAULT NULL,
  `freedom_order_shippings_carrier_id` text DEFAULT NULL,
  `freedom_order_shippings_carrier_tradingname` text DEFAULT NULL,
  `freedom_order_timestamp` text DEFAULT NULL,
  `freedom_order_shippings_sellerid` text DEFAULT NULL,
  `freedom_order_shippings_agreedate` text DEFAULT NULL,
  `freedom_order_device` text DEFAULT NULL,
  `freedom_order_utm_key` text DEFAULT NULL,
  `freedom_order_utm_value` text DEFAULT NULL,
  `freedom_order_unique_id` text DEFAULT NULL,
  `freedom_order_utm_key_id` text DEFAULT NULL,
  `freedom_order_date_publish_kafka` text DEFAULT NULL,
  `freedom_order_nm_country` text DEFAULT NULL,
  `freedom_order_date_load` text DEFAULT NULL,
  `freedom_order_hour_load` text DEFAULT NULL,
  `freedom_order_minute_load` text DEFAULT NULL
) ENGINE=INNODB DEFAULT CHARSET=utf8;

select * from ods3.totalpedidos;
select count(*) from ods3.totalpedidos;

TRUNCATE table stage1.dimensao;
TRUNCATE table dw2.ft_order;

use ods3;
SELECT *, COALESCE(f.shippings_products_productname, o.freedom_order_shippings_products_productname) as product_name
from ods3.totalpedidos o left join de_para f on o.freedom_order_sr_sku = f.sr_sku;
# INSERIR DIMENSÃO #
INSERT INTO  stage1.dimensao ( freedom_order_sr_sku, freedom_order_shippings_products_productname) 
SELECT
f.sr_sku,
f.shippings_products_productname
from ods3.totalpedidos o 
left join de_para f 
on o.freedom_order_sr_sku = f.sr_sku;

select * from stage1.dimensao;

select count(*) from ods3.totalpedidos;
select count(*) from stage1.dimensao;

truncate table ods3.totalpedidos;
truncate table stage1.dimensao;

select * from stage1.dimensao;

# criando tabela fato #
CREATE TABLE fato (
  table_id int(10) NOT NULL AUTO_INCREMENT,
  freedom_order_sr_order text NOT NULL,
  freedom_order_sr_sku text NOT NULL,
  freedom_order_shippings_products_sku text NOT NULL,
  freedom_order_shippings_products_unitprice text NOT NULL,
  freedom_order_shippings_products_unitdiscount text NOT NULL,
  freedom_order_shippings_products_quantity text NOT NULL,
  freedom_order_shippings_products_netprice text NOT NULL,
  PRIMARY KEY (table_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

select * from stage1.fato;
select count(*) from stage1.fato;

#Inserir en fato_p los campos correspondientes.
INSERT INTOdim_customerdim_customer stage1.fato ( freedom_order_sr_order, freedom_order_sr_sku, freedom_order_shippings_products_sku, freedom_order_shippings_products_unitprice, freedom_order_shippings_products_unitdiscount, freedom_order_shippings_products_quantity, freedom_order_shippings_products_netprice) 
SELECT
o.freedom_order_sr_order, 
o.freedom_order_sr_sku, 
o.freedom_order_shippings_products_sku, 
o.freedom_order_shippings_products_unitprice, 
o.freedom_order_shippings_products_unitdiscount, 
o.freedom_order_shippings_products_quantity, 
o.freedom_order_shippings_products_netprice
from ods3.totalpedidos as o;

select * from stage1.fato;

use stage1;

select * from stage1.fato;

use stage1;
CREATE TABLE stage1.dimensaonova (
    ID int(10) auto_increment not null, 
    freedom_order_customer_cpfcnpj VARCHAR(50) NOT NULL,
    freedom_order_customer_birthdate DATE DEFAULT NULL,
    freedom_order_customer_gender VARCHAR(30) NOT NULL,
    freedom_order_customer_persontype VARCHAR(30) NOT NULL,
    freedom_order_customer_score DOUBLE NOT NULL,
    freedom_order_customer_address_country VARCHAR(10) NOT NULL,
    freedom_order_customer_address_state VARCHAR(20) NOT NULL,
    freedom_order_customer_address_statecode VARCHAR(10) NOT NULL,
    freedom_order_customer_address_city VARCHAR(50) NOT NULL,
    freedom_order_customer_address_district TEXT NOT NULL,
    PRIMARY KEY (ID)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

select * from stage1.dimensaonova;
Select count(*) from stage1.dimensao_c;

use stage1;
INSERT INTO  stage1.dimensaonova (freedom_order_customer_cpfcnpj,freedom_order_customer_birthdate,freedom_order_customer_gender,freedom_order_customer_persontype,freedom_order_customer_score,freedom_order_customer_address_country,freedom_order_customer_address_state,freedom_order_customer_address_statecode,freedom_order_customer_address_city,freedom_order_customer_address_district)
SELECT distinct 
freedom_order_customer_cpfcnpj,
IF(STRCMP(freedom_order_customer_birthdate,"NULL") = 0, '0000-00-00', SUBSTR(freedom_order_customer_birthdate,1,10)) as freedom_order_customer_birthdate,
freedom_order_customer_gender,
freedom_order_customer_persontype,
freedom_order_customer_score,
freedom_order_customer_address_country,
freedom_order_customer_address_state,
freedom_order_customer_address_statecode,
freedom_order_customer_address_city,
freedom_order_customer_address_district
FROM ods3.totalpedidos;
  
# Criando Tabela Product + Select Distinct #
CREATE TABLE dw2.dim_product (
    freedom_order_sr_sku VARCHAR(20) NOT NULL,
    freedom_order_shippings_products_productname VARCHAR(50) NOT NULL,
    PRIMARY KEY (freedom_order_sr_sku)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

SELECT DISTINCT
     freedom_order_sr_sku,
       freedom_order_shippings_products_productname
       FROM ods3.totalpedidos
     ORDER BY freedom_order_shippings_products_productname;
     
     ## Criando tabela Customer + Select Distinct ##
	CREATE TABLE dw2.dim_customer (
    freedom_order_customer_cpfcnpj VARCHAR(30) NOT NULL,
    freedom_order_customer_externalcode VARCHAR(15) NOT NULL,
    freedom_order_customer_name TEXT NOT NULL,
    freedom_order_customer_email TEXT NOT NULL,
    freedom_order_customer_birthdate DATE,
    freedom_order_customer_createdate TIMESTAMP,
    freedom_order_customer_gender VARCHAR(10) NOT NULL,
    freedom_order_customer_persontype VARCHAR(10) NOT NULL,
    freedom_order_customer_phonenumber VARCHAR(15) NOT NULL,
    freedom_order_customer_phoneddd VARCHAR(2) NOT NULL,
    freedom_order_customer_mobilenumber VARCHAR(15) NOT NULL,
    freedom_order_customer_mobileddd VARCHAR(2) NOT NULL,
    freedom_order_customer_score DOUBLE NOT NULL,
    freedom_order_customer_address_country VARCHAR(2) NOT NULL,
    freedom_order_customer_address_state VARCHAR(20) NOT NULL,
    freedom_order_customer_address_statecode VARCHAR(2) NOT NULL,
    freedom_order_customer_address_city VARCHAR(20) NOT NULL,
    freedom_order_customer_address_street TEXT NOT NULL,
    freedom_order_customer_address_number VARCHAR(5) NOT NULL,
    freedom_order_customer_address_district TEXT NOT NULL,
    freedom_order_customer_address_postalcode VARCHAR(10) NOT NULL,
    PRIMARY KEY (freedom_order_customer_cpfcnpj)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

SELECT DISTINCT
  freedom_order_customer_cpfcnpj,
  freedom_order_customer_externalcode,
  freedom_order_customer_name,
  freedom_order_customer_email,
  IF(STRCMP(freedom_order_customer_birthdate,"NULL") = 0, 0, SUBSTR(freedom_order_customer_birthdate,1,10)) as freedom_order_customer_birthdate,
  freedom_order_customer_createdate,
  freedom_order_customer_gender,
  freedom_order_customer_persontype,
  freedom_order_customer_phonenumber,
  freedom_order_customer_phoneddd,
  freedom_order_customer_mobilenumber,
  freedom_order_customer_mobileddd,
  freedom_order_customer_score,
  freedom_order_customer_address_country,
  freedom_order_customer_address_state,
  freedom_order_customer_address_statecode,
  freedom_order_customer_address_city,
  freedom_order_customer_address_street,
  freedom_order_customer_address_number,
  freedom_order_customer_address_district,
  freedom_order_customer_address_postalcode
  FROM ods3.totalpedidos;


