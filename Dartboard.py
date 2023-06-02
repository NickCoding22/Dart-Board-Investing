import random
import StockClasses

class DartboardInvestor :
    # Universal and FINAL Variables
    num_stocks = 22
    starting_spot = 2
    ending_spot = 7706
    stock_file_path = "./Dart-Board-Investing/nasdaq_screener_1684901667987.csv"
    stock_tester = StockClasses.StockValidator()
    r = random.Random() # True (sorta) randomness used in actual project
    # r = random.Random(456) # Seeded randomness used in testing

    # Generates and processes stocks
    def __init__ (self):
        self.stock_tickers = [] # List of stock tickers (index 0 is "" and the indexes correspond to positions on board)
        self.stocks = [] # List of stocks and info (indexing is same as stock_ticker_dictionary; index 0 is "")
        self.generate_stocks()
        self.process_stocks()

    # Generates the stocks by going to [num_stocks] random lines
    # and adding that line into the array [stocks]; returns [stocks].
    # Makes it so the first index of [stocks] is an empty string.
    def generate_stocks (self):
        self.stocks.append("")

        def get_next_line () :
            next_line_number = self.r.randint(self.starting_spot, self.ending_spot)
            print("Finding Stock #" + str(i + 1) + " at line " + str(next_line_number) + "...")
            return next_line_number

        for i in range(self.num_stocks):
            stock_valid = False
            while not stock_valid:
                next_line_number = get_next_line()
                next_stock = self.get_stock(next_line_number)
                while "^" in next_stock or "Warrant" in next_stock:
                    next_line_number = get_next_line()
                    next_stock = self.get_stock(next_line_number)
                stock_valid = self.stock_tester.validate_stock(next_stock[0:next_stock.index(",")])
            self.stocks.append(next_stock)
            print("Found Stock #" + str(i + 1) + "!")
        return self.stocks

    # Opens the csv every time (maybe find a better way) and iterates
    # through the needed number of lines until line number [line_number]
    # is found and returned as a STRING.
    def get_stock (self, line_number):
        stock_csv = open(self.stock_file_path, "r")
        full_line = ""
        i = 2
        while i < line_number:
            stock_csv.readline()
            i += 1
        full_line = stock_csv.readline()
        stock_csv.close()
        return full_line


    # Considering the list [stocks] adds them to a dictionary. This
    # results in each one being associated with a dartboard score. 
    # No return.
    def process_stocks (self):
        self.stock_tickers.append("")
        for i in range(self.num_stocks):
            dart_score = i + 1
            stock_info = self.stocks[dart_score]
            self.stock_tickers.append(stock_info[0:stock_info.index(",")])
            print_output = "Stock " + str(dart_score) + ": " + self.stock_tickers[dart_score]
            print(print_output)

# Process to get random stocks and assign them to certain values

stockValidator = StockClasses.StockValidator()
stockHandler = StockClasses.StockHandler()
dartboardInvestor = DartboardInvestor()
stockValidator.validate_stocks(dartboardInvestor.stock_tickers[1:])

# Testing StockHandler class 

STAA = {}
i = 1
while i < 5:
    amount = 25
    if i > 2:
        amount = 50
    if i > 3:
        amount = 75
    STAA[dartboardInvestor.stock_tickers[i]] = amount
    i += 1
stockHandler.generate_order_data(STAA) # Orders are properly generated at the varying amounts
stockHandler.place_orders() # Orders are properly placed
