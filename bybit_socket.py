import ccxt.pro as ccxtpro
import ccxt
from asyncio import run
from time import sleep



async def main():
    connect = ccxtpro.kraken({'newUpdates': False}) # ccxtpro.kraken({'newUpdates': False}) ccxt.bybit({'newUpdates': False})
    while True:
        orderbook = await connect.watch_order_book('ETH/USDT', limit=10)
        print(f"Best Ask: {orderbook['asks'][0]} | Best Bid: {orderbook['bids'][0]}")
        # connect.sleep(999)
        sleep(0.9)
    await connect.close()


run(main())