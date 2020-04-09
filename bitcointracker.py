
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'10',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '143d6305-aee8-44eb-96a0-0e6fc7da2a37',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  #print(data)
  for i in range(10):
  	name=data['data'][i]['name']
  	symbol=data['data'][i]['symbol']
  	print(str(i+1)+". "+name+" ("+symbol+")")
  	price=format(data['data'][i]['quote']['USD']['price'],'.4f')
  	print("Price: " +str(price)+ ' $')
  	pchg1hour=format((data['data'][i]['quote']['USD']['percent_change_1h'])*100,'.2f')
  	print("Percentage change in the last hour: "+str(pchg1hour)+"%")
  	pchg24hour=format((data['data'][i]['quote']['USD']['percent_change_24h'])*100,'.2f')
  	print("Percentage change in 24 hour: "+str(pchg24hour)+"%")
  	pchng7day=format((data['data'][i]['quote']['USD']['percent_change_7d'])*100,'.2f')
  	print("Percentage change in last 7 days: "+str(pchng7day)+"%")
  	print('')
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)