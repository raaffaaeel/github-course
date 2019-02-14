COMANDOS MYSQL

SELECT * FROW dw.Customers;   - SELEÇÃO DE ALGO

SELECT * FROM celebs;         - 

SELECT name FROM celebs;      - Especifica a coluna para consultar dados

INTEGER                       - Um número inteiro 
positivo ou negativo

TEXT                          - Uma string de texto

DATE                          - Data formatada como 
AAAA-MM-DD para o ano, mês e dia
REAL, um valor decimal 
CREATE TABLE                  - Cláusulas executam tarefas específicas no SQL.
table_name                    - refere-se ao nome da tabela à qual o comando é aplicado.
(id INTEGER, name TEXT, age INTEGER) - É uma lista de parâmetros que definem cada coluna ou atributo na tabela e seu tipo de dados:

ALTER TABLE - Adiciona uma nova coluna a uma tabela
ALTER TABLE  - é uma cláusula que permite fazer as alterações especificadas. 
2. celebs    - é o nome da tabela que está sendo alterada. 
3. ADD COLUMN - é uma cláusula que permite adicionar uma nova coluna a uma tabela:
twitter_handle - é o nome da nova coluna sendo adicionada
TEXT  - é o tipo de dados para a nova coluna

INSERIR UMA NOVA COLUNA NA TABELA
ALTER TABLE celebs 
ADD COLUMN nome da nova coluna + tipos de dados da coluna 
SELECT * FROM celebs; 

INSTRUÇÕES
UPDATE  - instrução edita uma linha em uma tabela
celebs  - é o nome da tabela. 
SET     - é uma cláusula que indica a coluna 

INSERIR UM DADO EM UMA COLUNA
UPDATE celebs 
SET twitter_handle = '@taylorswift13' 
WHERE id = 4; 
SELECT * FROM celebs;

INSTRUÇÕES
DELETE FROM - é uma cláusula que permite excluir linhas de uma tabela.
celebs - é o nome da tabela da qual queremos excluir linhas.
WHERE - é uma cláusula que permite selecionar quais linhas você deseja excluir. Aqui queremos excluir todas as linhas onde a coluna twitter_handle IS NULL.
IS NULL - é uma condição no SQL que retorna true quando o valor é NULLe false no caso contrário.

DELETAR TODAS AS LINHAS NÃO PREENCHIDAS COM O TWITTER
DELETE FROM celebs 
WHERE twitter_handle IS NULL;
SELECT * FROM celebs;

INSTRUÇÕES
PRIMARY KEY - colunas podem ser usadas para identificar exclusivamente a linha. Tentativas de inserir uma linha com um valor idêntico a uma linha já na tabela resultará em uma violação de restrição que não permitirá inserir a nova linha.

2. UNIQUE  - colunas têm um valor diferente para cada linha. Isso é semelhante a, PRIMARY KEYexceto que uma tabela pode ter várias UNIQUEcolunas diferentes .

3. NOT NULL - colunas devem ter um valor. As tentativas de inserir uma linha sem um valor para uma NOT NULLcoluna resultarão em uma violação de restrição e a nova linha não será inserida.

4. DEFAULT - colunas tomam um argumento adicional que será o valor assumido para uma linha inserida se a nova linha não especificar um valor para essa coluna.

CRIAR NOVA TABELA
CREATE TABLE awards (
   id INTEGER PRIMARY KEY,
   recipient TEXT NOT NULL,
   award_name TEXT DEFAULT 'Grammy'); 
SELECT * FROM celebs;

SELECT * FROM movies  - Criar Tabela de filmes
SELECT name, genre  - Criar colunas com 2 informações
FROM movies;


INSTRUÇÕES

SELECT  - É usado toda vez que você deseja consultar dados de um banco de dados
WHERE   - Cláusula para obter apenas as informações que desejamos.

SELECT name, genre, year - Criar colunas com 3 informações
FROM movies;

SELECT name AS 'Alias'  - Alterar um nome de uma pasta por um novo nome
FROM movies;

OBTER APENAS INFORMAÇÃO QUE NECESSITAMOS
SELECT *
FROM movies
WHERE imdb_rating > 8;

