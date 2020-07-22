import alpaca_trade_api as tradeapi
import datetime
from config import *

class MeanReversionAlgo : 
    def __init__(self):
        self.key_id = API_KEY
        self.secret_key = API_SECRET
        self.base_url = 'https://paper-api.alpaca.markets'
        self.data_url = 'https://data.alpaca.markets'

        # The symbol we will be trading
        self.symbol = 'SPY'

        # How many seconds we will wait in between updating the streak values
        self.tick_size = 5
        self.tick_index = 0

        # The percentage of our buying power that we will allocate to a new position\
        # Needs to be updated with appropriate model
        self.base_bet = 10

        # These variables track the information about the current streak
        self.streak_count = 0
        self.streak_start = 0
        self.streak_increasing = True

        # When this variable is not None, we have an order open
        self.current_order = None

        # The closing price of the last aggregate we saw
        self.last_price = 0

        # used to use tick data as second aggs data (mot every tick, but sec)
        self.last_trade_time = datetime.datetime.utcnow()

        #instantiate REST API
        self.api = tradeapi.REST(self.key_id, self.secret_key, self.base_url)

        # Cancel any open orders so they don't interfere with this script
        self.api.cancel_all_orders()

        try:
            self.position = int(self.api.get_position(self.symbol).qty)
        except:
            # No position exists
            self.position = 0

        # Figure out how much money we have to work with, accounting for margin
        account_info = self.api.get_account()
        self.equity = float(account_info.equity)
        self.margin_multiplier = float(account_info.multiplier)
        total_buying_power = self.margin_multiplier * self.equity
        print(f'Initial total buying power = {total_buying_power}')

    def account_info(self):
        account = self.api.get_account()
        print(account)

if __name__ == '__main__':
    trader = MeanReversionAlgo()
    trader.account_info()