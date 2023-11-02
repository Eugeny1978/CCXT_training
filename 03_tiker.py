import time
import pandas as pd
import ccxt
import json
from accounts import BYBIT_KEYS, BINANCE_KEYS, GATEIO_KEYS, KEYS_01
import ccxt.async_support as ccxt_async # link against the asynchronous version of ccxt

symbol = 'ETHUSDT'

bybit = ccxt.bybit() # Публичный Запрос. Авторизация не Требуется
data = bybit.fetch_status() #
data_json = json.dumps(data)
print(data_json)

data = bybit.fetch_ticker(symbol) #
data_json = json.dumps(data)
print(data_json)