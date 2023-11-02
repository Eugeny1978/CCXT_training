import time
import pandas as pd
import ccxt
import json
from accounts import BYBIT_KEYS, BINANCE_KEYS, GATEIO_KEYS, KEYS_01
import ccxt.async_support as ccxt_async # link against the asynchronous version of ccxt

pd.options.display.width= None # Отображение Таблицы на весь Экран
pd.options.display.max_columns= 20 # Макс Кол-во Отображаемых Колонок
# pd.set_option('display.max_rows', 1000)
# pd.set_option('display.max_columns', 1000)
# with pd.option_context('display.max_columns', None): # Для Отображения Всех Колонок
#     print(df)

print('----- BYBIT EXCHANCE -----')
bybit = ccxt.bybit(BYBIT_KEYS)
balance = bybit.fetch_balance()
balance_json = json.dumps(balance)
indexes = ['free', 'used', 'total', 'debt']
columns = [balance['free'], balance['used'], balance['total'], balance['debt']]
df = pd.DataFrame(columns, index=indexes)
print(df)

print('')
print('----- BINANCE EXCHANCE -----')
binance = ccxt.binance(BINANCE_KEYS)
balance = binance.fetch_balance()
balance_json = json.dumps(balance)
indexes = ['free', 'used', 'total']
columns = [balance['free'], balance['used'], balance['total']]
df = pd.DataFrame(columns, index=indexes)
df_compact = df.loc[:, (df != 0).any(axis=0)]
print(df_compact)

print('')
print('----- GATEIO EXCHANCE -----')
gateio = ccxt.gateio(GATEIO_KEYS)
balance = gateio.fetch_balance()
balance_json = json.dumps(balance)
indexes = ['free', 'used', 'total']
columns = [balance['free'], balance['used'], balance['total']]
df = pd.DataFrame(columns, index=indexes)
print(df)