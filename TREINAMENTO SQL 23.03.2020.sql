TREINAMENTO SQL 23.03.2020


https://elias.praciano.com/2014/01/mysql-tipos-de-dados/


https://dev.mysql.com/

wampserver
http://www.wampserver.com/


-----------------------------------------------------
CREATE DATABASE TREINAMENTO;

DROP DATABASE TREINAMENTO;

CREATE DATABASE TREINAMENTO
DEFAULT CHARACTER SET utf8
DEFAULT COLLATE utf8_general_ci;
-----------------------------------------------------
USE TREINAMENTO;

CREATE TABLE TB_CATEGORIA (
Id_Categoria INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
Categoria VARCHAR(50) NOT NULL
) AUTO_INCREMENT = 1;

--------------------------------------------------
describe TB_CATEGORIA

--------------------------------------------------
DROP TABLE TB_CATEGORIA;

--------------------------------------------------
CREATE TABLE TB_CATEGORIA (
Id_Categoria INT PRIMARY KEY AUTO_INCREMENT,
Categoria VARCHAR(50) NOT NULL
) AUTO_INCREMENT = 1;
---------------------------------------------------

CREATE TABLE TB_EDITORA (
Id_Editora INT PRIMARY KEY AUTO_INCREMENT,
Editora VARCHAR(50) NOT NULL
) AUTO_INCREMENT = 1;


---------------------------------------------------

CREATE TABLE TB_AUTORES (
Id_Autor INT PRIMARY KEY AUTO_INCREMENT,
Nome_Autor VARCHAR(50) NOT NULL,
Sobrenome_Autor VARCHAR(50) NOT NULL,
Sexo ENUM('M', 'F'),
Nacionalidade VARCHAR(50) Default  'Brasil'
) AUTO_INCREMENT = 1,
 DEFAULT CHARSET = utf8;

---------------------------------------------------
 
 ALTER TABLE TB_AUTORES ADD Nascimento  DATE;

---------------------------------------------------
CREATE TABLE TB_LIVRO (
Id_Livro INT PRIMARY KEY AUTO_INCREMENT,
Nome_Livro VARCHAR(100) NOT NULL,
Data_Publicacao DATE NOT NULL,
Preco_Livro DECIMAL(6,2),
Id_Categoria  INT,
Id_Autor  INT,
Id_Editora INT,
 constraint fk_categoria FOREIGN KEY (Id_Categoria)  REFERENCES tb_categoria (Id_Categoria),
 constraint fk_autor FOREIGN KEY (Id_Autor)  REFERENCES tb_autores (Id_Autor)
) AUTO_INCREMENT = 1,
 DEFAULT CHARSET = utf8;

---------------------------------------------------

ALTER TABLE TB_LIVRO ADD
 constraint fk_editora FOREIGN KEY (Id_Editora)  REFERENCES tb_editora (Id_Editora);

---------------------------------------------------

Insert Into tb_autores(Nome_Autor, Sobrenome_Autor, Sexo, Nascimento)
Values('Clarice', 'Lispector', 'F', '1920-12-10');

---------------------------------------------------

Insert Into tb_categoria(Categoria)
Values('ROMANCE');

---------------------------------------------------
Insert Into tb_editora(Editora)
Values('ROCCO');
---------------------------------------------------
select * from tb_autores;

---------------------------------------------------
select * from tb_categoria;

---------------------------------------------------
select * from tb_editora;
---------------------------------------------------
SHOW TABLES;
---------------------------------------------------
Insert Into tb_livro(Nome_Livro, Data_Publicacao, Preco_Livro, Id_Categoria, Id_Autor, Id_Editora)
Values('A HORA DA ESTRELA', '1977-01-01', 20.50, 1, 1, 1);

---------------------------------------------------
Insert Into tb_livro
Values(DEFAULT, 'A HORA DA ESTRELA 2', '1977-01-01', 20.50, 1, 1, 1),
      (DEFAULT, 'OUTRO LIVRO', '1989-01-01', 33.50, 1, 1, 1),
      (DEFAULT, 'TESTE', '1997-01-01', 11.50, 1, 1, 1);


---------------------------------------------------
select * from tb_livro;

---------------------------------------------------

