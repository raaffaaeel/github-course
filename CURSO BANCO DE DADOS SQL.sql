
COMPRAR CURSO SQL PARA BIG DATA DA (DSA)

CURSO BANCO DE DADOS SQL

# CRIANDO BANCO DE DADOS #


Banco de Dados

Comandos no SQL 

1- Grupo.

DML > (Data Manipulation Language) (Desenvolvimento)

> SELECT: Pesquisa
> UPDATE: Atualização de Dados
> DELETE: Eliminação de Dados
> INSERT: Inserção de Dados


2- Grupo.

DDL (Data Definition Language) (Suporte)

> CREATE: Definição de um objeto (tabela, Índice)
> ALTER: Alteração de um objeto.
> DROP: Eliminação de um objeto.


3-Grupo.

DCL > (Data Control Language) (Suporte/Desenvolvimento)

> GRANT : Fornecer um privilégio
> REVOKE : Tirar um privilégio

---------------------------------------------------------

SQLite > é um engime (motor) de banco de dados SQL.

https://www.sqlite.org

Lista completa de Bancos de Dados NoSQL visite > http://nosql-database.org



CREATE DATABASE PROJETO;

# CONECTANDO AO BANCO #

USE PROJETO;

# CRIANDO A TABELA #

CREATE TABLE CLIENTE(
	NOME VARCHAR(30)
	SEXO CHAR(1)
	EMAIL VARCHAR(30)
	CPF INT(11)
	TELEFONE VARCHAR(30)
	ENDERECO VARCHAR(100)
	);
	
# VERIFICANDO AS TABELAS #
	SHOW TABLES;

# DESCREVENDO TABELAS #
DESC CLIENTE;

### AULA 9 ###

	# PARA CARACTER LITERAIS COMO ÁRVORE, JOÃO, MATEMÁTICA.
# USAR --> CHAR e VARCHAR
# CHAR > PREENCHER SEMPRE (10).
# VARCHAR > PREENCHER QT DE CARACTERC JOÃO(4)

# PARA CARACTER NÚMEROS --> INT e FLOT.
# FLOT USADO PARA NUMEROS REAIS EX: 1345,89 FLOAT (6,2)
# INT USADO PARA NUMEROS INTEIROS EX: 10 23 500.
# NUMEROS QUE Ñ NECESSITAM DE CÁLCULOS PODEM SER TIPADOS COMO VARCHAR!

# PARA FOTOS DOCUMENTOS --> BLOB.

# PARA TEXTO INTENSOS E GRANDES --> TEXT.

### AULA 11 ###

# MOSTRANDO AS TABELAS #
SHOW TABLES

# EXIBINDO A ESTRUTURA DE UMA TABELA #
DESC CLIENTE

# INSERINDO INFORMAÇÃO NAS COLUNAS #

INSERT INTO CLIENTE VALUES('JOAO','M','JOAO@GMAIL.COM',983638273,'229233110','MAIA LACERDA - ESTACIO - RIO DE JANEIRO - RJ');

INSERT INTO CLIENTE VALUES('CELIA','F','CELIA@GMAIL.COM',541521456,'25078869','RIACHUELO - CENTRO - RIO DE JANEIRO - RJ');

INSERT INTO CLIENTE VALUES('JORGE','M',NULL,885755896,'58748895','OSCAR CURY - BOM RETIRO - PATOS DE MINAS - MG');


### FORMA 02 - COLOCANDO AS COLUNAS ###

INSERT INTO CLIENTE(NOME,SEXO,ENDERECO,TELEFONE,CPF) VALUES('LILIAN','F','SENADOR SOARES - TIJUCA - RIO DE JANEIRO - RJ','947785696',30414212319);

# FORMA 03 - INSERT COMPACTO -  SOMENTE EM MYSQL #

INSERT INTO CLIENTE VALUES ('ANA','F',ANA@GLOBO.COM',85548962,'548556985','PRES ANTONIO CARLOS - CENTRO - SAO PAULO - SP),

						   

# AULA 13 COMANDO SELECT #



### AULA 13 -  COMANDO SELECT ###


SELECT NOW(); # Serve para mostrar qualquer coisa # 

SELECT 'FELIPE MAPRA';

SELECT 'BANCO DE DADOS';

### ALIAS DE COLUNAS / são apelidos ###

SELECT 'RAFAEL MACEDO' AS O CARA;

SELECT NOME, SEXO, EMAIL FROM CLIENTE;

SELECT NOME, SEXO, EMAIL, ENDERECO FROM CLIENTE;

SELECT SEXO, EMAIL FROM CLIENTE;    */# A FORMA DE COLOCAR O SELECT MOSTRA A SEQUENCIA QUE TRAZ A CONSULTA #*/

### APENAS PARA FINS ACADEMICOS ###

SELECT * FROM CLIENTES;


*/# CONSULTA UTLIZANDO FILTRO WHERE */#

*/# ESSA FUNÇÃO ABAIXO VAI TRAZER APENAS INFORMAÇÃO MASCULINA DA TABELA */#

SELECT NOME, SEXO, FROM CLINTE
WHERE SEXO = 'M';

SELECT NOME, SEXO, FROM CLINTE
WHERE SEXO = 'F';

SELECT NOME, SEXO, FROM CLINTE
WHERE ENDERECO = 'RJ';

SHOW TABLES; Apenas no MYSQL traz qualquer coisa do banco #


## EXEMPLOS ##

''' ! Tipo	Explicação	Valores permitidos	Exemplo
BOOLEAN	Armazena um bit de informação, utilizado para verdadeiro ou falso.	Verdadeiro/falso	true/false
VARCHAR(n)	Uma string com tamanho máximo n	[0-9a-zA-Z]+{n}	"foo"
CHAR(n)	Uma string com tamanho fixo n	[0-9a-zA-Z]{n}	"foo"
SMALLINT	Número inteiro com 16 bits de precisão	\-?[0-9]+	584
INTEGER	Número inteiro com 32 bits de precisão	\-?[0-9]+	-8748
FLOAT	Número decimal	\-?[0-9]+[\.[0-9]+]?	48.96
NUMBER(n,[d])	Um número com n dígitos (e d dígitos decimais se mencionado)	\-?[0-9]+[\.[0-9]+]?	484.65
DATE	Uma data (Padrão americano)	[0-9][0-9][0-9][0-9]\-[0-1][0-9]\-[0-3][0-9]	2009-03-24
TIME	Um período de sessenta minutos; 1/24 de um dia	[0-2][0-9]\:[0-5][0-9]\:[0-5][0-9]	11:24:56
TIMESTAMP	Data e hora	[0-9]+	18648689595962
BLOB	Qualquer dado	Qualquer	'''



####    ####

SELECT COUNT * FROM CLIENTE;

SELECT COUNT * AS "QUANTIDADE" FROM CLIENTE;


#########  17.09.2019 #####

CREATE DATABASE ESTUDO;

USE ESTUDO;

CREATE TABLE CLIENTE(
	NOME VARCHAR(30),
	SEXO CHAR(1),
	EMAIL VARCHAR(30),
	CPF VARCHAR(11),
	TELEFONE VARCHAR(30),
	ENDERECO VARCHAR(100)
	CIDADE VARCHAR(30)
	ID VARCHAR(1000)
	);


INSERT INTO CLIENTE VALUES('RAFAEL','M','RAFAEL@GMAIL.COM',983638273,'229233110','MAIA LACERDA - ESTACIO - RIO DE JANEIRO - RJ','RIO DE JANEIRO',1);

INSERT INTO CLIENTE VALUES('ARTHUR','M','ARTHUR@GMAIL.COM',541521456,'25078869','RIACHUELO - CENTRO - RIO DE JANEIRO - RJ','RIO DE JANEIRO',2);

INSERT INTO CLIENTE VALUES('EVELYN','F',NULL,885755896,'58748895','OSCAR CURY - BOM RETIRO - PATOS DE MINAS - MG','MINAS GERAIS',3);

INSERT INTO CLIENTE VALUES('LUCIA','F',NULL,585755896,'58748895','OSCAR MARIA - BOM RETIRO - PATOS DE MINAS - SP','SÃO PAULO',4);

INSERT INTO CLIENTE VALUES('LUIS','M','LUIS@GMAIL.COM',685755896,'58748895','OSCAR SANTO - BOM RETIRO - CENTRO - SP','SÃO PAULO',5);

INSERT INTO CLIENTE VALUES('PEDRO','M','PEDRO@GMAIL.COM',785755896,'58748895','OSCAR FLEURY - BOM RETIRO - PERDIZES - SP','SÃO PAULO',6);

INSERT INTO CLIENTE VALUES('ADEMAR ','M','ADEMAR@GMAIL.COM',785755896,'58748895','ESTRADA CAPAO - VALE DO CAPAO - PALMEIRAS - BA','BAHIA',7);

INSERT INTO CLIENTE VALUES('PEDRO','M','PEDRO@GMAIL.COM',785755896,'58748895','OSCAR FLEURY - BOM RETIRO - PERDIZES - SP','SÃO PAULO',8);

INSERT INTO CLIENTE VALUES('LUIS CARLOS JUNIOR','M','PEDRO@GMAIL.COM',565755896,'58748895','BERNARDES MARCOLINO - VILA AURORA - ITAPEVI - SP','SÃO PAULO',9);

SELECT * FROM CLIENTE;

# CONTANDO QT DE LINHAS DA TABELA #
SELECT COUNT(*) FROM CLIENTE;

#QUANTIDADE DE REGISTROS DA TABELA#
SELECT COUNT(*) AS "QUANTIDADE DE REGISTROS DA TABELA"
FROM CLIENTE;

# APONTAR QUANTIDADE DE CADA SEXO TEM NA TABELA ##
SELECT SEXO, count(*) AS "QUANTIDADE"
FROM CLIENTE
GROUP BY SEXO;


# FUNÇÃO OR # MODO DE COMO CONTAR APENAS SEXO (F) NA TABELA  QUE MORA NO rIO DE JANEIRO

SELECT NOME, SEXO, ENDERECO
FROM CLIENTE
WHERE SEXO = 'f'
OR ENDERECO = 'RIO DE JANEIRO'


