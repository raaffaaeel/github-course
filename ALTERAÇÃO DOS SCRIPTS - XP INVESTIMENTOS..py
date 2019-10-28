
GIT SUBIR VM 

ssh bernardo.aflalo@10.96.22.5 -L 12002:localhost:12002  (APONTAR MAQ)

ls

cd projects

ls

cd + nome do arquivo/

git branch ( apontar diretorio )


====  ( Clonar Arquivo VM ) =====

git status 
git add .
git commit -m "Feat: Atualizando querys nome do arq"
git push
git push + msg
git status 
git clone





ALTERAÇÃO DOS SCRIPTS - XP INVESTIMENTOS.

====== ANTES ======

from xpy import xpy_db
athena = xpy_db.athena
conn = athena.get_conn(Nome,Nome)
query = "ababababab"
df = athena.make_simple_query(conn, query)


=======================================================


===== DEPOIS ======

from xpy import xpy_databricks
conn = xpy_databricks.get_conn()

query = """
asdsas
"""

df = xpy_databricks.make_query(conn, query)

 

 ======================================================

(EXEMPLO DE MARGE )

 final_chave= tab_clibol.merge(tab_tsx, left_on = 'COD_CLIENTE', right_on = 'cod_cliente', how='inner')

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


