#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3 as sq
import pandas as pd


# In[5]:


conn = sq.connect('london_crime.db')


# In[6]:


df=pd.read_csv('D:/tableau/Uk crime/london_crime.csv')


# In[8]:


curs = conn.cursor()


# In[10]:


df.to_sql('London_crime', conn, if_exists='replace', index=False)


# In[11]:


pd.read_sql("""SELECT *
                        FROM london_crime
                        limit 10;""", conn)


# In[19]:


pd.read_sql("""SELECT type
                        FROM london_crime
                        limit 10;""", conn)


# In[ ]:




