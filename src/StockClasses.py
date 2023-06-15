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
        self.market_orders = [] # List of market order data
        for property_name, value in account:
            print(f"\"{property_name}\": {value}")

    # Takes in a dictionary of [stock_tickers] and [amounts] 
    # and generates the given order data. 
    # [market_orders] is then filled with the generated
    # market order data for each stock ticker and amount
    def generate_order_data (self, stock_tickers_and_amounts) :
        for stock_ticker in stock_tickers_and_amounts.keys():
            amount = stock_tickers_and_amounts[stock_ticker]
            print(amount)
            market_order_data = MarketOrderRequest(
                                            symbol = stock_ticker,
                                            notional = amount,
                                            side = OrderSide.BUY,
                                            time_in_force=TimeInForce.DAY
            )
            print(market_order_data)
            self.market_orders.append(market_order_data)
        print("Orders Successfully Generated")

    # Writes the give orders to a text file to keep track.
    def write_orders_to_file (self, orders) :
        return None

    # Using the local list of market_order_data, in [market_orders] 
    # the orders are placed
    def place_orders (self) :
        i = 1
        for market_order_data in self.market_orders:
            market_order = trading_client.submit_order(market_order_data)
            print("Order #" + str(i) + " has been submitted.")
            print(market_order)
            i += 1
        print("All orders have been placed.")