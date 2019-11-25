
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


### PROCEDURES TABELAS HISTORICAS ###

CREATE PROCEDURE sp_ins_hist_tmpmat
AS
	INSERT INTO WRK.GAN_TMPMAT_HIST
	SELECT
	 cast(MFAB as nvarchar(2)) as 'MFAB',
     cast(MCOD as nvarchar(12)) as 'MCOD',
     cast(MDESC as nvarchar(30)) as 'MDESC',
     cast(MUNV as nvarchar(2)) as 'MUNV',
     cast(MUNC as nvarchar(2)) as 'MUNC',
     cast(MUNCONV as float) as 'MUNCONV',
     cast(MRUAOP1 as nvarchar(1)) as 'MRUAOP1',
     cast(MBOXOP1 as nvarchar(2)) as 'MBOXOP1',
     cast(MRUAOP2 as nvarchar(1)) as 'MRUAOP2',
     cast(MBOXOP2 as nvarchar(2)) as 'MBOXOP2',
     cast(MPESO as float) as 'MPESO',
     cast(MC3 as float) as 'MC3',
     cast(MORIG as nvarchar(1)) as 'MORIG',
     cast(MTIP as nvarchar(1)) as 'MTIP',
     cast(MREDICM as float) as 'MREDICM',
     cast(MICM as float) as 'MICM',
     cast(MIPI as float) as 'MIPI',
     cast(MEMBL_COMP as float) as 'MEMBL_COMP',
     cast(MLEADTIME as float) as 'MLEADTIME',
     cast(MLINHA as nvarchar(2)) as 'MLINHA',
     cast(MDIR_AUX as nvarchar(1)) as 'MDIR_AUX',
     cast(MRT_ANT as float) as 'MRT_ANT',
     cast(MRT_ATU as float) as 'MRT_ATU',
     cast(MUPCOMP as float) as 'MUPCOMP',
     cast(MVPCOMP as float) as 'MVPCOMP',
     cast(MVPREP as float) as 'MVPREP',
     cast(MDTUCP as smalldatetime) as 'MDTUCP',
     cast(MDTUVEN as smalldatetime) as 'MDTUVEN',
     cast(MCLAS as nvarchar(1)) as 'MCLAS',
     cast(MCOMPR as nvarchar(7)) as 'MCOMPR',
     cast(MUSER as nvarchar(10)) as 'MUSER',
     cast(MPOSFIS as nvarchar(10)) as 'MPOSFIS',
     cast(MPROD as nvarchar(2)) as 'MPROD',
     cast(MREPS as float) as 'MREPS',
     cast(MTABFOR as float) as 'MTABFOR',
     cast(MALT as float) as 'MALT',
     cast(MLARG as float) as 'MLARG',
     cast(MPROF as float) as 'MPROF',
     cast(MMAL_ICM as float) as 'MMAL_ICM',
     cast(MPORT_MIN as nvarchar(10)) as 'MPORT_MIN',
     cast(MNEWCOD as nvarchar(14)) as 'MNEWCOD',
     cast(MEST_MIN as float) as 'MEST_MIN',
     cast(MEST_MAX as float) as 'MEST_MAX',
     cast(MTF_DAY as float) as 'MTF_DAY',
     cast(MTF_TX as float) as 'MTF_TX',
     cast(MTF_ANT as float) as 'MTF_ANT',
     cast(MCARACT as nvarchar(10)) as 'MCARACT',
     cast(VINC_COD as nvarchar(14)) as 'VINC_COD',
     cast(VINC_QTE as float) as 'VINC_QTE',
     cast(VINC_USE as float) as 'VINC_USE',
     cast(MBLOQPE as bit) as 'MBLOQPE',
     cast(MBC_ICM as float) as 'MBC_ICM',
     cast(MPESOFT as float) as 'MPESOFT',
     cast(MPESOTMP as float) as 'MPESOTMP',
     cast(MFLIN as bit) as 'MFLIN',
     cast(MTPCLAS as nvarchar(4)) as 'MTPCLAS',
     cast(MSUG as float) as 'MSUG',
     cast(MBXEST as nvarchar(1)) as 'MBXEST',
     cast(M_OLD as bit) as 'M_OLD',
     cast(MCAT as nvarchar(4)) as 'MCAT',
     cast(MLARG2 as float) as 'MLARG2',
     cast(MALT2 as float) as 'MALT2',
     cast(MPROF2 as float) as 'MPROF2',
     cast(MPESO2 as float) as 'MPESO2',
     cast(MTIPCAP as nvarchar(1)) as 'MTIPCAP',
     cast(MDIASPACK as float) as 'MDIASPACK',
     cast(MVPREPRJ as float) as 'MVPREPRJ',
     cast(MVPREPPR as float) as 'MVPREPPR',
     cast(MVPREPBA as float) as 'MVPREPBA',
     cast(MVPREPMG as float) as 'MVPREPMG',
     cast(MGI as nvarchar(1)) as 'MGI',
     cast(MMESINISRV as float) as 'MMESINISRV',
     cast(BCOD as nvarchar(14)) as 'BCOD',
     cast(FORALINHA as bit) as 'FORALINHA',
     cast(CJ as nvarchar(1)) as 'CJ',
     cast(MPRDPRINC as nvarchar(1)) as 'MPRDPRINC',
	 cast(replace(convert(varchar(10), GETDATE(), 120), '-', '') as int) as 'DT_PROCESSAMENTO'
	FROM 
		STG.GAN_TMPMAT
