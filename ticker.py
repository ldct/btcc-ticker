#!/usr/bin/env python

import time
import btcchina

access_key = "e4a761b5-0cb6-4cfb-9e66-d05799fecc8d"

with open("secret_key") as f:
	secret_key = f.readlines()[0]

bc = btcchina.BTCChina(access_key, secret_key)

while True:
	md = bc.get_market_depth2(1)
	depth = md['market_depth']
	s = "{0} {1:.2f} {2:.2f}\n".format(time.strftime("%d %b %Y %H:%M:%S", time.gmtime()), depth['bid'][0]['price'], depth['ask'][0]['price'])
	print s,

	with open("ticker_data", 'a') as ticker:
		ticker.write(s)

	time.sleep(1)
