# load the stock_info module from yahoo_fin
from yahoo_fin import stock_info as si
import math

#function to run program again
def try_again():
  repeat = input("Do you want to try another stock? ")

  if repeat == "Yes" or repeat == "Y" or repeat == "yes" or repeat == "y" or repeat == "YES":
    main()

  elif repeat == "No" or repeat == "no" or repeat == "NO" or repeat == "N" or repeat == "n":
      print("Thank you for using the program!")
      quit()
  else:
    print("Invalid entry. Please try again")
    try_again()

#main function
def main():
  ticker = input("Please enter your stock ticker: ")
# get input's live quote price
  try: 
    ticker_price = si.get_live_price(ticker)
    #check for "nan" values. Unsupported tickers return nan. (Index, commodity, futures etc.)
    if math.isnan(ticker_price) == True:
      print("Sorry, that's an error.")
      print("Please use tickers for individual stocks, not indexes.")   
      main()
    #print value if key/value is present in yahoo_fin scrape
    else:
      print ("The current price for", ticker, " is ", round(ticker_price, 2))
      try_again()
  #catch misc. errors
  except: 
    print("Sorry, that's an error. Please try again.")
    print("You may use any ticker from the DOW, NASDAQ, or S&P500. Index and commodity tickers are not yet supported." ) 
    main()
  
  
#call main function
main()




  





  

