import time
import btcchina

bc = btcchina.BTCChina(access_key,secret_key)

while True:
	md = bc.get_market_depth2(1)
	depth = md['market_depth']
	s = "{0} {1:.2f} {2:.2f}\n".format(time.strftime("%H:%M:%S", time.gmtime()), depth['ask'][0]['price'], depth['bid'][0]['price'])
	print s,

	with open("ticker", 'a') as ticker:
		ticker.write(s)

	time.sleep(5)
