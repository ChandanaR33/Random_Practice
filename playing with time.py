import time

print(time.tzname)

print(time.time())
#gives us two values, the timezone not accounting for daylight savings
#and the one accounting for it. 

#run the following command on the terminal to switch time zone
sudo timedatectl set-timezone UTC

#coinmarketpro is being called 

import time, requests, json
import datetime as dt 

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC&convert=USD'
headers = {'Accept':application/json, 'Accept-Encoding':'deflate, gzip', 'X-CMC_PRO_API_KEY':key}

r = requests.get(url, headers=headers)

if r.status_code == 200:
	response = json.loads(r.text)

print(response)

#python format for the datetime object that is returned is %Y-%m-%dT%H:%M:%S.%fZ. 
lastUpdated = response['data']['BTC']['quote']['USD']['last_updated']
timestamp = dt.datetime.strptime(lastUpdated, '%Y-%m-%dT%H:%M:%S..000Z')
print(timestamp)

lastUpdatedUnix = int(lastUpdated.strftime("%s"))

dateOnly = str(lastUpdatedDt.strftime('%Y-%m-%d'))

dateonlyUnix = dt.datetime.strptime(lastUpdated, "%s")

#getting yesterdays OHLCV data from Cryptocompare API

req = requests.get('https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD')
if req.content != '':
	response = request.content
	response = json.loads(response)
	print(response)

dayIndex = len(response['Data']) - 2

time = int(response['Data'][dayIndex]['time'])
priceHigh = float(response['Data'][dayIndex]['high'])
priceLow = float(response['Data'][dayIndex]['low'])
priceClose = float(response['Data'][dayIndex]['close'])
priceTime = float(response)['Data'][dayIndex]['open']

timestampDateOnly = dt.datetime.utcfromtimestamp(time).strftime('%d/%m/%Y')

#adding and subtracting time using timedelta
from datetime import timedelta

today = 1533781210

tomorrow = dt.datetime.utcfromtimestamp(today) + timedelta(days=1)
tomorrow = tomorrow.strftime('%d/%m/%Y')
