CREATE TABLE `pedidos00` (
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


########################################################

CREATE TABLE pocco.dimensao (
  `freedom_order_sr_order` TEXT DEFAULT NULL,
  `freedom_order_sr_payments` TEXT DEFAULT NULL,
  `freedom_order_sr_shipping` TEXT DEFAULT NULL,
  `freedom_order_sr_customer` TEXT DEFAULT NULL,
  `freedom_order_sr_sku` TEXT DEFAULT NULL,
  `freedom_order_catalog` TEXT DEFAULT NULL,
  `freedom_order_storecode` TEXT DEFAULT NULL,
  `freedom_order_saledate` TEXT DEFAULT NULL,
  `freedom_order_saleschannel` TEXT DEFAULT NULL,
  `freedom_order_amount` TEXT DEFAULT NULL,
  `freedom_order_subtotal` TEXT DEFAULT NULL,
  `freedom_order_id_code` TEXT DEFAULT NULL,
  `freedom_order_id_origin` TEXT DEFAULT NULL,
  `freedom_order_id_country` TEXT DEFAULT NULL,
  `freedom_order_customer_externalcode` TEXT DEFAULT NULL,
  `freedom_order_customer_name` TEXT DEFAULT NULL,
  `freedom_order_customer_email` TEXT DEFAULT NULL,
  `freedom_order_customer_cpfcnpj` TEXT DEFAULT NULL,
  `freedom_order_customer_inscricaoestadual` TEXT DEFAULT NULL,
  `freedom_order_customer_birthdate` TEXT DEFAULT NULL,
  `freedom_order_customer_createdate` TEXT DEFAULT NULL,
  `freedom_order_customer_gender` TEXT DEFAULT NULL,
  `freedom_order_customer_persontype` TEXT DEFAULT NULL,
  `freedom_order_customer_phonenumber` TEXT DEFAULT NULL,
  `freedom_order_customer_phoneddd` TEXT DEFAULT NULL,
  `freedom_order_customer_mobilenumber` TEXT DEFAULT NULL,
  `freedom_order_customer_mobileddd` TEXT DEFAULT NULL,
  `freedom_order_customer_score` TEXT DEFAULT NULL,
  `freedom_order_customer_address_country` TEXT DEFAULT NULL,
  `freedom_order_customer_address_state` TEXT DEFAULT NULL,
  `freedom_order_customer_address_statecode` TEXT DEFAULT NULL,
  `freedom_order_customer_address_city` TEXT DEFAULT NULL,
  `freedom_order_customer_address_street` TEXT DEFAULT NULL,
  `freedom_order_customer_address_number` TEXT DEFAULT NULL,
  `freedom_order_customer_address_district` TEXT DEFAULT NULL,
  `freedom_order_customer_address_postalcode` TEXT DEFAULT NULL,
  `freedom_order_customer_address_referencepoint` TEXT DEFAULT NULL,
  `freedom_order_customer_address_description` TEXT DEFAULT NULL,
  `freedom_order_customer_address_businessaddress` TEXT DEFAULT NULL,
  `freedom_order_payments_cardholder` TEXT DEFAULT NULL,
  `freedom_order_payments_expirationmonth` TEXT DEFAULT NULL,
  `freedom_order_payments_expirationyear` TEXT DEFAULT NULL,
  `freedom_order_payments_securitycode` TEXT DEFAULT NULL,
  `freedom_order_payments_cardbrand` TEXT DEFAULT NULL,
  `freedom_order_payments_installmentsnumber` TEXT DEFAULT NULL,
  `freedom_order_payments_value` TEXT DEFAULT NULL,
  `freedom_order_payments_optin` TEXT DEFAULT NULL,
  `freedom_order_payments_externalcode` TEXT DEFAULT NULL,
  `freedom_order_payments_paymentdate` TEXT DEFAULT NULL,
  `freedom_order_payments_deliveryid` TEXT DEFAULT NULL,
  `freedom_order_payments_typepayment` TEXT DEFAULT NULL,
  `freedom_order_shippings_deliveryid` TEXT DEFAULT NULL,
  `freedom_order_shippings_servicedelivery` TEXT DEFAULT NULL,
  `freedom_order_shippings_deadlineindays` TEXT DEFAULT NULL,
  `freedom_order_shippings_expecteddeliverydate` TEXT DEFAULT NULL,
  `freedom_order_shippings_freight` TEXT DEFAULT NULL,
  `freedom_order_shippings_canceledpayment` TEXT DEFAULT NULL,
  `freedom_order_shippings_status` TEXT DEFAULT NULL,
  `freedom_order_shippings_laststatusdate` TEXT DEFAULT NULL,
  `freedom_order_shippings_statushistory_date` TEXT DEFAULT NULL,
  `freedom_order_shippings_statushistory_username` TEXT DEFAULT NULL,
  `freedom_order_shippings_statushistory_externalcode` TEXT DEFAULT NULL,
  `freedom_order_shippings_statushistory_status` TEXT DEFAULT NULL,
  `freedom_order_shippings_address_country` TEXT DEFAULT NULL,
  `freedom_order_shippings_address_state` TEXT DEFAULT NULL,
  `freedom_order_shippings_address_statecode` TEXT DEFAULT NULL,
  `freedom_order_shippings_address_city` TEXT DEFAULT NULL,
  `freedom_order_shippings_address_street` TEXT DEFAULT NULL,
  `freedom_order_shippings_address_number` TEXT DEFAULT NULL,
  `freedom_order_shippings_address_district` TEXT DEFAULT NULL,
  `freedom_order_shippings_address_postalcode` TEXT DEFAULT NULL,
  `freedom_order_shippings_address_referencepoint` TEXT DEFAULT NULL,
  `freedom_order_shippings_address_description` TEXT DEFAULT NULL,
  `freedom_order_shippings_address_businessaddress` TEXT DEFAULT NULL,
  `freedom_order_shippings_recipient_name` TEXT DEFAULT NULL,
  `freedom_order_shippings_recipient_cpfcnpj` TEXT DEFAULT NULL,
  `freedom_order_shippings_recipient_birthdate` TEXT DEFAULT NULL,
  `freedom_order_shippings_recipient_gender` TEXT DEFAULT NULL,
  `freedom_order_shippings_recipient_persontype` TEXT DEFAULT NULL,
  `freedom_order_shippings_recipient_phonenumber` TEXT DEFAULT NULL,
  `freedom_order_shippings_recipient_phoneddd` TEXT DEFAULT NULL,
  `freedom_order_shippings_recipient_mobilenumber` TEXT DEFAULT NULL,
  `freedom_order_shippings_recipient_mobileddd` TEXT DEFAULT NULL,
  `freedom_order_shippings_products_externalcode` TEXT DEFAULT NULL,
  `freedom_order_shippings_products_sku` TEXT DEFAULT NULL,
  `freedom_order_shippings_products_unitprice` TEXT DEFAULT NULL,
  `freedom_order_shippings_products_unitdiscount` TEXT DEFAULT NULL,
  `freedom_order_shippings_products_quantity` TEXT DEFAULT NULL,
  `freedom_order_shippings_products_productname` TEXT DEFAULT NULL,
  `freedom_order_shippings_products_freebie` TEXT DEFAULT NULL,
  `freedom_order_shippings_products_netprice` TEXT DEFAULT NULL,
  `freedom_order_shippings_carrier_id` TEXT DEFAULT NULL,
  `freedom_order_shippings_carrier_tradingname` TEXT DEFAULT NULL,
  `freedom_order_timestamp` TEXT DEFAULT NULL,
  `freedom_order_shippings_sellerid` TEXT DEFAULT NULL,
  `freedom_order_shippings_agreedate` TEXT DEFAULT NULL,
  `freedom_order_device` TEXT DEFAULT NULL,
  `freedom_order_utm_key` TEXT DEFAULT NULL,
  `freedom_order_unique_id` TEXT DEFAULT NULL,
  `freedom_order_date_publish_kafka` TEXT DEFAULT NULL,
  `freedom_order_nm_country` TEXT DEFAULT NULL,
  `freedom_order_date_load` TEXT DEFAULT NULL,
  `freedom_order_hour_load` TEXT DEFAULT NULL,
  `freedom_order_minute_load` TEXT DEFAULT NULL
) ENGINE=INNODB DEFAULT CHARSET=utf8;

INSERT INTO stage2.orders_00 (
  freedom_order_sr_order,
  freedom_order_sr_payments,
  freedom_order_sr_shipping,
  freedom_order_sr_customer,
  freedom_order_sr_sku,
  freedom_order_catalog,
  freedom_order_storecode,
  freedom_order_saledate,
  freedom_order_saleschannel,
  freedom_order_amount,
  freedom_order_subtotal,
  freedom_order_id_code,
  freedom_order_id_origin,
  freedom_order_id_country,
  freedom_order_customer_externalcode,
  freedom_order_customer_name,
  freedom_order_customer_email,
  freedom_order_customer_cpfcnpj,
  freedom_order_customer_inscricaoestadual,
  freedom_order_customer_birthdate,
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
  freedom_order_customer_address_postalcode,
  freedom_order_customer_address_referencepoint,
  freedom_order_customer_address_description,
  freedom_order_customer_address_businessaddress,
  freedom_order_payments_cardholder,
  freedom_order_payments_expirationmonth,
  freedom_order_payments_expirationyear,
  freedom_order_payments_securitycode,
  freedom_order_payments_cardbrand,
  freedom_order_payments_installmentsnumber,
  freedom_order_payments_value,
  freedom_order_payments_optin,
  freedom_order_payments_externalcode,
  freedom_order_payments_paymentdate,
  freedom_order_payments_deliveryid,
  freedom_order_payments_typepayment,
  freedom_order_shippings_deliveryid,
  freedom_order_shippings_servicedelivery,
  freedom_order_shippings_deadlineindays,
  freedom_order_shippings_expecteddeliverydate,
  freedom_order_shippings_freight,
  freedom_order_shippings_canceledpayment,
  freedom_order_shippings_status,
  freedom_order_shippings_laststatusdate,
  freedom_order_shippings_statushistory_date,
  freedom_order_shippings_statushistory_username,
  freedom_order_shippings_statushistory_externalcode,
  freedom_order_shippings_statushistory_status,
  freedom_order_shippings_address_country,
  freedom_order_shippings_address_state,
  freedom_order_shippings_address_statecode,
  freedom_order_shippings_address_city,
  freedom_order_shippings_address_street,
  freedom_order_shippings_address_number,
  freedom_order_shippings_address_district,
  freedom_order_shippings_address_postalcode,
  freedom_order_shippings_address_referencepoint,
  freedom_order_shippings_address_description,
  freedom_order_shippings_address_businessaddress,
  freedom_order_shippings_recipient_name,
  freedom_order_shippings_recipient_cpfcnpj,
  freedom_order_shippings_recipient_birthdate,
  freedom_order_shippings_recipient_gender,
  freedom_order_shippings_recipient_persontype,
  freedom_order_shippings_recipient_phonenumber,
  freedom_order_shippings_recipient_phoneddd,
  freedom_order_shippings_recipient_mobilenumber,
  freedom_order_shippings_recipient_mobileddd,
  freedom_order_shippings_products_externalcode,
  freedom_order_shippings_products_sku,
  freedom_order_shippings_products_unitprice,
  freedom_order_shippings_products_unitdiscount,
  freedom_order_shippings_products_quantity,
  freedom_order_shippings_products_productname,
  freedom_order_shippings_products_freebie,
  freedom_order_shippings_products_netprice,
  freedom_order_shippings_carrier_id,
  freedom_order_shippings_carrier_tradingname,
  freedom_order_timestamp,
  freedom_order_shippings_sellerid,
  freedom_order_shippings_agreedate,
  freedom_order_device,
  freedom_order_utm_key,
  freedom_order_unique_id,
  freedom_order_date_publish_kafka,
  freedom_order_nm_country,
  freedom_order_date_load,
  freedom_order_hour_load,
  freedom_order_minute_load)  
SELECT 
  freedom_order_sr_order,
  freedom_order_sr_payments,
  freedom_order_sr_shipping,
  freedom_order_sr_customer,
  freedom_order_sr_sku,
  freedom_order_catalog,
  freedom_order_storecode,
  freedom_order_saledate,
  freedom_order_saleschannel,
  freedom_order_amount,
  freedom_order_subtotal,
  freedom_order_id_code,
  freedom_order_id_origin,
  freedom_order_id_country,
  freedom_order_customer_externalcode,
  freedom_order_customer_name,
  freedom_order_customer_email,
  freedom_order_customer_cpfcnpj,
  freedom_order_customer_inscricaoestadual,
  freedom_order_customer_birthdate,
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
  freedom_order_customer_address_postalcode,
  freedom_order_customer_address_referencepoint,
  freedom_order_customer_address_description,
  freedom_order_customer_address_businessaddress,
  freedom_order_payments_cardholder,
  freedom_order_payments_expirationmonth,
  freedom_order_payments_expirationyear,
  freedom_order_payments_securitycode,
  freedom_order_payments_cardbrand,
  freedom_order_payments_installmentsnumber,
  freedom_order_payments_value,
  freedom_order_payments_optin,
  freedom_order_payments_externalcode,
  freedom_order_payments_paymentdate,
  freedom_order_payments_deliveryid,
  freedom_order_payments_typepayment,
  freedom_order_shippings_deliveryid,
  freedom_order_shippings_servicedelivery,
  freedom_order_shippings_deadlineindays,
  freedom_order_shippings_expecteddeliverydate,
  freedom_order_shippings_freight,
  freedom_order_shippings_canceledpayment,
  freedom_order_shippings_status,
  freedom_order_shippings_laststatusdate,
  freedom_order_shippings_statushistory_date,
  freedom_order_shippings_statushistory_username,
  freedom_order_shippings_statushistory_externalcode,
  freedom_order_shippings_statushistory_status,
  freedom_order_shippings_address_country,
  freedom_order_shippings_address_state,
  freedom_order_shippings_address_statecode,
  freedom_order_shippings_address_city,
  freedom_order_shippings_address_street,
  freedom_order_shippings_address_number,
  freedom_order_shippings_address_district,
  freedom_order_shippings_address_postalcode,
  freedom_order_shippings_address_referencepoint,
  freedom_order_shippings_address_description,
  freedom_order_shippings_address_businessaddress,
  freedom_order_shippings_recipient_name,
  freedom_order_shippings_recipient_cpfcnpj,
  freedom_order_shippings_recipient_birthdate,
  freedom_order_shippings_recipient_gender,
  freedom_order_shippings_recipient_persontype,
  freedom_order_shippings_recipient_phonenumber,
  freedom_order_shippings_recipient_phoneddd,
  freedom_order_shippings_recipient_mobilenumber,
  freedom_order_shippings_recipient_mobileddd,
  freedom_order_shippings_products_externalcode,
  freedom_order_shippings_products_sku,
  freedom_order_shippings_products_unitprice,
  freedom_order_shippings_products_unitdiscount,
  freedom_order_shippings_products_quantity,
  freedom_order_shippings_products_productname,
  freedom_order_shippings_products_freebie,
  freedom_order_shippings_products_netprice,
  freedom_order_shippings_carrier_id,
  freedom_order_shippings_carrier_tradingname,
  freedom_order_timestamp,
  freedom_order_shippings_sellerid,
  freedom_order_shippings_agreedate,
  freedom_order_device,
  freedom_order_utm_key,
  freedom_order_unique_id,
  freedom_order_date_publish_kafka,
  freedom_order_nm_country,
  freedom_order_date_load,
  freedom_order_hour_load,
  freedom_order_minute_load
FROM talend.orders_00;

SELECT * FROM
   (SELECT id, 
       freedom_order_sr_order, 
       SUBSTR(freedom_order_shippings_statushistory_date,1,11) as status_timestamp,
       ROW_NUMBER() OVER(PARTITION BY SUBSTR(freedom_order_shippings_statushistory_date,1,11)) AS row_num
         FROM stage2.orders_00
       WHERE freedom_order_sr_order = '150022717_782202196'
       ORDER BY freedom_order_sr_order, status_timestamp desc) a
WHERE row_num = 1;

SELECT DISTINCT
       freedom_order_sr_order,
       SUBSTR(freedom_order_shippings_statushistory_date,1,13) as status_timestamp
         FROM stage2.orders_00
       ORDER BY freedom_order_sr_order, status_timestamp desc;


 //Deduplica | Retorna status do pedido por hora
 
 SELECT b.freedom_order_sr_sku,
       a.freedom_order_sr_order,
       a.status_timestamp,
       b.freedom_order_shippings_products_productname,
       b.freedom_order_shippings_products_sku,
       b.freedom_order_shippings_products_unitprice,
       b.freedom_order_shippings_products_unitdiscount,
     b.freedom_order_shippings_products_quantity,
       b.freedom_order_shippings_products_netprice
FROM stage2.orders_00 as b,
    ( SELECT DISTINCT
       freedom_order_sr_order, 
       SUBSTR(freedom_order_shippings_statushistory_date,1,13) as status_timestamp
         FROM stage2.orders_00
       ORDER BY freedom_order_sr_order, status_timestamp desc) as a
       WHERE  a.freedom_order_sr_order = b.freedom_order_sr_order;

DW

// dim_product
freedom_order_sr_sku
freedom_order_shippings_products_productname (essa coluna que precisa sofrer datacleansing)

CREATE TABLE dw2.dim_product (
    freedom_order_sr_sku VARCHAR(20) NOT NULL,
    freedom_order_shippings_products_productname TEXT NOT NULL,
    PRIMARY KEY (freedom_order_sr_sku)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

SELECT DISTINCT
     freedom_order_sr_sku,
       freedom_order_shippings_products_productname
       FROM stage2.orders_00
     ORDER BY freedom_order_shippings_products_productname;

//ft_order
freedom_order_sr_order (chave do pedido)
freedom_order_sr_sku (chave do produto)
freedom_order_shippings_products_sku
freedom_order_shippings_products_unitprice
freedom_order_shippings_products_unitdiscount
freedom_order_shippings_products_quantity
freedom_order_shippings_products_netprice

CREATE TABLE dw2.ft_order (
    freedom_order_sr_order VARCHAR(30) NOT NULL,
    freedom_order_customer_cpfcnpj VARCHAR(20) NOT NULL,
    freedom_order_sr_sku VARCHAR(20) NOT NULL,
    status_date DATE NOT NULL,
    status_hour INT NOT NULL,
    freedom_order_shippings_products_unitprice DOUBLE NOT NULL,
    freedom_order_shippings_products_unitdiscount DOUBLE NOT NULL,
    freedom_order_shippings_products_quantity INT NOT NULL,
    freedom_order_shippings_products_netprice DOUBLE NOT NULL,
    PRIMARY KEY (freedom_order_sr_order),
    FOREIGN KEY (freedom_order_customer_cpfcnpj) REFERENCES dim_customer(freedom_order_customer_cpfcnpj),
    FOREIGN KEY (freedom_order_sr_sku) REFERENCES dim_product(freedom_order_sr_sku)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

SELECT a.freedom_order_sr_order,
       b.freedom_order_customer_cpfcnpj,
       b.freedom_order_sr_sku,
       a.status_date,
       a.status_hour,
       b.freedom_order_shippings_products_unitprice,
       b.freedom_order_shippings_products_unitdiscount,
       b.freedom_order_shippings_products_quantity,
       b.freedom_order_shippings_products_netprice
FROM stage2.orders_00 as b,
    ( SELECT DISTINCT
       freedom_order_sr_order, 
       SUBSTR(freedom_order_shippings_statushistory_date,1,10) as status_date,
       SUBSTR(freedom_order_shippings_statushistory_date,12,2) as status_hour
         FROM stage2.orders_00
       ORDER BY freedom_order_sr_order, status_date desc, status_hour desc) as a
       WHERE  a.freedom_order_sr_order = b.freedom_order_sr_order;

//dim_customer
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
  FROM stage2.orders_00;

