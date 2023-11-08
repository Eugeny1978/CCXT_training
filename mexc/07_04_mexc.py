from time import time
import pandas as pd
import ccxt
import json
from accounts import MEXC_KEYS_luch
import asyncio
import ccxt.async_support as ccxt_async # link against the asynchronous version of ccxt
import pprint


pd.options.display.width= None # Отображение Таблицы на весь Экран
pd.options.display.max_columns= 20 # Макс Кол-во Отображаемых Колонок
# pd.set_option('display.max_rows', 1000)
# pd.set_option('display.max_columns', 1000)

print('----- MEXC EXCHANCE -----')
my_symbol =  'ETH/USDT' # 'ETHUSDT'
time_start = time()
mexc = ccxt.mexc(MEXC_KEYS_luch)
markets = mexc.load_markets()

# order_book = mexc.fetch_order_book(my_symbol)
# order_book2 = mexc.fetch_l2_order_book(my_symbol)
# order_books = [order_book, order_book2]
#
# path_to_file = 'json/order_book.json'
# path_to_file_2 = 'json/order_book_2l.json'
# paths = [path_to_file, path_to_file_2]
# i = 0
# for ob in order_books:
#     try:
#         with open(paths[i], 'w') as file:
#             json.dump(ob, file, indent=4, sort_keys=True)
#     except Exception as error:
#         print(error)
#     i += 1

# print(mexc.symbols)
# print(mexc.spot2_public_get_market_api_default_symbols) # не отрабатывает
# default_symbols = mexc.fetch_markets()
# try:
#     with open('txt/symbols', 'a') as file:
#         for symb in default_symbols:
#             file.write(str(symb))
# except Exception as error:
#     print(error)

# interest = mexc.fetch_open_interest('MX/USDT')
# print(interest)
# print(mexc.fetch_l3_order_book('MX/USDT'))
# tik = mexc.fetch_ticker('MX/USDT')
# # tik = json.dumps(mexc.fetch_ticker('MX/USDT'))
# print(tik)
# print(tik['vwap']) # средневзвешенная цена за последние 24 часа

# candles = mexc.fetch_ohlcv('MX/USDT', '1h', limit=48)
# print(type(candles))
# print(candles)

# print(mexc.rateLimit)

# order = {'symbol': my_symbol,
#          'type': 'limit',
#          'side': 'buy',
#          'amount': 0.005,
#          'price': 1900 }

# order = {'symbol': 'MX/USDT',
#          'type': 'limit',
#          'side': 'buy',
#          'amount': 5,
#          'price': 2.743 }

# order = {'symbol': 'DEGOUSDT',
#
# list_orders = [order]
# my_order = mexc.create_order(symbol=order['symbol'], type=order['type'], side=order['side'], amount=order['amount'], price=order['price'])
# my_orders = mexc.create_orders(list_orders)


# response1 = mexc.fetch_ohlcv('ADA/USDT', '1h', limit= 1)
# response2 = mexc.fetch_ohlcv('ADA/USDT', '1h', limit= 1, params={'price':'index'})
# print(response1)
# print(response2)
# # Convenience methods
# mark_klines = mexc.fetch_mark_ohlcv('ADA/USDT', '1h', limit= 1)
# index_klines = mexc.fetch_index_ohlcv('ADA/USDT', '1h', limit= 1)
# print(mark_klines)
# print(index_klines)

# print(mexc.status)
# print(mexc.requiredCredentials) # что требуется для авторизации на данной бирже


# ВАРИАНТЫ АВТОРИЗАЦИИ
# # any time
# bitfinex = ccxt.bitfinex ()
# bitfinex.apiKey = 'YOUR_BFX_API_KEY'
# bitfinex.secret = 'YOUR_BFX_SECRET'
#
# # upon instantiation
# hitbtc = ccxt.hitbtc ({
#     'apiKey': 'YOUR_HITBTC_API_KEY',
#     'secret': 'YOUR_HITBTC_SECRET_KEY',
# })
#
# # from variable id
# exchange_id = 'binance'
# exchange_class = getattr(ccxt, exchange_id)
# exchange = exchange_class({
#     'apiKey': 'YOUR_API_KEY',
#     'secret': 'YOUR_SECRET',
# })

# print(mexc.fetch_accounts())
print(mexc.fetch_trading_fees())

print(f'SYNC Прошло Времени: {round(time() - time_start, 4)}')