SELECT LI.NOME_LIVRO,
       LI.DATA_PUBLICACAO,
       LI.PRECO_LIVRO,
       AU.NOME_AUTOR,
       AU.SOBRENOME_AUTOR,
       CA.CATEGORIA,
       ED.EDITORA
  FROM TB_LIVRO  LI
 INNER JOIN TB_AUTORES   AU ON AU.ID_AUTOR     = LI.ID_AUTOR
 INNER JOIN TB_CATEGORIA CA ON CA.ID_CATEGORIA = LI.ID_CATEGORIA 
 INNER JOIN TB_EDITORA   ED ON ED.ID_EDITORA   = LI.ID_EDITORA

	--------------------------------------------------------------------------

	 <<<<<<<<<< DIA 2 >>>>>>>>>>>>>>>


	SELECT LI.NOME_LIVRO,
       LI.DATA_PUBLICACAO,
       LI.PRECO_LIVRO,
       AU.NOME_AUTOR,
       AU.SOBRENOME_AUTOR,
       CA.CATEGORIA,
       ED.EDITORA
  FROM TB_LIVRO  LI
 INNER JOIN TB_AUTORES   AU ON AU.ID_AUTOR     = LI.ID_AUTOR
 INNER JOIN TB_CATEGORIA CA ON CA.ID_CATEGORIA = LI.ID_CATEGORIA 
 INNER JOIN TB_EDITORA   ED ON ED.ID_EDITORA   = LI.ID_EDITORA;


SET FOREIGN_KEY_CHECKS=1;

ALTER TABLE `TB_LIVRO` 
	DROP INDEX  `fk_categoria`;
    
ALTER TABLE `TB_LIVRO` 
	DROP INDEX  `fk_autores`;    
    
ALTER TABLE `TB_LIVRO` 
	DROP INDEX  `fk_editora`;    

----------------------------------------------
ALTER TABLE tb_categoria ENGINE=InnoDB;
ALTER TABLE tb_autores   ENGINE=InnoDB;
ALTER TABLE tb_editora   ENGINE=InnoDB;
ALTER TABLE tb_livro     ENGINE=InnoDB;

----------------------------------------------
DROP TABLE TB_EDITORA;

----------------------------------------------
CREATE TABLE TB_EDITORA (
Id_Editora INT PRIMARY KEY AUTO_INCREMENT,
Editora VARCHAR(50) NOT NULL
) AUTO_INCREMENT = 1,
  ENGINE=InnoDB;

-------------------------------------------
Insert Into tb_editora(Editora)
Values('ROCCO');

Insert Into tb_editora(Editora)
Values('RELX GROUP');

Insert Into tb_editora(Editora)
Values('PEARSON');

-------------------------------------------
Insert Into tb_livro(Nome_Livro, Data_Publicacao, Preco_Livro, Id_Categoria, Id_Autor, Id_Editora)
Values('A HORA DA ESTRELA', '1977-01-01', 20.50, 6, 10, 1);

-------------------------------------------      
SELECT * FROM TB_AUTORES;

ALTER TABLE TB_AUTORES CHANGE DATA_NASCIMENTO DATA_NASCIMENTO_OLD DATE;

ALTER TABLE TB_AUTORES ADD Data_Nascimento DATE AFTER SEXO;

UPDATE TB_AUTORES SET Data_Nascimento = DATA_NASCIMENTO_OLD;

ALTER TABLE TB_AUTORES DROP DATA_NASCIMENTO_OLD;

ALTER TABLE TB_AUTORES ADD Data_Atualizacao DATETIME DEFAULT NOW() FIRST;

ALTER TABLE TB_AUTORES DROP Data_Atualizacao;

ALTER TABLE TB_AUTORES ADD Data_Atualizacao DATE;

ALTER TABLE TB_AUTORES MODIFY Data_Atualizacao DATETIME DEFAULT NOW();

UPDATE TB_AUTORES SET Data_Atualizacao = now();

ALTER TABLE TB_AUTORES DROP Data_Atualizacao;

ALTER TABLE TB_AUTORES ADD Data_Atualizacao DATETIME DEFAULT NOW();

ALTER TABLE TB_LIVRO RENAME TO TB_LIVROS;

SELECT * FROM TB_LIVROS;

-----------------------------------------------

CREATE TABLE IF NOT EXISTS TB_PESSOAS(
Id_pessoa       INT PRIMARY KEY AUTO_INCREMENT,
Nome_Pessoa     VARCHAR(100) UNIQUE NOT NULL,
Status          ENUM('A', 'I') NOT NULL,
Data_Cadastro   DATE
)AUTO_INCREMENT = 1,
 DEFAULT CHARSET = utf8;
 
 DESCRIBE TB_PESSOAS;
 
 DROP TABLE IF EXISTS TB_PESSOAS;

 -------------------------------------------
---------------------------------------------------
SELECT * FROM tb_autores;

INSERT INTO TB_AUTORES(Nome_Autor, Sobrenome_Autor, Sexo, Nacionalidade, Data_Nascimento)
Values('Maria', 'Joana', 'F', 'Portugal' ,'1980-01-01'),
      ('Joao', 'Clovis', 'M', 'Argentina', '2000-10-25'),
      ('Mateus', 'Gloria' , 'M', 'Brasil', '1999,08,05');

DELETE FROM TB_AUTORES
WHERE ID_AUTOR = 7;

UPDATE TB_AUTORES SET NOME_AUTOR = UPPER(NOME_AUTOR)
WHERE ID_AUTOR = 9;

UPDATE TB_AUTORES SET NOME_AUTOR = CONCAT(' ' , NOME_AUTOR)
WHERE ID_AUTOR = 3;

UPDATE TB_AUTORES SET NOME_AUTOR = TRIM(NOME_AUTOR)
WHERE ID_AUTOR = 3;

UPDATE TB_AUTORES SET NOME_AUTOR = UPPER(NOME_AUTOR);

UPDATE TB_AUTORES SET NOME_AUTOR = LOWER(NOME_AUTOR);

UPDATE TB_AUTORES SET NOME_AUTOR = 'Mateus'
where NOME_AUTOR = 'MATEUS';

-------------------------------------------------
CLONAR A TABELA TB_EDITORA

FAZER UNION E UNION ALL

