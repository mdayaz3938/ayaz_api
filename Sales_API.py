import requests
#API URL
url = f'https://globalmart-api.onrender.com/mentorskool/v1/sales?offset=1&limit=100'

#data from reqests
sales_data = []

for i in range(n_requests):
    sales_response = requests.get(url, headers={'access_token': 'fe66583bfe5185048c66571293e0d358'})
    if sales_response:
        print(f'retrieving data...')
        sales_data = sales_response.json()
    else :
        print(f'The response status is {sales_response.status_code}')

print(f'data collection comepleted')
print(sales_data)