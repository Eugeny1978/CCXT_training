import time
import pandas as pd
import ccxt
import json
from accounts import BYBIT_KEYS, BINANCE_KEYS, GATEIO_KEYS, KEYS_01
import ccxt.async_support as ccxt_async # link against the asynchronous version of ccxt

# Корректные Варианты
symbol = 'ETHUSDT'
symbol2 = 'ETH/USDT'
# Некорректные Варианты
symbol2 = 'ETH_USDT'
symbol3 = 'ethusdt'
symbol4 = 'ETH USDT'
symbol5 = 'ETH-USDT'
symbol6 = 'uETHUSDT'

# bybit = ccxt.bybit() # Публичный Запрос. Авторизация не Требуется
# Корректные символы: symbol = 'ETHUSDT', symbol2 = 'ETH/USDT'
# order_book = bybit.fetch_order_book(symbol, limit=1000) # , max limit=200, limit=25 - по умолчанию
# order_book_json = json.dumps(order_book)
# print(order_book_json)

# gateio = ccxt.gateio() # Публичный Запрос. Авторизация не Требуется
# # Корректные символы: symbol2 = 'ETH/USDT'
# order_book = gateio.fetch_order_book(symbol2) # , max limit=1000, limit=10 - по умолчанию
# order_book_json = json.dumps(order_book)
# print(order_book_json)

# binance = ccxt.binance() # Публичный Запрос. Авторизация не Требуется
# order_book = binance.fetch_order_book(symbol, limit=5000) # , max limit=5000,  limit=100 - по умолчанию
# order_book_json = json.dumps(order_book)
# print(order_book_json)