# FUNÇÃO AND # QUAM TEM A MENOR CONDIÇÃO DE SER VERDADEIRO NA TABELA #
SELECT NOME, SEXO, ENDERECO
FROM CLIENTE
WHERE ENDERECO = 'OSCAR CURY - BOM RETIRO - PATOS DE MINAS - MG'
AND SEXO = 'F';


SELECT * FROM CLIENTE;


# TRAZER CAMPOS NULO NA TABELA #
SELECT NOME, SEXO, ENDERECO
FROM CLIENTE
WHERE EMAIL = NULL;

# TRAZER CAMPOS É NULO NA TABELA #
SELECT NOME, SEXO, ENDERECO, EMAIL
FROM CLIENTE
WHERE EMAIL IS NULL;

# TRAZER CAMPOS NÃO NULO NA TABELA #
SELECT NOME, SEXO, ENDERECO, EMAIL
FROM CLIENTE
WHERE EMAIL IS NOT NULL;



CLAUSULA UPDATE

# CLAUSULA UPDATE PARA ATUALIZAR VALORES #

# MOSTRAR NA TABELA AS 2 COLUNAS NOME E EMAIL #
SELECT NOME, EMAIL
FROM CLIENTE;

# UTILIZAR O UPDATE SEMPRE ACOMPANHADO DA CLAUSULA WHERE #

UPDATE CLIENTE
SET EMAIL ='EVELYN@HOTMAIL.COM'
WHERE NOME ='EVELYN';

UPDATE CLIENTE
SET EMAIL ='LUCIA@GMAIL.COM'
WHERE NOME ='LUCIA';

###########################################


SELECT * FROM CLIENTE;

# INSERINDO COLUNA NA TABELA #
Alter table CLIENTE Add CIDADE VARCHAR(30);

ALTER TABLE CLIENTE ADD ID VARCHAR(1000);

# APAGAR COLUNA #
ALTER TABLE CLIENTE DROP COLUMN CIDADE;

# APAGAR LINHA DA TABELA #
DELETE FROM CLIENTE
WHERE NOME = 'PEDRO';

#### AULA 16 ####

** ENTRANDO COM MAIS TELEFONES **

# INSERINDO SEGUNDO TELEFONE NO REGIDTRO ##
UPDATE CLIENTE 
SET TELEFONE = '229233110 - 968894243'
WHERE NOME = 'RAFAEL'

SELECT * FROM CLIENTE;

# CONTANDO QT DE REGISDTRO POR CIDADE ##
SELECT CIDADE, COUNT(*) AS "QUANTIDADE"
FROM CLIENTE
GROUP BY CIDADE;

----------------------------------------

## 1 - FORMA NORMAL ##

/ 1 TODO CAMPO VETORIZADO SE TORNARÁ OUTRA TABELA > ELEMENTOS DO MESMO TIPO

/ 2 TODO CAMPO MULTIVALORADO SE TORNARÁ OUTRA TABELA > UM CAMPO DIVISIVEL 

/ 3 TODA TABELA NECESSITA DE PELO MENOS UM CAMPO QUE INDENTIFIQUE TODO O REGISTRO COMO SENDO ÚNICO.
 > É O QUE CHAMAMOS DE CHAVE PRIMÁRIA OU PRIMARY KEY*/

  / * PRIMEIRO ALGARISMO - OBRIGATORIEDADE
 0 - NÃO OBRIGATORIO
 1 - OBRIGATORIO

 / * SEGUNDO ALGARISMO - CARDINALIDADE
 1 - MAXIMO DE UM
 N - MAIS DE UM



  # MODELAGEM DO CLIENTE #

 CREATE DATABASE COMERCIO;

 USE COMERCIO;

 # ENTEDER COMO USAR VARIAVEL (ENUM) CAMPO SEXO - PARA FIXAR DOIS VALORES ###
  CREATE TABLE CLIENTE(
	IDCLIENTE INT PRIMARY KEY AUTO_INCREMENT,
	NOME VARCHAR(30) NOT NULL,
	EMAIL VARCHAR(50) UNIQUE, 
	CPF VARCHAR(15) UNIQUE,
	Sexo ENUM(1) NOT NULL
);
--------------------------------------

 # MODELAGEM DO CLIENTE #

CREATE DATABASE COMERCIO;

 USE COMERCIO;

CREATE TABLE CLIENTE(
	IDCLIENTE INT PRIMARY KEY AUTO_INCREMENT,
	NOME VARCHAR(30) NOT NULL,
	EMAIL VARCHAR(50) UNIQUE, 
	CPF VARCHAR(15) UNIQUE,
	Sexo ENUM('M','F') NOT NULL
);

create table TELEFONE(
	IDTELEFONE INT PRIMARY KEY AUTO_INCREMENT,
	TIPO ENUM('COM','RES','CEL'),
	NUMERO VARCHAR(10),
	ID_CLIENTE INT,
	FOREIGN KEY(ID_CLIENTE)
	REFERENCES CLIENTE(IDCLIENTE)
);

CREATE TABLE ENDERECO(
	IDENDERECO INT PRIMARY KEY AUTO_INCREMENT,
	RUA VARCHAR(30) NOT NULL,
	BAIRRO VARCHAR(30) NOT NULL,
	CIDADE VARCHAR(30) NOT NULL,
	ESTADO CHAR(2) NOT NULL,
	ID_CLIENTE INT UNIQUE,
	FOREIGN KEY(ID_CLIENTE)
	REFERENCES CLIENTE(IDCLIENTE)
);

/ * CHAVE ESTRANGEIRA - FK

É A CHAVE PRIMARIA DE UMA TABELA, QUE VAI ATÉ OUTRA TABELA FAZER REFERENCIA */

## APAGAR TABELA TELEFONE  ##
DROP TABLE TELEFONE;
ALTER TABLE TELEFONE DROP FOREIGN KEY ID_CLIENTE;
ALTER TABLE TELEFONE DROP INDEX ID_CLIENTE;


SELECT * FROM CLIENTE;

## INSERIRNDO INFORMAÇÕES NA TABELA CLIENTE ##
INSERT INTO CLIENTE VALUES(NULL,'RAFAEL','RAFAEL.MACEDO@BLUESHIFT.COM.BR',89011867090,'M');
INSERT INTO CLIENTE VALUES(NULL,'EVELYN','EVELYN.MACEDO@GMAIL.COM.BR',79011867090,'F');
INSERT INTO CLIENTE VALUES(NULL,'ARTHUR','ARTHUR.MACEDO@GMAIL.COM.BR',69011867090,'M');
INSERT INTO CLIENTE VALUES(NULL,'LINA','LINA.MACEDO@GMAIL.COM.BR',59011867090,'F');
INSERT INTO CLIENTE VALUES(NULL,'ADEMAR','ADEMAR.MACEDO@GMAIL.COM.BR',49011867090,'M');
INSERT INTO CLIENTE VALUES(NULL,'JUNIOR','JUNIOR.MACEDO@GMAIL.COM.BR',39011867090,'M');
INSERT INTO CLIENTE VALUES(NULL,'FERNANDO','FERNANDO.MACEDO@GMAIL.COM.BR',29011867090,'M');
INSERT INTO CLIENTE VALUES(NULL,'URSULA','URSULA.MACEDO@GMAIL.COM.BR',19011867090,'F');
INSERT INTO CLIENTE VALUES(NULL,'LUIS','LUIS.MACEDO@GMAIL.COM.BR',13011867090,'M');
INSERT INTO CLIENTE VALUES(NULL,'LUCIA','LUCIA.MACEDO@GMAIL.COM.BR',14011867090,'F');
INSERT INTO CLIENTE VALUES(NULL,'FERNANDO',NULL,15011867099,'M');


DESC ENDERECO;

## INSERIRNDO INFORMAÇÕES NA TABELA ENDEREÇO ##
INSERT INTO ENDERECO VALUES(NULL,'RUA A','CENTRO','BELO HORIZONTE','MG',1);
INSERT INTO ENDERECO VALUES(NULL,'RUA B','CENTRO','BELO HORIZONTE','MG',2);
INSERT INTO ENDERECO VALUES(NULL,'RUA C','CENTRO','BELO HORIZONTE','MG',3);
INSERT INTO ENDERECO VALUES(NULL,'RUA D','CENTRO','BELO HORIZONTE','MG',4);
INSERT INTO ENDERECO VALUES(NULL,'RUA E','CENTRO','BELO HORIZONTE','MG',5);
INSERT INTO ENDERECO VALUES(NULL,'RUA F','CENTRO','BELO HORIZONTE','MG',6);
INSERT INTO ENDERECO VALUES(NULL,'RUA G','CENTRO','BELO HORIZONTE','MG',7);
INSERT INTO ENDERECO VALUES(NULL,'RUA H','CENTRO','BELO HORIZONTE','MG',8);
INSERT INTO ENDERECO VALUES(NULL,'RUA I','CENTRO','BELO HORIZONTE','MG',9);
INSERT INTO ENDERECO VALUES(NULL,'RUA J','CENTRO','BELO HORIZONTE','MG',10);
INSERT INTO ENDERECO VALUES(NULL,'RUA L','CENTRO','BELO HORIZONTE','MG',11);

SELECT * FROM TELEFONE;
## INSERINDO INFORMAÇÕES NA TABELA TELEFONE ##
INSERT INTO TELEFONE VALUES(NULL,'CEL','968894250',4);
INSERT INTO TELEFONE VALUES(NULL,'COM','41415500',5);
INSERT INTO TELEFONE VALUES(NULL,'RES','21001010',6);
INSERT INTO TELEFONE VALUES(NULL,'CEL','968894244',7);
INSERT INTO TELEFONE VALUES(NULL,'COM','968894243',8);
INSERT INTO TELEFONE VALUES(NULL,'CEL','968894245',9);
INSERT INTO TELEFONE VALUES(NULL,'RES','32147890',10);
INSERT INTO TELEFONE VALUES(NULL,'CEL','968894246',11);
INSERT INTO TELEFONE VALUES(NULL,'COM','968894243',4);
INSERT INTO TELEFONE VALUES(NULL,'CEL','968894247',5);
INSERT INTO TELEFONE VALUES(NULL,'RES','21134567',6);


