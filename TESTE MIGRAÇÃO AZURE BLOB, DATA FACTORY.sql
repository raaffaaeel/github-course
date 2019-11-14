
TESTE MIGRAÇÃO AZURE BLOB, DATA FACTORY

# EXEMPLO 1 #
create schema STG;

create table STG.PESSOAS_FUNCIONARIO (
id varchar(200),	
first_name varchar(200),	
last_name varchar(200),	
job_title varchar(200),	
salary varchar(200),	
)

## APAGAR LINHA DUPLICADA ##
select * from STG.PESSOAS_FUNCIONARIO
where id != 'id'

----------------------------------------

create schema DIM;

create table DIM.PESSOAS_FUNCIONARIO (
id int,	
first_name varchar(200),	
last_name varchar(200),	
job_title varchar(200),	
salary float	
)

# criar novo schema e nova tabela, e criar procedure que tira a linha de cabeçalho. 

select * from DIM.PESSOAS_FUNCIONARIO;


## CRIANDO PROCEDURE ##
USE testerafaelblob
GO
CREATE PROCEDURE Selectalterando_typo 
AS
	INSERT INTO DIM.PESSOAS_FUNCIONARIO 
	SELECT 
		Cast (id AS int) AS id,
		first_name,
		last_name,
		job_title,
		Cast  (replace (salary, ',','.') AS float) AS salary
	FROM 
		STG.PESSOAS_FUNCIONARIO
	where 
		id != 'id';
GO

select * from DIM.PESSOAS_FUNCIONARIO;

exec Selectalterando_typo;

truncate table DIM.PESSOAS_FUNCIONARIO;

-------------------------------------------------------------

# EXEMPLO 2 #

USE STG;

create table STG.PESSOAS_RELATORIOS (
id varchar(4000),
codigo varchar(4000),
first_namevarchar(4000),
last_name varchar(4000),
email varchar(4000),
gender varchar(4000),
ip_address varchar(4000),
fone varchar(4000),
sexo varchar(4000),
salary varchar(4000)	
)


create table DIM.PESSOAS_RELATORIOS (
id int,
codigo varchar(4000),
first_namevarchar(4000),
last_name varchar(4000),
email varchar(4000),
gender varchar(4000),
ip_address varchar(4000),
fone varchar(4000),
sexo varchar(4000),
salary float
)

select * from STG.PESSOAS_RELATORIOS;
select * from DIM.PESSOAS_RELATORIOS;

_______________________________________________________________



## TRAZ AS COLUNAS E CONTA AS QUANTIDADES DE LINHAS ##
SELECT RME,RNEEDEXPOR, count(*)
FROM STG.GAN_SCADGER
group by RME,RNEEDEXPOR;

## TRAZ AS COLUNAS SELECIONADAS ###
SELECT distinct RME,RNEEDEXPOR
FROM STG.GAN_SCADGER;


## CONTANDO A TABELA INTEIRA ##
select count(*) 
FROM STG.GAN_SCADGER;
