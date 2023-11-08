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
my_symbol = 'ETH/USDT'
print('----- MEXC EXCHANCE -----')

async def a_func_1(mexcA):
    await mexcA.fetch_balance()

async def a_func_2(mexcA):
    await mexcA.fetch_orders(my_symbol)

async def a_func_3(mexcA):
    await mexcA.fetch_order_book(my_symbol)

async def a_func_4(mexcA):
    await mexcA.fetch_ticker(symbol=my_symbol)

async def a_func():
    time_start = time()
    mexcA = ccxt_async.mexc(MEXC_KEYS_luch)
    await mexcA.load_markets()

    await a_func_1(mexcA)
    await a_func_2(mexcA)
    await a_func_3(mexcA)
    await a_func_4(mexcA)
    await mexcA.close()
    print(f'ASYNC Прошло Времени: {round(time() - time_start, 4)}')


time_start = time()
mexc = ccxt.mexc(MEXC_KEYS_luch)
markets = mexc.load_markets()
balance = mexc.fetch_balance()
orders = mexc.fetch_orders(my_symbol)
order_book = mexc.fetch_order_book(my_symbol)
mexc.fetch_ticker(symbol=my_symbol)
print(f'SYNC Прошло Времени: {round(time() - time_start, 4)}')


# asyncio.run(a_func())




