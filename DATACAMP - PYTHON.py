DATACAMP 1

# Modelo de como mostrar grafico das informações abaixo.

import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, pop) # plt.scatter(year, pop)
plt.show()

import	matplotlib.pyplot as 

# CONTRUIR GRAFICO DE DISPERSÃO #
plt.scatter(pop, life_exp)

# MOATRAR O PLOT #
plt.show()

# IMPRIMIR ULTIMA DATA DAS VARIAVEIS YEAR E POP #
# Exemplo 1 #
year = [1950, 1970, 1990, 2010]
print(year[-1])

pop = [2.519, 3.692, 5.263, 6.972]
print(pop[-1])

# Exemplo 2 #
year = [1950, 1970, 1990, 2010]
indice = len(year) - 1   # print(year[-1])
print(indice)
ultimo = year[indice]
print(ultimo)

pop = [2.519, 3.692, 5.263, 6.972]
indice = len(pop) - 1
print(indice)
ultimo = pop[indice]
print(ultimo)

( Resolvido )
# IMPRIMIR ULTIMA DATA DAS VARIAVEIS YEAR E POP #
print(year[-1])
print(pop[-1])

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Faça um gráfico de linhas: ano no eixo x, pop no eixo y
plt.plot(year, pop)

# Exiba o gráfico com plt.show()
plt.show()


# 2 Exercicio #

# IMPRIMIR ULTIMO DATA DAS VARIAVEIS gdp_cap E gdp_cap #
print(gdp_cap[-1])
print(life_exp[[-1])

# Faça um gráfico de linhas: gdp_cap no eixo x, life_exp no eixo y #
plt.plot(gdp_cap, life_exp)

# Exiba o gráfico com plt.show()
plt.show()


# 3 Exercicio #

# ALTERAR GRAFICO DE LINHA ABAIXO PARA UM GRAFICO DE DISPERSÃO #
plt.scatter(gdp_cap, life_exp)

# COLOQUE O EIXO  X EM UMA ESCALA  LOGARITMICA #
plt.xscale('log')

# MOSTRAR O PLOT
plt.show()



# 3 EXERCICIO #

# IMPORTAR PACOTE #
import	matplotlib.pyplot as 

# CONSTRUIR GRAFICO DE DISPERSÃO #
plt.scatter(pop, life_exp)

# MOATRAR O PLOT #
plt.show()


# HISTOGRAMA #
import	matplotlb.pyplot as plt	
help(plt.hist)





