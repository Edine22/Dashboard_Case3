#!/usr/bin/env python
# coding: utf-8

# # Case 3: Laadpaal Data

# ### Importeren packages

# In[10]:


#importeren van de packages
import pandas as pd
import streamlit as st
import requests
import plotly.express as px
import plotly as plt
import geopandas as gpd


# ### Importeren data

# In[2]:


#importeren van de data
df1 = pd.read_csv('laadpaaldata.csv')
df1.head()


# In[3]:


#Geen rijen worden verwijderd na deze functie, dit betekent dat deze dataset goede/complete informatie bevat.
df1.dropna()


# In[4]:


URL = 'https://api.openchargemap.io/v3/poi/?output=json&countrycode=NL&maxresults=100&compact=true&verbose=false&key=d72b2b71-ac69-4b31-8f6e-39e8481cda42'
response = requests.get(url=URL).json()
df2 = pd.DataFrame.from_dict(response)
df2.head()


# In[5]:


#in df2 worden veel rijen verwijderd na de dropna functie, in deze dataset mist veel data
df2.dropna()


# In[6]:


URL2 ='https://opendata.rdw.nl/resource/w4rt-e856.json'
response2 = requests.get(url=URL2).json()
df3 = pd.DataFrame.from_dict(response2)
df3.head()


# In[7]:


df3.columns


# ### Schrijven code 

# In[8]:


#kaart
st.map(data=df2, zoom=6, use_container_width=True)


# In[11]:


#Histogram van de laadtijd
fig = px.histogram(df1, x="ChargeTime")

fig.update_layout(
    title_text='Laadtijden per auto (t/m 12 uur lang)',
    xaxis_title_text='Laadtijd (in uren)',
    yaxis_title_text="Hoeveelheid auto's")

fig.add_annotation(x=0.9, y=0.9,
            text=df1["ChargeTime"].median(),
            showarrow=False,
            yshift=10,
            xref="paper",
            yref="paper",
            bordercolor="#ffffff",
            borderwidth=0.5,
            bgcolor="#293f95",
            opacity=0.8,
            font=dict(
            family="Courier New, monospace",
            size=16,
            color="#ffffff"
            ),
            )

fig.show()


# In[ ]:





# In[ ]:




