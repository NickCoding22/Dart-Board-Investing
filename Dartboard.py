import random

# Universal and FINAL Variables
num_stocks = 22
starting_spot = 2
ending_spot = 7706
r = random.Random()

class Dartboard :
    stock_ticker_dictionary = {}
    stock_csv = ""
    stocks = []

    #
    def __init__ (self):
        self.generate_stocks()
        self.process_stocks()

    # Generates the stocks by going to [num_stocks] random lines
    # and adding that line into the array [stocks]; returns [stocks].
    def generate_stocks (self):
        for i in range(num_stocks):
            next_line_number = r.randint(starting_spot, ending_spot)
            print("Finding Stock #" + str(i + 1) + " at line " + str(next_line_number) + "...")
            next_stock = self.get_stock(next_line_number)
            self.stocks.append(next_stock)
            print("Found Stock #" + str(i + 1) + "!")
        return self.stocks

    # Opens the csv every time (maybe find a better way) and iterates
    # through the needed number of lines until line number [line_number]
    # is found and returned as a STRING.
    def get_stock (self, line_number):
        stock_csv = open("/Users/nickscomputer/Desktop/Summer Project 2023/nasdaq_screener_1684901667987.csv", "r")
        full_line = ""
        i = 2
        while i <= line_number:
            full_line = stock_csv.readline()
            i += 1
        stock_csv.close()
        return full_line


    # Considering the list [stocks] adds them to a dictionary. This
    # results in each one being associated with a dartboard score. 
    # No return.
    def process_stocks (self):
        for i in range(num_stocks):
            dart_score = i + 1
            if i == 20: 
                dart_score = 25
            elif i == 21:
                dart_score = 50
            self.stock_ticker_dictionary[dart_score] = self.stocks[i]
            print_output = "Stock " + str(dart_score) + ": " + self.stocks[i]
            print(print_output)

# Process to get random stocks and assign them to certain values

dartboard = Dartboard()
