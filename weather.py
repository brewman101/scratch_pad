key=input('Please provide an API Key?\n')



import requests


url = "https://sws-data.sws.bom.gov.au/api/v1/get-k-index"
headers = {'Content-Type': 'application/json; charset=UTF-8'}
requestBody = {
  'api_key': key,
  'options': { 'location': 'Australian region'}}

response = requests.post(url, headers=headers, json=requestBody)

if response.status_code == 200:
  responseBody = response.json()
  data = responseBody['data']
  print(data)
else:
  responseBody = response.json()
  errors = responseBody['errors']
  print(errors)