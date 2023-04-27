#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests

n_records = int(input(f'no of records: '))
limit = int(input(f'limit: '))
sales_data = []

for offset in range(0, n_records, limit):
    url = f'https://globalmart-api.onrender.com/mentorskool/v1/sales?offset={offset}&limit={limit}'
    response = requests.get(url, headers={'access_token': 'fe66583bfe5185048c66571293e0d358'})
    if response.ok:
        sales_data.extend(response.json()['data'])
        print(f'Retrieving data... {offset + limit} records obtained')
    else:
        print(f'Error {response.status_code} occurred while fetching data')
        break

print(f'Data collection completed with {len(sales_data)} records obtained.')


# In[4]:


sales_data


# In[6]:


#creating sales_data to dataframe
import pandas as pd
data=pd.DataFrame(sales_data)
data


# In[7]:


import pandas as pd

# extracting data from orders and creating new columns req
data[['order_id', 'ship_mode','order_status','order_purchase_date','order_approved_at','order_delivered_carrier_date','order_delivered_customer_date','order_estimated_delivery_date']] = data['order'].apply(lambda x: pd.Series([x['order_id'],x['ship_mode'],x['order_status'],x['order_purchase_date'],x['order_approved_at'],x['order_delivered_carrier_date'],x['order_delivered_customer_date'],x['order_estimated_delivery_date']]))
data[['customer_id', 'customer_name','segment','contact_number','customer_address']] = data['order'].apply(lambda x: pd.Series([x['customer']['customer_id'],x['customer']['customer_name'], x['customer']['segment'],x['customer']['contact_number'],x['customer']['address']]))
data[['vendor_id', 'vendor_name']] = data['order'].apply(lambda x: pd.Series([x['vendor']['VendorID'], x['vendor']['Vendor Name']]))

data = data.drop(columns=['order'])
print(data)


# In[8]:


#extracting data from products column

data[['product_id','product_name','colors','category','sub_category','date_added','manufacturer','sizes','upc','weight', 'product_photos_qty']] = data['product'].apply(lambda x: pd.Series([x['product_id'],x['product_name'],x['colors'],x['category'],x['sub_category'],x['date_added'],x['manufacturer'],x['sizes'],x['upc'],x['weight'],x['product_photos_qty']]))

data = data.drop(columns=['product'])
print(data)


# In[9]:


data=pd.DataFrame(data)


# In[10]:


data


# In[11]:


data.columns


# In[12]:


#droping the unwanted columns and storing into new data frame

new_data = data.drop(columns=['ship_mode','order_approved_at','order_delivered_carrier_date','segment','contact_number', 'customer_address', 'vendor_name', 'product_name','sub_category', 'date_added', 'manufacturer', 'sizes', 'upc', 'weight',
       'product_photos_qty'])

new_data


# In[13]:


new_data.columns


# In[14]:


#changing the order of columns as required output

new_data1=new_data[['id','sales_amt','qty','discount','profit_amt','order_id','order_purchase_date','order_status','order_delivered_customer_date','order_estimated_delivery_date','product_id','colors','category','customer_id','customer_name','vendor_id']]


# In[15]:


new_data1


# In[16]:


#importing into csv file
new_data1.to_csv('output_api.csv', index=False)


# In[17]:


new_df = pd.read_csv('output_api.csv')
new_df


# In[18]:


new_df


# In[19]:


new_df.shape


# In[20]:


new_df.describe()


# In[21]:


new_df.isnull()


# In[22]:


new_df.isnull().sum()


# In[23]:


(new_df.isnull().sum()/new_df.shape[0])*100


# In[24]:


new_df.info()


# In[25]:


new_df.duplicated().sum()


# In[26]:


datq=new_df


# In[27]:


datq


# In[28]:


datq['customer_name']


# In[29]:


datq[['first_name', 'last_name']] = datq['customer_name'].str.split(' ', n=1, expand=True)

# print the modified dataframe
print(datq)


# In[30]:


dataq=pd.DataFrame(datq)

dataq


# In[31]:


dataq['first_name']


# In[32]:


count = sum([1 for name in dataq['first_name'] if name == 'Alan'])

# print the count
count


# In[33]:


co = ([name for name in dataq['first_name'] if name == 'Alan'])

# print the count
co


# In[34]:


dataq['order_purchase_date'] = pd.to_datetime(dataq['order_purchase_date'])

# get day of the order
dataq['order_day'] = dataq['order_purchase_date'].dt.day_name()

dataq


# In[35]:


# define a lambda function to label the days as 'weekday' or 'weekend'
label_func = lambda x: 'weekend' if x in ['Saturday', 'Sunday'] else 'weekday'

# apply the lambda function to the days_of_week column to derive a new column called day_label
dataq['day_label'] = (dataq['order_day'].apply(label_func))


print(dataq)


# In[36]:


count_weekend = sum([1 for name in dataq['day_label'] if name == 'weekend'])

# print the count
count_weekend


# In[37]:


# Group the data by day_label and calculate the total sales for each group
sales_by_day = dataq.groupby('day_label')['sales_amt'].sum()

# Compare the sales of weekends and weekdays
if sales_by_day['weekend'] > sales_by_day['weekday']:
    print("Weekends have the highest sales.")
else:
    print("Weekdays have the highest sales.")


# In[38]:


# Group the data by day_label and calculate the total sales for each group
sales_by_cat = dataq.groupby('category')['sales_amt'].sum()

sales_by_cat


# In[39]:


dataq


# In[50]:


#How many orders are late delivered to the customers?
late_orders = dataq[dataq['order_delivered_customer_date'] > dataq['order_estimated_delivery_date']]
num_late_orders = len(late_orders)
print(f"Number of late orders: {num_late_orders}")


# In[49]:


# Which vendors lead to the highest delay in deliveries?
late_orders = dataq[pd.to_datetime(dataq['order_delivered_customer_date']) > pd.to_datetime(dataq['order_estimated_delivery_date'])]
avg_delay_by_vendor = late_orders.groupby('vendor_id').apply(lambda x: (pd.to_datetime(x['order_delivered_customer_date']) - pd.to_datetime(x['order_estimated_delivery_date'])).mean())
avg_delay_by_vendor = avg_delay_by_vendor.reset_index()
avg_delay_by_vendor.columns = ['vendor_id', 'avg_delay']
avg_delay_by_vendor = avg_delay_by_vendor.sort_values('avg_delay', ascending=False)
print(avg_delay_by_vendor.head())


# In[43]:


# How many orders got canceled by the users?
canceled_orders = dataq[dataq['order_status'] == 'canceled']
num_canceled_orders = len(canceled_orders)
print(f"Number of canceled orders: {num_canceled_orders}")


# In[44]:


# Which category has the highest sales?
sales_by_category = dataq.groupby('category')['sales_amt'].sum()
sales_by_category = sales_by_category.reset_index()
sales_by_category = sales_by_category.sort_values('sales_amt', ascending=False)
print(sales_by_category.head())


# In[45]:


# In which month the sales was highest?
dataq['month'] = pd.DatetimeIndex(dataq['order_purchase_date']).month
sales_by_month = dataq.groupby('month')['sales_amt'].sum()
sales_by_month = sales_by_month.reset_index()
sales_by_month = sales_by_month.sort_values('sales_amt', ascending=False)
print(sales_by_month.head())


# In[48]:


# Sales are highest on weekends or weekdays?
sales_by_day = dataq.groupby('day_label')['sales_amt'].sum()
sales_by_day


# In[51]:


# Group the data by day_label and calculate the total sales for each group
sales_by_day = dataq.groupby('day_label')['sales_amt'].sum()

# Compare the sales of weekends and weekdays
if sales_by_day['weekend'] > sales_by_day['weekday']:
    print("Weekends have the highest sales.")
else:
    print("Weekdays have the highest sales.")


# In[ ]:




