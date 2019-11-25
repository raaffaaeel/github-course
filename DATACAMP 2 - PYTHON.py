DATACAMP 2

>>>>>> 3 EXERCICIO <<<<<<

# IMPORTAR PACOTE #
import	matplotlib.pyplot as 

# CONSTRUIR GRAFICO DE DISPERSÃO #
plt.scatter(pop, life_exp)

# MOATRAR O PLOT #
plt.show()


>>>>>> 4 EXERCICIO <<<<<<

import	matplotlb.pyplot as plt	
help(plt.hist)

values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values, bins = 20)
plt.show()


# 4 EXERCICIO # 

# Create histogram of life_exp data
plt.hist(life_exp)

# Display histogram
plt.show()



>>>>>> 5 EXERCICIO <<<<<<

# CONSTRUIR HISTOGRAMA COM 5 POSIÇÕES #
plt.hist(life_exp, bins = 5)

# MOSTRAR E LIMPAR PLOTAGEM #
plt.show()
plt.clf()

# CONSTRUIR HISTOGRAMA COM 20 POSIÇÕES #
plt.hist(life_exp, bins = 20)


# MOSTRE E LIMPE NOVAMENTE #
plt.show()
plt.clf()


>>>>>> 6 EXERCICIO <<<<<<

# Histograma de life_exp, 15 posições #
plt.hist(life_exp, bins = 15)

# MOSTRAR E TRAÇAR CLARA
plt.show()
plt.clf()

# Histograma de life_exp1950, 15 posições
plt.hist(life_exp1950, bins = 15)

# MOSTRAR E LIMPAR A PLOTAGEM NOVAMENTE
plt.show()
plt.clf() 


%%%%%% >>>>>> Custumização <<<<<< %%%%%%%

import matplotlib.pyplot as plt
year = [1950, 1951, 1952, ..., 2100]
pop = [2.538, 2.57, 2.62, ...,10.85]

#ADD MORE DATA #
year = [1800, 1850, 1900] + year
pop = [1.0, 1.262, 1.650] + POP

plt.plot(year, pop)

plot.show()

# INSERINDO NOME NO GRAFICO #
plt.xlabel('year')
plt.ylabel('population')
plt.title('Word population Projections')
plt.yticks([0,2,4,6,8,10]),
           ['0','2B','4B','6B','8B','10B'])


plot.show()


plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

>>>>>> 7 EXERCICIO <<<<<<

# GRAFICO DE DISPERSÃO BASICO, ESCALA DE LOG #
plt.scatter(gdp_cap, life_exp)
plt.xscale('log') 

# Strings CORDAS
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# ADICIONAR ROTULOS DE EIXO
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')


# AICIONAR TITULO 
plt.title('World Development in 2007')

# APOS A PERSONALIZAÇÃO, EXIBIR GRAFICO
plt.show()


>>>>>> 8 EXERCICIO <<<<<<

# GRAFICO DE DISPERSÃO
plt.scatter(gdp_cap, life_exp)

# PERSONALIZAÇÃO ANTERIOR 
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# DEFINIÇÃO of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)

# APÓS A PERSONALIZAÇÃO EXIBIR GRAFICO
plt.show()


>>>>>> 9 EXERCICIO <<<<<<

# Import numpy as np
import numpy as np

# Amarzenar pop como uma matrix numpy  np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop * 2

# Update: definir argumentos np_pop
plt.scatter(gdp_cap, life_exp, s = pop)

# Personalização
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Mostrar grafico
plt.show()


>>>>>> 10 EXERCICIO <<<<<<

# Specify c and alpha inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show()


>>>>>> 11 EXERCICIO <<<<<<