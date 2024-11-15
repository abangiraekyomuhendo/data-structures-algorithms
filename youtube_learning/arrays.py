#Store apple's stock price for 5 days and answer:
#1. What was the price on day 1?
#2. What was the price on day 3?

stock_prices = [298,305,320,301,292]
#stock_prices[0] #to retrieve the price for day one
#stock_prices[320] # this will retrieve price from day three

#on what day was the price 301?
#looking by value
#run a for loop to check 

def find_stock_price(stock_prices):
    for i in range(len(stock_prices)):
        if stock_prices[i]==301:
            return i
    return -1

result =  find_stock_price(stock_prices)
print("The index of 301 is: ", result)   
    
