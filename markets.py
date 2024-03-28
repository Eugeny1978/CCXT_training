import time
import pandas as pd
import ccxt
import json
from accounts import BYBIT_KEYS, BITTIM_KEYS

div_line = '-' * 120
def jprint(data):
    print(json.dumps(data), div_line, sep='\n')

# print('----- BYBIT EXCHANCE -----')
# SYMBOL = 'ETH/USDT'
# connect = ccxt.bybit()
# markets = connect.load_markets()
# market_symbol = markets[SYMBOL]
#
# jprint(market_symbol)

# print('----- BITTEAM EXCHANCE -----')
SYMBOL = 'DUSD/USDT'
connect = ccxt.bitteam(BITTIM_KEYS)

# connect = ccxt.bitteam()
# markets = connect.load_markets()
# jprint(markets[SYMBOL])

# ledger = connect.fetch_ledger() # ccxt.base.errors.NotSupported: bitteam fetchLedger() is not supported yet
# jprint(ledger)
#
my_trades = connect.fetch_my_trades(SYMBOL) # нормально - Перевернул строну у мейкера как и должно быть
jprint(my_trades)


