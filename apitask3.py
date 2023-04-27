#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests

n_records = int(input(f'no of records: '))
limit = int(input(f'limit: '))
sales_data = []

for offset in range(0, n_records, limit):
    url = f'https://globalmart-api.onrender.com/mentorskool/v1/sales?offset={offset}&limit={limit}'
    try:
        response = requests.get(url, headers={'access_token': 'fe66583bfe5185048c66571293e0d358'})
        response.raise_for_status()  # raises an exception for non-2xx response codes
        sales_data.extend(response.json()['data'])
        print(f'Retrieving data... {offset + limit} records obtained')
    except requests.exceptions.HTTPError as err:
        print(f'HTTP error occurred while fetching data: {err}')
        break
    except requests.exceptions.RequestException as err:
        print(f'Request error occurred while fetching data: {err}')
        break
    except IndexError as err:
        print(f'Index out of range error occurred: {err}')
        break

print(f'Data collection completed with {len(sales_data)} records obtained.')

# Accessing the nth element
n = int(input('accesss which index: '))
try:
    print(sales_data[n])
except IndexError as err:
    print(f'Index out of range error occurred: {err}')


# In[3]:


len(sales_data)


# In[4]:


import requests

n_records = int(input(f'no of records: '))
limit = int(input(f'limit: '))
sales_data = []

for offset in range(0, n_records, limit):
    url = f'https://globalmart-api.onrender.com/mentorskool/v1/sales?offset={offset}&limit={limit}'
    try:
        response = requests.get(url, headers={'access_token': 'fe66583bfe5185048c66571293e0d358'})
        response.raise_for_status()  # raises an exception for non-2xx response codes
        sales_data.extend(response.json()['data'])
        print(f'Retrieving data... {offset + limit} records obtained')
    except requests.exceptions.HTTPError as err:
        print(f'HTTP error occurred while fetching data: {err}')
        break
    except requests.exceptions.RequestException as err:
        print(f'Request error occurred while fetching data: {err}')
        break
    except IndexError as err:
        print(f'Index out of range error occurred: {err}')
        break

print(f'Data collection completed with {len(sales_data)} records obtained.')

# Accessing the nth element
#n = int(input('accesss which index: '))
#try:
 #   print(sales_data[n])
#except IndexError as err:
 #   print(f'Index out of range error occurred: {err}')


# In[5]:


len(sales_data)


# In[7]:


sales_data


# In[ ]:




