import time
from mexc_api.spot import Spot
from mexc_api.websocket import SpotWebsocketStreamClient
from mexc_api.common.enums import Side, OrderType, StreamInterval, Action
from mexc_api.common.exceptions import MexcAPIError
from accounts import MEXC_KEYS_luch

# В списке через IDE не найти этой библиотеки
# pip install mexc-api

spot = Spot(MEXC_KEYS_luch['apiKey'], MEXC_KEYS_luch['secret'])
symbols = spot.market.default_symbols()
print(sorted(symbols))

# server_time = spot.market.server_time()
# print(server_time)
#
# # order_book = spot.market.order_book("MXUSDT")
# order_book = spot.market.order_book("ETHUSDT")
# print(order_book)
#
# order = spot.account.test_new_order(
#     "MXUSDT",
#     Side.BUY,
#     OrderType.LIMIT,
#     '1',
#     price='1'
# )
# ETHUSDT Через АПИ не Торгуется (вообще многие пары не торгуются
# order = spot.account.test_new_order(
#     "ETHUSDT",
#     Side.BUY,
#     OrderType.LIMIT,
#     '0.005',
#     price='1900'
# )
# print(order)
#
# ws = SpotWebsocketStreamClient(
#     KEY,
#     SECRET,
#     on_message=print
# )
# time.sleep(1)
# ws.klines("MXUSDT", StreamInterval.ONE_MIN)
# ws.account_orders()
#
# time.sleep(5)
# ws.account_orders(Action.UNSUBSCRIBE)
# ws.klines("MXUSDT", StreamInterval.ONE_MIN, Action.UNSUBSCRIBE)
# ws.stop()