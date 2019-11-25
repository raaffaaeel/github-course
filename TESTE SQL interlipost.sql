Email

Olá Evelyn, tudo bem? 

Primeiramente gostaria de agradecer sua disponibilidade em participar de um processo seletivo na Intelipost.

Gostaria que você realizasse dois testes: SQL e API. Aguardo retorno até amanhã, Quarta-feira (13/11) às 18hrs, por favor. Faça o máximo que puder.

1. SQL

Usando https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all : 

(1) Qual é o nome do cliente que comprou a maior quantidade de "Tofu"?

(2) Quais são os 3 produtos mais vendidos?

(3) Qual é a soma dos preços dos produtos comprados por clientes que possuem “Maria” como contato?

Instruções:
As respostas devem ser suas queries, pois assim conseguiremos avaliar como você chegou aos resultados.
Não é necessário instalar o SQL e criar o banco e tabelas. Você deve utilizar o client sql online disponibilizado pela w3schools.
O nome de algumas funções pode mudar dependendo do gerenciador de banco (microsoft, oracle, postgree etc). Atenção a este ponto ao utilizar as funções.

2. API

Problema:
Identifique no arquivo anexo (JSON) e aponte o erro em sua estrutura. Este JSON trata-se de um pedido de envio (pedido fechado no site do cliente) que precisa ser criado na Intelipost. 
Existem campos necessários no JSON para que o pedido possa ser criado, mas se estiverem fora da estrutura padrão estabelecida em nossa documentação (https://docs.intelipost.com.br/v1/pedido-de-envio/criar-pedido-de-envio) o pedido não seria criado corretamente. 

Acesso ao Painel Intelipost
https://secure.intelipost.com.br/dashboard  

usuario - felipe.araujo@intelipost.com.br
senha - felipe.araujo@intelipost.com.br  

API Key para teste no Docs: d518d1f05d7071792cadadf047c99d21680d81c51d37aebb88b9845418d0e08d

Qualquer dúvida, estou à disposição.


SELECT 
	orders.OrderID,
    orders.CustomerID,
    detail.ProductId,
    detail.Quantity,
    prod.ProductName,
    cliente.CustomerName
FROM 
	OrderDetails as detail
INNER JOIN 
	Orders as orders
ON
	orders.OrderId = detail.OrderId
INNER JOIN
	Products as prod
ON 
	detail.ProductID = prod.ProductID
INNER JOIN 
	Customers as cliente
ON orders.CustomerID = cliente.CustomerID
WHERE 
	prod.ProductName = 'Tofu'
	




SELECT 
    prod.ProductName,
    cliente.CustomerName,
    sum(detail.Quantity)
FROM  OrderDetails as detail
INNER JOIN 	Orders as orders
ON 	orders.OrderId = detail.OrderId
INNER JOIN 	Products as prod
ON 	detail.ProductID = prod.ProductID
INNER JOIN 	Customers as cliente
ON orders.CustomerID = cliente.CustomerID
WHERE 
	prod.ProductName = 'Tofu' 
GROUP BY 
	prod.ProductName,
    cliente.CustomerName
ORDER BY 
	sum(detail.Quantity) DESC



Olá Evelyn, tudo bem? 

Primeiramente gostaria de agradecer sua disponibilidade em participar de um processo seletivo na Intelipost.

Gostaria que você realizasse dois testes: SQL e API. Aguardo retorno até amanhã, Quarta-feira (13/11) às 18hrs, por favor. Faça o máximo que puder.

1. SQL

Usando https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all : 

(1) Qual é o nome do cliente que comprou a maior quantidade de "Tofu"?

SELECT 
    prod.ProductName,
    cliente.CustomerName,
    sum(detail.Quantity)
FROM  OrderDetails as detail
INNER JOIN 	Orders as orders
ON 	orders.OrderId = detail.OrderId
INNER JOIN 	Products as prod
ON 	detail.ProductID = prod.ProductID
INNER JOIN 	Customers as cliente
ON orders.CustomerID = cliente.CustomerID
WHERE 
	prod.ProductName = 'Tofu' 
GROUP BY 
	prod.ProductName,
    cliente.CustomerName
ORDER BY 
	sum(detail.Quantity) DESC

RESPOSTA --> PRODUTO > Tofu	CLIENTE >Save-a-lot Markets	QUANTIDADE > 42 


(2) Quais são os 3 produtos mais vendidos?

SELECT
    detail.ProductId,
    prd.ProductName,
    sum(detail.Quantity) as Total_Vendido
FROM  OrderDetails as detail
INNER JOIN 	Products as prd
ON 	detail.ProductId = prd.ProductId

GROUP BY 
	detail.ProductId,
	prd.ProductName
ORDER BY 
	sum(detail.Quantity) DESC


respostas:

ID  Nome Produtos       QT
31	Gorgonzola Telino	458
60	Camembert Pierrot	430
35	Steeleye Stout	    369



(3) Qual é a soma dos preços dos produtos comprados por clientes que possuem “Maria” como contato?

Resposta:

SELECT 
    prod.Price,
    cliente.CustomerName,
    sum(detail.Quantity)
FROM  OrderDetails as detail
INNER JOIN 	Orders as orders
ON 	orders.OrderId = detail.OrderId
INNER JOIN 	Products as prod
ON 	detail.ProductID = prod.ProductID
INNER JOIN 	Customers as cliente
ON orders.CustomerID = cliente.CustomerID

WHERE CustomerName LIKE ‘MARIA’

GROUP BY 
	prod.ProductName,
    cliente.CustomerName
ORDER BY 
	sum(detail.Quantity) DESC

Instruções:
As respostas devem ser suas queries, pois assim conseguiremos avaliar como você chegou aos resultados.
Não é necessário instalar o SQL e criar o banco e tabelas. Você deve utilizar o client sql online disponibilizado pela w3schools.
O nome de algumas funções pode mudar dependendo do gerenciador de banco (microsoft, oracle, postgree etc). Atenção a este ponto ao utilizar as funções.



SELECT CODIGO, NOME FROM CLIENTES
WHERE NOME LIKE ‘%MARIA%’



Price = Products  >>> Prod

OrderID = OrderDetails  >>>  detail

ContactName = Customers  >>> Cliente


SELECT 
    prod.Price,
    cliente.CustomerName,
    sum(detail.Quantity)
FROM  OrderDetails as detail
INNER JOIN 	Orders as orders
ON 	orders.OrderId = detail.OrderId
INNER JOIN 	Products as prod
ON 	detail.ProductID = prod.ProductID
INNER JOIN 	Customers as cliente
ON orders.CustomerID = cliente.CustomerID

WHERE CustomerName LIKE ‘MARIA’

GROUP BY 
	prod.ProductName,
    cliente.CustomerName
ORDER BY 
	sum(detail.Quantity) DESC

---------------------------------------------------------------------------------



SELECT DISTINCT RDTGER,RDTNASC,RDTCAD,RDTCONS,RDTS_RF,RDTSTATUS,RDTAPRV
FROM STG.GAN_SCADGER
--NULL
--20171114
--20180921
--F


COALESCE(try_cast(convert(varchar(10), TRY_CONVERT(DATE, RLASTUPD, 3), 112) as int), 19000101) as 'CLI_DT_ULTIMA_ATUALIZACAO'

select top 10
	t1.campo,
	--cast(t1.campo as int) as cast_int,
	COALESCE(try_cast(convert(varchar(10), TRY_CONVERT(DATE, t1.campo, 3), 112) as int), 19000101) as try_cast_convertendo_data,
	try_cast(t1.campo as int) as validacao 
from 
	(select RDTAPRV as campo from STG.GAN_SCADGER) as t1
where try_cast(t1.campo as int) is null 
AND t1.campo is not null
--and t1.campo <> 'T'


select convert(varchar(10), '04/05/06', 121)

select convert(date, '04/05/06',112) 


select CONVERT(DATE, '19/05/06', 3)

select cast(convert(varchar(10), CONVERT(DATE, RLASTUPD, 3), 112) as int) 


select cast(convert(varchar(10), GETDATE(), 112) as int) as 'PRD_DT_PROCESSAMENTO'



SELECT DISTINCT RDTGER,RDTNASC,RDTCAD,RDTCONS,RDTS_RF,RDTSTATUS,RDTAPRV
FROM STG.GAN_SCADGER
--NULL
--20171114
--20180921
--F


COALESCE(try_cast(convert(varchar(10), TRY_CONVERT(DATE, RLASTUPD, 3), 112) as int), 19000101) as 'CLI_DT_ULTIMA_ATUALIZACAO'

select top 10
	t1.campo,
	--cast(t1.campo as int) as cast_int,
	COALESCE(try_cast(convert(varchar(10), TRY_CONVERT(DATE, t1.campo, 3), 112) as int), 19000101) as try_cast_convertendo_data,
	try_cast(t1.campo as int) as validacao 
from 
	(select RDTAPRV as campo from STG.GAN_SCADGER) as t1
where try_cast(t1.campo as int) is null 
AND t1.campo is not null
--and t1.campo <> 'T'


select convert(varchar(10), '04/05/06', 121)

select convert(date, '04/05/06',112) 


select CONVERT(DATE, '19/05/06', 3)

select cast(convert(varchar(10), CONVERT(DATE, RLASTUPD, 3), 112) as int) 


select cast(convert(varchar(10), GETDATE(), 112) as int) as 'PRD_DT_PROCESSAMENTO'



___________________________________________________________________________________


COALESCE(try_cast(convert(varchar(10), TRY_CONVERT(DATE, BDT, 3), 112) as int), 19000101) as 'VND_DT_VENDA',

cast(trim(DTSAIDA) as int) as 'VND_DT_SAIDA',

cast(replace(convert(varchar(10), GETDATE(), 120), '-', '') as int) as 'VND_DT_PROCESSAMENTO',

-- Apontar as colunas e tipo da tabela --
select * from INFORMATION_SCHEMA.COLUMNS
where TABLE_NAME = 'GAN_TMPVM'

-- Alterando data '2019-01-09' para 20190109 --
select COALESCE(try_cast(convert(varchar(10), TRY_CONVERT(DATE, '2019-01-09', 23), 112) as int), 19000101)

-- Teste de campos --
SELECT DISTINCT BTAB
FROM STG.GAN_TMPVM


select CONVERT(DATE, '2019-01-09', 23)

select coalesce('jessica', null, 'rafa') as teste


---------------------------------------------------------

Cast feito para transformar os tipos criados inicialmente como Varchar(4000) nas tabelas STG 

Ele altera os tipos inseridos na STG e insere na WRK certos.

CREATE PROCEDURE PRC_INS_WRK_VENDAS
AS

TRUNCATE TABLE WRK.BFS_FAT_VENDAS

INSERT INTO WRK.BFS_FAT_VENDAS
SELECT
	BFIL as 'VND_NU_FILIAL',
	COALESCE(try_cast(convert(varchar(10), TRY_CONVERT(DATE, BDT, 23), 112) as int), 19000101) as 'VND_DT_VENDA',
	COALESCE(DIMLOJA.TAB_SK_TABELA, -1) as 'TAB_SK_CODIGO ',
	cast(trim(BNF) as bigint) as 'VND_NU_NOTAFISCAL',
	COALESCE(DIMPRODUTO.PRD_SK_PRODUTO, -1) as 'PRD_SK_PRODUTO',
	BPROD as 'PRD_DS_CLASSIFICACAO',
	COALESCE(DIMLINHA.LIN_SK_LINHA, -1) as 'LIN_SK_LINHA',
	COALESCE(DIMVENDEDOR.VEN_SK_VENDEDOR, -1)  as 'VEN_SK_VENDEDOR',
	cast(trim(BQTE) as int) as 'VND_NU_QUANTIDADE',
	cast(trim(BVRNF) as float) as 'VND_VL_NOTAFISCAL',
	cast(trim(BVRIMP) as float) as 'VND_VL_IMPOSTO',
	cast(trim(BDFIN) as float) as 'VND_VL_JUROSFINANCEIROS',
	cast(trim(BVLIQ) as float) as 'VND_VL_VALORLIQUIDO',
	cast(trim(BCREP) as float) as 'VND_VL_FATURAMENTOLIQUIDO',
	cast(trim(BCOMIS) as float) as 'VND_VL_COMISSAO',
	cast(trim(BFRETE) as float) as 'VND_VL_FRETE',
	cast(trim(BMG2) as float) as 'VND_VL_MARGEM2',
	cast(trim(BPORC_MG2) as float) as 'VND_PC_MARGEM2',
	cast(trim(BMG3) as float) as 'VND_VL_MARGEM3',
	cast(trim(BPORC_MG3) as float) as 'VND_PC_MARGEM3',
	cast(trim(BTX_DESC) as float) as 'VND_VL_DESCONTO', 
	BTX_AUTOR  as 'VND_DS_RESPONSAVELDESCONTO',
	cast(trim(BPED) as bigint) as 'VND_NU_PEDIDO',
	COALESCE(DIMCLIENTE.CLI_SK_CLIENTE, -1) as 'CLI_SK_CLIENTE',
	NULL as 'CPG_SK_CODIGO',  -- BCPG
	cast(trim(BMG) as float) as 'VND_VL_MARGEM',
	cast(trim(BPORC) as float) as 'VND_PC_MARGEM',
	BCLASSE as 'VND_DS_CLASSE',
	BSERIE as 'VND_NU_SERIE',
	cast(trim(BREBATE) as float) as 'VND_VL_REBATE',
	BCAT as 'VND_DS_CATEGORIA',
	cast(trim(BFOR_PED) as bigint) as  'VND_NU_ORDEMCOMPRA',
	cast(trim(BFOR_AV) as float) as 'VND_VL_PRECOCOMPRA',
	cast(trim(BENC_CP) as float) as 'VND_VL_ENCARGOS',
	cast(trim(BJUR) as float) as 'VND_VL_JUROS',
	cast(trim(BMB1) as float) as 'VND_VL_MDFORNEC',
	cast(trim(BPORC_MB1) as float) as 'VND_PC_MD',
	cast(trim(BMB2) as float) as 'VND_VL_MARGEMBRUTA',
	cast(trim(BPORC_MB2) as float) as 'VND_PC_MARGEMBRUTA',
	cast(trim(BSUG) as float) as 'VND_VL_SUGESTAO',
	BSUG_CPG as 'VND_NU_SUGESTAOPAGAMENTO', 
	cast(trim(BSUG_JRS) as float) as 'VND_VL_SUGESTAOJUROS',
	cast(trim(BFOR_MERC) as float) as 'VND_VL_OCMERC',
	cast(trim(BFOR_FT) as float) as 'VND_VL_OCFRETE',
	cast(trim(BFOR_IPI) as float) as 'VND_VL_OCIPI',
	cast(trim(BFOR_ICM) as float) as 'VND_VL_OCICM',
	cast(trim(BCOMISR) as float) as 'VND_VL_COMISSAORETORNO',
	cast(trim(BRETER) as float) as 'VND_VL_RETER',
	cast(trim(BRED_BC) as float) as 'VND_PC_REDUCAOBASECALCULO',
	cast(trim(BFTEMBUT) as float) as 'VND_VL_FRETEEMBUTIDO',
	cast(trim(BPIS) as float) as 'VND_VL_PIS',
	cast(trim(BCONFINS) as float) as 'VND_VL_CONFINS',
	cast(trim(BICM) as float) as 'VND_VL_ICM',
	BCERT as 'VND_CO_CERTIFICADO', 
	cast(trim(BJUREST) as float) as 'VND_VL_JUROSESTOQUE',
	NULL as 'RUA_SK_RUA',
	CODORIG as 'VND_CO_CODIGOORIGEM',
	cast(trim(ANO) as float) as 'VND_NU_ANO',
	cast(trim(MES) as float) as 'VND_NU_MES',
	BCOD_SERV  as 'VND_CO_SERVICO',
	COALESCE(DIMPRODUTOCJ.PRD_SK_PRODUTO, -1) as 'PRD_SK_PRODUTO_CJ',
	CJ as 'VND_ST_VENDACASADA',
	ISSERVICO  as 'VND_ST_SERVICO',
	UFEXPED as 'VND_CO_UFEXPEDICAO',
	NOMFILEXP  as 'VND_DS_FILIALEXPEDICAO',
	FAB as 'VND_DS_FABRICANTE',
	cast(trim(ROMANEIO) as bigint) as 'VND_CO_ROMANEIO',
	COALESCE(try_cast(convert(varchar(10), TRY_CONVERT(DATE, DTENTREG, 23), 112) as int), 19000101) as 'VND_DT_ENTREGA',
	NOMEMOTO as 'VND_DS_MOTORISTA',
	PLACA as 'VND_DS_PLACA',
	NOMETRAN as 'VND_DS_TRANSPORTADORA',
	TIPFROTA as 'VND_DS_TIPOFROTA',
	NOMFILVND  as 'VND_DS_FILIALVENDA',
	TABVND as 'VND_DS_LOJAVENDA',
	NULL as 'CAT_SK_CATEGORIA',
	cast(trim(CHORPED) as time) as 'VND_HR_HORAPEDIDO',
	COALESCE(try_cast(convert(varchar(10), TRY_CONVERT(DATE, DTSAIDA, 23), 112) as int), 19000101) as 'VND_DT_SAIDA',
	ORIVENDA as 'VND_CO_ORIGEMVENDA',
	cast(replace(convert(varchar(10), GETDATE(), 120), '-', '') as int) as 'VND_DT_PROCESSAMENTO',
	cast(trim(CRED_ICMST) as float) as 'VND_VL_SUBSTITUICAOTRIBUTARIA',
	cast(trim(CRED_ICMS) as float) as 'VND_VL_CREDITOICMS',
	cast(trim(PEDAPI) as int) as 'VND_ST_PEDIDOAPP'
FROM 
	STG.GAN_TMPVM tmpvm
left join 
	DIM.BFS_LOJA DIMLOJA
ON tmpvm.BTAB = DIMLOJA.TAB_CO_TABELA  
left join
	DIM.BFS_LINHA DIMLINHA
ON 	tmpvm.BLINHA = DIMLINHA.LIN_DS_BLINHA
left join
	DIM.BFS_VENDEDOR DIMVENDEDOR
ON	tmpvm.BVEND = DIMVENDEDOR.VEN_CO_CODIGO
left join
	DIM.BFS_CLIENTE DIMCLIENTE
ON  tmpvm.BCLI = DIMCLIENTE.CLI_CO_CODIGO
left join
	DIM.BFS_PRODUTO DIMPRODUTO
ON tmpvm.BCOD = DIMPRODUTO.PRD_CO_PRODUTO
left join
	DIM.BFS_PRODUTO DIMPRODUTOCJ
ON 	tmpvm.BCOD_CJ = DIMPRODUTOCJ.PRD_CO_PRODUTO

GO		

SELECT * FROM WRK.BFS_FAT_VENDAS



_______________________________________________________

-- VERIFICAR SE EXISTE INFORMAÇÕES DUPLICADAS NA TABELA --
SELECT CLI_CO_CODIGO, COUNT(1) AS TOTAL_REGISTROS 
FROM DIM.BFS_CLIENTE 
GROUP BY CLI_CO_CODIGO
HAVING COUNT(1) > 1

_______________________________________________________