CREATE TABLE `tb_editora_sis2` (
  `Id_Editora` int(11) NOT NULL AUTO_INCREMENT,
  `Editora` varchar(50) NOT NULL,
  PRIMARY KEY (`Id_Editora`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;



INSERT INTO tb_editora_SIS2(editora)
values ('ROCCO'),
       ('SARAIVA'),
       ('TESTE');
       
       
SELECT EDITORA
  FROM TB_EDITORA
UNION ALL
SELECT EDITORA
  FROM TB_EDITORA_SIS2

-------------------------------------------------
SELECT DISTINCT NOME_AUTOR,
       SOBRENOME_AUTOR,
       SEXO,
       DATA_NASCIMENTO,
       NACIONALIDADE
  FROM TB_AUTORES
-------------------------------------------------
SELECT COALESCE(SEXO, 'A') AS SEXO
FROM TB_AUTORES;

	SELECT NOME_LIVRO,
	   DATA_PUBLICACAO,
	   PRECO_LIVRO,
       ED.EDITORA
  FROM TB_LIVROS LI
  INNER JOIN TB_EDITORA   ED ON ED.ID_EDITORA   = COALESCE(LI.ID_EDITORA, -1) 



SELECT LI.NOME_LIVRO,
	   LI.DATA_PUBLICACAO,
	   LI.PRECO_LIVRO,
       AU.NOME_AUTOR,
       AU.SOBRENOME_AUTOR,
       CA.CATEGORIA,
       ED.EDITORA,
       LI.ID_EDITORA,
       LI.ID_AUTOR
FROM (
		SELECT NOME_LIVRO,
			   DATA_PUBLICACAO,
			   PRECO_LIVRO,
			   COALESCE(ID_CATEGORIA, -1) AS ID_CATEGORIA,
			   COALESCE(ID_AUTOR, -1) AS ID_AUTOR,
			   COALESCE(ID_EDITORA, -1) AS ID_EDITORA
		  FROM TB_LIVROS
      ) AS LI  
 LEFT JOIN TB_AUTORES   AU ON AU.ID_AUTOR     = LI.ID_AUTOR
 LEFT JOIN TB_CATEGORIA CA ON CA.ID_CATEGORIA = LI.ID_CATEGORIA 
 LEFT JOIN TB_EDITORA   ED ON ED.ID_EDITORA   = LI.ID_EDITORA;

---------------------------------------------------

SELECT NOME_LIVRO,
       AVG(PRECO_LIVRO) PRECO_LIVRO,
       COUNT(1) COUNT
  FROM TB_LIVROS
 GROUP BY NOME_LIVRO
 HAVING COUNT(1) > 1

-------------------------------------------------

TRUNCATE TABLE tb_editora_sis2;
TRUNCATE  tb_editora_sis2;



--------------------------------------------------------------------------

	 <<<<<<<<<< DIA 3 >>>>>>>>>>>>>

	 SELECT *
FROM TB_LIVRO;

UPDATE TB_LIVRO SET NOME_LIVRO = UPPER('Dom Quixote') , PRECO_LIVRO = 30.00
WHERE ID_LIVRO = 6;

UPDATE TB_LIVRO SET NOME_LIVRO = UPPER('A Divina comedia') ,ID_CATEGORIA = 3, ID_EDITORA = 2
WHERE NOME_LIVRO = 'A HORA DA ESTRELA';

/* tirar o flag da preferencia 
   sql editor*/
   
UPDATE TB_LIVRO SET NOME_LIVRO = UPPER('A Divina comedia') ,ID_CATEGORIA = 3, ID_EDITORA = 2
WHERE NOME_LIVRO = 'A HORA DA ESTRELA'
limit 1;   


SELECT * 
 FROM TB_LIVROS
WHERE NOME_LIVRO = 'A HORA DA ESTRELA'
  AND ID_AUTOR IS NULL ;


SELECT * 
 FROM TB_LIVROS
WHERE NOME_LIVRO = 'A HORA DA ESTRELA'
  AND ID_AUTOR IS NOT NULL ;




SELECT COUNT(1) 
FROM(
		SELECT LI.NOME_LIVRO,
			   LI.DATA_PUBLICACAO,
			   LI.PRECO_LIVRO,
			   AU.NOME_AUTOR,
			   AU.SOBRENOME_AUTOR,
			   CA.CATEGORIA,
			   ED.EDITORA
		  FROM TB_LIVROS  LI
		 INNER JOIN TB_AUTORES   AU ON AU.ID_AUTOR     = LI.ID_AUTOR
		 INNER JOIN TB_CATEGORIA CA ON CA.ID_CATEGORIA = LI.ID_CATEGORIA 
		 INNER JOIN TB_EDITORA   ED ON ED.ID_EDITORA   = LI.ID_EDITORA
    ) AS COUNT; 

-------------------------------------------------------------------
SELECT * 
  FROM TB_LIVROS 
WHERE ID_AUTOR NOT IN (SELECT ID_AUTOR
						FROM tb_autores)
OR ID_AUTOR IS NULL;


SELECT *
  FROM TB_LIVROS LI
 WHERE NOT EXISTS (SELECT 1
                    FROM TB_AUTORES AU
				   WHERE AU.ID_AUTOR = LI.ID_AUTOR);

 -------------------------------------------------------------



SELECT *
  FROM TB_LIVROS LI
 WHERE  EXISTS (SELECT 1
                    FROM TB_AUTORES AU
				   WHERE AU.ID_AUTOR = LI.ID_AUTOR);


 ------------------------------------------------------------

 SELECT *
  FROM TB_LIVROS LI
ORDER BY NOME_LIVRO  ASC;

SELECT *
  FROM TB_LIVROS LI
ORDER BY PRECO_LIVRO DESC;

------------------------------------------------------------
SELECT * 
  FROM TB_LIVROS 
WHERE ID_CATEGORIA NOT IN (SELECT ID_CATEGORIA
						FROM TB_CATEGORIA);

SELECT * 
  FROM TB_LIVROS 
WHERE ID_EDITORA NOT IN (SELECT ID_EDITORA
						FROM TB_EDITORA);

SELECT * 
  FROM TB_LIVROS 
WHERE ID_AUTOR IN (SELECT ID_AUTOR
					FROM TB_AUTORES);


SELECT COUNT(1) 
FROM(
		SELECT LI.NOME_LIVRO,
			   LI.DATA_PUBLICACAO,
			   LI.PRECO_LIVRO,
			   AU.NOME_AUTOR,
			   AU.SOBRENOME_AUTOR,
			   CA.CATEGORIA,
			   ED.EDITORA
		  FROM TB_LIVROS  LI
		  LEFT JOIN TB_AUTORES   AU ON AU.ID_AUTOR     = LI.ID_AUTOR
		 INNER JOIN TB_CATEGORIA CA ON CA.ID_CATEGORIA = LI.ID_CATEGORIA 
		 INNER JOIN TB_EDITORA   ED ON ED.ID_EDITORA   = LI.ID_EDITORA
    ) AS COUNT; 
 

---------------------------------------------------

 SELECT * 
   FROM TB_AUTORES AU
   WHERE NOT EXISTS (SELECT 1
                       FROM TB_LIVROS LI
                       WHERE LI.ID_AUTOR = AU.ID_AUTOR);

SELECT * FROM TB_AUTORES
WHERE NOME_AUTOR = 'CLARICE'
 AND NACIONALIDADE IS NULL;


DELETE FROM TB_AUTORES
WHERE NOME_AUTOR = 'CLARICE'
 AND NACIONALIDADE IS NULL;
 
 

--------------------------------------------------
CREATE TABLE `tb_categoria_2` (
  `Id_Categoria` int(11) NOT NULL AUTO_INCREMENT,
  `Categoria` varchar(50) NOT NULL,
  PRIMARY KEY (`Id_Categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

insert into tb_categoria_2(id_categoria, categoria)
select * from tb_categoria;

select * from tb_categoria_2;
---------------------------------------------------
IMPORTAR CSV.


select * from treinamento.tb_categoria_2;

DELETE FROM TB_CATEGORIA WHERE ID_CATEGORIA IN  (10, 11, 12, 13, 14, 15, 16);


----------------------------------------------------
CREATE TABLE `tb_autores_STG` (
  `Id_Autor` int(11) NOT NULL AUTO_INCREMENT,
  `Nome_Autor` varchar(50) NOT NULL,
  `Sobrenome_Autor` varchar(50) NOT NULL,
  `Sexo` enum('M','F') DEFAULT NULL,
  `Data_Nascimento` date DEFAULT NULL,
  `Nacionalidade` varchar(50) DEFAULT 'Brasil',
  `Data_Atualizacao` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Id_Autor`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-----------------------------------
INSERT INTO tb_autores_STG
SELECT * FROM tb_autores;


UPDATE tb_autores_STG SET NACIONALIDADE = 'USA'
WHERE ID_AUTOR = 10;

-----------------------------------

BEGIN TRANSACTION
MERGE
  TREINAMENTO.TB_AUTORES AS DESTINO
USING TREINAMENTO.TB_AUTORES_STG AS ORIGEM
ON (DESTINO.ID_AUTOR = ORIGEM.ID_AUTOR)
WHEN MATCHED THEN -- CASO EXISTA REGISTROS
  UPDATE SET DESTINO.NACIONALIDADE = ORIGEM.NASCIONALIDADE
WHEN NOT MATCHED BY TARGET THEN -- CASO NAO EXISTA
  INSERT INTO (NOME_AUTOR, SOBRENOME_AUTOR, SEXO, DATA_NASCIMENTO, NACIONALIDADE, DATA_ATUALIZACAO)  
  VALUES(ORIGEM.NOME_AUTOR, ORIGEM.SOBRENOME_AUTOR, ORIGEM.SEXO, ORIGEM.DATA_NASCIMENTO, ORIGEM.NACIONALIDADE, DEFAULT);
  
--    ROLLBACK TRANSACTION 
    
--    COMMIT TRANSACTION
END;    

----------------------------------------------

SELECT *
  FROM TB_LIVROS
WHERE DATA_PUBLICACAO BETWEEN '1977-01-01' AND '1989-01-01';

----------------------------------------------
CREATE OR REPLACE VIEW VW_LISTAGEM_LIVRO AS
SELECT LI.NOME_LIVRO,
       LI.DATA_PUBLICACAO,
       LI.PRECO_LIVRO,
       AU.NOME_AUTOR,
       AU.SOBRENOME_AUTOR,
       CA.CATEGORIA,
       ED.EDITORA
  FROM TB_LIVROS LI
 INNER JOIN TB_AUTORES   AU ON AU.ID_AUTOR     = LI.ID_AUTOR
 INNER JOIN TB_CATEGORIA CA ON CA.ID_CATEGORIA = LI.ID_CATEGORIA 
 INNER JOIN TB_EDITORA   ED ON ED.ID_EDITORA   = LI.ID_EDITORA;
 
  SELECT * FROM VW_LISTAGEM_LIVRO;

--------------------------------------------
DELIMITER $
CREATE TRIGGER TRG_DT_ATUALIZACAO_AUTOR 
 BEFORE UPDATE ON TB_LIVROS
FOR EACH ROW
BEGIN
  UPDATE TB_AUTORES SET DATA_ATUALIZACAO = NOW()
  WHERE ID_AUTOR = NEW.ID_AUTOR;
END$

DELIMITER ;

DROP  TRIGGER TRG_DT_ATUALIZACAO_AUTOR 


SELECT * FROM TB_AUTORES;
SELECT * FROM TB_LIVROS;

UPDATE TB_LIVROS SET PRECO_LIVRO = 40
WHERE ID_LIVRO = 2;

---------------------------------------------
SELECT NOME_LIVRO,
       CASE WHEN NOME_LIVRO = 'A HORA DA ESTRELA' THEN
         1
	   ELSE
         CASE WHEN NOME_LIVRO = 'A DIVINA COMEDIA' THEN
		   2
		 ELSE
           3
		END
	   END VALORES
  FROM TB_LIVROS

 --------------------------------------------------------------------
SELECT SUM(PRECO_LIVRO) OVER(PARTITION BY NOME_LIVRO)  AS R
  FROM TB_LIVROS;


  --------------------------------------------------------------------

POWER BI

  Dcalendario1 = 
ADDCOLUMNS(
CALENDARAUTO();
"ANO"; FORMAT ([DATE]; "YYYY");
"MES NOME"; FORMAT([DATE]; "MMM");
"MES NUMERO"; MONTH([DATE];
"TRIMESTRE"; FORMAT([DATE]; "q");
"ANO MES"; CONCATENATE(YEAR([DATE]); FORMAT(MONTH([DATE]); "00");
"DIA SEMANA ANO"; WEEKDAY([DATE]));))

--  Codigo para criar tabela calendario com todas as regras de data etc 

DCalendario = 
ADDCOLUMNS(
    CALENDARAUTO(),
    "Ano",FORMAT([Date],"yyyy"),
    "Mes Nome", FORMAT([Date],"mmm"),
    "Mes Numero", MONTH([Date]),
    "Trimestre", FORMAT([Date],"q"),
    "Ano Mes", CONCATENATE(YEAR([Date]),FORMAT(MONTH([Date]), "00")),
    "Dia Semana Ano", WEEKDAY([Date]))

 --------------------------------------------------------------------

 >>>  Medidas em DAX usadas no treinamento de power bi feitas pelo Lucas Silva  <<<


 %MoM = DIVIDE([Total Vendas]-[Total Vendas Ultimo Mes];[Total Vendas Ultimo Mes];0,1)

 %Vendas = DIVIDE([Total Vendas];[Total Venda All];0)

 Media Vendas = AVERAGE(FVendas[ValorVenda])

 Rank = RANKX(ALL(DProduto[Produto]); [Total Vendas];;DESC)

 RealouACC = 
VAR EscolhaACCouReal = SELECTEDVALUE(RealAcc[Real ou ACC])
Return
IF(EscolhaACCouReal = "Real";[Total Vendas];
    IF(EscolhaACCouReal = "ACC"; [Tota Acumulado];[Total Vendas]))


Tota Acumulado = CALCULATE([Total Vendas]; DATESYTD(DCalendario[Date]))


Total acumulado de Total Vendas em Date = 
CALCULATE(
	[Total Vendas];
	FILTER(
		ALLSELECTED('DCalendario'[Date]);
		ISONORAFTER('DCalendario'[Date]; MAX('DCalendario'[Date]); DESC)
	)
)


Total Acumulado Geral = 
    CALCULATE([Total Vendas];
            FILTER(ALL(DCalendario[Date]); 
                    DCalendario[Date] <= MAX(DCalendario[Date])
                   )
            )


Total Venda All = CALCULATE([Total Vendas]; ALL(DProduto))


Total Vendas = SUM(FVendas[ValorVenda])

Total Vendas Ultimo Ano = CALCULATE([Total Vendas]; DATEADD(DCalendario[Date];-1;YEAR))

Total Vendas Ultimo Ano 2 = CALCULATE([Total Vendas]; PARALLELPERIOD(DCalendario[Date];-1;YEAR))

Total Vendas Ultimo Mes = CALCULATE([Total Vendas]; PARALLELPERIOD(DCalendario[Date];-1;MONTH))

Venda Maxima = MAX(FVendas[ValorVenda])

Venda Minima = MIN(FVendas[ValorVenda])

YoY = ([Total Vendas]-[Total Vendas Ultimo Ano 2])/[Total Vendas Ultimo Ano 2]

YoY 2 = DIVIDE([Total Vendas]-[Total Vendas Ultimo Ano 2];[Total Vendas Ultimo Ano 2];0,1)


--------------------------------------------------------------------

Prova (Power Bi)

Linguagem M -> para inserir coluna ID

= Table.TransformColumns(#"Linhas Agrupadas", {"tabela", each Table.AddIndexColumn(_, "ClienteID", 1, 1)})

	