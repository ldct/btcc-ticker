import time
import btcchina

access_key = "e4a761b5-0cb6-4cfb-9e66-d05799fecc8d"
with open("secret_key") as f:
	secret_key = f.readlines()[0]

bc = btcchina.BTCChina(access_key,secret_key)

while True:
	command = raw_input('order: ').split(' ')
	order = command[0]
	price = float(command[1])

	if order == "b":
		print bc.buy(str(price), 0.001)
	elif order == "s":
		print bc.sell(str(price), 0.001)
	elif order == "p":
		print bc.buy(str(price), 0.001)
		print bc.sell(str(price + 0.01) , 0.001)
