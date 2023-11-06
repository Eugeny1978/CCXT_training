from time import time
import pandas as pd
import ccxt
import json
from accounts import MEXC_KEYS_luch
import ccxt.async_support as ccxt_async # link against the asynchronous version of ccxt


pd.options.display.width= None # Отображение Таблицы на весь Экран
pd.options.display.max_columns= 20 # Макс Кол-во Отображаемых Колонок
# pd.set_option('display.max_rows', 1000)
# pd.set_option('display.max_columns', 1000)


def balance_to_df(balance):
    indexes = ['free', 'used', 'total']
    columns = [balance['free'], balance['used'], balance['total']]
    return pd.DataFrame(columns, index=indexes)

def take_time():
    global time_start
    t = round(time() - time_start, 5)
    time_start = time()
    return t


print('----- MEXC EXCHANCE -----')

time0 = time()
time_start = time()

spot = ccxt.mexc(MEXC_KEYS_luch)
# spot.options['defaultType'] =  'spot'
print(f'Затрачено времени: Создание Экземляра spot: {take_time()}')

swap = ccxt.mexc(MEXC_KEYS_luch)
swap.options['defaultType'] =  'swap'
# spot.options['sandboxMode'] = True # не отрабатывает. Биржа не предоставляет возможности торговать через апи по демо счету
print(f'Затрачено времени: Создание Экземляра swap: {take_time()}')

spot.load_markets()
print(f'Затрачено времени: Загрузить Рынки spot: {take_time()}')

swap.load_markets()
print(f'Затрачено времени: Загрузить Рынки swap: {take_time()}')

spot_balance = spot.fetch_balance()
print('SPOT balance: ')
print(balance_to_df(spot_balance))
print(f'Затрачено времени: Баланс spot: {take_time()}')

swap_balance = swap.fetch_balance()
print('SWAP balance: ')
print(balance_to_df(swap_balance))
print(f'Затрачено времени: Баланс swap: {take_time()}')

print(f'\nОбщее время: {round(time() - time0, 4)}')













# data = exchange.load_markets()
# path_to_file = 'json/load_markets.json'
# try:
#     with open(path_to_file, 'w') as file:
#         json.dump(data, file, indent=4, sort_keys=True)
# except Exception as error:
#     print(error)

