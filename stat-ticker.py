import collections, time
import btcchina

#long-only sma crossover

access_key = "e4a761b5-0cb6-4cfb-9e66-d05799fecc8d"
with open("secret_key") as f:
	secret_key = f.readlines()[0]


bc = btcchina.BTCChina(access_key,secret_key)

fast_deque = collections.deque(maxlen = 10)
slow_deque = collections.deque(maxlen = 50)

while True:
	md = bc.get_market_depth2(1)
	depth = md['market_depth']

	bid = depth['bid'][0]['price']
	ask = depth['ask'][0]['price']
	
	fast_deque.append(ask)
	slow_deque.append(ask)

	fast_sma = sum(fast_deque) / len(fast_deque)
	slow_sma = sum(slow_deque) / len(slow_deque)


	s = "{0} {1:.2f} {2:.2f} spread: {3:.2f} cross: {4:.2f}\n".format(time.strftime("%H:%M:%S", time.gmtime()), bid, ask, ask-bid, fast_sma - slow_sma)
	print s,

	time.sleep(1)
