import time
import pandas as pd
import ccxt
import json
from accounts import BYBIT_KEYS, BINANCE_KEYS, GATEIO_KEYS
import ccxt.async_support as ccxt_async # link against the asynchronous version of ccxt

pd.options.display.width= None # Отображение Таблицы на весь Экран
pd.options.display.max_columns= 20 # Макс Кол-во Отображаемых Колонок
pd.set_option('display.max_rows', 10) # Макс Кол-во Отображаемых Строк

exchange = ccxt.binance(BINANCE_KEYS)

# 7. Create LIMIT ORDER
symbol = 'ETHUSDT'
amount = 1
price = 1900
