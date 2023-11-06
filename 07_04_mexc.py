from time import time
import pandas as pd
import ccxt
import json
from accounts import MEXC_KEYS_luch
import asyncio
import ccxt.async_support as ccxt_async # link against the asynchronous version of ccxt


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

order = {'symbol': 'DEGOUSDT',
         'type': 'limit',
         'side': 'buy',
         'amount': 7,
         'price': 1.5470 }



list_orders = [order]

my_order = mexc.create_order(symbol=order['symbol'], type=order['type'], side=order['side'], amount=order['amount'], price=order['price'])
# my_orders = mexc.create_orders(list_orders)



print(f'SYNC Прошло Времени: {round(time() - time_start, 4)}')