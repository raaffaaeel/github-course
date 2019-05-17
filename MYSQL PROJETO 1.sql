# Script em SQL PROJETO MIGRAÇÃO DE DADOS language para criar e popular as tabelas.alter

#CREATE TABLE ODS
use ods;
CREATE TABLE `ods`.`o_pedidos` (
table_id INT NOT NULL AUTO_INCREMENT,
region TEXT,
country TEXT,
item_type TEXT,
sales_channel TEXT,
order_priority TEXT,
order_date TEXT,
order_id TEXT,
ship_date TEXT,
units_sold TEXT,
unit_price TEXT,
unit_cost TEXT,
total_revenue TEXT,
total_cost TEXT,
total_profit TEXT,
PRIMARY KEY (table_id))
ENGINE=INNODB DEFAULT CHARSET=utf8;
select * from `ods`.`o_pedidos`;


#CREATE TABLE STAGE
use stage;
CREATE TABLE stage.region (
region_id INT NOT NULL AUTO_INCREMENT,
region TEXT,
PRIMARY KEY (region_id))
ENGINE=INNODB DEFAULT CHARSET=utf8;
CREATE TABLE stage.country (
country_id INT NOT NULL AUTO_INCREMENT,
country TEXT,
PRIMARY KEY (country_id))
ENGINE=INNODB DEFAULT CHARSET=utf8;
CREATE TABLE stage.`channel` (
channel_id INT NOT NULL AUTO_INCREMENT,
`channel` TEXT,
PRIMARY KEY (channel_id))
ENGINE=INNODB DEFAULT CHARSET=utf8;
CREATE TABLE `stage`.`orders` (
table_id INT NOT NULL AUTO_INCREMENT,
region TEXT,
country TEXT,
item_type TEXT,
sales_channel TEXT,
order_priority TEXT,
order_date TEXT,
order_id varchar(10),
ship_date TEXT,
units_sold TEXT,
unit_price TEXT,
unit_cost TEXT,
total_revenue TEXT,
total_cost TEXT,
total_profit TEXT,
PRIMARY KEY (table_id))
ENGINE=INNODB DEFAULT CHARSET=utf8;
#DROP TABLE  `stage`.`orders`;

#CREATE INDEX
#CREATE INDEX stage_orders_1 ON `stage`.`orders` (order_id);

#CREATE TABLE DW
CREATE TABLE dw.dim_region (
region_id INT NOT NULL,
region TEXT,
PRIMARY KEY (region_id))
ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE dw.dim_country (
country_id INT NOT NULL,
country TEXT,
PRIMARY KEY (country_id))
ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE dw.dim_channel (
channel_id INT NOT NULL,
`channel` TEXT,
PRIMARY KEY (channel_id))
ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE `dw`.`ft_orders` (
id_ft INT NOT NULL AUTO_INCREMENT,
region_id INT NOT NULL,
country_id INT NOT NULL,
channel_id INT NOT NULL,
item_type TEXT,
order_priority TEXT,
order_date DATE,
order_id VARCHAR(10) NOT NULL,
ship_date DATE,
units_sold DOUBLE,
unit_price DOUBLE,
unit_cost DOUBLE,
total_revenue DOUBLE,
total_cost DOUBLE,
total_profit DOUBLE,
PRIMARY KEY (id_ft),
FOREIGN KEY (region_id) REFERENCES dw.dim_region(region_id),
FOREIGN KEY (country_id) REFERENCES dw.dim_country(country_id),
FOREIGN KEY (channel_id) REFERENCES dw.dim_channel(channel_id)
)
ENGINE=INNODB DEFAULT CHARSET=utf8;
#DROP TABLE `dw`.`ft_orders` ;

CREATE INDEX

CREATE INDEX ft_orders_1 ON `dw`.`ft_orders` (order_id);



#INSERT STAGE
insert into stage.region (region)  select region from ods.o_pedidos where region <> 'region' group by region;
insert into stage.country (country)  select country from ods.o_pedidos where country <> 'country' group by country;
insert into stage.`channel` (`channel`)  select sales_channel from ods.o_pedidos where sales_channel <> 'sales_channel' group by sales_channel;
insert into stage.orders (region, country, item_type, sales_channel, order_priority, 
	order_date, order_id, ship_date, units_sold, unit_price, unit_cost, total_revenue, 
    total_cost, total_profit) 
		select region, country, item_type, sales_channel, order_priority, 
        order_date, order_id, ship_date, units_sold, unit_price, unit_cost, 
        total_revenue, total_cost, total_profit from ods.o_pedidos;


INSERT DW


insert into dw.dim_region (region_id, region)  
	select max(a.region_id) as region_id, a.region from stage.region a 
		left join dw.dim_region b on a.region = b.region 
	where b.region is null
	group by a.region;  
    
insert into dw.dim_country (country_id, country)  
	select max(a.country_id) as country_id, a.country from stage.country a 
    left join dw.dim_country b on a.country = b.country 
	where b.country is null
	group by a.country;

insert into dw.dim_channel (channel_id, `channel`)  
	select max(a.channel_id) as channel_id, a.`channel` from stage.`channel` a 
	left join dw.dim_channel b on a.`channel` = b.`channel` 
	where b.`channel` is null
    group by a.`channel`;



INSERT INTO dw.ft_orders 
 (region_id,country_id,channel_id,item_type,order_priority,order_date,order_id,
 ship_date,units_sold,unit_price,unit_cost,total_revenue,total_cost,total_profit) 
	select
		 f.region_id,
		 f.country_id,
		 f.channel_id,
		 f.item_type,
		 f.order_priority,
		 f.order_date,
		 f.order_id,
		 f.ship_date,
		 f.units_sold,
		 f.unit_price,
		 f.unit_cost,
		 f.total_revenue,
		 f.total_cost,
		 f.total_profit
	from 
	 (
		 select 
		 b.region_id,
		 c.country_id,
		 d.channel_id,
		 a.item_type,a.order_priority,
		 STR_TO_DATE(a.order_date,'%m/%d/%Y') as order_date ,
		 a.order_id,
		 STR_TO_DATE(a.ship_date,'%m/%d/%Y') as ship_date ,
		 a.units_sold,a.unit_price,a.unit_cost,a.total_revenue,a.total_cost,a.total_profit,
		  ROW_NUMBER() OVER (PARTITION BY a.order_id ORDER BY a.order_id ASC) AS deduplica
		 from stage.`orders` a 
			left join dw.dim_region b on a.region = b.region
			left join dw.dim_country c on a.country = c.country
			left join dw.dim_channel d on a.sales_channel = d.`channel`
			left join dw.ft_orders e on a.order_id = e.order_id
		 where e.order_id is null
	  ) f 
where f.deduplica = 1;


select sum(a.total_revenue) as total, c.region, d.country from dw.ft_orders a 
	inner join (select max(left(order_date,4)) as order_date from dw.ft_orders)b on left(a.order_date,4) =  b.order_date
    inner join dw.dim_region c on a.region_id = c.region_id
    inner join dw.dim_country d on a.country_id = d.country_id
group by c.region, d.country order by sum(a.total_revenue) desc;


#O total de vendas dos últimos10 dias
select sum(a.total_revenue) as total, a.order_date from dw.ft_orders a 
group by  a.order_date order by a.order_date desc limit 10


#O total de vendas e o acumulado de vendas dos últimos 30 dias   
SELECT a.order_date, a.total_revenue, SUM(a.total_revenue) OVER(ORDER BY a.order_date) AS cumulative_sum
FROM (select order_date, SUM(total_revenue) as total_revenue from dw.ft_orders group by order_date order by order_date desc limit 10) a
