#!/usr/bin/env python
# coding: utf-8

# 1. Import required libraries and read the dataset.
# 

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv('honeyproduction.csv')
df


# 2. Check the first few samples, shape, info of the data and try to familiarize yourself with different features.
# 

# In[2]:


# samples 
df.sample(5)


# In[3]:


# shape
df.shape


# In[4]:


# info
df.info()


# In[5]:


df.describe()


# 3. Display the percentage distribution of the data in each year using the pie chart.
# 

# In[6]:


# plot the pie chart
plt.pie(df.groupby('year').size(),autopct='%1.1f%%',labels=df.groupby('year').size().index)
plt.title('Distribution of years')
plt.axis('equal')
plt.show()



# 4. Plot and Understand the distribution of the variable "price per lb" using displot, and write your findings.
# 

# In[7]:


sns.displot(df['priceperlb'],bins=20, kde=True, rug=True)  # Create the distribution plot

plt.title('Distribution of Price per lb')
plt.xlabel('Price per lb')
plt.ylabel('Density')
plt.show()


# Honey having priceperlb aorund 1.5 has highest number of sales


# 5. Plot and understand the relationship between the variables 'numcol' and 'prodval' through scatterplot, and
# write your findings

# In[8]:


plt.figure(figsize=(7,4))
sns.scatterplot(df,x = 'numcol', y = 'prodvalue' )
plt.title('Scatter Plot of numcol vs prodvalue')
plt.xlabel('numcol')
plt.ylabel('prodvalue')
plt.grid(True)
plt.show()

#honey producing colonies around 500000 have maximum numbers of prodvalue and 
#colonies around 100000 capacity have most number of units but has least or minimum value of production


# 6. Plot and understand the relationship between categorical variable 'year' and a numerical variable
# 'prodvalue' through boxplot, and write your findings

# In[9]:


plt.figure(figsize=(10,6))
sns.boxplot(df, x = 'year', y = 'prodvalue')
plt.title('Boxplot between year and prodvalue')
plt.xlabel('year')
plt.ylabel('prodvalue')
plt.grid()
plt.show()

# mostly production in all the years are consistent but there are some years 
# where production is exceeded (we can observe from outliers) such as 2010,2011 and 2012


# 7. Visualize and understand the relationship between the multiple pairs of variables throughout different years
# using pairplot and add your inferences. (use columns 'numcol', 'yield percol', 'total prod', 'prodvalue','year')
# 

# In[10]:


plt.figure(figsize=(10,5))
sns.pairplot(df[['numcol', 'yieldpercol', 'totalprod', 'prodvalue','year']],hue='year')
plt.suptitle('Pairplot of variables by year', y=1.02)
plt.show()

# prodvalue increases as total production inscreases
# totalprod increases with the increase in number of colonies


# 8. Display the correlation values using a plot and add your inferences. (use columns 'numcol', 'yield percol',
# 'total prod', 'stocks', 'price per lb', 'prodvalue')
# 

# In[11]:


plt.figure(figsize=(10, 8))
sns.heatmap(df[['numcol', 'yieldpercol', 'totalprod', 'prodvalue','stocks','priceperlb',]].corr(),cmap='viridis',annot=True)
plt.title('Correlation Heatmap')
plt.show()

#totalprod and numcol has highest correlation implies higheer te numcols higher the totalprod
#yieldpercol decreases with the increase in priceperlb


# In[ ]:




