import datetime
from time import sleep
from binance.client import Client
from secrets import KEY, SECRET

# initialize api
client = Client(KEY, SECRET)

# input symbols and quantity
symbol = 'BTCUSDT'
quantity = '0.05'

order = False

while not order:
    BTC = client.get_historical_klines(symbol=symbol, interval='1m', start_str="1 minute ago UTC")
    print(BTC)
    break