GO



CREATE PROCEDURE sp_ins_hist_tmpmest_full
AS
	INSERT INTO WRK.GAN_TMPEST_FULL_HIST
	SELECT 
	 cast(EMP as float) as 'EMP',
	 cast(FILIAL as nvarchar(2)) as 'FILIAL',
	 cast(CODPRO as nvarchar(14)) as 'CODPRO',
	 cast(QTE as float) as 'QTE',
	 cast(RUA_I as float) as 'RUA_I',
	 cast(ENT_I as float) as 'ENT_I',
	 cast(SAI_I as float) as 'SAI_I',
	 cast(RUA_J as float) as 'RUA_J',
	 cast(ENT_J as float) as 'ENT_J',
	 cast(SAI_J as float) as 'SAI_J',
	 cast(RUA_K as float) as 'RUA_K',
	 cast(ENT_K as float) as 'ENT_K',
	 cast(SAI_K as float) as 'SAI_K',
	 cast(RUA_P as float) as 'RUA_P',
	 cast(ENT_P as float) as 'ENT_P',
	 cast(SAI_P as float) as 'SAI_P',
	 cast(RUA_Q as float) as 'RUA_Q',
	 cast(ENT_Q as float) as 'ENT_Q',
	 cast(SAI_Q as float) as 'SAI_Q',
	 cast(RUA_B as float) as 'RUA_B',
	 cast(ENT_B as float) as 'ENT_B',
	 cast(SAI_B as float) as 'SAI_B',
	 cast(RUA_T as float) as 'RUA_T',
	 cast(ENT_T as float) as 'ENT_T',
	 cast(SAI_T as float) as 'SAI_T',
	 cast(RUA_M as float) as 'RUA_M',
	 cast(ENT_M as float) as 'ENT_M',
	 cast(SAI_M as float) as 'SAI_M',
	 cast(RUA_D as float) as 'RUA_D',
	 cast(ENT_D as float) as 'ENT_D',
	 cast(SAI_D as float) as 'SAI_D',
	 cast(RUA_A as float) as 'RUA_A',
	 cast(ENT_A as float) as 'ENT_A',
	 cast(SAI_A as float) as 'SAI_A',
	 cast(FISICO as float) as 'FISICO',
	 cast(RESERVA as float) as 'RESERVA',
	 cast(JIT as bit) as 'JIT',
	 PREV_ETG,
	 cast(FORAMIX as bit) as 'FORAMIX',
	 cast(REGIONAL as float) as 'REGIONAL',
	 cast(REP as float) as 'REP',
	 cast(REPJUR as float) as 'REPJUR',
	 cast(QTEJUR as float) as 'QTEJUR',
	 cast(DIASPACK as nvarchar(2)) as 'DIASPACK',
	 cast(DTFLIN as date) as 'DTFLIN',
	 cast(replace(convert(varchar(10), GETDATE(), 120), '-', '') as int) as 'DT_PROCESSAMENTO'
	FROM
	 STG.GAN_TMPEST_FULL
GO


