from time import time
import pandas as pd
import ccxt
import json
from accounts import BYBIT_KEYS, BINANCE_KEYS, GATEIO_KEYS, BINANCE_KEYS_luch
# import ccxt.async_support as ccxt # link against the asynchronous version of ccxt

pd.options.display.width= None # Отображение Таблицы на весь Экран
pd.options.display.max_columns= 20 # Макс Кол-во Отображаемых Колонок
pd.set_option('display.max_rows', 10) # Макс Кол-во Отображаемых Строк

# exchange = ccxt.binance(BINANCE_KEYS)
# # 7. Create LIMIT ORDER
# symbol = 'ETHUSDT'
# amount = 1
# price = 1900
# option_future = {'options': {'defaultType': 'future'}}
# option_sandboxMode = {'options': {'sandboxMode': True}}
# params = BINANCE_KEYS
# params['options'] = {'defaultType': 'future'}
# exchange = ccxt.binance(params)

# # Экземпляр для Работы на Фьючерсах
# exchange = ccxt.binance(BINANCE_KEYS_luch)
# exchange.options['defaultType'] = 'future' # 'spot', 'future', 'margin', 'delivery', 'option'
# # exchange.options['sandboxMode'] = True # виртуальная торговля
# balance = exchange.fetch_balance()
# balance_json = json.dumps(balance)
# print(balance_json)

# Экземпляр для Работы на Фьючерсах (НОВЫЙ СПОСОБ. прежний тоже работает)
# exchange = ccxt.binanceusdm(BINANCE_KEYS_luch)
# balance = exchange.fetch_balance()
# balance_json = json.dumps(balance)
# print(balance_json)

# exchange = ccxt.binance({'enableRateLimit': True})
# exchange.options['sandboxMode'] = True
# # exchange.set_sandbox_mode(True)
# balance = exchange.fetch_balance()
# balance_json = json.dumps(balance)
# print(balance_json)

# print('----- BYBIT EXCHANCE -----')
# exchange = ccxt.bybit(BYBIT_KEYS)
# # exchange.options['sandboxMode'] = True
# exchange.options['defaultType'] = 'future'
# balance = exchange.fetch_balance()
# balance_json = json.dumps(balance)
# # indexes = ['free', 'used', 'total', 'debt']
# # columns = [balance['free'], balance['used'], balance['total'], balance['debt']]
# # df = pd.DataFrame(columns, index=indexes)
# # print(df)
# print(balance_json)

# print('----- GATE.IO EXCHANCE -----')
# exchange = ccxt.gateio(GATEIO_KEYS)
# exchange.options['sandboxMode'] = True
# exchange.options['defaultType'] = 'future'
# balance = exchange.fetch_balance()
# balance_json = json.dumps(balance)
# indexes = ['free', 'used', 'total', 'debt']
# columns = [balance['free'], balance['used'], balance['total'], balance['debt']]
# df = pd.DataFrame(columns, index=indexes)
# print(df)
# print(balance_json)

# exchange.load_markets()
# symbol = 'BTC/USDT'
# amount = 1.2345678  # amount in base currency BTC
# price = 87654.321  # price in quote currency USDT
# formatted_amount = exchange.amount_to_precision(symbol, amount)
# formatted_price = exchange.price_to_precision(symbol, price)
# print(formatted_amount, formatted_price)

def process_format(exchange, name_exchange):
    time_start = time()
    exchange.load_markets() # ОБЯЗАТЕЛЬНО перед ПОСЛЕДУЮЩЕЙ РАБОТОЙ! (см мануал Loading Markets)
    formatted_amount = exchange.amount_to_precision(symbol, amount)
    formatted_price = exchange.price_to_precision(symbol, price)
    print(f'--------- {name_exchange} EXCHANCE | formatted values ---------')
    print(f'{formatted_amount} | {formatted_price}')
    print(f'Время выполнения: {round(time() - time_start, 3)}')


symbol = 'ETH/USDT'
amount = 100.23456789  # amount in base currency BTC
price = 1800.123456789  # price in quote currency USDT
print(f'Simbol: {symbol} | Amount: {amount} | Price: {price}')

exchanges = [ccxt.binance(), ccxt.gateio(), ccxt.bybit(), ccxt.mexc(), ccxt.huobi()]
names = ['BINANCE', 'GATE.IO', 'BYBIT', 'MEXC', 'HUOBI']

time_0 = time()
i = 0
for exchange in exchanges:
    process_format(exchange, names[i])
    i += 1
print(f'ОБЩЕЕ Время выполнения: {round(time() - time_0, 3)}')




