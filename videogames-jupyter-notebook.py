
# coding: utf-8

# <h1>Venda de jogos de videogame na História</h1>
# <br>
# Esta apresentação foi criada por <b>Paulo Henrique Vasconcellos</b>. Aqui eu irei realizar algumas análises sobre os dados encontrados <a href='https://www.kaggle.com/gregorut/videogamesales'>neste dataset</a>.

# In[1]:


get_ipython().magic('matplotlib inline')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')


# In[2]:


#Leitura do arquivo
videogames = pd.read_csv('vgsales.csv')


# In[3]:


#Exibindo as 10 primeiras linhas do Dataframe
videogames.head(10)


# In[4]:


#Resumo de informações em todas as colunas
videogames.describe()


# In[5]:


#Tipo de dado em cada coluna
videogames.dtypes


# In[6]:


#Quantidade de linhas e colunas no Dataframe
videogames.shape


# In[7]:


#Renomeando colunas
videogames.columns = ['Ranking', 'Nome', 'Plataforma', 'Ano', 'Gênero',
                      'Editora','Vendas América do Norte','Vendas EUA',
                      'Vendas Japão', 'Outras vendas', 'Vendas Global']


# In[8]:


#Exibindo as 10 primeiras linhas do arquivo
videogames.head(10)


# In[9]:


#Verificando linhas onde não há ano de lançamento definido
videogames[videogames['Ano'].isnull()].head()


# In[10]:


#Contagem de jogos lançados por plataforma
videogames['Plataforma'].value_counts()


# In[11]:


#Os dois pedaços de código abaixo fazem a mesma coisa
videogames['Plataforma'].value_counts().plot()

titulos_lancados = videogames['Plataforma'].value_counts()
titulos_lancados.plot()


# In[12]:


#Criando um gráfico utilizando apenas uma linha de código
videogames['Plataforma'].value_counts().head(10).plot(kind='bar', figsize=(11,5), grid=False, rot=0, color='green')

#Enfeitando o gráfico. Abaixo, definimos um título
plt.title('Os 10 videogames com mais títulos lançados')
plt.xlabel('Videogame') #eixo x
plt.ylabel('Quantidade de jogos lançados') #eixo y
plt.show()


# In[13]:


#Os 10 jogos mais vendidos da história
top_10_vendidos = videogames[['Nome','Vendas Global']].head(10).set_index('Nome').sort_values('Vendas Global', ascending=True)
top_10_vendidos.plot(kind='barh',figsize=(11,7), grid=False, color='darkred', legend=False)

plt.title('Os 10 jogos mais vendidos no mundo')
plt.xlabel('Total de vendas (em milhões de dólares)')
plt.show()


# In[14]:


#Mapa de calor
crosstab_vg = pd.crosstab(videogames['Plataforma'], videogames['Gênero'])
crosstab_vg.head()


# In[15]:


#Adicionar coluna total
crosstab_vg['Total'] = crosstab_vg.sum(axis=1)
crosstab_vg.head()


# In[19]:


top10_platforms = crosstab_vg[crosstab_vg['Total'] > 1000].sort_values('Total', ascending = False)
top10_final = top10_platforms.append(pd.DataFrame(top10_platforms.sum(), columns=['total']).T, ignore_index=False)

sns.set(font_scale=1)
plt.figure(figsize=(18, 9))
sns.heatmap(top10_final, annot=True, vmax=top10_final.loc[:'PS', :'Strategy'].values.max(), vmin=top10_final.loc[:, :'Strategy'].values.min(), fmt='d')
plt.xlabel('GÊNERO')
plt.ylabel('CONSOLE')
plt.title('QUANTIDADE DE TÍTULOS POR GÊNERO E CONSOLE')
plt.show()

