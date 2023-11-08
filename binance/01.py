from time import time
import pandas as pd
import ccxt
import json
from accounts import BINANCE_TEST_SPOT_KEYS_luch, BINANCE_KEYS_luch, BINANCE_KEYS
import asyncio
import ccxt.async_support as ccxt_async # link against the asynchronous version of ccxt
import pprint

pd.options.display.width= None # Отображение Таблицы на весь Экран
pd.options.display.max_columns= 20 # Макс Кол-во Отображаемых Колонок
# pd.set_option('display.max_rows', 1000)
# pd.set_option('display.max_columns', 1000)

print('----- BINANCE TEST SPOT EXCHANCE -----')
# exchange = ccxt.binance(BINANCE_TEST_SPOT_KEYS_luch)
# exchange.set_sandbox_mode(True)
#
# balance = exchange.fetch_balance()
# print(exchange.status)
# balance_json = json.dumps(balance)
# indexes = ['free', 'used', 'total']
# columns = [balance['free'], balance['used'], balance['total']]
# df = pd.DataFrame(columns, index=indexes)
# df_compact = df.loc[:, (df != 0).any(axis=0)]
# print(df_compact)

# exchange = ccxt.binance(BINANCE_KEYS)
exchange = ccxt.binance(BINANCE_KEYS_luch)

def get_balance(exchange):
    try:
        balance = exchange.fetch_balance()
        indexes = ['free', 'used', 'total']
        columns = [balance['free'], balance['used'], balance['total']]
        df = pd.DataFrame(columns, index=indexes)
        df_compact = df.loc[:, (df != 0).any(axis=0)]
        print(df_compact)
        print(list(df_compact.columns))
        return df_compact
    except Exception as error:
        print(error.args)
        print(pd.DataFrame({'ERROR': error.args}))
        return pd.DataFrame()

balance = get_balance(exchange)