## INSERINDO NOVOS DADOS NAS 3 TABELAS ## 
INSERT INTO CLIENTE VALUES(NULL,'VAGNER','VAGNER.MACEDO@BLUESHIFT.COM.BR',56789034521,'M');
INSERT INTO CLIENTE VALUES(NULL,'MARIO','MARIO.MACEDO@GMAIL.COM.BR',83011867090,'M');
INSERT INTO CLIENTE VALUES(NULL,'ARTHUR','MARIA.ALMEIDA@GMAIL.COM.BR',73011867090,'F');
INSERT INTO CLIENTE VALUES(NULL,'ISABELA','ISABELA.TEMPONI@GMAIL.COM.BR',99911867456,'F');

INSERT INTO ENDERECO VALUES(NULL,'RUA MATRIZ','VILA AURORA','ITAPEVI','MG',16);
INSERT INTO ENDERECO VALUES(NULL,'RUA ONZE','SUBURBANO','JANDIRA','SP',13);
INSERT INTO ENDERECO VALUES(NULL,'RUA DA PAZ','PORTELA','BARUERI','SP',14);
INSERT INTO ENDERECO VALUES(NULL,'RUA WALTER BALTAZAR','PORTELA','CARAPICUIBA','SP',15);

INSERT INTO TELEFONE VALUES(NULL,'CEL','968894250',11);
INSERT INTO TELEFONE VALUES(NULL,'COM','41415500',12);
INSERT INTO TELEFONE VALUES(NULL,'RES','21001010',13);
INSERT INTO TELEFONE VALUES(NULL,'RES','966615112',15);

SELECT * FROM CLIENTE;
SELECT * FROM ENDERECO;
SELECT * FROM TELEFONE;


## CONCEITO ##

## SELEÇÃO - PROJEÇÃO - JUNÇÃO ##

## PROJEÇÃO TUDO QUE QUEREMOS MOSTRAR NA TELA ##
# PROJETANDO UMA TABELA #
SELECT NOW() AS "DATA"; 

SELECT NOME, NOW() AS "DATA" / > ISSO É UMA PROJEÇÃO
FROM CLIENTE;

### SELEÇÃO TEORIA DOS CONJUNTOS ###

SELECT NOME, SEXO
FROM CLIENTE;

SELECT NOME, SEXO
FROM CLIENTE
WHERE SEXO = 'M';  /* SELECAO */

UPDATE CLIENTE
SET SEXO = 'F'
WHERE IDCLIENTE = 5; /* SELECAO */

---------------------------------------

Banco de Dados

Comandos no SQL 

1- Grupo.

DML > (Data Manipulation Language) (Desenvolvimento)

> SELECT: Pesquisa
> UPDATE: Atualização de Dados
> DELETE: Eliminação de Dados
> INSERT: Inserção de Dados


2- Grupo.

DDL (Data Definition Language) (Suporte)

> CREATE: Definição de um objeto (tabela, Índice)
> ALTER: Alteração de um objeto.
> DROP: Eliminação de um objeto.


3-Grupo.

DCL > (Data Control Language) (Suporte/Desenvolvimento)

> GRANT : Fornecer um privilégio
> REVOKE : Tirar um privilégio

================================================================


## JUNCAO ##

SELECT NOME, SEXO, BAIRRO, CIDADE, "DATA"
FROM CLIENTE, ENDERECO
WHERE IDCLIENTE =ID_CLIENTE; /* CLAUSULA DE SELECAO */

SELECT NOME, SEXO, BAIRRO, CIDADE, "DATA"
FROM CLIENTE, ENDERECO
WHERE IDCLIENTE =ID_CLIENTE;
AND BAIRRO = 'CENTRO'

/* JOIN - JUNCAO */ 

SELECT NOME, SEXO, BAIRRO, CIDADE
FROM CLIENTE
INNER JOIN ENDERECO
ON IDCLIENTE = ID_CLIENTE
WHERE BAIRRO = 'CENTRO';  /* CLAUSULA DE SELECAO */

## PONTEIRANDO A QUERY ##

SELECT CLIENTE.NOME, CLIENTE.SEXO, ENDERECO.BAIRRO, ENDERECO.CIDADE, TELEFONE.TIPO, TELEFONE.NUMERO
FROM CLIENTE
INNER JOIN ENDERECO
ON CLIENTE.IDCLIENTE = ENDERECO.ID_CLIENTE
INNER JOIN TELEFONE
ON CLIENTE.IDCLIENTE = TELEFONE.ID_CLIENTE;


## APELIDANDO TABELAS COM AS INICIAIS ##

SELECT C.NOME, C.SEXO, E.BAIRRO, E.CIDADE, T.TIPO, T.NUMERO
FROM CLIENTE C
INNER JOIN ENDERECO E
ON C.IDCLIENTE = E.ID_CLIENTE
INNER JOIN TELEFONE T
ON C.IDCLIENTE = T.ID_CLIENTE;

## QUERY COMPLETA COM SELECAO - PROJECAO - JUNCAO ##
SELECT CLIENTE.NOME, CLIENTE.SEXO, ENDERECO.BAIRRO, ENDERECO.CIDADE, TELEFONE.TIPO, TELEFONE.NUMERO
FROM CLIENTE
INNER JOIN ENDERECO
ON CLIENTE.IDCLIENTE = ENDERECO.ID_CLIENTE
INNER JOIN TELEFONE
ON CLIENTE.IDCLIENTE = TELEFONE.ID_CLIENTE
WHERE SEXO = 'M';


## EXERCICIO DE FIXACAO ##


## EXERCICIO DE FIXACAO ##

CREATE DATABASE PROJETO;
USE PROJETO;

CREATE TABLE CLIENTE(
	IDCLIENTE INT PRIMARY KEY AUTO_INCREMENT,
	NOME VARCHAR(30) NOT NULL,
	EMAIL VARCHAR(50) UNIQUE, 
	CPF VARCHAR(15) UNIQUE,
	Sexo ENUM('M','F') NOT NULL
);

CREATE TABLE ENDERECO(
	IDENDERECO INT PRIMARY KEY AUTO_INCREMENT,
	RUA VARCHAR(30) NOT NULL,
	BAIRRO VARCHAR(30) NOT NULL,
	CIDADE VARCHAR(30) NOT NULL,
	ESTADO CHAR(2) NOT NULL,
	ID_CLIENTE INT UNIQUE,
	FOREIGN KEY(ID_CLIENTE)
	REFERENCES CLIENTE(IDCLIENTE)
    );

create table TELEFONE(
	IDTELEFONE INT PRIMARY KEY AUTO_INCREMENT,
	TIPO ENUM('COM','RES','CEL'),
	NUMERO VARCHAR(10),
	ID_CLIENTE INT,
	FOREIGN KEY(ID_CLIENTE)
	REFERENCES CLIENTE(IDCLIENTE)
    );

CREATE TABLE CARROS(
	IDCARROS INT PRIMARY KEY AUTO_INCREMENT,
	PLACA VARCHAR(30) NOT NULL,
	COR VARCHAR(30) NOT NULL,
	MODELO VARCHAR(30) NOT NULL,
	ID_CLIENTE INT UNIQUE,
	FOREIGN KEY(ID_CLIENTE)
	REFERENCES CLIENTE(IDCLIENTE)
    );


## INSERIRNDO INFORMAÇÕES NA TABELA CLIENTE ##
INSERT INTO CLIENTE VALUES(NULL,'LAIS','LAIS.SOUSA@BLUESHIFT.COM.BR',11111867090,'F');
INSERT INTO CLIENTE VALUES(NULL,'LIVIA','LIVIA.MACEDO@GMAIL.COM.BR',22211867090,'F');
INSERT INTO CLIENTE VALUES(NULL,'ARTHUR','ARTHUR.MACEDO@GMAIL.COM.BR',69011867090,'M');
INSERT INTO CLIENTE VALUES(NULL,'LARRISA','LARISSA.MACEDO@GMAIL.COM.BR',33311867090,'F');
INSERT INTO CLIENTE VALUES(NULL,'ADEMIR','ADEMIR.ALMEIDA@GMAIL.COM.BR',45611867090,'M');
INSERT INTO CLIENTE VALUES(NULL,'JUNIOR','JUNIOR.MACEDO@GMAIL.COM.BR',39011867090,'M');
INSERT INTO CLIENTE VALUES(NULL,'FERNANDA','FERNANDO.MENDES@GMAIL.COM.BR',29011867890,'F');
INSERT INTO CLIENTE VALUES(NULL,'URSULA','URSULA.MACEDO@GMAIL.COM.BR',19011867090,'F');
INSERT INTO CLIENTE VALUES(NULL,'LUIS','LUIS.MACEDO@GMAIL.COM.BR',13011867090,'M');
INSERT INTO CLIENTE VALUES(NULL,'LUCIA','LUCIA.MACEDO@GMAIL.COM.BR',14011867090,'F');
INSERT INTO CLIENTE VALUES(NULL,'FERNANDO',NULL,15011867099,'M');
INSERT INTO CLIENTE VALUES(NULL,'ALMIR','ALMIR.MACEDO@GMAIL.COM.BR',22311868090,'M');


## INSERIRNDO INFORMAÇÕES NA TABELA ENDEREÇO ##
INSERT INTO ENDERECO VALUES(NULL,'RUA ABC','CENTRO','BELO HORIZONTE','MG',1);
INSERT INTO ENDERECO VALUES(NULL,'RUA DEF','CENTRO','SAO PAULO','SP',2);
INSERT INTO ENDERECO VALUES(NULL,'RUA GHI','CENTRO','RIO DE JANEIRO','RJ',3);
INSERT INTO ENDERECO VALUES(NULL,'RUA JLM','CENTRO','RIO DE JANEIRO','RJ',4);
INSERT INTO ENDERECO VALUES(NULL,'RUA NOP','CENTRO','SAO PAULO','SP',5);
INSERT INTO ENDERECO VALUES(NULL,'RUA QRS','CENTRO','SAO PAULO','SP',6);
INSERT INTO ENDERECO VALUES(NULL,'RUA TUV','CENTRO','BELO HORIZONTE','MG',7);
INSERT INTO ENDERECO VALUES(NULL,'RUA XYZ','CENTRO','BELO HORIZONTE','MG',8);
INSERT INTO ENDERECO VALUES(NULL,'RUA MARCOLINO','CENTRO','BELO HORIZONTE','MG',9);
INSERT INTO ENDERECO VALUES(NULL,'RUA BERNARDES','CENTRO','BELO HORIZONTE','MG',10);
INSERT INTO ENDERECO VALUES(NULL,'RUA CAPAO','CARAMEZ','BAHIA','BA',11);
INSERT INTO ENDERECO VALUES(NULL,'RUA PALMEIRAS','BUENO','SAO PAULO','BSP',12);


## INSERINDO INFORMAÇÕES NA TABELA TELEFONE ##
INSERT INTO TELEFONE VALUES(NULL,'CEL','968894250',1);
INSERT INTO TELEFONE VALUES(NULL,'COM','41415500',2);
INSERT INTO TELEFONE VALUES(NULL,'RES','21001010',3);
INSERT INTO TELEFONE VALUES(NULL,'CEL','968894244',4);
INSERT INTO TELEFONE VALUES(NULL,'COM','968894243',5);
INSERT INTO TELEFONE VALUES(NULL,'CEL','968894245',6);
INSERT INTO TELEFONE VALUES(NULL,'RES','32147890',7);
INSERT INTO TELEFONE VALUES(NULL,'CEL','968894246',8);
INSERT INTO TELEFONE VALUES(NULL,'COM','968894243',9);
INSERT INTO TELEFONE VALUES(NULL,'CEL','968894247',10);
INSERT INTO TELEFONE VALUES(NULL,'RES','21134567',11);
INSERT INTO TELEFONE VALUES(NULL,'RES','235134569',12);

## INSERINDO INFORMAÇÕES NA TABELA CARROS ##
INSERT INTO CARROS VALUES(NULL,'CYS4505','BRANCO','GOL',1);
INSERT INTO CARROS VALUES(NULL,'EMA2010','PRETO','CAPTIVA',2);
INSERT INTO CARROS VALUES(NULL,'FRR1726','BRANCO','CRUZE',3);
INSERT INTO CARROS VALUES(NULL,'EER4040','AZUL','FUSCA',4);
INSERT INTO CARROS VALUES(NULL,'CSS5667','BRANCO','FIESTA',5);
INSERT INTO CARROS VALUES(NULL,'ENO0000','PRATA','UNO',6);
INSERT INTO CARROS VALUES(NULL,'CYZ0989','BEGE','SANTANA',7);
INSERT INTO CARROS VALUES(NULL,'CYS4678','BRANCO','SANTA FE',8);
INSERT INTO CARROS VALUES(NULL,'CYS6745','CREME','ECOSPORT',9);
INSERT INTO CARROS VALUES(NULL,'AAH9878','CINZA','ESCORT',10);
INSERT INTO CARROS VALUES(NULL,'ETR1720','PRETO','I30',11);
INSERT INTO CARROS VALUES(NULL,'EVT2209','VERMELHO','PRISMA',12);

Select * from cliente;

SELECT NOME, SEXO, BAIRRO, CIDADE, "DATA"
FROM CLIENTE, ENDERECO, TELEFONE, CARROS
WHERE IDCLIENTE =ID_CLIENTE; /* CLAUSULA DE SELECAO */

SELECT CLIENTE.NOME, CLIENTE.SEXO, ENDERECO.BAIRRO, ENDERECO.CIDADE, TELEFONE.TIPO, TELEFONE.NUMERO, CARROS.MODELO, CARROS.PLACA, CARROS.COR
FROM CLIENTE
INNER JOIN ENDERECO
ON CLIENTE.IDCLIENTE = ENDERECO.ID_CLIENTE
INNER JOIN TELEFONE
ON CLIENTE.IDCLIENTE = TELEFONE.ID_CLIENTE
INNER JOIN CARROS
ON CLIENTE.IDCLIENTE = CARROS.ID_CLIENTE;


*** EXERCICIO ***
## PARA UMA CAMPANHA DE MKT, O SETOR SOLICITOU UM RELATORIO COM NOME, EMAIL E TELEFONE CELULAR.alter
## DOS CLIENTES QUE MORAM NO ESTADO DO RIO DE JANEIRO VOCE TERA QUE PASSAR
## A QUERY PARA GERAR O RELATORIO PARA O PROGRAMA ##

USE COMERCIO;
SELECT C.NOME,C.EMAIL,T.NUMERO
FROM CLIENTE C
INNER JOIN TELEFONE T
ON C.IDCLIENTE = T.ID_CLIENTE
INNER JOIN ENDERECO E
ON C.IDCLIENTE = E.ID_CLIENTE
WHERE TIPO = 'CEL' AND ESTADO = 'MG';

## PARA UMA CAMPANHA DE PRODUTOS DE BELEZA, O COMERCIAL SOLICITOU
## UM RELATORIOCOM NOME, EMAIL E TELEFONE CELULAR DAS MULHERES
## QUE MORAM NO ESTADO DE SAO PAULO VOCE TERA QUE PASSAR A 
## A QUERY PARA GERAR O RELATORIO PARA O PROGRAMA

USE COMERCIO;

