import requests
import json
import time
data = requests.get('https://api.coingecko.com/api/v3/search/trending').text
parse = json.loads(data)
print(json.dumps(parse, indent=4, sort_keys=True))
#while True:
	#t = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/history?date=25-09-2021&localization=es').text
	#t = json.loads(t)
	#price = int(t["bitcoin"]["usd"])
	#print("El Historico de BTC es", price)
	#print(t)
	#time.sleep(5)
