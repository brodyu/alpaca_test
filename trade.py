import alpaca_trade_api as tradeapi
from config import *

#authentication and connection details
BASE_URL = 'https://paper-api.alpaca.markets'

#instantiate REST API
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

#obtain account information
account = api.get_account()
print(account)