CREATE PROCEDURE sp_ins_hist_tmpvm
AS
	INSERT INTO WRK.GAN_TMPVM_HIST
	SELECT 
		cast(BEMP as float) as 'BEMP',
		cast(BFIL as nvarchar(2)) as 'BFIL',
		cast(BDT as smalldatetime) as 'BDT',
		cast(BTAB as nvarchar(2)) as 'BTAB',
		cast(BNF as float) as 'BNF',
		cast(BCOD as nvarchar(14)) as 'BCOD',
		cast(BPROD as nvarchar(4)) as 'BPROD',
		cast(BLINHA as nvarchar(2)) as 'BLINHA',
		cast(BVEND as nvarchar(7)) as 'BVEND',
		cast(BQTE as float) as 'BQTE',
		cast(BVRNF as float) as 'BVRNF',
		cast(BVRIMP as float) as 'BVRIMP',
		cast(BDFIN as float) as 'BDFIN',
		cast(BVLIQ as float) as 'BVLIQ',
		cast(BCREP as float) as 'BCREP',
		cast(BCOMIS as float) as 'BCOMIS',
		cast(BFRETE as float) as 'BFRETE',
		cast(BMG2 as float) as 'BMG2',
		cast(BPORC_MG2 as float) as 'BPORC_MG2',
		cast(BMG3 as float) as 'BMG3',
		cast(BPORC_MG3 as float) as 'BPORC_MG3',
		cast(BTX_DESC as float) as 'BTX_DESC',
		cast(BTX_AUTOR as nvarchar(10)) as 'BTX_AUTOR',
		cast(BPED as float) as 'BPED',
		cast(BCLI as nvarchar(7)) as 'BCLI',
		cast(BCPG as nvarchar(2)) as 'BCPG',
		cast(BLJP as float) as 'BLJP',
		cast(BLJA as float) as 'BLJA',
		cast(BGN as float) as 'BGN',
		cast(BADM as float) as 'BADM',
		cast(BCREPS as float) as 'BCREPS',
		cast(BMG as float) as 'BMG',
		cast(BPORC as float) as 'BPORC',
		cast(BCLASSE as nvarchar(4)) as 'BCLASSE',
		cast(BADD as float) as 'BADD',
		cast(BSERIE as nvarchar(2)) as 'BSERIE',
		cast(BREBATE as float) as 'BREBATE',
		cast(BCAT as nvarchar(4)) as 'BCAT',
		cast(BFOR_PED as float) as 'BFOR_PED',
		cast(BFOR_AV as float) as 'BFOR_AV',
		cast(BENC_CP as float) as 'BENC_CP',
		cast(BJUR as float) as 'BJUR',
		cast(BMB1 as float) as 'BMB1',
		cast(BPORC_MB1 as float) as 'BPORC_MB1',
		cast(BMB2 as float) as 'BMB2',
		cast(BPORC_MB2 as float) as 'BPORC_MB2',
		cast(BSUG as float) as 'BSUG',
		cast(BSUG_CPG as nvarchar(2)) as 'BSUG_CPG',
		cast(BSUG_JRS as float) as 'BSUG_JRS',
		cast(BFOR_MERC as float) as 'BFOR_MERC',
		cast(BFOR_FT as float) as 'BFOR_FT',
		cast(BFOR_IPI as float) as 'BFOR_IPI',
		cast(BFOR_ICM as float) as 'BFOR_ICM',
		cast(BCOMISR as float) as 'BCOMISR',
		cast(BRETER as float) as 'BRETER',
		cast(BRED_BC as float) as 'BRED_BC',
		cast(BFTEMBUT as float) as 'BFTEMBUT',
		cast(BCTLM as float) as 'BCTLM',
		cast(BPIS as float) as 'BPIS',
		cast(BCONFINS as float) as 'BCONFINS',
		cast(BICM as float) as 'BICM',
		cast(BBC as float) as 'BBC',
		cast(BCERT as nvarchar(10)) as 'BCERT',
		cast(BJUREST as float) as 'BJUREST',
		cast(BRUA as nvarchar(1)) as 'BRUA',
		cast(BDIFICM as float) as 'BDIFICM',
		cast(BEMMOVEL as float) as 'BEMMOVEL',
		cast(CODORIG as nvarchar(14)) as 'CODORIG',
		cast(KEYSERV as NVARCHAR(40)) as 'KEYSERV',
		cast(BPROM_CPG as nvarchar(2)) as 'BPROM_CPG',
		cast(BPROM_JRS as float) as 'BPROM_JRS',
		cast(BPROM_MRG as float) as 'BPROM_MRG',
		cast(BPROM_REND as float) as 'BPROM_REND',
		cast(BVENLIM as float) as 'BVENLIM',
		cast(BGERLIM as float) as 'BGERLIM',
		cast(BCREP_AVP as float) as 'BCREP_AVP',
		cast(BMB2_AVP as float) as 'BMB2_AVP',
		cast(BP_MB2_AVP as float) as 'BP_MB2_AVP',
		cast(BVRIMP_FRE as float) as 'BVRIMP_FRE',
		cast(BCODCOMISS as NVARCHAR(40)) as 'BCODCOMISS',
		cast(BALIQIPI as NVARCHAR(40)) as 'BALIQIPI',
		cast(P_VICMSUFR as numeric(14,2)) as 'P_VICMSUFR',
		cast(P_VICMSUFD as numeric(14,2)) as 'P_VICMSUFD',
		cast(P_VFCPUFDE as numeric(14,2)) as 'P_VFCPUFDE',
		cast(CRED_ICMST as numeric(14,2)) as 'CRED_ICMST',
		cast(CRED_ICMS as numeric(14,2)) as 'CRED_ICMS',
		cast(CREP_ORI as numeric(14,2)) as 'CREP_ORI',
		cast(CREPAVPORI as numeric(14,2)) as 'CREPAVPORI',
		cast(CREPS_ORI as numeric(14,2)) as 'CREPS_ORI',
		cast(PEDAPI as bit) as 'PEDAPI',
		cast(ALCADA as char(1)) as 'ALCADA',
		cast(ANO as nvarchar(4)) as 'ANO',
		cast(MES as nvarchar(2)) as 'MES',
		cast(ESTOURO as float) as 'ESTOURO',
		cast(REBVPC as float) as 'REBVPC',
		cast(REBPRICE as float) as 'REBPRICE',
		cast(BCOD_SERV as nvarchar(14)) as 'BCOD_SERV',
		cast(BCOD_CJ as nvarchar(14)) as 'BCOD_CJ',
		cast(CJ as nvarchar(1)) as 'CJ',
		cast(ISSERVICO as bit) as 'ISSERVICO',
		cast(UFEXPED as nvarchar(5)) as 'UFEXPED',
		cast(NOMFILEXP as nvarchar(30)) as 'NOMFILEXP',
		cast(FAB as nvarchar(10)) as 'FAB',
		cast(ROMANEIO as numeric(18,0)) as 'ROMANEIO',
		cast(DTENTREG as datetime) as 'DTENTREG',
		cast(NOMEMOTO as nvarchar(40)) as 'NOMEMOTO',
		cast(PLACA as nvarchar(15)) as 'PLACA',
		cast(NOMETRAN as nvarchar(40)) as 'NOMETRAN',
		cast(TIPFROTA as nvarchar(30)) as 'TIPFROTA',
		cast(NOMFILVND as nvarchar(40)) as 'NOMFILVND',
		cast(TABVND as nvarchar(40)) as 'TABVND',
		cast(CATPROD as nvarchar(20)) as 'CATPROD',
		cast(VLRBONUS as numeric(14,2)) as 'VLRBONUS',
		cast(CHORPED as nvarchar(8)) as 'CHORPED',
		cast(DTSAIDA as datetime) as 'DTSAIDA',
		cast(ORIVENDA as nvarchar(10)) as 'ORIVENDA',
		cast(BPEDM1 as nvarchar(15)) as 'BPEDM1',
		cast(BPAICS as nvarchar(15)) as 'BPAICS',
		cast(BTIPODOC as nvarchar(15)) as 'BTIPODOC',
		cast(BVREMOTA as nvarchar(15)) as 'BVREMOTA',
		cast(CHAVESAP as nvarchar(15)) as 'CHAVESAP',
		cast(replace(convert(varchar(10), GETDATE(), 120), '-', '') as int) as 'DT_PROCESSAMENTO'
	FROM 
		STG.GAN_TMPVM
GO



