from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass, AssetStatus, AssetExchange

import API_Keys

API_KEY = API_Keys.API_Key_ID
SECRET_KEY = API_Keys.Secret_Key
trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)
account = trading_client.get_account()

class StockValidator:
    # Validates stocks as tradeable and fractionable, returning true if they are
    # and false if they are not.
    def validate_stocks (self, stock_tickers) :
        for stock_ticker in stock_tickers:
            if not self.validate_stock(stock_ticker):
                print("Stocks are not valid.")
                return False
        print("Stocks are valid.")
        return True
    
    # Same as above, but for individal stocks
    def validate_stock (self, stock_ticker) :
        asset = trading_client.get_asset(stock_ticker)
        if not asset.tradable:
            print(asset.symbol + " is not tradable :(")
            return False
        elif not asset.fractionable:
            print(asset.symbol + " is not fractional :(")
            return False
        else:
            print(asset.symbol + " is all good :)")
            return True

class StockHandler:

    # Prints the info with the universal [trading_client] and [account].
    def __init__ (self):
        for property_name, value in account:
            print(f"\"{property_name}\": {value}")

    # Takes in a list of stock tickers (stocks) and generates the given assets. 
    # Using stocks, a list of orders are created and returned.
    def generate_orders (self, stock_tickers, amounts) :
        return None

    # Writes the give orders to a text file to keep track.
    def write_orders_to_file (self, orders) :
        return None

    # Given a list of stocks with associated amounts and stock tickers, 
    # the orders are placed.
    def place_orders (self, stocks) :
        return None

# Setting parameters for our buy order
# market_order_data = MarketOrderRequest(
#                       symbol="BTC/USD",
#                       qty=1,
#                       side=OrderSide.BUY,
#                       time_in_force=TimeInForce.GTC
#                   )

# market_order = trading_client.submit_order(market_order_data)
# for property_name, value in market_order:
#   print(f"\"{property_name}\": {value}")