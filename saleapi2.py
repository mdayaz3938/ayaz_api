#!/usr/bin/env python
# coding: utf-8

# # Here goes my code

# In[28]:


import requests

#API URL & header
url = f'https://globalmart-api.onrender.com/mentorskool/v1/sales?offset=1&limit=100'
header = {'access_token': 'fe66583bfe5185048c66571293e0d358'}

#data from reqests
sales_data = []

print(f'retrieving data...')
sales_response = requests.get(url, headers=header)
if sales_response:
    sales_data = sales_response.json()['data']
    print(f'records obtained \n')
else :
    print(f'The response status is {sales_response.status_code}')

print(sales_data)


# # Aim: to retrieve 500 records

# In[38]:


import requests

# API URL & header & params

# given in website
offset = 1
limit = 100

# page & url
page = f'/mentorskool/v1/sales?offset={offset}&limit={limit}'
url = f'https://globalmart-api.onrender.com{page}'

# giving access_token in header 
header = {'access_token': 'fe66583bfe5185048c66571293e0d358'}

# data for reqests
n_records = 500

# intiliaze new list to append data from different pages 
sales_data = []

# running a loop till we get to the desired records
print(f'retrieving data...')
while offset <= n_records: 
    sales_response = requests.get(url, headers=header)
    if sales_response:
        sales_data.extend(sales_response.json()['data'])
        offset = offset + limit
        print(".")
    else :
        print(f'The response status is {sales_response.status_code}')
print(f'records obtained \n')


# lets check the data we obtained

# In[39]:


print(sales_data)
print(len(sales_data))

