import time
import pandas as pd
import ccxt
import json
from accounts import BYBIT_KEYS, BINANCE_KEYS, GATEIO_KEYS
import ccxt.async_support as ccxt_async # link against the asynchronous version of ccxt

pd.options.display.width= None # Отображение Таблицы на весь Экран
pd.options.display.max_columns= 20 # Макс Кол-во Отображаемых Колонок
pd.set_option('display.max_rows', 10) # Макс Кол-во Отображаемых Строк

def get_balance(exchange):
    balance = exchange.fetch_balance()
    balance_json = json.dumps(balance)
    indexes = ['free', 'used', 'total']
    columns = [balance['free'], balance['used'], balance['total']]
    df = pd.DataFrame(columns, index=indexes)
    df_compact = df.loc[:, (df != 0).any(axis=0)]
    df = df_compact.transpose()
    print('----- BINANCE EXCHANCE -----')
    print(df)
    return df

def get_last_prices(exchange, symbol):
    try:
        data = exchange.fetch_ticker(symbol)
        bid = data['bid']
        ask = data['ask']
        # data_json = json.dumps(data)
        # print(data_json)
    except Exception as error:
        print(error)
        bid, ask = 0, 0
    return {'bid': bid, 'ask': ask}

def is_ammount_enough(exchange, symbol, amount):
    min_size_usdt = 10
    ask_price = get_last_prices(exchange, symbol)['ask']
    if ask_price == None: ask_price = 0
    size_usdt = float(ask_price) * float(amount)
    print(f'symbol: {symbol} | amount: {amount} | price: {ask_price} | size_usdt: {round(size_usdt, 4)}')
    enough = True if size_usdt >= min_size_usdt else False
    return {'enough': enough, 'size_usdt': size_usdt}

def main():
    csv_file = 'csv/balance_binance.csv'

    binance = ccxt.binance(BINANCE_KEYS)
    df = get_balance(binance)
    df.to_csv(csv_file, index_label='Coin')

    df = pd.read_csv(csv_file, index_col='Coin')
    total_size_usdt = 0
    for coin, row in df.iterrows():
        if coin == 'USDT':
            continue
        symbol = f'{coin}USDT'
        amount = row['free']
        is_ammount = is_ammount_enough(binance, symbol, amount)
        total_size_usdt += is_ammount['size_usdt']
        if is_ammount['enough']:
            # params = {'timeInForce': 'PostOmly'}
            binance.create_market_sell_order(symbol=symbol, amount=amount) # , params=params
            print(f'Продажа по рынку: {symbol} | {amount}')
            time.sleep(1)

    print(f'\nИтого хвостов на сумуу USDT: {total_size_usdt}')
    new_balance = get_balance(binance)

# --- RUN --------------
main()