SELECT NOME, EMAIL, NUMERO
FROM CLIENTE
INNER JOIN TELEFONE T
ON IDCLIENTE = T.ID_CLIENTE
INNER JOIN ENDERECO E
ON IDCLIENTE = E.ID_CLIENTE
WHERE SEXO = 'F' AND TIPO = 'CEL' AND ESTADO = 'MG';


##  IFNULL ## RECEBE UM VALOR NULO E TRAZ NA INFORMAÇÃO DE SAIDA A MSG ##

SELECT C.NOME "CLIENTE" 
	   IFNULL(C.EMAIL,'SEM EMAIL') AS "EMAIL",
       T.NUMERO AS "CELULAR"
FROM CLIENTE C
INNER JOIN TELEFONE T
ON C.IDCLIENTE = T.ID_CLIENTE
INNER JOIN ENDERECO E
ON C.IDCLIENTE = E.ID_CLIENTE
WHERE TIPO = 'CEL' AND ESTADO = 'RJ';

IFNULL(C.EMAIL,'SEM EMAIL')    

##  IFNULL ## RECEBE UM VALOR NULO E TRAZ NA INFORMAÇÃO DE SAIDA A MSG ##
SELECT C.NOME "CLIENTE",
	   IFNULL(C.EMAIL,'SEM EMAIL') AS "EMAIL", 
	   T.NUMERO AS "CELULAR"
FROM CLIENTE C
INNER JOIN TELEFONE T
ON C.IDCLIENTE = T.ID_CLIENTE
INNER JOIN ENDERECO E
ON C.IDCLIENTE = E.ID_CLIENTE
WHERE TIPO = 'CEL' AND ESTADO = 'SP';



## CRIANDO A VIEW ##
CREATE VIEW RELATORIO AS
SELECT C.NOME,C.SEXO,
       ifnull(C.EMAIL,'SEM EMAIL') AS "EMAIL",
       T.TIPO,
       T.NUMERO,
       E.BAIRRO,
       E.CIDADE,
       E.ESTADO
FROM CLIENTE C
INNER JOIN TELEFONE T
ON C.IDCLIENTE = T.ID_CLIENTE
INNER JOIN ENDERECO E
ON C.IDCLIENTE = E.ID_CLIENTE;


SELECT * FROM RELATORIO;


## FILTARNDO DENTRO DA VIEW ##
SELECT * FROM RELATORIO
WHERE SEXO = 'F';

SELECT * FROM RELATORIO
WHERE SEXO = 'M';


## CRIANDO A VIEW UTILIZANDO SEMPRE V_ ##
CREATE VIEW V_RELATORIO AS
SELECT C.NOME,C.SEXO,
       ifnull(C.EMAIL,'SEM EMAIL') AS "EMAIL",
       T.TIPO,
       T.NUMERO,
       E.BAIRRO,
       E.CIDADE,
       E.ESTADO
FROM CLIENTE C
INNER JOIN TELEFONE T
ON C.IDCLIENTE = T.ID_CLIENTE
INNER JOIN ENDERECO E
ON C.IDCLIENTE = E.ID_CLIENTE;


## FILTARNDO DENTRO DA VIEW ##
SELECT * FROM V_RELATORIO
WHERE SEXO = 'F';

SELECT * FROM V_RELATORIO
WHERE SEXO = 'M';

## MOSTRAR TODAS AS TABELAS ##
SHOW TABLES;

DROP VIEW V_RELATORIO;

--------------------------------------------

## APAGANDO UM VIEW ##

DROP VIEW V_RELATORIO;

--------------------------------------------

## FAZER PROJECAO UTILIZANDO A VIEW ##
SELECT NOME, SEXO, CIDADE
FROM V_RELATORIO;
## NAO FAZ DELETE UTILIZANDO A VIEW DEVIDO INNER JOIN ##

## ORDENAR POR NOME ##
SELECT NOME, SEXO, CPF, CIDADE
FROM CLIENTE
INNER JOIN ENDERECO
ON IDCLIENTE = ID_CLIENTE
ORDER BY NOME;

## ORDENAR VISUALIZAÇÃO DO MAIOR PARA MENOR##
SELECT NOME, SEXO, CPF, CIDADE
FROM CLIENTE
INNER JOIN ENDERECO
ON IDCLIENTE = ID_CLIENTE
ORDER BY NOME, CPF ASC;

## ORDENANDO PELA COLUNA 4 DA TABELA ##
SELECT NOME, SEXO, CPF, CIDADE
FROM CLIENTE
INNER JOIN ENDERECO
ON IDCLIENTE = ID_CLIENTE
ORDER BY 4;

--------------------------------------------

## DELIMITADOR E ESTADO DE SERVIDOR ##

DELIMITER $
SELECT * FROM V_RELATORIO;
DELIMITER#
DELIMITER  #

##  PROCEDURES  ## 
## SEMPRE COLOCAR DELIMITER $ OU $$ ## 

DELIMITER $$
CREATE PROCEDURE CONTA()
BEGIN
    SELECT 10 + 20 AS "CONTA"; /*CORPO DO PROCEDIMENTO*/
END $$
DELIMITER ;

## CHAMANDO A PROCEDURE ##

CALL CONTA()$$

DELIMITER ;
