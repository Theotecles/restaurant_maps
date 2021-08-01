import requests

api_key = 'BeltX-EOm4uNL3Ii3F5qkYCD2FOVeTSvld-FFLes6pSj2oW3FfdOA4sGxMgZlj7WDcMMHxjJctQiEiR7UAvvkuDkPQ61O0ib3Qzhyi17VQPsj-pXqoSvy5fkyMwFYXYx'

# USING THE YELP BUSINESS SEARCH API: https://www.yelp.com/developers/documentation/v3/business_search
# HEADERS CONTAIN THE API KEY
headers = {'Authorization': 'Bearer {}'.format(api_key), 'content-type': 'application/json'}
search_api_url = 'https://www.yelp.com/developers/documentation/v3/business_search'
params = {
    'term': 'restaurants',
    'location': 'Cincinnati, Ohio',
    'limit': 50
}

# MAKE THE GET CALL WITH A TIME OUT OF 5 SECONDS
response = requests.get(search_api_url, headers=headers, params=params, timeout=5)
print(response.url)
print(response.status_code)
print(response.headers)