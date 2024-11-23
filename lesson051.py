# https://api.coinbase.com/v2/prices/buy?currency=USD
# In terminal run:
#       curl https://api.coinbase.com/v2/prices/buy?currency=USD

import requests

def inform_Mark(price):
    print(f"Hello there, the price of BTC ${price} is good now.")

my_good_price = 98_000

response = requests.get("https://api.coinbase.com/v2/prices/buy?currency=USD")
print(response)

price = float(response.json()['data']['amount'])
print(price)

if (price < my_good_price):
    inform_Mark(price)