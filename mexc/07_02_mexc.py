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

print('----- MEXC EXCHANCE -----')

mexc = ccxt.mexc(MEXC_KEYS_luch)
mexc_markets = mexc.load_markets()

symbol = 'ETH/USDT'
etheur_1 = mexc.markets[symbol]
etheur_2 = mexc.market(symbol)
etheur_Id = mexc.market_id(symbol)
symbols_1 = mexc.symbols
symbols_2 = list(mexc.markets.keys())
currencies = mexc.currencies

print(dir(mexc))

# SWAP Symbols
# 'BTC/USDT:BTC'  // BTC/USDT inverse perpetual swap contract funded in BTC
# 'BTC/USDT:USDT' // BTC/USDT linear perpetual swap contract funded in USDT
# 'ETH/USDT:ETH'  // ETH/USDT inverse perpetual swap contract funded in ETH
# 'ETH/USDT:USDT' // ETH/USDT linear perpetual swap contract funded in USDT

# OPTION Symbols
# 'BTC/USDT:BTC-211225-60000-P'  // BTC/USDT put option contract strike price 60000 USDT settled in BTC (inverse) on 2021-12-25
# 'ETH/USDT:USDT-211225-40000-C' // BTC/USDT call option contract strike price 40000 USDT settled in USDT (linear, vanilla) on 2021-12-25
# 'ETH/USDT:ETH-210625-5000-P'   // ETH/USDT put option contract strike price 5000 USDT settled in ETH (inverse) on 2021-06-25
# 'ETH/USDT:USDT-210625-5000-C'  // ETH/USDT call option contract strike price 5000 USDT settled in USDT (linear, vanilla) on 2021-06-25


