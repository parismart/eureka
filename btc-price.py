import requests
import json
import os
import time
while True:
	t = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd').txt
	t = json.loads(t)
	price = int(t["bitcoin"]["usd"])

	os.system(f"notify-send -t 10000 \"El precio de BTC es {price}\"")
	time.sleep(60)
