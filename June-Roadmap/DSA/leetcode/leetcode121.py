#leetcode 121  Best time to buy and sell stock!

def stockProfit(prices):
    min_price = float("inf")
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
    return max_profit                

print(stockProfit([1, 3, 5, 7, 99, 34, 993]))			    
	
