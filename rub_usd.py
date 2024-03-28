import requests
from time import sleep, time
from datetime import datetime

time_format ='%Y-%M-%d %H:%m:%S'

def get_rate_RUB_USD():
    url = 'https://api.tinkoff.ru/v1/currency_rates?from=USD&to=RUB'
    responce = requests.get(url).json()
    # print(responce)
    debit_cards_rate = responce['payload']['rates'][2]
    return debit_cards_rate

def get_rate_RUB_USD_full():
    url = 'https://api.tinkoff.ru/v1/currency_rates?from=USD&to=RUB'
    responce = requests.get(url).json()
    for category in responce['payload']['rates']:
        print(category['category'])


# for i in range(10):
#     rate = get_rate_RUB_USD()
#     print(f"Buy: {rate['buy']}| Sell: {rate['sell']} | {datetime.now().strftime(time_format)}")
#     sleep(5)


if __name__ == '__main__':
    print(get_rate_RUB_USD_full())