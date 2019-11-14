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



Instruções:
As respostas devem ser suas queries, pois assim conseguiremos avaliar como você chegou aos resultados.
Não é necessário instalar o SQL e criar o banco e tabelas. Você deve utilizar o client sql online disponibilizado pela w3schools.
O nome de algumas funções pode mudar dependendo do gerenciador de banco (microsoft, oracle, postgree etc). Atenção a este ponto ao utilizar as funções.