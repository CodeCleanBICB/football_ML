#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to get tables and their names from a webpage
def get_tables_with_names(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    tables = soup.find_all('table')
    table_names = soup.find_all('caption')
    return tables, table_names

# Function to parse tables and save both first and second sheets as CSV files
def parse_tables(tables, table_names):
    data_frames = {}
    for i, (table, name) in enumerate(zip(tables, table_names)):
        # Get table name
        table_name = name.text.strip().replace(' ', '_')
        if i % 2 == 1:  
            table_name = f"{table_name}_versus" # Rename every other sheet 
        
        # Parse table
        df = pd.read_html(str(table))
        # Save only the second sheet of every table             
        data_frames[table_name] = df[0]
        df[0].to_csv(f"{table_name}.csv", index=False)
    return data_frames

# URL of the webpage
url = "https://fbref.com/en/comps/9/Premier-League-Stats#all_rank_key"

# Get tables and their names from the webpage
tables, table_names = get_tables_with_names(url)

# Parse tables and save both first and second sheets as CSV files
data_frames = parse_tables(tables, table_names)


# In[2]:


len(data_frames)


# In[3]:


data_frames["Regular_season_Table"]


# In[4]:


data_frames["Regular_season_Table_versus"]


# In[ ]:




