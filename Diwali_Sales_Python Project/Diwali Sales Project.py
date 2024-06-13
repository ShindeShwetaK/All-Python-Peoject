#!/usr/bin/env python
# coding: utf-8

# In[5]:


# import python libraries
#!pip install is used to install the required libraries
#!pip install pandas
#!pip install numpy
#!pip install matplotlib 
import numpy as np  #Help to work with Arrays
import pandas as pd # to work on data frame i.e tables
import matplotlib.pyplot as plt # visualizing data and chart building
get_ipython().run_line_magic('matplotlib', 'inline')
##When you run this command at the beginning of your notebook,
##it configures Matplotlib to render the plots inline, meaning that the plots will appear directly below the code cell.
import seaborn as sns# visualizing data and chart building


# In[10]:


# import csv file
df = pd.read_csv(r'C:\Users\karti\Downloads\Diwali Sales Data.csv', encoding= 'unicode_escape')
#r is to read the special symbols in the given file path
#unicode_escape is used to avoid encoding error


# In[11]:


df.shape #df=dateframe
#(11251, 15)(rows,columns)


# In[12]:


df.head()
#by default with show 5 values


# In[13]:


df.head(15)
#to get given values


# In[14]:


df.info()
#gives all the info of the data inside the file here status and unnamed1 has 0 records init.


# In[16]:


df.drop(['Status','unnamed1'],axis=1,inplace=True)
#axis=1 means delete the whole status column below
#inplace=true means the commit the changes given in the commant


# In[17]:


df.info()
#status and unnamed1 deleted


# In[18]:


pd.isnull(df)
#false= not is null
#true=isnull


# In[19]:


pd.isnull(df).sum()
#here summ will give total null values in all given col here amount has 12 null values


# In[20]:


df.shape


# In[21]:


#to drop null values
df.dropna(inplace=True)


# In[23]:


df.shape


# In[24]:


pd.isnull(df).sum()
#df.dropna deleted the 12 null amount rows


# #Both are the same 
# 
# df_test.dropna(inplace=True)
# 
# 
# df_test=df_test.dropna
# 
# 
# But prefere inplace as assigning will create memory for variable

# In[25]:


#change the data type
df['Amount']=df['Amount'].astype('int')


# In[26]:


df['Amount'].dtypes


# In[27]:


df.columns


# In[29]:


#will rename col'Marital_Status':'Shadi' but here we have not use inplace or assigned to variable so will not save
df.rename(columns={'Marital_Status':'Shadi'})


# In[30]:


# describe() method returns description of the data in the DataFrame (i.e. count, mean, std, etc)
df.describe()


# In[33]:


# use describe() for specific columns
df[['Age', 'Orders', 'Amount']].describe()


# # Exploratory Data Analysis

# # Gender

# In[35]:


sns.countplot(x = 'Gender',data = df)


# In[34]:


# the code you provided creates a countplot of 'Gender' categories and adds count labels to each bar on the plot. 
ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[36]:


#as_index=False will give indexes to the df
df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)


# In[43]:


#as_index= will give not indexes to the df and use the 1st column as index
df.groupby(['Gender'], as_index=True)['Amount'].sum().sort_values(by='Amount', ascending=False)


# In[44]:


#as_index= will give not indexes to the df and use the 1st column as index
df.groupby(['Gender'], as_index=True)['Amount'].sum().sort_values


# In[45]:


# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)
#"1e7" stands for 1 multiplied by 10 raised to the power of 7, which equals 10,000,000.


# From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men

# # Age

# In[47]:


sns.countplot(data = df, x = 'Age Group')
#Will classify accouding to the sage group
# here we understand that 26-35 age groups has done max shopping 0-17 the least


# In[48]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[49]:


# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# From above graphs we can see that most of the buyers are of age group between 26-35 yrs female

# # State
# 

# In[59]:


# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(11)
#Head is count of bars

sns.set(rc={'figure.figsize':(17,5)}) #If not given then the state names overlap each other
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[62]:


sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(17,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')


# From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively. Where kerla has given more orders then Haryana, Gujrat,Bihar but the total amount paid is less the the 3 states.

# # Marital Status

# In[63]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[64]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# From above graphs we can see that most of the buyers are married (women) and they have high purchasing power

# # Occupation

# In[65]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[71]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector

# # Product Category

# In[74]:


sns.set(rc={'figure.figsize':(25,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[75]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category

# # Product ID

# In[76]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[84]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')
#nlargest(10) is same as head(10)


# # Conclusion
# *Married women age group 26-35 yrs from UP,  Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category*

# In[ ]:




