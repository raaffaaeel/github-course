PARTE 1 >>>
RESUMO DESTE PROJETO, FOI ENVIADO OS NOMES DAS TABELAS E COLUNAS PARA SER INSERIDAS NO BANCO SQL SERVER, TODAS ESSAS TABELAS VAI SUBIR TODOS OS DIAS OS ARQUIVOS VIA BLOB STORAGE, NESTE CASO PARA CADA,
TABELA INSERIDA NO BANCO FOI CRIADO (JSON), ATRAVÉS DE PROGRAMAÇÃO EM PYTHON NO QUAL, INSERIMOS UM ARQUIVO .TXT COM OS NOMES DE CADA COLUNA SEPARADOR POR VIRGULA E SALVOS COM NOME DA TABELA.TXT
APÓS CRIAMOS UM PIPELINE NO DATA FACTORY PARA CARREGAR OS DADOS INSERIDOS NO BLOB E CARREGAR AS TABELAS (STG) CRIADAS NO BANCO COM TODAS AS COLUNAS VARCHAR DE 4000. 

OBS >>> ESTES PASSOS ACIMA SÃO PARA POPULAR A STAGE DO BANCO COM OS DADOS.

PARTE 2 >>>
CRIAR TABELAS WRK PARA CADA TABELA STG, FAZENDO O CONVERTE DOS TYPOS VARCHAR 4000, PARA O MODELO CORRETO DE CADA COLUNA.


PARTE 3 >>> 
CRIAR VIEW DAS TABELAS QUE VAI SER INSERIDAS DENTRO DO (CUBO DO ANALYSIS SERVICES) 


PARTE 4 >>> 
CRIAÇÃO DO LOGIC APP NA PLATAFORMA AZURE, PARA PROGRAMAR O CARREGAMENTO TODOS OS DIAS PARA CARREGAR OS NOVOS ARQUIVOS 


PARTE 5 >>>
MONTAR O ANALYSIS SERVICES (CUBO) PARA SUBIR AS TABELAS DO BANCO NO CASO VIEW, PARA INICIAR AS RELAÇÕES ENTRE FATO E DIMENSÃO.


PARTE 6 >>>






FAST SHOP >> inicio 04/11/2019

MIGRAÇÃO DE TABELAS DO (SAP) (EXCEL) (ARQUIVOS).

Contato > Leandro 
Contato > Rodrigo

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Blob Storage - TESTE 

8813add0-971e-44dc-817e-0a512257a763
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

SSID: GUEST
USUARIO: guestfast
SENHA:   fast@2020

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

POC 

@Cruze2014

Server name > testerafaelblob


Serve admin login > userlogin

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


Server name > testejessicablob

Serve admin login > userlogin

Senha > @Jessica2019

(US) East US

Database > testejessicablob

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

C:\Users\BlueShift\source\repos\BI_FAST_SHOP_CUBOS

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
asazure://westus.asazure.windows.net/fsbicontabilidadegerencial

asazure://eastus.asazure.windows.net/fscontabilidadegerencial

asazure://eastus.asazure.windows.net/fsbicorporativo


portal azure:
lfsouza@fastshop.com.br
microsoft@04


servidor SQL:
srv-fast.database.windows.net,1433
usr_lfsouza
s4(Tu?6^SLV>&xX


Blobs: 
fsarquivo2 --> container0

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Meu Usuario.

usuario: TRAFAELDAM
 
A senha de acesso é Fast@2019



LB341027947SE 

____________________________________________________________



testando 1 # USAMOS ESSA STRING PARA INSERIR O ARQUIVO COM ANO, MÊS, DIA. #
@concat('foo-name','/',formatDateTime(utcnow(),'yyyy/MM/dd'))
@concat ('raw/', activity('LeParametrosCarga').output.firstRow.tabela, '/',formatDateTime(utcnow(),'yyyy/MM/dd'))		

TESTE 2
folderPath" : " /'raw/' @ {formatDateTime (dias úteis (utcnow (), - 1), 'aaaa')} / @ {formatDateTime (dias úteis (utcnow (), - 1), 'MM')} / @ {formatDateTime ( adddays (utcnow (), - 1), 'dd')}

folderPath" : "/ @ {formatDateTime (dias úteis (utcnow (), - 1), 'aaaa')} / @ {formatDateTime (dias úteis (utcnow (), - 1), 'MM')} / @ {formatDateTime ( adddays (utcnow (), - 1), 'dd')}

@concat('raw/'{formatDateTime (dias úteis (utcnow (), - 1), 'aaaa')} / @ {formatDateTime (dias úteis (utcnow (), - 1), 'MM')} / @ {formatDateTime ( adddays (utcnow (), - 1), 'dd')})






CUBO MODELO VENDAS HORA HISTORICO

CUBO VENDAS HORA|ESTOQUE HISTORICO

2019-12-28T01:00:00Z


#UNIVESP #APONTAEVAI #DEUSNOCOMANDO

#univesp #apontaevai #deusnocomando




SELECT [dbo].[VW_FATO_VENDAS].* FROM [dbo].[VW_FATO_VENDAS]



select 
	f.*
from 
	VW_FATO_VENDAS as f
inner join 
	VW_DIM_CALENDARIO as cal
on f.[DATA DA VENDA (BDT)] = cal.[ID DATA]
where cal.[NUMERO ANO] = 2019




RATEIO PIVA PROJEÇÃO
TBL SERVIÇOS
MKTPLACE
TBL META DIARIZADA O2
PIVA
TBL FLUXO TOTAL SITE
FATO APPVENDEDOR


C:\Users\BlueShift\source\repos\BI_FAST_SHOP_CUBOS\BI_FAST_SHOP