EXERCICIOS_MYSQL

create database Contas;
drop database Contas;
create database Contas;

-- Criando tabela ContasPagar --
Create table ContasPagar(
CodPagar INT,
CodCliente INT,
DataVencimento DATE,
DataPagamento DATE,
ValorPagar FLOAT 
);

-- Criando tabela Produtos --
Create table Produtos(
CodProduto int,
Descriçao Varchar(45),
PrecoCusto float,
PrecoVenda float,
MargemLucro float,
Fornecedor Varchar(45),
DataUltimaCompra date,
Estoque Int,
EstoqueMinimo int
);

-- Criando tabela Caixa --
Create table Caixa(
CodLancamento int,
Descricao varchar(70),
DataLancamento date,
Valor float,
Observacao Varchar(200)
);

-- Criando tabela ContasReceber --
Create table ContasReceber(
CodReceber int,
CodCliente int,
DataVencimento date,
DataRecebimento date,
valorReceber float
);

-- Criando tabela Material --
Create table Material(
IdMaterial Int KEY,
NomeMaterial Varchar(30)
);


-- Criando tabela Categoria --
Create table Categoria(
IdCategoria Int KEY,
NomeCategoria Char(40)
);

-- Criando tabela Unidmedida --
Create table Unidmedida(
IdUnidMedida Int KEY, 
SiglaUnidMedida Char(2), 
DescUnidMedida Varchar(40)
);

## Renomeiar o nome da tabela para MEDIDA ##
RENAME TABLE unidmedida TO MEDIDA;

## Alterar o tamanho do campo NomeMaterial para Varchar(40)##
ALTER TABLE MATERIAL
MODIFY NomeMaterial varchar(40)

-- Altere o nome do campo NomeMaterial para MaterialNome;
ALTER TABLE MATERIAL
RENAME COLUMN NomeMaterial TO  MaterialNome;


-- Inserir os campos: IdCategoriaint e IdUnidMedidaInt -
ALTER TABLE MATERIAL
ADD idCategoria int,
ADD idUnidMedida int


-- Exclua a coluna MaterialNome --
ALTER TABLE MATERIAL DROP COLUMN MaterialNome


-- Adicionando coluna TipoCategoria, e excluindo coluna NomeCat --
ALTER TABLE categoria
ADD TipoCategoria int,
Drop column NomeCat

================================================================

-- Renomear coluna + Adicionar coluna + Excluir coluna TipoMed --
ALTER TABLE MEDIDA
RENAME COLUMN DescUnidMedida TO  NomeUnidMedida
ALTER TABLE MEDIDA
ADD TipoMed varchar(30)
ALTER TABLE MEDIDA DROP COLUMN TipoMed;


****************************************************************

-- Criando schema construção --
create database construcao;

-- Criando tabela setor --
create table SETOR(
IdSetor Int KEY,
NomeSetor Char(40)
);


-- Excluir Schema Cosntrução --
drop database construcao;

-- Criando schema --
create database empresa;

-- selecionando schema para criar a tabela --
use empresa;

create table funcionario(
nome varchar(40)
);


-- Adicionar colunas e valor para cada coluna --
ALTER TABLE funcionario
ADD Cracha VARCHAR(60),
ADD Salario numeric (10),
ADD TempoServico numeric(2),
ADD Idade  NUMERIC(2),
ADD DataNascimento date

-- Criando Schema --
create database Comercio

-- Criando tabela dados --
Create table dados(
Rg varchar(20),
Nome varchar (40),
Cidade Varchar (20),
Telefone numeric (15)
);