INSTRUÇÕES
WHEREA   - Cláusula filtra o conjunto de resultados para incluir apenas as linhas nas quais a condição a seguir é verdadeira.
imdb_rating > 8 - é a condição. Aqui, apenas as linhas com um valor maior que 8 na imdb_ratingcoluna serão retornadas.

= igual a
!= não é igual a
> Melhor que
< menos que
>= Melhor que ou igual a
<= menos que ou igual a

Suponha que queremos dar uma olhada em todos os filmes não tão bem recebidos no banco de dados.
SELECT *
FROM movies
WHERE year > 2014;

LIKE  - Pode ser um operador útil quando você deseja comparar valores semelhantes.

name LIKE 'Se_en'  - É uma condição que avalia a namecoluna para um padrão específico.
Se_en  - Representa um padrão com um caractere curinga .
%  - O sinal de porcentagem é outro caractere curinga que pode ser usado com LIKE


Esta declaração abaixo filtra o conjunto de resultados para incluir apenas filmes com nomes que começam com a letra 'A':
SELECT * 
FROM movies
WHERE name LIKE 'A%';

A% corresponde a todos os filmes com nomes que começam com a letra 'A'
%a corresponde a todos os filmes que terminam com "a"

BETWEEN operador pode ser usado em uma WHEREcláusula para filtrar o conjunto de resultados dentro de um determinado intervalo.

Nesta declaração, o BETWEENoperador está sendo usado para filtrar o conjunto de resultados para incluir apenas filmes com years entre 1990 e 1999.
SELECT *
FROM movies
WHERE year BETWEEN 1990 AND 1999;


Essa declaração filtra o conjunto de resultados para incluir apenas filmes com names que começam com as letras 'A' até, mas sem incluir 'J'.
SELECT *
FROM movies
WHERE name BETWEEN 'A' AND 'J';

Usando o BETWEEN operador, escreva uma nova consulta que selecione todas as informações sobre os filmes que foram lançados na década de 1970.
SELECT *
FROM movies
WHERE year BETWEEN 1970 AND 1979;

Usando AND, escreva uma nova consulta que selecione todos os filmes feitos antes de 1985 que também estão no horror gênero.
SELECT *
FROM movies
WHERE year < 1985
AND genre = 'horror';


INSTRUÇÕES
Com OR, se alguma das condições for verdadeira, a linha será adicionada ao resultado.
SELECT *
FROM movies
WHERE year > 2014
OR genre = 'action';

Usando OR, escreva uma consulta que retorne todos os filmes que são um romance ou uma comédia.
SELECT *
FROM movies
WHERE genre = 'romance'
OU gênero = 'comédia';

Suponha que queremos recuperar as colunas namee yeartodos os filmes, ordenados pelo nome em ordem alfabética.
SELECT name, year
FROM movies
ORDER BY name;

Escreva uma nova consulta que recupera os name, yeare imdb_ratingcolunas de todos os filmes, ordenada maior para o menor por seus ratings.
SELECT nome, year, imdb_rating
FROM movies
ORDER BY imdb_rating DESC;

INSTRUÇÕES
LIMIT  - É uma cláusula que permite especificar o número máximo de linhas que o conjunto de resultados terá.

LIMITe ORDER BY, escreva uma consulta que retorne os 3 principais filmes com classificação mais alta.
SELECT *
FROM movies
ORDER BY imdb_rating DESC
LIMITE 3 ;


Selecione a name coluna e use uma CASE instrução para criar a segunda coluna que é:

'Chill' se genre = 'romance'
'Chill' se genre = 'comedy'
'Intenso' em todos os outros casos.

SELECT name ,
CASE
WHEN genre = 'romance' THEN 'Chill'
WHEN genre = 'comedy'  THEN 'Chill'
ELSE 'Intense'
END AS 'Mood'
FROM movies;

AULA 3 CODECADEMY

Aqui está uma prévia rápida de alguns agregados importantes que abordaremos nos próximos cinco exercícios:
COUNT(): conta o número de linhas
SUM(): a soma dos valores em uma coluna
MAX()/ MIN(): o maior / menor valor
AVG(): a média dos valores em uma coluna
ROUND(): arredondar os valores na coluna

Vamos contar quantos aplicativos estão na tabela.
SELECT COUNT(*) 
FROM fake_apps;

Qual é o número total de downloads para todos os aplicativos combinados?
SELECT SUM(downloads)
FROM fake_apps;

