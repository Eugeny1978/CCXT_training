import time
import pandas as pd
import ccxt
import json
from accounts import BYBIT_KEYS, BINANCE_KEYS, GATEIO_KEYS, GATEIO_KEYS_TEST
import ccxt.async_support as ccxt_async # link against the asynchronous version of ccxt

pd.options.display.width= None # Отображение Таблицы на весь Экран
pd.options.display.max_columns= 20 # Макс Кол-во Отображаемых Колонок
# pd.set_option('display.max_rows', 1000)
# pd.set_option('display.max_columns', 1000)
# with pd.option_context('display.max_columns', None): # Для Отображения Всех Колонок
#     print(df)

print('')
print('----- GATEIO EXCHANCE -----')
exchange = ccxt.gateio(GATEIO_KEYS)
exchange.options['sandboxMode'] = True
# exchange.options['defaultType'] =  'future'  # 'future', 'swap'
balance = exchange.fetch_balance()
balance_json = json.dumps(balance)
indexes = ['free', 'used', 'total']
columns = [balance['free'], balance['used'], balance['total']]
df = pd.DataFrame(columns, index=indexes)
print(df)
