import alpaca_trade_api as tradeapi

#authentication and connection details
api_key = 'PKJA4FK19MW5RW239JOL'
api_secret = 'BGP9VmVwUPKnXY5vqpBdAUSZn6HHxe9JWNuTKhX/'
base_url = 'https://paper-api.alpaca.markets'

#instantiate REST API
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

#obtain account information
account = api.get_account()
print(account)