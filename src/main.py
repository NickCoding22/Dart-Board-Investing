import StockClasses
import Dartboard
import GPIOHandler
import sys

# Setup the stockvalidator for one last check
# Setup the stockHandler to generate and place orders
# Setup the dartboard to create the association between scores and stocks
# Validate the stocks, last check
stockValidator = StockClasses.StockValidator()
stockHandler = StockClasses.StockHandler()
dartboardInvestor = Dartboard.DartboardInvestor()
stockValidator.validate_stocks(dartboardInvestor.stock_tickers[1:])

# Runs for a total of 10 inputs; generates the scores and the multipliers
print(sys.argv[1])
dollar_amount = int(sys.argv[1])
STAA = GPIOHandler.collect_scores()
STAA = dartboardInvestor.convert_to_stocks(STAA)
total_investment = 0
for score in list(STAA.keys()) :
    STAA[score] *= dollar_amount
    total_investment += STAA[score]

print("------------------------")
print(STAA)
print("Total: " + str(total_investment))
invest_y_n = input("Invest? y/n\n")

if invest_y_n == "y" :
    stockHandler.generate_order_data(STAA) # Orders are properly generated at the varying amounts
    stockHandler.place_orders() # Orders are properly placed
else :
    print("Program ended")