INSTRUÇÕES
MAX() - Pega o nome de uma coluna como argumento e retorna o maior valor nessa coluna. Aqui, retornamos o maior valor na downloadscoluna.

MIN() - FUnciona da mesma maneira, mas faz exatamente o oposto; ele retorna o menor valor.

Escreva uma nova consulta que calcule o preço médio de todos os aplicativos na tabela.
SELECT AVG (downloads)
FROM fake_apps;

No último exercício, conseguimos obter o preço médio de um aplicativo (US $ 2,02365) usando essa consulta:
SELECT ROUND (avg(prince), 2)
FROM fake_apps;


Na consulta anterior, adicione uma WHEREcláusula para contar o número total de aplicativos que foram baixados mais de 20.000 vezes, a cada preço.
SELECT category,
SUM(downloads)
FROM fake_apps
GROUP BY category;


Por exemplo, podemos querer saber quantos filmes têm classificações da IMDb que arredondam para 1, 2, 3, 4, 5. Poderíamos fazer isso usando a seguinte sintaxe:
SELECT ROUND(imdb_rating),
COUNT(name)
FROM movies
GROUP BY ROUND(imdb_rating)
ORDER BY ROUND(imdb_rating);

Escreva a consulta exata, mas use números de referência de coluna em vez de nomes de coluna depois GROUP BY.
SELECT category, 
   price,
   AVG(downloads)
FROM fake_apps
GROUP BY 1, 2;

Adicione uma HAVINGcláusula para restringir a consulta a pontos de preço que tenham mais de 10 aplicativos.
SELECT price, 
   ROUND(AVG(downloads)),
   COUNT(*)
FROM fake_apps
GROUP BY price
HAVING COUNT(*) > 10;

Você acabou de aprender como usar funções agregadas para executar cálculos em seus dados. O que podemos generalizar até agora?

COUNT(): conta o número de linhas
SUM(): a soma dos valores em uma coluna
MAX()/ MIN(): o maior / menor valor
AVG(): a média dos valores em uma coluna
ROUND(): arredondar os valores na coluna
As funções agregadas combinam várias linhas para formar um valor único de informações mais significativas.

GROUP BY é uma cláusula usada com funções agregadas para combinar dados de uma ou mais colunas.
HAVING limitar os resultados de uma consulta com base em uma propriedade agregada.

AULA 4 CODECADEMY

orders  - Conteria apenas as informações necessárias para descrever o que foi ordenado.

subscriptions - Conteria as informações para descrever cada tipo de assinatura.

customers - Conteria as informações para cada cliente.

Usando as tabelas exibidas, qual é a descriptionda revista encomendada em order_id1?
Digite sua resposta na linha 1 do editor de código.
SELECT *
FROM orders
JOIN customers
ON orders.customer_id =
customers.customer_id;

Junte a orderstabela e a subscriptionstabela e selecione todas as colunas.
Certifique-se de participar na subscription_id coluna.
SELECT *
FROM orders
JOIN subscriptions
ON orders.subscription_id = subscriptions.subscription_id;

Não remova a consulta anterior.
Adicione uma segunda consulta após a primeira, selecionando apenas as linhas da junção onde description é igual a 'Fashion Magazine'
SELECT *
FROM orders
JOIN subscriptions
	ON orders.subscription_id=
	subscriptions.subscription_id
WHERE subscriptions.description = 'Fashion Magazine';

Existe uma newspapertabela que contém informações sobre os assinantes do jornal.
Conte o número de assinantes que usam um jornal impresso COUNT().

SELECT COUNT(*)
FROM newspaper;

SELECT COUNT(*)
FROM online;

SELECT COUNT(*)
FROM newspaper
JOIN online
	ON newspaper.id = online.id;

	Vamos voltar para os nossos newspaper e online assinantes.

Suponha que queremos saber quantos usuários assinam o jornal impresso, mas não o on-line.

Comece executando uma junção esquerda de newspaper tabela e online tabela em suas id colunas e selecionando todas as colunas.
SELECT *
FROM newspaper
LEFT JOIN online
	ON newspaper.id = online.id;
  
-- Second query
SELECT *
FROM newspaper
LEFT JOIN online
	ON newspaper.id = online.id
WHERE online.id IS NULL;